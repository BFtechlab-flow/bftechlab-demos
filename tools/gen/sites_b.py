# -*- coding: utf-8 -*-
"""Demo sites: law firm, real estate, fitness, hair salon."""
import json
from lib import *


# =====================================================================  LAW
def law():
    S = setup(dict(
        slug="law", name="BF Law Group", kind="law firm", style="soft", header="dark",
        tagline="Personal injury attorneys",
        description="Demo website for a personal injury law firm: free case review form, practice areas, sample results, attorney profiles. Built by BF Tech Lab.",
        og="1479142506502-19b3a3b7ff33",
        fonts="family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700",
        font_display=['"Playfair Display"', "Georgia", "serif"], font_sans=["Inter", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#13233d", "50": "#f1f4f8", "100": "#e3e8f0", "700": "#0b1729"},
                "accent": {"DEFAULT": "#c6a15b", "600": "#ab8641"},
                "night": {"DEFAULT": "#0e1828", "800": "#152238", "700": "#1e2f4a"},
                "ink": "#121a26", "paper": "#f7f5f0", "line": "#e3ddd0"},
        banner_cls="bg-accent text-night font-medium", accent_ink="text-night",
        phone="(555) 555-0180", tel="+15555550180",
        address="500 Court Street, Suite 300<br>Brookside, PA 00000",
        nav=[("Practice areas", "#practice"), ("Results", "#results"), ("Attorneys", "#attorneys"), ("FAQ", "#faq"), ("Contact", "#visit")],
        cta=("Free case review", "#review"),
        footer_note="Attorney advertising. This website is a demo and does not provide legal advice. Prior results do not guarantee a similar outcome.",
    ))
    t = S["t"]
    side = demo_form(S, "quickcase",
        f'<p class="sm:col-span-2 font-display text-2xl">Free case review</p><p class="sm:col-span-2 -mt-2 text-sm text-ink/60">Talk to an attorney today. 100% confidential.</p>' +
        sel(S, "What happened?", "case", ["Car accident", "Truck accident", "Motorcycle accident", "Slip and fall", "Work injury", "Other injury"], req=True, span=True, first="Choose...") +
        inp(S, "Name", "name", req=True, ac="name") + inp(S, "Phone", "phone", "tel", req=True, ac="tel"),
        "Get my free review", "Thank you, {name}. An attorney will call you within the hour about your {case} case.",
        cls="bg-paper text-ink rounded-2xl p-6 shadow-2xl", btn=t["btn"], note="No fee unless we win")
    hero = hero_full(S, "1479142506502-19b3a3b7ff33", "Personal injury &middot; Serving Brookside since 1996",
        'Hurt in an accident? <em class="text-accent">You pay nothing unless we win.</em>',
        "A free, confidential case review with an attorney, not a call center. We deal with the insurance companies so you can focus on getting better.",
        f'<a href="#review" class="{t["btn_accent"]}">Get a free case review</a><a href="tel:{S["tel"]}" class="{t["btn_line_d"]}">{PHONE_ICON} Call 24/7</a>',
        side=side, points=["No upfront costs", "Hospital &amp; home visits", "Se habla espa&ntilde;ol"], opacity="opacity-50")
    st = stats(S, [("$85M+", "Recovered for clients (sample)"), ("2,400+", "Cases handled"), ("$0", "Fees unless we win"), ("24/7", "Free consultations")], dark=True)
    areas = [("Car accidents", "Rear-end, intersection and hit-and-run crashes, including claims against your own insurer."),
             ("Truck accidents", "Commercial trucking cases with multiple insurers, driver logs and company records."),
             ("Motorcycle accidents", "Riders face bias from insurers. We fight for the full value of your claim."),
             ("Slip &amp; fall", "Injuries in stores, parking lots and rental properties caused by unsafe conditions."),
             ("Workplace injuries", "Workers' compensation plus third-party claims when someone else is responsible."),
             ("Wrongful death", "Compassionate help for families who lost a loved one through someone's negligence.")]
    cards = "".join(f'<a href="#review" class="reveal group block rounded-2xl border border-line bg-white p-7 hover:border-accent hover:shadow-xl transition">'
                    f'<p class="font-display text-3xl text-accent">{i:02d}</p><h3 class="{t["h3"]} mt-3">{a}</h3><p class="mt-2 text-sm text-ink/70">{b}</p>'
                    f'<p class="mt-5 text-sm font-semibold text-brand group-hover:text-accent-600">Free case review &rarr;</p></a>' for i, (a, b) in enumerate(areas, 1))
    practice = section("practice", "bg-paper", heading(S, "Practice areas", "If you were hurt, we can help") + f'<div class="mt-12 grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{cards}</div>', S)
    res = [("$2.1M", "Truck accident", "Spinal injury after a delivery truck ran a red light."), ("$1.3M", "Workplace fall", "Scaffold collapse at a construction site."),
           ("$850K", "Car accident", "Broken hip in an intersection crash, insurer first offered $40K."), ("$475K", "Slip &amp; fall", "Unmarked wet floor at a grocery store.")]
    rc = "".join(f'<div class="reveal rounded-2xl bg-night-800 border border-white/10 p-7"><p class="font-display text-5xl text-accent">{a}</p>'
                 f'<p class="mt-3 font-semibold text-white">{b}</p><p class="mt-1 text-sm text-white/65">{c}</p></div>' for a, b, c in res)
    results = section("results", "bg-night text-white", heading(S, "Recent results", "Real recoveries for real families", dark=True) +
                      f'<div class="mt-12 grid sm:grid-cols-2 lg:grid-cols-4 gap-5">{rc}</div><p class="mt-6 text-sm text-white/50">Sample results for this demo. Prior results do not guarantee a similar outcome.</p>', S)
    why = section("why", "bg-white", split(S, "1698047682091-782b1e5c6536",
        text_block(S, "Why BF Law Group", "You'll always talk to your attorney", [
            "Big advertising firms pass you to a case manager. Here, the attorney who takes your case returns your calls, answers your questions and stands next to you in court.",
            "We advance every cost of your case, from medical records to expert witnesses. If we don't win, you don't owe us anything."]) +
        checks(S, ["Direct cell number for your attorney", "We come to you: hospital, home or video call", "Spanish-speaking staff"]),
        reverse=True), S)
    attys = section("attorneys", "bg-paper", heading(S, "Our attorneys", "Three trial lawyers. One focus: injured people.") + team(S, [
        ("1560250097-0b93528c311a", "Robert Hale", "Founding partner", "30 years of trial experience and more than 200 jury verdicts. Former insurance defense lawyer who switched sides."),
        ("1573496359142-b8d87734a5a2", "Claire Donovan", "Partner", "Handles truck and workplace cases. Known for preparing every case as if it is going to trial."),
        ("1718209881007-c0ecdfc00f9d", "Marcus Reed", "Associate attorney", "Car, motorcycle and slip-and-fall cases. Grew up in Brookside and speaks Spanish."),
    ]), S)
    how = section("how", "bg-white", heading(S, "How it works", "What happens after you call") + steps(S, [
        ("Free review", "Tell us what happened. We'll tell you honestly if you have a case."),
        ("Investigation", "We gather police reports, photos, witnesses and medical records."),
        ("Treatment &amp; negotiation", "You focus on recovery while we deal with the insurers."),
        ("Settlement or trial", "Most cases settle. If they won't pay what's fair, we go to court."),
    ]), S)
    revs = section("reviews", "bg-paper", heading(S, "Client reviews", "What our clients say") + reviews(S, [
        ("Mr. Hale called me back himself the same evening. Two years later he got us more than five times the first offer.", "Sample client"),
        ("They visited me in the hospital and handled everything with the insurance. I never felt alone.", "Sample client"),
        ("Clear, honest and patient. They explained every step in Spanish to my parents.", "Sample client"),
    ]), S)
    form = multistep(S, "case-form", [
        ("What happened?", chips(S, "case", ["Car accident", "Truck accident", "Motorcycle", "Slip &amp; fall", "Work injury", "Other"], req=True)),
        ("A few details", chips(S, "when", ["Within 30 days", "1 to 6 months ago", "6 to 12 months ago", "Over a year ago"], req=True, label="When did it happen?") +
         chips(S, "doctor", ["Yes", "No", "Not yet"], req=True, label="Did you see a doctor?", span=False) +
         chips(S, "fault", ["No", "Partly", "Not sure"], label="Were you at fault?", span=False)),
        ("How can we reach you?", inp(S, "Name", "name", req=True, ac="name") + inp(S, "Phone", "phone", "tel", req=True, ac="tel") +
         inp(S, "Email", "email", "email", ac="email", span=True) + area(S, "Briefly, what happened? (optional)", "story") +
         consent(S, "I agree to be contacted about my case. Submitting this form does not create an attorney-client relationship.")),
    ], "Request free review", "We received your request", "Thank you, {name}. An attorney will call you within one hour during business hours. Everything you shared stays confidential.")
    review = form_section(S, "review", "Free case review", "Find out what your case is worth",
        "Three short questions. An attorney reviews every request personally and calls you back, usually within the hour.",
        ["100% free and confidential", "No fee unless we win your case", "Available 24/7, including weekends"], form,
        after=f'<p class="mt-8 text-white/70">Rather talk now? <a href="tel:{S["tel"]}" class="font-semibold text-accent">{S["phone"]}</a></p>')
    vis = visit(S, "1497366754035-f200968a6e72", "Contact", "Meet us downtown",
                "Free parking in the building garage. Can't come in? We'll come to you.",
                [("Monday &ndash; Friday", "8:30 am &ndash; 6:00 pm"), ("Saturday", "By appointment"), ("Phone consultations", "24/7")],
                "Home, hospital &amp; video consultations", f'<a href="tel:{S["tel"]}" class="{t["btn"]}">Call {S["phone"]}</a><a href="#review" class="{t["btn_line"]}">Free case review</a>')
    fq = faq(S, [
        ("How much does a lawyer cost?", "Nothing upfront. We work on a contingency fee: we're paid a percentage of what we recover, and only if we win."),
        ("Should I talk to the other driver's insurance company?", "It's best to talk to a lawyer first. Adjusters are trained to minimize your claim, and what you say can be used against you."),
        ("How long will my case take?", "Many cases settle in 6 to 18 months. Cases that go to trial can take longer. We'll give you an honest timeline."),
        ("What is my case worth?", "It depends on your injuries, medical bills, lost wages and how the accident happened. A free review gives you a realistic range."),
        ("Is there a deadline to file?", "Yes. Most states give you about two years from the date of the injury, sometimes less. Don't wait to get advice."),
    ], bg="bg-white")
    S["mobile"] = mobile_bar(S, "Free case review", "#review")
    body = hero + st + practice + results + why + attys + how + revs + review + vis + fq
    return S, body, ""


