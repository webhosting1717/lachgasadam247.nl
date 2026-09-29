# -*- coding: utf-8 -*-
"""Gedeelde instellingen, layout en helpers voor de statische site lachgasadam247.nl.

Gebruik: python3 _build/build.py  (vanuit de root van de repository)
"""
import html
import json
import os
import re

SITE = "https://lachgasadam247.nl"
BRAND = "LachGasAdam247"
EMAIL = "info@lachgasadam247.nl"
PHONE_DISPLAY = "+31 6 84 12 95 69"
PHONE_TEL = "+31684129569"
WA_NUMBER = "31684129569"
TODAY = "2026-09-29"
CSS_VERSION = "20260929"
OG_IMAGE = SITE + "/images/opengraph-image.png"
BUSINESS_ID = SITE + "/#business"
WEBSITE_ID = SITE + "/#website"


def wa(text="LachGasAdam247 - lachgas bestellen"):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, quote(text))


WA_DEFAULT = wa()
WA_ORDER = wa("LachGasAdam247 - lachgas bestellen. Adres: , aantal: ")


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------------------
# Structured data
# ---------------------------------------------------------------------------
HOURS = {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "00:00",
    "closes": "23:59",
}

STADSDELEN = [
    ("amsterdam-centrum", "Amsterdam Centrum"),
    ("amsterdam-noord", "Amsterdam Noord"),
    ("amsterdam-zuid", "Amsterdam Zuid"),
    ("amsterdam-oost", "Amsterdam Oost"),
    ("amsterdam-west", "Amsterdam West"),
    ("amsterdam-nieuw-west", "Amsterdam Nieuw-West"),
    ("amsterdam-zuidoost", "Amsterdam Zuidoost"),
    ("weesp", "Weesp"),
]

REGIO = [
    ("amstelveen", "Amstelveen"),
    ("diemen", "Diemen"),
    ("zaandam", "Zaandam"),
    ("haarlem", "Haarlem"),
    ("hoofddorp", "Hoofddorp"),
    ("almere", "Almere"),
    ("purmerend", "Purmerend"),
]

TANKS = [
    ("2kg", "Lachgas tank 2 kg"),
    ("4kg", "Lachgas tank 4 kg"),
    ("10kg", "Lachgas tank 10 kg"),
]


def business_node():
    area = [{"@type": "City", "name": "Amsterdam", "sameAs": "https://nl.wikipedia.org/wiki/Amsterdam"}]
    for slug, name in STADSDELEN:
        area.append({"@type": "AdministrativeArea", "name": name,
                     "containedInPlace": {"@type": "City", "name": "Amsterdam"}})
    for slug, name in REGIO:
        area.append({"@type": "City", "name": name})
    return {
        "@type": "LocalBusiness",
        "@id": BUSINESS_ID,
        "name": BRAND,
        "alternateName": [BRAND + ".nl", "Lachgas Amsterdam 247"],
        "description": "LachGasAdam247 bezorgt lachgas tanks aan huis in Amsterdam en omstreken. 24/7 bereikbaar via WhatsApp en telefoon, doorgaans bezorgd in 20 tot 30 minuten.",
        "url": SITE + "/",
        "telephone": PHONE_TEL,
        "email": EMAIL,
        "image": OG_IMAGE,
        "logo": {"@type": "ImageObject", "url": SITE + "/images/icon-512.png", "width": 512, "height": 512},
        "sameAs": ["https://wa.me/" + WA_NUMBER],
        "priceRange": "€€",
        "currenciesAccepted": "EUR",
        "address": {"@type": "PostalAddress", "addressLocality": "Amsterdam",
                    "addressRegion": "Noord-Holland", "addressCountry": "NL"},
        "geo": {"@type": "GeoCoordinates", "latitude": 52.3676, "longitude": 4.9041},
        "areaServed": area,
        "openingHoursSpecification": HOURS,
        "contactPoint": {"@type": "ContactPoint", "telephone": PHONE_TEL, "email": EMAIL,
                         "contactType": "customer service", "availableLanguage": ["nl", "en"],
                         "areaServed": "NL", "hoursAvailable": HOURS},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Lachgas tanks",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": name + " bezorgen in Amsterdam",
                                                   "url": SITE + "/lachgas-tanks/" + slug + "/"}}
                for slug, name in TANKS
            ],
        },
        "knowsAbout": ["Lachgas bestellen", "Lachgas bezorgen", "Lachgas tanks", "Bezorgservice Amsterdam"],
    }


