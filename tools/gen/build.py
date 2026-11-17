# -*- coding: utf-8 -*-
"""Build every demo site into the repo root: python3 tools/gen/build.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from lib import page  # noqa: E402

modules = []
for name in ("sites_a", "sites_b", "sites_c"):
    if os.path.exists(os.path.join(HERE, name + ".py")):
        modules.append(__import__(name))

only = set(sys.argv[1:])
built = []
for mod in modules:
    for fn in mod.SITES:
        S, body, js = fn()
        if only and S["slug"] not in only:
            continue
        out_dir = os.path.join(ROOT, S["slug"])
        os.makedirs(out_dir, exist_ok=True)
        html = page(S, body, js)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(html)
        built.append((S["slug"], len(html)))

for slug, n in built:
    print(f"{slug:14s} {n/1024:6.1f} KB")
