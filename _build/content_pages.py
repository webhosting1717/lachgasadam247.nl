# -*- coding: utf-8 -*-
"""Overige pagina's: zakelijk, 24/7, over ons, contact, privacy, algemene voorwaarden, 404."""
from common import (SITE, BUSINESS_ID, EMAIL, PHONE_DISPLAY, PHONE_TEL, WA_DEFAULT, WA_ORDER, esc, hero, checks, steps,
                    facts, faq_html, cta_block, toc, phone_link, wa_link, wa, doc_page, crumbs_html)


def zakelijk_page():
    path = "/zakelijk/"
    page = dict(
        path=path,
        title="Lachgas zakelijk bestellen Amsterdam | Horeca en evenementen",
        description="Lachgas zakelijk bestellen in Amsterdam? Levering aan horeca, evenementen en bedrijven: grotere aantallen, 10 kg tanks, op afspraak. Bel %s." % PHONE_DISPLAY,
        h1="Lachgas voor feesten, evenementen en horeca in Amsterdam",
        lead="LachGasAdam247 levert aan particulieren én zakelijke afnemers. Of je nu een verjaardag thuis organiseert, een borrel op kantoor, een festival-afterparty, een evenement of een horecazaak runt: wij leveren de juiste hoeveelheid op het juiste moment. Grotere aantallen en 10 kg tanks plannen we vooraf met je in.",
        crumbs=[("Home", "/"), ("Zakelijk en evenementen", None)],
        priority="0.8", changefreq="monthly", auto_toc=True,
        faq=[
            ("Leveren jullie ook zakelijk, bijvoorbeeld aan horeca en evenementen?",
             "Ja. We leveren zowel aan particulieren als aan zakelijke afnemers, zoals horeca, clubs, eventlocaties, festivals en bedrijven. Stuur je bedrijfsnaam, het gewenste aantal en het moment via WhatsApp mee voor een passende afspraak."),
            ("Kan ik een vaste leverafspraak maken voor mijn horecazaak?",
             "Ja. Voor horeca en clubs maken we graag afspraken over vaste levermomenten en aantallen, zodat je nooit zonder zit. Neem contact op via WhatsApp of bel ons."),
            ("Hoeveel lachgas heb ik nodig voor een feest of evenement?",
             "Dat hangt af van het aantal gasten en de duur. Voor een huisfeest met tien tot twintig personen volstaat vaak een 4 kg tank; voor grote feesten en evenementen leveren we 10 kg tanks, eventueel meerdere. Vertel ons wat je organiseert, dan adviseren we over de hoeveelheid."),
            ("Kunnen jullie op een specifiek tijdstip leveren?",
             "Ja. Bij zakelijke bestellingen en evenementen spreken we vooraf een tijdstip en een plek van overdracht af, bijvoorbeeld bij een laad- en losplek, een personeelsingang of een receptie."),
            ("Krijg ik een factuur?",
             "Vraag ernaar bij je bestelling; we bespreken de betaal- en factuurafspraken in het gesprek."),
        ],
        speakable=["#h1", ".lead"],
    )
    page["schema"] = [{
        "@type": "Service",
        "@id": SITE + path + "#service",
        "name": "Zakelijke lachgas levering Amsterdam",
        "serviceType": "Lachgas levering voor horeca en evenementen",
        "provider": {"@id": BUSINESS_ID},
        "areaServed": {"@type": "City", "name": "Amsterdam"},
        "audience": {"@type": "BusinessAudience", "name": "Horeca, evenementen en bedrijven"},
        "url": SITE + path,
    }]
    body = [
        hero(page, "Zakelijk · feesten · horeca", ["Grotere aantallen en 10 kg tanks", "Levering op afspraak, ook 's nachts", "Vaste afspraken voor horeca en clubs", "Prijs vooraf bevestigd"]),
        '<section class="section" aria-labelledby="h-part"><div class="wrap prose"><h2 id="h-part" data-nav="Particulier">Particulier: thuis, feest of borrel</h2>'
        '<p>Voor een gewone bestelling is een WhatsApp-bericht voldoende; wij bezorgen doorgaans binnen 20 tot 30 minuten in heel Amsterdam. Organiseer je een verjaardag, een housewarming of een borrel met een grotere groep? Kies dan een <a href="/lachgas-tanks/4kg/">4 kg tank</a> of bestel meerdere tanks tegelijk. Voor grotere hoeveelheden of een levering op een specifiek tijdstip raden we aan vooraf contact op te nemen, zodat we de bezorging goed kunnen plannen.</p>'
        '<h3>Tips voor een feest thuis</h3>%s</div></section>' % checks([
            "Bestel op tijd, zeker in het weekend, op Koningsdag en tijdens grote evenementen.",
            "Geef het aantal gasten door, dan adviseren we over de maat en het aantal tanks.",
            "Zet de tank op een vaste, geventileerde plek waar hij niet kan omvallen en waar gasten er niet mee gaan slepen.",
            "Spreek af dat niemand daarna nog rijdt of fietst. Lees onze tips over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig en verantwoord gebruik</a>.",
        ]),
        '<section class="section alt" aria-labelledby="h-zak"><div class="wrap prose"><h2 id="h-zak" data-nav="Zakelijk">Zakelijk: horeca, clubs, evenementen en bedrijven</h2>'
        '<p>Bestel je zakelijk, geef dan je bedrijfsnaam, het leveradres, een aanspreekpunt en het gewenste aantal door. Bij evenementen en horeca is een goede afspraak over het moment en de plek van overdracht extra belangrijk, bijvoorbeeld bij een laad- en losplek, een personeelsingang of de receptie. We stemmen dat graag met je af en plannen bij grotere hoeveelheden de levering vooraf.</p>'
        '<h3>Voor wie</h3>%s'
        '<h3>Wat wij bieden</h3>%s</div></section>' % (
            checks([
                "<strong>Horeca en clubs</strong> in het centrum, De Pijp, Oost, Noord en rond het Rembrandtplein en Leidseplein: vaste levermomenten en aantallen.",
                "<strong>Evenementen en festivals</strong>: afterparty's, privéfeesten, bedrijfsfeesten en gehuurde locaties in Amsterdam en de regio.",
                "<strong>Eventlocaties en organisatoren</strong>: levering op afspraak bij de locatie, met een aanspreekpunt ter plaatse.",
                "<strong>Bedrijven en kantoren</strong>: borrels en personeelsfeesten op de Zuidas, bij Sloterdijk, in Zuidoost en in het centrum.",
            ]),
            checks([
                "<strong>Alle maten</strong>: <a href=\"/lachgas-tanks/2kg/\">2 kg</a>, <a href=\"/lachgas-tanks/4kg/\">4 kg</a> en <a href=\"/lachgas-tanks/10kg/\">10 kg tanks</a>, ook in grotere aantallen.",
                "<strong>Levering op afspraak</strong>, ook &rsquo;s nachts en in het weekend. Wij zijn 24/7 bereikbaar.",
                "<strong>Eén aanspreekpunt</strong> via WhatsApp of telefoon, met een duidelijke bevestiging van aantal, moment en prijs.",
                "<strong>Kennis van de stad</strong>: we houden rekening met afsluitingen, evenementen en laad- en losplekken.",
            ])),
        '<section class="section" aria-labelledby="h-druk"><div class="wrap prose"><h2 id="h-druk" data-nav="Drukke momenten">Drukke momenten in Amsterdam</h2>'
        '<p>Op deze dagen is de stad extra druk en zijn straten afgesloten. Wij zijn dan gewoon bereikbaar, maar bestel eerder en geef je adres volledig door.</p>%s'
        '<p>Op al deze dagen bevestigen we de verwachte aankomsttijd voordat we vertrekken, zodat je weet waar je aan toe bent. Lees ook over <a href="/lachgas-24-7-amsterdam/">lachgas 24/7 en &rsquo;s nachts bestellen</a>.</p></div></section>' % checks([
            "<strong>Koningsdag (27 april).</strong> De hele stad is op de been en veel straten en grachten zijn afgesloten.",
            "<strong>Amsterdam Pride en de Canal Parade (begin augustus).</strong> Rond de grachten is het erg druk en zijn bruggen afgesloten.",
            "<strong>Amsterdam Dance Event (oktober).</strong> Het uitgaansleven is dagenlang extra druk, vooral in het centrum en bij de festivallocaties.",
            "<strong>Oud en Nieuw.</strong> Straten vol, vuurwerkdrukte en langere ritten.",
            "<strong>Evenementen in de Johan Cruijff ArenA, de Ziggo Dome en de RAI.</strong> Rond deze locaties in Zuidoost en Zuid is het drukker op de weg.",
        ]),
        '<section class="section alt" aria-labelledby="h-zo"><div class="wrap prose"><h2 id="h-zo" data-nav="Zo werkt het">Zo werkt een zakelijke bestelling</h2>%s</div></section>' % steps([
            "<strong>Stuur je aanvraag via WhatsApp of bel %s.</strong> Vermeld je bedrijfsnaam, het leveradres, het gewenste aantal en het moment." % phone_link(),
            "<strong>Wij bevestigen.</strong> Je ontvangt een bevestiging met aantal, maat, levermoment, plek van overdracht en prijs.",
            "<strong>Levering op afspraak.</strong> Onze bezorger komt op het afgesproken moment naar de afgesproken plek en meldt zich bij je aanspreekpunt.",
            "<strong>Veilige overdracht en betaling.</strong> Betaal- en factuurafspraken bespreken we in het gesprek.",
        ]),
        faq_html(page["faq"], "Veelgestelde vragen over zakelijk bestellen"),
        cta_block("Zakelijke aanvraag of feest? Neem contact op", wa_text="LachGasAdam247 - zakelijke aanvraag. Bedrijf: , adres: , aantal: , moment: "),
    ]
    page["body"] = "".join(body)
    return page