def website_node():
    return {"@type": "WebSite", "@id": WEBSITE_ID, "name": BRAND, "url": SITE + "/",
            "inLanguage": "nl-NL", "publisher": {"@id": BUSINESS_ID}}


def webpage_node(page):
    node = {
        "@type": page.get("page_type", "WebPage"),
        "@id": SITE + page["path"] + "#webpage",
        "url": SITE + page["path"],
        "name": page["title"],
        "description": page["description"],
        "inLanguage": "nl-NL",
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": BUSINESS_ID},
        "datePublished": page.get("published", TODAY),
        "dateModified": page.get("modified", TODAY),
        "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE},
        "breadcrumb": {"@id": SITE + page["path"] + "#breadcrumb"},
    }
    if page.get("speakable"):
        node["speakable"] = {"@type": "SpeakableSpecification", "cssSelector": page["speakable"]}
    return node


def breadcrumb_node(page):
    items = []
    for i, (name, href) in enumerate(page["crumbs"], start=1):
        item = {"@type": "ListItem", "position": i, "name": name}
        if href:
            item["item"] = SITE + href
        else:
            item["item"] = SITE + page["path"]
        items.append(item)
    return {"@type": "BreadcrumbList", "@id": SITE + page["path"] + "#breadcrumb", "itemListElement": items}


def faq_node(page):
    return {
        "@type": "FAQPage",
        "@id": SITE + page["path"] + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in page["faq"]
        ],
    }


def strip_tags(s):
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def jsonld(page):
    graph = [business_node(), website_node(), webpage_node(page), breadcrumb_node(page)]
    graph += page.get("schema", [])
    if page.get("faq"):
        graph.append(faq_node(page))
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False,
                      separators=(",", ":"))
    return data.replace("</", "<\\/")


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------
_I = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">%s</svg>'
ICONS = {
    "chat": _I % '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.4A8 8 0 1 1 21 12z"/>',
    "clock": _I % '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "check": _I % '<path d="M20 6 9 17l-5-5"/>',
    "pin": _I % '<path d="M12 21s7-6.2 7-11a7 7 0 0 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "bolt": _I % '<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/>',
    "home": _I % '<path d="M3 11 12 3l9 8"/><path d="M5 10v10h14V10"/>',
    "tag": _I % '<path d="M20 12 12 20 3 11V3h8l9 9z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "users": _I % '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M17.5 13.5a6.5 6.5 0 0 1 4 6.5"/>',
    "noform": _I % '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="m8 12 8 0"/><path d="m8 16 5 0"/><path d="M3 3l18 18"/>',
    "shield": _I % '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3z"/><path d="m9 12 2 2 4-4"/>',
    "moon": _I % '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
}


def slugify(text):
    t = strip_tags(text).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:60] or "sectie"


def auto_toc(body, exclude=("h-cta",)):
    """Bouw een 'Op deze pagina'-navigatie uit de h2-koppen met een id."""
    items = []
    for m in re.finditer(r'<h2 id="([^"]+)"(?: data-nav="([^"]*)")?>(.*?)</h2>', body):
        if m.group(1) in exclude or m.group(1) == "h1":
            continue
        items.append((m.group(1), m.group(2) or strip_tags(m.group(3))))
    if len(items) < 3:
        return ""
    return ('<nav class="jump pagetoc" aria-label="Op deze pagina"><div class="wrap"><ul>'
            '<li class="lbl">Op deze pagina:</li>'
            + "".join('<li><a href="#%s">%s</a></li>' % (i, esc(t)) for i, t in items)
            + "</ul></div></nav>")


def add_h2_ids(body):
    used = set()
    def f(m):
        sl = slugify(m.group(1)); base = sl; n = 2
        while sl in used:
            sl = "%s-%d" % (base, n); n += 1
        used.add(sl)
        return '<h2 id="%s">%s</h2>' % (sl, m.group(1))
    return re.sub(r"<h2>(.*?)</h2>", f, body)


def icon_cards(items):
    """items: list of (icon, title, text)"""
    return ('<div class="cards">' + "".join(
        '<div class="card"><h3>%s%s</h3><p>%s</p></div>' % (ICONS[i], esc(t), x) for i, t, x in items) + "</div>")


def chips(items, label=None):
    return ('<ul class="chips">' + ('<li class="lbl">%s</li>' % esc(label) if label else "")
            + "".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for h, t in items) + "</ul>")



