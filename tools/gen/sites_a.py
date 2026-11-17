# -*- coding: utf-8 -*-
"""Demo sites: restaurant, plumbing, roofing, landscaping."""
from lib import *


# =====================================================================  RESTAURANT
def restaurant():
    S = setup(dict(
        slug="restaurant", name="BF Trattoria", kind="restaurant", style="soft", header="dark",
        tagline="Handmade pasta &middot; Wood-fired pizza",
        description="Demo website for an independent Italian restaurant: menu with tabs, online table requests, private events. Built by BF Tech Lab.",
        og="1774509625509-8c452b51649e",
        fonts="family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Manrope:wght@400;500;600;700",
        font_display=["Cormorant Garamond", "Georgia", "serif"], font_sans=["Manrope", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#a8492b", "50": "#faf0ea", "100": "#f3e1d6", "700": "#8a3a21"},
                "accent": {"DEFAULT": "#d9a441", "600": "#c38e2c"},
                "night": {"DEFAULT": "#16110e", "800": "#211a16", "700": "#2d241f"},
                "ink": "#231a15", "paper": "#f8f3ec", "line": "#e8dccd"},
        tokens=dict(h1="font-display font-semibold leading-[1.02] text-5xl sm:text-6xl lg:text-7xl",
                    h2="font-display text-4xl sm:text-5xl font-semibold leading-[1.05]",
                    h3="font-display text-2xl font-semibold leading-snug"),
        banner_cls="bg-brand text-white/95", accent_ink="text-night",
        phone="(555) 555-0140", tel="+15555550140",
        address="212 Main Street<br>Brookside, PA 00000",
        nav=[("Menu", "#menu"), ("Reservations", "#reserve"), ("Private events", "#events"), ("Our story", "#story"), ("Visit", "#visit")],
        cta=("Book a table", "#reserve"),
    ))
    t = S["t"]
    times = ["5:00 pm", "5:30 pm", "6:00 pm", "6:30 pm", "7:00 pm", "7:30 pm", "8:00 pm", "8:30 pm", "9:00 pm", "9:30 pm"]
    guests = [("2", "2 guests"), ("1", "1 guest"), ("3", "3 guests"), ("4", "4 guests"), ("5", "5 guests"), ("6", "6 guests"), ("7", "7 guests"), ("8", "8 guests")]
    quick = f'''<form id="quick" class="bg-paper text-ink rounded-2xl p-6 shadow-2xl">
  <p class="font-display text-3xl">Reserve a table</p>
  <p class="text-sm text-ink/60 mt-1">Tonight's last openings go fast.</p>
  <div class="mt-5 grid grid-cols-2 gap-3">
    <label class="col-span-2 text-xs font-semibold">Date<input type="date" name="qdate" class="mt-1 w-full {t["input"]}"></label>
    <label class="text-xs font-semibold">Time<select name="qtime" class="mt-1 w-full {t["input"]}">{"".join(f"<option>{x}</option>" for x in times)}</select></label>
    <label class="text-xs font-semibold">Guests<select name="qguests" class="mt-1 w-full {t["input"]}">{"".join(f'<option value="{a}">{b}</option>' for a, b in guests)}</select></label>
  </div>
  <button class="{t["btn_accent"]} w-full mt-5">Find a table</button>
  <p class="mt-3 text-xs text-ink/60">Parties of 9 or more: please call us.</p>
</form>'''
    hero = hero_full(S, "1774509625509-8c452b51649e",
                     "Since 2009 &middot; Downtown Brookside",
                     'Pasta rolled every morning. <em class="text-accent">Pizza from the wood fire.</em>',
                     "A neighborhood trattoria with a short menu, a long wine list and tables that fill up fast on Fridays. Book online in thirty seconds.",
                     f'<a href="#reserve" class="{t["btn_accent"]}">Book a table</a><a href="#menu" class="{t["btn_line_d"]}">View the menu</a>',
                     side=quick, points=["Open Tuesday to Sunday", "Lunch Friday to Sunday", "Takeout &amp; delivery"], opacity="opacity-70")

    known = section("", "bg-paper", heading(S, "What we're known for", "Simple Italian food, made from scratch every day") + photo_cards(S, [
        dict(img="1611270629569-8b357cb88da9", title="Pasta made daily", text="Pappardelle, rigatoni and ravioli rolled by hand every morning, never dried, never frozen."),
        dict(img="1622880833523-7cf1c0bd4296", title="A 900&deg; wood oven", text="Neapolitan-style pizza in ninety seconds, with a 48-hour dough and San Marzano tomatoes."),
        dict(img="1597290282695-edc43d0e7129", title="120 Italian wines", text="From easy reds by the glass to bottles for a celebration, picked by our sommelier."),
    ]), S)

    def panel(img, items, pos="object-center"):
        return (f'<div class="grid lg:grid-cols-5 gap-10 items-start"><div class="lg:col-span-3">{price_list(S, items, cols=1)}</div>'
                f'<div class="lg:col-span-2 lg:sticky lg:top-24"><img src="{U(img, 800)}" alt="" loading="lazy" class="w-full aspect-[4/5] object-cover {pos} rounded-3xl shadow-xl"></div></div>')
    menu_tabs = tabs(S, [
        ("antipasti", "Antipasti", panel("1572715376701-98568319fd0b", [
            ("Burrata &amp; heirloom tomatoes", "Basil oil, sea salt, grilled sourdough", "$16", "V"),
            ("Fried calamari", "Lemon aioli, Calabrian chili", "$15"),
            ("Meatballs al forno", "Sunday sauce, ricotta, focaccia", "$14"),
            ("Arancini", "Saffron risotto, mozzarella, pomodoro", "$12", "V"),
            ("Tuscan kale salad", "Pecorino, lemon, toasted breadcrumbs", "$13", "V"),
        ])),
        ("pasta", "Pasta", panel("1766706519060-d44bd9dc50f7", [
            ("Pappardelle bolognese", "Slow-cooked beef &amp; pork ragù, parmigiano", "$24"),
            ("Cacio e pepe", "Tonnarelli, pecorino romano, black pepper", "$19", "V"),
            ("Pesto genovese", "Trofie, basil, pine nuts, green beans", "$21", "V"),
            ("Lobster ravioli", "Brown butter, sage, lemon zest", "$32"),
            ("Rigatoni alla vodka", "Tomato, cream, Calabrian chili", "$22", "V"),
            ("Mushroom risotto", "Carnaroli rice, porcini, thyme", "$24", "V GF"),
        ])),
        ("pizza", "Pizza", panel("1579751626657-72bc17010498", [
            ("Margherita", "San Marzano, fior di latte, basil", "$17", "V"),
            ("Diavola", "Spicy salami, mozzarella, hot honey", "$20"),
            ("Funghi", "Wild mushrooms, fontina, truffle oil", "$20", "V"),
            ("Prosciutto &amp; arugula", "Prosciutto di Parma, shaved parmigiano", "$22"),
            ("Gluten-free crust", "Any pizza, baked on its own tray", "+$3", "GF"),
        ])),
        ("mains", "Mains", panel("1767065584562-0127cdec486d", [
            ("Chicken parmigiana", "Hand-breaded, spaghetti pomodoro", "$28"),
            ("Branzino", "Whole roasted, lemon, capers, olives", "$34", "GF"),
            ("Braised short rib", "Barolo sauce, creamy polenta", "$36", "GF"),
            ("Eggplant parmigiana", "Layers of eggplant, ricotta, basil", "$24", "V"),
        ])),
        ("dolci", "Dolci", panel("1714385905983-6f8e06fffae1", [
            ("Tiramisu", "Mascarpone, espresso, cocoa", "$10", "V"),
            ("Panna cotta", "Vanilla bean, macerated berries", "$9", "V GF"),
            ("Cannoli", "Two shells, ricotta, pistachio", "$8", "V"),
            ("Affogato", "Vanilla gelato, hot espresso", "$8", "V GF"),
        ])),
        ("drinks", "Drinks", panel("1547595628-c61a29f496f0", [
            ("Aperol spritz", "Aperitivo, prosecco, orange", "$13"),
            ("Negroni", "Gin, vermouth, bitter", "$14"),
            ("House red or white", "By the glass", "$11"),
            ("Italian sodas", "Blood orange, lemon, chinotto", "$5"),
            ("Espresso / cappuccino", "", "$4 / $5"),
        ])),
    ])
    menu = section("menu", "bg-white", heading(S, "The menu", "Short menu. Everything made here.",
                   "Our menu follows the season. Tell us about allergies when you book and the kitchen will take care of you.") +
                   f'<div class="reveal mt-10">{menu_tabs}</div><p class="mt-6 text-sm text-ink/55">V vegetarian &middot; GF gluten-free &middot; Prices are examples for this demo.</p>', S)

    story = section("story", "bg-paper", split(S, "1689588532679-4bb5fdd8f6d5",
        text_block(S, "Our story", "Chef Marco and a family recipe book", [
            "Marco Rinaldi learned to roll pasta next to his grandmother in Bologna. In 2009 he opened BF Trattoria with twelve tables and the same recipes.",
            "Today the room is bigger, but the rules are the same: flour from a family mill, tomatoes from a farm ten miles away, and nothing on the menu we wouldn't serve at home."]) +
        checks(S, ["Pasta and bread made fresh every morning", "Local produce from May to October", "Wine list built for every budget"]),
        pos="object-top"), S)

    events = section("events", "bg-night text-white", split(S, "1712630514718-3830cc6c0d0a",
        text_block(S, "Private events", "Birthdays, rehearsal dinners and team nights", [
            "Book the back room for 12 to 40 guests, or the whole restaurant for up to 90. Set menus start at $55 per person, with wine pairings available."], dark=True) +
        checks(S, ["Family-style or plated set menus", "Microphone and screen for toasts", "Dedicated host for the evening"], dark=True) +
        f'<a href="#reserve" data-occasion="Private event" class="{t["btn_accent"]} mt-8">Plan an event</a>', reverse=True), S)

    gal = section("gallery", "bg-white", heading(S, "From our kitchen", "A look inside") + gallery(S, [
        ("1776362441386-c02107b86576", "Friday night in the dining room"), ("1621996346565-e3dbc646d9a9", "Rigatoni alla vodka"),
        ("1787550275377-9f54a07c68c8", "Panna cotta with berries"), ("1786209677036-1580ca1b280d", "Set for a private dinner"),
        ("1579992357154-faf4bde95b3d", "Espresso to finish"), ("1761095596591-a56b0296c190", "Plating in the open kitchen"),
    ]), S)

    revs = section("reviews", "bg-paper", heading(S, "Guests say", "The kind of place you come back to") + reviews(S, [
        ("Best cacio e pepe outside of Rome, and I've been to Rome. Booked online at lunch for that night.", "Sample guest"),
        ("We did my parents' 40th in the back room. The set menu was perfect and the staff made it feel special.", "Sample guest"),
        ("Gluten-free pizza that actually tastes like pizza. My daughter was thrilled.", "Sample guest"),
    ]), S)

    form = demo_form(S, "reserve-form",
        inp(S, "Date", "date", "date", req=True) +
        sel(S, "Time", "time", times, req=True) +
        sel(S, "Guests", "guests", guests, req=True) +
        sel(S, "Occasion", "occasion", ["None", "Birthday", "Anniversary", "Business dinner", "Private event"]) +
        inp(S, "Your name", "name", req=True, ac="name") +
        inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
        inp(S, "Email (optional)", "email", "email", ac="email", span=True) +
        area(S, "Anything we should know?", "notes", "Allergies, high chair, a table by the window...") +
        consent(S, "Text me to confirm my reservation."),
        "Request this table",
        "Grazie, {name}! Your request for {guests} guests on {date} at {time} is in. We'll text you a confirmation within 15 minutes.",
        cls="rounded-3xl bg-paper text-ink p-6 sm:p-8 shadow-2xl", btn=t["btn"])
    reserve = form_section(S, "reserve", "Reservations", "Book your table",
        "Choose a time and we'll text you to confirm. Can't find a slot? Call us; we often have room at the bar.",
        ["Confirmation by text within 15 minutes", "Tables held for 15 minutes after booking time", "Parties of 9 or more: please call"], form,
        after=f'<p class="mt-8 text-white/70">Prefer to call? <a href="tel:{S["tel"]}" class="font-semibold text-accent">{S["phone"]}</a></p>')

    vis = visit(S, "1517248135467-4c7edcad34c4", "Visit", "Find us on Main Street",
                "Street parking and a free lot behind the building after 5 pm.",
                [("Monday", "Closed"), ("Tuesday &ndash; Thursday", "4:30 &ndash; 9:30 pm"), ("Friday", "11:30 am &ndash; 10:30 pm"),
                 ("Saturday", "11:30 am &ndash; 10:30 pm"), ("Sunday", "11:30 am &ndash; 8:30 pm")],
                "Walk-ins welcome at the bar", f'<a href="#reserve" class="{t["btn"]}">Book a table</a><a href="tel:{S["tel"]}" class="{t["btn_line"]}">Call {S["phone"]}</a>')
    fq = faq(S, [
        ("Do you take walk-ins?", "Yes. The bar and four high-tops are kept for walk-ins every night, first come, first served."),
        ("Do you have gluten-free options?", "Gluten-free pasta and pizza crust are available, cooked separately. Tell us about any allergy when you book."),
        ("Is there a kids' menu?", "Yes: small pasta, mini pizzas and gelato. High chairs and booster seats are available."),
        ("Can I order takeout?", "Order by phone or online for pickup, or through the usual delivery apps within 5 miles."),
        ("Do you sell gift cards?", "Yes, at the host stand and online, in any amount."),
    ])
    S["mobile"] = mobile_bar(S, "Book a table", "#reserve")
    js = r"""
const q = $('#quick');
if (q) q.addEventListener('submit', e => {
  e.preventDefault();
  const f = $('#reserve-form');
  const qv = n => q.elements.namedItem(n).value;
  if (qv('qdate')) f.elements.namedItem('date').value = qv('qdate');
  f.elements.namedItem('time').value = qv('qtime');
  f.elements.namedItem('guests').value = qv('qguests');
  $('#reserve').scrollIntoView({ behavior: 'smooth' });
  setTimeout(() => f.elements.namedItem('name').focus({ preventScroll: true }), 700);
});
$$('[data-occasion]').forEach(a => a.addEventListener('click', () => { $('#reserve-form').elements.namedItem('occasion').value = a.dataset.occasion; }));
"""
    body = hero + known + menu + story + events + gal + revs + reserve + vis + fq
    return S, body, js


