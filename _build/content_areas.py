# -*- coding: utf-8 -*-
"""Bezorggebied-pagina's: stadsdelen van Amsterdam en de regio."""
from common import (SITE, BUSINESS_ID, STADSDELEN, REGIO, PHONE_DISPLAY, PHONE_TEL, WA_ORDER, esc, hero,
                  checks, steps, faq_html, cta_block, link_cards, phone_link, wa_link, toc, wa)

AREAS = {}

# ---------------------------------------------------------------------------
# Stadsdelen
# ---------------------------------------------------------------------------
AREAS["amsterdam-centrum"] = dict(
    name="Amsterdam Centrum", kind="stadsdeel",
    title="Lachgas Amsterdam Centrum bestellen | 24/7 bezorgd",
    description="Lachgas bestellen in Amsterdam Centrum? 24/7 bezorgd in Grachtengordel, Jordaan, De Wallen en Plantage in 20-30 min. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amsterdam Centrum",
    lead="Lachgas nodig in het centrum van Amsterdam? LachGasAdam247 bezorgt lachgas tanks 24/7 in de Grachtengordel, de Jordaan, De Wallen, de Nieuwmarkt, het Waterlooplein, de Plantage en de Oostelijke Eilanden. Stuur je adres via WhatsApp en wij zijn er doorgaans binnen 20 tot 30 minuten.",
    wijken=["Grachtengordel", "Jordaan", "Negen Straatjes", "Nieuwmarkt", "De Wallen", "Waterlooplein", "Plantage",
            "Oostelijke Eilanden", "Kadijken", "Haarlemmerbuurt", "Westelijke Eilanden", "Weesperbuurt"],
    intro=[
        "Het centrum van Amsterdam is het drukste en meest compacte deel van de stad. Grachtenpanden zonder parkeerplek, smalle straten, bruggen en autoluwe zones maken bezorgen hier anders dan in de buitenwijken. Onze bezorgers kennen de routes door de binnenstad en weten waar je wel en niet kunt stoppen. Daardoor bezorgen wij lachgas in Amsterdam Centrum doorgaans binnen 20 tot 30 minuten, ook &rsquo;s nachts en in het weekend.",
        "Of je nu in een bovenwoning aan de Prinsengracht woont, in een appartement in de Jordaan of tijdelijk in een hotel bij het Rembrandtplein verblijft: het bestelproces is hetzelfde. Je stuurt een WhatsApp-bericht met je adres en het gewenste aantal, wij bevestigen het levermoment en de prijs, en we komen naar je toe.",
    ],
    letten=[
        "<strong>Geef de juiste bel en verdieping door.</strong> In grachtenpanden zitten vaak meerdere woningen achter één voordeur. Een verdieping en de naam op de bel schelen minuten.",
        "<strong>Autoluwe zones en afgesloten straten.</strong> Rond de Wallen, de Nieuwmarkt en delen van de Grachtengordel kunnen we niet altijd tot aan de deur rijden. We spreken dan een goed bereikbaar punt af, bijvoorbeeld bij een brug of op de hoek van een gracht.",
        "<strong>Hotels en kantoren.</strong> Rond Amsterdam Centraal, het Rembrandtplein, het Leidseplein en de Dam leveren we regelmatig bij hotels en kantoren. Geef een aanspreekpunt en een geschikt moment door.",
        "<strong>Drukke momenten.</strong> Op Koningsdag, tijdens Pride, het Amsterdam Dance Event en Oud en Nieuw zijn straten en bruggen in het centrum afgesloten. Bestel dan iets eerder.",
    ],
    extra_h="Uitgaan in het centrum: Leidseplein, Rembrandtplein en De Wallen",
    extra="Het centrum is het uitgaanshart van Amsterdam. Rond het Leidseplein, het Rembrandtplein, de Reguliersdwarsstraat, de Nieuwmarkt en De Wallen is het tot diep in de nacht druk. Bestel je lachgas &rsquo;s nachts in het centrum, dan helpt het als je een exact adres opgeeft en niet alleen een plein of straatnaam. Wij bezorgen bij woningen, appartementen, hotels en kantoren, niet op straat of in de horeca zelf zonder afspraak met de eigenaar. Voor feesten en zakelijke leveringen, bijvoorbeeld aan een bar of een evenementenlocatie, kijk je op onze pagina over <a href=\"/zakelijk/\">lachgas voor horeca en evenementen</a>.",
    faq=[
        ("Hoe snel bezorgen jullie lachgas in Amsterdam Centrum?",
         "Doorgaans binnen 20 tot 30 minuten. In het centrum zijn we vaak snel, maar afgesloten straten, evenementen en drukte op de grachten kunnen de rit iets langer maken. We bevestigen de verwachte aankomsttijd altijd vooraf."),
        ("Bezorgen jullie ook in autoluwe straten en op de Wallen?",
         "Ja. Kunnen we niet tot aan de deur rijden, dan spreken we een goed bereikbaar punt in de buurt af, bijvoorbeeld bij een brug of op de hoek van de straat. Geef bij je bestelling je exacte adres door, dan stellen wij een geschikte plek voor."),
        ("Kan ik lachgas laten bezorgen bij mijn hotel in het centrum?",
         "Ja, bij hotels rond Amsterdam Centraal, de Dam, het Leidseplein en het Rembrandtplein bezorgen we regelmatig. Geef de naam van het hotel, je kamernummer of een aanspreekpunt en een geschikt moment door."),
    ],
    nearby=["amsterdam-west", "amsterdam-zuid", "amsterdam-oost", "amsterdam-noord"],
    geo=(52.3731, 4.8926),
)

AREAS["amsterdam-noord"] = dict(
    name="Amsterdam Noord", kind="stadsdeel",
    title="Lachgas Amsterdam Noord bestellen | 24/7 bezorgd",
    description="Lachgas bestellen in Amsterdam Noord? 24/7 bezorgd in Overhoeks, NDSM, Buikslotermeer, Nieuwendam en heel Noord. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amsterdam Noord",
    lead="Woon je aan de overkant van het IJ? LachGasAdam247 bezorgt lachgas tanks in heel Amsterdam Noord: van Overhoeks en de NDSM-werf tot Nieuwendam, Buikslotermeer, Banne Buiksloot en Kadoelen. 24/7 bereikbaar via WhatsApp en telefoon, met een aankomsttijd die we vooraf bevestigen.",
    wijken=["Overhoeks", "Buiksloterham", "NDSM-werf", "Van der Pekbuurt", "Vogelbuurt", "Volewijck", "Tuindorp Oostzaan",
            "Nieuwendam", "Molenwijk", "Buikslotermeer", "Banne Buiksloot", "Kadoelen", "Elzenhagen", "Schellingwoude", "Nieuwendammerdijk"],
    intro=[
        "Amsterdam Noord ligt aan de overkant van het IJ en is met de rest van de stad verbonden via de IJtunnel, de pont en de Noord/Zuidlijn. Voor onze bezorgers betekent dat: een vaste route via de tunnel of de ring A10, en goede kennis van de wijken tussen het water en de Waterlandse dorpen. Wij bezorgen lachgas in heel Amsterdam Noord, van de nieuwe appartementen in Overhoeks en Buiksloterham tot de tuindorpen in Nieuwendam en de flats in Molenwijk en Banne Buiksloot.",
        "Noord is groot en gevarieerd. Dichtbebouwde buurten vlak bij het IJ, zoals de Van der Pekbuurt en de Vogelbuurt, wisselen af met ruimere wijken verder naar het noorden. Geef daarom altijd een volledig adres met postcode door, zodat wij de verwachte aankomsttijd goed kunnen inschatten en je precies weet wanneer we er zijn.",
    ],
    letten=[
        "<strong>Route via de IJtunnel of de ring.</strong> Omdat Noord aan de andere kant van het water ligt, bevestigen we de aankomsttijd altijd vooraf. Bij drukte in de IJtunnel kiezen we de route via de A10.",
        "<strong>Nieuwbouw en appartementencomplexen.</strong> In Overhoeks, Buiksloterham en Elzenhagen staan veel nieuwe complexen met meerdere ingangen. Geef het bouwnummer, de ingang en de verdieping door.",
        "<strong>Tuindorpen en dijkwoningen.</strong> In Tuindorp Oostzaan, Nieuwendam en langs de Nieuwendammerdijk zijn straten soms smal of eenrichting. Een herkenningspunt helpt.",
        "<strong>NDSM en evenementen.</strong> Rond de NDSM-werf en de Noorderparkbar is het bij festivals en in het weekend druk. Bestel iets eerder en geef een exact adres door.",
    ],
    extra_h="NDSM, Overhoeks en de Noordse hotspots",
    extra="Noord is de afgelopen jaren uitgegroeid tot een van de populairste delen van Amsterdam om te wonen en uit te gaan. Rond de NDSM-werf, de Tolhuistuin, het EYE Filmmuseum, A&rsquo;DAM Toren en de Pllek-oever wordt tot laat gefeest. Ook in de nieuwe woonwijken rond het Buikslotermeerplein en station Noord wonen steeds meer jonge huishoudens. Wij bezorgen bij woningen, appartementen, hotels en kantoren in heel Noord, ook &rsquo;s nachts. Woon je net buiten de stad, bijvoorbeeld in Landsmeer, Zunderdorp of Durgerdam? Stuur je postcode, dan bevestigen we of we bij jou kunnen bezorgen.",
    faq=[
        ("Duurt bezorgen in Amsterdam Noord langer dan in het centrum?",
         "Soms iets langer, omdat we het IJ moeten oversteken via de IJtunnel of de ring. In de praktijk bezorgen we in Noord doorgaans binnen 20 tot 40 minuten. We laten je altijd vooraf weten wanneer je ons kunt verwachten."),
        ("Bezorgen jullie ook in Landsmeer, Zunderdorp en Durgerdam?",
         "De dorpen rond Noord liggen aan de rand van ons werkgebied. Stuur je postcode via WhatsApp, dan laten we direct weten of we kunnen komen en wat de verwachte aankomsttijd is."),
        ("Kan ik lachgas bestellen bij een feest op de NDSM-werf?",
         "Ja, als je een adres of locatie hebt waar we kunnen afleveren, bijvoorbeeld een woning, een boot met vaste ligplaats of een gehuurde ruimte. Bij evenementen en zakelijke leveringen plannen we het moment vooraf. Kijk ook op onze pagina voor <a href=\"/zakelijk/\">feesten, horeca en evenementen</a>."),
    ],
    nearby=["amsterdam-centrum", "zaandam", "purmerend", "amsterdam-oost"],
    geo=(52.3990, 4.9160),
)

