# -*- coding: utf-8 -*-
"""Informatiepagina's (artikelen) over lachgas."""
from common import (SITE, BUSINESS_ID, OG_IMAGE, TODAY, PHONE_DISPLAY, esc, doc_page, checks, steps, faq_html,
                    cta_block, toc, crumbs_html)

ARTICLES = {}

ARTICLES["wat-is-lachgas"] = dict(
    title="Wat is lachgas (N2O)? Feiten, gebruik en geschiedenis",
    description="Wat is lachgas precies? Alles over distikstofmonoxide (N2O): eigenschappen, geschiedenis sinds 1772, gebruik in zorg, horeca en industrie, en het milieu.",
    h1="Wat is lachgas?",
    lead="Lachgas is de gangbare naam voor distikstofmonoxide, een kleurloos gas met een lichtzoete geur en de scheikundige formule N<sub>2</sub>O. Het wordt al meer dan twee eeuwen gebruikt in de geneeskunde, en tegenwoordig ook in de voedingsindustrie, de horeca en de techniek. In dit artikel lees je wat lachgas is, hoe het werkt en waar het vandaan komt.",
    body="""
<h2>De scheikunde van lachgas</h2>
<p>Distikstofmonoxide bestaat uit twee stikstofatomen en één zuurstofatoom. Bij kamertemperatuur en normale druk is het een gas dat ongeveer anderhalf keer zo zwaar is als lucht. Onder druk wordt het vloeibaar, en in die vorm wordt het bewaard in stalen tanks en cilinders. Lachgas brandt zelf niet, maar het onderhoudt wel een verbranding, net als zuurstof. Daarom mag een tank nooit in de buurt van open vuur of een warmtebron staan.</p>
<p>Lachgas lost slecht op in water en reageert bij normale temperaturen nauwelijks met andere stoffen. Dat maakt het stabiel en makkelijk te bewaren. In het lichaam werkt het snel: het wordt via de longen opgenomen in het bloed en binnen enkele minuten ook weer uitgeademd.</p>
<h2>Geschiedenis: van Priestley tot de tandarts</h2>
<p>De Britse wetenschapper Joseph Priestley ontdekte lachgas in 1772. Aan het eind van die eeuw onderzocht de chemicus Humphry Davy de werking van het gas op mensen. Hij merkte dat proefpersonen gingen lachen en euforisch werden, en gaf het gas daarom de naam laughing gas: lachgas. Davy opperde al dat het gas bruikbaar zou kunnen zijn bij operaties, maar het duurde nog decennia voordat dat idee werd opgepakt.</p>
<p>In 1844 gebruikte de Amerikaanse tandarts Horace Wells lachgas voor het eerst om een tandheelkundige ingreep pijnloos te maken. Daarmee begon het medische gebruik van lachgas als pijnstiller en licht verdovend middel. Tot op de dag van vandaag wordt lachgas, gemengd met zuurstof, gebruikt bij tandartsen, tijdens bevallingen en op spoedeisende hulpafdelingen.</p>
<h2>Waarvoor wordt lachgas gebruikt?</h2>
""" + checks([
        "<strong>In de zorg.</strong> Als pijnstillend en licht verdovend gas, altijd gemengd met zuurstof en onder toezicht van een arts of tandarts.",
        "<strong>In de voedingsindustrie en de horeca.</strong> Als drijfgas in slagroomspuiten en spuitbussen, onder de aanduiding E942. De bekende slagroompatronen bevatten lachgas.",
        "<strong>In de techniek en de autosport.</strong> Als oxidator die extra zuurstof levert aan een verbrandingsmotor of een raketmotor.",
        "<strong>In laboratoria en de industrie.</strong> Onder meer bij chemische analyses en als beschermgas.",
    ]) + """
<h2>Hoe werkt lachgas in het lichaam?</h2>
<p>Lachgas werkt in op het centrale zenuwstelsel. Het remt bepaalde receptoren in de hersenen en zorgt daardoor voor een kortdurend gevoel van roes, ontspanning en een verminderde pijnbeleving. Het effect begint binnen enkele seconden en houdt meestal maar een paar minuten aan. Omdat lachgas de opname van zuurstof kan verdringen, ontstaat bij inademen zonder zuurstof snel een tekort aan zuurstof in het bloed. Dat verklaart de duizeligheid, het flauwvallen en het risico op letsel.</p>
<p>Bij regelmatig of veelvuldig gebruik blokkeert lachgas vitamine B12 in het lichaam. Een tekort aan B12 kan leiden tot tintelingen, gevoelloosheid en blijvende zenuwschade. Lees hierover meer in ons artikel over <a href="/lachgas-informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a>.</p>
<h2>Lachgas en het milieu</h2>
<p>Distikstofmonoxide is een sterk broeikasgas. Over een periode van honderd jaar werkt het ongeveer 270 keer sterker dan koolstofdioxide, en het draagt bovendien bij aan de afbraak van de ozonlaag. De grootste bronnen zijn de landbouw (kunstmest en mest) en de industrie. Ga zorgvuldig om met lachgas en laat het niet onnodig ontsnappen uit een tank.</p>
<h2>Lachgas en de wet</h2>
<p>Lachgas valt in Nederland onder wet- en regelgeving die de afgelopen jaren is aangescherpt. Lees ons overzicht van de <a href="/lachgas-informatie/regels-en-wetgeving/">regels en wetgeving rond lachgas in Nederland</a>. LachGasAdam247 levert uitsluitend aan volwassenen (18+) en alleen in lijn met de geldende wet.</p>
""",
    faq=[
        ("Is lachgas hetzelfde als het gas in slagroompatronen?",
         "Ja. Slagroompatronen bevatten distikstofmonoxide (N2O), aangeduid als E942. Lachgas tanks bevatten hetzelfde gas, maar in een veel grotere hoeveelheid onder druk."),
        ("Waarom heet het lachgas?",
         "Humphry Davy gaf het gas rond 1799 de naam laughing gas, omdat proefpersonen die het inademden gingen lachen en euforisch werden. De Nederlandse naam lachgas is daar een vertaling van."),
        ("Is lachgas verslavend?",
         "Lachgas is niet lichamelijk verslavend zoals nicotine of alcohol, maar er kan wel gewenning en psychische afhankelijkheid ontstaan bij veelvuldig gebruik. Regelmatig gebruik brengt bovendien gezondheidsrisico's met zich mee, zoals een vitamine B12-tekort."),
    ],
)