# =====================================================================  PLUMBING
def plumbing():
    S = setup(dict(
        slug="plumbing", name="BF Plumbing", kind="plumbing company", style="bold", header="dark",
        tagline="Plumbing &middot; Drains &middot; Water heaters",
        description="Demo website for a local plumbing company: same-day call-back form, upfront price guide, service-area checker, online booking. Built by BF Tech Lab.",
        og="1676210133055-eab6ef033ce3",
        fonts="family=Archivo:wght@500;600;700;800&family=Inter:wght@400;500;600;700",
        font_display=["Archivo", "Impact", "sans-serif"], font_sans=["Inter", "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#1565c0", "50": "#eef5fd", "100": "#dbe9fb", "700": "#0d4f9a"},
                "accent": {"DEFAULT": "#ffc233", "600": "#d99a00"},
                "night": {"DEFAULT": "#0b1a2c", "800": "#11243b", "700": "#1b324f"},
                "ink": "#0b1a2c", "paper": "#f3f6fa", "line": "#d9e2ec"},
        tokens=dict(h1="font-display font-extrabold uppercase leading-[.95] tracking-tight text-5xl sm:text-6xl lg:text-7xl",
                    h2="font-display text-4xl sm:text-5xl font-extrabold uppercase leading-[1.0] tracking-tight",
                    h3="font-display text-xl font-extrabold uppercase leading-tight"),
        banner_cls="bg-accent text-night font-medium", accent_ink="text-night",
        phone="(555) 555-0150", tel="+15555550150",
        address="88 Industrial Way, Unit 4<br>Brookside, PA 00000",
        nav=[("Services", "#services"), ("Prices", "#prices"), ("Service area", "#area"), ("Reviews", "#reviews"), ("Contact", "#visit")],
        cta=("Book online", "#book"),
        header_extra='<span class="hidden sm:inline-flex items-center gap-1.5 rounded-full bg-red-500/15 text-red-300 text-xs font-bold uppercase tracking-wider px-3 py-1.5"><span class="w-2 h-2 rounded-full bg-red-400 animate-pulse"></span>24/7</span>',
    ))
    t = S["t"]
    side = demo_form(S, "callback",
        f'<p class="sm:col-span-2 font-display text-2xl font-extrabold uppercase">Get a plumber today</p>' +
        chips(S, "issue", ["Leak or burst pipe", "Clogged drain", "Water heater", "Toilet", "Something else"], req=True, label="What's going on?") +
        inp(S, "ZIP code", "zip", req=True, ph="e.g. 19020", extra=' inputmode="numeric" maxlength="5"') +
        inp(S, "Mobile number", "phone", "tel", req=True, ac="tel"),
        "Call me back", "Thanks! A dispatcher will call you within 15 minutes about your {issue}.",
        cls="bg-white text-ink rounded-xl p-6 shadow-2xl", note="Average call-back: 9 minutes")
    hero = hero_full(S, "1676210133055-eab6ef033ce3", "Licensed &amp; insured &middot; Family owned since 2006",
        'Leak? Clog? No hot water? <span class="text-accent">We\'re on the way.</span>',
        "Same-day plumbing for homes around Brookside. You get the price before we start, a clean, uniformed plumber and a 1-year warranty on every repair.",
        f'<a href="tel:{S["tel"]}" class="{t["btn"]}">{PHONE_ICON} Call {S["phone"]}</a><a href="#book" class="{t["btn_line_d"]}">Book online</a>',
        side=side, points=["Upfront prices", "No extra charge on Saturdays", "1-year warranty"], pos="object-center", opacity="opacity-50")
    st = stats(S, [("4.9&#9733;", "Average rating (sample)"), ("12,000+", "Jobs completed"), ("60 min", "Average arrival time"), ("1 year", "Warranty on labor")])
    services = section("services", "bg-paper", heading(S, "Services", "Fixed right the first time", "Every truck carries the parts for 90% of repairs, so most jobs are finished in one visit.") + photo_cards(S, [
        dict(img="1542013936693-884638332954", title="Leaks &amp; pipe repair", text="Dripping faucets, burst pipes, slab leaks. We find it fast and fix it without tearing up your home.", meta="From $149"),
        dict(img="1565538810643-b5bdb714032a", title="Drain cleaning", text="Kitchen, bath and main lines cleared with professional cable and hydro-jetting equipment.", meta="From $129"),
        dict(img="1620653713380-7a34b773fef8", title="Water heaters", text="Repairs, flushes and same-day replacement of tank and tankless water heaters.", meta="Repairs from $189 &middot; installs from $1,450"),
        dict(img="1584622650111-993a426fbf0a", title="Toilets &amp; faucets", text="Running toilets, low pressure, new fixtures. We haul the old ones away.", meta="From $119"),
        dict(img="1650551182991-b07558247564", title="Sewer &amp; camera inspection", text="See inside your pipes on video before you spend a dollar on digging.", meta="From $199"),
        dict(img="1781344334901-cfd593c38145", title="Bathroom remodels", text="Showers, tubs and vanities, from rough-in to the last bead of caulk.", meta="Free estimate"),
    ]), S)
    rows = [("Drain cleaning (sink or tub)", "$129 &ndash; $249", "about 1 hour"), ("Faucet replacement", "$189 &ndash; $349", "1 &ndash; 2 hours"),
            ("Toilet repair", "$119 &ndash; $249", "about 1 hour"), ("Water heater flush", "$129", "45 minutes"),
            ("Garbage disposal install", "$249 &ndash; $399", "1 &ndash; 2 hours"), ("Water heater replacement (40&ndash;50 gal)", "$1,450 &ndash; $2,100", "half a day")]
    trs = "".join(f'<tr class="border-b border-line"><td class="py-3.5 pr-4 font-semibold">{a}</td><td class="py-3.5 pr-4 whitespace-nowrap">{b}</td><td class="py-3.5 text-ink/60 hidden sm:table-cell">{c}</td></tr>' for a, b, c in rows)
    prices = section("prices", "bg-white",
        f'<div class="grid lg:grid-cols-5 gap-10 items-start"><div class="lg:col-span-3">{heading(S, "Upfront price guide", "Know the price before we pick up a wrench")}'
        f'<div class="reveal mt-8 overflow-x-auto"><table class="w-full text-sm"><thead><tr class="text-left text-xs uppercase tracking-wider text-ink/50 border-b-2 border-ink"><th class="py-3 pr-4">Job</th><th class="py-3 pr-4">Typical price</th><th class="py-3 hidden sm:table-cell">Time on site</th></tr></thead><tbody>{trs}</tbody></table></div>'
        f'<p class="mt-4 text-xs text-ink/50">Example prices for this demo. Your plumber confirms the exact price before starting.</p></div>'
        f'<div class="reveal lg:col-span-2 rounded-xl bg-night text-white p-7"><p class="{t["eyebrow_d"]}">Home Club membership</p><p class="font-display text-4xl font-extrabold mt-2">$14<span class="text-lg text-white/60">/month</span></p>'
        f'{checks(S, ["No trip fees, ever", "15% off every repair", "Yearly plumbing inspection", "Priority scheduling, even on weekends"], dark=True)}'
        f'<a href="#book" class="{t["btn"]} w-full mt-7">Join when you book</a></div></div>', S)
    towns = ["Brookside", "Millbrook", "Oak Ridge", "Cedar Falls", "Riverton", "Fairview", "Lakewood", "Hillcrest"]
    town_html = "".join(f'<span class="rounded-md border border-white/15 px-3 py-1.5 text-sm text-white/80">{x}</span>' for x in towns)
    area_html = (f'<div class="grid lg:grid-cols-2 gap-10 items-center"><div>{heading(S, "Service area", "Do we cover your street?", "Enter your ZIP code. We serve homes within 25 miles of Brookside, with no travel charge.", dark=True)}'
                 f'<div class="reveal mt-6 flex flex-wrap gap-2">{town_html}</div></div>'
                 f'<form id="zipcheck" class="reveal rounded-xl bg-night-800 border border-white/10 p-6 sm:p-8"><label class="block text-sm font-semibold">Your ZIP code'
                 f'<div class="mt-2 flex gap-2"><input name="zip" inputmode="numeric" maxlength="5" placeholder="e.g. 19020" class="flex-1 min-w-0 rounded-lg bg-white text-ink px-4 py-3 text-lg font-semibold">'
                 f'<button class="{t["btn"]}">Check</button></div></label><p id="zipout" class="mt-5 text-lg text-white/80" aria-live="polite">We usually arrive within 60 minutes.</p></form></div>')
    areasec = section("area", "bg-night text-white", area_html, S)
    about = section("about", "bg-paper", split(S, "1749532125405-70950966b0e5",
        text_block(S, "Who shows up", "Plumbers you'd let in with the kids at home", [
            "Marcus Hill started BF Plumbing in 2006 with one van and a promise: show up on time, explain the options, leave the house cleaner than you found it.",
            "Today 14 licensed plumbers work from our Brookside shop. Every one of them is background-checked, trained in-house and paid by the hour, not by the upsell."]) +
        checks(S, ["Text with photo and name before arrival", "Shoe covers and drop cloths on every job", "Licensed master plumbers on every team"]),
        badge=f'<div class="absolute -bottom-6 -right-2 sm:right-6 flex items-center gap-3 bg-white rounded-xl shadow-xl p-3 pr-5"><img src="{U("1522529599102-193c0d76b5b6", 200, 200)}" alt="Marcus Hill" class="w-14 h-14 rounded-lg object-cover"><div><p class="font-bold text-sm">Marcus Hill</p><p class="text-xs text-ink/60">Owner, master plumber</p></div></div>'), S)
    how = section("how", "bg-white", heading(S, "How it works", "Four steps, no surprises") + steps(S, [
        ("Call or book", "A real person answers 24/7. Most calls get a same-day arrival window."),
        ("Price first", "Your plumber diagnoses the problem and gives you a written price before any work."),
        ("Fixed &amp; cleaned up", "We protect floors, finish the job and take the old parts away."),
        ("1-year warranty", "If the same problem comes back within a year, so do we, at no charge."),
    ]), S)
    revs = section("reviews", "bg-night text-white", heading(S, "Reviews", "Neighbors who called us", dark=True) + reviews(S, [
        ("Water heater died on a Sunday morning. They had a new one in by 2 pm and the price was exactly what they quoted.", "Sample customer"),
        ("He showed me the camera video of the drain before doing anything. Honest, fast and tidy.", "Sample customer"),
        ("Booked online at 11 pm, got a call at 7:30 the next morning. Leak fixed before I left for work.", "Sample customer"),
    ], dark=True), S)
    book = multistep(S, "booking", [
        ("What do you need?", chips(S, "service", ["Leak or burst pipe", "Clogged drain", "Water heater", "Toilet", "Faucet or fixture", "Remodel estimate", "Other"], req=True) +
         area(S, "Tell us more (optional)", "details", "e.g. water under the kitchen sink since this morning")),
        ("When works for you?", chips(S, "when", ["As soon as possible", "Today", "Tomorrow", "This week"], req=True, label="Day") +
         chips(S, "slot", ["Morning (8&ndash;12)", "Afternoon (12&ndash;4)", "Evening (4&ndash;8)"], req=True, label="Arrival window")),
        ("Your details", inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
         inp(S, "Street address or ZIP", "address", req=True, ac="street-address", span=True) + consent(S)),
    ], "Send request", "Request received", "Thanks, {name}! We'll call you within 15 minutes to confirm your arrival window for {when}.")
    booksec = form_section(S, "book", "Book online", "Book a plumber in under a minute",
        "Pick what you need and when. We call to confirm the arrival window and the price range before we head out.",
        ["A real person calls you back, never a robot", "Arrival windows of 2 hours, with a text when we're on the way", "Emergency? Call us now: we answer 24/7"], book,
        after=f'<a href="tel:{S["tel"]}" class="{t["btn"]} mt-8">{PHONE_ICON} {S["phone"]}</a>')
    vis = visit(S, "1771627278637-10eb2e9857b5", "Contact", "Office &amp; dispatch",
                "Emergencies are answered 24 hours a day, 7 days a week.",
                [("Monday &ndash; Friday", "7:00 am &ndash; 7:00 pm"), ("Saturday", "8:00 am &ndash; 4:00 pm"), ("Sunday", "Emergency calls only"), ("Phone line", "24/7")],
                "Serving homes within 25 miles of Brookside", f'<a href="tel:{S["tel"]}" class="{t["btn_dark"]}">Call {S["phone"]}</a><a href="#book" class="{t["btn_line"]}">Book online</a>')
    fq = faq(S, [
        ("Do you charge a trip fee?", "There's a $49 diagnostic fee, which is waived if you go ahead with the repair. Home Club members never pay it."),
        ("Are your plumbers licensed?", "Yes. Every team is led by a licensed master plumber, and the company is fully insured."),
        ("Do you charge more on weekends?", "Saturdays are the same price as weekdays. Nights, Sundays and holidays have a flat $95 emergency fee."),
        ("Can I pay over time?", "Yes. Water heaters and bigger jobs can be financed over 12 to 60 months, subject to approval."),
        ("What does the warranty cover?", "Labor on every repair for one year. New water heaters also carry the manufacturer's 6 to 12-year tank warranty."),
    ], bg="bg-white")
    S["mobile"] = mobile_bar(S, "Book online", "#book")
    js = r"""
const zc = $('#zipcheck');
if (zc) zc.addEventListener('submit', e => {
  e.preventDefault();
  const z = zc.elements.namedItem('zip').value.trim(), out = $('#zipout');
  if (!/^\d{5}$/.test(z)) { out.textContent = 'Please enter a 5-digit ZIP code.'; return; }
  out.innerHTML = /^(19|18)/.test(z)
    ? `<strong class="text-accent">Yes, we serve ${esc(z)}.</strong> Next opening: today, 2&ndash;4 pm. <a href="#book" class="underline">Book it</a>`
    : `We may not cover ${esc(z)} yet. <a href="tel:+15555550150" class="underline text-accent">Call us</a> and we'll check right away.`;
});
"""
    body = hero + st + services + prices + areasec + about + how + revs + booksec + vis + fq
    return S, body, js


