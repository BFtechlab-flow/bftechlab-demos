# -*- coding: utf-8 -*-
"""Shared building blocks for the BF Tech Lab demo websites.

Each demo is a single static HTML file (Tailwind CDN + GSAP, no build step).
Site files in this folder describe content; this module turns it into pages.
"""
import json


def U(pid, w=900, h=None, q=75):
    """Unsplash image URL (hotlinked, as the Unsplash license allows)."""
    u = f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&q={q}"
    return u + (f"&h={h}" if h else "")


# ---------------------------------------------------------------- tokens
BOLD = dict(
    eyebrow="text-accent-600 font-semibold uppercase tracking-[.2em] text-xs",
    eyebrow_d="text-accent font-semibold uppercase tracking-[.2em] text-xs",
    h1="font-display font-bold uppercase leading-[.95] text-5xl sm:text-6xl lg:text-7xl",
    h2="font-display text-4xl sm:text-5xl font-bold uppercase leading-[1.02]",
    h3="font-display text-2xl font-bold uppercase leading-tight",
    btn="inline-flex items-center justify-center gap-2 rounded-md bg-accent hover:brightness-110 {ai} font-bold px-6 py-3.5 transition",
    btn_sm="rounded-md bg-accent hover:brightness-110 {ai} text-sm font-bold px-4 py-2.5 transition whitespace-nowrap",
    btn_dark="inline-flex items-center justify-center gap-2 rounded-md bg-night hover:bg-night-700 text-white font-bold px-6 py-3.5 transition",
    btn_line="inline-flex items-center justify-center gap-2 rounded-md border-2 border-ink font-bold px-6 py-3 transition hover:bg-ink hover:text-white",
    btn_line_d="inline-flex items-center justify-center gap-2 rounded-md border-2 border-white/30 hover:border-accent text-white font-bold px-6 py-3 transition",
    card="rounded-xl",
    img_r="rounded-xl",
    chip="rounded-md",
    input="rounded-lg border border-line bg-white px-3 py-3",
    pad="py-16 md:py-24",
    tab="rounded-md",
)
SOFT = dict(
    eyebrow="text-sm font-semibold text-brand uppercase tracking-wider",
    eyebrow_d="text-sm font-semibold text-accent uppercase tracking-wider",
    h1="font-display font-semibold leading-[1.05] text-4xl sm:text-5xl lg:text-6xl",
    h2="font-display text-3xl sm:text-4xl lg:text-[2.6rem] font-semibold leading-tight",
    h3="font-display text-xl font-semibold leading-snug",
    btn="inline-flex items-center justify-center gap-2 rounded-full bg-brand hover:bg-brand-700 text-white font-semibold px-6 py-3.5 transition",
    btn_sm="rounded-full bg-brand hover:bg-brand-700 text-white text-sm font-semibold px-5 py-2.5 transition whitespace-nowrap",
    btn_dark="inline-flex items-center justify-center gap-2 rounded-full bg-night hover:bg-night-700 text-white font-semibold px-6 py-3.5 transition",
    btn_line="inline-flex items-center justify-center gap-2 rounded-full border-2 border-ink/15 hover:border-brand font-semibold px-6 py-3 transition",
    btn_line_d="inline-flex items-center justify-center gap-2 rounded-full border-2 border-white/30 hover:border-white text-white font-semibold px-6 py-3 transition",
    card="rounded-2xl",
    img_r="rounded-3xl",
    chip="rounded-full",
    input="rounded-xl border border-line bg-white px-4 py-3",
    pad="py-16 md:py-24",
    tab="rounded-full",
)


def setup(S):
    """Resolve design tokens for a site config (mutates and returns S)."""
    base = BOLD if S.get("style") == "bold" else SOFT
    t = dict(base)
    t.update(S.get("tokens", {}))
    ai = S.get("accent_ink", "text-night")
    S["t"] = {k: v.replace("{ai}", ai) for k, v in t.items()}
    # an accent-coloured button, available on every site
    S["t"].setdefault("btn_accent", BOLD["btn"].replace("{ai}", ai).replace("rounded-md", S["t"]["tab"]))
    return S


def T(S, k):
    return S["t"][k]


CHECK = '<svg class="mt-0.5 shrink-0" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
PHONE_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
STARS = '<p class="text-[#f5a524] tracking-wider" aria-label="5 out of 5 stars">★★★★★</p>'


# ---------------------------------------------------------------- small parts
def section(sid, cls, inner, S=None, pad=None, wrap="max-w-6xl"):
    p = pad if pad is not None else (T(S, "pad") if S else "py-16 md:py-24")
    idattr = f' id="{sid}"' if sid else ""
    return f'<section{idattr} class="{cls} {p}">\n  <div class="{wrap} mx-auto px-4 sm:px-6">\n{inner}\n  </div>\n</section>\n'