ARTICLES["veilig-gebruik"] = dict(
    title="Veilig en verantwoord omgaan met lachgas | Tips en risico's",
    description="Veilig omgaan met lachgas: de basisregels over inademen, zitten, ventilatie, alcohol en verkeer, de risico's en wanneer je hulp zoekt. Uitsluitend 18+.",
    h1="Veilig en verantwoord omgaan met lachgas",
    lead="Lachgas is bij correct en verantwoord gebruik geen onschuldig gas. Direct inademen uit een tank kan letsel veroorzaken, in een afgesloten ruimte kan zuurstoftekort ontstaan en veelvuldig gebruik kan leiden tot zenuwschade. Op deze pagina zetten we de basisregels op een rij, zodat je weet waar je op moet letten. Lachgas is uitsluitend bestemd voor volwassenen (18+).",
    body="""
<h2>De basisregels</h2>
""" + checks([
        "<strong>Adem nooit rechtstreeks uit een tank of cilinder.</strong> Het gas komt onder hoge druk en extreem koud vrij en kan bevriezingsletsel aan lippen, keel en longen veroorzaken.",
        "<strong>Niet voor het verkeer.</strong> Gebruik lachgas niet als je daarna nog gaat autorijden, scooter rijden of fietsen, en niet voordat je machines bedient. Het beïnvloedt je reactievermogen en evenwicht. Lees meer over <a href=\"/lachgas-informatie/lachgas-en-verkeer/\">lachgas en het verkeer</a>.",
        "<strong>Ga zitten.</strong> Je kunt duizelig worden of flauwvallen. Een val van een stoel of een trap veroorzaakt onnodig letsel.",
        "<strong>Zorg voor frisse lucht.</strong> Gebruik het alleen in een goed geventileerde ruimte. In een kleine, afgesloten ruimte kan het gas zuurstof verdringen.",
        "<strong>Niet combineren.</strong> Meng lachgas niet met alcohol, medicijnen of andere drugs. De effecten versterken elkaar en het risico op flauwvallen en ongelukken neemt sterk toe.",
        "<strong>Niet vaak en niet veel.</strong> Veelvuldig gebruik kan leiden tot een vitamine B12-tekort met tintelingen, gevoelloosheid of zenuwschade. Neem lange pauzes en houd het bij een enkele keer.",
        "<strong>Nooit met een masker, zak of afgesloten hulpmiddel.</strong> Alles wat de toevoer van zuurstof afsluit, is levensgevaarlijk.",
        "<strong>Bewaar tanks veilig.</strong> Rechtop, goed vastgezet, koel en droog, en buiten bereik van kinderen. Lees onze tips over <a href=\"/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/\">bewaren en vervoeren</a>.",
    ]) + """
<h2>Wat zijn de risico's van lachgas?</h2>
<p>De belangrijkste risico's op korte termijn zijn duizeligheid, misselijkheid, hoofdpijn, flauwvallen en letsel door vallen. Bij direct contact met het gas uit een tank ontstaat bevriezing van huid en slijmvliezen. In een afgesloten ruimte kan zuurstoftekort optreden, met in het ergste geval bewusteloosheid en hersenschade. Wie lachgas combineert met alcohol of andere middelen, loopt een sterk verhoogd risico.</p>
<p>Op langere termijn is het grootste risico een tekort aan vitamine B12. Lachgas maakt B12 in het lichaam onwerkzaam, wat bij regelmatig gebruik leidt tot tintelingen en gevoelloosheid in handen en voeten, spierzwakte, problemen met lopen en in ernstige gevallen blijvende schade aan het ruggenmerg. Ook bloedarmoede, concentratieproblemen en stemmingsklachten komen voor. Herstel is niet altijd volledig.</p>
<h2>Wanneer moet je hulp zoeken?</h2>
""" + checks([
        "<strong>Bel 112</strong> bij bewusteloosheid, ademhalingsproblemen, een epileptische aanval of ernstig letsel na een val.",
        "<strong>Ga naar de huisarts</strong> bij tintelingen, gevoelloosheid, krachtverlies, problemen met lopen of aanhoudende vermoeidheid. Vertel dat je lachgas hebt gebruikt; dat maakt de diagnose sneller.",
        "<strong>Neem contact op met de huisartsenpost</strong> als klachten buiten kantooruren ontstaan en niet vanzelf overgaan.",
    ]) + """
<div class="callout"><p><strong>Onafhankelijke informatie en hulp.</strong> Betrouwbare informatie over lachgas vind je bij <a href="https://www.drugsinfo.nl" target="_blank" rel="noopener nofollow">Drugsinfo van het Trimbos-instituut</a>. Maak je je zorgen over je eigen gebruik of dat van een ander? Bel de Drugs Infolijn of bespreek het met je huisarts.</p></div>
<h2>Onze verantwoordelijkheid</h2>
<p>LachGasAdam247 levert uitsluitend aan volwassenen (18+) en alleen in lijn met de geldende wet- en regelgeving. Wij plaatsen geen instructies voor misbruik op onze website en verwachten van klanten dat zij verantwoord met de producten omgaan. Twijfel je of iets veilig is? Doe het dan niet.</p>
""",
    faq=[
        ("Is lachgas veilig?",
         "Lachgas is bij correct gebruik geen onschuldig gas. Direct inademen uit een tank kan letsel veroorzaken, in een afgesloten ruimte kan zuurstoftekort ontstaan en veelvuldig gebruik kan leiden tot een vitamine B12-tekort en zenuwschade. Houd je aan de basisregels en gebruik het nooit voordat je gaat rijden."),
        ("Mag ik lachgas combineren met alcohol?",
         "Nee. De combinatie van lachgas met alcohol of andere drugs verhoogt het risico op flauwvallen, misselijkheid en ongelukken aanzienlijk."),
        ("Wat doe ik als iemand flauwvalt na lachgas?",
         "Leg de persoon op de zij, zorg voor frisse lucht en blijf erbij. Komt hij of zij niet binnen een minuut bij, ademt de persoon niet normaal of ontstaat een aanval? Bel direct 112."),
    ],
)