# =====================================================================  ROOFING
def roofing():
    S = setup(dict(
        slug="roofing", name="BF Roofing", kind="roofing company", style="bold", header="dark",
        tagline="Roof replacement &middot; Repairs &middot; Storm damage",
        description="Demo website for a local roofing contractor: free inspection requests, roof cost estimator, project gallery. Built by BF Tech Lab.",
        og="1635424709845-3a85ad5e1f5e",
        fonts="family=Oswald:wght@500;600;700&family=Source+Sans+3:wght@400;600;700",
        font_display=["Oswald", "Impact", "sans-serif"], font_sans=['"Source Sans 3"', "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#d9502b", "50": "#fdf2ee", "100": "#fbe3da", "700": "#b8401c"},
                "accent": {"DEFAULT": "#e4572e", "600": "#c8461f"},
                "night": {"DEFAULT": "#16181b", "800": "#1f2226", "700": "#2b2f34"},
                "ink": "#16181b", "paper": "#f4f3f1", "line": "#e0ddd8"},
        banner_cls="bg-accent text-white font-medium", accent_ink="text-white",
        phone="(555) 555-0160", tel="+15555550160",
        address="1400 Commerce Drive<br>Brookside, PA 00000",
        nav=[("Services", "#services"), ("Cost estimator", "#estimate"), ("Our work", "#work"), ("Reviews", "#reviews"), ("Contact", "#visit")],
        cta=("Free inspection", "#inspect"),
    ))
    t = S["t"]
    side = demo_form(S, "quickinspect",
        f'<p class="sm:col-span-2 font-display text-2xl font-bold uppercase">Free roof inspection</p><p class="sm:col-span-2 -mt-2 text-sm text-ink/60">Photos of every issue, no obligation.</p>' +
        chips(S, "reason", ["Leak", "Storm damage", "Old roof", "Selling my home"], req=True, label="Reason") +
        inp(S, "ZIP code", "zip", req=True, extra=' inputmode="numeric" maxlength="5"') + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel"),
        "Book my inspection", "Thanks! We'll call you today to book your free inspection ({reason}).",
        cls="bg-white text-ink rounded-xl p-6 shadow-2xl", note="Most inspections within 48 hours")
    hero = hero_full(S, "1635424709845-3a85ad5e1f5e", "Licensed &middot; Insured &middot; 25-year workmanship warranty",
        'A new roof in one day. <span class="text-accent">Built for the next 25 years.</span>',
        "Free inspections with photos of every problem, straight answers on repair or replace, and real help with your insurance claim after a storm.",
        f'<a href="#inspect" class="{t["btn"]}">Get a free inspection</a><a href="tel:{S["tel"]}" class="{t["btn_line_d"]}">{PHONE_ICON} {S["phone"]}</a>',
        side=side, points=["Own crews, no subcontractors", "Financing from 0% APR", "Insurance claim help"], pos="object-top", opacity="opacity-55")
    st = stats(S, [("1,800+", "Roofs installed"), ("25 years", "Workmanship warranty"), ("1 day", "Typical install"), ("4.9&#9733;", "Average rating (sample)")])
    services = section("services", "bg-paper", heading(S, "What we do", "Roofing, gutters and everything up top") + photo_cards(S, [
        dict(img="1570129477492-45c003edd2be", title="Roof replacement", text="Full tear-off, new underlayment, ice and water shield, and architectural shingles, usually in one day.", meta="Free quote in 24 hours"),
        dict(img="1633759593085-1eaeb724fc88", title="Roof repair", text="Leaks, missing shingles, flashing and vents fixed fast, with photos before and after.", meta="Repairs from $350"),
        dict(img="1632759145351-1d592919f522", title="Storm &amp; hail damage", text="We document the damage, meet your adjuster on the roof and handle the paperwork.", meta="Insurance claim help"),
        dict(img="1779941373840-a93f6e0d5db0", title="Metal roofing", text="Standing-seam metal that lasts 50+ years, sheds snow and cuts cooling costs.", meta="40-year paint warranty"),
        dict(img="1566071634551-224a639a1c7d", title="Gutters &amp; downspouts", text="Seamless aluminum gutters made on site in 20 colors, with optional leaf guards.", meta="From $11 per foot"),
        dict(img="1710139323182-69622cad5c3b", title="Ventilation &amp; skylights", text="Ridge vents, attic fans and leak-free skylights to keep your attic dry and cool.", meta="Free attic check"),
    ]), S)
    def rchips(name, opts, checked):
        return "".join(f'<label class="chip cursor-pointer"><input type="radio" name="{name}" value="{v}" class="sr-only"{" checked" if v == checked else ""}>'
                       f'<span class="inline-block rounded-md border border-white/20 px-4 py-2 text-sm font-semibold">{l}</span></label>' for v, l in opts)
    est = (f'<div class="grid lg:grid-cols-2 gap-10 items-start"><div>{heading(S, "Cost estimator", "What would a new roof cost?", "Move the sliders for a ballpark range. Your free inspection gives you an exact, written quote.", dark=True)}'
           f'<form id="estimator" class="reveal mt-8 space-y-6" onsubmit="return false">'
           f'<label class="block text-sm font-semibold">Home size <span id="e-size-out" class="float-right text-accent"></span><input id="e-size" type="range" min="1000" max="5000" step="100" value="2200" class="w-full mt-3"></label>'
           f'<div><p class="text-sm font-semibold">Stories</p><div class="mt-2 flex flex-wrap gap-2">{rchips("stories", [(1, "1"), (2, "2"), (3, "3")], 2)}</div></div>'
           f'<div><p class="text-sm font-semibold">Roof shape</p><div class="mt-2 flex flex-wrap gap-2">{rchips("pitch", [(1.12, "Simple"), (1.25, "Medium"), (1.4, "Complex")], 1.25)}</div></div>'
           f'<div><p class="text-sm font-semibold">Material</p><div class="mt-2 flex flex-wrap gap-2">{rchips("mat", [(1, "Architectural shingles"), (2, "Premium shingles"), (3, "Standing-seam metal")], 1)}</div></div>'
           f'</form></div>'
           f'<div class="reveal rounded-xl bg-white text-ink p-7 sm:p-8 lg:mt-16"><p class="text-sm font-semibold text-ink/60">Estimated price range</p><p class="font-display text-5xl font-bold mt-2"><span id="e-low"></span> &ndash; <span id="e-high"></span></p>'
           f'<p class="mt-3 text-ink/70">or about <strong id="e-month" class="text-ink"></strong> per month with financing*</p><p class="mt-1 text-sm text-ink/50">Roof area about <span id="e-area"></span> sq ft</p>'
           f'<a href="#inspect" class="{t["btn"]} w-full mt-7">Get my exact quote</a><p class="mt-4 text-xs text-ink/50">*Example: 120 months at 7.99% APR, subject to credit approval. Ballpark figures for this demo.</p></div></div>')
    estsec = section("estimate", "bg-night text-white", est, S)
    work = section("work", "bg-white", heading(S, "Our work", "Recent roofs around Brookside") + gallery(S, [
        ("1598228723793-52759bba239c", "Architectural shingles &middot; Oak Ridge"), ("1781797221329-c3d083ab6d99", "Full replacement &middot; Brookside"),
        ("1762374974129-f9266d9c4efc", "Storm damage claim &middot; Riverton"), ("1759105734106-47594c3eea11", "Standing-seam metal &middot; Fairview"),
        ("1628624747186-a941c476b7ef", "New gutters &amp; roof &middot; Cedar Falls"), ("1572120360610-d971b9d7767c", "Porch roof repair &middot; Hillcrest"),
    ]), S)
    how = section("how", "bg-paper", heading(S, "How it works", "From first call to final walkthrough") + steps(S, [
        ("Free inspection", "We check the roof, attic and gutters, and text you photos of every issue."),
        ("Clear proposal", "Repair or replace, options and prices in writing. No pressure, no expiring deals."),
        ("Install day", "Our own crew tears off, installs and cleans up with a magnetic nail sweep."),
        ("Walkthrough &amp; warranty", "We walk the job with you and register your 25-year workmanship warranty."),
    ]), S)
    about = section("about", "bg-white", split(S, "1635424825057-7fb6dcd651ef",
        text_block(S, "Family owned since 1998", "We only send our own crews", [
            "Dan Kowalski started on roofs at 17. Today his company has six full-time crews, all employees, all trained in-house.",
            "That means the people on your roof are the people we know, insure and stand behind for 25 years."]) +
        checks(S, ["Manufacturer-certified installers", "Fully licensed and insured, $2M liability", "Written warranty transferable to the next owner"]),
        pos="object-top",
        badge=f'<div class="absolute -bottom-6 left-4 sm:left-6 flex items-center gap-3 bg-white rounded-xl shadow-xl p-3 pr-5"><img src="{U("1672748341520-6a839e6c05bb", 200, 200)}" alt="Dan Kowalski" class="w-14 h-14 rounded-lg object-cover object-top"><div><p class="font-bold text-sm">Dan Kowalski</p><p class="text-xs text-ink/60">Owner</p></div></div>'), S)
    revs = section("reviews", "bg-night text-white", heading(S, "Reviews", "Homeowners on their new roofs", dark=True) + reviews(S, [
        ("After the hailstorm they met our adjuster on the roof. Insurance covered the full replacement and the crew finished in a day.", "Sample homeowner"),
        ("They sent photos of every damaged spot. Turned out we only needed a repair, not a new roof. That's honesty.", "Sample homeowner"),
        ("Not a single nail in the driveway. They even cleaned the gutters before leaving.", "Sample homeowner"),
    ], dark=True), S)
    form = multistep(S, "inspect-form", [
        ("What's going on?", chips(S, "issue", ["Active leak", "Storm or hail damage", "Missing shingles", "Roof is getting old", "Buying or selling", "Gutters"], req=True)),
        ("About your home", sel(S, "Roof age", "age", ["Under 10 years", "10 to 20 years", "Over 20 years", "Not sure"], req=True, first="Choose...") +
         chips(S, "stories", ["1 story", "2 stories", "3 stories"], req=True, label="Stories", span=False) +
         chips(S, "claim", ["Yes", "No", "Not sure"], label="Insurance claim?", span=False)),
        ("Your details", inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
         inp(S, "Email", "email", "email", ac="email") + inp(S, "Property address", "address", req=True, ac="street-address") + consent(S)),
    ], "Book free inspection", "Inspection requested", "Thanks, {name}! We'll call today to book your free inspection. You'll get photos of every issue within 24 hours of the visit.")
    insp = form_section(S, "inspect", "Free inspection", "Book your free roof inspection",
        "Takes 45 minutes. You don't need to be home if we can reach the roof safely; we'll send everything by text and email.",
        ["Photos of every issue, sent the same day", "Honest advice: repair when repair is enough", "Written quote valid for 90 days"], form, dark=False)
    vis = visit(S, "1787094497609-5efe6029b950", "Contact", "Visit our showroom",
                "See shingle colors and metal panels in person, or ask for samples at home.",
                [("Monday &ndash; Friday", "7:30 am &ndash; 5:30 pm"), ("Saturday", "9:00 am &ndash; 1:00 pm"), ("Sunday", "Closed"), ("Emergency tarping", "24/7")],
                "Shingle &amp; metal samples in the showroom", f'<a href="tel:{S["tel"]}" class="{t["btn_dark"]}">Call {S["phone"]}</a><a href="#inspect" class="{t["btn_line"]}">Free inspection</a>')
    fq = faq(S, [
        ("Will my insurance pay for a new roof?", "If the damage comes from a covered event like hail or wind, often yes. We document everything and meet your adjuster so nothing is missed."),
        ("How long does a replacement take?", "Most homes are done in one day, two for larger or more complex roofs. We tarp and clean up every evening."),
        ("Do you install over the old shingles?", "No. We always tear off down to the deck so we can replace any rotten wood and give you a full warranty."),
        ("Do you offer financing?", "Yes, from 0% APR for 12 months or low monthly payments up to 15 years, subject to approval."),
        ("What does the warranty cover?", "Our workmanship for 25 years, plus the manufacturer's material warranty. Both transfer if you sell the house."),
    ], bg="bg-paper")
    S["mobile"] = mobile_bar(S, "Free inspection", "#inspect")
    js = r"""
(function () {
  const f = $('#estimator'); if (!f) return;
  const size = $('#e-size');
  const rate = { 1: [4.6, 6.2], 2: [6.2, 8.1], 3: [10.5, 14.5] };
  function calc() {
    const st = Number(f.querySelector('[name=stories]:checked').value);
    const pitch = Number(f.querySelector('[name=pitch]:checked').value);
    const mat = f.querySelector('[name=mat]:checked').value;
    const area = Math.round(Number(size.value) / st * pitch * 1.1 / 10) * 10;
    const lo = Math.round(area * rate[mat][0] / 100) * 100, hi = Math.round(area * rate[mat][1] / 100) * 100;
    const r = 0.0799 / 12, n = 120, mid = (lo + hi) / 2;
    $('#e-size-out').textContent = Number(size.value).toLocaleString('en-US') + ' sq ft';
    $('#e-area').textContent = area.toLocaleString('en-US');
    $('#e-low').textContent = money(lo); $('#e-high').textContent = money(hi);
    $('#e-month').textContent = money(mid * r / (1 - Math.pow(1 + r, -n)));
  }
  f.addEventListener('input', calc); f.addEventListener('change', calc); calc();
})();
"""
    S["css"] = "#estimator .chip input:checked + span { background: var(--accent); border-color: var(--accent); color: #fff; }"
    body = hero + st + services + estsec + work + how + about + revs + insp + vis + fq
    return S, body, js