def heading(S, eyebrow, title, lead=None, dark=False, center=False, maxw="max-w-2xl"):
    eb = T(S, "eyebrow_d") if dark else T(S, "eyebrow")
    lc = "text-white/70" if dark else "text-ink/70"
    c = " mx-auto text-center" if center else ""
    out = f'<div class="reveal {maxw}{c}">'
    if eyebrow:
        out += f'<p class="{eb}">{eyebrow}</p>'
    out += f'<h2 class="{T(S, "h2")} mt-2">{title}</h2>'
    if lead:
        out += f'<p class="mt-4 text-lg {lc}">{lead}</p>'
    return out + "</div>"


def checks(S, items, dark=False, cls="mt-6 space-y-3"):
    col = "text-accent" if dark else "text-brand"
    li = "".join(f'<li class="flex gap-3"><span class="{col}">{CHECK}</span><span>{x}</span></li>' for x in items)
    return f'<ul class="{cls}">{li}</ul>'


def stats(S, items, dark=False):
    bg = "bg-night text-white border-white/10" if dark else "bg-white border-line"
    sub = "text-white/60" if dark else "text-ink/60"
    cells = "".join(
        f'<div class="reveal"><p class="font-display text-3xl sm:text-4xl {"font-normal" if S.get("single_weight") else "font-bold"}">{a}</p><p class="mt-1 text-sm {sub}">{b}</p></div>'
        for a, b in items)
    return (f'<section class="{bg} border-y"><div class="max-w-6xl mx-auto px-4 sm:px-6 py-10 grid grid-cols-2 md:grid-cols-4 gap-8">'
            f'{cells}</div></section>\n')


def photo_cards(S, items, cols=3, dark=False, ratio="aspect-[16/10]", mt="mt-12"):
    grid = {2: "sm:grid-cols-2", 3: "sm:grid-cols-2 lg:grid-cols-3", 4: "sm:grid-cols-2 lg:grid-cols-4"}[cols]
    cb = "bg-night-800 border-white/10" if dark else "bg-white border-line"
    tc = "text-white/65" if dark else "text-ink/70"
    mc = "text-accent" if dark else "text-brand"
    out = []
    for it in items:
        meta = f'<p class="mt-auto pt-4 text-sm font-semibold {mc}">{it["meta"]}</p>' if it.get("meta") else ""
        pos = it.get("pos", "object-center")
        out.append(
            f'<article class="reveal group overflow-hidden {T(S, "card")} border {cb} hover:shadow-xl transition flex flex-col">'
            f'<div class="{ratio} overflow-hidden"><img src="{U(it["img"], 760)}" alt="{it.get("alt", "")}" loading="lazy" class="w-full h-full object-cover {pos} transition duration-500 group-hover:scale-105"></div>'
            f'<div class="p-6 flex-1 flex flex-col"><h3 class="{T(S, "h3")}">{it["title"]}</h3>'
            f'<p class="mt-2 text-sm {tc}">{it["text"]}</p>{meta}</div></article>')
    return f'<div class="{mt} grid {grid} gap-6">{"".join(out)}</div>'


def split(S, img, inner, reverse=False, ratio="aspect-[4/5]", pos="object-center", badge="", alt=""):
    pic = (f'<div class="reveal relative{" lg:order-2" if reverse else ""}">'
           f'<img src="{U(img, 1000)}" alt="{alt}" loading="lazy" class="w-full {ratio} object-cover {pos} {T(S, "img_r")} shadow-xl">{badge}</div>')
    txt = f'<div class="reveal">{inner}</div>'
    return f'<div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">{pic}{txt}</div>'


def text_block(S, eyebrow, title, paras, dark=False):
    eb = T(S, "eyebrow_d") if dark else T(S, "eyebrow")
    pc = "text-white/70" if dark else "text-ink/70"
    ps = "".join(f'<p class="mt-4 {pc}">{p}</p>' for p in paras)
    return f'<p class="{eb}">{eyebrow}</p><h2 class="{T(S, "h2")} mt-2">{title}</h2>{ps}'


def team(S, members, dark=False, ratio="aspect-[4/5]"):
    rc = "text-accent" if dark else "text-brand"
    bc = "text-white/65" if dark else "text-ink/70"
    cols = "md:grid-cols-3" if len(members) == 3 else "sm:grid-cols-2 lg:grid-cols-4" if len(members) == 4 else "md:grid-cols-2"
    out = []
    for m in members:
        img, name, role, bio = m[:4]
        pos = m[4] if len(m) > 4 else "object-top"
        out.append(
            f'<article class="reveal"><div class="{ratio} overflow-hidden {T(S, "img_r")} bg-line"><img src="{U(img, 640)}" alt="{name}" loading="lazy" class="w-full h-full object-cover {pos}"></div>'
            f'<h3 class="{T(S, "h3")} mt-5">{name}</h3><p class="text-sm font-semibold {rc} mt-1">{role}</p><p class="text-sm {bc} mt-3">{bio}</p></article>')
    return f'<div class="mt-12 grid {cols} gap-8">{"".join(out)}</div>'