ARTICLES["lachgas-en-verkeer"] = dict(
    title="Lachgas in het verkeer: regels, risico's en straffen",
    description="Lachgas en verkeer gaan niet samen. Wat lachgas met je rijvaardigheid doet, welke regels gelden bij rijden onder invloed en welke straffen erop staan.",
    h1="Lachgas in het verkeer",
    lead="Lachgas beïnvloedt je reactievermogen, je evenwicht en je waarneming. Autorijden, scooter rijden of fietsen na het gebruik van lachgas is daarom gevaarlijk en strafbaar. Op deze pagina lees je wat lachgas met je rijvaardigheid doet, welke regels gelden en wat de gevolgen kunnen zijn.",
    body="""
<h2>Wat doet lachgas met je rijvaardigheid?</h2>
<p>Lachgas geeft binnen seconden een roes: je wordt licht in je hoofd, je waarneming vervormt, je reactietijd wordt langer en je evenwicht is verstoord. Het effect duurt meestal maar een paar minuten, maar in die minuten ben je niet in staat om veilig aan het verkeer deel te nemen. Ook na de roes kunnen duizeligheid, misselijkheid en concentratieproblemen nog een tijd aanhouden.</p>
<p>Wie lachgas gebruikt tijdens het rijden, bijvoorbeeld achter het stuur, loopt een extreem risico: een korte black-out of flauwte bij vijftig kilometer per uur is genoeg voor een ernstig ongeluk. De afgelopen jaren zijn in Nederland meerdere dodelijke ongevallen gebeurd waarbij lachgas in het spel was.</p>
<h2>Welke regels gelden?</h2>
<p>De Wegenverkeerswet verbiedt het besturen van een voertuig onder invloed van een stof waarvan je weet of redelijkerwijs moet weten dat die je rijvaardigheid vermindert. Lachgas valt daar onder. Dat geldt niet alleen voor auto's en motoren, maar ook voor scooters, brommers en fietsen. Sinds lachgas in 2023 onder de Opiumwet is gebracht, is bovendien het bezit ervan in de auto in de meeste situaties op zichzelf al een overtreding.</p>
<p>Bij een controle kan de politie je staande houden op basis van je rijgedrag en uiterlijke kenmerken. Een ballon of tank in de auto is voor de politie aanleiding voor nader onderzoek. Rijden onder invloed van lachgas kan leiden tot een boete, een rijverbod, invordering van je rijbewijs en, bij een ongeluk met letsel, vervolging voor een misdrijf.</p>
<h2>Wat betekent dit in de praktijk?</h2>
""" + checks([
        "<strong>Gebruik nooit lachgas als je daarna nog moet rijden of fietsen.</strong> Regel vooraf hoe je thuiskomt: te voet, met het openbaar vervoer of met een nuchtere chauffeur.",
        "<strong>Ook op de fiets.</strong> Fietsen onder invloed is in Amsterdam een veelvoorkomende oorzaak van ongelukken. Duizeligheid op een drukke gracht of een trambaan is levensgevaarlijk.",
        "<strong>Vervoer een tank alleen nuchter en veilig.</strong> Rechtop, vastgezet en in de kofferbak, niet losliggend op de achterbank. Lees onze tips voor <a href=\"/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/\">bewaren en vervoeren</a>.",
        "<strong>Laat het bezorgen.</strong> Juist omdat je een tank niet zelf wilt ophalen na een avond uit, bezorgen wij aan huis. Zo hoeft niemand de weg op.",
    ]) + """
<h2>Waarom wij hier aandacht aan besteden</h2>
<p>Als bezorgservice vinden wij het belangrijk dat onze klanten veilig thuisblijven. Wij bezorgen 24/7 aan huis in heel Amsterdam, zodat je nooit in de verleiding komt om zelf de weg op te gaan. Gebruik lachgas uitsluitend thuis of op een plek waar je kunt blijven, ga zitten en zorg dat je niet meer hoeft te rijden. Meer tips lees je op de pagina over <a href="/lachgas-informatie/veilig-gebruik/">veilig en verantwoord gebruik</a>.</p>
""",
    faq=[
        ("Is rijden na lachgas strafbaar?",
         "Ja. Op grond van de Wegenverkeerswet is het verboden een voertuig te besturen onder invloed van een stof die je rijvaardigheid vermindert. Lachgas valt daar onder. Dat geldt voor auto's, motoren, scooters en fietsen."),
        ("Hoe lang na lachgas mag ik weer rijden?",
         "De roes duurt enkele minuten, maar duizeligheid en concentratieproblemen kunnen langer aanhouden. Wie lachgas heeft gebruikt, kan die avond beter helemaal niet meer rijden. Regel vooraf een alternatief."),
        ("Mag ik een lachgas tank in de auto vervoeren?",
         "Sinds lachgas onder de Opiumwet valt, gelden strikte regels voor bezit en vervoer. Vervoer een tank in ieder geval altijd nuchter, rechtop en vastgezet in de kofferbak, nooit in een warme auto. Bij twijfel over de regels raadpleeg je rijksoverheid.nl."),
    ],
)

