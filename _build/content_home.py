# -*- coding: utf-8 -*-
"""Homepage."""
from common import (SITE, BUSINESS_ID, EMAIL, PHONE_DISPLAY, PHONE_TEL, WA_DEFAULT, WA_ORDER, STADSDELEN, REGIO, TANKS,
                    esc, checks, steps, facts, faq_html, cta_block, toc, phone_link, wa_link, wa, chips, icon_cards, ICONS)
from content_areas import AREAS

FAQ = [
    ("Hoe kan ik lachgas bestellen in Amsterdam?",
     "Lachgas bestellen in Amsterdam doe je via WhatsApp of telefoon. Stuur je adres, het gewenste aantal en het moment waarop je wilt ontvangen. Wij bevestigen het levermoment en de prijs en komen daarna naar het afgesproken adres. Er is geen account, formulier of webshop nodig."),
    ("Kan ik lachgas 24/7 bestellen in Amsterdam?",
     "Ja. LachGasAdam247 is 24 uur per dag, 7 dagen per week bereikbaar via WhatsApp en telefoon, ook 's avonds laat, 's nachts, in het weekend en op feestdagen. Het levermoment stemmen we altijd vooraf met je af. Lees meer over <a href=\"/lachgas-24-7-amsterdam/\">lachgas 24/7 en 's nachts bestellen</a>."),
    ("Hoe snel wordt lachgas in Amsterdam bezorgd?",
     "Doorgaans bezorgen wij in Amsterdam binnen 20 tot 30 minuten. De exacte tijd hangt af van je locatie, het tijdstip en de drukte. Voordat wij vertrekken, laten we je weten wanneer je ons kunt verwachten. Buiten Amsterdam kan het iets langer duren."),
    ("Wat kost lachgas in Amsterdam?",
     "De prijs hangt af van het aantal en de maat die je bestelt en van het moment en de locatie van de levering. Je hoort de prijs altijd vooraf in de bevestiging, zodat je precies weet waar je aan toe bent en er geen kosten achteraf bijkomen. Stuur een WhatsApp-bericht voor de actuele prijs."),
    ("Hoe kan ik betalen?",
     "De betaalwijze bespreken we in het gesprek bij je bestelling, zodat die past bij jouw situatie. Je weet dus vooraf hoe en wanneer je betaalt."),
    ("In welke stadsdelen van Amsterdam bezorgen jullie?",
     "Wij bezorgen in alle stadsdelen van Amsterdam: Centrum, Noord, Zuid, Oost, West, Nieuw-West en Zuidoost, plus Weesp. Bekijk per stadsdeel de wijken waar wij komen op de pagina <a href=\"/bezorggebied/\">bezorggebied</a>. Twijfel je over je adres? Stuur je postcode, dan bevestigen we het direct."),
    ("Bezorgen jullie ook buiten Amsterdam, zoals in Amstelveen, Diemen, Zaandam, Haarlem, Almere en Purmerend?",
     "Ja, in de regio rond Amsterdam werken wij in overleg. Stuur je postcode via WhatsApp, dan laten we weten of we bij jou kunnen bezorgen en wat de verwachte aankomsttijd is. Omdat de afstand groter is, duurt bezorging buiten Amsterdam doorgaans iets langer."),
    ("Welke maten lachgas tanks leveren jullie?",
     "Wij leveren lachgas tanks van <a href=\"/lachgas-tanks/2kg/\">2 kg</a>, <a href=\"/lachgas-tanks/4kg/\">4 kg</a> en <a href=\"/lachgas-tanks/10kg/\">10 kg</a>. Welke maten en aantallen beschikbaar zijn, bevestigen we bij je bestelling. Twijfel je over de juiste keuze? Vraag het ons, dan adviseren we je graag."),
    ("Kan ik lachgas laten bezorgen bij een hotel of kantoor?",
     "Ja. Het leveradres mag een woning, appartement, hotel of kantoor zijn. Geef bij een hotel of bedrijf een aanspreekpunt en een geschikt moment door, zodat de overdracht soepel verloopt."),
    ("Leveren jullie ook zakelijk, bijvoorbeeld aan horeca en evenementen?",
     "Ja. We leveren zowel aan particulieren als aan zakelijke afnemers, zoals horeca en evenementen. Stuur je bedrijfsnaam, het gewenste aantal en het moment via WhatsApp mee voor een passende afspraak. Bij grotere hoeveelheden plannen we de levering vooraf. Lees meer op de pagina <a href=\"/zakelijk/\">zakelijk en evenementen</a>."),
    ("Bezorgen jullie ook op Koningsdag, tijdens Pride en tijdens het Amsterdam Dance Event?",
     "Ja, wij zijn ook op drukke dagen bereikbaar. In de stad is het dan drukker en zijn sommige straten afgesloten, dus de rit kan langer duren. Bestel daarom iets eerder en geef je adres volledig door."),
    ("Wat heb ik nodig om te bestellen?",
     "Een volledig leveradres met postcode en huisnummer (en eventueel verdieping en bel), het gewenste aantal, je gewenste tijdstip en een telefoonnummer of WhatsApp waarop je bereikbaar bent. Zakelijk geef je ook je bedrijfsnaam door."),
    ("Moet ik een account aanmaken of een formulier invullen?",
     "Nee. Je hoeft niets in te vullen op een website. Een WhatsApp-bericht of telefoontje met je adres en het gewenste aantal is genoeg."),
    ("Moet ik 18 jaar of ouder zijn om lachgas te bestellen?",
     "Ja. Lachgas is uitsluitend bestemd voor volwassenen (18+). Bij twijfel over je leeftijd kunnen we om een geldig identiteitsbewijs vragen."),
    ("Is lachgas veilig?",
     "Lachgas is bij correct en verantwoord gebruik geen onschuldig gas. Direct inademen uit een tank kan letsel veroorzaken, en veelvuldig gebruik kan leiden tot een vitamine B12-tekort en zenuwschade. Lees onze tips over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig en verantwoord gebruik</a> en gebruik het nooit voordat je gaat rijden."),
    ("Mag ik lachgas gebruiken als ik moet rijden of fietsen?",
     "Nee. Lachgas beïnvloedt je reactievermogen en evenwicht. Gebruik het nooit als je daarna nog gaat autorijden of fietsen, en nooit voordat je machines bedient. Lees meer over <a href=\"/lachgas-informatie/lachgas-en-verkeer/\">lachgas in het verkeer</a>."),
    ("Welke regels gelden voor lachgas in Nederland?",
     "Lachgas valt onder Nederlandse regelgeving; sinds 2023 staat het op lijst II van de Opiumwet, met uitzonderingen voor medische, technische en voedingsdoeleinden. Informeer jezelf over de actuele regels via rijksoverheid.nl en lees ons overzicht van de <a href=\"/lachgas-informatie/regels-en-wetgeving/\">regels en wetgeving</a>. Wij leveren alleen in lijn met de geldende wet en onze beoordeling van de order."),
    ("Wat als ik niet op het afgesproken moment aanwezig kan zijn?",
     "Zorg dat je bereikbaar bent op het afgesproken moment. Kun je toch niet aanwezig zijn? Neem dan zo snel mogelijk contact met ons op via WhatsApp of telefoon, dan kijken we samen naar een nieuw levermoment."),
    ("Kan ik mijn bestelling wijzigen of annuleren?",
     "Ja, in overleg. Neem zo snel mogelijk contact op. Is de levering al voorbereid of onderweg, dan kunnen redelijke kosten in rekening worden gebracht. Zie ook de <a href=\"/algemene-voorwaarden/\">algemene voorwaarden</a>."),
    ("Waarom bestel ik via WhatsApp of telefoon en niet via een webshop?",
     "Omdat het sneller en persoonlijker is. Je spreekt direct met ons, krijgt een duidelijke bevestiging met levermoment en prijs en hoeft geen account of formulier in te vullen. Zo blijft de lijn tussen jouw bericht en de levering zo kort mogelijk."),
    ("Hoe neem ik contact op met LachGasAdam247?",
     "Stuur een WhatsApp-bericht of bel %s. Je kunt ons ook mailen op %s. De snelste manier is WhatsApp of telefoon; wij zijn 24/7 bereikbaar." % (PHONE_DISPLAY, EMAIL)),
]