def gallery(S, items):
    out = []
    for i, (img, cap) in enumerate(items):
        big = " md:col-span-2 md:row-span-2" if i == 0 else ""
        out.append(
            f'<figure class="reveal group relative overflow-hidden {T(S, "card")}{big}"><img src="{U(img, 900 if i == 0 else 600)}" alt="{cap}" loading="lazy" class="w-full h-full min-h-[180px] object-cover transition duration-700 group-hover:scale-105">'
            f'<figcaption class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/70 to-transparent text-white text-sm font-semibold p-4 pt-10">{cap}</figcaption></figure>')
    cols = "md:grid-cols-3" if len(items) % 3 == 0 else "md:grid-cols-4"
    return f'<div class="mt-12 grid grid-cols-2 {cols} auto-rows-[180px] md:auto-rows-[230px] gap-3">{"".join(out)}</div>'


def reviews(S, items, dark=False):
    cb = "border border-white/10 bg-night-800" if dark else "bg-white shadow-sm border border-line"
    qc = "text-white/85" if dark else "text-ink/80"
    fc = "text-white/50" if dark else "text-ink/55"
    figs = "".join(
        f'<figure class="reveal {T(S, "card")} {cb} p-6">{STARS}<blockquote class="mt-3 {qc}">"{q}"</blockquote>'
        f'<figcaption class="mt-4 text-xs {fc}">{who} · Sample review</figcaption></figure>' for q, who in items)
    note = f'<p class="mt-6 text-sm {fc}">Sample reviews for this demo. On your site, your real Google reviews appear here.</p>'
    return f'<div class="mt-10 grid md:grid-cols-3 gap-5">{figs}</div>{note}'


def steps(S, items, dark=False):
    nc = "text-accent" if dark else "text-brand"
    tc = "text-white/65" if dark else "text-ink/70"
    cb = "bg-night-800 border-white/10" if dark else "bg-white border-line"
    cols = "md:grid-cols-4" if len(items) == 4 else "md:grid-cols-3"
    cells = "".join(
        f'<div class="reveal {T(S, "card")} border {cb} p-6"><p class="font-display text-4xl {nc} {"font-normal" if S.get("single_weight") else "font-bold"}">{i:02d}</p>'
        f'<h3 class="{T(S, "h3")} mt-3">{a}</h3><p class="text-sm {tc} mt-2">{b}</p></div>'
        for i, (a, b) in enumerate(items, 1))
    return f'<div class="mt-12 grid sm:grid-cols-2 {cols} gap-5">{cells}</div>'


def cta_band(S, img, title, text, buttons, pos="object-center"):
    return (f'<section class="relative overflow-hidden bg-night text-white">'
            f'<img src="{U(img, 1800)}" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover {pos} opacity-40">'
            f'<div class="absolute inset-0 bg-gradient-to-r from-night via-night/85 to-night/40" aria-hidden="true"></div>'
            f'<div class="relative max-w-6xl mx-auto px-4 sm:px-6 py-16 md:py-20 grid md:grid-cols-3 gap-8 items-center">'
            f'<div class="reveal md:col-span-2"><h2 class="{T(S, "h2")}">{title}</h2><p class="mt-4 text-lg text-white/75 max-w-2xl">{text}</p></div>'
            f'<div class="reveal flex flex-wrap md:justify-end gap-3">{buttons}</div></div></section>\n')


def hours_table(S, rows, dark=False):
    dv = "divide-white/10" if dark else "divide-line"
    trs = "".join(f'<tr><th scope="row" class="py-2.5 text-left font-semibold">{a}</th><td class="py-2.5 text-right">{b}</td></tr>' for a, b in rows)
    return f'<table class="mt-6 w-full max-w-sm text-sm"><caption class="sr-only">Opening hours</caption><tbody class="divide-y {dv}">{trs}</tbody></table>'


def visit(S, img, eyebrow, title, note, hours, caption, buttons, pos="object-center"):
    addr = S["address"]
    q = addr.replace("<br>", " ").replace(" ", "+")
    inner = (
        f'<div class="grid md:grid-cols-2 gap-10 lg:gap-14">'
        f'<div class="reveal"><p class="{T(S, "eyebrow")}">{eyebrow}</p><h2 class="{T(S, "h2")} mt-2">{title}</h2>'
        f'<address class="not-italic mt-6 text-ink/80">{addr}</address><p class="mt-2 text-sm text-ink/60">{note}</p>'
        f'{hours_table(S, hours)}<div class="mt-8 flex flex-wrap gap-3">{buttons}</div></div>'
        f'<div class="reveal {T(S, "img_r")} overflow-hidden bg-line min-h-[340px] relative">'
        f'<img src="{U(img, 1100)}" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover {pos}">'
        f'<div class="absolute inset-0 bg-gradient-to-t from-black/65 via-transparent to-transparent" aria-hidden="true"></div>'
        f'<div class="absolute bottom-4 left-4 right-4 flex flex-wrap items-end justify-between gap-3 text-white">'
        f'<p class="font-display text-xl leading-tight max-w-xs">{caption}</p>'
        f'<a href="https://maps.google.com/?q={q}" class="{T(S, "chip")} bg-white text-ink px-4 py-2 text-sm font-semibold shadow">Get directions</a></div></div></div>')
    return section("visit", "bg-paper", inner, S)


