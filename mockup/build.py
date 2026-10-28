"""Generate the static mockup pages for The Dog Club Bali.

Run:  python3 mockup/build.py
Every page shares the same header, footer and design tokens, and all business
content (prices, hours, contacts) lives in the data at the top of this file.
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"

# ---------------------------------------------------------------------------
# Business data (taken from the live thedogclub.id content)
# ---------------------------------------------------------------------------
PAWSI = "https://book.pawsi.id/thedogclubbali"
WA_NUMBER = "628113940055"
WA_DISPLAY = "+62 811 394 0055"
PHONE_DISPLAY = "+62 361 934 4153"
PHONE_TEL = "+623619344153"
EMAIL = "woof@thedogclub.id"
FRANCHISE_EMAIL = "franchise@thedogclub.id"
ADDRESS = "Jl. Umalas 1 No. 1700, Kerobokan Kelod, Kuta Utara, Kabupaten Badung, Bali 80361"
INSTAGRAM = "https://www.instagram.com/thedogclub.bali/"
FACEBOOK = "https://www.facebook.com/thedogclubbali"
MAP_QUERY = quote("The Dog Club Bali, Jl. Umalas 1 No. 1700, Kerobokan Kelod")
MAP_EMBED = f"https://www.google.com/maps?q={MAP_QUERY}&output=embed"
MAP_LINK = f"https://www.google.com/maps/search/?api=1&query={MAP_QUERY}"
TAX_NOTE = "Prices in IDR. 10% tax &amp; service not included."


def wa(message):
    return f"https://wa.me/{WA_NUMBER}?text={quote(message)}"


def img(photo_id, w=1200):
    return f"https://images.unsplash.com/photo-{photo_id}?auto=format&fit=crop&w={w}&q=80"


IMG = {
    "park": "1548199973-03cce0bbc87b",
    "play": "1583511655857-d19b40a7a54e",
    "spa": "1516734212186-a967f81ad0d7",
    "people": "1525253086316-d0c936c814f8",
    "hotel": "1587300003388-59208cc962cb",
    "training": "1530281700549-e82e7bf110d6",
    "walk": "1477884213360-7e9d7dcc1e48",
    "party": "1558788353-f76d92427f16",
    "taxi": "1544568100-847a948585b9",
    "vet": "1543466835-00a7907e9de1",
    "pug": "1517849845537-4d257902454a",
    "puppy": "1561037404-61cd46aa615b",
}

# name, area, description, link, link label, external, badge
LOCATIONS = [
    ("The Dog Club", "Umalas", "Dog park, daycare, hotel, spa and training. Our flagship club.", "umalas.html", "Visit Umalas", False, ""),
    ("The Dog Club", "Ungasan", "Our club in the south of Bali.", wa("Hi! I'd like to know more about The Dog Club Ungasan."), "Ask for directions", True, ""),
    ("The Dog Hotel", "Berawa", "Our dedicated dog hotel in Berawa.", "https://thedoghotel.id/", "Visit thedoghotel.id", True, ""),
    ("The Dog Club", "Seseh", "A new club is on its way.", "", "", False, "Coming soon"),
]

# Hours shared by daycare and spa
HOURS_STANDARD = [("Monday", "9am – 4pm"), ("Tuesday – Sunday", "9am – 6pm")]

TYPICAL_DAY = [
    ("7am", "Wake up at the Dog Villa, relaxed and ready for the day."),
    ("8am", "Morning beach walk with the gang along Batu Belig beach (Prestige boarding)."),
    ("9am", "Boarding doggies are brought from the Villa to the Park. Let the fun begin!"),
    ("9am – 5pm", "Playtime at the Club, all dogs supervised by our trained staff."),
    ("5pm", "Well-deserved feeding time at the Park."),
    ("6pm", "Quick inspection, then back to the Dog Villa for a good night's rest."),
]

# slug, nav label, card title, short text, icon, image key
SERVICES = [
    ("dog-daycare", "Dog Daycare", "Dog Daycare",
     "Cage-free, supervised play in our 700 sqm park with two bone-shaped pools.", "fa-sun", "park"),
    ("luxury-dog-hotel", "Luxury Dog Hotel", "Luxury Dog Hotel",
     "Overnight stays at the cage-free Dog Villa, supervised by our staff 24/7.", "fa-moon", "hotel"),
    ("dog-spa-massage-grooming", "Dog Spa, Massage & Grooming", "Spa &amp; Grooming",
     "Grooming, haircuts, pawdicures and massages with 100% natural products.", "fa-spa", "spa"),
    ("dog-training", "Dog Training", "Dog Training",
     "Obedience, agility and behaviour classes, private or in a group.", "fa-medal", "training"),
    ("dog-walking", "Dog Walking", "Beach Walks",
     "One-hour morning walks on the beach or through the rice paddies.", "fa-shoe-prints", "walk"),
    ("dog-birthday-party", "Dog Birthday Party", "Birthday Pawties",
     "Cake, balloons, party hats and all their best friends at the Park.", "fa-cake-candles", "party"),
    ("pet-taxi", "Pet Taxi", "Pet Taxi",
     "Dog car, tuk-tuk or scooter. Free pick-up within 2 km of the Club.", "fa-van-shuttle", "taxi"),
    ("in-house-vet", "In-house Vet", "In-house Vet",
     "Vaccines, check-ups and treatments while your dog plays.", "fa-stethoscope", "vet"),
]

# Pricing tables: title, page slug, rows of (item, detail, price)
PRICING = [
    ("Dog Daycare", "dog-daycare", [
        ("Half-day", "4 hours, daily", "80.000"),
        ("Half-day", "Monthly", "1.500.000"),
        ("Full-day", "Within opening hours, daily", "100.000"),
        ("Full-day", "Monthly", "2.000.000"),
    ]),
    ("Luxury Dog Hotel", "luxury-dog-hotel", [
        ("Deluxe", "Night stay + park access, weekday", "160.000"),
        ("Deluxe", "Fri, Sat, Sun", "190.000"),
        ("Deluxe", "Monthly", "3.600.000"),
        ("Prestige", "Deluxe + 1h beach walk, weekday", "200.000"),
        ("Prestige", "Fri, Sat, Sun", "230.000"),
        ("Prestige", "Monthly", "5.000.000"),
    ]),
    ("Premium Dog Food", "luxury-dog-hotel", [
        ("Under 10 kg", "Per day", "30.000"),
        ("10 – 20 kg", "Per day", "40.000"),
        ("20 – 30 kg", "Per day", "50.000"),
        ("Over 30 kg", "Per day", "60.000"),
    ]),
    ("Dog Spa", "dog-spa-massage-grooming", [
        ("Grooming", "Short hair", "80.000"),
        ("Grooming", "Long hair", "160.000"),
        ("Quick wash", "Shampoo + towel dry", "50.000"),
        ("Haircut", "Breed-adapted cut", "80.000"),
        ("Style cut", "The look you want", "160.000"),
        ("Pawdicure", "Soak, trim, buff", "50.000"),
        ("Massage", "Full body, natural products", "50.000"),
        ("Tick removal", "", "100.000"),
    ]),
    ("Dog Training", "dog-training", [
        ("Obedience", "Private, 1 session", "300.000"),
        ("Agility", "Private, 1 session", "300.000"),
        ("Dog behaviourist", "Private, 1 session", "350.000"),
        ("Obedience", "Private, 10 sessions", "2.500.000"),
        ("Agility", "Private, 10 sessions", "2.500.000"),
        ("Obedience &amp; Agility", "Group class at the Park", "150.000"),
    ]),
    ("Dog Walking", "dog-walking", [
        ("Beach or rice paddy walk", "1 hour, 3 – 4 km", "80.000"),
    ]),
    ("Pet Taxi", "pet-taxi", [
        ("Under 2 km", "One way", "Free"),
        ("2 – 5 km", "One way", "30.000"),
        ("5 – 8 km", "One way", "50.000"),
        ("Over 8 km", "Via partner pet taxi", "On request"),
    ]),
    ("In-house Vet", "in-house-vet", [
        ("Full vaccine", "", "380.000"),
        ("Rabies vaccine", "", "150.000"),
        ("Bordetella vaccine", "", "280.000"),
        ("Anal glands", "Treatment", "280.000"),
        ("Vitamins", "Treatment", "250.000"),
        ("Blood test &amp; others", "", "On request"),
    ]),
]
PRICE = {title: rows for title, _, rows in PRICING}

FAQS = [
    ("How do I register my dog?",
     f"<p>Register once on our booking portal (Pawsi). You'll fill in your details and your pup's, and upload the vaccination book. "
     f"Registration is free and the information is for internal use only. See <a class='underline' href='join-the-club.html'>Join the Club</a> for the full steps.</p>"),
    ("What types of boarding do you offer?",
     "<p>Two types: <strong>Deluxe</strong> and <strong>Prestige</strong>. Deluxe includes daily park access and a night at the Dog Villa, which has a pool and private bedrooms on request. "
     "Prestige adds a daily morning beach walk with friends. You'll receive highlights of your dog's day on WhatsApp.</p>"
     "<p>Capacity is limited on purpose, so please book your slot in advance, especially for weekends.</p>"),
    ("What does a typical day at The Dog Club look like?",
     "<ul class='list-disc ml-5 space-y-1'>" + "".join(f"<li><strong>{t}</strong>: {d}</li>" for t, d in TYPICAL_DAY) + "</ul>"),
    ("Is it safe for my dog at The Dog Club?",
     "<p>Whenever several dogs share a space there are some risks, much like kids at school. Most parents agree the benefits of socialisation and exercise outweigh them. "
     "Through our policies, hygiene standards and trained staff we take every precaution to minimise risks, though they can't be eliminated entirely. "
     "Aggressive dogs are not allowed at the Club.</p>"),
    ("What happens if my dog gets into a fight or gets wounded?",
     "<p>Most dogs love to play vigorously, and minor cuts or scrapes can happen. Our certified staff monitor the dogs at all times, but no supervision can fully prevent injuries. "
     "Like most pet care facilities, The Dog Club does not cover veterinary charges for these situations. They are rare exceptions: most dogs go home happily tired, clean and healthy.</p>"),
    ("Do you have swimming pools for dogs?",
     "<p>Yes, three: two bone-shaped pools in the Park and one standard pool at the Dog Villa. Not a water dog? No problem, plenty of pups play while avoiding the splashes. "
     "We also offer swimming lessons in our shallow pool.</p>"),
    ("What are your grooming options?",
     "<p>Grooming, quick wash, haircut, style cut, pawdicure, massage and tick removal, all with natural products. "
     "Grooming must be booked in advance. See the <a class='underline' href='dog-spa-massage-grooming.html'>Dog Spa</a> page for prices.</p>"),
    ("Will you take my dog for a walk?",
     "<p>Yes. Dogs leave around 8am with our Dog Taxi and two staff walk the group on leash for one hour (3 – 4 km), usually along Batu Belig beach.</p>"),
    ("Can you train my cheeky pup?",
     "<p>A trained doggie is a happy doggie! Ask our team for a training appointment. Our trainer can work with your dog while they stay with us.</p>"),
    ("Do you have a taxi service for my dog?",
     "<p>Yes. Our fleet has a scooter, a dog tuk-tuk and a van. Under 2 km is free, 2 – 5 km is IDR 30.000 one way, 5 – 8 km is IDR 50.000 one way, "
     "and beyond 8 km our partner pet taxi takes over (price on request).</p>"),
    ("What about fleas and ticks?",
     "<p>Your dog must arrive free of fleas and ticks and be on flea and tick prevention. Every dog goes through a check-in inspection before entering the Park.</p>"),
    ("How will my dog behave after a stay?",
     "<p>Life at the Club is exciting! Dogs usually go home tired but happy and may sleep more than usual. Some get a little diarrhoea from the excitement, which is normal, "
     "and active dogs can lose a bit of weight from all the play. Feed them well after a big day.</p>"),
]

BLOG = [
    ("separation-anxiety", "How to Help Your Dog Overcome Separation Anxiety", "Health", "puppy"),
    ("balis-top-10-natural-treats", "Bali's Top 10 Natural Treats and Supplements", "Health", "pug"),
    ("balis-best-dog-friendly-spots", "Bali's Best Dog-Friendly Spots: Intro to Canine Adventures", "Tips", "walk"),
    ("tips-for-new-dog-owners", "Tips for New Dog Owners: Paw-some Pet Parenting!", "Tips", "people"),
]

LEGAL = [
    ("privacy-policy", "Privacy Policy"),
    ("terms-of-service", "Terms of Service"),
    ("refund-policy", "Refund &amp; Returns Policy"),
    ("shipping-policy", "Shipping Policy"),
]

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("pricing.html", "Pricing"),
    ("our-schedule.html", "Schedule"),
    ("join-the-club.html", "Join the Club"),
    ("about-us.html", "About"),
    ("blog.html", "Blog"),
    ("faqs.html", "FAQ"),
]

LOGO = """
            <a href="index.html" class="flex items-center gap-3 group" aria-label="The Dog Club home">
                <div class="w-10 h-10 rounded-full bg-forest text-sunshine flex items-center justify-center group-hover:scale-105 transition-transform">
                    <i class="fa-solid fa-dog text-lg"></i>
                </div>
                <div class="flex flex-col">
                    <span class="font-editorial text-xl sm:text-2xl font-bold tracking-tight text-forest">THE DOG CLUB</span>
                    <span class="text-[10px] tracking-widest uppercase font-semibold text-softGray -mt-1">Bali</span>
                </div>
            </a>"""


def header(active):
    def link(href, label):
        cls = "text-sunshine" if href == active else "hover:text-sunshine"
        return f'<a href="{href}" class="{cls} transition-colors">{label}</a>'

    service_active = active in {s[0] + ".html" for s in SERVICES} or active == "services.html"
    dropdown = "".join(
        f'<a href="{slug}.html" class="flex items-center gap-3 px-4 py-2.5 rounded-xl hover:bg-beige transition-colors">'
        f'<i class="fa-solid {icon} text-sunshine w-5 text-center"></i><span>{label}</span></a>'
        for slug, label, _, _, icon, _ in SERVICES
    )
    desktop = []
    for href, label in NAV:
        if href == "services.html":
            cls = "text-sunshine" if service_active else "hover:text-sunshine"
            desktop.append(f"""
                <div class="relative group">
                    <a href="services.html" class="{cls} transition-colors inline-flex items-center gap-1.5 py-6">Services <i class="fa-solid fa-chevron-down text-[10px]"></i></a>
                    <div class="invisible opacity-0 group-hover:visible group-hover:opacity-100 group-focus-within:visible group-focus-within:opacity-100 transition-all absolute left-1/2 -translate-x-1/2 top-full w-72 bg-cream border border-beigeDark rounded-2xl shadow-xl p-2 text-sm">
                        {dropdown}
                        <a href="services.html" class="block px-4 py-2.5 mt-1 border-t border-beigeDark text-xs font-semibold uppercase tracking-wider text-softGray hover:text-forest">All services &rarr;</a>
                    </div>
                </div>""")
        else:
            desktop.append(link(href, label))

    mobile_services = "".join(
        f'<a href="{slug}.html" class="py-1.5 text-sm text-forest/80">{label}</a>' for slug, label, *_ in SERVICES
    )
    mobile = "".join(
        f'<a href="{href}" class="py-2 border-b border-beige">{label}</a>'
        for href, label in NAV if href != "services.html"
    )
    return f"""
    <div class="bg-forest text-cream text-xs sm:text-sm py-2 px-4 text-center font-medium tracking-wide flex justify-center items-center gap-2">
        <span class="inline-block w-2 h-2 rounded-full bg-sunshine animate-pulse"></span>
        <span>Free pet taxi for pick-ups within 2 km of the Club.</span>
        <a href="pet-taxi.html" class="underline hover:text-sunshine transition-colors ml-1 font-semibold whitespace-nowrap">Learn more &rarr;</a>
    </div>

    <header class="sticky top-0 z-50 bg-cream/90 backdrop-blur-md border-b border-beigeDark/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            {LOGO}
            <nav class="hidden lg:flex items-center gap-7 text-sm font-medium text-forest" aria-label="Main">
                {''.join(desktop)}
            </nav>
            <div class="hidden lg:flex items-center gap-4">
                <a href="{PAWSI}" target="_blank" rel="noopener noreferrer"
                   class="bg-forest text-cream hover:bg-forestLight px-6 py-3 rounded-full text-sm font-semibold transition-all shadow-sm hover:shadow-md flex items-center gap-2 group">
                    <span>Book Now</span>
                    <i class="fa-solid fa-arrow-right text-xs group-hover:translate-x-1 transition-transform"></i>
                </a>
            </div>
            <button id="mobile-menu-btn" class="lg:hidden p-2 text-forest" aria-label="Toggle menu" aria-expanded="false" aria-controls="mobile-menu">
                <i class="fa-solid fa-bars text-2xl"></i>
            </button>
        </div>

        <div id="mobile-menu" class="hidden lg:hidden bg-cream border-b border-beigeDark px-6 py-6 max-h-[calc(100vh-5rem)] overflow-y-auto">
            <div class="flex flex-col gap-2 text-forest font-medium">
                <details class="border-b border-beige pb-2">
                    <summary class="py-2 flex justify-between items-center">Services <i class="fa-solid fa-chevron-down text-xs faq-icon transition-transform"></i></summary>
                    <div class="flex flex-col pl-3 pb-1">
                        <a href="services.html" class="py-1.5 text-sm font-semibold">All services</a>
                        {mobile_services}
                    </div>
                </details>
                {mobile}
                <a href="{PAWSI}" target="_blank" rel="noopener noreferrer"
                   class="mt-3 w-full bg-forest text-cream text-center py-3 rounded-full font-semibold flex items-center justify-center gap-2">
                    <span>Book via Pawsi</span>
                    <i class="fa-solid fa-arrow-up-right-from-square text-xs"></i>
                </a>
            </div>
        </div>
    </header>"""


def footer():
    service_links = "".join(
        f'<li><a href="{slug}.html" class="hover:text-sunshine transition-colors">{label}</a></li>'
        for slug, label, *_ in SERVICES
    )
    legal_links = "".join(
        f'<a href="{slug}.html" class="hover:underline">{title}</a>' for slug, title in LEGAL
    )
    return f"""
    <footer class="bg-forest text-cream pt-16 pb-24 md:pb-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-12 gap-10 pb-12 border-b border-forestLight">
                <div class="md:col-span-4">
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-10 h-10 rounded-full bg-sunshine text-forest flex items-center justify-center text-xl">
                            <i class="fa-solid fa-dog"></i>
                        </div>
                        <span class="font-editorial text-2xl font-bold tracking-tight">THE DOG CLUB</span>
                    </div>
                    <p class="text-sm text-cream/70 leading-relaxed mb-6">
                        Bali's happiness center for doggies: dog park, luxury hotel, spa and training in Umalas.
                    </p>
                    <div class="flex gap-3 text-sunshine">
                        <a href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer" aria-label="Instagram" class="w-9 h-9 rounded-full bg-forestLight flex items-center justify-center hover:bg-sunshine hover:text-forest transition-all"><i class="fa-brands fa-instagram"></i></a>
                        <a href="{FACEBOOK}" target="_blank" rel="noopener noreferrer" aria-label="Facebook" class="w-9 h-9 rounded-full bg-forestLight flex items-center justify-center hover:bg-sunshine hover:text-forest transition-all"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="{wa('Hi The Dog Club!')}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp" class="w-9 h-9 rounded-full bg-forestLight flex items-center justify-center hover:bg-sunshine hover:text-forest transition-all"><i class="fa-brands fa-whatsapp"></i></a>
                    </div>
                </div>

                <div class="md:col-span-3">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-sunshine mb-4">Services</h4>
                    <ul class="space-y-2 text-sm text-cream/80">{service_links}</ul>
                </div>

                <div class="md:col-span-2">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-sunshine mb-4">The Club</h4>
                    <ul class="space-y-2 text-sm text-cream/80">
                        <li><a href="about-us.html" class="hover:text-sunshine transition-colors">About us</a></li>
                        <li><a href="pricing.html" class="hover:text-sunshine transition-colors">Pricing</a></li>
                        <li><a href="our-schedule.html" class="hover:text-sunshine transition-colors">Our schedule</a></li>
                        <li><a href="join-the-club.html" class="hover:text-sunshine transition-colors">Join the Club</a></li>
                        <li><a href="umalas.html" class="hover:text-sunshine transition-colors">Location</a></li>
                        <li><a href="own-a-franchise.html" class="hover:text-sunshine transition-colors">Own a franchise</a></li>
                        <li><a href="blog.html" class="hover:text-sunshine transition-colors">Blog</a></li>
                        <li><a href="faqs.html" class="hover:text-sunshine transition-colors">FAQs</a></li>
                    </ul>
                </div>

                <div class="md:col-span-3">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-sunshine mb-4">Get in touch</h4>
                    <ul class="space-y-3 text-sm text-cream/80">
                        <li class="flex gap-3"><i class="fa-solid fa-location-dot text-sunshine mt-1"></i><a href="{MAP_LINK}" target="_blank" rel="noopener noreferrer" class="hover:text-sunshine">{ADDRESS}</a></li>
                        <li class="flex gap-3"><i class="fa-brands fa-whatsapp text-sunshine mt-1"></i><a href="{wa('Hi The Dog Club!')}" target="_blank" rel="noopener noreferrer" class="hover:text-sunshine">{WA_DISPLAY} (WhatsApp)</a></li>
                        <li class="flex gap-3"><i class="fa-solid fa-phone text-sunshine mt-1"></i><a href="tel:{PHONE_TEL}" class="hover:text-sunshine">{PHONE_DISPLAY}</a></li>
                        <li class="flex gap-3"><i class="fa-solid fa-envelope text-sunshine mt-1"></i><a href="mailto:{EMAIL}" class="hover:text-sunshine">{EMAIL}</a></li>
                    </ul>
                    <form data-mock-form class="mt-6 flex flex-col gap-2">
                        <label for="newsletter-email" class="text-xs text-cream/70">News, discounts and training tips, straight to your inbox.</label>
                        <div class="flex gap-2">
                            <input id="newsletter-email" type="email" required placeholder="Your email"
                                   class="min-w-0 flex-1 px-4 py-2.5 rounded-full bg-forestLight text-cream placeholder-cream/40 text-sm border border-forestLight focus:outline-none focus:border-sunshine">
                            <button type="submit" class="bg-sunshine hover:bg-sunshineHover text-forest text-sm font-bold px-5 rounded-full transition-all">Subscribe</button>
                        </div>
                        <p data-form-msg class="hidden text-xs text-sunshine">Thanks! You're on the list.</p>
                    </form>
                </div>
            </div>

            <div class="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-cream/50 gap-4">
                <p>&copy; <span data-year>2026</span> The Dog Club &middot; PT PMA The Dog Paradise. All rights reserved.</p>
                <div class="flex flex-wrap justify-center gap-4">{legal_links}</div>
            </div>
        </div>
    </footer>

    <div class="md:hidden fixed bottom-4 right-4 z-40">
        <a href="{PAWSI}" target="_blank" rel="noopener noreferrer"
           class="bg-sunshine text-forest font-bold px-5 py-3.5 rounded-full shadow-2xl flex items-center gap-2 text-xs uppercase tracking-wider border border-forest">
            <i class="fa-solid fa-calendar-check text-sm"></i>
            <span>Book Now</span>
        </a>
    </div>"""


def page(filename, title, description, body, active=None):
    full_title = "The Dog Club Bali — Dog Park, Hotel &amp; Spa in Umalas" if filename == "index.html" else f"{title} — The Dog Club Bali"
    html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{full_title}</title>
    <meta name="description" content="{escape(description)}">
    <meta property="og:title" content="{full_title}">
    <meta property="og:description" content="{escape(description)}">
    <meta property="og:type" content="website">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="assets/tailwind-config.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/site.css">
</head>
<body class="antialiased selection:bg-sunshine selection:text-forest">
{header(active or filename)}
    <main>
{body}
    </main>
{footer()}
    <script src="assets/site.js"></script>
</body>
</html>
"""
    (ROOT / filename).write_text(html)


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------
def btn_primary(label, href, external=False, icon="fa-arrow-right"):
    ext = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return (f'<a href="{href}"{ext} class="bg-forest hover:bg-forestLight text-cream px-8 py-4 rounded-full font-semibold text-center '
            f'transition-all shadow-md hover:shadow-lg inline-flex items-center justify-center gap-3"><span>{label}</span>'
            f'<i class="fa-solid {icon} text-xs"></i></a>')