AREAS["amsterdam-zuid"] = dict(
    name="Amsterdam Zuid", kind="stadsdeel",
    title="Lachgas Amsterdam Zuid bestellen | De Pijp, Zuidas | 24/7",
    description="Lachgas bestellen in Amsterdam Zuid? 24/7 bezorgd in De Pijp, Rivierenbuurt, Oud-Zuid, Zuidas en Buitenveldert in 20-30 min. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amsterdam Zuid",
    lead="Lachgas bestellen in De Pijp, de Rivierenbuurt, Oud-Zuid, het Museumkwartier, de Zuidas of Buitenveldert? LachGasAdam247 bezorgt lachgas tanks in heel Amsterdam Zuid, 24 uur per dag, doorgaans binnen 20 tot 30 minuten. Stuur je adres via WhatsApp en ontvang direct een bevestiging.",
    wijken=["De Pijp", "Rivierenbuurt", "Oud-Zuid", "Museumkwartier", "Apollobuurt", "Stadionbuurt", "Willemspark",
            "Prinses Irenebuurt", "Zuidas", "Buitenveldert", "Schinkelbuurt", "Hoofddorppleinbuurt", "Diamantbuurt"],
    intro=[
        "Amsterdam Zuid combineert de levendige straten van De Pijp en de Rivierenbuurt met het rustige Oud-Zuid rond het Vondelpark, het Museumkwartier en de Apollobuurt. Aan de zuidkant liggen de Zuidas, de RAI en Buitenveldert, met veel kantoren, hotels en congreslocaties. Wij bezorgen lachgas in al deze buurten, van een studentenwoning aan de Ceintuurbaan tot een appartement aan de Beethovenstraat of een hotel bij station Zuid.",
        "Zuid ligt dicht bij het centrum en is goed bereikbaar via de A10 en de Amstelveenseweg. Daardoor zijn onze bezorgers hier meestal snel ter plekke. In De Pijp en de Rivierenbuurt staan veel panden met een gedeelde voordeur en zonder parkeerplek; geef daarom bij je bestelling het huisnummer, de verdieping en de juiste bel door.",
    ],
    letten=[
        "<strong>De Pijp en de Rivierenbuurt.</strong> Smalle straten, weinig parkeerplek en veel gedeelde voordeuren. Laat weten of we bij de voordeur, een achteringang of op een afgesproken punt kunnen afleveren.",
        "<strong>Zuidas, RAI en station Zuid.</strong> Rond kantoren en hotels leveren we op afspraak bij een receptie of een aanspreekpunt. Bij beurzen en evenementen in de RAI is het drukker op de weg.",
        "<strong>Oud-Zuid en het Museumkwartier.</strong> Rustige woonstraten met vaak een duidelijke bel. Geef bij een souterrain of bovenwoning de juiste ingang door.",
        "<strong>Buitenveldert.</strong> Ruim opgezet, met flats en portieken. Vermeld het portiek en de verdieping.",
    ],
    extra_h="De Pijp, het Vondelpark en de Zuidas",
    extra="De Pijp is met de Albert Cuypmarkt, het Sarphatipark en de vele bars en restaurants een van de populairste uitgaansbuurten van Amsterdam. Rond het Marie Heinekenplein en de Gerard Douplein is het in het weekend tot laat druk. Oud-Zuid rond het Vondelpark en de Van Baerlestraat is rustiger en chiquer, terwijl de Zuidas overdag een zakelijk hart is met veel kantoren en hotels. Wij bezorgen in al deze delen van Zuid en houden bij het plannen rekening met drukte rond de Albert Cuyp, de RAI en de Amstelveenseweg. Grenst jouw adres aan Amstelveen? Kijk dan ook op de pagina <a href=\"/bezorggebied/amstelveen/\">lachgas Amstelveen</a>.",
    faq=[
        ("Bezorgen jullie lachgas in De Pijp ook &rsquo;s nachts?",
         "Ja. Wij zijn 24/7 bereikbaar en bezorgen in De Pijp, de Rivierenbuurt en de rest van Zuid ook &rsquo;s avonds laat en &rsquo;s nachts. Geef je adres, de verdieping en de juiste bel door, dan verloopt de overdracht snel."),
        ("Kunnen jullie leveren bij een kantoor of hotel op de Zuidas?",
         "Ja. Geef de naam van het gebouw of hotel, een aanspreekpunt en een geschikt moment door. Bij zakelijke leveringen stemmen we de plek van overdracht vooraf af, bijvoorbeeld bij de receptie of een laad- en losplek."),
        ("Hoe snel zijn jullie in Buitenveldert en bij de RAI?",
         "Doorgaans binnen 20 tot 30 minuten. Bij grote beurzen of evenementen in de RAI en bij drukte op de A10 kan het iets langer duren; we bevestigen de verwachte aankomsttijd altijd voordat we vertrekken."),
    ],
    nearby=["amsterdam-centrum", "amstelveen", "amsterdam-west", "amsterdam-oost"],
    geo=(52.3450, 4.8800),
)

AREAS["amsterdam-oost"] = dict(
    name="Amsterdam Oost", kind="stadsdeel",
    title="Lachgas Amsterdam Oost bestellen | IJburg, Oud-Oost | 24/7",
    description="Lachgas bestellen in Amsterdam Oost? 24/7 bezorgd in Oud-Oost, Indische Buurt, Watergraafsmeer en IJburg. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amsterdam Oost",
    lead="Van de Dapperbuurt en de Indische Buurt tot de Watergraafsmeer, Science Park, IJburg en het Oostelijk Havengebied: LachGasAdam247 bezorgt lachgas tanks in heel Amsterdam Oost. 24/7 bereikbaar via WhatsApp en telefoon, doorgaans bezorgd binnen 20 tot 30 minuten.",
    wijken=["Oud-Oost", "Oosterparkbuurt", "Dapperbuurt", "Indische Buurt", "Transvaalbuurt", "Weesperzijde", "Watergraafsmeer",
            "Science Park", "Betondorp", "Middenmeer", "IJburg", "Zeeburgereiland", "Oostelijk Havengebied", "Sporenburg", "KNSM-eiland", "Java-eiland"],
    intro=[
        "Amsterdam Oost is een gevarieerd stadsdeel. Dichtbebouwde buurten als de Dapperbuurt, de Indische Buurt en de Transvaalbuurt liggen rond het Oosterpark en het Flevopark. De Watergraafsmeer heeft veel laagbouw en rustige straten, terwijl IJburg, Zeeburgereiland en het Oostelijk Havengebied uit nieuwere appartementen aan het water bestaan. Wij bezorgen lachgas in al deze delen van Oost, dag en nacht.",
        "Rond Science Park, de Weesperzijde en de Watergraafsmeer wonen veel studenten en jonge huishoudens, vaak in complexen met een gedeelde ingang of in huizen met meerdere bellen. Vermeld bij je bestelling welke bel of ingang wij moeten gebruiken en houd je telefoon bij de hand zodra we in de buurt zijn. Zo verloopt de overdracht snel, ook in gebouwen zonder duidelijke naambordjes.",
    ],
    letten=[
        "<strong>IJburg en Zeeburgereiland.</strong> Bereikbaar via de IJburglaan en de Piet Heintunnel. Geef het eiland (Haveneiland, Steigereiland, Rieteiland, Centrumeiland) en het huisnummer door.",
        "<strong>Oostelijk Havengebied.</strong> Op het KNSM-eiland, Java-eiland, Sporenburg en Borneo-eiland staan grote wooncomplexen met meerdere ingangen. Vermeld de ingang en de verdieping.",
        "<strong>Indische Buurt en Dapperbuurt.</strong> Drukke woonstraten rond de Javastraat en de Dappermarkt. Een herkenningspunt en de juiste bel helpen.",
        "<strong>Watergraafsmeer en Science Park.</strong> Ruim opgezet en goed bereikbaar via de Middenweg en de ring. Bij studentencomplexen graag het gebouw en de ingang doorgeven.",
    ],
    extra_h="Javastraat, Oosterpark en IJburg",
    extra="Oost is de laatste jaren enorm populair geworden. De Javastraat, de Eerste van Swindenstraat en de Dappermarkt vormen het kloppende hart van de Indische Buurt en de Dapperbuurt, met veel bars en restaurants. Rond het Oosterpark, de Weesperzijde en de Amstel wordt in de zomer volop buiten geleefd. IJburg heeft met het Blijburg-strand en de haven een eigen sfeer aan het water. Wij bezorgen bij woningen en appartementen in heel Oost, ook &rsquo;s nachts en in het weekend. Woon je net over de grens in Diemen? Kijk dan op de pagina <a href=\"/bezorggebied/diemen/\">lachgas Diemen</a>.",
    faq=[
        ("Bezorgen jullie lachgas op IJburg?",
         "Ja. Wij bezorgen op alle eilanden van IJburg en op Zeeburgereiland. Omdat IJburg aan de rand van de stad ligt, bevestigen we de aankomsttijd vooraf. Doorgaans zijn we er binnen 25 tot 35 minuten."),
        ("Kan ik lachgas laten bezorgen bij een studentencomplex bij Science Park?",
         "Ja. Geef het gebouw, de ingang en je kamernummer of verdieping door en zorg dat je bereikbaar bent op je telefoon zodra onze bezorger in de buurt is."),
        ("Leveren jullie ook in de Indische Buurt en de Dapperbuurt &rsquo;s nachts?",
         "Ja, wij zijn 24/7 bereikbaar en bezorgen in de Indische Buurt, de Dapperbuurt en de rest van Oost ook &rsquo;s avonds laat en &rsquo;s nachts. Vermeld je adres volledig, inclusief de juiste bel."),
    ],
    nearby=["amsterdam-centrum", "diemen", "amsterdam-zuidoost", "amsterdam-noord"],
    geo=(52.3550, 4.9400),
)