def faq(S, items, eyebrow="FAQ", title="Questions we hear every day", bg="bg-white"):
    ic = "text-accent-600" if S.get("style") == "bold" else "text-brand"
    ds = "".join(
        f'<details class="reveal py-5"><summary class="flex cursor-pointer items-center justify-between gap-4 font-semibold">{q}'
        f'<span class="faq-icon text-2xl {ic} transition-transform" aria-hidden="true">+</span></summary><p class="mt-3 text-ink/70">{a}</p></details>'
        for q, a in items)
    inner = heading(S, eyebrow, title) + f'<div class="mt-10 divide-y divide-line border-y border-line">{ds}</div>'
    return section("faq", bg, inner, S, wrap="max-w-3xl")


# ---------------------------------------------------------------- forms
def inp(S, label, name, type="text", req=False, ph="", ac="", span=False, extra=""):
    r = " required" if req else ""
    a = f' autocomplete="{ac}"' if ac else ""
    p = f' placeholder="{ph}"' if ph else ""
    star = ' <span class="text-red-600" aria-hidden="true">*</span>' if req else ""
    sp = "sm:col-span-2 " if span else ""
    return (f'<label class="{sp}block text-sm font-semibold">{label}{star}'
            f'<input name="{name}" type="{type}"{r}{a}{p}{extra} class="mt-1.5 w-full {T(S, "input")} font-normal text-ink"></label>')


def area(S, label, name, ph="", span=True, rows=3):
    sp = "sm:col-span-2 " if span else ""
    return (f'<label class="{sp}block text-sm font-semibold">{label}'
            f'<textarea name="{name}" rows="{rows}" placeholder="{ph}" class="mt-1.5 w-full {T(S, "input")} font-normal text-ink"></textarea></label>')


def sel(S, label, name, options, req=False, span=False, first=None):
    r = " required" if req else ""
    sp = "sm:col-span-2 " if span else ""
    star = ' <span class="text-red-600" aria-hidden="true">*</span>' if req else ""
    opts = (f'<option value="">{first}</option>' if first else "") + "".join(
        f'<option value="{o[0]}">{o[1]}</option>' if isinstance(o, tuple) else f"<option>{o}</option>" for o in options)
    return (f'<label class="{sp}block text-sm font-semibold">{label}{star}'
            f'<select name="{name}"{r} class="mt-1.5 w-full {T(S, "input")} font-normal text-ink">{opts}</select></label>')


def chips(S, name, options, kind="radio", req=False, label=None, span=True, checked=None):
    r = " required" if (req and kind == "radio") else ""
    sp = "sm:col-span-2 " if span else ""
    opts = "".join(
        f'<label class="chip cursor-pointer"><input type="{kind}" name="{name}" value="{o}" class="sr-only"{r}{" checked" if o == checked else ""}>'
        f'<span class="inline-block {T(S, "chip")} border border-line bg-white text-ink px-4 py-2 text-sm font-medium transition hover:border-brand">{o}</span></label>'
        for o in options)
    lab = ""
    if label:
        star = ' <span class="text-red-600" aria-hidden="true">*</span>' if req else ""
        lab = f'<p class="text-sm font-semibold">{label}{star}</p>'
    return f'<fieldset class="{sp}block"><legend class="sr-only">{label or name}</legend>{lab}<div class="mt-2 flex flex-wrap gap-2">{opts}</div></fieldset>'


def consent(S, text="I agree to be contacted by phone, text or email about this request."):
    return (f'<label class="sm:col-span-2 flex items-start gap-3 text-sm"><input name="consent" type="checkbox" required '
            f'class="mt-1 w-4 h-4 shrink-0" style="accent-color:var(--brand)"> {text}</label>')


def demo_form(S, fid, fields, submit, ok_msg, cls="", note="Demo: on a live site this request goes straight to your phone and inbox.",
              err="Please fill in the required fields.", btn=None):
    b = btn or T(S, "btn")
    return (f'<form id="{fid}" data-demo class="grid sm:grid-cols-2 gap-4 {cls}" novalidate>{fields}'
            f'<p data-err hidden class="sm:col-span-2 text-sm font-semibold text-red-600" role="alert">{err}</p>'
            f'<div class="sm:col-span-2 flex flex-wrap items-center justify-between gap-3"><button class="{b}">{submit}</button>'
            f'<p class="text-xs opacity-60">{note}</p></div>'
            f'<p data-ok data-msg="{ok_msg}" hidden tabindex="-1" class="sm:col-span-2 {T(S, "card")} bg-brand-50 text-ink border border-brand/20 font-semibold p-4"></p></form>')