def btn_secondary(label, href, external=False):
    ext = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return (f'<a href="{href}"{ext} class="border-2 border-forest text-forest hover:bg-forest hover:text-cream px-8 py-4 '
            f'rounded-full font-semibold text-center transition-all inline-flex items-center justify-center gap-2">{label}</a>')


def btn_wa(label, message):
    return (f'<a href="{wa(message)}" target="_blank" rel="noopener noreferrer" class="bg-forest hover:bg-forestLight text-cream '
            f'px-8 py-4 rounded-full font-semibold text-center transition-all shadow-md hover:shadow-lg inline-flex items-center '
            f'justify-center gap-3"><i class="fa-brands fa-whatsapp text-lg"></i><span>{label}</span></a>')


def eyebrow(text, dark=False):
    return f'<span class="text-xs font-bold uppercase tracking-widest text-sunshine mb-2 block">{text}</span>'


def section_heading(kicker, title, text="", center=True):
    align = "text-center max-w-3xl mx-auto" if center else "max-w-3xl"
    para = f'<p class="text-forest/70 text-base sm:text-lg leading-relaxed">{text}</p>' if text else ""
    return f"""
            <div class="{align} mb-12 md:mb-16">
                {eyebrow(kicker)}
                <h2 class="font-editorial text-3xl sm:text-4xl md:text-5xl font-bold text-forest mb-4">{title}</h2>
                {para}
            </div>"""


