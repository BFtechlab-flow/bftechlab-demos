# -*- coding: utf-8 -*-
"""Demo sites: veterinary clinic, chiropractic, auto repair, med spa."""
from lib import *


# =====================================================================  VETERINARY
def vet():
    S = setup(dict(
        slug="veterinary", name="BF Animal Hospital", kind="veterinary clinic", style="soft", header="light",
        tagline="Dogs &middot; Cats &middot; Small pets",
        description="Demo website for a veterinary clinic: appointment requests by pet and reason, services, team, new client offer. Built by BF Tech Lab.",
        og="1700665537650-1bf37979aae0",
        fonts="family=Fredoka:wght@500;600&family=Nunito+Sans:wght@400;600;700",
        font_display=["Fredoka", "system-ui", "sans-serif"], font_sans=['"Nunito Sans"', "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#0f766e", "50": "#ebf8f6", "100": "#d3f0ec", "700": "#0b5f58"},
                "accent": {"DEFAULT": "#f59e0b", "600": "#d98706"},
                "night": {"DEFAULT": "#0f2e2b", "800": "#143b37", "700": "#1b4b46"},
                "ink": "#0f2e2b", "paper": "#f5faf9", "line": "#d5e9e5"},
        banner_cls="bg-night text-white/90", accent_ink="text-night",
        phone="(555) 555-0110", tel="+15555550110",
        address="260 Meadow Lane<br>Brookside, PA 00000",
        nav=[("Services", "#services"), ("New clients", "#offer"), ("Our team", "#team"), ("Appointments", "#book"), ("Visit", "#visit")],
        cta=("Book a visit", "#book"),
    ))
    t = S["t"]
    hero = hero_split(S, "1700665537650-1bf37979aae0", "1601979031925-424e53b6caaa", "Accepting new patients &middot; same-day sick visits",
        'Kind, unhurried care for the pets <span class="text-brand">you love.</span>',
        "Wellness exams, vaccines, dental care and surgery under one roof, with vets who explain everything and never rush you.",
        f'<a href="#book" class="{t["btn"]}">Request an appointment</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>',
        [("Caring since", "2002"), ("Google rating", "4.9&#9733;"), ("Sick visits", "Same day")],
        "Next openings: today 4:30 pm &amp; tomorrow morning", "Request online any time. We confirm by phone or text within the hour.", pos="object-[70%_center]")
    services = section("services", "bg-white", heading(S, "Services", "Everything your pet needs, from first shots to golden years") + photo_cards(S, [
        dict(img="1654895716780-b4664497420d", title="Wellness exams", text="Nose-to-tail checkups with time for your questions, and a written plan you can take home."),
        dict(img="1630438994394-3deff7a591bf", title="Vaccines &amp; prevention", text="Core vaccines, flea, tick and heartworm prevention tailored to your pet's lifestyle."),
        dict(img="1654895574745-82ef6b5970c4", title="Dental care", text="Cleanings under safe anesthesia, digital dental X-rays and gentle extractions."),
        dict(img="1551190822-a9333d879b1f", title="Surgery", text="Spays, neuters and soft-tissue surgery with advanced monitoring and pain control."),
        dict(img="1596272875729-ed2ff7d6d9c5", title="Cat-friendly visits", text="A separate cat waiting area, quiet exam room and gentle, low-stress handling."),
        dict(img="1558788353-f76d92427f16", title="Senior pet care", text="Bloodwork, arthritis management and comfort care to keep older pets happy longer."),
    ]), S)
    offer = (f'<section id="offer" class="bg-brand text-white"><div class="max-w-6xl mx-auto px-4 sm:px-6 py-12 md:py-14 grid md:grid-cols-3 gap-8 items-center">'
             f'<div class="reveal md:col-span-2"><p class="text-sm font-semibold uppercase tracking-wider text-accent">New clients</p>'
             f'<h2 class="font-display text-3xl sm:text-4xl font-semibold mt-2">First exam $45 <span class="text-white/60 text-2xl line-through ml-2">$75</span></h2>'
             f'<p class="mt-3 text-white/80 max-w-xl">Includes a full physical exam, weight check and a personalized vaccine and prevention plan. Bring your records, or we\'ll request them for you.</p></div>'
             f'<div class="reveal md:text-right"><a href="#book" class="{t["btn_accent"]}">Claim this offer</a></div></div></section>\n')
    team_s = section("team", "bg-paper", heading(S, "Our team", "Vets who remember your pet's name") + team(S, [
        ("1559839734-2b71ea197ec2", "Dr. Hannah Cole, DVM", "Medical director", "Twenty years in small-animal medicine. Shares her office with a three-legged cat named Biscuit."),
        ("1612349317150-e413f6a5b16d", "Dr. Ravi Patel, DVM", "Surgery &amp; dentistry", "Performs most of our surgeries and dental procedures. Patient with nervous dogs and their owners."),
        ("1770134223774-13b735e29201", "Megan Shaw, LVT", "Lead veterinary technician", "Runs our dental suite and new-puppy classes. Ask her anything about house training."),
    ]), S)
    form = multistep(S, "appt-form", [
        ("About your pet", chips(S, "species", ["Dog", "Cat", "Rabbit", "Other"], req=True, label="Species") +
         inp(S, "Pet's name", "petname", req=True) + sel(S, "Age", "age", ["Under 1 year", "1 to 7 years", "8 years or older"], req=True, first="Choose...")),
        ("Reason &amp; timing", chips(S, "reason", ["Wellness exam", "Vaccines", "Sick or injured", "Dental", "Surgery consult", "Other"], req=True, label="Reason for the visit") +
         chips(S, "when", ["Today", "Tomorrow", "This week", "Next week"], req=True, label="Preferred day") +
         chips(S, "slot", ["Morning", "Afternoon", "Evening"], label="Preferred time")),
        ("Your details", inp(S, "Your name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
         inp(S, "Email", "email", "email", ac="email") + chips(S, "newclient", ["Yes", "No"], label="New client?", span=False) + consent(S)),
    ], "Request appointment", "Request received", "Thanks, {name}! We'll call or text within the hour to confirm {petname}'s visit ({reason}).")
    book = form_section(S, "book", "Appointments", "Book a visit for your pet",
        "Tell us a little about your pet and when works. Sick pets are always seen the same day.",
        ["Same-day appointments for sick pets", "Separate cat and dog waiting areas", "Reminders by text before every visit"], form,
        after=(f'<div class="mt-8 rounded-2xl border border-white/15 p-5"><p class="font-semibold text-accent">Emergency after hours?</p>'
               f'<p class="mt-1 text-sm text-white/75">Call the 24/7 Valley Emergency Pet Center at <a href="tel:+15555550199" class="underline">(555) 555-0199</a>. We receive their report the next morning.</p></div>'))
    why = section("why", "bg-white", split(S, "1700665537604-412e89a285c3",
        text_block(S, "Why families choose us", "Unhurried visits, clear prices", [
            "Every appointment is at least 30 minutes, so there's time to examine your pet properly and answer your questions.",
            "Before any treatment you get a written estimate. No surprises at the front desk."]) +
        checks(S, ["Low-stress handling and treats for every patient", "Digital X-rays and in-house lab results in minutes", "Payment plans and most pet insurance accepted"]),
        reverse=True, pos="object-center"), S)
    revs = section("reviews", "bg-paper", heading(S, "Reviews", "From pet parents") + reviews(S, [
        ("Dr. Cole sat on the floor with our anxious rescue for ten minutes before even starting the exam. We're clients for life.", "Sample pet parent"),
        ("Our cat hates the vet, but the quiet cat room made a huge difference. In and out in 30 minutes.", "Sample pet parent"),
        ("They saw our puppy the same day she swallowed a sock and called every hour to update us.", "Sample pet parent"),
    ]), S)
    vis = visit(S, "1551076805-e1869033e561", "Visit", "Easy to find on Meadow Lane",
                "Free parking right outside, with a fenced grass area for dogs.",
                [("Monday &ndash; Friday", "7:30 am &ndash; 7:00 pm"), ("Saturday", "8:00 am &ndash; 2:00 pm"), ("Sunday", "Closed")],
                "Separate cat &amp; dog waiting areas", f'<a href="#book" class="{t["btn"]}">Book a visit</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>')
    fq = faq(S, [
        ("Do you see rabbits and other small pets?", "Yes. We see dogs, cats, rabbits, guinea pigs and ferrets. For birds and reptiles we'll refer you to a specialist."),
        ("Do you offer payment plans?", "Yes, for bills over $300, and we accept most pet insurance plans. Ask us to submit the claim for you."),
        ("Can I stay with my pet during the exam?", "Of course, for exams and vaccines. For surgery and dental procedures we'll update you by text."),
        ("How do I get my pet's records?", "Ask at the front desk or reply to any reminder text and we'll email them the same day."),
        ("What should I bring to the first visit?", "Previous records if you have them, a list of food and medications, and your pet on a leash or in a carrier."),
    ], bg="bg-white")
    S["mobile"] = mobile_bar(S, "Book a visit", "#book")
    body = hero + services + offer + team_s + book + why + revs + vis + fq
    return S, body, ""


# =====================================================================  CHIROPRACTIC
def chiro():
    S = setup(dict(
        slug="chiropractic", name="BF Chiropractic", kind="chiropractic clinic", style="soft", header="light",
        tagline="Chiropractic &amp; sports rehab",
        description="Demo website for a chiropractic clinic: conditions treated, new patient special, online booking, team and insurance info. Built by BF Tech Lab.",
        og="1706353399656-210cca727a33",
        fonts="family=Outfit:wght@500;600;700&family=Inter:wght@400;500;600;700",
        font_display=["Outfit", "system-ui", "sans-serif"], font_sans=["Inter", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#0f6a8b", "50": "#ecf6fa", "100": "#d7edf5", "700": "#0b5672"},
                "accent": {"DEFAULT": "#5ec4a5", "600": "#3fa587"},
                "night": {"DEFAULT": "#0d2536", "800": "#123047", "700": "#1a3f5c"},
                "ink": "#0d2536", "paper": "#f5f9fb", "line": "#d9e6ee"},
        banner_cls="bg-night text-white/90", accent_ink="text-night",
        phone="(555) 555-0125", tel="+15555550125",
        address="45 Wellness Park, Suite B<br>Brookside, PA 00000",
        nav=[("Conditions", "#conditions"), ("First visit", "#first"), ("Team", "#team"), ("Insurance", "#insurance"), ("Visit", "#visit")],
        cta=("Book a visit", "#book"),
    ))
    t = S["t"]
    hero = hero_split(S, "1706353399656-210cca727a33", "1562771379-eafdca7a02f8", "New patients seen this week",
        'Move without pain <span class="text-brand">again.</span>',
        "Gentle chiropractic care, rehab exercises and massage for back pain, neck pain, headaches and sports injuries. Most patients feel better within the first few visits.",
        f'<a href="#book" class="{t["btn"]}">Book your first visit</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>',
        [("First visit", "$59"), ("Visit length", "30 min"), ("Insurance", "Most plans")],
        "Openings today at 4:15 &amp; 5:30 pm", "Book online in a minute. Intake forms arrive by text, so you skip the clipboard.")
    cond = section("conditions", "bg-white", heading(S, "Conditions we treat", "Find relief for what's holding you back") + photo_cards(S, [
        dict(img="1618914241652-ff0a094b5a86", title="Lower back pain", text="From a pulled muscle to chronic stiffness, with care that addresses the cause, not just the pain."),
        dict(img="1615997393458-98aad1851521", title="Neck &amp; shoulder pain", text="Tension from desk work, poor sleep or old injuries, eased with adjustments and soft-tissue work."),
        dict(img="1573164574144-649081e9421a", title="Headaches", text="Tension headaches often start in the neck. Many patients see fewer and milder headaches."),
        dict(img="1769029271190-36b22f5e6771", title="Sciatica", text="Pain that runs down the leg, treated with gentle decompression and targeted exercises."),
        dict(img="1645005513713-9e2b92a687d3", title="Sports injuries", text="Sprains, strains and overuse injuries, with a rehab plan to get you back in the game."),
        dict(img="1649751361457-01d3a696c7e6", title="Posture &amp; mobility", text="Stiff hips, rounded shoulders, limited movement. We build strength where it's missing."),
    ]), S)
    special = (f'<section class="bg-brand text-white"><div class="max-w-6xl mx-auto px-4 sm:px-6 py-12 md:py-14 grid md:grid-cols-3 gap-8 items-center">'
               f'<div class="reveal md:col-span-2"><p class="text-sm font-semibold uppercase tracking-wider text-accent">New patient special</p>'
               f'<h2 class="font-display text-3xl sm:text-4xl font-semibold mt-2">$59 first visit, everything included</h2>'
               f'<p class="mt-3 text-white/80 max-w-xl">Consultation, full exam, X-rays if needed and your first treatment. Usually $189.</p></div>'
               f'<div class="reveal md:text-right"><a href="#book" class="{t["btn_accent"]}">Book the $59 visit</a></div></div></section>\n')
    first = section("first", "bg-paper", heading(S, "Your first visit", "What to expect in 60 minutes") + steps(S, [
        ("Listen", "We start with your story: what hurts, when it started and what you want to get back to."),
        ("Examine", "Posture, movement and neurological tests, plus X-rays only if you need them."),
        ("Plan", "A clear plan with the number of visits and the cost, in writing, before anything starts."),
        ("Treat", "Your first adjustment or soft-tissue treatment, and two exercises to do at home."),
    ]), S)
    more = section("more", "bg-white", split(S, "1639162906614-0603b0ae95fd",
        text_block(S, "More than adjustments", "Care that keeps working after you leave", [
            "Every plan combines hands-on treatment with exercises you can actually stick with, so the results last.",
            "Our massage therapist and rehab area are on site, so you don't need separate appointments elsewhere."]) +
        checks(S, ["Chiropractic adjustments, gentle or traditional", "Therapeutic massage and soft-tissue work", "Rehab exercises with progress tracking in our app"]),
        reverse=True), S)
    team_s = section("team", "bg-paper", heading(S, "Our team", "The people behind your recovery") + team(S, [
        ("1758691462651-611d730c5272", "Dr. Laura Bennett, DC", "Clinic director", "Fifteen years in practice. Specializes in back pain and helping desk workers move better."),
        ("1757125736482-328a3cdd9743", "Dr. Grace Lin, DC", "Sports &amp; pregnancy care", "Works with local runners and high school teams, and certified in prenatal chiropractic."),
        ("1594824476967-48c8b964273f", "Nicole Adams, LMT", "Massage therapist", "Deep tissue and sports massage, perfect alongside adjustments for stubborn tension."),
    ]), S)
    form = multistep(S, "chiro-form", [
        ("What brings you in?", chips(S, "concern", ["Lower back", "Neck or shoulders", "Headaches", "Sciatica", "Sports injury", "Other"], req=True) +
         chips(S, "duration", ["Under 2 weeks", "2 weeks to 3 months", "Over 3 months"], req=True, label="How long has it bothered you?")),
        ("Scheduling", chips(S, "pref", ["Earliest available", "Mornings", "Lunchtime", "Evenings", "Saturday"], req=True, label="Best time for you") +
         sel(S, "How will you pay?", "insurance", ["Health insurance (PPO)", "Medicare", "Auto accident (PIP)", "Workers' compensation", "Self-pay / HSA"], req=True, first="Choose...", span=True)),
        ("Your details", inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
         inp(S, "Email", "email", "email", ac="email", span=True) + consent(S)),
    ], "Request my visit", "Request received", "Thanks, {name}! We'll call to confirm your first visit and text you the intake forms.")
    book = form_section(S, "book", "Book online", "Start feeling better this week",
        "Three quick questions. We'll confirm your time and send intake forms by text.",
        ["$59 new patient visit with exam and X-rays", "Same-week appointments, early and late hours", "Clear plan and costs before any treatment"], form)
    ins = section("insurance", "bg-white", f'<div class="grid lg:grid-cols-2 gap-10 items-center"><div>{heading(S, "Insurance &amp; payment", "We handle the paperwork", "We're in network with most PPO plans and Medicare, and bill auto accident and workers\' compensation claims directly.")}</div>'
                  f'<div class="reveal flex flex-wrap gap-3">' + "".join(f'<span class="rounded-full border border-line bg-paper px-5 py-3 font-semibold">{x}</span>' for x in ["Most PPO plans", "Medicare", "Auto accident (PIP)", "Workers' comp", "HSA &amp; FSA cards", "Payment plans"]) +
                  '</div></div>', S)
    revs = section("reviews", "bg-paper", heading(S, "Reviews", "What patients say") + reviews(S, [
        ("Six weeks ago I couldn't tie my shoes. Dr. Bennett explained everything and gave me exercises that actually work.", "Sample patient"),
        ("Booked online on Sunday night, seen Monday morning. Forms by text, no waiting room clipboard.", "Sample patient"),
        ("Dr. Lin got me back to running after a hip injury, just in time for my half marathon.", "Sample patient"),
    ]), S)
    vis = visit(S, "1768507423533-b87b62769758", "Visit", "Easy parking, ground floor",
                "Wellness Park, right off Route 30. Step-free entrance and free parking at the door.",
                [("Monday, Wednesday, Friday", "8:00 am &ndash; 6:30 pm"), ("Tuesday, Thursday", "10:00 am &ndash; 7:00 pm"), ("Saturday", "9:00 am &ndash; 12:00 pm"), ("Sunday", "Closed")],
                "Early and evening appointments", f'<a href="#book" class="{t["btn"]}">Book a visit</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>')
    fq = faq(S, [
        ("Does an adjustment hurt?", "Most people feel relief, not pain. If you prefer, we use gentle techniques with no twisting or cracking."),
        ("Do I need a referral from my doctor?", "No. You can book directly. We're happy to coordinate with your doctor when it helps your care."),
        ("How many visits will I need?", "It depends on your condition. After the first exam you'll get a written plan, and many patients improve in 4 to 6 visits."),
        ("Is chiropractic safe?", "Chiropractic care is very safe when performed by a licensed chiropractor after a proper exam, which is how every visit starts here."),
        ("What should I wear?", "Comfortable clothes you can move in, like workout clothes. We have gowns if needed."),
    ], bg="bg-white")
    S["mobile"] = mobile_bar(S, "Book a visit", "#book")
    body = hero + cond + special + first + more + team_s + book + ins + revs + vis + fq
    return S, body, ""


# =====================================================================  AUTO REPAIR
def auto():
    S = setup(dict(
        slug="auto-repair", name="BF Auto Care", kind="auto repair shop", style="bold", header="dark",
        tagline="Repair &middot; Maintenance &middot; Tires",
        description="Demo website for an independent auto repair shop: service booking, coupons, live repair status checker, estimate requests. Built by BF Tech Lab.",
        og="1615906655593-ad0386982a0f",
        fonts="family=Saira+Condensed:wght@600;700;800&family=Inter:wght@400;500;600;700",
        font_display=['"Saira Condensed"', "Impact", "sans-serif"], font_sans=["Inter", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#e63329", "50": "#fdf1f0", "100": "#fbe0de", "700": "#c92b22"},
                "accent": {"DEFAULT": "#e63329", "600": "#c92b22"},
                "night": {"DEFAULT": "#121315", "800": "#1b1c1f", "700": "#26282c"},
                "ink": "#121315", "paper": "#f4f4f5", "line": "#dedfe2"},
        tokens=dict(h1="font-display font-extrabold uppercase leading-[.92] text-6xl sm:text-7xl lg:text-8xl",
                    h2="font-display text-5xl sm:text-6xl font-extrabold uppercase leading-[.98]",
                    h3="font-display text-2xl font-bold uppercase leading-tight"),
        banner_cls="bg-accent text-white font-medium", accent_ink="text-white",
        phone="(555) 555-0145", tel="+15555550145",
        address="905 Route 30 West<br>Brookside, PA 00000",
        nav=[("Services", "#services"), ("Coupons", "#deals"), ("Repair status", "#status"), ("Reviews", "#reviews"), ("Visit", "#visit")],
        cta=("Book service", "#book"),
    ))
    t = S["t"]
    days = ["Today", "Tomorrow", "This week", "Next week"]
    side = demo_form(S, "quickbook",
        f'<p class="sm:col-span-2 font-display text-3xl font-extrabold uppercase">Book a service</p>' +
        sel(S, "Service", "service", ["Oil change", "Brakes", "Tires &amp; alignment", "Check engine light", "AC &amp; heating", "State inspection", "Something else"], req=True, first="Choose...", span=True) +
        sel(S, "Day", "day", days, req=True) + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel"),
        "Book it", "Done! We'll text you to confirm a drop-off time {day} for your {service}.",
        cls="bg-white text-ink rounded-xl p-6 shadow-2xl", note="Free shuttle within 5 miles")
    hero = hero_full(S, "1615906655593-ad0386982a0f", "Certified technicians &middot; 24-month / 24,000-mile warranty",
        'Honest repairs. <span class="text-accent">Done when we say.</span>',
        "Digital inspections with photos sent to your phone, prices you approve before we start, and free loaner cars for bigger jobs.",
        f'<a href="#book" class="{t["btn"]}">Book a service</a><a href="tel:{S["tel"]}" class="{t["btn_line_d"]}">{PHONE_ICON} {S["phone"]}</a>',
        side=side, points=["All makes &amp; models", "Free loaner cars", "Same-day most repairs"], opacity="opacity-55")
    st = stats(S, [("24/24", "Months / miles warranty"), ("35,000+", "Cars repaired"), ("Same day", "Most repairs"), ("4.9&#9733;", "Average rating (sample)")])
    services = section("services", "bg-paper", heading(S, "Services", "Everything your car needs") + photo_cards(S, [
        dict(img="1768689033119-c3ac1e437d20", title="Oil change", text="Synthetic and conventional oil, new filter and a free 30-point inspection.", meta="From $49.95"),
        dict(img="1613214150384-14921ff659b2", title="Brakes", text="Pads, rotors, calipers and fluid. We show you the measurements before replacing anything.", meta="From $149 per axle"),
        dict(img="1599082267768-4815b2ea6bd2", title="Tires &amp; alignment", text="All major brands at fair prices, mounting, balancing and computer alignment.", meta="Alignment $89"),
        dict(img="1625047509248-ec889cbff17f", title="Check engine light", text="Full diagnostics with a clear explanation of what's wrong and what it costs.", meta="$99, credited to the repair"),
        dict(img="1486006920555-c77dcf18193c", title="AC &amp; heating", text="AC recharge, leak tests, heater cores and blend doors. Stay comfortable all year.", meta="From $129"),
        dict(img="1727893119356-1702fe921cf9", title="State inspection", text="Fast safety and emissions inspections, most done while you wait.", meta="$39"),
    ]), S)
    coupons = [("$20 OFF", "Any service over $150", "BF20"), ("FREE", "Brake inspection with photos", "BRAKES"), ("$49.95", "Synthetic blend oil change, up to 5 quarts", "OIL49")]
    cps = "".join(f'<div class="reveal relative rounded-xl border-2 border-dashed border-accent bg-white p-7 text-center">'
                  f'<p class="font-display text-6xl font-extrabold text-accent">{a}</p><p class="mt-2 font-semibold">{b}</p>'
                  f'<p class="mt-4 inline-block rounded-md bg-night text-white text-sm font-bold tracking-widest px-3 py-1.5">CODE {c}</p>'
                  f'<p class="mt-4 text-xs text-ink/50">Show this on your phone. Expires Dec 31. One per visit. Demo offer.</p></div>' for a, b, c in coupons)
    deals = section("deals", "bg-white", heading(S, "Coupons", "Save on your next visit") + f'<div class="mt-12 grid md:grid-cols-3 gap-6">{cps}</div>', S)
    status = (f'<div class="grid lg:grid-cols-2 gap-10 items-start"><div>{heading(S, "Repair status", "Where is my car?", "Enter the code from your drop-off text to see live progress. Try BF-1042 or BF-2077 in this demo.", dark=True)}'
              f'<form id="statusform" class="reveal mt-8 flex gap-2 max-w-md"><label class="sr-only" for="code">Repair code</label><input id="code" name="code" placeholder="BF-1042" class="flex-1 min-w-0 rounded-lg bg-white text-ink px-4 py-3 text-lg font-semibold uppercase tracking-wider"><button class="{t["btn"]}">Check</button></form>'
              f'<p id="statusmsg" class="mt-4 text-white/70" aria-live="polite"></p></div>'
              f'<div id="statusbox" class="reveal rounded-xl bg-night-800 border border-white/10 p-7 min-h-[300px]"><p class="text-white/50">Your repair timeline will appear here.</p></div></div>')
    statsec = section("status", "bg-night text-white", status, S)
    about = section("about", "bg-paper", split(S, "1618312980096-873bd19759a0",
        text_block(S, "Family owned since 1991", "The shop your neighbors trust", [
            "Tony Russo opened the shop with two bays and his father's toolbox. Today eight certified technicians work on everything from family SUVs to work trucks.",
            "Every car gets a digital inspection: photos and notes texted to you, so you see what we see and decide what gets done."]) +
        checks(S, ["Photos of every recommended repair", "Free loaner cars and local shuttle", "Comfortable waiting room with Wi-Fi and coffee"]),
        badge=f'<div class="absolute -bottom-6 right-4 sm:right-6 flex items-center gap-3 bg-white rounded-xl shadow-xl p-3 pr-5"><img src="{U("1568236700632-c0cfc08f486a", 200, 200)}" alt="Tony Russo" class="w-14 h-14 rounded-lg object-cover"><div><p class="font-bold text-sm">Tony Russo</p><p class="text-xs text-ink/60">Owner, master technician</p></div></div>'), S)
    revs = section("reviews", "bg-night text-white", heading(S, "Reviews", "Drivers who came back", dark=True) + reviews(S, [
        ("They texted me photos of my worn brake pads with the measurements. Fair price, done by lunch.", "Sample customer"),
        ("The dealer quoted $2,300. BF Auto Care found it was a $180 sensor. Honest people.", "Sample customer"),
        ("Free loaner car while they fixed my transmission. Didn't miss a single day of work.", "Sample customer"),
    ], dark=True), S)
    form = multistep(S, "estimate-form", [
        ("Your vehicle", inp(S, "Year, make &amp; model", "vehicle", req=True, ph="e.g. 2017 Honda CR-V", span=True) + inp(S, "Mileage", "miles", ph="e.g. 84,000", extra=' inputmode="numeric"')),
        ("What does it need?", chips(S, "needs", ["Oil change", "Brakes", "Tires", "Check engine light", "AC or heat", "Noise or vibration", "Inspection", "Not sure"], kind="checkbox", label="Select all that apply") +
         area(S, "Describe the problem (optional)", "notes", "e.g. squeal when braking, worse in the morning")),
        ("Drop-off &amp; contact", chips(S, "drop", ["Today", "Tomorrow", "This week"], req=True, label="When can you drop it off?") +
         inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") + consent(S)),
    ], "Get my estimate", "Request received", "Thanks, {name}! We'll text you an estimate for your {vehicle} and confirm drop-off {drop}.")
    book = form_section(S, "book", "Estimates &amp; booking", "Get a free estimate",
        "Tell us about your car. A service advisor texts you a price range and the first available time.",
        ["Estimate by text, usually within an hour", "You approve every repair before we start", "24-month / 24,000-mile warranty on parts and labor"], form, dark=False)
    vis = visit(S, "1764699186616-8f707281e4f3", "Visit", "On Route 30, next to the car wash",
                "Early drop-off box and key slot for after-hours drop-off.",
                [("Monday &ndash; Friday", "7:30 am &ndash; 6:00 pm"), ("Saturday", "8:00 am &ndash; 2:00 pm"), ("Sunday", "Closed")],
                "Free shuttle within 5 miles", f'<a href="#book" class="{t["btn_dark"]}">Book service</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>')
    fq = faq(S, [
        ("Do I need an appointment?", "For oil changes and inspections, walk-ins are welcome. For repairs, booking guarantees a technician is ready for your car."),
        ("Will servicing here void my factory warranty?", "No. Federal law lets you service your car anywhere. We use quality parts and keep records for your warranty."),
        ("What parts do you use?", "Original equipment or top-quality aftermarket parts, your choice. Both are covered by our 24/24 warranty."),
        ("Do you offer loaner cars?", "Yes, free for repairs that take more than a day, subject to availability. Book ahead to reserve one."),
        ("Can I pay over time?", "Yes. Repairs over $500 can be financed for 6 to 12 months, subject to approval."),
    ], bg="bg-white")
    S["mobile"] = mobile_bar(S, "Book service", "#book")
    js = r"""
const JOBS = {
  'BF-1042': { car: '2017 Honda CR-V', step: 3, eta: 'Today, 4:30 pm', notes: 'Front brake pads and rotors approved by text at 10:12 am.' },
  'BF-2077': { car: '2015 Ford F-150', step: 5, eta: 'Ready now', notes: 'Oil change, tire rotation and new wiper blades. Keys at the front desk.' }
};
const STEPS = ['Checked in', 'Inspected, photos sent', 'Repair approved', 'In the bay', 'Ready for pickup'];
$('#statusform').addEventListener('submit', e => {
  e.preventDefault();
  const code = $('#code').value.trim().toUpperCase().replace(/\s+/g, ''), j = JOBS[code], box = $('#statusbox');
  if (!j) { $('#statusmsg').textContent = 'We couldn\'t find that code. Try BF-1042 or BF-2077.'; return; }
  $('#statusmsg').textContent = '';
  box.innerHTML = `<p class="text-sm text-white/60">${esc(code)}</p><p class="font-display text-3xl font-bold uppercase mt-1">${esc(j.car)}</p>
    <p class="mt-1 text-accent font-semibold">${j.step === 5 ? 'Ready for pickup' : 'Estimated ready: ' + j.eta}</p>
    <ol class="mt-6 space-y-4">${STEPS.map((s, i) => `<li class="flex items-center gap-3"><span class="grid place-items-center w-7 h-7 rounded-full text-xs font-bold ${i < j.step ? 'bg-accent text-white' : 'border border-white/25 text-white/40'}">${i < j.step ? '&#10003;' : i + 1}</span><span class="${i < j.step ? 'text-white' : 'text-white/45'}">${s}</span></li>`).join('')}</ol>
    <p class="mt-6 text-sm text-white/70">${esc(j.notes)}</p>`;
});
"""
    body = hero + st + services + deals + statsec + about + revs + book + vis + fq
    return S, body, js


# =====================================================================  MED SPA
def medspa():
    S = setup(dict(
        slug="med-spa", name="BF Med Spa", kind="med spa", style="soft", header="light",
        tagline="Aesthetics &middot; Skin &middot; Wellness",
        description="Demo website for a medical spa: treatments with prices, membership plans, provider profiles, complimentary consultation booking. Built by BF Tech Lab.",
        og="1570172619644-dfd03ed5d881",
        fonts="family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;0,6..96,600;1,6..96,400;1,6..96,500&family=Manrope:wght@400;500;600;700",
        font_display=['"Bodoni Moda"', "Georgia", "serif"], font_sans=["Manrope", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#8a6a58", "50": "#f7f1ec", "100": "#efe4dc", "700": "#6f5444"},
                "accent": {"DEFAULT": "#d9c4a5", "600": "#b9a07c"},
                "night": {"DEFAULT": "#2a2320", "800": "#352d29", "700": "#463c37"},
                "ink": "#2a2320", "paper": "#fbf8f4", "line": "#ece2d6"},
        tokens=dict(h1="font-display font-normal leading-[1.05] text-5xl sm:text-6xl lg:text-7xl",
                    h2="font-display text-4xl sm:text-5xl font-normal leading-[1.08]",
                    h3="font-display text-2xl font-normal leading-snug"),
        banner_cls="bg-night text-white/90", accent_ink="text-night",
        phone="(555) 555-0115", tel="+15555550115",
        address="8 Willow Court, Suite 210<br>Brookside, PA 00000",
        nav=[("Treatments", "#treatments"), ("Membership", "#membership"), ("Providers", "#team"), ("Consultation", "#book"), ("Visit", "#visit")],
        cta=("Free consultation", "#book"),
        footer_note="Treatments are performed by licensed medical professionals under the supervision of a medical director. Individual results vary.",
    ))
    t = S["t"]
    hero = hero_split(S, "1570172619644-dfd03ed5d881", "1782931684641-39b88b348e1e", "Complimentary consultations",
        'Natural results. <em class="text-brand">Expert hands.</em>',
        "Wrinkle relaxers, fillers, facials, laser and skin treatments by licensed medical providers, planned around you in a calm, private space.",
        f'<a href="#book" class="{t["btn"]}">Book a free consultation</a><a href="#treatments" class="{t["btn_line"]}">View treatments</a>',
        [("Treatments done", "12,000+"), ("Injectors", "Nurse &amp; NP"), ("Google rating", "4.9&#9733;")],
        "Consultations this week: Thu &amp; Sat", "Tell us your goals and get an honest plan, with no pressure to book.")
    treat = section("treatments", "bg-white", heading(S, "Treatments", "Look rested, not different", "Every plan starts with a consultation. Prices are starting points; your provider confirms before treatment.") + photo_cards(S, [
        dict(img="1555820585-c5ae44394b79", title="Wrinkle relaxers", text="Soften forehead lines, frown lines and crow's feet while keeping your natural expression.", meta="From $12 per unit"),
        dict(img="1761718209708-9ab9ba1c7252", title="Dermal fillers", text="Restore volume to lips, cheeks and under-eyes with subtle, balanced results.", meta="From $650 per syringe"),
        dict(img="1731514771613-991a02407132", title="Signature facials", text="Deep cleansing, exfoliation and hydration. You walk out glowing, with zero downtime.", meta="From $145"),
        dict(img="1700760933574-9f0f4ea9aa3b", title="Laser hair removal", text="Smooth skin on any area, with a laser that is safe for every skin tone.", meta="From $99 per session"),
        dict(img="1573461160327-b450ce3d8e7f", title="Chemical peels", text="Even out tone, fade sun spots and refine texture, from light to medium depth.", meta="From $175"),
        dict(img="1585945037805-5fd82c2e60b1", title="Microneedling", text="Collagen induction to smooth acne scars and fine lines, with optional PRP.", meta="From $325"),
    ]), S)
    plans = [("Glow", 99, ["One signature facial every month", "10% off injectables and peels", "Member pricing on product"], False),
             ("Radiance", 179, ["One signature facial or peel monthly", "$100 injectables credit every quarter", "15% off all treatments", "Priority booking"], True)]
    pc = "".join(
        f'<div class="reveal relative rounded-3xl {"bg-night text-white" if hot else "bg-white border border-line"} p-8 sm:p-10 flex flex-col">'
        f'{"<span class=&quot;absolute -top-3 left-8 rounded-full bg-accent text-night text-xs font-semibold uppercase tracking-wider px-3 py-1&quot;>Most loved</span>" if hot else ""}'
        f'<p class="font-display text-4xl">{n}</p><p class="mt-4"><span class="font-display text-6xl">${p}</span><span class="{"text-white/60" if hot else "text-ink/60"}"> /month</span></p>'
        f'{checks(S, f, dark=hot, cls="mt-6 space-y-3 flex-1")}<a href="#book" class="{t["btn_accent"] if hot else t["btn"]} w-full mt-8">Join after your consultation</a></div>'
        for n, p, f, hot in plans).replace("&quot;", '"')
    member = section("membership", "bg-paper", f'<div class="grid lg:grid-cols-5 gap-10 items-center"><div class="lg:col-span-2">{heading(S, "Membership", "Your skin, on a schedule", "Consistent care gives the best results. Members save on every visit and can cancel any time after three months.")}</div>'
                     f'<div class="lg:col-span-3 grid sm:grid-cols-2 gap-6">{pc}</div></div>', S)
    exp = section("experience", "bg-white", split(S, "1759262151080-e05ba1c6294f",
        text_block(S, "The experience", "A calm, private space", [
            "Private treatment rooms, numbing for comfort and a follow-up check-in after every injectable appointment.",
            "Our medical director reviews every treatment plan, and your provider takes before-and-after photos so you can see your progress."]) +
        checks(S, ["Licensed nurse and NP injectors", "Medical director oversight", "Free two-week touch-up check"]),
        reverse=True), S)
    team_s = section("team", "bg-paper", heading(S, "Providers", "Meet your providers") + team(S, [
        ("1758600587391-338f5376b7ed", "Nina Park, NP-C", "Nurse practitioner &middot; Lead injector", "Ten years in aesthetic medicine. Known for natural lip and cheek work and very honest advice."),
        ("1765005204058-10418f5123c5", "Danielle Brooks, RN", "Aesthetic nurse", "Wrinkle relaxers and skin boosters. Patients love her gentle technique and steady hands."),
        ("1758691737605-69a0e78bd193", "Mei Chen, LE", "Licensed esthetician", "Facials, peels and laser treatments, with a focus on acne and sensitive skin."),
    ]), S)
    form = multistep(S, "consult-form", [
        ("What are you interested in?", chips(S, "interest", ["Wrinkle relaxers", "Fillers", "Facials", "Laser hair removal", "Peels", "Microneedling", "Not sure yet"], kind="checkbox", label="Select all that apply") +
         area(S, "Your goals (optional)", "goals", "e.g. look less tired, smoother skin before my wedding in June")),
        ("A little about you", chips(S, "before", ["Yes", "No"], req=True, label="Have you had aesthetic treatments before?", span=False) +
         chips(S, "when", ["Weekday daytime", "Weekday evening", "Saturday"], req=True, label="Best time for a consultation", span=False)),
        ("Your details", inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
         inp(S, "Email", "email", "email", ac="email", span=True) + consent(S)),
    ], "Request consultation", "Thank you", "Thank you, {name}. Our patient coordinator will call to book your complimentary consultation.")
    book = form_section(S, "book", "Free consultation", "Start with a conversation",
        "Twenty minutes with a provider to talk through your goals, options and costs. No obligation to book a treatment.",
        ["Complimentary and no-pressure", "Personalized plan with clear prices", "Same-day treatment available if you choose"], form)
    revs = section("reviews", "bg-white", heading(S, "Reviews", "Kind words from clients") + reviews(S, [
        ("Nina talked me out of more filler than I needed. The result is so natural my friends just say I look rested.", "Sample client"),
        ("The calmest spa I've ever been to. My skin has never looked better since starting the Glow membership.", "Sample client"),
        ("Laser hair removal on darker skin, done safely and with real care. Six sessions in and I'm thrilled.", "Sample client"),
    ]), S)
    vis = visit(S, "1761971976407-db2374e4ae12", "Visit", "Find us at Willow Court",
                "Second floor, elevator access, free parking in the courtyard.",
                [("Monday", "Closed"), ("Tuesday &ndash; Friday", "10:00 am &ndash; 7:00 pm"), ("Saturday", "9:00 am &ndash; 4:00 pm"), ("Sunday", "Closed")],
                "Private treatment rooms", f'<a href="#book" class="{t["btn"]}">Free consultation</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>')
    fq = faq(S, [
        ("Is the consultation really free?", "Yes. It's a 20-minute appointment with a provider, with no charge and no obligation to book a treatment."),
        ("Does it hurt?", "Most treatments are very comfortable. We use numbing cream and ice for injectables and tell you what to expect at every step."),
        ("How much downtime should I expect?", "Facials and wrinkle relaxers have none. Fillers and peels may cause mild redness or swelling for a day or two."),
        ("Who performs the treatments?", "Licensed nurses, nurse practitioners and estheticians, under the supervision of our medical director."),
        ("Do you offer payment plans?", "Yes, we offer monthly payment options for larger treatment plans, subject to approval."),
    ], bg="bg-paper")
    S["mobile"] = mobile_bar(S, "Free consultation", "#book")
    body = hero + treat + member + exp + team_s + book + revs + vis + fq
    return S, body, ""


SITES = [vet, chiro, auto, medspa]