def multistep(S, fid, step_list, submit, done_title, done_msg, cls=""):
    n = len(step_list)
    sts = "".join(
        f'<div class="step"><h3 class="{T(S, "h3")}">{title}</h3><div class="mt-5 grid sm:grid-cols-2 gap-5">{inner}</div></div>'
        for title, inner in step_list)
    return f'''<form id="{fid}" data-steps class="{T(S, "card")} bg-white text-ink p-6 sm:p-8 shadow-2xl {cls}" novalidate>
  <div class="h-1.5 rounded-full bg-line overflow-hidden" aria-hidden="true"><div data-bar class="h-full bg-brand transition-all duration-500" style="width:0"></div></div>
  <p data-steplabel class="mt-3 text-xs font-semibold text-ink/60" aria-live="polite">Step 1 of {n}</p>
  <div class="mt-5">{sts}</div>
  <p data-err hidden class="mt-4 text-sm font-semibold text-red-600" role="alert">Please complete this step to continue.</p>
  <div data-done hidden tabindex="-1" data-msg="{done_msg}" class="text-center py-8">
    <div class="mx-auto w-14 h-14 rounded-full bg-brand text-white grid place-items-center"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></div>
    <h3 class="{T(S, "h3")} mt-5">{done_title}</h3><p data-done-msg class="mt-2 text-ink/70 max-w-md mx-auto"></p>
    <p class="mt-4 text-xs text-ink/50">Demo: on a live site this request goes straight to your phone and inbox.</p>
  </div>
  <div data-nav class="mt-8 flex items-center justify-between gap-3">
    <button type="button" data-back class="invisible {T(S, "chip")} px-5 py-3 text-sm font-semibold hover:bg-brand-50 transition">&larr; Back</button>
    <button type="button" data-next class="{T(S, "btn")}">Continue</button>
    <button type="submit" data-submit hidden class="{T(S, "btn")}">{submit}</button>
  </div>
</form>'''


def form_section(S, sid, eyebrow, title, lead, bullets, form_html, dark=True, after=""):
    bg = "bg-night text-white" if dark else "bg-brand-50"
    left = heading(S, eyebrow, title, lead, dark=dark) + checks(S, bullets, dark=dark) + after
    inner = f'<div class="grid lg:grid-cols-5 gap-10 lg:gap-14 items-start"><div class="lg:col-span-2">{left}</div><div class="reveal lg:col-span-3">{form_html}</div></div>'
    return section(sid, bg, inner, S)


def tabs(S, items, list_cls="", dark=False):
    """items: list of (key, label, panel_html)."""
    base = "border-white/20 text-white/80" if dark else "border-line bg-white"
    btns = "".join(
        f'<button type="button" role="tab" data-tab="{k}" aria-selected="false" class="tabbtn {T(S, "tab")} border {base} px-4 py-2 text-sm font-semibold transition whitespace-nowrap">{lab}</button>'
        for k, lab, _ in items)
    panels = "".join(f'<div data-panel="{k}" role="tabpanel">{p}</div>' for k, _, p in items)
    return (f'<div data-tabs><div class="flex gap-2 overflow-x-auto pb-2 -mx-1 px-1 {list_cls}" role="tablist">{btns}</div>'
            f'<div class="mt-8">{panels}</div></div>')


def price_list(S, items, cols=2):
    """items: (name, desc, price, tags)."""
    rows = []
    for it in items:
        name, desc, price = it[:3]
        tags = it[3] if len(it) > 3 else ""
        tg = "".join(f'<span class="ml-1.5 align-middle text-[10px] font-bold tracking-wider rounded border border-brand/30 text-brand px-1">{x}</span>' for x in tags.split()) if tags else ""
        d = f'<p class="mt-1 text-sm text-ink/60">{desc}</p>' if desc else ""
        rows.append(
            f'<div class="py-4 border-b border-line"><div class="flex items-baseline gap-3"><h4 class="font-semibold">{name}{tg}</h4>'
            f'<span class="flex-1 border-b border-dotted border-ink/25 -translate-y-1" aria-hidden="true"></span><span class="font-semibold whitespace-nowrap">{price}</span></div>'
            f'{d}</div>')
    gc = "md:grid-cols-2 gap-x-10" if cols == 2 else ""
    return f'<div class="grid {gc}">{"".join(rows)}</div>'


# ---------------------------------------------------------------- page chrome
def banner(S):
    cls = S.get("banner_cls", "bg-night text-white/90")
    return (f'<div class="{cls} text-center text-xs sm:text-sm px-4 py-2">Demo website by <strong>BF Tech Lab</strong> &mdash; '
            f'{S["name"]} is a fictional {S["kind"]} and the photos are stock images.</div>\n')