def page_hero(kicker, title, intro, image_key, actions=""):
    return f"""
        <section class="pt-8 pb-16 md:pt-16 md:pb-20">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-12 gap-10 lg:gap-14 items-center">
                <div class="md:col-span-7">
                    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-beige border border-beigeDark text-forest text-xs font-semibold uppercase tracking-wider mb-6">
                        <i class="fa-solid fa-paw text-sunshine"></i> {kicker}
                    </div>
                    <h1 class="font-editorial text-4xl sm:text-5xl lg:text-6xl font-bold text-forest leading-[1.15] mb-6">{title}</h1>
                    <div class="text-base sm:text-lg text-forest/80 leading-relaxed space-y-4 max-w-2xl">{intro}</div>
                    <div class="flex flex-col sm:flex-row gap-4 mt-8">{actions}</div>
                </div>
                <div class="md:col-span-5">
                    <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-cream aspect-[4/5] bg-beige">
                        <img src="{img(IMG[image_key], 1000)}" alt="" class="w-full h-full object-cover">
                    </div>
                </div>
            </div>
        </section>"""


def simple_hero(kicker, title, intro=""):
    para = f'<p class="text-base sm:text-lg text-forest/75 leading-relaxed max-w-2xl mx-auto">{intro}</p>' if intro else ""
    return f"""
        <section class="pt-12 pb-12 md:pt-20 md:pb-16 text-center border-b border-beigeDark/50">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                {eyebrow(kicker)}
                <h1 class="font-editorial text-4xl sm:text-5xl lg:text-6xl font-bold text-forest leading-[1.15] mb-5">{title}</h1>
                {para}
            </div>
        </section>"""


def stat_row(items):
    cells = "".join(f"""
                <div class="bg-cream rounded-2xl border border-beigeDark p-5 flex items-center gap-4">
                    <div class="w-11 h-11 rounded-full bg-beige flex items-center justify-center text-forest shrink-0"><i class="fa-solid {icon}"></i></div>
                    <div><p class="font-bold text-forest leading-tight">{big}</p><p class="text-xs text-softGray">{small}</p></div>
                </div>""" for icon, big, small in items)
    return f'<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-{len(items)} gap-4">{cells}</div>'


def price_table(title, rows, link=None, dark_header=False):
    body = "".join(f"""
                    <li class="flex items-baseline justify-between gap-4 py-3 border-b border-beigeDark/70 last:border-0">
                        <div><p class="font-semibold text-forest">{item}</p>{f'<p class="text-xs text-softGray">{detail}</p>' if detail else ''}</div>
                        <p class="font-editorial font-bold text-lg text-forest whitespace-nowrap">{price}</p>
                    </li>""" for item, detail, price in rows)
    more = f'<a href="{link}" class="mt-4 inline-block text-xs font-semibold uppercase tracking-wider text-softGray hover:text-forest">Service details &rarr;</a>' if link else ""
    return f"""
                <div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8 flex flex-col">
                    <h3 class="font-editorial text-2xl font-bold text-forest mb-2">{title}</h3>
                    <ul class="flex-1">{body}</ul>
                    {more}
                </div>"""


def hours_card(title, rows, notes=()):
    lines = "".join(f'<li class="flex justify-between gap-4 py-2 border-b border-beigeDark/70 last:border-0"><span>{d}</span><span class="font-semibold">{h}</span></li>' for d, h in rows)
    note = "".join(f'<p class="text-xs text-softGray mt-3">{n}</p>' for n in notes)
    return f"""
                <div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8">
                    <div class="flex items-center gap-3 mb-4"><i class="fa-solid fa-clock text-sunshine"></i><h3 class="font-bold text-forest">{title}</h3></div>
                    <ul class="text-sm text-forest/85">{lines}</ul>
                    {note}
                </div>"""


def checklist(items):
    return '<ul class="space-y-3">' + "".join(
        f'<li class="flex items-start gap-3 text-forest/85"><i class="fa-solid fa-check text-sunshine mt-1"></i><span>{i}</span></li>' for i in items
    ) + "</ul>"


def timeline(items):
    rows = "".join(f"""
                    <li class="relative pl-8 pb-6 last:pb-0">
                        <span class="absolute left-0 top-1 w-3.5 h-3.5 rounded-full bg-sunshine ring-4 ring-beige"></span>
                        <p class="font-bold text-forest">{t}</p>
                        <p class="text-sm text-forest/75">{d}</p>
                    </li>""" for t, d in items)
    return f'<ol class="relative border-l-2 border-beigeDark ml-1.5 pl-0 [&>li]:-ml-[9px]">{rows}</ol>'


def faq_list(items):
    return '<div class="space-y-4">' + "".join(f"""
                <details class="bg-cream rounded-2xl border border-beigeDark overflow-hidden group">
                    <summary class="p-6 flex justify-between items-center gap-4 font-bold text-forest text-base sm:text-lg">
                        <span>{q}</span>
                        <i class="fa-solid fa-chevron-down text-sunshine transition-transform faq-icon"></i>
                    </summary>
                    <div class="px-6 pb-6 text-sm sm:text-base text-forest/80 leading-relaxed space-y-3">{a}</div>
                </details>""" for q, a in items) + "</div>"


def cta_band(title, text, actions):
    return f"""
        <section class="py-16 md:py-24 bg-forest text-cream">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="font-editorial text-3xl sm:text-4xl md:text-5xl font-bold mb-4">{title}</h2>
                <p class="text-cream/80 text-base sm:text-lg mb-8">{text}</p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">{actions}</div>
            </div>
        </section>"""


def cta_light_buttons(primary_label, primary_href, secondary_label=None, secondary_href=None, primary_external=True, wa_secondary=None):
    ext = ' target="_blank" rel="noopener noreferrer"' if primary_external else ""
    primary = (f'<a href="{primary_href}"{ext} '
               f'class="bg-sunshine hover:bg-sunshineHover text-forest px-8 py-4 rounded-full font-bold transition-all shadow-md inline-flex items-center justify-center gap-2">'
               f'<span>{primary_label}</span><i class="fa-solid fa-arrow-right text-xs"></i></a>')
    secondary = ""
    if wa_secondary:
        secondary = (f'<a href="{wa(wa_secondary)}" target="_blank" rel="noopener noreferrer" class="border-2 border-cream/40 hover:border-cream text-cream '
                     f'px-8 py-4 rounded-full font-semibold transition-all inline-flex items-center justify-center gap-2"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a>')
    elif secondary_label:
        secondary = (f'<a href="{secondary_href}" class="border-2 border-cream/40 hover:border-cream text-cream px-8 py-4 rounded-full font-semibold '
                     f'transition-all inline-flex items-center justify-center">{secondary_label}</a>')
    return primary + secondary


def location_cards():
    cards = []
    for name, area, desc, href, label, external, badge in LOCATIONS:
        ext = ' target="_blank" rel="noopener noreferrer"' if external else ""
        link = (f'<a href="{href}"{ext} class="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-forest hover:text-sunshine">{label} '
                f'<i class="fa-solid {"fa-arrow-up-right-from-square" if external else "fa-arrow-right"} text-xs"></i></a>') if href else ""
        tag = f'<span class="absolute top-4 right-4 text-[11px] font-bold uppercase tracking-wider bg-sunshine text-forest px-2.5 py-1 rounded-full">{badge}</span>' if badge else ""
        cards.append(f"""
                <div class="relative bg-cream rounded-3xl border border-beigeDark p-6 flex flex-col {'opacity-70' if badge else ''}">
                    {tag}
                    <div class="w-11 h-11 rounded-full bg-forest text-sunshine flex items-center justify-center mb-4"><i class="fa-solid fa-location-dot"></i></div>
                    <p class="text-xs font-bold uppercase tracking-wider text-softGray">{name}</p>
                    <h3 class="font-editorial text-2xl font-bold text-forest">{area}</h3>
                    <p class="text-sm text-forest/75 mt-2 flex-1">{desc}</p>
                    {link}
                </div>""")
    return f'<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">{"".join(cards)}</div>'