def nacht_page():
    path = "/lachgas-24-7-amsterdam/"
    page = dict(
        path=path,
        title="Lachgas 24/7 en 's nachts bestellen in Amsterdam",
        description="Lachgas 's nachts bestellen in Amsterdam? 24/7 bereikbaar, ook in weekend en op feestdagen, bezorgd in 20-30 min. WhatsApp of bel %s." % PHONE_DISPLAY,
        h1="Lachgas 24/7 en 's nachts bestellen in Amsterdam",
        lead="Amsterdam is een stad die nooit helemaal stilvalt, en onze bereikbaarheid ook niet. LachGasAdam247 is 24 uur per dag, 7 dagen per week bereikbaar via WhatsApp en telefoon. Ook 's avonds laat, 's nachts, in het weekend en op feestdagen bevestigen we je bestelling en bezorgen we doorgaans binnen 20 tot 30 minuten.",
        crumbs=[("Home", "/"), ("Lachgas 24/7", None)],
        priority="0.8", changefreq="monthly", auto_toc=True,
        faq=[
            ("Kan ik lachgas 's nachts bestellen in Amsterdam?",
             "Ja. LachGasAdam247 is 24 uur per dag bereikbaar via WhatsApp en telefoon, ook 's nachts, in het weekend en op feestdagen. Stuur je adres en het gewenste aantal, dan bevestigen we het levermoment en de prijs."),
            ("Is bezorgen 's nachts duurder?",
             "De prijs hangt af van het aantal, de maat, het moment en de locatie. Je hoort de prijs altijd vooraf in de bevestiging, ook 's nachts. Er komen geen kosten achteraf bij."),
            ("Hoe snel zijn jullie 's nachts?",
             "'s Nachts is het rustiger op de weg, waardoor we in Amsterdam doorgaans binnen 20 tot 30 minuten zijn. In uitgaansgebieden en bij evenementen kan het iets langer duren."),
            ("Bezorgen jullie ook op feestdagen?",
             "Ja. Wij zijn 7 dagen per week en ook op feestdagen bereikbaar, inclusief Koningsdag, Oud en Nieuw en tijdens Pride en het Amsterdam Dance Event. Op drukke dagen kan de levertijd iets langer zijn."),
        ],
        speakable=["#h1", ".lead"],
    )
    page["schema"] = [{
        "@type": "Service",
        "@id": SITE + path + "#service",
        "name": "Lachgas 24/7 bezorgen in Amsterdam",
        "serviceType": "Lachgas nachtbezorging",
        "provider": {"@id": BUSINESS_ID},
        "areaServed": {"@type": "City", "name": "Amsterdam"},
        "hoursAvailable": {"@type": "OpeningHoursSpecification",
                           "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                           "opens": "00:00", "closes": "23:59"},
        "url": SITE + path,
    }]
    body = [
        hero(page, "24/7 · ook 's nachts", ["Elke dag, elk uur bereikbaar", "Ook weekend en feestdagen", "Doorgaans 20 tot 30 minuten", "Prijs en levermoment vooraf"]),
        '<section class="section" aria-labelledby="h-nacht"><div class="wrap prose"><h2 id="h-nacht" data-nav="Bestellen ’s nachts">Zo werkt een bestelling &rsquo;s nachts</h2>%s'
        '<p>Bestel je &rsquo;s nachts, geef je adres dan extra duidelijk door en vermeld de verdieping en de juiste bel, zodat er geen tijd verloren gaat. Houd je telefoon bij de hand: onze bezorger stuurt een bericht of belt zodra hij in de straat is.</p></div></section>' % steps([
            "<strong>Stuur een WhatsApp-bericht</strong> met je volledige adres, de verdieping en de juiste bel, of bel %s." % phone_link(),
            "<strong>Je ontvangt een bevestiging</strong> met levermoment en prijs.",
            "<strong>Houd je telefoon bij de hand</strong>, zodat onze bezorger je kan bereiken zodra hij in de straat is.",
            "<strong>Wij bezorgen</strong> op het afgesproken adres en zorgen voor een veilige overdracht.",
        ]),
        '<section class="section alt" aria-labelledby="h-uit"><div class="wrap prose"><h2 id="h-uit" data-nav="Uitgaanswijken">Ook in de uitgaanswijken van Amsterdam</h2>'
        '<p>Van het Leidseplein, het Rembrandtplein en de Wallen in het <a href="/bezorggebied/amsterdam-centrum/">centrum</a> tot <a href="/bezorggebied/amsterdam-zuid/">De Pijp</a>, de Javastraat in <a href="/bezorggebied/amsterdam-oost/">Oost</a>, de NDSM-werf in <a href="/bezorggebied/amsterdam-noord/">Noord</a>, de Foodhallen in <a href="/bezorggebied/amsterdam-west/">West</a> en de omgeving van de Ziggo Dome in <a href="/bezorggebied/amsterdam-zuidoost/">Zuidoost</a>: wij bezorgen &rsquo;s nachts op een adres in heel Amsterdam. Wij leveren bij woningen, appartementen, hotels en kantoren, niet op straat.</p>'
        '<h3>Weekend en feestdagen</h3>'
        '<p>In het weekend en op feestdagen is het drukker in de stad. Op Koningsdag, tijdens Pride, het Amsterdam Dance Event en met Oud en Nieuw zijn straten afgesloten en kan de rit langer duren. Wij zijn op al die dagen bereikbaar en bevestigen de verwachte aankomsttijd altijd voordat we vertrekken. Bestel op die dagen iets eerder.</p>'
        '<h3>Waarom &rsquo;s nachts vaak juist snel</h3>'
        '<p>&rsquo;s Nachts is het rustig op de ring en in de stad. Geen spits, geen laad- en losverkeer en minder afsluitingen. Daardoor zijn onze bezorgers tussen middernacht en de vroege ochtend vaak juist snel ter plekke, ook in stadsdelen die verder van het centrum liggen, zoals Noord, Nieuw-West en Zuidoost.</p></div></section>',
        '<section class="section" aria-labelledby="h-ver"><div class="wrap prose"><h2 id="h-ver" data-nav="Verantwoord">Verantwoord blijven, ook &rsquo;s nachts</h2>'
        '<p>Lachgas is uitsluitend bestemd voor volwassenen (18+). Gebruik het nooit voordat je gaat rijden of fietsen, combineer het niet met alcohol of andere drugs, ga zitten en zorg voor frisse lucht. Juist &rsquo;s nachts, na een avond uit, is de combinatie met alcohol een groot risico. Lees onze tips over <a href="/lachgas-informatie/veilig-gebruik/">veilig en verantwoord gebruik</a> en over <a href="/lachgas-informatie/lachgas-en-verkeer/">lachgas in het verkeer</a>.</p>'
        '<div class="callout"><p><strong>Acute klachten of een noodgeval?</strong> Bel direct 112.</p></div></div></section>',
        faq_html(page["faq"], "Veelgestelde vragen over 24/7 bestellen"),
        cta_block("Nu bestellen, dag of nacht"),
    ]
    page["body"] = "".join(body)
    return page


def over_ons_page():
    path = "/over-ons/"
    page = dict(
        path=path,
        title="Over LachGasAdam247 | Lachgas bezorgservice Amsterdam",
        description="LachGasAdam247 is een Amsterdamse bezorgservice voor lachgas tanks: 24/7 bereikbaar, alle stadsdelen en de regio, prijs vooraf en verantwoord beleid (18+).",
        h1="Over LachGasAdam247",
        lead="LachGasAdam247 is een Amsterdamse bezorgservice voor lachgas tanks. Wij zijn 24 uur per dag bereikbaar via WhatsApp en telefoon, bezorgen in alle stadsdelen van Amsterdam en in de regio, en werken met een duidelijke prijs en een bevestigd levermoment. Geen webshop, geen account, geen wachtrij: gewoon een bericht en een bezorger aan je deur.",
        crumbs=[("Home", "/"), ("Over ons", None)],
        priority="0.5", changefreq="monthly",
        speakable=["#h1", ".lead"],
    )
    page["schema"] = [{"@type": "AboutPage", "@id": SITE + path + "#about", "url": SITE + path, "mainEntity": {"@id": BUSINESS_ID}}]
    body = [
        doc_page(page,
                 '<h2>Hoe wij werken</h2>'
                 '<p>Wij zijn begonnen omdat lachgas bestellen in Amsterdam vaak onnodig ingewikkeld was: onduidelijke prijzen, vage levertijden en bezorgers die de stad niet kenden. Wij doen het anders. Je stuurt een WhatsApp-bericht of belt, je hoort direct de prijs en het levermoment, en onze bezorger, die de stadsdelen en de routes kent, komt naar je toe. Doorgaans binnen 20 tot 30 minuten.</p>'
                 '<h2>Waar wij voor staan</h2>' + checks([
                     "<strong>Bereikbaar wanneer jij het nodig hebt.</strong> Dag en nacht, doordeweeks en in het weekend.",
                     "<strong>Duidelijkheid vooraf.</strong> Prijs en levermoment staan vast voordat we vertrekken. Geen kosten achteraf.",
                     "<strong>Gefocust op Amsterdam.</strong> Amsterdam en omstreken zijn onze thuisbasis. We plannen routes op de stad en houden rekening met drukte en afsluitingen.",
                     "<strong>Particulier en zakelijk.</strong> Van een bestelling thuis tot horeca en evenementen.",
                     "<strong>Verantwoord.</strong> Uitsluitend aan volwassenen (18+), alleen in lijn met de geldende wet, en met eerlijke informatie over risico&rsquo;s en veilig gebruik.",
                 ]) +
                 '<h2>Ons bezorggebied</h2>'
                 '<p>Wij bezorgen in alle zeven stadsdelen van Amsterdam plus Weesp, en in overleg in Amstelveen, Diemen, Zaandam, Haarlem, Hoofddorp, Almere en Purmerend. Bekijk het <a href="/bezorggebied/">volledige bezorggebied</a>.</p>'
                 '<h2>Verantwoord beleid</h2>'
                 '<p>Lachgas is geen onschuldig product. Daarom leveren wij uitsluitend aan volwassenen, vragen we bij twijfel om een identiteitsbewijs, behouden we ons het recht voor een bestelling te weigeren en plaatsen we geen instructies voor misbruik op onze website. Op onze <a href="/lachgas-informatie/">informatiepagina&rsquo;s</a> lees je eerlijk over de risico&rsquo;s, de regels en veilig gebruik.</p>'
                 '<h2>Contact</h2>'
                 '<p>WhatsApp of bel %s, of mail naar <a href="mailto:%s">%s</a>. Alle contactmogelijkheden vind je op de <a href="/contact/">contactpagina</a>.</p>' % (phone_link(), EMAIL, EMAIL)),
        cta_block(),
    ]
    page["body"] = "".join(body)
    return page


def contact_page():
    path = "/contact/"
    page = dict(
        path=path,
        title="Contact LachGasAdam247 | WhatsApp of bel %s" % PHONE_DISPLAY,
        description="Contact met LachGasAdam247: bestel lachgas in Amsterdam via WhatsApp of bel %s. 24/7 bereikbaar. E-mail: %s." % (PHONE_DISPLAY, EMAIL),
        h1="Contact: lachgas bestellen in Amsterdam",
        lead="Wij zijn 24 uur per dag, 7 dagen per week bereikbaar. De snelste manier om lachgas te bestellen is via WhatsApp of telefoon. Stuur je adres en het gewenste aantal, dan bevestigen we het levermoment en de prijs.",
        crumbs=[("Home", "/"), ("Contact", None)],
        priority="0.7", changefreq="monthly",
        page_type="ContactPage",
        faq=[
            ("Wat is het telefoonnummer van LachGasAdam247?",
             "Je bereikt ons 24/7 op %s, via telefoon en WhatsApp." % PHONE_DISPLAY),
            ("Wat moet ik in mijn WhatsApp-bericht zetten?",
             "Je volledige leveradres met postcode, huisnummer en eventueel verdieping en bel, het gewenste aantal en de maat, het moment waarop je wilt ontvangen en een nummer waarop je bereikbaar bent. Zakelijk geef je ook je bedrijfsnaam door."),
            ("Kan ik ook mailen?",
             "Ja, voor vragen die geen haast hebben mail je naar %s. Voor bestellingen is WhatsApp of telefoon veel sneller." % EMAIL),
        ],
        speakable=["#h1", ".lead"],
    )
    body = [
        '<section class="hero" id="top" aria-labelledby="h1"><div class="wrap">%s<div class="hero-in"><p class="eyebrow">Contact · 24/7 bereikbaar</p><h1 id="h1">%s</h1><p class="lead">%s</p></div></div></section>'
        % (crumbs_html(page["crumbs"]), esc(page["h1"]), page["lead"]),
        '<section class="section" aria-labelledby="h-kanalen"><div class="wrap"><h2 id="h-kanalen">Zo bereik je ons</h2><div class="cards contact">'
        '<div class="card"><h3>WhatsApp</h3><p>Stuur je adres en het gewenste aantal. Wij bevestigen levermoment en prijs.</p><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">Open WhatsApp</a></div>'
        '<div class="card"><h3>Telefoon</h3><p>Liever praten over levering en details? Bel ons, ook &rsquo;s nachts.</p><a class="btn btn-call" href="tel:%s">Bel %s</a></div>'
        '<div class="card"><h3>E-mail</h3><p>Voor vragen die geen haast hebben.</p><a class="btn btn-call" href="mailto:%s">%s</a></div>'
        '</div></div></section>' % (WA_ORDER, PHONE_TEL, PHONE_DISPLAY, EMAIL, EMAIL),
        '<section class="section alt" aria-labelledby="h-geg"><div class="wrap prose"><h2 id="h-geg">Gegevens</h2>%s'
        '<h3>Wat geef je door bij je bestelling?</h3>%s</div></section>' % (
            facts([
                ("Naam", "LachGasAdam247"),
                ("Telefoon", phone_link()),
                ("WhatsApp", wa_link("Open WhatsApp-gesprek")),
                ("E-mail", '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)),
                ("Bereikbaar", "24 uur per dag, 7 dagen per week, ook op feestdagen"),
                ("Werkgebied", 'Amsterdam en omstreken, zie <a href="/bezorggebied/">bezorggebied</a>'),
                ("Leeftijd", "Uitsluitend voor volwassenen (18+)"),
            ]),
            checks([
                "Je volledige leveradres: straat, huisnummer, postcode en eventueel de verdieping.",
                "De juiste bel of ingang, bijvoorbeeld bij een portiek, gedeelde voordeur of intercom.",
                "Het gewenste aantal en de <a href=\"/lachgas-tanks/\">maat tank</a> die je wilt hebben.",
                "Het moment waarop je de levering wilt ontvangen.",
                "Een nummer waarop je bereikbaar bent zodra onze bezorger in de buurt is.",
                "Voor zakelijke bestellingen: je bedrijfsnaam en een aanspreekpunt.",
            ])),
        faq_html(page["faq"], "Veelgestelde vragen over contact"),
    ]
    page["body"] = "".join(body)
    return page


def privacy_page():
    path = "/privacy/"
    page = dict(
        path=path,
        title="Privacyverklaring | LachGasAdam247",
        description="Lees hoe LachGasAdam247 omgaat met je persoonsgegevens bij bestellingen via WhatsApp, telefoon en e-mail en bij het bezoeken van deze website.",
        h1="Privacyverklaring",
        lead="Deze pagina beschrijft hoe LachGasAdam247 omgaat met persoonsgegevens in lijn met hoe wij onze dienst aanbieden: lachgaslevering in Amsterdam en omstreken, bereikbaar via WhatsApp, telefoon en e-mail, 24/7 zoals op de website vermeld.",
        crumbs=[("Home", "/"), ("Privacy", None)],
        priority="0.3", changefreq="yearly", published="2026-09-20",
    )
    body = doc_page(page,
        '<h2>Verwerkingsverantwoordelijke</h2><p>LachGasAdam247 (hierna: &ldquo;wij&rdquo;). Voor vragen over privacy kun je contact opnemen via WhatsApp of telefoon (%s) of via e-mail: <a href="mailto:%s">%s</a>.</p>' % (PHONE_DISPLAY, EMAIL, EMAIL) +
        '<h2>Welke gegevens verwerken wij?</h2><p>Afhankelijk van hoe je contact met ons opneemt of een bestelling plaatst, kan dat zijn:</p><ul><li>Naam en contactgegevens (telefoonnummer, WhatsApp-nummer, e-mailadres)</li><li>Adres- en levergegevens (bezorgadres in Amsterdam of omstreken)</li><li>Inhoud van berichten die je naar ons stuurt</li><li>Technische gegevens bij bezoek aan de website (zoals IP-adres en browsertype), voor zover standaard server- of hostinglogs dat met zich meebrengen</li></ul>'
        '<h2>Doeleinden</h2><ul><li>Het aannemen en uitvoeren van bestellingen en leveringen</li><li>Contact over je bestelling, planning en bevestiging</li><li>Beantwoorden van vragen en klantenservice</li><li>Handhaving van onze overeenkomst en wettelijke verplichtingen</li></ul>'
        '<h2>Grondslag</h2><p>Verwerking geschiedt op basis van uitvoering van een overeenkomst, gerechtvaardigd belang (bijvoorbeeld bereikbaarheid van de dienst) of, waar van toepassing, toestemming.</p>'
        '<h2>Bewaartermijn</h2><p>Wij bewaren gegevens niet langer dan nodig voor de genoemde doeleinden, tenzij een langere bewaartermijn wettelijk verplicht is (bijvoorbeeld voor de administratie).</p>'
        '<h2>Delen met derden</h2><p>Gegevens worden alleen gedeeld als dat nodig is voor de levering (bijvoorbeeld met een bezorger) of als de wet dat vereist. Bij communicatie via WhatsApp gelden de voorwaarden en het privacybeleid van WhatsApp. Hosting van de website vindt plaats bij een hostingpartij die als verwerker optreedt.</p>'
        '<h2>Cookies en tracking</h2><p>Deze website plaatst zelf geen cookies en gebruikt geen tracking- of advertentiescripts. Je browser of de hostingpartij kan wel technische gegevens verwerken die nodig zijn voor de werking van de website.</p>'
        '<h2>Jouw rechten</h2><p>Onder de AVG heb je rechten op inzage, correctie, verwijdering, beperking, dataportabiliteit en bezwaar waar relevant. Neem contact op via WhatsApp, telefoon of e-mail. Je kunt ook een klacht indienen bij de Autoriteit Persoonsgegevens.</p>'
        '<h2>Wijzigingen</h2><p>Wij kunnen deze verklaring aanpassen. De datum van laatste wijziging is 29 september 2026. Bij grote wijzigingen vermelden we dat op de website.</p><p style="margin-top:2rem"><a href="/">&larr; Terug naar de homepage</a></p>')
    page["body"] = body
    return page


def voorwaarden_page():
    path = "/algemene-voorwaarden/"
    page = dict(
        path=path,
        title="Algemene voorwaarden | LachGasAdam247",
        description="Algemene voorwaarden van LachGasAdam247 voor aanvragen, bestellingen en leveringen van lachgas in Amsterdam en omstreken.",
        h1="Algemene voorwaarden",
        lead="Deze algemene voorwaarden zijn van toepassing op aanvragen, bestellingen en leveringen van lachgas via LachGasAdam247, met levering in Amsterdam en omstreken, zoals op de website beschreven. Door een bestelling te plaatsen ga je akkoord met deze voorwaarden.",
        crumbs=[("Home", "/"), ("Algemene voorwaarden", None)],
        priority="0.3", changefreq="yearly", published="2026-09-20",
    )
    body = doc_page(page,
        '<h2>1. Dienst</h2><p>Wij leveren lachgas aan huis of op een afgesproken locatie, volgens de stappen op de website: contact via WhatsApp of telefoon, bevestiging met levermoment en bedrag, en bezorging met veilige overdracht.</p>'
        '<h2>2. Leeftijd</h2><p>Wij leveren uitsluitend aan personen van 18 jaar en ouder. Bij twijfel over je leeftijd kunnen wij om een geldig identiteitsbewijs vragen.</p>'
        '<h2>3. Werkgebied en beschikbaarheid</h2><p>Levering vindt plaats in het gebied dat wij op de website hanteren (Amsterdam en omstreken). Onze communicatie vermeldt <strong>24/7 bereikbaarheid</strong>; concrete levertijden en planning stemmen wij in overleg met jou af en bevestigen wij per bericht of telefonisch.</p>'
        '<h2>4. Bestelling en totstandkoming overeenkomst</h2><p>Een overeenkomst komt tot stand na bevestiging door ons (bijvoorbeeld via WhatsApp, telefoon of e-mail), inclusief de voor jou relevante voorwaarden zoals prijs, hoeveelheid, leveradres en moment. Wij behouden ons het recht voor een bestelling te weigeren.</p>'
        '<h2>5. Prijzen en betaling</h2><p>Wij hanteren de prijs zoals bij de bestelling bevestigd. Eventuele kosten worden vooraf duidelijk gecommuniceerd. Betalingsafspraken (moment en wijze) volgen uit de bevestiging, tenzij anders overeengekomen.</p>'
        '<h2>6. Levering en veiligheid</h2><p>Levering geschiedt volgens de gemaakte afspraken. Jij zorgt voor een bereikbaar leveradres en medewerking voor een veilige overdracht. Wij verwachten dat je producten verantwoordelijk gebruikt en de geldende wet- en regelgeving respecteert.</p>'
        '<h2>7. Annulering en wijziging</h2><p>Annulering of wijziging van een bestelling is mogelijk volgens de afspraken in de bevestiging. Redelijke kosten kunnen in rekening worden gebracht als de levering al is voorbereid of onderweg is.</p>'
        '<h2>8. Klachten</h2><p>Klachten kun je melden via <a href="mailto:%s">%s</a> of telefonisch en via WhatsApp op %s. Wij streven naar een snelle en nette oplossing.</p>' % (EMAIL, EMAIL, PHONE_DISPLAY) +
        '<h2>9. Aansprakelijkheid</h2><p>Onze aansprakelijkheid is beperkt tot hetgeen wettelijk verplicht is en tot directe schade, met uitzondering van opzet of grove schuld. Wij zijn niet aansprakelijk voor gevolgschade, tenzij dwingend recht anders bepaalt.</p>'
        '<h2>10. Toepasselijk recht</h2><p>Op deze voorwaarden is Nederlands recht van toepassing. Geschillen worden voorgelegd aan de bevoegde rechter in Nederland.</p><p style="margin-top:2rem"><a href="/">&larr; Terug naar de homepage</a></p>')
    page["body"] = body
    return page


def notfound_page():
    page = dict(
        path="/404.html",
        title="Pagina niet gevonden | LachGasAdam247",
        description="Deze pagina bestaat niet. Ga terug naar de homepage van LachGasAdam247 voor lachgas bestellen in Amsterdam.",
        h1="Pagina niet gevonden",
        lead="Deze pagina bestaat niet (meer). Ga terug naar de homepage, kies een bezorggebied of bestel direct via WhatsApp.",
        crumbs=[("Home", "/"), ("Pagina niet gevonden", None)],
        robots="noindex, follow",
        sitemap=False,
    )
    body = ('<article class="wrap prose doc"><h1>%s</h1><p class="lead">%s</p>'
            '<p><a class="btn btn-wa" href="%s" target="_blank" rel="noopener">WhatsApp</a> <a class="btn btn-call" href="/">Naar de homepage</a></p>'
            '<h2>Populaire pagina&rsquo;s</h2>%s</article>'
            % (esc(page["h1"]), page["lead"], WA_DEFAULT, toc([
                ("/bezorggebied/", "Bezorggebied"), ("/lachgas-tanks/", "Lachgas tanks"), ("/zakelijk/", "Zakelijk en evenementen"),
                ("/lachgas-24-7-amsterdam/", "Lachgas 24/7"), ("/lachgas-informatie/", "Lachgas informatie"), ("/contact/", "Contact")])))
    page["body"] = body
    return page


def pages():
    return [zakelijk_page(), nacht_page(), over_ons_page(), contact_page(), privacy_page(), voorwaarden_page(), notfound_page()]