def header(S):
    dark = S.get("header") == "dark"
    hc = "bg-night text-white" if dark else "bg-paper/90 backdrop-blur border-b border-line text-ink"
    mark_bg = "bg-accent " + S.get("accent_ink", "text-night") if dark else "bg-brand text-white"
    shape = "rounded-lg" if S.get("style") == "bold" else "rounded-full"
    tag_c = "text-accent" if dark else "text-ink/50"
    first, rest = S["name"].split(" ", 1)
    if S.get("style") == "bold":
        name_html = (f'<span class="font-display text-xl sm:text-2xl font-bold tracking-wide uppercase leading-none">{S["name"]}'
                     f'<span class="block text-[10px] sm:text-[11px] font-semibold tracking-[.22em] {tag_c} mt-0.5">{S["tagline"]}</span></span>')
    else:
        wc = "text-accent" if dark else "text-brand"
        name_html = (f'<span class="font-display text-xl leading-none">{first} <span class="{wc}">{rest}</span>'
                     f'<span class="block font-sans text-[10px] font-semibold tracking-[.2em] uppercase {tag_c} mt-1">{S["tagline"]}</span></span>')
    nav = "".join(f'<a href="{h}" class="hover:opacity-70 transition">{l}</a>' for l, h in S["nav"])
    pc = "text-accent" if dark else "text-brand"
    cta_cls = T(S, "btn_sm") if S.get("style") == "bold" or not dark else T(S, "btn_sm").replace("bg-brand hover:bg-brand-700 text-white", f"bg-accent hover:brightness-105 {S.get('accent_ink', 'text-night')}")
    extra = S.get("header_extra", "")
    return f'''<header id="top" class="sticky top-0 z-40 {hc}">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-4">
    <a href="#top" class="flex items-center gap-2.5 shrink-0" aria-label="{S["name"]} home">
      <span class="grid place-items-center w-10 h-10 {shape} {mark_bg} font-display text-lg font-bold tracking-tight" aria-hidden="true">BF</span>
      {name_html}
    </a>
    <nav class="hidden lg:flex items-center gap-6 text-sm font-semibold whitespace-nowrap" aria-label="Main">{nav}</nav>
    <div class="flex items-center gap-2 sm:gap-3">{extra}
      <a href="tel:{S["tel"]}" class="hidden xl:inline text-sm font-semibold {pc}">{S["phone"]}</a>
      <a href="{S["cta"][1]}" class="{cta_cls}">{S["cta"][0]}</a>
    </div>
  </div>
</header>
'''


def hero_full(S, img, kicker, h1, sub, ctas, side="", points=None, pos="object-center", opacity="opacity-60", tall=False):
    pts = ""
    if points:
        pts = '<ul class="hero-in mt-8 flex flex-wrap gap-x-6 gap-y-2 text-sm text-white/80">' + "".join(
            f'<li class="flex items-center gap-2"><span class="text-accent">{CHECK}</span>{p}</li>' for p in points) + "</ul>"
    left_span = "lg:col-span-7" if side else "lg:col-span-9"
    side_html = f'<div class="hero-in lg:col-span-5">{side}</div>' if side else ""
    py = "pt-16 pb-20 md:pt-24 md:pb-28" if not tall else "pt-20 pb-24 md:pt-32 md:pb-40"
    return f'''<section class="relative bg-night text-white overflow-hidden">
  <img src="{U(img, 2000)}" alt="" class="absolute inset-0 w-full h-full object-cover {pos} {opacity}" fetchpriority="high">
  <div class="absolute inset-0 bg-gradient-to-r from-night via-night/80 to-night/25" aria-hidden="true"></div>
  <div class="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-night/60 to-transparent" aria-hidden="true"></div>
  <div class="relative max-w-6xl mx-auto px-4 sm:px-6 {py} grid lg:grid-cols-12 gap-10 items-center">
    <div class="{left_span}">
      <p class="hero-in {T(S, "eyebrow_d")}">{kicker}</p>
      <h1 class="hero-in {T(S, "h1")} mt-4">{h1}</h1>
      <p class="hero-in mt-6 text-lg text-white/80 max-w-xl">{sub}</p>
      <div class="hero-in mt-8 flex flex-wrap gap-3">{ctas}</div>
      {pts}
    </div>
    {side_html}
  </div>
</section>
'''


def hero_split(S, img, inset, chip, h1, sub, ctas, stat_items, card_title, card_text, pos="object-center", inset_pos="object-center"):
    dl = "".join(f'<div><dt class="text-xs text-ink/60">{a}</dt><dd class="font-display text-2xl mt-0.5">{b}</dd></div>' for a, b in stat_items)
    return f'''<section class="relative overflow-hidden">
  <div class="absolute inset-0 dots opacity-60" aria-hidden="true"></div>
  <div class="relative max-w-6xl mx-auto px-4 sm:px-6 pt-14 pb-24 md:pt-20 md:pb-28 grid md:grid-cols-2 gap-12 items-center">
    <div>
      <p class="hero-in inline-flex items-center gap-2 rounded-full bg-brand-100 text-brand-700 text-xs font-semibold px-3 py-1.5"><span class="w-2 h-2 rounded-full bg-brand"></span> {chip}</p>
      <h1 class="hero-in {T(S, "h1")} mt-5">{h1}</h1>
      <p class="hero-in mt-5 text-lg text-ink/75 max-w-lg">{sub}</p>
      <div class="hero-in mt-8 flex flex-wrap gap-3">{ctas}</div>
      <dl class="hero-in mt-10 grid grid-cols-3 gap-4 max-w-md">{dl}</dl>
    </div>
    <div class="hero-in relative">
      <div class="absolute -top-6 -right-6 w-44 h-44 rounded-full bg-accent/30 blur-2xl" aria-hidden="true"></div>
      <div class="relative">
        <img src="{U(img, 1100, 1300)}" alt="" fetchpriority="high" class="w-full aspect-[4/5] sm:aspect-square object-cover {pos} rounded-[2rem] shadow-2xl">
        <img src="{U(inset, 500, 500)}" alt="" class="hidden sm:block absolute -top-5 -right-5 w-36 h-36 object-cover {inset_pos} rounded-full border-[6px] border-paper shadow-xl">
        <div class="absolute left-4 right-4 -bottom-6 flex items-start gap-3 bg-paper text-ink {T(S, "card")} p-4 shadow-xl">
          <span class="mt-0.5 inline-flex w-9 h-9 shrink-0 items-center justify-center rounded-full bg-brand-100 text-brand-700" aria-hidden="true">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/></svg></span>
          <div><p class="font-semibold text-sm">{card_title}</p><p class="text-xs text-ink/60 mt-0.5">{card_text}</p></div>
        </div>
      </div>
    </div>
  </div>
</section>
'''