ARTICLES["regels-en-wetgeving"] = dict(
    title="Regels en wetgeving rond lachgas in Nederland (2026)",
    description="Welke regels gelden voor lachgas in Nederland? Sinds 2023 staat lachgas op lijst II van de Opiumwet. Wat dat betekent, de uitzonderingen en het verkeer.",
    h1="Regels en wetgeving rond lachgas in Nederland",
    lead="De regels rond lachgas zijn de afgelopen jaren flink aangescherpt. Sinds 1 januari 2023 staat distikstofmonoxide op lijst II van de Opiumwet, en daarnaast gelden regels in het verkeer en lokale regels van gemeenten. Op deze pagina zetten we de hoofdlijnen op een rij. De regels kunnen wijzigen; raadpleeg voor de actuele stand altijd rijksoverheid.nl.",
    body="""
<h2>Lachgas en de Opiumwet</h2>
<p>Op 1 januari 2023 heeft de Rijksoverheid lachgas op lijst II van de Opiumwet geplaatst. Daarmee is het verboden om lachgas te produceren, te verhandelen, in bezit te hebben of in of uit te voeren voor recreatief gebruik. Voor het plaatsen op lijst II koos de overheid vanwege de gezondheidsrisico's, de overlast in wijken en het aantal verkeersongevallen waarbij lachgas een rol speelde.</p>
<p>De wet maakt uitzonderingen voor legitieme toepassingen. Lachgas mag nog steeds worden gebruikt voor <strong>medische doeleinden</strong> (bijvoorbeeld bij tandartsen en in ziekenhuizen), voor <strong>technische doeleinden</strong> (zoals in de industrie en de autosport) en in de <strong>voedingsindustrie</strong> (bijvoorbeeld slagroompatronen als drijfgas). Voor die toepassingen gelden aparte regels en voorwaarden.</p>
<h2>Lachgas in het verkeer</h2>
<p>Los van de Opiumwet verbiedt de Wegenverkeerswet het besturen van een voertuig onder invloed van een stof die de rijvaardigheid vermindert. Lachgas valt daar onder, ook op de fiets of de scooter. Lees ons artikel over <a href="/lachgas-informatie/lachgas-en-verkeer/">lachgas in het verkeer</a> voor de details.</p>
<h2>Lokale regels in Amsterdam</h2>
<p>Voordat het landelijke verbod inging, hadden veel gemeenten, waaronder Amsterdam, al een verbod op het gebruik van lachgas in de openbare ruimte in hun Algemene Plaatselijke Verordening (APV). In bepaalde gebieden en bij evenementen gold een lachgasverbod op straat. De handhaving in de openbare ruimte ligt bij de politie en de handhavers van de gemeente. Op straat, in parken en bij evenementen is het gebruik van lachgas in Amsterdam niet toegestaan.</p>
<h2>Wat betekent dit voor jou?</h2>
""" + checks([
        "<strong>Informeer jezelf.</strong> De regels kunnen wijzigen. Raadpleeg de actuele informatie op <a href=\"https://www.rijksoverheid.nl\" target=\"_blank\" rel=\"noopener nofollow\">rijksoverheid.nl</a> en de website van de gemeente Amsterdam.",
        "<strong>Je bent zelf verantwoordelijk</strong> voor het gebruik van producten die je bestelt en voor het naleven van de wet.",
        "<strong>Nooit in het verkeer.</strong> Rijden of fietsen onder invloed van lachgas is strafbaar en gevaarlijk.",
        "<strong>Niet op straat of in de openbare ruimte.</strong> Gebruik in parken, op pleinen en bij evenementen is in Amsterdam niet toegestaan.",
        "<strong>Uitsluitend 18+.</strong> Lachgas is nooit bestemd voor minderjarigen.",
    ]) + """
<h2>Hoe LachGasAdam247 hiermee omgaat</h2>
<p>LachGasAdam247 levert uitsluitend aan volwassenen (18+) en alleen in lijn met de geldende wet en onze beoordeling van de order. Wij behouden ons het recht voor een bestelling te weigeren. Op onze website staan geen instructies voor misbruik, en we verwijzen actief naar informatie over <a href="/lachgas-informatie/veilig-gebruik/">veilig en verantwoord gebruik</a>. Heb je vragen over de regels, dan verwijzen we je naar de officiële bronnen van de Rijksoverheid.</p>
<p class="meta">Deze pagina is een algemene, informatieve samenvatting en geen juridisch advies. Laatst bijgewerkt: september 2026.</p>
""",
    faq=[
        ("Is lachgas verboden in Nederland?",
         "Sinds 1 januari 2023 staat lachgas op lijst II van de Opiumwet. Productie, handel, bezit en in- en uitvoer voor recreatief gebruik zijn daarmee verboden. Er gelden uitzonderingen voor medische, technische en voedingsdoeleinden."),
        ("Mag ik lachgas gebruiken op straat in Amsterdam?",
         "Nee. Het gebruik van lachgas in de openbare ruimte is in Amsterdam niet toegestaan en kan leiden tot een boete. Bovendien geldt het landelijke verbod van de Opiumwet."),
        ("Waar vind ik de actuele regels?",
         "Op rijksoverheid.nl vind je de actuele informatie over lachgas en de Opiumwet. Voor lokale regels kijk je op de website van de gemeente Amsterdam."),
    ],
)