# =====================================================================  REAL ESTATE
def realestate():
    S = setup(dict(
        slug="real-estate", name="BF Realty", kind="real estate agency", style="soft", header="light",
        tagline="Homes in Brookside &amp; the valley",
        description="Demo website for a local real estate agency: searchable listings with filters and detail views, home valuation requests, neighborhood guides. Built by BF Tech Lab.",
        og="1505843513577-22bb7d21e455",
        fonts="family=Marcellus&family=Jost:wght@400;500;600;700",
        font_display=["Marcellus", "Georgia", "serif"], font_sans=["Jost", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#2a2724", "50": "#f6f3ee", "100": "#ece7df", "700": "#151311"},
                "accent": {"DEFAULT": "#b8925a", "600": "#9c7843"},
                "night": {"DEFAULT": "#1b1a19", "800": "#252321", "700": "#33302d"},
                "ink": "#1b1a19", "paper": "#faf8f5", "line": "#e8e1d6"},
        tokens=dict(h1="font-display font-normal leading-[1.05] text-5xl sm:text-6xl lg:text-7xl",
                    h2="font-display text-4xl sm:text-5xl font-normal leading-[1.08]",
                    h3="font-display text-xl font-normal leading-snug"),
        single_weight=True, banner_cls="bg-night text-white/90", accent_ink="text-night",
        phone="(555) 555-0190", tel="+15555550190",
        address="10 Market Square<br>Brookside, PA 00000",
        nav=[("Listings", "#listings"), ("Sell", "#value"), ("Neighborhoods", "#areas"), ("About", "#about"), ("Contact", "#visit")],
        cta=("Home value", "#value"),
    ))
    t = S["t"]
    search = (f'<form id="hsearch" class="hero-in mt-10 bg-white text-ink rounded-2xl p-2 grid sm:grid-cols-[1fr_1fr_1fr_auto] gap-2 max-w-3xl shadow-2xl" role="search">'
              f'<select name="area" class="rounded-xl bg-brand-50 px-3 py-3 font-medium"><option value="">Any area</option><option>Brookside</option><option>Oak Ridge</option><option>Cedar Falls</option><option>Riverton</option><option>Fairview</option><option>Hillcrest</option></select>'
              f'<select name="type" class="rounded-xl bg-brand-50 px-3 py-3 font-medium"><option value="">Any type</option><option>House</option><option>Townhome</option></select>'
              f'<select name="max" class="rounded-xl bg-brand-50 px-3 py-3 font-medium"><option value="">Any price</option><option value="400000">Up to $400k</option><option value="600000">Up to $600k</option><option value="800000">Up to $800k</option><option value="1000000">Up to $1M</option></select>'
              f'<button class="rounded-xl bg-accent text-night font-semibold px-6 py-3">Search</button></form>')
    hero = (f'<section class="relative bg-night text-white overflow-hidden"><img src="{U("1505843513577-22bb7d21e455", 2000)}" alt="" class="absolute inset-0 w-full h-full object-cover opacity-75" fetchpriority="high">'
            f'<div class="absolute inset-0 bg-gradient-to-t from-night via-night/40 to-night/10" aria-hidden="true"></div>'
            f'<div class="relative max-w-6xl mx-auto px-4 sm:px-6 pt-28 pb-16 md:pt-44 md:pb-24"><p class="hero-in {t["eyebrow_d"]}">BF Realty &middot; Brookside &amp; the valley</p>'
            f'<h1 class="hero-in {t["h1"]} mt-4 max-w-3xl">Find the home that fits the life you want.</h1>'
            f'<p class="hero-in mt-5 text-lg text-white/85 max-w-xl">Local agents, honest advice and homes you won\'t see everywhere else. Search below, or ask what your home is worth.</p>{search}</div></section>\n')
    listings = [
        dict(id="l1", img="1531971589569-0d9370cbe1e5", img2="1564078516393-cf04bd966897", price=1249000, addr="18 Ridgeview Court", area="Oak Ridge", type="House", beds=4, baths=3.5, sqft=3850, status="New", desc="Modern home with walls of glass, a heated pool and an open kitchen made for entertaining. Three-car garage and smart-home lighting."),
        dict(id="l2", img="1584738766473-61c083514bf4", img2="1763827513396-5917fc6c84f3", price=689000, addr="402 Maple Avenue", area="Brookside", type="House", beds=4, baths=3, sqft=2940, status="Open house Sat 1&ndash;3", desc="Classic farmhouse with a wraparound porch on a quiet, tree-lined street. Renovated kitchen, original wood floors, walk to downtown."),
        dict(id="l3", img="1592595896616-c37162298647", img2="1773578978637-c9771e7a9913", price=529000, addr="77 Willow Bend", area="Cedar Falls", type="House", beds=3, baths=2, sqft=2150, status="For sale", desc="Single-level living with a bright great room, gas fireplace and a fenced backyard. New roof in 2023."),
        dict(id="l4", img="1786051385612-5fac26efaf88", img2="1771372125074-5c7c4332095f", price=975000, addr="9 Lakeshore Drive", area="Riverton", type="House", beds=5, baths=4, sqft=4200, status="For sale", desc="Colonial with an in-ground pool, finished basement and a chef's kitchen. Five bedrooms, including a first-floor suite."),
        dict(id="l5", img="1564013799919-ab600027ffc6", img2="1763827513396-5917fc6c84f3", price=845000, addr="1450 Harbor Lane", area="Riverton", type="House", beds=4, baths=3.5, sqft=3400, status="Price reduced", desc="Two-story home with balconies, a resort-style pool and a covered outdoor kitchen. Minutes from the riverfront trail."),
        dict(id="l6", img="1625603736199-775425d2890a", img2="1773578978637-c9771e7a9913", price=459000, addr="25 Orchard Street", area="Brookside", type="House", beds=3, baths=2, sqft=1780, status="Pending", desc="Charming gambrel-roof home with a front porch, updated baths and a detached workshop."),
        dict(id="l7", img="1771366260867-7e07094579d7", img2="1564078516393-cf04bd966897", price=612000, addr="6 Cypress Walk", area="Oak Ridge", type="Townhome", beds=3, baths=2.5, sqft=2050, status="New", desc="End-unit townhome with high ceilings, a private courtyard and an attached two-car garage. Low HOA fees."),
        dict(id="l8", img="1605146769289-440113cc3d00", img2="1771372125074-5c7c4332095f", price=349000, addr="310 Elm Street", area="Fairview", type="House", beds=3, baths=2, sqft=1420, status="For sale", desc="Move-in ready starter home with an attached garage, new flooring and a level backyard."),
        dict(id="l9", img="1536745511564-a5fa6e596e7b", img2="1763827513396-5917fc6c84f3", price=739000, addr="52 Summit Road", area="Hillcrest", type="House", beds=4, baths=3, sqft=3100, status="Sold", desc="Hillside home with a pool and stone patio surrounded by mature trees. Sold in 6 days, 4% over asking."),
    ]
    fl = (f'<div class="reveal mt-10 grid grid-cols-2 md:grid-cols-4 gap-3 bg-white {t["card"]} border border-line p-3" role="group" aria-label="Filter listings">'
          f'<label class="text-xs font-semibold text-ink/60">Area<select id="f-area" class="mt-1 w-full rounded-xl bg-brand-50 px-3 py-2.5 text-sm font-medium text-ink"><option value="">All areas</option><option>Brookside</option><option>Oak Ridge</option><option>Cedar Falls</option><option>Riverton</option><option>Fairview</option><option>Hillcrest</option></select></label>'
          f'<label class="text-xs font-semibold text-ink/60">Bedrooms<select id="f-beds" class="mt-1 w-full rounded-xl bg-brand-50 px-3 py-2.5 text-sm font-medium text-ink"><option value="0">Any</option><option value="3">3+</option><option value="4">4+</option><option value="5">5+</option></select></label>'
          f'<label class="text-xs font-semibold text-ink/60">Max price<select id="f-max" class="mt-1 w-full rounded-xl bg-brand-50 px-3 py-2.5 text-sm font-medium text-ink"><option value="">Any</option><option value="400000">$400k</option><option value="600000">$600k</option><option value="800000">$800k</option><option value="1000000">$1M</option></select></label>'
          f'<label class="text-xs font-semibold text-ink/60">Sort<select id="f-sort" class="mt-1 w-full rounded-xl bg-brand-50 px-3 py-2.5 text-sm font-medium text-ink"><option value="new">Newest</option><option value="price-asc">Price, low to high</option><option value="price-desc">Price, high to low</option><option value="size">Largest</option></select></label></div>')
    lsec = section("listings", "bg-paper", f'<div class="flex flex-wrap items-end justify-between gap-4">{heading(S, "Featured listings", "Homes for sale now")}'
                   f'<p class="text-sm text-ink/60"><span id="l-count" class="font-semibold text-ink">0</span> homes match</p></div>{fl}'
                   f'<div id="l-grid" class="mt-8 grid sm:grid-cols-2 lg:grid-cols-3 gap-6" aria-live="polite"></div>'
                   f'<div id="l-empty" hidden class="mt-10 text-center rounded-2xl border-2 border-dashed border-line p-10"><p class="font-display text-2xl">No homes match those filters yet</p><p class="mt-2 text-ink/60">Tell us what you\'re looking for and we\'ll send new listings first.</p><a href="#visit" class="{t["btn"]} mt-6">Contact an agent</a></div>', S)
    dialog = (f'<dialog id="home-dialog" class="w-[calc(100%-2rem)] max-w-4xl rounded-3xl p-0 bg-white text-ink" aria-labelledby="h-title"><div class="relative">'
              f'<button type="button" data-close class="absolute right-3 top-3 z-10 w-10 h-10 rounded-full bg-white/90 text-xl font-bold" aria-label="Close">&times;</button>'
              f'<div class="grid grid-cols-3 gap-1"><img id="h-img" alt="" class="col-span-2 w-full h-64 sm:h-80 object-cover"><img id="h-img2" alt="" class="w-full h-64 sm:h-80 object-cover"></div>'
              f'<div class="p-6 sm:p-8"><div class="flex flex-wrap items-start justify-between gap-4"><div><p id="h-status" class="text-xs font-semibold uppercase tracking-wider text-accent-600"></p><h3 id="h-title" class="font-display text-3xl mt-1"></h3><p id="h-area" class="text-ink/60"></p></div>'
              f'<p id="h-price" class="font-display text-4xl"></p></div><dl id="h-specs" class="mt-6 grid grid-cols-3 gap-3 text-sm"></dl><p id="h-desc" class="mt-6 text-ink/75"></p>'
              f'<div class="mt-7 grid sm:grid-cols-3 gap-3"><a id="h-sms" class="{t["btn"]}">Schedule a tour</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call the agent</a><a href="#value" data-close class="{t["btn_line"]}">Sell my home first</a></div>'
              f'<p id="h-pay" class="mt-4 text-xs text-ink/50"></p></div></div></dialog>')
    vform = demo_form(S, "value-form",
        inp(S, "Property address", "address", req=True, ac="street-address", span=True) +
        sel(S, "Bedrooms", "beds", ["2", "3", "4", "5+"], req=True, first="Choose...") + sel(S, "Condition", "condition", ["Move-in ready", "Needs some updates", "Needs major work"], req=True, first="Choose...") +
        chips(S, "timeline", ["0&ndash;3 months", "3&ndash;6 months", "6+ months", "Just curious"], req=True, label="When are you thinking of selling?") +
        inp(S, "Name", "name", req=True, ac="name") + inp(S, "Email", "email", "email", req=True, ac="email") + consent(S),
        "Get my home value", "Thanks, {name}! Your free home value report for {address} will be in your inbox within 24 hours.",
        cls="rounded-3xl bg-white text-ink p-6 sm:p-8 shadow-2xl")
    value = form_section(S, "value", "Selling?", "What is your home worth?",
        "Get a free, personal valuation from a local agent, based on recent sales on your street, not an online guess.",
        ["Report within 24 hours, no obligation", "Recent sales and active competition nearby", "Tips to raise your price before listing"], vform)
    areas = section("areas", "bg-white", heading(S, "Neighborhoods", "Where Brookside lives") + photo_cards(S, [
        dict(img="1761839259488-2bdeeae794f5", title="Downtown Brookside", text="Walkable streets, cafes and the Friday farmers market.", meta="Median price $465k"),
        dict(img="1770638048811-e175eded18fe", title="Oak Ridge", text="Quiet cul-de-sacs, top-rated schools and big backyards.", meta="Median price $720k"),
        dict(img="1616113364365-b6013f3dad25", title="Riverton", text="Riverfront trail, newer homes and easy highway access.", meta="Median price $640k"),
        dict(img="1627927518258-b67557570840", title="Historic district", text="Victorian homes with porches, on gas-lit streets.", meta="Median price $555k"),
    ], cols=4, ratio="aspect-[4/5]"), S)
    about = section("about", "bg-paper", split(S, "1585240975858-7264fd020798",
        text_block(S, "Your agent", "Jessica Moreno, broker &amp; owner", [
            "Jessica has helped more than 340 families buy and sell in the valley since 2010. She grew up in Riverton and still coaches Little League there.",
            "Her team prices homes with real data, markets them with professional photos and video, and answers the phone on weekends."]) +
        f'<dl class="mt-8 grid grid-cols-3 gap-4 max-w-md">'
        f'<div><dt class="text-xs text-ink/60">Homes sold</dt><dd class="font-display text-3xl">340+</dd></div>'
        f'<div><dt class="text-xs text-ink/60">Avg. days on market</dt><dd class="font-display text-3xl">18</dd></div>'
        f'<div><dt class="text-xs text-ink/60">Of asking price</dt><dd class="font-display text-3xl">101%</dd></div></dl><p class="mt-3 text-xs text-ink/50">Sample figures for this demo.</p>',
        pos="object-top"), S)
    revs = section("reviews", "bg-white", heading(S, "Client stories", "Buyers and sellers") + reviews(S, [
        ("We sold in five days for more than asking, and Jessica found our next house before it hit the market.", "Sample seller"),
        ("First-time buyers with a hundred questions. She answered every single one, even on Sundays.", "Sample buyer"),
        ("The photos and video of our home were stunning. Twelve showings the first weekend.", "Sample seller"),
    ]), S)
    vis = visit(S, "1564078516393-cf04bd966897", "Contact", "Stop by the office",
                "On the square, across from the bank. Parking in the rear lot.",
                [("Monday &ndash; Friday", "9:00 am &ndash; 6:00 pm"), ("Saturday", "10:00 am &ndash; 4:00 pm"), ("Sunday", "Open houses &amp; by appointment")],
                "Agents available 7 days a week", f'<a href="tel:{S["tel"]}" class="{t["btn"]}">Call {S["phone"]}</a><a href="#listings" class="{t["btn_line"]}">Browse homes</a>')
    fq = faq(S, [
        ("Do I need to be pre-approved before touring homes?", "It's not required, but it helps you move fast when the right home appears. We can connect you with local lenders."),
        ("How do you decide the listing price?", "We study recent sales, active competition and your home's condition, then walk you through the numbers before you decide."),
        ("Can you help me buy and sell at the same time?", "Yes. We plan the timing so you're not stuck with two mortgages or nowhere to live."),
        ("How long does it take to sell?", "Well-priced homes in our area sell in about three weeks on average, depending on the season and price range."),
        ("What does it cost to work with you as a buyer?", "We explain all fees upfront in a written buyer agreement before you tour, so there are no surprises."),
    ])
    S["mobile"] = mobile_bar(S, "Search homes", "#listings")
    js = "const HOMES = " + json.dumps(listings) + ";\n" + r"""
const img = (id, w) => `https://images.unsplash.com/photo-${id}?auto=format&fit=crop&w=${w}&q=75`;
const fa = $('#f-area'), fb = $('#f-beds'), fm = $('#f-max'), fs = $('#f-sort'); let ftype = '';
function list() {
  let l = HOMES.filter(h => (!fa.value || h.area === fa.value) && h.beds >= Number(fb.value) && (!fm.value || h.price <= Number(fm.value)) && (!ftype || h.type === ftype));
  const so = { 'price-asc': (a, b) => a.price - b.price, 'price-desc': (a, b) => b.price - a.price, size: (a, b) => b.sqft - a.sqft,
               new: (a, b) => (a.status === 'Sold') - (b.status === 'Sold') || HOMES.indexOf(a) - HOMES.indexOf(b) };
  return l.sort(so[fs.value] || so.new);
}
function render() {
  const l = list();
  $('#l-count').textContent = l.filter(h => h.status !== 'Sold').length;
  $('#l-empty').hidden = l.length > 0;
  $('#l-grid').innerHTML = l.map(h => `
    <article class="group bg-white rounded-2xl border border-line overflow-hidden hover:shadow-xl transition flex flex-col ${h.status === 'Sold' ? 'opacity-80' : ''}">
      <button type="button" data-home="${h.id}" class="relative block aspect-[4/3] overflow-hidden text-left" aria-label="See details for ${esc(h.addr)}">
        <img src="${img(h.img, 800)}" alt="${esc(h.addr)}" loading="lazy" class="w-full h-full object-cover transition duration-500 group-hover:scale-105">
        <span class="absolute top-3 left-3 rounded-full ${h.status === 'Sold' ? 'bg-night text-white' : h.status === 'Pending' ? 'bg-white text-ink' : 'bg-accent text-night'} text-xs font-semibold px-3 py-1">${h.status}</span>
      </button>
      <div class="p-5 flex-1 flex flex-col">
        <p class="font-display text-2xl ${h.status === 'Sold' ? 'line-through text-ink/40' : ''}">${money(h.price)}</p>
        <h3 class="mt-1 font-semibold">${esc(h.addr)}</h3><p class="text-sm text-ink/60">${esc(h.area)} &middot; ${h.type}</p>
        <ul class="mt-4 flex gap-4 text-sm text-ink/80"><li><strong>${h.beds}</strong> bd</li><li><strong>${h.baths}</strong> ba</li><li><strong>${h.sqft.toLocaleString('en-US')}</strong> sq ft</li></ul>
        <button type="button" data-home="${h.id}" class="mt-auto pt-5 text-left text-sm font-semibold text-accent-600 hover:underline">View details &rarr;</button>
      </div>
    </article>`).join('');
}
[fa, fb, fm, fs].forEach(el => el.addEventListener('input', render));
$('#hsearch').addEventListener('submit', e => {
  e.preventDefault(); const f = e.target;
  const v = n => f.elements.namedItem(n).value;
  fa.value = v('area'); fm.value = v('max'); ftype = v('type'); render();
  $('#listings').scrollIntoView({ behavior: 'smooth' });
});
const dlg = $('#home-dialog');
document.addEventListener('click', e => {
  const b = e.target.closest('[data-home]'); if (!b) return;
  const h = HOMES.find(x => x.id === b.dataset.home); if (!h) return;
  $('#h-img').src = img(h.img, 1200); $('#h-img2').src = img(h.img2, 600);
  $('#h-status').innerHTML = h.status; $('#h-title').textContent = h.addr; $('#h-area').textContent = `${h.area}, PA · ${h.type}`;
  $('#h-price').textContent = h.status === 'Sold' ? 'Sold' : money(h.price);
  $('#h-specs').innerHTML = [['Bedrooms', h.beds], ['Bathrooms', h.baths], ['Square feet', h.sqft.toLocaleString('en-US')]]
    .map(([k, v]) => `<div class="rounded-xl bg-brand-50 p-3"><dt class="text-xs text-ink/60">${k}</dt><dd class="font-semibold text-lg">${v}</dd></div>`).join('');
  $('#h-desc').textContent = h.desc;
  const r = 0.0675 / 12, n = 360, P = h.price * 0.8;
  $('#h-pay').textContent = h.status === 'Sold' ? '' : `Estimated mortgage about ${money(P * r / (1 - Math.pow(1 + r, -n)))}/month with 20% down at 6.75% for 30 years, before taxes and insurance. Example only.`;
  $('#h-sms').href = `sms:+15555550190?body=${encodeURIComponent('Hi, I would like to tour ' + h.addr + ' (' + money(h.price) + ').')}`;
  $('#h-sms').textContent = h.status === 'Sold' ? 'Find me one like it' : 'Schedule a tour';
  dlg.showModal ? dlg.showModal() : dlg.setAttribute('open', '');
});
render();
"""
    body = hero + lsec + value + areas + about + revs + vis + fq + dialog
    return S, body, js