AREAS["amsterdam-west"] = dict(
    name="Amsterdam West", kind="stadsdeel",
    title="Lachgas Amsterdam West bestellen | Oud-West, Baarsjes | 24/7",
    description="Lachgas bestellen in Amsterdam West? 24/7 bezorgd in Oud-West, De Baarsjes, Bos en Lommer en Westerpark in 20-30 min. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amsterdam West",
    lead="Lachgas bestellen in Oud-West, De Baarsjes, Bos en Lommer of de Westerparkbuurt? LachGasAdam247 bezorgt lachgas tanks in heel Amsterdam West, 24 uur per dag en 7 dagen per week. Stuur je adres via WhatsApp en wij zijn er doorgaans binnen 20 tot 30 minuten.",
    wijken=["Oud-West", "Kinkerbuurt", "Helmersbuurt", "Da Costabuurt", "Vondelbuurt", "De Baarsjes", "Chassébuurt",
            "Mercatorbuurt", "Bos en Lommer", "Kolenkitbuurt", "Landlust", "Westerpark", "Staatsliedenbuurt", "Spaarndammerbuurt", "Zeeheldenbuurt", "Frederik Hendrikbuurt"],
    intro=[
        "Amsterdam West bestaat uit levendige woonbuurten die direct aan het centrum grenzen. Oud-West rond de Kinkerstraat, De Hallen en de Overtoom, De Baarsjes rond de Jan Evertsenstraat en het Mercatorplein, Bos en Lommer langs de ring en de Westerparkbuurt met de Westergasfabriek en de Staatsliedenbuurt. Wij bezorgen lachgas in al deze buurten, dag en nacht.",
        "Omdat West langs de A10 ligt en via de Jan van Galenstraat, de Admiraal de Ruijterweg en de Haarlemmerweg goed verbonden is met het centrum en de ring, zijn onze bezorgers hier meestal vlot ter plekke. In de oudere panden in Oud-West en De Baarsjes zijn trappen steil en gangen smal. Laat het weten als je op een hogere verdieping woont of als je adres lastig te vinden is, dan nemen we dat mee in de planning.",
    ],
    letten=[
        "<strong>Oud-West en de Kinkerbuurt.</strong> Drukke straten rond de Kinkerstraat, De Hallen en de Ten Katemarkt. Geef de juiste bel en verdieping door.",
        "<strong>De Baarsjes en Bos en Lommer.</strong> Veel portiekwoningen en gerenoveerde complexen. Vermeld het portiek en of de voordeur op de begane grond of via een galerij bereikbaar is.",
        "<strong>Westerpark en Spaarndammerbuurt.</strong> Rond het Westerpark en de Westergasfabriek is het bij festivals en in het weekend druk. Bestel dan iets eerder.",
        "<strong>Nieuwbouw in Houthavens en Landlust.</strong> Nieuwe complexen met meerdere ingangen; geef het gebouw en de ingang door.",
    ],
    extra_h="De Hallen, Westergasfabriek en de Foodhallen",
    extra="West is populair bij jonge Amsterdammers. De Foodhallen en De Hallen in Oud-West, de bars rond de Bilderdijkstraat en de Overtoom, het Westerpark met de Westergasfabriek en de Houthavens aan het IJ zijn drukbezochte plekken. Ook de Spaarndammerbuurt en de Zeeheldenbuurt zijn de afgelopen jaren flink veranderd, met nieuwe horeca en woningen. Wij bezorgen lachgas bij woningen en appartementen in heel West, ook &rsquo;s nachts en in het weekend. Woon je verder naar het westen, in Osdorp, Slotervaart of Geuzenveld? Kijk dan op de pagina <a href=\"/bezorggebied/amsterdam-nieuw-west/\">lachgas Amsterdam Nieuw-West</a>.",
    faq=[
        ("Hoe snel bezorgen jullie in Oud-West en De Baarsjes?",
         "Doorgaans binnen 20 tot 30 minuten. West ligt dicht bij het centrum en is goed bereikbaar via de ring, waardoor onze bezorgers hier meestal snel zijn. We bevestigen de aankomsttijd vooraf."),
        ("Bezorgen jullie ook in de Houthavens en de Spaarndammerbuurt?",
         "Ja. De Houthavens, de Spaarndammerbuurt en de Zeeheldenbuurt horen bij ons bezorggebied in West. Geef bij nieuwbouwcomplexen het gebouw en de ingang door."),
        ("Ik woon op driehoog zonder lift, is dat een probleem?",
         "Nee. Laat het bij je bestelling weten, dan houden we er rekening mee. Zorg dat je bereikbaar bent zodra onze bezorger in de straat is, dan kunnen we de overdracht bij de voordeur of op je verdieping afspreken."),
    ],
    nearby=["amsterdam-centrum", "amsterdam-nieuw-west", "amsterdam-zuid", "haarlem"],
    geo=(52.3720, 4.8600),
)

AREAS["amsterdam-nieuw-west"] = dict(
    name="Amsterdam Nieuw-West", kind="stadsdeel",
    title="Lachgas Amsterdam Nieuw-West bestellen | Osdorp | 24/7",
    description="Lachgas bestellen in Nieuw-West? 24/7 bezorgd in Osdorp, Slotervaart, Slotermeer, Geuzenveld, De Aker en Nieuw Sloten. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amsterdam Nieuw-West",
    lead="Lachgas bestellen in Osdorp, Slotervaart, Slotermeer, Geuzenveld, De Aker, Nieuw Sloten of Overtoomse Veld? LachGasAdam247 bezorgt lachgas tanks in heel Amsterdam Nieuw-West, 24/7 en doorgaans binnen 20 tot 30 minuten. Bestellen doe je via WhatsApp of telefoon.",
    wijken=["Osdorp", "De Aker", "Geuzenveld", "Slotermeer", "Slotervaart", "Nieuw Sloten", "Overtoomse Veld", "Sloten",
            "Westlandgracht", "Delflandpleinbuurt", "Lelylaan", "Eendracht", "Sloterdijk"],
    intro=[
        "Nieuw-West bestaat grotendeels uit de Westelijke Tuinsteden: ruim opgezette wijken met veel groen, brede lanen, de Sloterplas en flatgebouwen met meerdere portieken. Onder Nieuw-West vallen Osdorp, Geuzenveld, Slotermeer, Slotervaart, De Aker, Nieuw Sloten en Overtoomse Veld, plus het dorp Sloten en het gebied rond Sloterdijk. Wij bezorgen lachgas in al deze wijken, dag en nacht.",
        "Dankzij de aansluitingen op de A10, de A5 en de Cornelis Lelylaan kunnen we routes in dit stadsdeel meestal goed plannen. Bij een bestelling in Osdorp, Geuzenveld of Slotermeer helpt het als je doorgeeft bij welk portiek of welke ingang wij moeten zijn en op welke verdieping je woont. Dat voorkomt onnodig zoeken tussen gebouwen die op elkaar lijken.",
    ],
    letten=[
        "<strong>Portiekflats en galerijflats.</strong> In Slotermeer, Geuzenveld en Osdorp staan veel flats met meerdere portieken. Vermeld het portiek, de galerij en de verdieping.",
        "<strong>Nieuwbouw en renovatie.</strong> Rond het Osdorpplein, de Lelylaan en het Delflandplein zijn veel nieuwe complexen gebouwd. Geef het gebouw en de ingang door.",
        "<strong>De Aker en Nieuw Sloten.</strong> Ruime woonwijken met eengezinswoningen; hier is bezorgen doorgaans eenvoudig. Een huisnummer en postcode zijn genoeg.",
        "<strong>Sloterdijk en de Westpoort.</strong> Kantoren en hotels rond station Sloterdijk bedienen we op afspraak met een aanspreekpunt.",
    ],
    extra_h="Sloterplas, Osdorpplein en station Lelylaan",
    extra="Nieuw-West is een stadsdeel in beweging. Rond het Osdorpplein, de Sloterplas en het Plein &rsquo;40-&rsquo;45 is de afgelopen jaren veel vernieuwd, en langs de Lelylaan en bij station Sloterdijk verrijzen nieuwe woontorens. Ook studenten en jonge huishoudens vinden hier steeds vaker een woning. Wij bezorgen lachgas bij woningen, appartementen, hotels en kantoren in heel Nieuw-West, ook &rsquo;s nachts en in het weekend. Woon je net buiten de stad in Badhoevedorp, Hoofddorp of Halfweg? Kijk dan op de pagina <a href=\"/bezorggebied/hoofddorp/\">lachgas Hoofddorp en Haarlemmermeer</a>.",
    faq=[
        ("Bezorgen jullie ook in Osdorp en De Aker, aan de rand van de stad?",
         "Ja. Osdorp, De Aker en Nieuw Sloten horen volledig bij ons bezorggebied. Omdat deze wijken aan de westrand van Amsterdam liggen, kan de rit iets langer duren dan in het centrum; we bevestigen de aankomsttijd vooraf."),
        ("Wat moet ik doorgeven bij een flat in Slotermeer of Geuzenveld?",
         "Het adres met huisnummer, het portiek of de ingang, de verdieping en de naam op de bel. Houd je telefoon bij de hand zodra we in de buurt zijn, dan vinden we elkaar snel."),
        ("Kunnen jullie leveren bij een hotel bij station Sloterdijk?",
         "Ja. Geef de naam van het hotel, een aanspreekpunt of kamernummer en een geschikt moment door. Rond Sloterdijk leveren we regelmatig bij hotels en kantoren."),
    ],
    nearby=["amsterdam-west", "hoofddorp", "haarlem", "amsterdam-zuid"],
    geo=(52.3600, 4.8100),
)