ARTICLES["lachgas-tank-bewaren-en-vervoeren"] = dict(
    title="Lachgas tank veilig bewaren en vervoeren | Praktische tips",
    description="Hoe bewaar en vervoer je een lachgas tank veilig? Tips over rechtop zetten, temperatuur, ventilatie, kinderen, vervoer in de auto en lege tanks.",
    h1="Een lachgas tank veilig bewaren en vervoeren",
    lead="Een lachgas tank is een stalen drukcilinder met vloeibaar N<sub>2</sub>O onder hoge druk. Zolang je er zorgvuldig mee omgaat, is bewaren en vervoeren veilig. Op deze pagina lees je waar je op moet letten: van de plek in huis tot het vervoer in de auto en het omgaan met een lege tank.",
    body="""
<h2>Bewaren in huis</h2>
""" + checks([
        "<strong>Rechtop en vastgezet.</strong> Zet de tank altijd rechtop op een stevige, vlakke ondergrond en zorg dat hij niet kan omvallen, bijvoorbeeld in een hoek of tegen een muur.",
        "<strong>Koel en droog.</strong> Bewaar de tank bij kamertemperatuur of koeler, uit direct zonlicht en niet naast een verwarming, oven, kachel of open vuur. Bij hoge temperaturen loopt de druk in de tank op.",
        "<strong>Geventileerd.</strong> Kies een ruimte met voldoende ventilatie. Mocht er ooit gas ontsnappen, dan kan het zich niet ophopen.",
        "<strong>Buiten bereik van kinderen en huisdieren.</strong> Een tank is geen speelgoed. Bewaar hem op een plek waar kinderen niet bij kunnen.",
        "<strong>Kraan dicht.</strong> Draai de kraan na gebruik altijd goed dicht en controleer of je geen sissend geluid hoort.",
        "<strong>Niet in de badkamer of kelder.</strong> Vocht veroorzaakt roest op de cilinder en de kraan; een vochtige kelder zonder ventilatie is ongeschikt.",
    ]) + """
<h2>Vervoeren in de auto</h2>
<p>Vervoer je een tank zelf, doe dat dan altijd nuchter. Zet de tank rechtop in de kofferbak en zet hem vast, bijvoorbeeld met een spanband of tussen stevige spullen, zodat hij bij remmen niet kan omvallen of gaan rollen. Laat een tank nooit achter in een geparkeerde auto in de zon: de temperatuur in een auto kan in de zomer boven de zestig graden komen en de druk in de tank loopt dan snel op. Houd bij het vervoer rekening met de regels van de Opiumwet; lees ons artikel over <a href="/lachgas-informatie/regels-en-wetgeving/">regels en wetgeving</a>.</p>
<p>Wil je liever niet zelf rijden? Wij bezorgen aan huis in heel Amsterdam en de regio, doorgaans binnen 20 tot 30 minuten. Zo hoef je zelf niet met een tank de weg op.</p>
<h2>Bevriezing en temperatuur</h2>
<p>Bij het openen van de kraan komt het gas onder hoge druk en extreem koud vrij. Raak de kraan en de uitstroomopening niet met blote handen aan tijdens het gebruik en adem nooit rechtstreeks uit de tank. Het gas kan huid en slijmvliezen bevriezen. Voelt de tank tijdens het gebruik ijskoud aan en zit er rijp op? Dat is normaal; laat de tank een tijdje met rust.</p>
<h2>Lege tanks</h2>
<p>Een lege tank is een drukcilinder en hoort niet bij het huisvuil. Gooi hem niet in de afvalcontainer en probeer hem niet open te maken of te doorboren. Vraag ons bij je bestelling wat je met een lege tank kunt doen; wij maken daar afspraken over in het gesprek. Ook de milieustraat van de gemeente Amsterdam neemt drukcilinders in als klein gevaarlijk afval.</p>
<h2>Wat je niet moet doen</h2>
""" + checks([
        "Nooit verhitten, ook niet in warm water, om de druk te verhogen.",
        "Nooit laten vallen, stoten of gebruiken als steun of opstapje.",
        "Nooit knutselen aan de kraan of het ventiel.",
        "Nooit bewaren naast brandbare stoffen, gasflessen of open vuur.",
        "Nooit in een afgesloten kast zonder ventilatie in een slaapkamer.",
    ]) + """
<p>Lees ook onze pagina over <a href="/lachgas-informatie/veilig-gebruik/">veilig en verantwoord gebruik</a> en bekijk de <a href="/lachgas-tanks/">maten en hoeveelheden van onze lachgas tanks</a>.</p>
""",
    faq=[
        ("Hoe lang kan ik een lachgas tank bewaren?",
         "Een goed afgesloten tank die rechtop, koel en droog staat, blijft lang bruikbaar. Controleer regelmatig of de kraan dicht is en of er geen roest op de cilinder of het ventiel zit."),
        ("Mag een lachgas tank in de zon staan?",
         "Nee. Direct zonlicht en warmte laten de druk in de tank oplopen. Bewaar de tank in de schaduw, bij kamertemperatuur of koeler, en nooit in een warme auto."),
        ("Wat doe ik met een lege tank?",
         "Vraag ons bij je bestelling naar de mogelijkheden; wij maken daar afspraken over. Gooi een lege tank nooit bij het huisvuil. De milieustraat neemt drukcilinders in als klein gevaarlijk afval."),
    ],
)