def home_page():
    path = "/"
    page = dict(
        path=path,
        title="Lachgas Amsterdam bestellen: 24/7 bezorgd | LachGasAdam247",
        description="Lachgas bestellen in Amsterdam? LachGasAdam247 bezorgt 24/7 in alle stadsdelen in 20-30 min. WhatsApp of bel %s." % PHONE_DISPLAY,
        h1="Lachgas Amsterdam bestellen: 24/7 aan huis bezorgd",
        lead="Lachgas bestellen in Amsterdam? LachGasAdam247 bezorgt lachgas tanks aan huis in alle stadsdelen van Amsterdam en in de omliggende regio. Wij zijn 24 uur per dag bereikbaar via WhatsApp en telefoon en bezorgen doorgaans binnen 20 tot 30 minuten. Stuur je adres en het gewenste aantal, ontvang een duidelijke bevestiging en wij komen naar je toe.",
        crumbs=[("Home", None)],
        faq=FAQ,
        priority="1.0", changefreq="weekly",
        speakable=["#h1", ".lead"],
    )
    page["schema"] = [
        {
            "@type": "Service",
            "@id": SITE + "/#service",
            "name": "Lachgas bezorgen in Amsterdam",
            "serviceType": "Lachgas levering en bezorging",
            "provider": {"@id": BUSINESS_ID},
            "areaServed": {"@type": "City", "name": "Amsterdam"},
            "availableChannel": [
                {"@type": "ServiceChannel", "serviceUrl": WA_DEFAULT, "name": "WhatsApp"},
                {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": PHONE_TEL, "contactType": "customer service"}, "name": "Telefoon"},
            ],
            "hoursAvailable": {"@type": "OpeningHoursSpecification",
                               "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                               "opens": "00:00", "closes": "23:59"},
        },
        {
            "@type": "ItemList",
            "@id": SITE + "/#stadsdelen",
            "name": "Bezorggebieden lachgas Amsterdam",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": "Lachgas bestellen in %s" % n, "url": SITE + "/bezorggebied/%s/" % s}
                for i, (s, n) in enumerate(STADSDELEN)
            ],
        },
        {
            "@type": "HowTo",
            "@id": SITE + "/#howto",
            "name": "Lachgas bestellen in Amsterdam via WhatsApp",
            "description": "In vier stappen lachgas bestellen en aan huis laten bezorgen in Amsterdam.",
            "totalTime": "PT30M",
            "step": [
                {"@type": "HowToStep", "position": 1, "name": "Stuur een WhatsApp-bericht of bel", "text": "Geef je adres in Amsterdam, het gewenste aantal en het moment waarop je wilt ontvangen door via WhatsApp of bel %s." % PHONE_DISPLAY},
                {"@type": "HowToStep", "position": 2, "name": "Ontvang de bevestiging", "text": "Wij bevestigen het levermoment en de prijs, zodat je vooraf weet waar je aan toe bent."},
                {"@type": "HowToStep", "position": 3, "name": "Wij rijden naar je toe", "text": "Onze bezorger rijdt naar het afgesproken adres. Doorgaans bezorgen wij in Amsterdam binnen 20 tot 30 minuten."},
                {"@type": "HowToStep", "position": 4, "name": "Veilige overdracht en betaling", "text": "De bestelling wordt op het afgesproken adres overgedragen. De betaalwijze bespreken we in het gesprek."},
            ],
        },
    ]

    stads_cards = ('<div class="areas">' + "".join(
        '<article class="area"><h3><a href="/bezorggebied/%s/">Lachgas %s</a></h3><p class="wijken"><strong>Wijken:</strong> %s.</p><p>%s</p><p><a href="/bezorggebied/%s/">Lachgas bestellen in %s &rarr;</a></p></article>'
        % (s, esc(n), ", ".join(AREAS[s]["wijken"][:7]), AREAS[s]["intro"][0].split(". ")[0] + ".", s, esc(n))
        for s, n in STADSDELEN) + "</div>")

    regio_list = ('<ul class="plain">' + "".join(
        '<li><strong><a href="/bezorggebied/%s/">Lachgas %s</a>.</strong> %s</li>' % (s, esc(n), AREAS[s]["lead"].split(". ")[0] + ".")
        for s, n in REGIO) + "</ul>")

    body = [
        # Hero
        '<section class="hero" id="top" aria-labelledby="h1"><div class="wrap"><div class="hero-in">'
        '<p class="eyebrow">Lachgas Amsterdam &middot; 24/7 bereikbaar</p><h1 id="h1">%s</h1><p class="lead">%s</p>'
        '<ul class="points"><li>24/7 beschikbaar, ook &rsquo;s nachts en in het weekend</li><li>Doorgaans bezorgd binnen 20 tot 30 minuten</li><li>Duidelijke prijs en levermoment vooraf</li><li>Alle stadsdelen van Amsterdam en de regio</li></ul>'
        '<div class="cta-row"><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp: lachgas bestellen</a><a class="btn btn-call" href="tel:%s">Bel %s</a></div>'
        '<p class="fine">Uitsluitend voor volwassenen (18+). Gebruik lachgas altijd verantwoord en in overeenstemming met de geldende wet- en regelgeving.</p>'
        '%s</div>'
        '<div class="strip">'
        '<div>%s<div><strong>1. Stuur je adres</strong><p>Via WhatsApp of telefoon, met het gewenste aantal.</p></div></div>'
        '<div>%s<div><strong>2. Bevestiging</strong><p>Je hoort direct het levermoment en de prijs.</p></div></div>'
        '<div>%s<div><strong>3. Bezorgd</strong><p>Doorgaans binnen 20 tot 30 minuten aan je deur.</p></div></div>'
        '</div></div></section>' % (esc(page["h1"]), page["lead"], WA_ORDER, PHONE_TEL, PHONE_DISPLAY,
                                    chips([("/bezorggebied/%s/" % s, n) for s, n in STADSDELEN] + [("/bezorggebied/", "Regio en meer")], "Direct naar jouw stadsdeel"),
                                    ICONS["chat"], ICONS["check"], ICONS["home"]),

        # Inhoud
        '<section class="section" id="inhoud" aria-labelledby="h-inhoud"><div class="wrap"><h2 id="h-inhoud">Inhoud: alles over lachgas Amsterdam</h2>'
        '<p class="intro">Op deze pagina vind je alles over lachgas bestellen en laten bezorgen in Amsterdam: hoe het werkt, waar wij bezorgen, wat het kost, hoe snel wij er zijn en waar je op moet letten. Kies hieronder direct het onderwerp waarin je geïnteresseerd bent.</p>%s</div></section>' % toc([
            ("#in-het-kort", "In het kort"), ("#lachgas-bestellen-amsterdam", "Lachgas bestellen"), ("#lachgas-bezorgen-amsterdam", "Lachgas bezorgen"),
            ("#bezorggebieden", "Stadsdelen"), ("#regio-amsterdam", "Regio Amsterdam"), ("#lachgas-24-7", "24/7 en 's nachts"),
            ("#feesten-evenementen-horeca", "Feesten en horeca"), ("#lachgas-tanks", "Tanks en maten"), ("#prijs-betalen", "Prijs en betaling"),
            ("#waarom-lachgasadam247", "Waarom wij"), ("#waar-op-letten", "Waar op letten"), ("#lachgas-informatie", "Informatie en veiligheid"),
            ("#faq", "Veelgestelde vragen"), ("#contact", "Contact")]),

        # In het kort
        '<section class="section alt" id="in-het-kort" aria-labelledby="h-kort"><div class="wrap"><h2 id="h-kort">Lachgas Amsterdam in het kort</h2>'
        '<p class="intro">De belangrijkste informatie over lachgas bestellen bij LachGasAdam247, overzichtelijk bij elkaar.</p>%s</div></section>' % facts([
            ("Bezorggebied", 'Heel Amsterdam (Centrum, Noord, Zuid, Oost, West, Nieuw-West, Zuidoost en Weesp) en de regio, waaronder Amstelveen, Diemen, Zaandam, Haarlem, Hoofddorp, Almere en Purmerend. Zie <a href="/bezorggebied/">bezorggebied</a>'),
            ("Bereikbaar", "24 uur per dag, 7 dagen per week, via WhatsApp en telefoon"),
            ("Bestellen via", '%s of bel %s' % (wa_link("WhatsApp"), phone_link())),
            ("Levertijd", "Doorgaans 20 tot 30 minuten in Amsterdam; in de regio en bij drukte iets langer. De aankomsttijd bevestigen we altijd vooraf"),
            ("Prijs", "Vooraf bevestigd in het gesprek, zonder kosten achteraf"),
            ("Betaling", "De betaalwijze bespreken we bij je bestelling"),
            ("Producten", '<a href="/lachgas-tanks/">Lachgas tanks</a> van 2 kg, 4 kg en 10 kg'),
            ("Klanten", 'Particulieren en <a href="/zakelijk/">zakelijke afnemers</a>, zoals horeca en evenementen'),
            ("Leeftijd", "Uitsluitend voor volwassenen (18+)"),
            ("E-mail", '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)),
        ]),

        # Bestellen
        '<section class="section" id="lachgas-bestellen-amsterdam" aria-labelledby="h-bestellen"><div class="wrap prose"><h2 id="h-bestellen">Lachgas bestellen in Amsterdam: zo werkt het</h2>'
        '<p>Lachgas bestellen in Amsterdam bij LachGasAdam247 gaat zonder webshop, zonder account en zonder wachtrij. Je stuurt een WhatsApp-bericht of belt, en regelt alles in één gesprek. Zo blijft de lijn kort, van je eerste bericht tot de levering aan je deur. Hieronder lees je precies hoe het werkt en wat je kunt verwachten.</p>%s'
        '<h3>Wat geef je door bij je bestelling?</h3>%s'
        '<h3>Geen formulier en geen account nodig</h3><p>Veel bezorgdiensten laten je eerst een account aanmaken of een formulier invullen. Bij ons niet. Je hoeft geen gegevens in te voeren op een website: een bericht met je adres en het gewenste aantal is genoeg. Dat scheelt tijd en houdt het overzichtelijk. Lachgas kopen in Amsterdam is bij ons dus niet meer dan een gesprek.</p>'
        '<h3>Tips voor een snelle bestelling</h3>%s</div></section>' % (
            steps([
                "<strong>Stuur een WhatsApp-bericht of bel.</strong> Geef je adres in Amsterdam, het gewenste aantal en het moment waarop je wilt ontvangen. Bel je liever? Dat kan ook: wij zijn 24/7 bereikbaar op %s." % phone_link(),
                "<strong>Ontvang de bevestiging.</strong> Wij bevestigen het levermoment en de prijs. Je weet dus vooraf waar je aan toe bent en er komen geen verrassingen achteraf.",
                "<strong>Wij rijden naar je toe.</strong> Onze bezorger rijdt naar het afgesproken adres in Amsterdam of omstreken. Doorgaans bezorgen wij in Amsterdam binnen 20 tot 30 minuten.",
                "<strong>Veilige overdracht en betaling.</strong> De bestelling wordt op het afgesproken adres overgedragen. De betaalwijze bespreken we in het gesprek, zodat die past bij jouw situatie.",
            ]),
            checks([
                "Je volledige leveradres: straat, huisnummer, postcode en eventueel de verdieping.",
                "De juiste bel of ingang, bijvoorbeeld bij een portiek, gedeelde voordeur of intercom.",
                "Het gewenste aantal of de maat tank die je wilt hebben.",
                "Het moment waarop je de levering wilt ontvangen.",
                "Een nummer waarop je bereikbaar bent zodra onze bezorger in de buurt is.",
                "Voor zakelijke bestellingen: je bedrijfsnaam en een aanspreekpunt.",
            ]),
            checks([
                "Geef je adres zo volledig mogelijk door. Dat scheelt de meeste tijd bij de levering.",
                "Bestel iets eerder op drukke momenten, zoals in het weekend, op Koningsdag en tijdens grote evenementen.",
                "Houd je telefoon bij de hand zodra je hebt besteld, zodat wij je kunnen bereiken.",
                "Twijfel je over de hoeveelheid? Vraag het ons, dan denken wij graag met je mee.",
            ])),

        # Bezorgen
        '<section class="section alt" id="lachgas-bezorgen-amsterdam" aria-labelledby="h-bezorgen"><div class="wrap prose"><h2 id="h-bezorgen">Lachgas bezorgen in Amsterdam: snel en 24/7</h2>'
        '<p>LachGasAdam247 bezorgt lachgas in Amsterdam op elk moment van de dag en nacht. Doorgaans bezorgen wij binnen 20 tot 30 minuten nadat je bestelling is bevestigd. De exacte tijd hangt af van je locatie, het tijdstip en de drukte op de weg. Voordat wij vertrekken, laten we je altijd weten wanneer je ons kunt verwachten.</p>'
        '<h3>Wat bepaalt de levertijd?</h3>%s'
        '<h3>Amsterdam is compact, maar niet altijd makkelijk</h3><p>Amsterdam ligt rond het IJ en de Amstel, met bruggen, smalle grachten, autoluwe zones en veel tram- en fietsverkeer. De Noord/Zuidlijn, de pont en de IJtunnel verbinden Noord met de rest van de stad, en de A10 loopt als ring om Amsterdam. Bij het plannen van de rit houden we rekening met deze routes, zodat je niet langer wacht dan nodig. Woon je in een stadsdeel dat verder van het centrum ligt, zoals Zuidoost, Nieuw-West of Noord, dan bevestigen we de aankomsttijd extra duidelijk.</p>'
        '<h3>Bezorgd op elk adres</h3><p>Je kunt lachgas laten bezorgen bij een woning, appartement, hotel of kantoor in Amsterdam. Geef bij een hotel of bedrijf een aanspreekpunt en een geschikt moment door. Is je adres lastig te vinden, of woon je op een verdieping zonder duidelijke bel? Laat het weten bij je bestelling, dan spreken we een herkenningspunt of een goed bereikbare plek in de buurt af.</p></div></section>' % checks([
            "<strong>Je locatie.</strong> In het centrum en de stadsdelen dichtbij zijn we doorgaans het snelst ter plekke. Aan de rand van de stad of aan de overkant van het IJ kan het iets langer duren.",
            "<strong>Het tijdstip.</strong> Overdag in de spits is het drukker op de weg dan &rsquo;s nachts. In het weekend en tijdens uitgaansuren zijn sommige straten drukker.",
            "<strong>Evenementen en afsluitingen.</strong> Koningsdag, Pride, het Amsterdam Dance Event en wedstrijden in de Johan Cruijff ArenA zorgen voor drukte en afgesloten straten.",
            "<strong>Bereikbaarheid van je adres.</strong> Een adres in een autoluwe zone of aan een smalle gracht vraagt om een goede afspraak over de plek van overdracht.",
        ]),

        # Stadsdelen
        '<section class="section" id="bezorggebieden" aria-labelledby="h-gebieden"><div class="wrap"><h2 id="h-gebieden">Lachgas bezorgen in alle stadsdelen van Amsterdam</h2>'
        '<p class="intro">Amsterdam (020) bestaat uit zeven stadsdelen, aangevuld met Weesp. LachGasAdam247 bezorgt lachgas in elk stadsdeel. Klik op je stadsdeel voor de wijken, bezorgtips en veelgestelde vragen. Staat jouw buurt er niet bij? Stuur je postcode via WhatsApp, dan bevestigen we direct of we bij jou kunnen bezorgen.</p>%s'
        '<p style="margin-top:1.25rem"><a href="/bezorggebied/">Bekijk het volledige bezorggebied &rarr;</a></p></div></section>' % stads_cards,

        # Regio
        '<section class="section alt" id="regio-amsterdam" aria-labelledby="h-regio"><div class="wrap prose"><h2 id="h-regio">Lachgas in de regio Amsterdam</h2>'
        '<p>Naast Amsterdam zelf werken wij in de omliggende gemeenten. Omdat de afstand daar groter is, plannen we deze leveringen in overleg en bevestigen we de verwachte aankomsttijd vooraf. Stuur je postcode via WhatsApp of bel %s, dan weet je meteen of en wanneer we bij je kunnen zijn.</p>%s</div></section>' % (phone_link(), regio_list),

        # 24/7
        '<section class="section" id="lachgas-24-7" aria-labelledby="h-247"><div class="wrap prose"><h2 id="h-247">Lachgas 24/7 en &rsquo;s nachts bestellen in Amsterdam</h2>'
        '<p>Amsterdam is een stad die nooit helemaal stilvalt, en onze bereikbaarheid ook niet. LachGasAdam247 is 24 uur per dag, 7 dagen per week bereikbaar via WhatsApp en telefoon. Dat betekent dat je ook &rsquo;s avonds laat, &rsquo;s nachts, in het weekend en op feestdagen een bericht kunt sturen. We bevestigen het levermoment en de prijs, en bezorgen doorgaans binnen 20 tot 30 minuten.</p>'
        '<p>Van het Leidseplein, het Rembrandtplein en de Wallen in het centrum tot De Pijp, Oost, de NDSM-werf in Noord en de omgeving van de Ziggo Dome in Zuidoost: wij bezorgen op een adres in heel Amsterdam. Lees meer over <a href="/lachgas-24-7-amsterdam/">lachgas 24/7 en &rsquo;s nachts bestellen</a>.</p></div></section>',

        # Feesten
        '<section class="section alt" id="feesten-evenementen-horeca" aria-labelledby="h-feest"><div class="wrap prose"><h2 id="h-feest">Lachgas voor feesten, evenementen en horeca in Amsterdam</h2>'
        '<p>LachGasAdam247 levert aan particulieren en aan zakelijke afnemers. Of je nu een verjaardag thuis organiseert, een borrel op kantoor, een evenement of een horecazaak runt: het bestelproces is hetzelfde. Stuur je adres, het gewenste aantal en het moment, en wij bevestigen de levering. Voor grotere hoeveelheden, 10 kg tanks en levering op een specifiek tijdstip plannen we de bezorging vooraf.</p>'
        '<p>Op Koningsdag, tijdens Pride, het Amsterdam Dance Event, Oud en Nieuw en bij evenementen in de ArenA, de Ziggo Dome en de RAI zijn wij gewoon bereikbaar; bestel dan iets eerder. Lees meer op de pagina <a href="/zakelijk/">lachgas voor horeca, feesten en evenementen</a>.</p></div></section>',

        # Tanks
        '<section class="section" id="lachgas-tanks" aria-labelledby="h-tanks"><div class="wrap prose"><h2 id="h-tanks">Lachgas tanks en cilinders: maten en hoeveelheden</h2>'
        '<p>LachGasAdam247 levert lachgas tanks in drie maten. Welke maat en welk aantal het beste past, hangt af van je situatie: een kleine groep thuis, een huisfeest of een evenement. Welke maten en hoeveelheden beschikbaar zijn, bevestigen we bij je bestelling. Twijfel je? Stuur een WhatsApp-bericht, dan denken wij graag met je mee.</p>%s'
        '<h3>Lachgas kopen in Amsterdam zonder gedoe</h3><p>Wie lachgas wil kopen in Amsterdam, zoekt vaak een aanbieder die snel, duidelijk en betrouwbaar is. Bij LachGasAdam247 weet je vooraf welke tank je krijgt, wanneer wij komen en wat de prijs is. Geen verborgen kosten, geen omwegen. Bekijk het <a href="/lachgas-tanks/">overzicht van alle lachgas tanks</a> en lees hoe je een tank <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">veilig bewaart en vervoert</a>.</p></div></section>' % toc([("/lachgas-tanks/%s/" % s, n) for s, n in TANKS]),

        # Prijs
        '<section class="section alt" id="prijs-betalen" aria-labelledby="h-prijs"><div class="wrap prose"><h2 id="h-prijs">Wat kost lachgas in Amsterdam? Prijs en betaling</h2>'
        '<p>Een van de meest gestelde vragen is wat lachgas in Amsterdam kost. De prijs hangt af van het aantal en de maat die je bestelt en van het moment en de locatie van de levering. Daarom hanteren wij geen vaste prijslijst op deze website, maar bevestigen we de prijs altijd vooraf in het gesprek.</p>'
        '<h3>Zo weet je waar je aan toe bent</h3>%s'
        '<h3>Betaling</h3><p>De betaalwijze bespreken we in het gesprek bij je bestelling, zodat die past bij jouw situatie. Zo weet je vooraf hoe en wanneer je betaalt. Voor de precieze afspraken verwijzen wij naar onze <a href="/algemene-voorwaarden/">algemene voorwaarden</a>.</p>'
        '<p>Wil je nu weten wat lachgas in Amsterdam kost? Stuur een bericht via %s of bel %s.</p></div></section>' % (checks([
            "Je stuurt je adres en het gewenste aantal via WhatsApp of telefoon.",
            "Je ontvangt de prijs en het levermoment in de bevestiging, voordat wij vertrekken.",
            "Je betaalt wat is afgesproken: er komen geen kosten achteraf bij.",
        ]), wa_link("WhatsApp"), phone_link()),

        # Waarom
        '<section class="section" id="waarom-lachgasadam247" aria-labelledby="h-waarom"><div class="wrap"><h2 id="h-waarom">Waarom lachgas bestellen bij LachGasAdam247</h2>'
        '<p class="intro">Lachgas Amsterdam bezorgen doen wij anders: minder gedoe, meer duidelijkheid bij elke bestelling.</p>%s'
        '<p style="margin-top:1.25rem"><a href="/over-ons/">Meer over LachGasAdam247 &rarr;</a></p></div></section>' % icon_cards([
            ("moon", "24/7 bereikbaar", "Dag en nacht, doordeweeks en in het weekend: je kunt ons altijd bereiken via WhatsApp of telefoon."),
            ("bolt", "Snel ter plekke", "Doorgaans bezorgen wij binnen 20 tot 30 minuten en we laten altijd vooraf weten wanneer je ons kunt verwachten."),
            ("tag", "Duidelijke prijs vooraf", "Levermoment en prijs staan vooraf vast. Geen kosten achteraf, geen vage beloftes."),
            ("pin", "Gefocust op Amsterdam", "Amsterdam en omstreken zijn onze thuisbasis. We plannen routes op de stad en houden rekening met drukte en afsluitingen."),
            ("users", "Particulier en zakelijk", "Van een bestelling thuis tot horeca en evenementen: het bestelproces is hetzelfde en we denken graag mee."),
            ("noform", "Geen formulier of account", "Een bericht met je adres en aantal is genoeg. Geen webshop, geen inlog, geen wachtrij."),
        ]),

        # Waar op letten
        '<section class="section alt" id="waar-op-letten" aria-labelledby="h-letten"><div class="wrap prose"><h2 id="h-letten">Waar let je op bij een lachgas bezorgdienst in Amsterdam?</h2>'
        '<p>Er zijn veel aanbieders die lachgas bezorgen in Amsterdam. Met deze acht punten herken je een betrouwbare dienst, en zo werken wij.</p>%s</div></section>' % steps([
            "<strong>Een duidelijke prijs vooraf.</strong> Je hoort het bedrag voordat er gereden wordt, zonder toeslagen achteraf.",
            "<strong>Echt persoonlijk contact.</strong> Je spreekt of appt met een mens, niet met een chatbot of een wachtrij.",
            "<strong>Eerlijke levertijden.</strong> Een aanbieder die eerlijk is over de aankomsttijd en die vooraf bevestigt.",
            "<strong>Bereikbaarheid.</strong> Ook &rsquo;s avonds, &rsquo;s nachts en in het weekend kun je contact opnemen.",
            "<strong>Lokale kennis.</strong> Kennis van de stadsdelen, de routes en de drukke momenten in Amsterdam.",
            "<strong>Veilige overdracht.</strong> Een zorgvuldige afhandeling op het afgesproken adres.",
            "<strong>Duidelijke voorwaarden en contactgegevens.</strong> Voorwaarden, privacyverklaring en contactgegevens staan gewoon op de site: <a href=\"/algemene-voorwaarden/\">algemene voorwaarden</a>, <a href=\"/privacy/\">privacyverklaring</a> en <a href=\"/contact/\">contact</a>.",
            "<strong>Verantwoordelijk handelen.</strong> Alleen aan volwassenen en in lijn met de geldende regels, met eerlijke informatie over risico&rsquo;s.",
        ]),

        # Informatie & veiligheid
        '<section class="section" id="lachgas-informatie" aria-labelledby="h-info"><div class="wrap prose"><h2 id="h-info">Informatie, veilig gebruik en regels</h2>'
        '<p>Lachgas (distikstofmonoxide, N<sub>2</sub>O) is een kleurloos gas dat al sinds 1772 bekend is en wordt gebruikt in de zorg, de horeca en de techniek. Het is bij correct gebruik geen onschuldig gas: direct inademen uit een tank kan letsel veroorzaken en veelvuldig gebruik kan leiden tot een vitamine B12-tekort en zenuwschade. Lachgas is uitsluitend bestemd voor volwassenen (18+). Gebruik het nooit voordat je gaat rijden of fietsen, combineer het niet met alcohol of andere drugs en houd rekening met de geldende wet- en regelgeving.</p>%s'
        '<div class="callout"><p><strong>Acute klachten of een noodgeval?</strong> Bel direct 112. Betrouwbare, onafhankelijke informatie vind je bij <a href="https://www.drugsinfo.nl" target="_blank" rel="noopener nofollow">Drugsinfo van het Trimbos-instituut</a>.</p></div></div></section>' % toc([
            ("/lachgas-informatie/wat-is-lachgas/", "Wat is lachgas?"),
            ("/lachgas-informatie/veilig-gebruik/", "Veilig en verantwoord gebruik"),
            ("/lachgas-informatie/lachgas-en-verkeer/", "Lachgas in het verkeer"),
            ("/lachgas-informatie/regels-en-wetgeving/", "Regels en wetgeving"),
            ("/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/", "Tank bewaren en vervoeren"),
            ("/lachgas-informatie/lachgas-en-vitamine-b12/", "Lachgas en vitamine B12"),
        ]),

        faq_html(FAQ, "Veelgestelde vragen over lachgas in Amsterdam",
                 "Antwoorden op de vragen die wij het vaakst krijgen over lachgas bestellen, bezorgen en gebruiken in Amsterdam. Staat jouw vraag er niet bij? Stuur ons een WhatsApp-bericht."),

        # Contact
        '<section class="section" id="contact" aria-labelledby="h-contact"><div class="wrap"><h2 id="h-contact">Contact: lachgas bestellen in Amsterdam</h2>'
        '<p class="intro">Wij zijn 24 uur per dag, 7 dagen per week bereikbaar. De snelste manier om lachgas te bestellen is via WhatsApp of telefoon.</p><div class="cards contact">'
        '<div class="card"><h3>WhatsApp</h3><p>Stuur je adres en het gewenste aantal. Wij bevestigen levermoment en prijs.</p><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Open WhatsApp</a></div>'
        '<div class="card"><h3>Telefoon</h3><p>Liever praten over levering en details? Bel ons, ook &rsquo;s nachts.</p><a class="btn btn-call" href="tel:%s">Bel %s</a></div>'
        '<div class="card"><h3>E-mail</h3><p>Voor vragen die geen haast hebben.</p><a class="btn btn-call" href="mailto:%s">%s</a></div>'
        '</div></div></section>' % (WA_ORDER, PHONE_TEL, PHONE_DISPLAY, EMAIL, EMAIL),
    ]
    page["body"] = "".join(body)
    return page


def pages():
    return [home_page()]