def crumbs_html(crumbs):
    out = ['<nav class="crumbs" aria-label="Kruimelpad"><ol>']
    for name, href in crumbs:
        if href:
            out.append('<li><a href="%s">%s</a></li>' % (href, esc(name)))
        else:
            out.append('<li aria-current="page">%s</li>' % esc(name))
    out.append("</ol></nav>")
    return "".join(out)


def faq_html(faq, title="Veelgestelde vragen", intro=None, hid="h-faq"):
    parts = ['<section class="section alt" id="faq" aria-labelledby="%s"><div class="wrap prose">' % hid,
             '<h2 id="%s" data-nav="Veelgestelde vragen">%s</h2>' % (hid, esc(title))]
    if intro:
        parts.append('<p class="intro">%s</p>' % intro)
    for q, a in faq:
        parts.append('<div class="qa"><h3>%s</h3><p>%s</p></div>' % (q, a))
    parts.append("</div></section>")
    return "".join(parts)


def cta_block(title="Nu lachgas bestellen in Amsterdam", text=None, wa_text=None):
    if text is None:
        text = ("Stuur je adres en het gewenste aantal via WhatsApp of bel ons. Wij bevestigen het levermoment en de prijs "
                "en bezorgen doorgaans binnen 20 tot 30 minuten. 24/7, ook &rsquo;s nachts en in het weekend.")
    link = wa(wa_text) if wa_text else WA_ORDER
    return ('<section class="section cta-section" aria-labelledby="h-cta"><div class="wrap"><div class="cta-box">'
            '<h2 id="h-cta">%s</h2><p>%s</p>'
            '<div class="cta-row"><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp: lachgas bestellen</a>'
            '<a class="btn btn-call" href="tel:%s">Bel %s</a></div>'
            '<p class="fine">Uitsluitend voor volwassenen (18+). Gebruik lachgas altijd verantwoord en in overeenstemming met de geldende wet- en regelgeving.</p>'
            '</div></div></section>' % (esc(title), text, link, PHONE_TEL, PHONE_DISPLAY))


def checks(items):
    return '<ul class="checks">' + "".join("<li>%s</li>" % i for i in items) + "</ul>"


def steps(items):
    return '<ol class="steps">' + "".join("<li>%s</li>" % i for i in items) + "</ol>"


def facts(rows):
    return '<dl class="facts">' + "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (esc(k), v) for k, v in rows) + "</dl>"


def link_cards(items):
    """items: list of (href, title, text)"""
    out = ['<div class="cards">']
    for href, title, text in items:
        out.append('<div class="card"><h3><a href="%s">%s</a></h3><p>%s</p><p class="more"><a href="%s">%s &rarr;</a></p></div>'
                   % (href, esc(title), text, href, "Lees meer"))
    out.append("</div>")
    return "".join(out)


def toc(items):
    return '<ul class="toc">' + "".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for h, t in items) + "</ul>"


def phone_link():
    return '<a href="tel:%s">%s</a>' % (PHONE_TEL, PHONE_DISPLAY)


def wa_link(label="WhatsApp", text=None):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (wa(text) if text else WA_DEFAULT, label)


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
NAV = [
    ("/", "Home"),
    ("/#lachgas-bestellen-amsterdam", "Bestellen"),
    ("/bezorggebied/", "Bezorggebied"),
    ("/lachgas-tanks/", "Tanks"),
    ("/zakelijk/", "Zakelijk"),
    ("/lachgas-24-7-amsterdam/", "24/7"),
    ("/lachgas-informatie/", "Informatie"),
    ("/contact/", "Contact"),
]


def nav_html(current):
    out = ['<nav class="jump" aria-label="Hoofdmenu"><div class="wrap"><ul>']
    for href, label in NAV:
        base = href.split("#")[0]
        attrs = ' aria-current="page"' if (base == current and "#" not in href) else ""
        out.append('<li><a href="%s"%s>%s</a></li>' % (href, attrs, esc(label)))
    out.append("</ul></div></nav>")
    return "".join(out)