ARTICLES["lachgas-en-vitamine-b12"] = dict(
    title="Lachgas en vitamine B12: risico's, klachten en herstel",
    description="Waarom veroorzaakt lachgas een vitamine B12-tekort? Hoe lachgas B12 blokkeert, welke klachten dat geeft en wanneer je naar de huisarts moet.",
    h1="Lachgas en vitamine B12",
    lead="Het belangrijkste gezondheidsrisico van regelmatig lachgasgebruik is een tekort aan vitamine B12. Lachgas maakt B12 in het lichaam onwerkzaam, en dat kan leiden tot tintelingen, gevoelloosheid, spierzwakte en blijvende zenuwschade. Op deze pagina lees je hoe dat werkt, welke klachten je kunt herkennen en wanneer je hulp moet zoeken.",
    body="""
<h2>Hoe blokkeert lachgas vitamine B12?</h2>
<p>Vitamine B12 (cobalamine) is nodig voor de aanmaak van rode bloedcellen en voor het onderhoud van de beschermlaag rond zenuwen, de myeline. Lachgas oxideert het kobaltatoom in vitamine B12, waardoor de vitamine niet meer werkt. Het lichaam heeft dan wel B12 in voorraad, maar kan het niet gebruiken. Bij een enkele keer gebruik herstelt dat vanzelf. Bij regelmatig of veelvuldig gebruik raakt de werkzame voorraad uitgeput en ontstaan klachten.</p>
<h2>Welke klachten horen bij een B12-tekort?</h2>
""" + checks([
        "<strong>Tintelingen en gevoelloosheid</strong> in handen, voeten, armen of benen, vaak beginnend in de vingertoppen en tenen.",
        "<strong>Spierzwakte en problemen met lopen</strong>, een onzeker of wankel gevoel, of het gevoel op watten te lopen.",
        "<strong>Vermoeidheid en bloedarmoede</strong>, kortademigheid bij inspanning en een bleke huid.",
        "<strong>Concentratieproblemen, vergeetachtigheid en stemmingsklachten</strong> zoals somberheid of prikkelbaarheid.",
        "<strong>In ernstige gevallen: schade aan het ruggenmerg</strong> (gecombineerde strengziekte), met verlamming en blijvend krachtverlies.",
    ]) + """
<h2>Wie loopt extra risico?</h2>
<p>Het risico neemt toe met de hoeveelheid en de frequentie van het gebruik. Wie wekelijks of vaker lachgas gebruikt, of grote hoeveelheden op één avond, loopt duidelijk meer risico. Mensen die al een lage B12-spiegel hebben, bijvoorbeeld vegetariërs en veganisten, mensen met maag- of darmproblemen en zwangere vrouwen, zijn extra kwetsbaar. Ook wie medicijnen gebruikt die de opname van B12 verminderen, zoals maagzuurremmers of metformine, moet extra voorzichtig zijn.</p>
<h2>Is de schade te herstellen?</h2>
<p>Bij vroege klachten en direct stoppen met lachgas herstelt het lichaam zich vaak goed, soms met hulp van B12-injecties of tabletten via de huisarts. Bij langdurige klachten of schade aan het ruggenmerg is het herstel niet altijd volledig; sommige mensen houden blijvend tintelingen, gevoelloosheid of krachtverlies. Daarom is het belangrijk om klachten serieus te nemen en niet te wachten.</p>
<div class="callout"><p><strong>Heb je tintelingen, gevoelloosheid of krachtverlies?</strong> Stop met lachgas en ga naar je huisarts. Vertel dat je lachgas hebt gebruikt; dat maakt de diagnose sneller. Bij acute klachten, zoals uitval of niet meer kunnen lopen, bel je 112.</p></div>
<h2>Hoe verklein je het risico?</h2>
""" + checks([
        "Gebruik lachgas niet vaak en niet veel. Houd het bij een enkele keer en neem lange pauzes.",
        "Combineer het niet met alcohol of andere drugs.",
        "Ken je eigen risicofactoren: een vegetarisch of veganistisch dieet, maag- of darmproblemen, zwangerschap en bepaalde medicijnen.",
        "Neem bij klachten direct contact op met je huisarts; hoe eerder, hoe beter de kans op herstel.",
    ]) + """
<p>Meer over veilig gebruik lees je op de pagina <a href="/lachgas-informatie/veilig-gebruik/">veilig en verantwoord omgaan met lachgas</a>. Onafhankelijke informatie vind je bij <a href="https://www.drugsinfo.nl" target="_blank" rel="noopener nofollow">Drugsinfo van het Trimbos-instituut</a>.</p>
<p class="meta">Deze pagina is algemene gezondheidsinformatie en vervangt geen medisch advies. Neem bij klachten altijd contact op met je huisarts.</p>
""",
    faq=[
        ("Helpt het om vitamine B12-tabletten te slikken als ik lachgas gebruik?",
         "Extra B12 slikken neemt het risico niet weg. Lachgas maakt de B12 in je lichaam onwerkzaam, ongeacht hoeveel je binnenkrijgt. De enige manier om het risico te verkleinen is minder en minder vaak gebruiken."),
        ("Hoe snel ontstaat een B12-tekort door lachgas?",
         "Dat verschilt per persoon. Bij intensief gebruik kunnen klachten binnen weken ontstaan; bij mensen met een lage B12-spiegel soms nog sneller. Bij een enkele keer gebruik herstelt het lichaam zich meestal vanzelf."),
        ("Zijn tintelingen door lachgas blijvend?",
         "Bij vroeg stoppen en behandeling herstellen veel mensen goed. Bij langdurig gebruik en schade aan het ruggenmerg kan het herstel onvolledig zijn. Ga daarom bij de eerste klachten naar de huisarts."),
    ],
)