def service_cards(exclude=None):
    cards = "".join(f"""
                <a href="{slug}.html" class="group bg-cream rounded-3xl border border-beigeDark overflow-hidden hover:border-sunshine/60 hover:shadow-lg transition-all flex flex-col">
                    <div class="h-48 overflow-hidden bg-beige"><img src="{img(IMG[image], 800)}" alt="" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"></div>
                    <div class="p-6 flex-1 flex flex-col">
                        <div class="w-10 h-10 rounded-xl bg-forest/5 text-forest flex items-center justify-center mb-4"><i class="fa-solid {icon}"></i></div>
                        <h3 class="font-editorial text-xl font-bold text-forest mb-2">{title}</h3>
                        <p class="text-sm text-forest/75 leading-relaxed flex-1">{short}</p>
                        <span class="mt-4 text-sm font-semibold text-forest inline-flex items-center gap-2">Discover <i class="fa-solid fa-arrow-right text-xs group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </a>""" for slug, _, title, short, icon, image in SERVICES if slug != exclude)
    return f'<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>'


def section(inner, bg="bg-cream", border=False, narrow=False):
    width = "max-w-4xl" if narrow else "max-w-7xl"
    b = " border-y border-beigeDark/50" if border else ""
    return f"""
        <section class="py-16 md:py-24 {bg}{b}">
            <div class="{width} mx-auto px-4 sm:px-6 lg:px-8">{inner}
            </div>
        </section>"""