def footer_html():
    stads = "".join('<li><a href="/bezorggebied/%s/">Lachgas %s</a></li>' % (s, esc(n)) for s, n in STADSDELEN)
    regio = "".join('<li><a href="/bezorggebied/%s/">Lachgas %s</a></li>' % (s, esc(n)) for s, n in REGIO)
    tanks = "".join('<li><a href="/lachgas-tanks/%s/">%s</a></li>' % (s, esc(n)) for s, n in TANKS)
    return ('<footer class="site-footer"><div class="wrap"><div class="foot-grid">'
            '<div><a class="logo" href="/">LACHGAS<span>ADAM247</span></a>'
            '<p style="margin-top:.75rem">Lachgas Amsterdam bestellen: 24/7 bereikbaar via WhatsApp en telefoon, bezorging in heel Amsterdam en omstreken, doorgaans binnen 20 tot 30 minuten. Uitsluitend voor volwassenen (18+).</p>'
            '<ul><li><a href="tel:%(tel)s">%(phone)s</a></li><li><a href="%(wa)s" target="_blank" rel="noopener">WhatsApp</a></li>'
            '<li><a href="mailto:%(email)s">%(email)s</a></li><li style="color:var(--muted);padding:.4rem 0;font-size:.95rem">Bereikbaar: 24/7</li></ul></div>'
            '<div><h2>Stadsdelen</h2><ul>%(stads)s</ul></div>'
            '<div><h2>Regio</h2><ul>%(regio)s</ul><h2 style="margin-top:1.25rem">Tanks</h2><ul>%(tanks)s</ul></div>'
            '<div><h2>Meer</h2><ul>'
            '<li><a href="/lachgas-tanks/">Lachgas tanks en maten</a></li>'
            '<li><a href="/zakelijk/">Horeca, feesten en evenementen</a></li>'
            '<li><a href="/lachgas-24-7-amsterdam/">Lachgas 24/7 en &rsquo;s nachts</a></li>'
            '<li><a href="/lachgas-informatie/">Lachgas informatie</a></li>'
            '<li><a href="/lachgas-informatie/veilig-gebruik/">Veilig gebruik</a></li>'
            '<li><a href="/over-ons/">Over ons</a></li>'
            '<li><a href="/contact/">Contact</a></li>'
            '<li><a href="/privacy/">Privacy</a></li>'
            '<li><a href="/algemene-voorwaarden/">Algemene voorwaarden</a></li>'
            '</ul></div></div>'
            '<div class="foot-bottom">&copy; 2026 %(brand)s. Alle rechten voorbehouden. Lachgas is uitsluitend bestemd voor volwassenen (18+).</div>'
            '</div></footer>'
            % {"tel": PHONE_TEL, "phone": PHONE_DISPLAY, "wa": WA_DEFAULT, "email": EMAIL,
               "stads": stads, "regio": regio, "tanks": tanks, "brand": BRAND})


WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.372a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.883 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>')


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.css"), encoding="utf-8") as _f:
    CSS = "".join(line.strip() + ("\n" if line.strip().endswith("}") else "") for line in _f if line.strip()).strip()


def page_body(page):
    body = page["body"]
    if page.get("auto_toc"):
        cut = body.find("</section>")
        if cut > 0:
            cut += len("</section>")
            body = body[:cut] + auto_toc(body) + body[cut:]
    return body