AREAS["amsterdam-zuidoost"] = dict(
    name="Amsterdam Zuidoost", kind="stadsdeel",
    title="Lachgas Amsterdam Zuidoost bestellen | Bijlmer | 24/7",
    description="Lachgas bestellen in Zuidoost of de Bijlmer? 24/7 bezorgd in Bijlmer, Gaasperdam, Holendrecht, Reigersbos en rond de ArenA. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amsterdam Zuidoost",
    lead="Lachgas bestellen in de Bijlmer, Gaasperdam, Holendrecht, Reigersbos of rond de Johan Cruijff ArenA? LachGasAdam247 bezorgt lachgas tanks in heel Amsterdam Zuidoost, 24 uur per dag. Stuur je adres via WhatsApp en wij bevestigen direct het levermoment en de prijs.",
    wijken=["Bijlmer-Centrum", "Bijlmer-Oost", "Amsterdamse Poort", "Venserpolder", "Ganzenhoef", "Kraaiennest",
            "Gaasperdam", "Holendrecht", "Reigersbos", "Nellestein", "Gein", "Driemond", "ArenAPoort", "Bullewijk"],
    intro=[
        "Zuidoost heeft een heel eigen opzet: de Bijlmer met hoge flatgebouwen, veel groen en parkeergarages, en woonwijken als Gaasperdam, Holendrecht, Reigersbos, Gein en Driemond met meer laagbouw. Rond de Amsterdamse Poort, de ArenAPoort en Bullewijk liggen winkels, kantoren, hotels en de grote evenementenlocaties van Amsterdam. Wij bezorgen lachgas in heel Zuidoost, dag en nacht.",
        "In grote flats is het belangrijk dat wij precies weten bij welk gebouw, welk portiek en welke verdieping je woont, zodat de overdracht snel verloopt. Geef ook door of we bij de hoofdingang, een zijingang of bij de parkeergarage moeten zijn. Zuidoost is via de A2, de A9 en de Gooiseweg goed bereikbaar, waardoor we hier doorgaans binnen 20 tot 35 minuten zijn.",
    ],
    letten=[
        "<strong>Flats in de Bijlmer.</strong> Vermeld de naam van de flat, het portiek of de ingang en de verdieping. Bij gebouwen met meerdere ingangen spreken we een duidelijke plek af.",
        "<strong>Evenementen rond de ArenA.</strong> Bij wedstrijden van Ajax, concerten in de Ziggo Dome of de AFAS Live is het rond de ArenAPoort en de Amsterdamse Poort druk en zijn wegen soms afgesloten. Bestel dan eerder.",
        "<strong>Gaasperdam, Reigersbos en Gein.</strong> Rustige woonwijken met eengezinswoningen en portiekflats. Een huisnummer, postcode en eventueel het portiek zijn voldoende.",
        "<strong>Hotels en kantoren.</strong> Rond station Bijlmer ArenA en Bullewijk leveren we bij hotels en kantoren op afspraak met een aanspreekpunt.",
    ],
    extra_h="ArenA, Ziggo Dome en de Amsterdamse Poort",
    extra="Zuidoost is het evenementenhart van Amsterdam. De Johan Cruijff ArenA, de Ziggo Dome en de AFAS Live trekken vrijwel elk weekend tienduizenden bezoekers, en rond de Amsterdamse Poort en het Anton de Komplein is het overdag en &rsquo;s avonds druk. Ook het Amsterdam UMC (locatie AMC) en de kantoren bij Bullewijk zorgen voor veel verkeer. Wij houden bij het plannen van de rit rekening met evenementen en afsluitingen, en bevestigen de aankomsttijd altijd vooraf. Plan je een bestelling rond een concert of wedstrijd? Geef dat door, dan houden we er rekening mee. Woon je in Diemen of Duivendrecht? Kijk dan op de pagina <a href=\"/bezorggebied/diemen/\">lachgas Diemen</a>.",
    faq=[
        ("Bezorgen jullie lachgas in de Bijlmer &rsquo;s nachts?",
         "Ja. Wij zijn 24/7 bereikbaar en bezorgen in Bijlmer-Centrum, Bijlmer-Oost, Gaasperdam en de rest van Zuidoost ook &rsquo;s avonds laat en &rsquo;s nachts. Geef bij een flat altijd het gebouw, het portiek en de verdieping door."),
        ("Kan ik bestellen als er een concert of wedstrijd is bij de ArenA?",
         "Ja, wij zijn dan gewoon bereikbaar. Rond de ArenA, de Ziggo Dome en de AFAS Live kan het verkeer vastlopen en zijn straten soms afgesloten, dus bestel iets eerder en geef je adres volledig door. Op straat of bij de evenementenlocatie zelf leveren we niet."),
        ("Leveren jullie ook in Driemond, Gein en Reigersbos?",
         "Ja. Driemond, Gein, Reigersbos, Holendrecht en Nellestein horen bij ons bezorggebied in Zuidoost. Omdat deze wijken aan de zuidrand van de stad liggen, bevestigen we de verwachte aankomsttijd vooraf."),
    ],
    nearby=["diemen", "amsterdam-oost", "weesp", "amstelveen"],
    geo=(52.3150, 4.9600),
)

AREAS["weesp"] = dict(
    name="Weesp", kind="stadsdeel",
    title="Lachgas Weesp bestellen | 24/7 bezorgd | LachGasAdam247",
    description="Lachgas bestellen in Weesp? 24/7 bezorgd in het centrum, Weesp-Noord, Weesp-Zuid en de Bloemendalerpolder. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Weesp",
    lead="Weesp hoort sinds 2022 bij de gemeente Amsterdam en valt volledig binnen ons bezorggebied. LachGasAdam247 bezorgt lachgas tanks in het historische centrum aan de Vecht, in Weesp-Noord, Weesp-Zuid, de Bloemendalerpolder en Nieuwe Vecht. 24/7 bereikbaar via WhatsApp en telefoon.",
    wijken=["Centrum Weesp", "Weesp-Noord", "Weesp-Zuid", "Hogeweij", "Aetsveld", "Leeuwenveld", "Bloemendalerpolder", "Nieuwe Vecht", "Weespersluis", "Driemond (grens)"],
    intro=[
        "Weesp heeft nog altijd een eigen karakter: een historisch stadscentrum aan de Vecht, met smalle straten, water, oude vestingwerken en compacte bebouwing. Daaromheen liggen nieuwere wijken zoals Hogeweij, Aetsveld, Leeuwenveld en de nieuwbouw in de Bloemendalerpolder (Weespersluis). Wij bezorgen lachgas in heel Weesp en in de directe omgeving.",
        "Omdat Weesp iets buiten de stad ligt, aan de A1 en de spoorlijn richting het Gooi, plannen we leveringen hier graag vooraf en bevestigen we de aankomsttijd voordat we vertrekken. Vanuit Amsterdam Zuidoost of Diemen zijn we doorgaans binnen 25 tot 40 minuten in Weesp. Geef je adres, postcode en gewenste moment door via WhatsApp of telefoon, dan laten we direct weten wat haalbaar is.",
    ],
    letten=[
        "<strong>Het centrum aan de Vecht.</strong> Smalle straten en eenrichtingsverkeer rond de Nieuwstraat, de Slijkstraat en de Oudegracht. We spreken een goed bereikbare plek af als we niet tot aan de deur kunnen.",
        "<strong>Bloemendalerpolder en Weespersluis.</strong> Nieuwbouw met straten die nog niet in elke navigatie staan. Een postcode en huisnummer plus een herkenningspunt helpen.",
        "<strong>Weesp-Noord en Weesp-Zuid.</strong> Rustige woonwijken met eengezinswoningen en portiekflats. Vermeld het portiek en de verdieping waar van toepassing.",
        "<strong>Omliggende dorpen.</strong> Muiden, Muiderberg, Driemond en de Vechtstreek liggen aan de rand van ons werkgebied. Stuur je postcode, dan bevestigen we of we kunnen komen.",
    ],
    extra_h="Weesp, Muiden en de Vechtstreek",
    extra="Weesp is een populaire plek voor wie rustig wil wonen op een kwartier van Amsterdam. Rond het Fort aan de Ossenmarkt, de Vecht en de Grote Kerk is het in de zomer gezellig druk met terrassen en bootjes. Ook in de nieuwe wijken in de Bloemendalerpolder wonen veel jonge gezinnen en stellen die uit Amsterdam zijn verhuisd. Wij bezorgen bij woningen en appartementen in heel Weesp, en in overleg ook in Muiden, Muiderberg en de dorpen langs de Vecht. Woon je dichter bij Amsterdam Zuidoost of Diemen? Bekijk dan ook onze pagina&rsquo;s voor <a href=\"/bezorggebied/amsterdam-zuidoost/\">lachgas Amsterdam Zuidoost</a> en <a href=\"/bezorggebied/diemen/\">lachgas Diemen</a>.",
    faq=[
        ("Hoe lang duurt bezorgen in Weesp?",
         "Doorgaans 25 tot 40 minuten, afhankelijk van waar onze bezorger op dat moment is en de drukte op de A1 en de Gooiseweg. We bevestigen de verwachte aankomsttijd altijd vooraf."),
        ("Bezorgen jullie ook in Muiden en Muiderberg?",
         "In overleg. Muiden, Muiderberg en de dorpen aan de Vecht liggen aan de rand van ons werkgebied. Stuur je postcode via WhatsApp, dan laten we direct weten of we kunnen komen."),
        ("Kan ik lachgas bestellen in de nieuwbouw in de Bloemendalerpolder?",
         "Ja. Geef je postcode en huisnummer door en, omdat sommige straten nog nieuw zijn, een herkenningspunt zoals een plein of een hoekwoning. Zo vindt onze bezorger je adres snel."),
    ],
    nearby=["amsterdam-zuidoost", "diemen", "almere", "amsterdam-oost"],
    geo=(52.3070, 5.0430),
)

# ---------------------------------------------------------------------------
# Regio
# ---------------------------------------------------------------------------
AREAS["amstelveen"] = dict(
    name="Amstelveen", kind="regio",
    title="Lachgas Amstelveen bestellen | 24/7 bezorgd vanuit Amsterdam",
    description="Lachgas bestellen in Amstelveen? 24/7 bezorgd in Stadshart, Randwijck, Westwijk, Waardhuizen en op Uilenstede. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Amstelveen",
    lead="Amstelveen grenst direct aan Amsterdam Zuid en Nieuw-West en hoort bij ons vaste werkgebied. LachGasAdam247 bezorgt lachgas tanks in Randwijck, het Keizer Karelpark, het Stadshart, Westwijk, Waardhuizen, Kostverloren, Bankras en op de campus van Uilenstede. 24/7 bereikbaar, aankomsttijd vooraf bevestigd.",
    wijken=["Stadshart", "Randwijck", "Elsrijk", "Keizer Karelpark", "Bankras", "Kostverloren", "Groenelaan", "Waardhuizen",
            "Middenhoven", "Westwijk", "Uilenstede", "Bovenkerk", "Nes aan de Amstel"],
    intro=[
        "Amstelveen ligt tegen de zuidkant van Amsterdam aan en is via de Amstelveenseweg, de Beneluxbaan, de A9 en tramlijn 25 uitstekend bereikbaar. Voor onze bezorgers is Amstelveen daardoor bijna een verlengstuk van Amsterdam Zuid: vanuit Buitenveldert of de Zuidas zijn we in een paar minuten in Randwijck, Elsrijk of het Stadshart.",
        "Wij bezorgen in heel Amstelveen, van de appartementen in het Stadshart en de studentencampus Uilenstede tot de ruime woonwijken Westwijk, Waardhuizen en Middenhoven en het dorpse Bovenkerk en Nes aan de Amstel. Stuur je adres via WhatsApp, dan bevestigen we het levermoment en de prijs. Doorgaans zijn we in Amstelveen binnen 25 tot 40 minuten.",
    ],
    letten=[
        "<strong>Uilenstede.</strong> Op de studentencampus staan veel gebouwen die op elkaar lijken. Geef het gebouwnummer, de ingang en je kamer of verdieping door.",
        "<strong>Stadshart en Bankras.</strong> Appartementencomplexen met meerdere ingangen en parkeergarages. Vermeld de ingang en de verdieping.",
        "<strong>Westwijk, Waardhuizen en Middenhoven.</strong> Ruime wijken met eengezinswoningen; een huisnummer en postcode zijn genoeg.",
        "<strong>Bovenkerk en Nes aan de Amstel.</strong> Aan de zuidrand van Amstelveen; hier plannen we de rit vooraf en bevestigen we de aankomsttijd.",
    ],
    extra_h="Stadshart, Uilenstede en het Amsterdamse Bos",
    extra="Amstelveen is een rustige, groene stad met een internationaal karakter en veel expats en studenten. Rond het Stadshart, het Stadsplein en de Amsterdamseweg zit de horeca, en de campus van Uilenstede is met duizenden studenten een van de grootste van Nederland. Wij bezorgen bij woningen, appartementen, studentenkamers en hotels in heel Amstelveen, ook &rsquo;s nachts en in het weekend. Woon je aan de Amsterdamse kant van de grens, in Buitenveldert of de Zuidas? Kijk dan op de pagina <a href=\"/bezorggebied/amsterdam-zuid/\">lachgas Amsterdam Zuid</a>.",
    faq=[
        ("Bezorgen jullie ook op Uilenstede?",
         "Ja. Uilenstede is een van de plekken in Amstelveen waar we het vaakst komen. Geef het gebouwnummer, de ingang en je kamernummer of verdieping door en houd je telefoon bij de hand."),
        ("Hoe lang duurt bezorgen in Amstelveen?",
         "Doorgaans 25 tot 40 minuten, afhankelijk van waar je in Amstelveen woont en waar onze bezorger op dat moment is. Randwijck en Elsrijk zijn het snelst bereikbaar; Westwijk en Bovenkerk duren iets langer."),
        ("Is bezorgen in Amstelveen duurder dan in Amsterdam?",
         "De prijs hangt af van het aantal, de maat en het levermoment. Je hoort de prijs altijd vooraf in de bevestiging, ook als er een toeslag voor de afstand geldt. Er komen geen kosten achteraf bij."),
    ],
    nearby=["amsterdam-zuid", "amsterdam-nieuw-west", "hoofddorp", "amsterdam-zuidoost"],
    geo=(52.3030, 4.8630),
)