ORDER = ["wat-is-lachgas", "veilig-gebruik", "lachgas-en-verkeer", "regels-en-wetgeving",
         "lachgas-tank-bewaren-en-vervoeren", "lachgas-en-vitamine-b12"]


def article_page(slug):
    a = ARTICLES[slug]
    path = "/lachgas-informatie/%s/" % slug
    page = dict(
        path=path,
        title=a["title"],
        description=a["description"],
        h1=a["h1"],
        lead=a["lead"],
        crumbs=[("Home", "/"), ("Lachgas informatie", "/lachgas-informatie/"), (a["h1"], None)],
        faq=a["faq"],
        og_type="article",
        priority="0.6", changefreq="monthly",
        speakable=["#h1", ".lead"],
    )
    page["schema"] = [{
        "@type": "Article",
        "@id": SITE + path + "#article",
        "headline": a["h1"],
        "description": a["description"],
        "url": SITE + path,
        "mainEntityOfPage": {"@id": SITE + path + "#webpage"},
        "image": OG_IMAGE,
        "inLanguage": "nl-NL",
        "datePublished": TODAY,
        "dateModified": TODAY,
        "author": {"@id": BUSINESS_ID},
        "publisher": {"@id": BUSINESS_ID},
        "about": {"@type": "Thing", "name": "Lachgas (distikstofmonoxide, N2O)"},
    }]
    others = [("/lachgas-informatie/%s/" % s, ARTICLES[s]["h1"]) for s in ORDER if s != slug]
    body = [
        doc_page(page, a["body"] +
                 '<h2>Meer lezen over lachgas</h2><p>Bekijk het <a href="/lachgas-informatie/">overzicht van alle informatiepagina&rsquo;s</a> of lees verder:</p>' + toc(others)),
        faq_html(a["faq"], "Veelgestelde vragen"),
        cta_block(),
    ]
    page["body"] = "".join(body)
    return page