def text_to_html(path):
    """Plain text exported from the old site -> headings/paragraphs/lists."""
    out, in_list = [], False
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        is_bullet = line.startswith("•")
        if in_list and not is_bullet:
            out.append("</ul>")
            in_list = False
        if is_bullet:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{escape(line.lstrip('• '))}</li>")
        elif len(line) < 70 and not line.endswith((".", ",", ";")):
            out.append(f"<h2>{escape(line)}</h2>")
        else:
            out.append(f"<p>{escape(line)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def build_home():
    tabs = [
        ("park", "fa-tree", "The Park", "A 700 sqm playground",
         "Three separate play areas let our staff group dogs by size, affinity and energy level. Two bone-shaped pools and an agility area keep everyone busy all day.",
         ["700 sqm cage-free park", "2 bone-shaped swimming pools", "Agility area &amp; 3 play zones"], "park"),
        ("villa", "fa-house", "The Dog Villa", "Where boarding dogs sleep",
         "At night, hotel guests move next door to the Dog Villa: a cage-free home with a big garden and its own pool, supervised by our staff 24/7.",
         ["Cage-free, home-like rooms", "Garden &amp; pool", "Daily WhatsApp highlights"], "hotel"),
        ("spa", "fa-spa", "Dog Spa", "Fresh and pampered",
         "Our groomers wash, cut, style and massage using 100% natural products, so your pup goes home cleaner and happier than ever.",
         ["Grooming &amp; style cuts", "Pawdicure &amp; massage", "Natural products only"], "spa"),
        ("training", "fa-medal", "Training", "Good boys &amp; girls",
         "Ary, our national-champion trainer, teaches obedience, agility and behaviour in private sessions or group classes at the Park.",
         ["Obedience &amp; agility", "Dog behaviourist sessions", "Private or group classes"], "training"),
    ]
    tab_buttons = "".join(
        f'<button type="button" role="tab" data-tab-btn="{key}" aria-selected="{"true" if i == 0 else "false"}" '
        f'class="px-6 py-3 rounded-full text-sm font-semibold whitespace-nowrap transition-all {"bg-forest text-cream" if i == 0 else "bg-beige text-forest hover:bg-beigeDark"}">'
        f'<i class="fa-solid {icon} mr-2"></i>{label}</button>'
        for i, (key, icon, label, *_rest) in enumerate(tabs)
    )
    tab_panels = "".join(f"""
                <div data-tab-panel="{key}" role="tabpanel" class="grid md:grid-cols-12 gap-8 items-center w-full {'' if i == 0 else 'hidden'}">
                    <div class="md:col-span-6 space-y-4">
                        <h3 class="font-editorial text-2xl sm:text-3xl font-bold text-forest">{title}</h3>
                        <p class="text-forest/80 text-sm sm:text-base leading-relaxed">{desc}</p>
                        <ul class="space-y-2 pt-2">{''.join(f'<li class="flex items-center gap-2 text-sm text-forest font-medium"><i class="fa-solid fa-check text-sunshine"></i> {b}</li>' for b in bullets)}</ul>
                    </div>
                    <div class="md:col-span-6">
                        <div class="rounded-2xl overflow-hidden h-64 sm:h-80 shadow-lg border border-beigeDark bg-beige">
                            <img src="{img(IMG[image], 900)}" alt="" loading="lazy" class="w-full h-full object-cover">
                        </div>
                    </div>
                </div>""" for i, (key, _icon, _label, title, desc, bullets, image) in enumerate(tabs))

    popular = [
        ("Full-day Daycare", "100.000", "per day", "dog-daycare.html"),
        ("Deluxe Hotel", "160.000", "per night, weekday", "luxury-dog-hotel.html"),
        ("Grooming", "80.000", "short hair", "dog-spa-massage-grooming.html"),
        ("Beach Walk", "80.000", "1 hour", "dog-walking.html"),
    ]
    popular_cards = "".join(f"""
                    <a href="{href}" class="rounded-2xl border border-forestLight bg-forestLight/40 p-6 hover:border-sunshine transition-all">
                        <p class="text-sm text-cream/70 mb-2">{name}</p>
                        <p class="font-editorial text-3xl font-bold text-sunshine">IDR {price}</p>
                        <p class="text-xs text-cream/60 mt-1">{unit}</p>
                    </a>""" for name, price, unit, href in popular)

    steps = [
        ("1", "Register on Pawsi", "Create your profile and your dog's, and upload the vaccination book. It's free."),
        ("2", "Book your visit", "Pick daycare, a hotel stay, grooming or a walk, and choose your date."),
        ("3", "Drop off (or we pick up)", "Bring your dog to Umalas, or use our pet taxi, free within 2 km."),
    ]
    step_cards = "".join(f"""
                <div class="bg-cream rounded-3xl border border-beigeDark p-8">
                    <span class="font-editorial text-5xl font-bold text-sunshine">{n}</span>
                    <h3 class="font-editorial text-2xl font-bold text-forest mt-3 mb-2">{t}</h3>
                    <p class="text-sm text-forest/75 leading-relaxed">{d}</p>
                </div>""" for n, t, d in steps)

    reviews = "".join("""
                <div class="bg-beige/30 p-6 rounded-3xl border border-dashed border-beigeDark flex flex-col justify-between">
                    <div>
                        <div class="flex text-sunshine text-sm mb-4"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
                        <p class="text-forest/50 text-sm leading-relaxed italic mb-6">Placeholder: a real Google review from a Dog Club customer goes here, managed from the admin dashboard.</p>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-beigeDark"></div>
                        <div><p class="text-xs font-bold text-forest/60">Customer name</p><p class="text-[11px] text-softGray">Google review</p></div>
                    </div>
                </div>""" for _ in range(3))

    body = f"""
        <section class="relative pt-8 pb-16 md:pt-16 md:pb-24 overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid md:grid-cols-12 gap-8 lg:gap-12 items-center">
                    <div class="md:col-span-7 flex flex-col items-start">
                        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-beige border border-beigeDark text-forest text-xs font-semibold uppercase tracking-wider mb-6">
                            <i class="fa-solid fa-location-dot text-sunshine"></i> Umalas &middot; Ungasan &middot; Berawa
                        </div>
                        <h1 class="font-editorial text-4xl sm:text-5xl lg:text-6xl font-bold text-forest leading-[1.15] mb-6">
                            Your furry friend's new <span class="italic font-normal text-sunshine">favorite</span> place.
                        </h1>
                        <p class="text-base sm:text-lg text-forest/80 leading-relaxed mb-8 max-w-xl">
                            Bali's happiness center for doggies: a cage-free dog park, luxury dog hotel, spa and training, all with a dog-loving team that treats your pup like family.
                        </p>
                        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 w-full sm:w-auto">
                            {btn_primary("Book via Pawsi", PAWSI, external=True)}
                            {btn_secondary("Explore services", "services.html")}
                        </div>
                        <div class="mt-12 pt-8 border-t border-beigeDark/60 grid grid-cols-2 sm:grid-cols-3 gap-6 w-full">
                            <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-full bg-beige flex items-center justify-center text-forest shrink-0"><i class="fa-solid fa-tree"></i></div><span class="text-xs font-medium text-forest/90 leading-tight">700 sqm cage-free park</span></div>
                            <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-full bg-beige flex items-center justify-center text-forest shrink-0"><i class="fa-solid fa-water-ladder"></i></div><span class="text-xs font-medium text-forest/90 leading-tight">2 bone-shaped pools</span></div>
                            <div class="flex items-center gap-3 col-span-2 sm:col-span-1"><div class="w-10 h-10 rounded-full bg-beige flex items-center justify-center text-forest shrink-0"><i class="fa-solid fa-shield-halved"></i></div><span class="text-xs font-medium text-forest/90 leading-tight">Supervised by trained staff</span></div>
                        </div>
                    </div>
                    <div class="md:col-span-5 relative mt-6 md:mt-0">
                        <div class="relative mx-auto max-w-md md:max-w-none">
                            <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-cream aspect-[4/5] bg-beige">
                                <img src="{img(IMG['park'], 1000)}" alt="Dogs playing in the park at The Dog Club" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-gradient-to-t from-forest/40 via-transparent to-transparent"></div>
                            </div>
                            <div class="absolute -bottom-6 left-2 sm:-left-6 bg-cream p-4 rounded-2xl shadow-xl border border-beigeDark flex items-center gap-3 max-w-[240px]">
                                <div class="w-12 h-12 rounded-xl bg-forest text-sunshine flex items-center justify-center shrink-0"><i class="fa-brands fa-whatsapp text-xl"></i></div>
                                <div><p class="text-xs font-bold text-forest">Daily highlights</p><p class="text-[11px] text-softGray">Photos of your pup's day on WhatsApp</p></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

{section(section_heading("Our locations", "Find the club nearest to you", "Three places across Bali, with a fourth on the way.") + location_cards(), bg="bg-cream")}
        <section class="py-16 md:py-24 bg-beige/60 border-y border-beigeDark/50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-2 gap-10 lg:gap-16 items-center">
                <div class="rounded-3xl overflow-hidden h-80 md:h-[28rem] bg-beige shadow-lg">
                    <img src="{img(IMG['people'], 1000)}" alt="" loading="lazy" class="w-full h-full object-cover">
                </div>
                <div>
                    {eyebrow("Our philosophy")}
                    <h2 class="font-editorial text-3xl sm:text-4xl md:text-5xl font-bold text-forest mb-6">Your dog should enjoy their holiday as much as you do.</h2>
                    <p class="text-forest/80 text-base sm:text-lg leading-relaxed mb-6">
                        Our dog-loving team combines home-like attention with supervised fun, whether your pup stays for a day, a week or several months. Cage-free, safe and full of friends.
                    </p>
                    {checklist(["Cage-free environment, day and night", "Dogs grouped by size, affinity and energy level", "Trained staff chosen for their love of dogs", "Highlights of your dog's day sent on WhatsApp"])}
                    <a href="about-us.html" class="mt-8 inline-flex items-center gap-2 font-semibold text-forest hover:text-sunshine">More about us <i class="fa-solid fa-arrow-right text-xs"></i></a>
                </div>
            </div>
        </section>
{section(section_heading("What we offer", "Everything your dog needs", "Eight services under one roof in Umalas, from a day of play to a month-long pawcation.") + service_cards())}

        <section class="py-16 md:py-24 bg-cream border-t border-beigeDark/50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-col md:flex-row md:items-end justify-between mb-10">
                    <div>{eyebrow("Designed for joy")}<h2 class="font-editorial text-3xl sm:text-4xl md:text-5xl font-bold text-forest">Inside the Club</h2></div>
                    <p class="text-forest/70 max-w-md text-sm sm:text-base mt-4 md:mt-0">A look at the spaces where your dog plays, rests and gets pampered.</p>
                </div>
                <div class="flex gap-2 overflow-x-auto pb-4 mb-8 border-b border-beigeDark no-scrollbar" role="tablist">{tab_buttons}</div>
                <div class="bg-beige/40 rounded-3xl p-6 md:p-10 border border-beigeDark min-h-[380px] flex items-center">{tab_panels}
                </div>
            </div>
        </section>

        <section class="py-16 md:py-24 bg-forest text-cream">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center max-w-3xl mx-auto mb-12">
                    {eyebrow("Transparent pricing")}
                    <h2 class="font-editorial text-3xl sm:text-4xl md:text-5xl font-bold mb-4">Popular services</h2>
                    <p class="text-cream/80">{TAX_NOTE}</p>
                </div>
                <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">{popular_cards}
                </div>
                <div class="text-center mt-10">
                    <a href="pricing.html" class="bg-sunshine hover:bg-sunshineHover text-forest px-8 py-4 rounded-full font-bold transition-all shadow-md inline-flex items-center gap-2">See full price list <i class="fa-solid fa-arrow-right text-xs"></i></a>
                </div>
            </div>
        </section>
{section(section_heading("Join the Club", "Three steps to your first visit") + f'<div class="grid md:grid-cols-3 gap-6">{step_cards}</div><div class="text-center mt-10">{btn_primary("Register on Pawsi", PAWSI, external=True)}</div>')}

        <section class="py-16 md:py-24 bg-beige/40 border-y border-beigeDark/50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-5">
                    {eyebrow("Visit us")}
                    <h2 class="font-editorial text-3xl sm:text-4xl font-bold text-forest mb-6">Find us in Umalas</h2>
                    <div class="space-y-6">
                        <div class="flex items-start gap-4"><div class="w-10 h-10 rounded-full bg-forest text-sunshine flex items-center justify-center shrink-0"><i class="fa-solid fa-location-dot"></i></div>
                            <div><h3 class="font-bold text-forest">Address</h3><p class="text-sm text-forest/80">{ADDRESS}</p></div></div>
                        <div class="flex items-start gap-4"><div class="w-10 h-10 rounded-full bg-forest text-sunshine flex items-center justify-center shrink-0"><i class="fa-solid fa-clock"></i></div>
                            <div><h3 class="font-bold text-forest">Opening hours</h3><p class="text-sm text-forest/80">Monday: 9am – 4pm<br>Tuesday – Sunday: 9am – 6pm</p></div></div>
                        <div class="flex items-start gap-4"><div class="w-10 h-10 rounded-full bg-forest text-sunshine flex items-center justify-center shrink-0"><i class="fa-solid fa-syringe"></i></div>
                            <div><h3 class="font-bold text-forest">Entry requirements</h3><p class="text-sm text-forest/80">Fully vaccinated, on flea &amp; tick prevention, and friendly with other dogs.</p></div></div>
                    </div>
                    <div class="mt-8 flex flex-col sm:flex-row gap-3">
                        <a href="{MAP_LINK}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 bg-forest text-cream px-6 py-3 rounded-full text-sm font-semibold hover:bg-forestLight transition-all"><i class="fa-solid fa-diamond-turn-right"></i> Get directions</a>
                        <a href="{wa('Hi The Dog Club! I have a question.')}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 border-2 border-forest text-forest px-6 py-3 rounded-full text-sm font-semibold hover:bg-forest hover:text-cream transition-all"><i class="fa-brands fa-whatsapp"></i> WhatsApp us</a>
                    </div>
                </div>
                <div class="lg:col-span-7">
                    <div class="bg-cream p-3 rounded-3xl border border-beigeDark shadow-lg">
                        <iframe src="{MAP_EMBED}" title="Map to The Dog Club in Umalas" class="w-full h-80 sm:h-96 rounded-2xl border-0" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
            </div>
        </section>
{section(section_heading("Community love", "Happy tails", "What dog parents in Bali say about The Dog Club.") + f'<div class="grid md:grid-cols-3 gap-8">{reviews}</div>')}
{section(section_heading("Got questions?", "Frequently asked questions") + faq_list(FAQS[:4]) + '<div class="text-center mt-10"><a href="faqs.html" class="font-semibold text-forest hover:text-sunshine inline-flex items-center gap-2">See all FAQs <i class="fa-solid fa-arrow-right text-xs"></i></a></div>', bg="bg-beige/40", border=True, narrow=True)}"""
    page("index.html", "Home", "Bali's happiness center for doggies in Umalas: cage-free dog park, luxury dog hotel, spa, training, beach walks and pet taxi.", body)


def build_services():
    body = simple_hero("Our services", "Everything your dog needs, under one roof",
                       "From a day of play to a month-long pawcation, every service is run by our trained, dog-loving team in Umalas.")
    body += section(service_cards())
    body += cta_band("Not sure where to start?", "Tell us about your dog and we'll recommend the right service.",
                     cta_light_buttons("Book via Pawsi", PAWSI, wa_secondary="Hi The Dog Club! Which service is right for my dog?"))
    page("services.html", "Services", "Dog daycare, luxury dog hotel, spa and grooming, training, beach walks, birthday parties, pet taxi and in-house vet in Umalas, Bali.", body)


def service_page(slug, kicker, title, intro, image, actions, sections, cta, description):
    body = page_hero(kicker, title, intro, image, actions)
    body += "".join(sections)
    body += section(section_heading("More from the Club", "Other services") + service_cards(exclude=slug), bg="bg-cream")
    body += cta
    label = next(s[1] for s in SERVICES if s[0] == slug)
    page(f"{slug}.html", label, description, body, active=f"{slug}.html")


def two_col(left, right, bg="bg-beige/40"):
    return section(f'<div class="grid lg:grid-cols-2 gap-8 items-start">{left}{right}</div>', bg=bg, border=True)


def build_daycare():
    sections = [
        section(stat_row([("fa-tree", "700 sqm", "Cage-free park"), ("fa-water-ladder", "2 pools", "Bone-shaped"),
                          ("fa-layer-group", "3 play areas", "Grouped by size &amp; energy"), ("fa-eye", "Fully supervised", "By trained staff")])),
        two_col(
            f'<div>{hours_card("Daycare opening hours", HOURS_STANDARD, ["Register your dog before the first visit. Fully vaccinated dogs only.", "Weekends get busy: WhatsApp us or arrive early."])}'
            f'<div class="mt-8 bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8"><h3 class="font-bold text-forest mb-2">Need a lift?</h3><p class="text-sm text-forest/80">Our pet taxi picks your dog up for free within 2 km. <a class="underline" href="pet-taxi.html">See pet taxi</a>.</p></div></div>',
            f'<div id="pricing">{price_table("Daycare pricing", PRICE["Dog Daycare"])}<p class="text-xs text-softGray mt-3">{TAX_NOTE}</p></div>'),
        section(f'<div class="grid md:grid-cols-2 gap-12 items-center"><div>{section_heading("Why daycare", "Good for your dog, and for you", center=False)}'
                + checklist(["Socialising with other dogs and humans", "A clean, monitored environment",
                             "Staff chosen for their love of dogs", "Exercise and stimulation every dog needs",
                             "Helps dogs with separation anxiety or sadness"])
                + f'</div><div class="rounded-3xl overflow-hidden h-80 bg-beige shadow-lg"><img src="{img(IMG["play"], 900)}" alt="" loading="lazy" class="w-full h-full object-cover"></div></div>'),
    ]
    service_page("dog-daycare", "Dog Daycare", "Safe, supervised and fun",
                 "<p>Dog Daycare at The Dog Club is cage-free and fully supervised, for dogs of every breed and size.</p>"
                 "<p>Our 700 sqm park has two bone-shaped pools, an agility area and three separate play zones, so our staff can group dogs by affinity, size and energy level.</p>",
                 "park", btn_primary("Book daycare", PAWSI, external=True) + btn_secondary("See pricing", "#pricing"),
                 sections, cta_band("At The Dog Club, we look after your dog as if they were ours.", "Book a day of play in a few taps.",
                                    cta_light_buttons("Book daycare", PAWSI, wa_secondary="Hi! I'd like to book daycare for my dog.")),
                 "Cage-free, supervised dog daycare in Umalas, Bali: 700 sqm park, two bone-shaped pools and an agility area. From IDR 80.000.")


def build_hotel():
    food = f"""
                <div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8">
                    <h3 class="font-editorial text-2xl font-bold text-forest mb-2">Premium dog food</h3>
                    <p class="text-sm text-forest/80 mb-5">Two all-natural, vet-approved recipes with more than 50% fresh meat, high in vitamins, calcium and fibre, made for sensitive stomachs.</p>
                    <div class="grid sm:grid-cols-2 gap-4 mb-6">
                        <div class="rounded-2xl bg-beige/50 p-4"><p class="font-bold text-forest">Dog Club Delight</p><p class="text-xs text-forest/70 mt-1">Chicken, chicken liver, sweet potato, oats, carrots, green beans, berries, coconut oil, turmeric. Great for picky eaters.</p></div>
                        <div class="rounded-2xl bg-beige/50 p-4"><p class="font-bold text-forest">Dog Club Fuel</p><p class="text-xs text-forest/70 mt-1">Mackerel, sweet potato, eggs, oats, carrots, green beans, berries, coconut oil, turmeric. Great for allergy-prone dogs.</p></div>
                    </div>
                    <ul>{''.join(f'<li class="flex justify-between py-2 border-b border-beigeDark/70 last:border-0 text-sm"><span>{i}</span><span class="font-semibold">IDR {p}</span></li>' for i, _, p in PRICE["Premium Dog Food"])}</ul>
                    <p class="text-xs text-softGray mt-3">Price per day, by your dog's weight.</p>
                </div>"""
    sections = [
        section(f"""
                <div class="grid md:grid-cols-2 gap-6">
                    <div class="bg-cream rounded-3xl border border-beigeDark p-8">
                        <span class="text-xs font-bold uppercase tracking-wider text-softGray">Boarding</span>
                        <h3 class="font-editorial text-3xl font-bold text-forest mt-1 mb-3">Deluxe</h3>
                        <p class="text-sm text-forest/80 mb-5">Night at the Dog Villa plus daily park access and/or private playtime with our staff.</p>
                        <p class="font-editorial text-3xl font-bold text-forest">IDR 160.000 <span class="text-xs font-sans font-normal text-softGray">/ night, weekday</span></p>
                    </div>
                    <div class="bg-forest text-cream rounded-3xl border-2 border-sunshine p-8 relative">
                        <span class="absolute -top-3.5 right-6 bg-sunshine text-forest text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">Most loved</span>
                        <span class="text-xs font-bold uppercase tracking-wider text-sunshine">Boarding</span>
                        <h3 class="font-editorial text-3xl font-bold mt-1 mb-3">Prestige</h3>
                        <p class="text-sm text-cream/80 mb-5">Everything in Deluxe, plus a one-hour morning beach walk with friends every day.</p>
                        <p class="font-editorial text-3xl font-bold text-sunshine">IDR 200.000 <span class="text-xs font-sans font-normal text-cream/70">/ night, weekday</span></p>
                    </div>
                </div>"""),
        two_col(f'<div id="pricing">{price_table("Hotel pricing", PRICE["Luxury Dog Hotel"])}<p class="text-xs text-softGray mt-3">{TAX_NOTE}</p>'
                f'<div class="mt-8">{hours_card("Check-in &amp; check-out", [("Check-in", "9am – 6pm"), ("Standard check-out", "11am")], ["First stay? Fill in the free membership form (vaccines, behaviour notes). Capacity is limited, so book weekends early."])}</div></div>',
                f'<div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8"><h3 class="font-editorial text-2xl font-bold text-forest mb-6">A typical day for boarding dogs</h3>{timeline(TYPICAL_DAY)}</div>'),
        section(f'<div class="grid lg:grid-cols-2 gap-8 items-start">{food}'
                f'<div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8"><h3 class="font-editorial text-2xl font-bold text-forest mb-4">Special requests</h3>'
                f'<p class="text-sm text-forest/80 mb-5">Ask our staff for anything your dog needs during the stay. For example:</p>'
                + checklist(["Vaccination: full, rabies, bordetella", "Treatments: anti-tick, anal glands, vitamins", "Vet check-up",
                             "Training: agility, obedience, behaviourist", "Premium food (see left)"])
                + "</div></div>"),
    ]
    service_page("luxury-dog-hotel", "Luxury Dog Hotel", "The best pet boarding in Bali",
                 "<p>At night, our guests sleep at the <strong>Dog Villa</strong> next to the Park: a cage-free home with a big garden and a pool, supervised by our trained staff 24/7.</p>"
                 "<p>We know it's hard to leave your pet, so you'll receive highlights of their happy days on WhatsApp.</p>",
                 "hotel", btn_primary("Book a stay", PAWSI, external=True) + btn_secondary("See pricing", "#pricing"),
                 sections, cta_band("Treat your dog to a sleepover with friends.", "Weekend slots fill up fast. Book ahead.",
                                    cta_light_buttons("Book a stay", PAWSI, wa_secondary="Hi! I'd like to book a hotel stay for my dog.")),
                 "Cage-free luxury dog hotel in Umalas, Bali. Deluxe and Prestige boarding at the Dog Villa with 24/7 supervision. From IDR 160.000 per night.")


def build_spa():
    services = [
        ("Grooming", "Wash and blow-dry by our in-house team."),
        ("Quick wash", "Shampoo and towel dry for a dirty pup."),
        ("Haircut", "A simple cut adapted to your dog's breed."),
        ("Style cut", "Feeling fancy? The stylish cut you want."),
        ("Pawdicure", "Paw soak, nail trim, buffed or polished."),
        ("Massage", "Relaxing full-body massage with natural products."),
        ("Tick removal", "Careful, steady removal of ticks."),
    ]
    cards = "".join(f'<div class="bg-cream rounded-2xl border border-beigeDark p-5"><p class="font-bold text-forest">{t}</p><p class="text-sm text-forest/70 mt-1">{d}</p></div>' for t, d in services)
    sections = [
        section(section_heading("Treatments", "Pick your pamper", "Natural products only, delivered by trained stylists and bathers.") + f'<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">{cards}</div>'),
        two_col(f'<div>{hours_card("Spa opening hours", HOURS_STANDARD, ["Grooming must be booked in advance. You will fill in a short grooming form to confirm.", "Need a special treatment? Ask us."])}</div>',
                f'<div id="pricing">{price_table("Spa pricing", PRICE["Dog Spa"])}<p class="text-xs text-softGray mt-3">{TAX_NOTE}</p></div>'),
    ]
    service_page("dog-spa-massage-grooming", "Dog Spa", "Luxurious grooming &amp; dog spa",
                 "<p>Grooming, haircuts, massages, pawdicures and more. Our trained stylists and bathers send your furkid home fresher and happier than ever, using 100% natural products.</p>",
                 "spa", btn_primary("Book grooming", PAWSI, external=True) + btn_secondary("See pricing", "#pricing"),
                 sections, cta_band("Your doggie deserves to be pampered.", "Book a spa slot in advance.",
                                    cta_light_buttons("Book grooming", PAWSI, wa_secondary="Hi! I'd like to book grooming for my dog.")),
                 "Dog grooming, spa and massage in Umalas, Bali with 100% natural products. Grooming from IDR 80.000.")


def build_training():
    sections = [
        section(f"""
                <div class="grid md:grid-cols-2 gap-6">
                    <div class="bg-cream rounded-3xl border border-beigeDark p-8"><i class="fa-solid fa-hand text-2xl text-sunshine mb-4"></i>
                        <h3 class="font-editorial text-2xl font-bold text-forest mb-3">Obedience</h3>
                        <p class="text-sm text-forest/80 leading-relaxed">Essential for every breed, especially high-energy dogs. Sit, down, stay, come and leave it, plus loose-leash walking, rewards, no jumping and separation anxiety courses.</p></div>
                    <div class="bg-cream rounded-3xl border border-beigeDark p-8"><i class="fa-solid fa-person-running text-2xl text-sunshine mb-4"></i>
                        <h3 class="font-editorial text-2xl font-bold text-forest mb-3">Agility</h3>
                        <p class="text-sm text-forest/80 leading-relaxed">Once obedience is settled, dogs can step up to agility: running, jumping over obstacles and learning tricks. It's as fun as it looks on social media!</p></div>
                </div>"""),
        two_col(f'<div id="pricing">{price_table("Training pricing", PRICE["Dog Training"])}<p class="text-xs text-softGray mt-3">{TAX_NOTE}</p></div>',
                """<figure class="bg-forest text-cream rounded-3xl p-8">
                    <span class="text-xs font-bold uppercase tracking-widest text-sunshine">Meet the trainer</span>
                    <blockquote class="font-editorial text-xl leading-relaxed mt-4 mb-6">&ldquo;Everybody is able to train dogs, but not everybody can understand them. I consider I do, thanks to my years of experience and love for doggies.&rdquo;</blockquote>
                    <figcaption class="text-sm text-cream/80 space-y-2">
                        <p><strong class="text-cream">Ary</strong>, dog trainer since 2013</p>
                        <p>First Balinese to win a national agility championship, former Bali agility team member and chairman of the Doberman Club in Indonesia.</p>
                    </figcaption>
                </figure>"""),
        section(f'<div class="grid md:grid-cols-2 gap-12 items-center"><div>{section_heading("Benefits", "What your dog will learn", center=False)}'
                + checklist(["Better attention and focus", "Commands: sit, down, stay, come, heel, no", "Heel during leash walks",
                             "Body awareness and flexibility", "Confidence with moving objects", "Physical exercise and mental stimulation"])
                + f'</div><div class="rounded-3xl overflow-hidden h-80 bg-beige shadow-lg"><img src="{img(IMG["training"], 900)}" alt="" loading="lazy" class="w-full h-full object-cover"></div></div>'),
    ]
    service_page("dog-training", "Dog Training", "A trained doggie is a happy doggie",
                 "<p>Puppy, older dog, rescue or just a naughty one: training at The Dog Club teaches them to behave at home, at the park, on the beach and with other pets and humans.</p>"
                 "<p>Agility, obedience and behaviour classes, in a fun private or group session.</p>",
                 "training", btn_wa("Book a session", "Hi! I'd like to book a training session for my dog.") + btn_secondary("See pricing", "#pricing"),
                 sections, cta_band("Finally, a dog that listens.", "Book a private session or join a group class at the Park.",
                                    cta_light_buttons("Chat with us", wa("Hi! I'd like to book a training session for my dog."))),
                 "Dog obedience, agility and behaviour training in Umalas, Bali, with national champion trainer Ary. Private sessions from IDR 300.000.")


def build_walking():
    sections = [
        two_col(f'<div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8"><h3 class="font-editorial text-2xl font-bold text-forest mb-4">How it works</h3>'
                + checklist(["Morning walks on the beach (usually Batu Belig) or through the rice paddies",
                             "Dogs leave the Club around 8am in our Dog Taxi", "Two trained staff in charge of each group",
                             "On leash for one hour, about 3 – 4 km", "Back at the Club for a day of play"]) + "</div>",
                f'<div id="pricing">{price_table("Walking pricing", PRICE["Dog Walking"])}<p class="text-xs text-softGray mt-3">{TAX_NOTE} Included daily with Prestige boarding.</p></div>'),
        section(f'<div class="grid md:grid-cols-2 gap-12 items-center"><div>{section_heading("Benefits", "Starting the day off right", center=False)}'
                + checklist(["Burns calories and keeps weight in check", "Keeps joints in motion", "Helps regulate digestion", "Good for mental and physical health"])
                + f'</div><div class="rounded-3xl overflow-hidden h-80 bg-beige shadow-lg"><img src="{img(IMG["walk"], 900)}" alt="" loading="lazy" class="w-full h-full object-cover"></div></div>'),
    ]
    service_page("dog-walking", "Dog Walking", "Morning beach walks with friends",
                 "<p>Most dogs need a walk at least once a day. Ours come with sand, sea breeze and the whole gang, supervised by two trained staff.</p>",
                 "walk", btn_wa("Book a walk", "Hi! I'd like to book a beach walk for my dog.") + btn_secondary("See pricing", "#pricing"),
                 sections, cta_band("Dogs need exercise every day, just like us.", "Add a beach walk to your dog's daycare or stay.",
                                    cta_light_buttons("Go for a walk", wa("Hi! I'd like to book a beach walk for my dog."))),
                 "Morning dog beach walks in Bali, one hour on leash with two trained staff. IDR 80.000.")


def build_birthday():
    sections = [
        section(f'<div class="grid md:grid-cols-2 gap-12 items-center"><div>{section_heading("The pawty", "Like a kid&rsquo;s party, with more fur", center=False)}'
                '<p class="text-forest/80 leading-relaxed mb-6">Lots of excitement, a great deal of mess, cake, balloons and party hats, and a bunch of dogs playing freely with their besties. Few things are happier.</p>'
                + checklist(["The Park to yourselves and your guests", "Dog-friendly birthday cake", "Decorations, balloons and party hats", "Our staff supervising the fun"])
                + f'</div><div class="rounded-3xl overflow-hidden h-80 bg-beige shadow-lg"><img src="{img(IMG["party"], 900)}" alt="" loading="lazy" class="w-full h-full object-cover"></div></div>'),
        section(section_heading("Packages", "Three birthday packages", "Choose the package that suits your pup's big day.")
                + '<div class="grid md:grid-cols-3 gap-6">' + "".join(f"""
                <div class="bg-cream rounded-3xl border border-dashed border-beigeDark p-8 text-center">
                    <p class="text-xs font-bold uppercase tracking-wider text-softGray">Package {n}</p>
                    <p class="font-editorial text-2xl font-bold text-forest mt-2">Name &amp; price TBC</p>
                    <p class="text-sm text-forest/60 mt-3">Package details to be filled in from the admin dashboard.</p>
                </div>""" for n in (1, 2, 3)) + "</div>", bg="bg-beige/40", border=True),
    ]
    service_page("dog-birthday-party", "Birthday Party", "Make it memorable: a birthday pawty at the Club",
                 "<p>Let us organise the best day of your doggie's life, with cake, friends and a whole park to celebrate in.</p>",
                 "party", btn_wa("Plan a pawty", "Hi! I'd like to organise a birthday party for my dog."),
                 sections, cta_band("Their perfect barkday, with furry friends.", "Tell us the date and number of guests, and we'll handle the rest.",
                                    cta_light_buttons("Organise the pawty", wa("Hi! I'd like to organise a birthday party for my dog."))),
                 "Dog birthday parties at The Dog Club Bali: cake, balloons, party hats and the Park for your pup and friends.")


def build_taxi():
    sections = [
        two_col(f'<div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8"><h3 class="font-editorial text-2xl font-bold text-forest mb-4">How it works</h3>'
                + checklist(["Choose the distance, number of dogs and pick-up/drop-off times",
                             "We use a dog car, tuk-tuk or scooter depending on your dog's size and availability",
                             "Cage-free, safe and fun: dogs love it", "Often fully booked, so please book in advance"]) + "</div>",
                f'<div id="pricing">{price_table("Pet taxi pricing", PRICE["Pet Taxi"])}<p class="text-xs text-softGray mt-3">{TAX_NOTE}</p></div>'),
    ]
    service_page("pet-taxi", "Pet Taxi", "Dog car, tuk-tuk or scooter: we've got the ride",
                 "<p>No time to drop off your dog? We'll pick them up, free of charge within 2 km of the Club.</p>",
                 "taxi", btn_wa("Book a ride", "Hi! I'd like to book the pet taxi for my dog.") + btn_secondary("See pricing", "#pricing"),
                 sections, cta_band("Cage-free, even during the ride.", "Book your dog's lift on WhatsApp.",
                                    cta_light_buttons("Find your dog's lift", wa("Hi! I'd like to book the pet taxi for my dog."))),
                 "Pet taxi in Bali by dog car, tuk-tuk or scooter. Free within 2 km of The Dog Club in Umalas.")


def build_vet():
    sections = [
        two_col(f'<div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8"><h3 class="font-editorial text-2xl font-bold text-forest mb-4">Our partner vet</h3>'
                '<p class="text-sm text-forest/80 leading-relaxed mb-5"><strong>Dr. Farhan</strong> advises us on best practices and protocols so every dog is cared for and handled safely, and offers preventive and wellness care for your pup.</p>'
                + checklist(["Rabies, bordetella and full vaccines", "Anal gland and vitamin treatments", "Flea and tick prevention", "Light treatments and check-ups"]) + "</div>",
                f'<div id="pricing">{price_table("Vet pricing", PRICE["In-house Vet"])}<p class="text-xs text-softGray mt-3">{TAX_NOTE}</p></div>'),
    ]
    service_page("in-house-vet", "In-house Vet", "Vet appointments while your dog plays",
                 "<p>We partner with a veterinarian who gives light treatments and check-ups at the Club. How convenient is that?</p>",
                 "vet", btn_wa("Book the vet", "Hi! I'd like to book a vet appointment for my dog.") + btn_secondary("See pricing", "#pricing"),
                 sections, cta_band("Does your dog need a vaccine?", "Contact us on WhatsApp for an appointment.",
                                    cta_light_buttons("Book your vet appointment", wa("Hi! I'd like to book a vet appointment for my dog."))),
                 "In-house vet at The Dog Club Bali: vaccines, check-ups and treatments while your dog plays. Rabies vaccine IDR 150.000.")


def build_pricing():
    jump = "".join(f'<a href="#{title.lower().replace(" ", "-")}" class="px-4 py-2 rounded-full bg-beige text-forest text-sm font-semibold whitespace-nowrap hover:bg-beigeDark">{title}</a>' for title, _, _ in PRICING)
    tables = "".join(f'<div id="{title.lower().replace(" ", "-")}" class="scroll-mt-28">{price_table(title, rows, link=f"{slug}.html")}</div>' for title, slug, rows in PRICING)
    body = simple_hero("Pricing", "Clear prices, no surprises", f"Every service in one place. {TAX_NOTE}")
    body += section(f'<div class="flex gap-2 overflow-x-auto pb-4 mb-8 no-scrollbar">{jump}</div>'
                    f'<div class="grid md:grid-cols-2 gap-6">{tables}'
                    '<div class="bg-beige/40 rounded-3xl border border-dashed border-beigeDark p-8 flex flex-col justify-center"><h3 class="font-editorial text-2xl font-bold text-forest mb-2">Birthday party</h3>'
                    '<p class="text-sm text-forest/75">Three packages. <a class="underline" href="dog-birthday-party.html">See packages</a> or ask us on WhatsApp.</p></div></div>')
    body += cta_band("Ready to book?", "Register once on Pawsi, then book any service in a few taps.",
                     cta_light_buttons("Book via Pawsi", PAWSI, wa_secondary="Hi! I have a question about your prices."))
    page("pricing.html", "Pricing", "Prices for dog daycare, hotel, spa, training, walks, pet taxi and vet at The Dog Club Bali.", body)


def build_schedule():
    body = simple_hero("Our schedule", "When we're open, and how the day runs", "Plan your visit around our opening hours and the daily rhythm at the Club.")
    body += section(f"""
                <div class="grid lg:grid-cols-3 gap-6">
                    {hours_card("Daycare &amp; Park", HOURS_STANDARD)}
                    {hours_card("Dog Spa", HOURS_STANDARD, ["By appointment only."])}
                    {hours_card("Luxury Dog Hotel", [("Check-in", "9am – 6pm"), ("Check-out", "11am"), ("Supervision", "24/7")])}
                </div>""")
    body += section(f'<div class="grid lg:grid-cols-2 gap-12 items-start"><div>{section_heading("A day at the Club", "The daily rhythm", "Boarding dogs follow this routine. Daycare dogs join for the 9am – 5pm playtime.", center=False)}'
                    f'<div class="rounded-3xl overflow-hidden h-72 bg-beige shadow-lg"><img src="{img(IMG["play"], 900)}" alt="" loading="lazy" class="w-full h-full object-cover"></div></div>'
                    f'<div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8">{timeline(TYPICAL_DAY)}</div></div>', bg="bg-beige/40", border=True)
    body += cta_band("Weekends get busy.", "Book ahead or WhatsApp us before coming.",
                     cta_light_buttons("Book via Pawsi", PAWSI, wa_secondary="Hi! Is there space at the Club today?"))
    page("our-schedule.html", "Our Schedule", "Opening hours and daily schedule at The Dog Club Bali in Umalas.", body)


def build_join():
    steps = [
        ("Register on Pawsi", "Create your account and your dog's profile. It's free, and your data is for internal use only."),
        ("Upload the vaccine book", "Rabies, full vaccine and bordetella records. Fully vaccinated dogs only."),
        ("Tell us about your dog", "Noticeable behaviours, health notes and anything that helps us care for them."),
        ("Book and visit", "Choose a service and date. Every visit starts with a quick check-in inspection."),
    ]
    step_list = "".join(f"""
                <li class="bg-cream rounded-3xl border border-beigeDark p-6 flex gap-5">
                    <span class="font-editorial text-4xl font-bold text-sunshine leading-none">{i}</span>
                    <div><h3 class="font-bold text-forest text-lg">{t}</h3><p class="text-sm text-forest/75 mt-1">{d}</p></div>
                </li>""" for i, (t, d) in enumerate(steps, 1))
    body = page_hero("Join the Club", "Become part of the pack",
                     "<p>Your dog is family, and we work hard to give them the love and care they deserve. Registration is free and takes a few minutes.</p>",
                     "people", btn_primary("Register on Pawsi", PAWSI, external=True) + btn_secondary("Read the FAQ", "faqs.html"))
    body += section(section_heading("How to join", "Four simple steps") + f'<ol class="grid md:grid-cols-2 gap-6">{step_list}</ol>', bg="bg-beige/40", border=True)
    body += section(f"""
                <div class="grid lg:grid-cols-2 gap-8">
                    <div class="bg-cream rounded-3xl border border-beigeDark p-8">
                        <h3 class="font-editorial text-2xl font-bold text-forest mb-4">Entry requirements</h3>
                        {checklist(["Up-to-date vaccinations (rabies, full vaccine, bordetella)", "On flea and tick prevention, and free of fleas and ticks on arrival", "No aggressive behaviour towards dogs or people", "Registered on Pawsi before the first visit"])}
                    </div>
                    <div class="bg-cream rounded-3xl border border-beigeDark p-8">
                        <h3 class="font-editorial text-2xl font-bold text-forest mb-4">Our promise, and the honest part</h3>
                        <p class="text-sm text-forest/80 leading-relaxed mb-3">Leaving your dog at a pet care facility is a bit like taking a child to school or camp: when many dogs share a space, some risks exist. Most parents agree that socialisation, exercise and care by trained professionals outweigh them.</p>
                        <p class="text-sm text-forest/80 leading-relaxed">Through our policies and commitment to hygiene, our staff take every precaution to minimise risks, though they can never be eliminated entirely. Questions? We're happy to talk.</p>
                    </div>
                </div>""")
    body += cta_band("Ready to join the fun?", "Register once, then book any service in a few taps.",
                     cta_light_buttons("Register on Pawsi", PAWSI, wa_secondary="Hi! I'd like to register my dog."))
    page("join-the-club.html", "Join the Club", "Register your dog at The Dog Club Bali: free sign-up on Pawsi, vaccine requirements and what to expect.", body)


def build_about():
    body = page_hero("About us", "Your dog should enjoy their holiday as much as you do",
                     "<p>The Dog Club started with a simple idea. Our dog-loving team combines home-like attention with supervised fun so your pet has a wonderful time.</p>"
                     "<p>A wide choice of services, great amenities and a cage-free environment: that's what we're proud of, and recommended for.</p>",
                     "people", btn_secondary("Our services", "services.html"))
    body += section(stat_row([("fa-tree", "700 sqm park", "In Umalas"), ("fa-water-ladder", "3 pools", "Park &amp; Villa"),
                              ("fa-house", "Cage-free", "Day and night"), ("fa-heart", "Since 2019", "Building strong puppies")]), bg="bg-beige/40", border=True)
    body += section(f"""
                <div class="bg-forest text-cream rounded-3xl p-8 sm:p-12 grid md:grid-cols-2 gap-8 items-center">
                    <div>
                        {eyebrow("Careers")}
                        <h2 class="font-editorial text-3xl sm:text-4xl font-bold mb-3">You love dogs and want to join our team?</h2>
                        <p class="text-cream/80">Send us your CV and a few words about you and dogs.</p>
                    </div>
                    <div class="md:text-right">
                        <a href="mailto:{EMAIL}?subject={quote('Job application')}" class="bg-sunshine hover:bg-sunshineHover text-forest px-8 py-4 rounded-full font-bold inline-flex items-center gap-2"><i class="fa-solid fa-envelope"></i> Apply today</a>
                    </div>
                </div>""")
    page("about-us.html", "About us", "The Dog Club Bali: a cage-free dog park, hotel and spa in Umalas run by a dog-loving team.", body)


def build_faqs():
    body = simple_hero("FAQs", "Common questions before your dog's visit", "Can't find your answer? We're here to help on WhatsApp.")
    body += section(faq_list(FAQS), narrow=True)
    body += cta_band("Still have a question?", "Our team answers on WhatsApp during opening hours.",
                     cta_light_buttons("Chat on WhatsApp", wa("Hi! I have a question.")))
    page("faqs.html", "FAQs", "Answers about registration, boarding, safety, pools, grooming, walks and pet taxi at The Dog Club Bali.", body)


def build_umalas():
    body = page_hero("Umalas, Bali", "Bali's finest dog hotel and dog park",
                     "<p>Whether it's for a day, a week or several months, our dog-loving team takes care of your pup while you're away, in the funniest yet safest environment in Bali.</p>",
                     "park", btn_primary("Book via Pawsi", PAWSI, external=True) + f'<a href="{MAP_LINK}" target="_blank" rel="noopener noreferrer" class="border-2 border-forest text-forest hover:bg-forest hover:text-cream px-8 py-4 rounded-full font-semibold text-center transition-all inline-flex items-center justify-center gap-2"><i class="fa-solid fa-diamond-turn-right"></i> Directions</a>')
    body += section(f"""
                <div class="grid lg:grid-cols-12 gap-10 items-start">
                    <div class="lg:col-span-5 space-y-6">
                        {hours_card("Opening hours", HOURS_STANDARD, ["Hotel check-in 9am – 6pm, check-out 11am."])}
                        <div class="bg-cream rounded-3xl border border-beigeDark p-6 sm:p-8 space-y-3 text-sm text-forest/85">
                            <p class="flex gap-3"><i class="fa-solid fa-location-dot text-sunshine mt-1"></i>{ADDRESS}</p>
                            <p class="flex gap-3"><i class="fa-brands fa-whatsapp text-sunshine mt-1"></i><a href="{wa('Hi The Dog Club!')}" target="_blank" rel="noopener noreferrer" class="underline">{WA_DISPLAY}</a></p>
                            <p class="flex gap-3"><i class="fa-solid fa-phone text-sunshine mt-1"></i><a href="tel:{PHONE_TEL}" class="underline">{PHONE_DISPLAY}</a></p>
                            <p class="flex gap-3"><i class="fa-solid fa-envelope text-sunshine mt-1"></i><a href="mailto:{EMAIL}" class="underline">{EMAIL}</a></p>
                        </div>
                    </div>
                    <div class="lg:col-span-7 bg-cream p-3 rounded-3xl border border-beigeDark shadow-lg">
                        <iframe src="{MAP_EMBED}" title="Map to The Dog Club in Umalas" class="w-full h-96 rounded-2xl border-0" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>""", bg="bg-beige/40", border=True)
    body += section(section_heading("At this location", "Services in Umalas") + service_cards())
    page("umalas.html", "Umalas", "The Dog Club Umalas: dog park, luxury dog hotel and spa at Jl. Umalas 1, Kerobokan Kelod, Bali. Hours, map and contact.", body)


def build_franchise():
    body = page_hero("Own a franchise", "Bring The Dog Club to your city",
                     "<p>A premium environment for pampered pets, and a rewarding dog daycare franchise for driven entrepreneurs.</p>",
                     "people", btn_secondary("Request the franchise guide", "#franchise-form"))
    body += section(f"""
                <div class="grid lg:grid-cols-12 gap-10 items-start">
                    <div class="lg:col-span-5 bg-cream rounded-3xl border border-beigeDark p-8 space-y-4 text-sm text-forest/85">
                        <h2 class="font-editorial text-2xl font-bold text-forest">The Dog Club office</h2>
                        <p class="flex gap-3"><i class="fa-solid fa-location-dot text-sunshine mt-1"></i>{ADDRESS}</p>
                        <p class="flex gap-3"><i class="fa-solid fa-envelope text-sunshine mt-1"></i><a class="underline" href="mailto:{FRANCHISE_EMAIL}">{FRANCHISE_EMAIL}</a></p>
                        <p class="flex gap-3"><i class="fa-solid fa-phone text-sunshine mt-1"></i><a class="underline" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
                        <p class="flex gap-3"><i class="fa-brands fa-whatsapp text-sunshine mt-1"></i><a class="underline" href="{wa('Hi! I am interested in a Dog Club franchise.')}" target="_blank" rel="noopener noreferrer">{WA_DISPLAY}</a></p>
                    </div>
                    <form id="franchise-form" data-mock-form class="lg:col-span-7 bg-cream rounded-3xl border border-beigeDark p-8 grid sm:grid-cols-2 gap-4 scroll-mt-28">
                        <h2 class="sm:col-span-2 font-editorial text-2xl font-bold text-forest">Get the franchise guide</h2>
                        <label class="text-sm font-semibold text-forest">Name<input required class="mt-1 w-full px-4 py-3 rounded-xl bg-white/60 border border-beigeDark focus:outline-none focus:border-forest font-normal"></label>
                        <label class="text-sm font-semibold text-forest">Email<input type="email" required class="mt-1 w-full px-4 py-3 rounded-xl bg-white/60 border border-beigeDark focus:outline-none focus:border-forest font-normal"></label>
                        <label class="text-sm font-semibold text-forest">Phone number<input type="tel" required class="mt-1 w-full px-4 py-3 rounded-xl bg-white/60 border border-beigeDark focus:outline-none focus:border-forest font-normal"></label>
                        <label class="text-sm font-semibold text-forest">City of interest<input class="mt-1 w-full px-4 py-3 rounded-xl bg-white/60 border border-beigeDark focus:outline-none focus:border-forest font-normal"></label>
                        <label class="sm:col-span-2 text-sm font-semibold text-forest">Message<textarea rows="4" class="mt-1 w-full px-4 py-3 rounded-xl bg-white/60 border border-beigeDark focus:outline-none focus:border-forest font-normal"></textarea></label>
                        <button type="submit" class="sm:col-span-2 bg-forest hover:bg-forestLight text-cream py-4 rounded-full font-semibold transition-all">Send request</button>
                        <p data-form-msg class="hidden sm:col-span-2 text-sm text-forest bg-beige rounded-xl p-3">Thank you! Our franchise team will email you the guide.</p>
                    </form>
                </div>""", bg="bg-beige/40", border=True)
    page("own-a-franchise.html", "Own a Franchise", "Open a The Dog Club franchise: a premium dog daycare and hotel concept from Bali.", body, active="own-a-franchise.html")


def build_blog():
    cards = "".join(f"""
                <a href="blog-{slug}.html" class="group bg-cream rounded-3xl border border-beigeDark overflow-hidden hover:shadow-lg transition-all flex flex-col">
                    <div class="h-56 overflow-hidden bg-beige"><img src="{img(IMG[image], 900)}" alt="" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"></div>
                    <div class="p-6 flex-1 flex flex-col">
                        <span class="text-xs font-bold uppercase tracking-wider text-sunshine">{cat}</span>
                        <h2 class="font-editorial text-2xl font-bold text-forest mt-2 mb-4 flex-1">{escape(title)}</h2>
                        <span class="text-sm font-semibold text-forest inline-flex items-center gap-2">Read article <i class="fa-solid fa-arrow-right text-xs group-hover:translate-x-1 transition-transform"></i></span>
                    </div>
                </a>""" for slug, title, cat, image in BLOG)
    body = simple_hero("Dog Club blog", "Tips, health and adventures", "Advice from our team for happier, healthier dogs in Bali.")
    body += section(f'<div class="grid md:grid-cols-2 gap-8">{cards}</div>')
    page("blog.html", "Blog", "Dog care tips, health advice and dog-friendly Bali guides from The Dog Club.", body)

    for slug, title, cat, image in BLOG:
        others = "".join(f'<li><a class="hover:text-sunshine" href="blog-{s}.html">{escape(t)}</a></li>' for s, t, _, _ in BLOG if s != slug)
        body = f"""
        <article class="pt-12 pb-16 md:pt-16">
            <div class="max-w-3xl mx-auto px-4 sm:px-6">
                <a href="blog.html" class="text-sm font-semibold text-softGray hover:text-forest"><i class="fa-solid fa-arrow-left text-xs mr-1"></i> All articles</a>
                <span class="block mt-6 text-xs font-bold uppercase tracking-wider text-sunshine">{cat}</span>
                <h1 class="font-editorial text-4xl sm:text-5xl font-bold text-forest leading-tight mt-3 mb-4">{escape(title)}</h1>
                <p class="text-sm text-softGray mb-8">The Dog Club team &middot; 29 November 2024</p>
                <div class="rounded-3xl overflow-hidden h-72 sm:h-96 bg-beige mb-10"><img src="{img(IMG[image], 1400)}" alt="" class="w-full h-full object-cover"></div>
                <div class="prose-club">{text_to_html(CONTENT / "blog" / f"{slug}.txt")}</div>
                <div class="mt-12 pt-8 border-t border-beigeDark">
                    <h2 class="font-editorial text-xl font-bold text-forest mb-3">Keep reading</h2>
                    <ul class="space-y-2 text-forest/80">{others}</ul>
                </div>
            </div>
        </article>"""
        body += cta_band("Give your dog the best day.", "Daycare, hotel, spa and training in Umalas.", cta_light_buttons("Explore services", "services.html", primary_external=False))
        page(f"blog-{slug}.html", title, f"{title} — advice from The Dog Club Bali.", body, active="blog.html")


def build_legal():
    for slug, title in LEGAL:
        body = simple_hero("Legal", title)
        body += section(f'<div class="prose-club">{text_to_html(CONTENT / "legal" / f"{slug}.txt")}</div>', narrow=True)
        page(f"{slug}.html", title.replace("&amp;", "&"), f"{title.replace('&amp;', '&')} of The Dog Club Bali.", body)


def build_404():
    body = f"""
        <section class="py-24 md:py-32 text-center">
            <div class="max-w-xl mx-auto px-4">
                <i class="fa-solid fa-bone text-5xl text-sunshine mb-6"></i>
                <h1 class="font-editorial text-4xl sm:text-5xl font-bold text-forest mb-4">This page ran off to play</h1>
                <p class="text-forest/75 mb-8">We couldn't find the page you're looking for.</p>
                {btn_primary("Back to home", "index.html")}
            </div>
        </section>"""
    page("404.html", "Page not found", "Page not found.", body)


if __name__ == "__main__":
    build_home()
    build_services()
    build_daycare()
    build_hotel()
    build_spa()
    build_training()
    build_walking()
    build_birthday()
    build_taxi()
    build_vet()
    build_pricing()
    build_schedule()
    build_join()
    build_about()
    build_faqs()
    build_umalas()
    build_franchise()
    build_blog()
    build_legal()
    build_404()
    print("Built", len(list(ROOT.glob("*.html"))), "pages")