AREAS["diemen"] = dict(
    name="Diemen", kind="regio",
    title="Lachgas Diemen bestellen | 24/7 bezorgd | LachGasAdam247",
    description="Lachgas bestellen in Diemen? 24/7 bezorgd in Diemen-Centrum, Noord, Zuid, Holland Park en Plantage de Sniep in 25-35 min. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Diemen",
    lead="Diemen ligt ingeklemd tussen Amsterdam Oost, Zuidoost en Weesp en is voor onze bezorgers snel bereikbaar. LachGasAdam247 bezorgt lachgas tanks in Diemen-Centrum, Diemen-Noord, Diemen-Zuid, Plantage de Sniep en Holland Park, en in overleg in Duivendrecht. 24/7 bereikbaar via WhatsApp en telefoon.",
    wijken=["Diemen-Centrum", "Diemen-Noord", "Diemen-Zuid", "Plantage de Sniep", "Holland Park", "Bergwijkpark", "Duivendrecht", "Over-Diemen"],
    intro=[
        "Diemen is een zelfstandige gemeente, maar voelt voor veel Amsterdammers als een buitenwijk van Oost. Via de Hartveldseweg, de Gooiseweg, de A1 en de A10 zijn we er vanuit Oost of Zuidoost in een paar minuten. Rond station Diemen Zuid is de afgelopen jaren de nieuwe wijk Holland Park verrezen, met duizenden appartementen en veel studenten en jonge stellen.",
        "Wij bezorgen lachgas in heel Diemen: het oude centrum rond de Ouddiemerlaan, de woonwijken Diemen-Noord en Diemen-Zuid, de nieuwbouw in Plantage de Sniep en Holland Park, en in overleg ook in Duivendrecht (gemeente Ouder-Amstel). Stuur je adres via WhatsApp, dan bevestigen we het levermoment en de prijs. Doorgaans zijn we in Diemen binnen 25 tot 35 minuten.",
    ],
    letten=[
        "<strong>Holland Park en Bergwijkpark.</strong> Grote nieuwbouwcomplexen met meerdere ingangen en woontorens. Geef de naam van het gebouw, de ingang en de verdieping door.",
        "<strong>Diemen-Centrum en Diemen-Noord.</strong> Woonstraten met eengezinswoningen en portiekflats. Vermeld het portiek waar nodig.",
        "<strong>Plantage de Sniep.</strong> Nieuwbouw aan het water; sommige straten zijn nog nieuw in navigatie. Een herkenningspunt helpt.",
        "<strong>Duivendrecht.</strong> Hoort bij de gemeente Ouder-Amstel en ligt naast Zuidoost. Levering in overleg met een aankomsttijd vooraf.",
    ],
    extra_h="Holland Park, station Diemen Zuid en de Diemerscheg",
    extra="Diemen is een van de snelst groeiende plekken rond Amsterdam. Holland Park bij station Diemen Zuid huisvest inmiddels duizenden bewoners, veelal studenten en starters die de stad net te duur vinden. Het oude centrum rond de Ouddiemerlaan en het Diemerplein blijft dorps en rustig, en de Diemerscheg en het Diemerbos zijn populaire plekken om buiten te zijn. Wij bezorgen bij woningen en appartementen in heel Diemen, ook &rsquo;s nachts en in het weekend. Woon je net over de grens in de Watergraafsmeer of op IJburg? Kijk dan op de pagina <a href=\"/bezorggebied/amsterdam-oost/\">lachgas Amsterdam Oost</a>.",
    faq=[
        ("Hoe snel bezorgen jullie in Holland Park en bij station Diemen Zuid?",
         "Doorgaans binnen 25 tot 35 minuten. Holland Park ligt direct aan de A10 en de Gooiseweg en is goed bereikbaar vanuit Zuidoost en Oost. Geef het gebouw en de ingang door, dan verloopt de overdracht snel."),
        ("Bezorgen jullie ook in Duivendrecht en Ouderkerk aan de Amstel?",
         "Duivendrecht ja, in overleg en met een aankomsttijd vooraf. Ouderkerk aan de Amstel ligt iets verder; stuur je postcode via WhatsApp, dan laten we weten of we kunnen komen."),
        ("Kan ik ook &rsquo;s nachts lachgas bestellen in Diemen?",
         "Ja. Wij zijn 24/7 bereikbaar en bezorgen in Diemen ook &rsquo;s avonds laat, &rsquo;s nachts en in het weekend. Vermeld je adres volledig, inclusief ingang en verdieping bij een complex."),
    ],
    nearby=["amsterdam-oost", "amsterdam-zuidoost", "weesp", "amsterdam-centrum"],
    geo=(52.3390, 4.9620),
)

AREAS["zaandam"] = dict(
    name="Zaandam", kind="regio",
    title="Lachgas Zaandam bestellen | 24/7 bezorgd vanuit Amsterdam",
    description="Lachgas bestellen in Zaandam? 24/7 bezorgd in Zaandam, Zaandijk, Koog aan de Zaan, Wormerveer en Krommenie. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Zaandam en Zaanstad",
    lead="Zaandam ligt direct ten noorden van Amsterdam, aan de overkant van het Noordzeekanaal. LachGasAdam247 bezorgt lachgas tanks in Zaandam-Centrum, Zaandam-Zuid, Poelenburg, Westerwatering, Zaandijk, Koog aan de Zaan, Wormerveer en Krommenie. 24/7 bereikbaar, met een aankomsttijd die we vooraf bevestigen.",
    wijken=["Zaandam-Centrum", "Zaandam-Zuid", "Inverdan", "Poelenburg", "Peldersveld", "Westerwatering", "Westerkoog", "Kogerveld",
            "Zaandijk", "Koog aan de Zaan", "Wormerveer", "Krommenie", "Assendelft", "Westzaan", "Oostzaan"],
    intro=[
        "Zaandam en de andere Zaanse kernen liggen op een kwartier rijden van Amsterdam Noord en West, via de Coentunnel, de A8 en de A10. Vanuit Noord of de Houthavens zijn we snel op de Provincialeweg en in het centrum van Zaandam. Wij bezorgen lachgas in heel Zaanstad: van de nieuwe Inverdan-wijk rond station Zaandam en de Gedempte Gracht tot Poelenburg, Westerwatering, Zaandijk, Koog aan de Zaan, Wormerveer en Krommenie.",
        "Omdat Zaandam buiten Amsterdam ligt, plannen we leveringen hier in overleg en bevestigen we de verwachte aankomsttijd vooraf. Doorgaans zijn we in Zaandam binnen 30 tot 45 minuten; voor Wormerveer, Krommenie en Assendelft rekenen we iets meer tijd. Stuur je adres en postcode via WhatsApp, dan weet je direct waar je aan toe bent.",
    ],
    letten=[
        "<strong>Inverdan en het centrum.</strong> Rond station Zaandam, de Gedempte Gracht en het Zaantheater staan veel appartementen boven winkels. Geef de ingang en de verdieping door.",
        "<strong>Poelenburg, Peldersveld en Kogerveld.</strong> Wijken met portiek- en galerijflats. Vermeld het portiek en de verdieping.",
        "<strong>Zaandijk, Koog en Wormerveer.</strong> Langs de Zaan, met smalle dijkwegen en eenrichtingsverkeer. Een herkenningspunt helpt.",
        "<strong>Coentunnel en spits.</strong> In de ochtend- en avondspits kan de Coentunnel vaststaan. &rsquo;s Avonds en in het weekend zijn we sneller.",
    ],
    extra_h="Zaanse Schans, Inverdan en de Zaanoevers",
    extra="Zaandam heeft zich de afgelopen jaren ontwikkeld van industriestad tot een populaire woonplaats voor Amsterdammers die meer ruimte zoeken. Rond de Zaanoevers en het Hembrugterrein verrijzen nieuwe appartementen, het centrum rond de Gedempte Gracht heeft veel horeca, en de Zaanse Schans trekt het hele jaar bezoekers. Wij bezorgen bij woningen, appartementen en hotels in heel Zaanstad, ook &rsquo;s nachts en in het weekend. Woon je aan de Amsterdamse kant van het kanaal, bijvoorbeeld in Tuindorp Oostzaan of Kadoelen? Kijk dan op de pagina <a href=\"/bezorggebied/amsterdam-noord/\">lachgas Amsterdam Noord</a>.",
    faq=[
        ("Hoe lang duurt bezorgen in Zaandam?",
         "Doorgaans 30 tot 45 minuten, afhankelijk van de drukte in de Coentunnel en waar onze bezorger op dat moment is. Voor Wormerveer, Krommenie en Assendelft rekenen we iets meer tijd. We bevestigen de aankomsttijd altijd vooraf."),
        ("Bezorgen jullie in heel Zaanstad, ook in Krommenie en Assendelft?",
         "Ja, in overleg. Krommenie, Assendelft en Westzaan liggen aan de rand van ons werkgebied. Stuur je postcode via WhatsApp, dan laten we direct weten of we kunnen komen en wanneer."),
        ("Kan ik ook in Oostzaan en Landsmeer bestellen?",
         "Ja, in overleg. Oostzaan en Landsmeer liggen tussen Amsterdam Noord en Zaandam en zijn goed bereikbaar. Stuur je adres, dan bevestigen we het levermoment."),
    ],
    nearby=["amsterdam-noord", "purmerend", "amsterdam-west", "haarlem"],
    geo=(52.4390, 4.8290),
)