def footer(S):
    extra = S.get("footer_note", "")
    return f'''<footer class="bg-night text-white/70">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 py-12 grid sm:grid-cols-3 gap-8 text-sm">
    <div><p class="font-display text-2xl text-white">{S["name"]}</p><p class="mt-2">{S["address"]}</p></div>
    <div><p class="font-semibold text-white">Contact</p><p class="mt-2"><a href="tel:{S["tel"]}" class="hover:text-white">{S["phone"]}</a><br><a href="{S["cta"][1]}" class="hover:text-white">{S["cta"][0]}</a></p></div>
    <div><p class="font-semibold text-white">About this demo</p><p class="mt-2">Designed and built by BF Tech Lab, websites and automations for small businesses. The business, people, prices and reviews are fictional.</p></div>
  </div>
  {f'<p class="max-w-6xl mx-auto px-4 sm:px-6 pb-6 text-xs text-white/45">{extra}</p>' if extra else ""}
  <p class="text-center text-xs text-white/40 pb-24 md:pb-8">&copy; <span data-year>2026</span> {S["name"]} (demo) &middot; Stock photos from Unsplash</p>
</footer>
'''


def mobile_bar(S, label, href):
    return (f'<div class="md:hidden fixed bottom-0 inset-x-0 z-40 bg-night/95 backdrop-blur p-3 flex gap-2">'
            f'<a href="tel:{S["tel"]}" class="flex-1 text-center {T(S, "chip")} border border-white/25 text-white font-bold py-3 text-sm">Call</a>'
            f'<a href="{href}" class="flex-[2] text-center {T(S, "chip")} bg-accent {S.get("accent_ink", "text-night")} font-bold py-3 text-sm">{label}</a></div>\n')


COMMON_JS = r"""
document.documentElement.classList.add('js');
document.querySelectorAll('[data-year]').forEach(e => e.textContent = new Date().getFullYear());
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const money = n => '$' + Math.round(Number(n) || 0).toLocaleString('en-US');

/* dialogs */
document.addEventListener('click', e => {
  const o = e.target.closest('[data-open]');
  if (o) { const d = document.getElementById(o.dataset.open); if (d && d.showModal) d.showModal(); }
  const c = e.target.closest('[data-close]');
  if (c) { const d = c.closest('dialog'); if (d) d.close(); }
});
$$('dialog').forEach(d => d.addEventListener('click', e => { if (e.target === d) d.close(); }));

/* tabs */
$$('[data-tabs]').forEach(box => {
  const btns = $$('[data-tab]', box);
  const show = k => {
    btns.forEach(b => b.setAttribute('aria-selected', String(b.dataset.tab === k)));
    $$('[data-panel]', box).forEach(p => p.hidden = p.dataset.panel !== k);
  };
  btns.forEach(b => b.addEventListener('click', () => show(b.dataset.tab)));
  if (btns[0]) show(btns[0].dataset.tab);
});

/* min date = today */
$$('input[type=date]').forEach(i => { const d = new Date(); i.min = new Date(d - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); });

/* validation */
function validScope(scope) {
  let ok = true; const seen = new Set();
  $$('input,select,textarea', scope).forEach(el => {
    if (!el.required || el.closest('[hidden]')) return;
    if (el.type === 'radio') {
      if (seen.has(el.name)) return; seen.add(el.name);
      if (!scope.querySelector(`input[name="${el.name}"]:checked`)) ok = false;
    } else if (el.type === 'checkbox') { if (!el.checked) ok = false; }
    else if (!String(el.value).trim()) ok = false;
    else if (el.type === 'tel' && el.value.replace(/\D/g, '').length < 10) ok = false;
    else if (el.type === 'email' && !/^\S+@\S+\.\S+$/.test(el.value)) ok = false;
  });
  return ok;
}
function fillMsg(f, tpl) {
  return tpl.replace(/\{(\w+)\}/g, (m, k) => {
    const el = f.elements.namedItem(k); let v = el ? (el.value || '') : '';
    if (el && el.length !== undefined && !el.value && el[0] && el[0].type === 'checkbox') v = [...el].filter(x => x.checked).map(x => x.value).join(', ');
    v = String(v).trim();
    if (k === 'name') v = v.split(' ')[0];
    return v || (k === 'name' ? 'there' : '—');
  });
}
$$('form[data-demo]').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  const err = $('[data-err]', f), ok = $('[data-ok]', f), good = validScope(f);
  if (err) err.hidden = good;
  if (!good) return;
  ok.textContent = fillMsg(f, ok.dataset.msg); ok.hidden = false; ok.focus();
  f.querySelectorAll('input:not([type=checkbox]):not([type=radio]):not([type=date]),textarea').forEach(i => i.value = '');
}));
$$('form[data-steps]').forEach(f => {
  const steps = $$('.step', f); let i = 0;
  const bar = $('[data-bar]', f), lab = $('[data-steplabel]', f), back = $('[data-back]', f),
        next = $('[data-next]', f), sub = $('[data-submit]', f), err = $('[data-err]', f);
  function show(n) {
    i = n; steps.forEach((s, k) => s.classList.toggle('active', k === i));
    bar.style.width = ((i + 1) / steps.length * 100) + '%';
    lab.textContent = `Step ${i + 1} of ${steps.length}`;
    back.classList.toggle('invisible', i === 0);
    next.hidden = i === steps.length - 1; sub.hidden = i !== steps.length - 1; err.hidden = true;
  }
  next.addEventListener('click', () => { if (!validScope(steps[i])) { err.hidden = false; return; } show(i + 1); });
  back.addEventListener('click', () => show(i - 1));
  f.addEventListener('submit', e => {
    e.preventDefault();
    if (!validScope(steps[i])) { err.hidden = false; return; }
    const done = $('[data-done]', f);
    $('[data-done-msg]', done).textContent = fillMsg(f, done.dataset.msg);
    steps.forEach(s => s.classList.remove('active'));
    $('[data-nav]', f).hidden = true; err.hidden = true; bar.style.width = '100%'; lab.textContent = 'Request sent';
    done.hidden = false; done.focus();
  });
  show(0);
});
"""