def hub_page():
    path = "/lachgas-informatie/"
    page = dict(
        path=path,
        title="Lachgas informatie: feiten, veilig gebruik en regels",
        description="Alles over lachgas: wat het is, veilig gebruik, de regels in Nederland, lachgas in het verkeer, tanks bewaren en het risico op een vitamine B12-tekort.",
        h1="Lachgas informatie",
        lead="Eerlijke, praktische informatie over lachgas: wat het is, hoe je er verantwoord mee omgaat, welke regels gelden in Nederland en welke risico&rsquo;s je moet kennen. Lachgas is uitsluitend bestemd voor volwassenen (18+).",
        crumbs=[("Home", "/"), ("Lachgas informatie", None)],
        priority="0.7", changefreq="monthly",
        speakable=["#h1", ".lead"],
    )
    page["schema"] = [{
        "@type": "ItemList",
        "@id": SITE + path + "#artikelen",
        "name": "Lachgas informatie",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": ARTICLES[s]["h1"], "url": SITE + "/lachgas-informatie/%s/" % s}
            for i, s in enumerate(ORDER)
        ],
    }]
    cards = ('<div class="cards">' + "".join(
        '<div class="card"><h3><a href="/lachgas-informatie/%s/">%s</a></h3><p>%s</p><p class="more"><a href="/lachgas-informatie/%s/">Lees verder &rarr;</a></p></div>'
        % (s, esc(ARTICLES[s]["h1"]), ARTICLES[s]["description"].split(". ")[0].rstrip("?") + ".", s) for s in ORDER) + "</div>")
    body = [
        '<section class="hero" id="top" aria-labelledby="h1"><div class="wrap">%s<div class="hero-in"><p class="eyebrow">Informatie · 18+</p><h1 id="h1">%s</h1><p class="lead">%s</p></div></div></section>'
        % (crumbs_html(page["crumbs"]), esc(page["h1"]), page["lead"]),
        '<section class="section" aria-labelledby="h-art"><div class="wrap"><h2 id="h-art">Artikelen</h2>%s</div></section>' % cards,
        '<section class="section alt" aria-labelledby="h-nood"><div class="wrap prose"><h2 id="h-nood">Hulp en betrouwbare bronnen</h2>'
        '<p>Bij acute klachten of een noodgeval bel je direct 112. Bij tintelingen, gevoelloosheid of andere klachten na lachgasgebruik ga je naar je huisarts. Onafhankelijke informatie vind je bij <a href="https://www.drugsinfo.nl" target="_blank" rel="noopener nofollow">Drugsinfo van het Trimbos-instituut</a>; de actuele regels vind je op <a href="https://www.rijksoverheid.nl" target="_blank" rel="noopener nofollow">rijksoverheid.nl</a>.</p></div></section>',
        cta_block(),
    ]
    page["body"] = "".join(body)
    return page


def pages():
    return [hub_page()] + [article_page(s) for s in ORDER]