AREAS["haarlem"] = dict(
    name="Haarlem", kind="regio",
    title="Lachgas Haarlem bestellen | 24/7 bezorgd vanuit Amsterdam",
    description="Lachgas bestellen in Haarlem? 24/7 bezorgd in Haarlem-Centrum, Noord, Oost, Schalkwijk en Zuid-West. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Haarlem",
    lead="Haarlem ligt op twintig minuten rijden ten westen van Amsterdam. LachGasAdam247 bezorgt lachgas tanks in het centrum van Haarlem, in Haarlem-Noord, Haarlem-Oost, Schalkwijk, Zuid-West en in overleg in Heemstede, Bloemendaal en Zandvoort. 24/7 bereikbaar via WhatsApp en telefoon, aankomsttijd vooraf bevestigd.",
    wijken=["Haarlem-Centrum", "Burgwalbuurt", "Haarlem-Noord", "Kleverpark", "Haarlem-Oost", "Parkwijk", "Schalkwijk", "Europawijk",
            "Zuid-West", "Bosch en Vaart", "Heemstede", "Bloemendaal", "Overveen", "Zandvoort", "Spaarndam"],
    intro=[
        "Haarlem is via de A200 (Haarlemmerweg), de A9 en de A5 goed bereikbaar vanuit Amsterdam West en Nieuw-West. Onze bezorgers rijden regelmatig naar Haarlem, vooral in het weekend en &rsquo;s avonds. Wij bezorgen in het historische centrum rond de Grote Markt en de Burgwal, in Haarlem-Noord en het Kleverpark, in Haarlem-Oost en Parkwijk, in Schalkwijk en in de wijken in Zuid-West rond de Leidsevaart.",
        "Omdat de reistijd naar Haarlem langer is dan binnen Amsterdam, plannen we leveringen hier in overleg. Doorgaans zijn we in Haarlem binnen 35 tot 50 minuten; voor Heemstede, Bloemendaal, Overveen en Zandvoort rekenen we iets meer tijd. Stuur je adres en postcode via WhatsApp of bel ons, dan bevestigen we het levermoment en de prijs voordat we vertrekken.",
    ],
    letten=[
        "<strong>Het centrum en de Burgwal.</strong> Smalle straten, eenrichtingsverkeer en een autoluw centrum rond de Grote Markt. We spreken een goed bereikbaar punt af als we niet tot aan de deur kunnen.",
        "<strong>Schalkwijk en Europawijk.</strong> Flats en portiekwoningen; vermeld het portiek en de verdieping.",
        "<strong>Haarlem-Noord en Kleverpark.</strong> Woonstraten met bovenwoningen en gedeelde voordeuren. Geef de juiste bel door.",
        "<strong>Heemstede, Bloemendaal en Zandvoort.</strong> Levering in overleg; in de zomer is het richting Zandvoort druk op de weg.",
    ],
    extra_h="Grote Markt, Haarlemmerhout en het strand",
    extra="Haarlem staat bekend om zijn gezellige centrum met de Grote Markt, de Botermarkt, de Haarlemmerhout en de vele bars en restaurants. Ook de studentenhuizen rond de Zijlweg en het Kleverpark en de nieuwbouw in Haarlem-Oost en bij het Spaarne zorgen voor een jong publiek. Wij bezorgen bij woningen, appartementen en hotels in heel Haarlem, ook &rsquo;s nachts en in het weekend. In de zomer bezorgen we in overleg ook in Zandvoort en Bloemendaal aan Zee. Woon je dichter bij Amsterdam, bijvoorbeeld in Halfweg of Zwanenburg? Kijk dan ook op de pagina <a href=\"/bezorggebied/hoofddorp/\">lachgas Hoofddorp en Haarlemmermeer</a>.",
    faq=[
        ("Hoe lang duurt bezorgen in Haarlem?",
         "Doorgaans 35 tot 50 minuten vanaf de bevestiging, afhankelijk van de drukte op de A200 en de A9 en waar onze bezorger op dat moment is. We bevestigen de verwachte aankomsttijd altijd vooraf."),
        ("Bezorgen jullie ook in Zandvoort en Bloemendaal aan Zee?",
         "In overleg, vooral in de zomermaanden en in het weekend. Stuur je adres via WhatsApp, dan laten we direct weten of we kunnen komen en wat de verwachte aankomsttijd is."),
        ("Is er een minimale bestelling voor Haarlem?",
         "Omdat de reistijd langer is, bespreken we bij een bestelling in Haarlem het aantal en de prijs vooraf. Je hoort in de bevestiging precies wat het kost, zonder verrassingen achteraf."),
    ],
    nearby=["amsterdam-west", "amsterdam-nieuw-west", "hoofddorp", "zaandam"],
    geo=(52.3874, 4.6462),
)

AREAS["hoofddorp"] = dict(
    name="Hoofddorp", kind="regio",
    title="Lachgas Hoofddorp bestellen | Haarlemmermeer | 24/7 bezorgd",
    description="Lachgas bestellen in Hoofddorp, Badhoevedorp, Nieuw-Vennep of bij Schiphol? 24/7 bezorgd in heel Haarlemmermeer. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Hoofddorp en Haarlemmermeer",
    lead="Hoofddorp, Badhoevedorp, Nieuw-Vennep, Zwanenburg, Halfweg en de hotels rond Schiphol: de gemeente Haarlemmermeer ligt direct ten westen van Amsterdam en hoort bij ons werkgebied. LachGasAdam247 bezorgt lachgas tanks in de hele Haarlemmermeer, 24/7 bereikbaar via WhatsApp en telefoon.",
    wijken=["Hoofddorp-Centrum", "Floriande", "Toolenburg", "Overbos", "Bornholm", "Pax", "Graan voor Visch", "Badhoevedorp",
            "Schiphol", "Nieuw-Vennep", "Zwanenburg", "Halfweg", "Lijnden", "Vijfhuizen", "Rijsenhout"],
    intro=[
        "Haarlemmermeer is een grote gemeente met Hoofddorp als centrum, omringd door dorpen als Badhoevedorp, Nieuw-Vennep, Zwanenburg, Halfweg en Vijfhuizen, en met de luchthaven Schiphol in het midden. Via de A4, de A5 en de A9 zijn we vanuit Amsterdam Nieuw-West en Zuid snel in Badhoevedorp en Hoofddorp. Wij bezorgen lachgas in het centrum van Hoofddorp, in de woonwijken Floriande, Toolenburg, Overbos, Bornholm en Pax, en in de omliggende dorpen.",
        "Rond Schiphol staan tientallen hotels waar we regelmatig leveren: geef de naam van het hotel, je kamernummer of een aanspreekpunt en een geschikt moment door. Omdat Haarlemmermeer buiten Amsterdam ligt, plannen we leveringen in overleg en bevestigen we de aankomsttijd vooraf. Doorgaans zijn we in Badhoevedorp binnen 25 tot 35 minuten en in Hoofddorp binnen 30 tot 45 minuten.",
    ],
    letten=[
        "<strong>Badhoevedorp en Lijnden.</strong> Direct naast Nieuw-West en de A4; hier zijn we het snelst. Geef je huisnummer en postcode door.",
        "<strong>Hotels rond Schiphol.</strong> Bij hotels aan de Schipholweg, in Schiphol-Oost, Badhoevedorp en Hoofddorp leveren we op afspraak bij de receptie of een aanspreekpunt. Op de luchthaven zelf leveren we niet.",
        "<strong>Floriande en Toolenburg.</strong> Nieuwbouwwijken met veel eengezinswoningen en soms lastig vindbare straten. Een herkenningspunt helpt.",
        "<strong>Nieuw-Vennep en Rijsenhout.</strong> Zuidelijker in de polder; levering in overleg met een aankomsttijd vooraf.",
    ],
    extra_h="Hoofddorp-Centrum, Schiphol en de dorpen in de polder",
    extra="Hoofddorp is uitgegroeid tot een stad met een druk centrum rond het Raadhuisplein en het Burgemeester Van Stamplein, veel jonge gezinnen in Floriande en Toolenburg en tienduizenden mensen die bij Schiphol werken. Badhoevedorp ligt op een steenworp van Amsterdam en verandert door de omlegging van de A9 in een rustig dorp met veel nieuwbouw. Wij bezorgen bij woningen, appartementen en hotels in de hele Haarlemmermeer, ook &rsquo;s nachts en in het weekend. Woon je aan de Amsterdamse kant, in Osdorp of Sloten? Kijk dan op de pagina <a href=\"/bezorggebied/amsterdam-nieuw-west/\">lachgas Amsterdam Nieuw-West</a>.",
    faq=[
        ("Bezorgen jullie bij hotels rond Schiphol?",
         "Ja, bij hotels in Badhoevedorp, Hoofddorp, Schiphol-Oost en langs de Schipholweg leveren we regelmatig. Geef de naam van het hotel, een aanspreekpunt of kamernummer en een geschikt moment door. Op het luchthaventerrein zelf leveren we niet."),
        ("Hoe lang duurt bezorgen in Hoofddorp?",
         "Doorgaans 30 tot 45 minuten; in Badhoevedorp en Lijnden zijn we sneller, meestal binnen 25 tot 35 minuten. We bevestigen de verwachte aankomsttijd altijd voordat we vertrekken."),
        ("Bezorgen jullie ook in Nieuw-Vennep en Vijfhuizen?",
         "Ja, in overleg. Stuur je adres en postcode via WhatsApp, dan laten we direct weten of we kunnen komen en wat de verwachte aankomsttijd is."),
    ],
    nearby=["amsterdam-nieuw-west", "amstelveen", "haarlem", "amsterdam-west"],
    geo=(52.3030, 4.6890),
)