def render(page):
    """Render a full HTML document for a page dict."""
    path = page["path"]
    url = SITE + path
    title = page["title"]
    desc = page["description"]
    robots = page.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")
    og_type = page.get("og_type", "website")
    noindex = "noindex" in robots
    head = [
        "<!DOCTYPE html>",
        '<html lang="nl-NL">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
        "<title>%s</title>" % esc(title),
        '<meta name="description" content="%s">' % esc(desc),
        '<meta name="robots" content="%s">' % robots,
    ]
    if not noindex:
        head += [
            '<link rel="canonical" href="%s">' % url,
            '<link rel="alternate" hreflang="nl-NL" href="%s">' % url,
            '<link rel="alternate" hreflang="nl" href="%s">' % url,
            '<link rel="alternate" hreflang="x-default" href="%s">' % url,
        ]
    head += [
        '<meta name="theme-color" content="#070c17">',
        '<meta name="color-scheme" content="dark">',
        '<meta name="author" content="%s">' % BRAND,
        '<meta name="geo.region" content="NL-NH">',
        '<meta name="geo.placename" content="Amsterdam">',
        '<meta name="geo.position" content="52.3676;4.9041">',
        '<meta name="ICBM" content="52.3676, 4.9041">',
        '<meta property="og:type" content="%s">' % og_type,
        '<meta property="og:site_name" content="%s">' % BRAND,
        '<meta property="og:locale" content="nl_NL">',
        '<meta property="og:url" content="%s">' % url,
        '<meta property="og:title" content="%s">' % esc(title),
        '<meta property="og:description" content="%s">' % esc(desc),
        '<meta property="og:image" content="%s">' % OG_IMAGE,
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="Lachgas Amsterdam bestellen bij LachGasAdam247, 24/7 bezorgd">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % esc(title),
        '<meta name="twitter:description" content="%s">' % esc(desc),
        '<meta name="twitter:image" content="%s">' % OG_IMAGE,
    ]
    if og_type == "article":
        head += [
            '<meta property="article:published_time" content="%s">' % page.get("published", TODAY),
            '<meta property="article:modified_time" content="%s">' % page.get("modified", TODAY),
        ]
    head += [
        '<link rel="icon" href="/favicon.ico" sizes="48x48">',
        '<link rel="icon" href="/images/icon-192.png" type="image/png" sizes="192x192">',
        '<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">',
        '<link rel="manifest" href="/manifest.webmanifest">',
        '<link rel="sitemap" type="application/xml" href="/sitemap.xml">',
        '<link rel="preload" href="/fonts/bebas-neue-latin.woff2" as="font" type="font/woff2" crossorigin>',
        '<meta name="apple-mobile-web-app-title" content="%s">' % BRAND,
        "<style>%s</style>" % CSS,
        '<script type="application/ld+json">%s</script>' % jsonld(page),
        "</head>",
        "<body>",
        '<a class="skip" href="#main">Ga naar inhoud</a>',
        '<header class="site-header"><div class="wrap header-in">'
        '<a class="logo" href="/" aria-label="%s, naar de homepage">LACHGAS<span>ADAM247</span></a>' % BRAND,
        '<div class="header-cta"><a class="btn btn-wa btn-sm" href="%s" target="_blank" rel="noopener">WhatsApp</a>'
        '<a class="btn btn-call btn-sm hide-sm" href="tel:%s">Bel %s</a></div></div></header>' % (WA_DEFAULT, PHONE_TEL, PHONE_DISPLAY),
        nav_html(path),
        '<main id="main">',
        page_body(page),
        "</main>",
        footer_html(),
        '<div class="bar" role="region" aria-label="Snel bestellen"><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp</a>'
        '<a class="btn btn-call" href="tel:%s">Bel nu</a></div>' % (WA_DEFAULT, PHONE_TEL),
        '<a class="fab" href="%s" target="_blank" rel="noopener" aria-label="Open WhatsApp">%s</a>' % (WA_DEFAULT, WA_SVG),
        "</body>",
        "</html>",
    ]
    return "\n".join(head) + "\n"


def doc_page(page, body_inner, meta=None):
    """Wrap an article-like body (h1 + prose) in the standard document layout."""
    body_inner = add_h2_ids(body_inner)
    toc_html = ""
    if page.get("auto_toc"):
        items = [(m.group(1), strip_tags(m.group(2))) for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body_inner)]
        if len(items) >= 3:
            toc_html = ('<nav class="doc-toc" aria-label="Op deze pagina"><p class="lbl">Op deze pagina</p><ol>'
                        + "".join('<li><a href="#%s">%s</a></li>' % (i, esc(t)) for i, t in items) + "</ol></nav>")
    return ('<article class="wrap prose doc">%s<h1>%s</h1>%s<p class="lead">%s</p>%s%s</article>'
            % (crumbs_html(page["crumbs"]), esc(page["h1"]), ('<p class="meta">%s</p>' % meta) if meta else "",
               page["lead"], toc_html, body_inner))


def hero(page, eyebrow, points=None, cta=True):
    pts = ""
    if points:
        pts = '<ul class="points">' + "".join("<li>%s</li>" % p for p in points) + "</ul>"
    ctas = ""
    if cta:
        ctas = ('<div class="cta-row"><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp: lachgas bestellen</a>'
                '<a class="btn btn-call" href="tel:%s">Bel %s</a></div>'
                '<p class="fine">Uitsluitend voor volwassenen (18+). Gebruik lachgas altijd verantwoord en in overeenstemming met de geldende wet- en regelgeving.</p>'
                % (WA_ORDER, PHONE_TEL, PHONE_DISPLAY))
    return ('<section class="hero" id="top" aria-labelledby="h1"><div class="wrap">%s<div class="hero-in">'
            '<p class="eyebrow">%s</p><h1 id="h1">%s</h1><p class="lead">%s</p>%s%s</div></div></section>'
            % (crumbs_html(page["crumbs"]) if page.get("crumbs_in_hero", True) and page["path"] != "/" else "",
               esc(eyebrow), esc(page["h1"]), page["lead"], pts, ctas))