ANIM_JS = r"""
(function () {
  const reveal = () => $$('.reveal').forEach(el => { el.style.opacity = 1; el.style.transform = 'none'; });
  try {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches || !window.gsap || !window.ScrollTrigger) return reveal();
    gsap.registerPlugin(ScrollTrigger);
    gsap.from('.hero-in', { y: 26, opacity: 0, duration: .75, ease: 'power3.out', stagger: .08 });
    $$('.reveal').forEach(el => gsap.to(el, { opacity: 1, y: 0, duration: .7, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 90%', once: true } }));
  } catch (e) { reveal(); }
})();
"""


def page(S, body, js=""):
    c = S["colors"]
    tw = {"theme": {"extend": {"colors": c, "fontFamily": {"display": S["font_display"], "sans": S["font_sans"]}}}}
    brand = c["brand"]["DEFAULT"]
    accent = c["accent"]["DEFAULT"]
    css_vars = (f"--brand:{brand};--brand-ink:{S.get('brand_ink_hex', '#ffffff')};--accent:{accent};"
                f"--paper:{c['paper']};--ink:{c['ink']};")
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{S["name"]} | Demo by BF Tech Lab</title>
<meta name="description" content="{S["description"]}">
<meta name="robots" content="noindex">
<meta property="og:title" content="{S["name"]} | Demo by BF Tech Lab">
<meta property="og:description" content="{S["description"]}">
<meta property="og:type" content="website">
<meta property="og:image" content="{U(S["og"], 1200, 630)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{S["fonts"]}&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config = {json.dumps(tw)};</script>
<style>
  :root {{ {css_vars} }}
  html {{ scroll-behavior: smooth; }}
  body {{ background: var(--paper); color: var(--ink); }}
  [hidden] {{ display: none !important; }}
  a[href^="tel:"] {{ white-space: nowrap; }}
  .js .reveal {{ opacity: 0; transform: translateY(22px); }}
  @media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} .js .reveal {{ opacity: 1 !important; transform: none !important; }} }}
  dialog::backdrop {{ background: rgba(10,10,10,.62); }}
  dialog {{ max-height: calc(100dvh - 2rem); }}
  details summary::-webkit-details-marker {{ display: none; }}
  details[open] .faq-icon {{ transform: rotate(45deg); }}
  input[type=range] {{ accent-color: var(--brand); }}
  .chip input:checked + span {{ background: var(--brand); color: var(--brand-ink); border-color: var(--brand); }}
  .chip input:focus-visible + span {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
  .step {{ display: none; }} .step.active {{ display: block; }}
  .tabbtn[aria-selected="true"] {{ background: var(--brand); color: var(--brand-ink); border-color: var(--brand); }}
  .dots {{ background-image: radial-gradient(color-mix(in srgb, var(--ink) 9%, transparent) 1px, transparent 1px); background-size: 14px 14px; }}
  {S.get("css", "")}
</style>
</head>
<body class="font-sans antialiased">
{banner(S)}{header(S)}<main>
{body}</main>
{footer(S)}{S.get("mobile", "")}
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
{COMMON_JS}
{js}
{ANIM_JS}
</script>
</body>
</html>
'''