AREAS["almere"] = dict(
    name="Almere", kind="regio",
    title="Lachgas Almere bestellen | 24/7 bezorgd vanuit Amsterdam",
    description="Lachgas bestellen in Almere? 24/7 bezorgd in Almere Stad, Buiten, Haven, Poort en Hout. Levering in overleg. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Almere",
    lead="Almere ligt aan de overkant van het IJmeer en is via de A1 en de A6 in ongeveer een half uur bereikbaar vanuit Amsterdam. LachGasAdam247 bezorgt lachgas tanks in Almere Stad, Almere Buiten, Almere Haven, Almere Poort, Almere Hout en Almere Muziekwijk. 24/7 bereikbaar via WhatsApp en telefoon, aankomsttijd vooraf bevestigd.",
    wijken=["Almere Stad", "Almere Centrum", "Muziekwijk", "Filmwijk", "Literatuurwijk", "Stedenwijk", "Almere Buiten", "Almere Haven",
            "Almere Poort", "Almere Hout", "Tussen de Vaarten", "Noorderplassen", "Danswijk", "Parkwijk"],
    intro=[
        "Almere is de grootste stad van Flevoland en de jongste stad van Nederland, met ruim tweehonderdduizend inwoners verdeeld over Almere Stad, Buiten, Haven, Poort en Hout. Veel bewoners zijn oorspronkelijk Amsterdammers, en de band met de stad is sterk. Vanuit Amsterdam Zuidoost of Oost rijden we via de A1 en de A6, of via de A9 en de Hollandse Brug, in ongeveer een half uur naar Almere.",
        "Wij bezorgen lachgas in alle stadsdelen van Almere: het centrum rond het Stadhuisplein en de Grote Markt, de Muziekwijk, Filmwijk en Literatuurwijk in Almere Stad, de wijken in Almere Buiten en Almere Haven, de nieuwbouw in Almere Poort en Almere Hout en de Noorderplassen. Omdat Almere verder van Amsterdam ligt, plannen we leveringen in overleg en bevestigen we de aankomsttijd vooraf. Doorgaans zijn we in Almere binnen 40 tot 60 minuten.",
    ],
    letten=[
        "<strong>Almere Poort en Almere Haven.</strong> Het dichtst bij Amsterdam, via de Hollandse Brug; hier zijn we het snelst.",
        "<strong>Almere Stad en het centrum.</strong> Appartementen boven winkels en woontorens rond het station; geef de ingang en de verdieping door.",
        "<strong>Almere Buiten en Almere Hout.</strong> Verder naar het oosten; reken op iets meer reistijd. Een herkenningspunt in nieuwbouwwijken helpt.",
        "<strong>Drukte op de A6 en de A1.</strong> In de spits en bij evenementen (zoals in de Noorderplassen of bij Almere Strand) kan het langer duren.",
    ],
    extra_h="Almere Centrum, Almere Poort en het strand",
    extra="Almere heeft een modern centrum met veel horeca rond het Stadhuisplein, de Grote Markt en de Esplanade, en een jong publiek in de Muziekwijk, Filmwijk en Almere Poort. In de zomer zijn Almere Strand, de Noorderplassen en het Almeerderstrand populair. Wij bezorgen bij woningen, appartementen en hotels in heel Almere, ook &rsquo;s nachts en in het weekend. Bestel je vanuit Almere, geef dan je adres, postcode en gewenste moment door, dan laten we direct weten wat haalbaar is. Woon je dichter bij Amsterdam, in Weesp of Muiden? Kijk dan op de pagina <a href=\"/bezorggebied/weesp/\">lachgas Weesp</a>.",
    faq=[
        ("Hoe lang duurt bezorgen in Almere?",
         "Doorgaans 40 tot 60 minuten, afhankelijk van het stadsdeel en de drukte op de A6 en de A1. Almere Poort en Almere Haven zijn het snelst bereikbaar; Almere Buiten en Almere Hout duren iets langer. We bevestigen de aankomsttijd altijd vooraf."),
        ("Bezorgen jullie in heel Almere?",
         "Ja: Almere Stad, Buiten, Haven, Poort en Hout. Omdat de afstand groter is, plannen we de levering in overleg. Stuur je adres via WhatsApp, dan hoor je direct of en wanneer we kunnen komen."),
        ("Geldt er een toeslag voor bezorging in Almere?",
         "De prijs hangt af van het aantal, de maat en de afstand. Je hoort de totaalprijs altijd vooraf in de bevestiging, inclusief een eventuele toeslag voor de rit naar Almere. Er komen geen kosten achteraf bij."),
    ],
    nearby=["weesp", "amsterdam-zuidoost", "diemen", "amsterdam-oost"],
    geo=(52.3508, 5.2647),
)

AREAS["purmerend"] = dict(
    name="Purmerend", kind="regio",
    title="Lachgas Purmerend bestellen | Waterland | 24/7 bezorgd",
    description="Lachgas bestellen in Purmerend? 24/7 bezorgd in het centrum, Weidevenne, Purmer-Noord, Purmer-Zuid en Waterland. WhatsApp of bel %s." % PHONE_DISPLAY,
    h1="Lachgas bestellen in Purmerend en Waterland",
    lead="Purmerend ligt ten noorden van Amsterdam, via de A7 en de A10 op ongeveer twintig minuten rijden van Amsterdam Noord. LachGasAdam247 bezorgt lachgas tanks in het centrum van Purmerend, in Weidevenne, Purmer-Noord, Purmer-Zuid, Overwhere en Wheermolen, en in overleg in de Waterlandse dorpen. 24/7 bereikbaar via WhatsApp en telefoon.",
    wijken=["Purmerend-Centrum", "Weidevenne", "Purmer-Noord", "Purmer-Zuid", "Overwhere", "Wheermolen", "Gors", "De Purmer",
            "Landsmeer", "Ilpendam", "Monnickendam", "Broek in Waterland", "Edam", "Volendam"],
    intro=[
        "Purmerend is de grootste stad van Waterland en groeide de afgelopen decennia uit tot een populaire woonplaats voor Amsterdammers. Via de A7 en de A10 rijden we vanuit Amsterdam Noord in ongeveer twintig minuten naar het centrum van Purmerend. Wij bezorgen lachgas in de binnenstad rond de Koemarkt en de Kaasmarkt, in Weidevenne, Purmer-Noord, Purmer-Zuid, Overwhere, Wheermolen en de Gors.",
        "In overleg bezorgen we ook in de Waterlandse dorpen tussen Amsterdam en Purmerend, zoals Landsmeer, Ilpendam, Broek in Waterland en Monnickendam, en verder in Edam en Volendam. Omdat Purmerend buiten Amsterdam ligt, plannen we leveringen vooraf en bevestigen we de aankomsttijd. Doorgaans zijn we in Purmerend binnen 30 tot 45 minuten.",
    ],
    letten=[
        "<strong>Purmerend-Centrum.</strong> Rond de Koemarkt en de Kaasmarkt is het in het weekend druk en zijn straten deels autoluw. We spreken een bereikbare plek af als we niet tot aan de deur kunnen.",
        "<strong>Weidevenne en Purmer-Zuid.</strong> Ruime nieuwbouwwijken met eengezinswoningen; een huisnummer en postcode zijn genoeg.",
        "<strong>Overwhere en Wheermolen.</strong> Portiek- en galerijflats; vermeld het portiek en de verdieping.",
        "<strong>Waterlandse dorpen.</strong> Landsmeer, Ilpendam, Broek in Waterland, Monnickendam, Edam en Volendam in overleg, met een aankomsttijd vooraf.",
    ],
    extra_h="Koemarkt, Weidevenne en de Waterlandse dorpen",
    extra="Purmerend heeft een gezellige binnenstad met veel horeca rond de Koemarkt, en jonge gezinnen in Weidevenne en Purmer-Zuid. De Waterlandse dorpen, van Broek in Waterland tot Monnickendam en Volendam, zijn populair bij wie rustig wil wonen op korte afstand van Amsterdam. Wij bezorgen bij woningen en appartementen in heel Purmerend en in overleg in Waterland, ook &rsquo;s nachts en in het weekend. Stuur je adres, postcode en gewenste moment via WhatsApp, dan laten we direct weten wat haalbaar is. Woon je dichter bij de stad, in Landsmeer of Amsterdam Noord? Kijk dan op de pagina <a href=\"/bezorggebied/amsterdam-noord/\">lachgas Amsterdam Noord</a>.",
    faq=[
        ("Hoe lang duurt bezorgen in Purmerend?",
         "Doorgaans 30 tot 45 minuten, afhankelijk van de drukte op de A7 en waar onze bezorger op dat moment is. We bevestigen de verwachte aankomsttijd altijd vooraf."),
        ("Bezorgen jullie ook in Volendam, Edam en Monnickendam?",
         "Ja, in overleg. De Waterlandse dorpen liggen aan de rand van ons werkgebied. Stuur je postcode via WhatsApp, dan laten we direct weten of we kunnen komen en wanneer."),
        ("Kan ik &rsquo;s nachts lachgas bestellen in Purmerend?",
         "Ja. Wij zijn 24/7 bereikbaar en bezorgen in Purmerend ook &rsquo;s avonds laat, &rsquo;s nachts en in het weekend. Omdat de afstand groter is, bevestigen we het levermoment vooraf."),
    ],
    nearby=["amsterdam-noord", "zaandam", "amsterdam-centrum", "almere"],
    geo=(52.5050, 4.9590),
)


ALL_AREA_SLUGS = [s for s, _ in STADSDELEN] + [s for s, _ in REGIO]