# =====================================================================  FITNESS
def fitness():
    S = setup(dict(
        slug="fitness", name="BF Fitness", kind="gym", style="bold", header="dark",
        tagline="Strength &middot; Conditioning &middot; Classes",
        description="Demo website for an independent gym: weekly class schedule with booking, membership plans with monthly/annual pricing, free trial sign-up. Built by BF Tech Lab.",
        og="1778828494354-9b717d36dc99",
        fonts="family=Anton&family=Inter:wght@400;500;600;700;800",
        font_display=["Anton", "Impact", "sans-serif"], font_sans=["Inter", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#111113", "50": "#f6f6f4", "100": "#e9e9e6", "700": "#000000"},
                "accent": {"DEFAULT": "#d4ff3a", "600": "#7a9a00"},
                "night": {"DEFAULT": "#0b0b0c", "800": "#161618", "700": "#232326"},
                "ink": "#0b0b0c", "paper": "#f3f3f1", "line": "#e1e1dd"},
        tokens=dict(h1="font-display font-normal uppercase leading-[.95] text-6xl sm:text-7xl lg:text-8xl",
                    h2="font-display text-5xl sm:text-6xl font-normal uppercase leading-[1.0]",
                    h3="font-display text-2xl font-normal uppercase leading-tight tracking-wide"),
        single_weight=True, banner_cls="bg-accent text-night font-medium", accent_ink="text-night",
        phone="(555) 555-0130", tel="+15555550130",
        address="77 Foundry Street<br>Brookside, PA 00000",
        nav=[("Classes", "#classes"), ("Schedule", "#schedule"), ("Membership", "#plans"), ("Coaches", "#coaches"), ("Visit", "#visit")],
        cta=("Free week", "#trial"),
    ))
    t = S["t"]
    hero = hero_full(S, "1778828494354-9b717d36dc99", "Open 5 am &ndash; 10 pm &middot; Coaches on the floor",
        'Get strong. <span class="text-accent">Stay consistent.</span>',
        "Coached classes, a fully equipped floor and a plan that fits your week. Your first seven days are on us.",
        f'<a href="#trial" class="{t["btn"]}">Claim your free week</a><a href="#schedule" class="{t["btn_line_d"]}">See the schedule</a>',
        points=["No sign-up fee", "Cancel anytime", "Childcare 8&ndash;11 am"], tall=True, opacity="opacity-70")
    st = stats(S, [("40+", "Classes every week"), ("12", "Certified coaches"), ("5 am", "Doors open"), ("4.9&#9733;", "Average rating (sample)")], dark=True)
    classes = section("classes", "bg-paper", heading(S, "Classes", "Find your thing") + photo_cards(S, [
        dict(img="1541534741688-6078c6bfb5c5", title="Strength", text="Barbell basics to personal records, coached in small groups.", meta="50 min &middot; all levels"),
        dict(img="1601422407692-ec4eeec1d9b3", title="HIIT", text="Intervals with kettlebells, rowers and bodyweight. Sweat guaranteed.", meta="45 min &middot; high intensity"),
        dict(img="1625594755684-a73285a64f66", title="Spin", text="Rhythm rides with lights and a playlist that pushes you.", meta="45 min &middot; low impact"),
        dict(img="1590556409324-aa1d726e5c3c", title="Boxing", text="Pad work, footwork and conditioning. No sparring, all fun.", meta="50 min &middot; beginner friendly"),
        dict(img="1552196563-55cd4e45efb3", title="Yoga &amp; mobility", text="Stretch, breathe and move better between hard sessions.", meta="60 min &middot; all levels"),
        dict(img="1747239685045-fcbcf98985db", title="Reformer pilates", text="Core strength and control on studio reformers, 8 people max.", meta="50 min &middot; small group"),
    ]), S)
    sched = {
        "Mon": [("6:00 am", "Strength", "Jake", 50, 3), ("7:15 am", "HIIT", "Ari", 45, 6), ("12:00 pm", "Spin", "Dana", 45, 9), ("5:30 pm", "Boxing", "Dana", 50, 2), ("6:45 pm", "Yoga &amp; mobility", "Ari", 60, 11)],
        "Tue": [("6:00 am", "HIIT", "Ari", 45, 4), ("9:30 am", "Reformer pilates", "Mia", 50, 1), ("12:00 pm", "Strength", "Jake", 50, 7), ("6:00 pm", "Spin", "Dana", 45, 5)],
        "Wed": [("6:00 am", "Strength", "Jake", 50, 5), ("7:15 am", "Spin", "Dana", 45, 8), ("12:00 pm", "HIIT", "Ari", 45, 6), ("5:30 pm", "Boxing", "Dana", 50, 0), ("6:45 pm", "Reformer pilates", "Mia", 50, 2)],
        "Thu": [("6:00 am", "HIIT", "Ari", 45, 7), ("9:30 am", "Yoga &amp; mobility", "Mia", 60, 10), ("12:00 pm", "Strength", "Jake", 50, 4), ("6:00 pm", "Spin", "Dana", 45, 3)],
        "Fri": [("6:00 am", "Strength", "Jake", 50, 6), ("7:15 am", "HIIT", "Ari", 45, 2), ("12:00 pm", "Boxing", "Dana", 50, 5), ("5:30 pm", "Yoga &amp; mobility", "Ari", 60, 12)],
        "Sat": [("8:00 am", "HIIT", "Ari", 45, 1), ("9:15 am", "Strength", "Jake", 50, 4), ("10:30 am", "Spin", "Dana", 45, 8)],
        "Sun": [("9:00 am", "Yoga &amp; mobility", "Mia", 60, 9), ("10:30 am", "Reformer pilates", "Mia", 50, 3)],
    }
    full = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}

    def rows(day):
        out = []
        for i, (tm, cl, co, mins, spots) in enumerate(sched[day]):
            sid = f"{day}-{i}"
            sp = '<span class="text-red-400 font-semibold">Full &middot; waitlist</span>' if spots == 0 else f'<span data-spots="{spots}">{spots} spots left</span>'
            btn = "Join waitlist" if spots == 0 else "Book"
            out.append(f'<div class="grid grid-cols-[5.5rem_1fr_auto] sm:grid-cols-[7rem_1fr_9rem_auto] items-center gap-4 py-4 border-b border-white/10">'
                       f'<p class="font-semibold">{tm}</p><div><p class="font-display text-2xl uppercase tracking-wide leading-none">{cl}</p><p class="text-sm text-white/60 mt-1">with {co} &middot; {mins} min</p></div>'
                       f'<p class="hidden sm:block text-sm text-white/70">{sp}</p>'
                       f'<button type="button" data-book="{sid}" class="rounded-md border-2 border-accent text-accent hover:bg-accent hover:text-night font-bold text-sm px-4 py-2 transition">{btn}</button></div>')
        return "".join(out)
    sched_tabs = tabs(S, [(d, full[d], f'<div class="border-t border-white/10">{rows(d)}</div>') for d in sched], dark=True)
    schedsec = section("schedule", "bg-night text-white", f'<div class="flex flex-wrap items-end justify-between gap-4">{heading(S, "This week", "Class schedule", "Book from your phone in two taps. Members can book 7 days ahead.", dark=True)}'
                       f'<p class="reveal text-sm text-white/60">Times shown for this demo week</p></div><div class="reveal mt-10">{sched_tabs}</div>', S)
    plans = [("Open gym", 39, 390, ["24/7 key-fob access", "Full strength &amp; cardio floor", "Locker rooms &amp; showers"], False),
             ("Unlimited", 99, 990, ["Everything in Open gym", "Unlimited classes", "Free InBody scan every month", "Bring a friend on Fridays"], True),
             ("Coached", 249, 2490, ["Everything in Unlimited", "4 personal training sessions a month", "Custom program in our app", "Nutrition check-ins"], False)]
    pc = ""
    for name, m, y, feats, hot in plans:
        bc = "bg-night text-white border-night" if hot else "bg-white border-line"
        tag = '<span class="absolute -top-3 left-6 rounded-md bg-accent text-night text-xs font-bold uppercase tracking-wider px-2.5 py-1">Most popular</span>' if hot else ""
        pc += (f'<div class="reveal relative rounded-xl border-2 {bc} p-7 flex flex-col">{tag}<p class="font-display text-3xl uppercase">{name}</p>'
               f'<p class="mt-4"><span class="font-display text-6xl" data-m="{m}" data-y="{round(y / 12)}">${m}</span><span class="{"text-white/60" if hot else "text-ink/60"}"> /month</span></p>'
               f'<p class="text-sm {"text-white/60" if hot else "text-ink/50"}" data-note data-m-note="Billed monthly, cancel anytime" data-y-note="Billed ${y:,} per year: 2 months free">Billed monthly, cancel anytime</p>'
               f'{checks(S, feats, dark=hot, cls="mt-6 space-y-3 flex-1")}<a href="#trial" class="{t["btn"] if hot else t["btn_dark"]} w-full mt-8">Start free week</a></div>')
    plansec = section("plans", "bg-paper", f'<div class="flex flex-wrap items-end justify-between gap-6">{heading(S, "Membership", "Simple plans. No contracts.")}'
                      f'<div class="reveal inline-flex rounded-md bg-white border border-line p-1" role="group" aria-label="Billing period">'
                      f'<button type="button" data-bill="m" aria-pressed="true" class="bill rounded px-4 py-2 text-sm font-bold">Monthly</button>'
                      f'<button type="button" data-bill="y" aria-pressed="false" class="bill rounded px-4 py-2 text-sm font-bold">Annual &middot; save 17%</button></div></div>'
                      f'<div class="mt-12 grid md:grid-cols-3 gap-6 items-stretch">{pc}</div>', S)
    coaches = section("coaches", "bg-white", heading(S, "Coaches", "People who know your name") + team(S, [
        ("1758875568932-0eefd3e60090", "Jake Morrison", "Head coach &middot; Strength", "Former college athlete. Has taught 600 people to deadlift safely, starting with an empty bar."),
        ("1782849206110-4a47f5acb1f0", "Ari Lopez", "HIIT &amp; conditioning", "Builds workouts that scale from first-timer to marathoner in the same room."),
        ("1548690312-e3b507d8c110", "Dana Brooks", "Boxing, spin &amp; mobility", "Brings the playlist and the energy. Specialist in getting people back from injury."),
    ]), S)
    revs = section("reviews", "bg-night text-white", heading(S, "Members", "Why people stay", dark=True) + reviews(S, [
        ("I've tried four gyms. This is the first one where the coaches noticed when I didn't show up, and texted me.", "Sample member"),
        ("Down 22 pounds and deadlifting my body weight. The 6 am strength class is the best part of my day.", "Sample member"),
        ("Booking classes from the app takes ten seconds. Childcare in the morning is a lifesaver.", "Sample member"),
    ], dark=True), S)
    tform = demo_form(S, "trial-form",
        inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
        inp(S, "Email", "email", "email", req=True, ac="email", span=True) +
        chips(S, "goal", ["Lose weight", "Build strength", "Get back in shape", "Train for an event"], req=True, label="Your main goal") +
        chips(S, "time", ["Early morning", "Lunchtime", "Evening", "Weekends"], label="When do you like to train?") + consent(S),
        "Start my free week", "You're in, {name}! We'll text your free pass. A coach will meet you at the front desk on your first visit.",
        cls="rounded-xl bg-white text-ink p-6 sm:p-8 shadow-2xl")
    trial = form_section(S, "trial", "Free week", "Try everything for 7 days",
        "Classes, open gym and a free intro session with a coach. No card needed.", ["Free 1:1 intro session", "All classes included", "No credit card, no pressure"], tform)
    vis = visit(S, "1623874514711-0f321325f318", "Visit", "Come see the space",
                "Free parking in our lot. Showers, lockers and towels included.",
                [("Monday &ndash; Friday", "5:00 am &ndash; 10:00 pm"), ("Saturday &ndash; Sunday", "7:00 am &ndash; 6:00 pm"), ("Members", "24/7 key-fob access")],
                "12,000 sq ft of training space", f'<a href="#trial" class="{t["btn_dark"]}">Claim free week</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>')
    fq = faq(S, [
        ("I'm a complete beginner. Is that okay?", "Absolutely. Every new member gets a free intro session, and every class has easier options. Half our members started from zero."),
        ("Is there a contract?", "No. Plans are month to month. Annual plans are optional and save you two months."),
        ("Can I freeze my membership?", "Yes, up to three months a year for travel, injury or anything else, at no charge."),
        ("How much is personal training?", "Packs start at $65 per session, or choose the Coached plan for four sessions a month plus unlimited classes."),
        ("Do you have childcare?", "Yes, weekday mornings from 8 to 11 am, for kids 6 months to 10 years. $5 per visit for members."),
    ], bg="bg-paper")
    S["mobile"] = mobile_bar(S, "Free week", "#trial")
    S["css"] = ".bill[aria-pressed=\"true\"]{background:var(--brand);color:#fff}"
    js = r"""
document.addEventListener('click', e => {
  const b = e.target.closest('[data-book]'); if (!b) return;
  const row = b.parentElement, sp = row.querySelector('[data-spots]');
  if (b.dataset.done) { b.dataset.done = ''; b.textContent = b.dataset.prev; b.classList.remove('bg-accent', 'text-night'); if (sp) { sp.dataset.spots = Number(sp.dataset.spots) + 1; sp.textContent = sp.dataset.spots + ' spots left'; } return; }
  b.dataset.prev = b.textContent; b.dataset.done = '1';
  b.textContent = b.dataset.prev === 'Book' ? 'Booked ✓' : 'On waitlist ✓';
  b.classList.add('bg-accent', 'text-night');
  if (sp && b.dataset.prev === 'Book') { sp.dataset.spots = Math.max(0, Number(sp.dataset.spots) - 1); sp.textContent = sp.dataset.spots + ' spots left'; }
});
$$('[data-bill]').forEach(btn => btn.addEventListener('click', () => {
  const y = btn.dataset.bill === 'y';
  $$('[data-bill]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
  $$('[data-m]').forEach(p => p.textContent = '$' + (y ? p.dataset.y : p.dataset.m));
  $$('[data-note]').forEach(n => n.textContent = y ? n.dataset.yNote : n.dataset.mNote);
}));
"""
    body = hero + st + classes + schedsec + plansec + coaches + revs + trial + vis + fq
    return S, body, js