# =====================================================================  LANDSCAPING
def landscaping():
    S = setup(dict(
        slug="landscaping", name="BF Landscapes", kind="landscaping company", style="soft", header="light",
        tagline="Design &middot; Lawn care &middot; Outdoor living",
        description="Demo website for a landscaping company: lawn care plan builder with live pricing, project gallery, free quote requests. Built by BF Tech Lab.",
        og="1597201278257-3687be27d954",
        fonts="family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500;600;700",
        font_display=['"DM Serif Display"', "Georgia", "serif"], font_sans=['"DM Sans"', "system-ui", "sans-serif"],
        colors={"brand": {"DEFAULT": "#2f6b3c", "50": "#eef6ee", "100": "#dcebdc", "700": "#245530"},
                "accent": {"DEFAULT": "#c9dc6b", "600": "#b3c955"},
                "night": {"DEFAULT": "#13261a", "800": "#1a3223", "700": "#24412e"},
                "ink": "#16261b", "paper": "#f6f5ee", "line": "#e1e3d3"},
        tokens=dict(h1="font-display font-normal leading-[1.02] text-5xl sm:text-6xl lg:text-7xl",
                    h2="font-display text-4xl sm:text-5xl font-normal leading-[1.05]",
                    h3="font-display text-2xl font-normal leading-snug"),
        single_weight=True, banner_cls="bg-night text-white/90", accent_ink="text-night",
        phone="(555) 555-0170", tel="+15555550170",
        address="31 Greenway Road<br>Brookside, PA 00000",
        nav=[("Services", "#services"), ("Lawn plans", "#plan"), ("Our work", "#work"), ("About", "#about"), ("Contact", "#visit")],
        cta=("Free quote", "#quote"),
    ))
    t = S["t"]
    hero = hero_full(S, "1597201278257-3687be27d954", "Design &middot; Build &middot; Maintain",
        'A yard you\'ll actually <em class="text-accent">want to spend time in.</em>',
        "Weekly lawn care, garden design and patios built to last, from one local crew that answers the phone and shows up on the same day every week.",
        f'<a href="#quote" class="{t["btn_accent"]}">Get a free quote</a><a href="#work" class="{t["btn_line_d"]}">See our work</a>',
        points=["Free on-site estimate", "Licensed &amp; insured", "Love it or we redo it"], tall=True, opacity="opacity-65")
    st = stats(S, [("650+", "Weekly lawn clients"), ("Since 2011", "Family owned"), ("48 h", "Design quotes"), ("4.9&#9733;", "Average rating (sample)")])
    services = section("services", "bg-white", heading(S, "Services", "Everything outside, handled") + photo_cards(S, [
        dict(img="1690068023694-053da714f95f", title="Weekly lawn care", text="Mowing, edging, trimming and blowing on the same day each week, April to November."),
        dict(img="1759891038233-9e55634b9838", title="Garden design &amp; planting", text="Beds that bloom from spring to fall, designed for your sun, soil and budget."),
        dict(img="1602860739945-9a61573cd62d", title="Patios &amp; hardscape", text="Paver patios, walkways, retaining walls and fire pits, built on a proper base."),
        dict(img="1594353162824-a8b237f9adae", title="Outdoor lighting", text="Low-voltage LED path, garden and tree lighting on a timer. Safer and beautiful."),
        dict(img="1761839259494-71caddcdd6b3", title="Tree &amp; shrub care", text="Pruning, shaping and seasonal feeding to keep everything healthy and tidy."),
        dict(img="1734079692079-172d8243ebd3", title="Seasonal cleanups", text="Spring and fall cleanups, leaf removal, mulch and hedge trimming."),
    ]), S)
    addons = [("fert", "Fertilization program", 45), ("weed", "Weed control", 25), ("aer", "Aeration &amp; overseeding", 20), ("leaf", "Fall leaf cleanup", 15), ("shrub", "Shrub trimming", 30)]
    plan = (f'<div class="grid lg:grid-cols-2 gap-10 items-start"><div>{heading(S, "Lawn care plans", "Build your plan, see your price", "Pick your lawn size and the extras you want. No contracts: pause or cancel any time.")}'
            f'<form id="planner" class="reveal mt-8 space-y-7" onsubmit="return false">'
            f'<label class="block text-sm font-semibold">Lawn size <span id="p-size-out" class="float-right text-brand"></span><input id="p-size" type="range" min="2000" max="20000" step="500" value="6000" class="w-full mt-3"></label>'
            f'<div><p class="text-sm font-semibold">Mowing</p><div class="mt-2 flex flex-wrap gap-2">'
            f'<label class="chip cursor-pointer"><input type="radio" name="freq" value="4.33" class="sr-only" checked><span class="inline-block rounded-full border border-line bg-white px-4 py-2 text-sm font-medium">Weekly</span></label>'
            f'<label class="chip cursor-pointer"><input type="radio" name="freq" value="2.17" class="sr-only"><span class="inline-block rounded-full border border-line bg-white px-4 py-2 text-sm font-medium">Every two weeks</span></label></div></div>'
            f'<div><p class="text-sm font-semibold">Add-ons</p><div class="mt-3 grid sm:grid-cols-2 gap-2">'
            + "".join(f'<label class="flex items-center justify-between gap-3 rounded-xl border border-line bg-white px-4 py-3 text-sm cursor-pointer"><span class="flex items-center gap-3"><input type="checkbox" name="add" value="{v}" data-label="{l}" class="w-4 h-4" style="accent-color:var(--brand)">{l}</span><span class="text-ink/50">+${v}</span></label>' for k, l, v in addons)
            + f'</div></div></form></div>'
            f'<div class="reveal lg:sticky lg:top-24 rounded-3xl bg-night text-white p-8 sm:p-10"><p class="text-sm font-semibold text-accent uppercase tracking-wider">Your plan</p>'
            f'<p class="font-display text-6xl mt-3"><span id="p-total"></span><span class="text-xl text-white/60 font-sans">/month</span></p>'
            f'<p class="mt-2 text-white/70"><span id="p-visit"></span> per mowing visit &middot; <span id="p-visits"></span> visits a month</p>'
            f'<ul id="p-list" class="mt-6 space-y-2 text-sm text-white/80"></ul>'
            f'<a href="#quote" id="p-cta" class="{t["btn_accent"]} w-full mt-8">Lock in this plan</a>'
            f'<p class="mt-4 text-xs text-white/50">First mow free for new clients. Example prices for this demo.</p></div></div>')
    plansec = section("plan", "bg-paper", plan, S)
    work = section("work", "bg-white", heading(S, "Our work", "Recent projects") + gallery(S, [
        ("1782594700873-bbeefef37e11", "Front lawn renovation &middot; Brookside"), ("1772040942277-b194d9d0b648", "Poolside planting &middot; Oak Ridge"),
        ("1769503236428-7773271074cf", "Cedar pergola &amp; pavers &middot; Riverton"), ("1681465766418-6474cfdcbb3c", "Modern entry garden &middot; Fairview"),
        ("1764969370921-7c8df49171cd", "Weekly lawn care &middot; Hillcrest"), ("1658692051708-519fbdac7e8f", "Garden lighting &middot; Cedar Falls"),
    ]), S)
    about = section("about", "bg-paper", split(S, "1734079692160-fcbe4be6ab96",
        text_block(S, "About us", "One crew, one phone number, every week", [
            "Luis and Ana Ortega started BF Landscapes in 2011 with a trailer and two mowers. Today 28 people keep 650 yards looking their best.",
            "Your crew leader stays the same all season, knows your yard and texts you after every visit, so you never wonder if we came."]) +
        checks(S, ["Same day every week, text after every visit", "Pet-safe and kid-safe treatment options", "Licensed, insured and background-checked"]),
        pos="object-center"), S)
    how = section("how", "bg-white", heading(S, "How it works", "From first walk-through to a yard you love") + steps(S, [
        ("Free walk-through", "We visit, listen to what you want and measure everything."),
        ("Design &amp; quote", "You get a drawing and a clear price within 48 hours."),
        ("Build or start", "We build your project or start your weekly care on a date that suits you."),
        ("Ongoing care", "Same crew, same day, with a text after every visit."),
    ]), S)
    revs = section("reviews", "bg-night text-white", heading(S, "Reviews", "Happy yards, happy neighbors", dark=True) + reviews(S, [
        ("They redid our front yard in a week. Neighbors keep stopping to ask who did it.", "Sample client"),
        ("Same crew every Tuesday, text with a photo when they're done. Never have to think about the lawn anymore.", "Sample client"),
        ("The patio and lighting turned our backyard into the place everyone wants to hang out.", "Sample client"),
    ], dark=True), S)
    form = demo_form(S, "quote-form",
        inp(S, "Name", "name", req=True, ac="name") + inp(S, "Mobile number", "phone", "tel", req=True, ac="tel") +
        inp(S, "Email", "email", "email", ac="email") + inp(S, "Property address", "address", req=True, ac="street-address") +
        chips(S, "services", ["Weekly lawn care", "Garden design", "Patio or hardscape", "Lighting", "Cleanup", "Tree &amp; shrub care"], kind="checkbox", label="What are you interested in?") +
        area(S, "Tell us about your yard", "message", "e.g. front beds need a refresh, thinking about a patio out back") + consent(S),
        "Request free quote", "Thanks, {name}! We'll call within one business day to book your free walk-through.",
        cls="rounded-3xl bg-white text-ink p-6 sm:p-8 shadow-2xl")
    quote = form_section(S, "quote", "Free quote", "Tell us about your yard",
        "We'll come out, walk the property with you and send a written quote within 48 hours.",
        ["No-obligation, on-site estimate", "Written quote with a drawing for design projects", "Flexible start dates, spring fills fast"], form)
    vis = visit(S, "1784293449032-200db587788c", "Contact", "Visit the yard",
                "Office and stone yard: see pavers, wall blocks and plant samples.",
                [("Monday &ndash; Friday", "7:00 am &ndash; 6:00 pm"), ("Saturday (Apr &ndash; Nov)", "8:00 am &ndash; 2:00 pm"), ("Sunday", "Closed")],
                "Stone yard &amp; plant samples on site", f'<a href="tel:{S["tel"]}" class="{t["btn"]}">Call {S["phone"]}</a><a href="#quote" class="{t["btn_line"]}">Free quote</a>')
    fq = faq(S, [
        ("Do I have to sign a contract?", "No. Weekly plans are month to month. Pause for vacation or cancel any time with a week's notice."),
        ("Do I need to be home?", "No. Just leave gates unlocked and dogs inside. We text you a photo when we're done."),
        ("Are your products safe for pets and kids?", "We offer organic and pet-safe options for every treatment, and we always flag the yard after spraying."),
        ("What areas do you serve?", "Brookside and towns within 15 miles, including Oak Ridge, Riverton, Fairview and Hillcrest."),
        ("Do you do snow removal?", "Yes, for weekly clients only, with per-push or seasonal pricing."),
    ])
    S["mobile"] = mobile_bar(S, "Free quote", "#quote")
    js = r"""
(function () {
  const f = $('#planner'); if (!f) return;
  const size = $('#p-size');
  function calc() {
    const sq = Number(size.value), freq = Number(f.querySelector('[name=freq]:checked').value);
    const visit = Math.round(28 + sq / 1000 * 4.2);
    const adds = $$('[name=add]:checked', f);
    const total = Math.round(visit * freq + adds.reduce((s, a) => s + Number(a.value), 0));
    $('#p-size-out').textContent = sq.toLocaleString('en-US') + ' sq ft';
    $('#p-visit').textContent = money(visit); $('#p-visits').textContent = freq > 3 ? 'about 4' : 'about 2';
    $('#p-total').textContent = money(total);
    $('#p-list').innerHTML = [`<li>&#10003; Mowing ${freq > 3 ? 'weekly' : 'every two weeks'}, edging &amp; blowing</li>`]
      .concat(adds.map(a => `<li>&#10003; ${a.dataset.label}</li>`)).join('');
  }
  f.addEventListener('input', calc); f.addEventListener('change', calc); calc();
  $('#p-cta').addEventListener('click', () => {
    const m = $('#quote-form').elements.namedItem('message');
    m.value = `Lawn plan: ${size.value} sq ft, ${$('#p-total').textContent}/month` ;
    const lawn = $('#quote-form').querySelector('input[name=services][value="Weekly lawn care"]'); if (lawn) lawn.checked = true;
  });
})();
"""
    body = hero + st + services + plansec + work + about + how + revs + quote + vis + fq
    return S, body, js


SITES = [restaurant, plumbing, roofing, landscaping]