def area_page(slug):
    a = AREAS[slug]
    path = "/bezorggebied/%s/" % slug
    page = dict(
        path=path,
        title=a["title"],
        description=a["description"],
        h1=a["h1"],
        lead=a["lead"],
        crumbs=[("Home", "/"), ("Bezorggebied", "/bezorggebied/"), (a["name"], None)],
        faq=a["faq"],
        priority="0.8" if a["kind"] == "stadsdeel" else "0.7",
        changefreq="weekly",
        speakable=["#h1", ".lead"],
    )
    lat, lon = a["geo"]
    page["schema"] = [{
        "@type": "Service",
        "@id": SITE + path + "#service",
        "name": "Lachgas bezorgen in %s" % a["name"],
        "serviceType": "Lachgas bezorgservice",
        "description": a["description"],
        "url": SITE + path,
        "provider": {"@id": BUSINESS_ID},
        "areaServed": {"@type": "Place", "name": a["name"],
                       "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lon}},
        "availableChannel": [
            {"@type": "ServiceChannel", "name": "WhatsApp", "serviceUrl": WA_ORDER},
            {"@type": "ServiceChannel", "name": "Telefoon",
             "servicePhone": {"@type": "ContactPoint", "telephone": PHONE_TEL, "contactType": "customer service"}},
        ],
        "hoursAvailable": {"@type": "OpeningHoursSpecification",
                           "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                           "opens": "00:00", "closes": "23:59"},
    }]

    points = [
        "24/7 bereikbaar via WhatsApp en telefoon",
        "Bezorging in heel %s" % a["name"],
        "Levermoment en prijs vooraf bevestigd",
        "Uitsluitend voor volwassenen (18+)",
    ]
    body = [hero(page, "Lachgas %s · 24/7 bezorgd" % a["name"], points)]

    # Intro + wijken
    body.append('<section class="section" aria-labelledby="h-intro"><div class="wrap prose">'
                '<h2 id="h-intro">Lachgas bezorgen in %s</h2>%s'
                '<h3>Wijken en gebieden waar wij bezorgen</h3><p class="wijken">%s.</p>'
                '<p>Staat jouw buurt er niet bij? Stuur je postcode via %s, dan bevestigen we direct of we bij jou kunnen bezorgen.</p>'
                '</div></section>'
                % (esc(a["name"]), "".join("<p>%s</p>" % p for p in a["intro"]), ", ".join(a["wijken"]),
                   wa_link("WhatsApp")))

    # Zo bestel je
    body.append('<section class="section alt" aria-labelledby="h-zo"><div class="wrap prose">'
                '<h2 id="h-zo">Zo bestel je lachgas in %s</h2>'
                '<p>Bestellen gaat zonder webshop, account of formulier. Je regelt alles in één WhatsApp-gesprek of telefoontje.</p>%s'
                '</div></section>'
                % (esc(a["name"]), steps([
                    "<strong>Stuur je adres in %s en het gewenste aantal.</strong> Via WhatsApp of bel %s. Geef ook de verdieping en de juiste bel door." % (esc(a["name"]), phone_link()),
                    "<strong>Ontvang de bevestiging.</strong> Wij bevestigen het levermoment en de prijs, zodat je vooraf weet waar je aan toe bent.",
                    "<strong>Wij rijden naar je toe.</strong> Onze bezorger komt naar het afgesproken adres. We laten weten wanneer we in de buurt zijn.",
                    "<strong>Veilige overdracht en betaling.</strong> De betaalwijze bespreken we in het gesprek. Geen kosten achteraf.",
                ])))

    # Waar we op letten
    body.append('<section class="section" aria-labelledby="h-letten"><div class="wrap prose">'
                '<h2 id="h-letten">Bezorgen in %s: waar wij op letten</h2>%s'
                '<h3>%s</h3><p>%s</p></div></section>'
                % (esc(a["name"]), checks(a["letten"]), esc(a["extra_h"]), a["extra"]))

    # Tanks + safety teaser
    body.append('<section class="section alt" aria-labelledby="h-tanks"><div class="wrap prose">'
                '<h2 id="h-tanks">Lachgas tanks voor %s</h2>'
                '<p>Wij leveren lachgas tanks in verschillende maten. Welke maat past, hangt af van je gelegenheid en het aantal mensen. Bekijk het overzicht van <a href="/lachgas-tanks/">lachgas tanks en maten</a> of vraag ons advies via WhatsApp.</p>%s'
                '<div class="callout"><p><strong>Verantwoord gebruik.</strong> Lachgas is uitsluitend voor volwassenen (18+). Gebruik het nooit voordat je gaat rijden of fietsen en lees onze tips over <a href="/lachgas-informatie/veilig-gebruik/">veilig en verantwoord gebruik</a>.</p></div>'
                '</div></section>'
                % (esc(a["name"]), toc([("/lachgas-tanks/2kg/", "Lachgas tank 2 kg"), ("/lachgas-tanks/4kg/", "Lachgas tank 4 kg"),
                                        ("/lachgas-tanks/10kg/", "Lachgas tank 10 kg"), ("/zakelijk/", "Horeca en evenementen")])))

    body.append(faq_html(a["faq"], "Veelgestelde vragen over lachgas in %s" % a["name"]))

    # Nearby
    near = [(("/bezorggebied/%s/" % n), "Lachgas %s" % AREAS[n]["name"]) for n in a["nearby"]]
    body.append('<section class="section" aria-labelledby="h-nearby"><div class="wrap prose">'
                '<h2 id="h-nearby">Ook in de buurt van %s</h2>'
                '<p>Wij bezorgen in alle stadsdelen van Amsterdam en in de regio. Bekijk de bezorggebieden in de buurt of het <a href="/bezorggebied/">volledige overzicht van bezorggebieden</a>.</p>%s'
                '</div></section>' % (esc(a["name"]), toc(near)))

    body.append(cta_block("Nu lachgas bestellen in %s" % a["name"],
                          wa_text="LachGasAdam247 - lachgas bestellen in %s. Adres: , aantal: " % a["name"]))
    page["body"] = "".join(body)
    return page


def overview_page():
    path = "/bezorggebied/"
    page = dict(
        path=path,
        title="Bezorggebied lachgas Amsterdam | Alle stadsdelen en regio",
        description="Waar bezorgen wij lachgas? In alle stadsdelen van Amsterdam en in Amstelveen, Diemen, Zaandam, Haarlem, Hoofddorp, Almere en Purmerend. 24/7, prijs vooraf.",
        h1="Bezorggebied: lachgas in heel Amsterdam en de regio",
        lead="LachGasAdam247 bezorgt lachgas tanks in alle zeven stadsdelen van Amsterdam plus Weesp, en in de omliggende gemeenten. Kies hieronder je stadsdeel of plaats voor de bezorginformatie, wijken en veelgestelde vragen. Twijfel je? Stuur je postcode via WhatsApp, dan bevestigen we direct of we bij jou kunnen bezorgen.",
        crumbs=[("Home", "/"), ("Bezorggebied", None)],
        priority="0.9", changefreq="weekly",
        faq=[
            ("Bezorgen jullie in heel Amsterdam?",
             "Ja. Wij bezorgen in alle stadsdelen: Centrum, Noord, Zuid, Oost, West, Nieuw-West en Zuidoost, plus Weesp. In Amsterdam zijn we doorgaans binnen 20 tot 30 minuten ter plekke."),
            ("Bezorgen jullie ook buiten Amsterdam?",
             "Ja, in de regio werken we in overleg: Amstelveen, Diemen, Zaandam, Haarlem, Hoofddorp en Haarlemmermeer, Almere en Purmerend. Omdat de afstand groter is, duurt bezorging daar iets langer en bevestigen we de aankomsttijd vooraf."),
            ("Mijn plaats staat er niet bij. Kunnen jullie toch komen?",
             "Stuur je postcode via WhatsApp. Ligt je adres in de buurt van ons werkgebied, dan laten we direct weten of we kunnen komen en wat de verwachte aankomsttijd is."),
        ],
        speakable=["#h1", ".lead"],
    )
    page["schema"] = [{
        "@type": "ItemList",
        "@id": SITE + path + "#gebieden",
        "name": "Bezorggebieden lachgas Amsterdam en regio",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": "Lachgas bestellen in %s" % AREAS[s]["name"],
             "url": SITE + "/bezorggebied/%s/" % s}
            for i, s in enumerate(ALL_AREA_SLUGS)
        ],
    }]
    stads_cards = link_cards([("/bezorggebied/%s/" % s, "Lachgas %s" % n,
                               "Wijken: " + ", ".join(AREAS[s]["wijken"][:6]) + " en meer.") for s, n in STADSDELEN])
    regio_cards = link_cards([("/bezorggebied/%s/" % s, "Lachgas %s" % n,
                               AREAS[s]["lead"].split(". ")[0] + ".") for s, n in REGIO])
    body = [
        hero(page, "Bezorggebied · 24/7", ["Alle stadsdelen van Amsterdam", "Regio in overleg", "Doorgaans 20 tot 30 minuten in Amsterdam", "Aankomsttijd vooraf bevestigd"]),
        '<section class="section" aria-labelledby="h-stads"><div class="wrap"><h2 id="h-stads">Stadsdelen van Amsterdam</h2>'
        '<p class="intro">Amsterdam (020) bestaat uit zeven stadsdelen, aangevuld met Weesp. In elk stadsdeel bezorgen wij lachgas, dag en nacht. Klik op je stadsdeel voor de wijken, bezorgtips en veelgestelde vragen.</p>%s</div></section>' % stads_cards,
        '<section class="section alt" aria-labelledby="h-regio"><div class="wrap"><h2 id="h-regio">Regio rond Amsterdam</h2>'
        '<p class="intro">Buiten Amsterdam bezorgen we in overleg. Omdat de afstand groter is, plannen we deze leveringen vooraf en bevestigen we de verwachte aankomsttijd voordat we vertrekken.</p>%s</div></section>' % regio_cards,
        '<section class="section" aria-labelledby="h-tijd"><div class="wrap prose"><h2 id="h-tijd">Levertijden per gebied</h2>'
        '<p>De genoemde tijden zijn indicaties vanaf het moment dat je bestelling is bevestigd. Drukte, evenementen en het tijdstip kunnen de rit langer maken; we laten je altijd vooraf weten wanneer je ons kunt verwachten.</p>'
        '<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Gebied</th><th>Indicatie levertijd</th></tr></thead><tbody>'
        '<tr><td><strong>Amsterdam Centrum, West, Zuid, Oost</strong></td><td>20 tot 30 minuten</td></tr>'
        '<tr><td><strong>Amsterdam Noord, Nieuw-West, Zuidoost</strong></td><td>20 tot 40 minuten</td></tr>'
        '<tr><td><strong>Weesp, Diemen, Amstelveen, Badhoevedorp</strong></td><td>25 tot 40 minuten</td></tr>'
        '<tr><td><strong>Zaandam, Hoofddorp, Purmerend</strong></td><td>30 tot 45 minuten</td></tr>'
        '<tr><td><strong>Haarlem, Almere</strong></td><td>35 tot 60 minuten</td></tr>'
        '</tbody></table></div></div></section>',
        faq_html(page["faq"], "Veelgestelde vragen over ons bezorggebied"),
        cta_block("Lachgas bestellen in jouw buurt"),
    ]
    page["body"] = "".join(body)
    return page


def pages():
    return [overview_page()] + [area_page(s) for s in ALL_AREA_SLUGS]