# =====================================================================  SALON
def salon():
    S = setup(dict(
        slug="salon", name="BF Salon", kind="hair salon", style="soft", header="light",
        tagline="Hair &middot; Color &middot; Care",
        description="Demo website for a hair salon: service menu with prices, stylist profiles, online booking with stylist and time selection. Built by BF Tech Lab.",
        og="1600948836101-f9ffda59d250",
        fonts="family=Italiana&family=Jost:wght@400;500;600",
        font_display=["Italiana", "Georgia", "serif"], font_sans=["Jost", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#8e5a52", "50": "#f8efeb", "100": "#f1e1dc", "700": "#744740"},
                "accent": {"DEFAULT": "#d6b38a", "600": "#b8946a"},
                "night": {"DEFAULT": "#251b1d", "800": "#2f2427", "700": "#3d3033"},
                "ink": "#251b1d", "paper": "#fbf6f3", "line": "#ecddd6"},
        tokens=dict(h1="font-display font-normal leading-[1.02] text-5xl sm:text-6xl lg:text-7xl",
                    h2="font-display text-4xl sm:text-5xl font-normal leading-[1.08]",
                    h3="font-display text-2xl font-normal leading-snug"),
        single_weight=True, banner_cls="bg-night text-white/90", accent_ink="text-night",
        phone="(555) 555-0120", tel="+15555550120",
        address="14 Linden Street<br>Brookside, PA 00000",
        nav=[("Services", "#services"), ("Stylists", "#team"), ("Looks", "#looks"), ("Book", "#book"), ("Visit", "#visit")],
        cta=("Book now", "#book"),
    ))
    t = S["t"]
    hero = hero_split(S, "1600948836101-f9ffda59d250", "1785456283212-338f5bc44d50", "6 openings left this week",
        'Hair that feels like <em class="text-brand">you</em>, only better.',
        "Cuts, color and balayage by stylists who listen first. Book online in under a minute, with the stylist you want.",
        f'<a href="#book" class="{t["btn"]}">Book an appointment</a><a href="#services" class="{t["btn_line"]}">See prices</a>',
        [("Google rating", "4.9&#9733;"), ("Stylists", "9"), ("Since", "2014")],
        "Free consultations, every day", "Not sure what you want? Book a 15-minute chat with a stylist, on us.")

    def panel(img, items, pos="object-center"):
        return (f'<div class="grid lg:grid-cols-5 gap-10 items-start"><div class="lg:col-span-3">{price_list(S, items, cols=1)}</div>'
                f'<div class="lg:col-span-2"><img src="{U(img, 800)}" alt="" loading="lazy" class="w-full aspect-[4/5] object-cover {pos} rounded-3xl shadow-xl"></div></div>')
    menu = tabs(S, [
        ("cuts", "Cuts &amp; styling", panel("1580618672591-eb180b1a973f", [
            ("Women's cut &amp; style", "Consultation, wash, cut and blow-dry", "from $65"), ("Blowout", "Wash and a smooth or bouncy finish", "from $45"),
            ("Curly cut", "Dry cut, curl by curl, with styling lesson", "from $85"), ("Kids' cut", "Under 12", "from $30"), ("Updo &amp; event styling", "Weddings, proms and parties", "from $85")])),
        ("color", "Color", panel("1707812343087-c9ff9e5abb43", [
            ("Single-process color", "Root to ends, one shade", "from $85"), ("Root touch-up", "Up to 1.5 inches of regrowth", "from $70"),
            ("Gloss or toner", "Shine and tone refresh", "from $45"), ("Gray blending", "Soft, low-maintenance coverage", "from $95"), ("Color correction", "Starts with a free consultation", "quote")])),
        ("balayage", "Balayage &amp; highlights", panel("1785456390070-9960e3997066", [
            ("Partial highlights", "Face-framing and crown", "from $120"), ("Full highlights", "Foils through the whole head", "from $160"),
            ("Balayage", "Hand-painted, soft grow-out", "from $185"), ("Lived-in color", "Balayage, gloss and blowout", "from $210")])),
        ("treat", "Treatments", panel("1712641966810-611ff1503c6d", [
            ("Deep conditioning mask", "15 minutes, add to any service", "$35"), ("Bond repair treatment", "For color-treated and damaged hair", "$40"),
            ("Keratin smoothing", "Frizz control for up to 4 months", "from $250"), ("Scalp treatment", "Exfoliation and massage", "$45")])),
        ("men", "Men's", panel("1788328155052-e02abe9ba983", [
            ("Men's cut", "Wash, cut and style", "$40"), ("Skin fade", "", "$45"), ("Beard trim &amp; line-up", "", "$25"),
            ("Cut &amp; beard", "", "$60"), ("Gray blending for men", "", "$45")])),
    ])
    services = section("services", "bg-white", heading(S, "Services &amp; prices", "The menu", "Prices depend on stylist level and hair length. Your stylist confirms the price before starting.") + f'<div class="reveal mt-10">{menu}</div>', S)
    team_s = section("team", "bg-paper", heading(S, "Stylists", "Meet the team") + team(S, [
        ("1580489944761-15a19d654956", "Sofia Reyes", "Owner &middot; Color specialist", "Fifteen years behind the chair and a soft spot for lived-in blondes. Trains every new stylist herself."),
        ("1662850886700-4ec19bd30d11", "Maya Carter", "Curl specialist", "Certified in curly cutting. Will teach you a routine that works on busy mornings."),
        ("1568602471122-7832951cc4c5", "Leo Grant", "Cuts &amp; men's grooming", "Precision cuts, fades and beard work. Quick, friendly and always on time."),
    ]), S)
    looks = section("looks", "bg-white", heading(S, "Recent looks", "Fresh from the chair") + gallery(S, [
        ("1785456390070-9960e3997066", "Soft balayage by Sofia"), ("1614020863825-28a0bb7e3c3c", "Copper glaze"),
        ("1535295972055-1c762f4483e5", "Curly cut by Maya"), ("1734111719430-fe4a3973f8af", "Round-brush blowout"),
        ("1785456283212-338f5bc44d50", "Beach waves"), ("1761839256791-6a93f89fb8b0", "Big smiles in the chair"),
    ]), S)
    form = multistep(S, "book-form", [
        ("Choose a service", chips(S, "service", ["Cut &amp; style", "Color", "Balayage", "Highlights", "Treatment", "Men's cut", "Free consultation"], req=True)),
        ("Stylist &amp; time", chips(S, "stylist", ["No preference", "Sofia", "Maya", "Leo"], req=True, label="Stylist", checked="No preference") +
         '<div class="sm:col-span-2"><p class="text-sm font-semibold">Day <span class="text-red-600" aria-hidden="true">*</span></p><div id="days" class="mt-2 flex flex-wrap gap-2"></div></div>' +
         chips(S, "time", ["10:00 am", "11:30 am", "1:00 pm", "2:30 pm", "4:00 pm", "5:30 pm"], req=True, label="Time")),
        ("Your details", inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
         inp(S, "Email", "email", "email", ac="email") + chips(S, "first", ["Yes", "No"], label="First visit with us?", span=False) + consent(S, "Text me a reminder the day before.")),
    ], "Book appointment", "You're booked!", "See you {day} at {time}, {name}. We'll text you a reminder the day before your {service}.")
    book = form_section(S, "book", "Book online", "Pick your stylist and time",
        "Real-time openings, confirmed instantly. Need to change? Reply to your reminder text.",
        ["Instant confirmation by text", "Free changes up to 24 hours before", "Gift cards available at the front desk"], form)
    revs = section("reviews", "bg-paper", heading(S, "Reviews", "Kind words") + reviews(S, [
        ("Sofia fixed a box-dye disaster in one session. I've never had so many compliments.", "Sample client"),
        ("Finally someone who knows how to cut curly hair. Maya changed my whole routine.", "Sample client"),
        ("Booked at midnight for the next morning. Leo was on time and the fade is perfect.", "Sample client"),
    ]), S)
    vis = visit(S, "1781450090585-1a511b7066d9", "Visit", "Come say hello",
                "Free parking behind the salon. Complimentary coffee, tea and Wi-Fi.",
                [("Monday", "Closed"), ("Tuesday &ndash; Friday", "9:00 am &ndash; 8:00 pm"), ("Saturday", "8:00 am &ndash; 5:00 pm"), ("Sunday", "10:00 am &ndash; 4:00 pm")],
                "Step-free entrance on Linden Street", f'<a href="#book" class="{t["btn"]}">Book now</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>')
    fq = faq(S, [
        ("Which service should I book?", "If you're unsure, book a free consultation. Your stylist will recommend the service and give you a price."),
        ("What's your cancellation policy?", "Please give us 24 hours' notice. Late cancellations and no-shows are charged 50% of the service."),
        ("Do you do patch tests for color?", "Yes. New color clients are asked to come in for a quick patch test at least 48 hours before."),
        ("Can I buy the products you use?", "Yes. Your stylist will recommend what you need, and nothing you don't."),
        ("Do you sell gift cards?", "Yes, in any amount, at the front desk or by phone."),
    ], bg="bg-white")
    S["mobile"] = mobile_bar(S, "Book now", "#book")
    js = r"""
(function () {
  const box = $('#days'); if (!box) return;
  const d = new Date(); let n = 0, out = '';
  while (n < 6) {
    d.setDate(d.getDate() + 1);
    if (d.getDay() === 1) continue;
    const lab = d.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
    out += `<label class="chip cursor-pointer"><input type="radio" name="day" value="${lab}" class="sr-only" required><span class="inline-block rounded-full border border-line bg-white text-ink px-4 py-2 text-sm font-medium transition hover:border-brand">${lab}</span></label>`;
    n++;
  }
  box.innerHTML = out;
})();
"""
    body = hero + services + team_s + looks + book + revs + vis + fq
    return S, body, js


SITES = [law, realestate, fitness, salon]
