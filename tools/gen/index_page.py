# -*- coding: utf-8 -*-
"""Landing page listing every demo: python3 tools/gen/index_page.py"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

CATS = [("health", "Health"), ("home", "Home services"), ("food", "Food &amp; drink"), ("pro", "Professional"), ("auto", "Automotive"), ("beauty", "Beauty &amp; fitness")]
DEMOS = [
    ("dental/", "health", "Dental practice", "BF Dental", "3-step appointment requests, new patient guide, insurance and team.", "1777331903190-341a3dd0441b"),
    ("veterinary/", "health", "Veterinary clinic", "BF Animal Hospital", "Appointment requests by pet and reason, services, team, new client offer.", "1700665537650-1bf37979aae0"),
    ("chiropractic/", "health", "Chiropractic clinic", "BF Chiropractic", "Conditions treated, new patient special, online booking, insurance.", "1706353399656-210cca727a33"),
    ("med-spa/", "health", "Med spa", "BF Med Spa", "Treatments with prices, memberships, providers, free consultation booking.", "1570172619644-dfd03ed5d881"),
    ("plumbing/", "home", "Plumber", "BF Plumbing", "Same-day call-back form, upfront price guide, ZIP code checker, online booking.", "1676210133055-eab6ef033ce3"),
    ("roofing/", "home", "Roofing contractor", "BF Roofing", "Free inspection requests, roof cost estimator, project gallery.", "1635424709845-3a85ad5e1f5e"),
    ("landscaping/", "home", "Landscaping", "BF Landscapes", "Lawn care plan builder with live pricing, portfolio, quote requests.", "1597201278257-3687be27d954"),
    ("restaurant/", "food", "Restaurant", "BF Trattoria", "Menu with tabs, table reservations, private events, gallery.", "1774509625509-8c452b51649e"),
    ("law/", "pro", "Law firm", "BF Law Group", "Free case review, practice areas, results and attorney profiles.", "1479142506502-19b3a3b7ff33"),
    ("real-estate/", "pro", "Real estate agency", "BF Realty", "Listings with filters and detail views, home valuation, neighborhoods.", "1505843513577-22bb7d21e455"),
    ("dealer/", "auto", "Used car dealer", "BF Motors", "Searchable inventory, text about any car, payment estimator, dealer admin.", "1551830820-330a71b99659"),
    ("auto-repair/", "auto", "Auto repair shop", "BF Auto Care", "Service booking, coupons, live repair status, estimate requests.", "1615906655593-ad0386982a0f"),
    ("salon/", "beauty", "Hair salon", "BF Salon", "Price menu, stylist profiles, booking with stylist and time.", "1600948836101-f9ffda59d250"),
    ("fitness/", "beauty", "Gym &amp; fitness studio", "BF Fitness", "Class schedule with booking, membership plans, free trial sign-up.", "1778828494354-9b717d36dc99"),
]


def build():
    chips = '<button class="f on" data-f="all">All</button>' + "".join(f'<button class="f" data-f="{k}">{l}</button>' for k, l in CATS)
    cards = "".join(
        f'<a class="card" href="{href}" data-c="{cat}"><div class="ph"><img src="https://images.unsplash.com/photo-{img}?auto=format&fit=crop&w=800&h=500&q=70" alt="" loading="lazy"></div>'
        f'<div class="bd"><span class="tag">{tag}</span><h2>{name}</h2><p>{desc}</p><span class="go">Open demo &rarr;</span></div></a>'
        for href, cat, tag, name, desc, img in DEMOS)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BF Tech Lab | Website demos</title>
<meta name="description" content="Working website demos by BF Tech Lab for independent small businesses: dental, veterinary, chiropractic, med spa, plumbing, roofing, landscaping, restaurant, law, real estate, car dealer, auto repair, salon and fitness.">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{ --bg:#f6f4ef; --ink:#15171a; --muted:#5c6168; --card:#fff; --line:#e3e1db; --accent:#ee9a1a; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; font-family: Inter, system-ui, -apple-system, "Segoe UI", sans-serif; background:var(--bg); color:var(--ink); }}
  main {{ max-width: 1160px; margin: 0 auto; padding: 56px 16px 72px; }}
  .kick {{ font-size:12px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:#a86400; margin:0; }}
  h1 {{ font-size: clamp(32px, 5.5vw, 56px); line-height:1.02; letter-spacing:-.02em; margin: 10px 0 14px; max-width: 16ch; }}
  .lead {{ color: var(--muted); margin: 0 0 30px; font-size: 18px; max-width: 60ch; line-height:1.55; }}
  .filters {{ display:flex; gap:8px; flex-wrap:wrap; margin: 0 0 26px; }}
  .f {{ font: inherit; font-size:14px; font-weight:600; border:1px solid var(--line); background:#fff; color:var(--ink); border-radius:999px; padding:8px 16px; cursor:pointer; }}
  .f.on {{ background: var(--ink); color:#fff; border-color: var(--ink); }}
  .grid {{ display:grid; gap:20px; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }}
  a.card {{ display:flex; flex-direction:column; background:var(--card); border:1px solid var(--line); border-radius:18px; overflow:hidden; color:inherit; text-decoration:none; transition: border-color .2s, transform .2s, box-shadow .2s; }}
  a.card:hover {{ border-color: var(--accent); transform: translateY(-3px); box-shadow: 0 18px 40px -20px rgba(0,0,0,.35); }}
  .ph {{ aspect-ratio: 16/10; overflow:hidden; background:#e8e5de; }}
  .ph img {{ width:100%; height:100%; object-fit:cover; display:block; transition: transform .6s; }}
  a.card:hover .ph img {{ transform: scale(1.05); }}
  .bd {{ padding: 18px 20px 20px; display:flex; flex-direction:column; flex:1; }}
  .tag {{ font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#a86400; }}
  h2 {{ margin: 6px 0 6px; font-size: 21px; letter-spacing:-.01em; }}
  .bd p {{ margin:0 0 16px; color:var(--muted); font-size:14.5px; line-height:1.5; }}
  .go {{ margin-top:auto; font-weight:700; font-size:14px; }}
  .note {{ margin-top: 44px; padding: 22px 24px; background:#fff; border:1px solid var(--line); border-radius:18px; color:var(--muted); line-height:1.6; }}
  .note strong {{ color: var(--ink); }}
  footer {{ margin-top: 28px; color: var(--muted); font-size: 14px; }}
  footer a {{ color: inherit; }}
  [hidden] {{ display:none !important; }}
</style>
</head>
<body>
<main>
  <p class="kick">BF Tech Lab &middot; Website demos</p>
  <h1>Websites built for local businesses.</h1>
  <p class="lead">Working examples of the websites we build for independent small businesses. Every demo is one fast page that works on any phone, with a form or tool that brings in customers. The businesses shown are fictional and the photos are stock images.</p>
  <div class="filters" role="group" aria-label="Filter by industry">{chips}</div>
  <div class="grid" id="grid">{cards}</div>
  <p class="note"><strong>Like one of these?</strong> We adapt it to your business: your name, logo, photos, services, prices and colors, connected to your phone and email.</p>
  <footer>BF Tech Lab &middot; websites and automations for small businesses &middot; Via Teodoro Frizzoni 26, 24121 Bergamo, Italy &middot; <a href="mailto:bftechlabselling@gmail.com">bftechlabselling@gmail.com</a></footer>
</main>
<script>
  const btns = document.querySelectorAll('.f'), cards = document.querySelectorAll('a.card');
  btns.forEach(b => b.addEventListener('click', () => {{
    btns.forEach(x => x.classList.toggle('on', x === b));
    cards.forEach(c => c.hidden = b.dataset.f !== 'all' && c.dataset.c !== b.dataset.f);
  }}));
</script>
</body>
</html>
'''
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    readme = ["# BF Tech Lab — website demos", "",
              "Demo websites for prospective clients. The businesses, people, prices and reviews are fictional; photos are stock images from Unsplash.", "",
              "| Demo | Industry | Path |", "| --- | --- | --- |"]
    for href, cat, tag, name, desc, img in DEMOS:
        readme.append(f"| {name} | {tag.replace('&amp;', '&')} | `{href}` |")
    readme += ["", "Each demo is a single HTML file (Tailwind CDN + GSAP, no build step), published with GitHub Pages from the `main` branch.",
               "The newer demos are generated from `tools/gen` (`python3 tools/gen/build.py`, then `python3 tools/gen/index_page.py`).", ""]
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(readme))
    print("index + README written,", len(DEMOS), "demos")


if __name__ == "__main__":
    build()
