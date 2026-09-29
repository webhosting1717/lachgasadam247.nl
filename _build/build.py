#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genereert alle HTML-pagina's, sitemap.xml en llms.txt voor lachgasadam247.nl.

Gebruik (vanuit de root van de repository):
    python3 _build/build.py

Alle teksten en instellingen staan in de content_*.py-bestanden en common.py.
Het telefoonnummer, e-mailadres en WhatsApp-nummer wijzig je op één plek in common.py.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import common  # noqa: E402
import content_home, content_areas, content_products, content_articles, content_pages  # noqa: E402


def write(path, data):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(data)


def main():
    pages = []
    for mod in (content_home, content_areas, content_products, content_articles, content_pages):
        pages += mod.pages()

    seen = set()
    for page in pages:
        assert page["path"] not in seen, "dubbel pad: " + page["path"]
        seen.add(page["path"])
        html = common.render(page)
        out = page["path"]
        if out.endswith("/"):
            out += "index.html"
        write(out, html)

    # sitemap.xml
    rows = []
    for page in pages:
        if page.get("sitemap", True) is False or "noindex" in page.get("robots", ""):
            continue
        rows.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>"
                    % (common.SITE, page["path"], page.get("modified", common.TODAY), page.get("changefreq", "monthly"),
                       page.get("priority", "0.5")))
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n")

    # llms.txt
    lines = [
        "# LachGasAdam247",
        "",
        "> Lachgas Amsterdam: LachGasAdam247 bezorgt lachgas tanks aan huis in heel Amsterdam en omstreken. "
        "Bestellen via WhatsApp of telefoon (%s), 24/7 bereikbaar, doorgaans bezorgd in 20 tot 30 minuten, "
        "prijs vooraf bevestigd. Uitsluitend voor volwassenen (18+)." % common.PHONE_DISPLAY,
        "",
        "## Belangrijkste pagina's",
        "- [Homepage: lachgas Amsterdam bestellen](%s/): bestellen, bezorgen, stadsdelen, regio, 24/7, prijs, veelgestelde vragen" % common.SITE,
        "- [Bezorggebied](%s/bezorggebied/): overzicht van alle stadsdelen en plaatsen in de regio" % common.SITE,
        "- [Lachgas tanks](%s/lachgas-tanks/): maten 2 kg, 4 kg en 10 kg" % common.SITE,
        "- [Zakelijk, feesten en evenementen](%s/zakelijk/)" % common.SITE,
        "- [Lachgas 24/7 en 's nachts](%s/lachgas-24-7-amsterdam/)" % common.SITE,
        "- [Lachgas informatie](%s/lachgas-informatie/): feiten, veilig gebruik, verkeer, regels, bewaren, vitamine B12" % common.SITE,
        "- [Over ons](%s/over-ons/)" % common.SITE,
        "- [Contact](%s/contact/)" % common.SITE,
        "- [Privacyverklaring](%s/privacy/)" % common.SITE,
        "- [Algemene voorwaarden](%s/algemene-voorwaarden/)" % common.SITE,
        "",
        "## Bezorggebieden in Amsterdam",
    ]
    for slug, name in common.STADSDELEN:
        lines.append("- [Lachgas %s](%s/bezorggebied/%s/)" % (name, common.SITE, slug))
    lines += ["", "## Regio rond Amsterdam"]
    for slug, name in common.REGIO:
        lines.append("- [Lachgas %s](%s/bezorggebied/%s/)" % (name, common.SITE, slug))
    lines += ["", "## Lachgas tanks"]
    for slug, name in common.TANKS:
        lines.append("- [%s](%s/lachgas-tanks/%s/)" % (name, common.SITE, slug))
    lines += ["", "## Informatie"]
    for slug in content_articles.ORDER:
        lines.append("- [%s](%s/lachgas-informatie/%s/)" % (content_articles.ARTICLES[slug]["h1"], common.SITE, slug))
    lines += ["", "## Contact", "- Telefoon en WhatsApp: %s" % common.PHONE_DISPLAY, "- E-mail: %s" % common.EMAIL,
              "- Bereikbaar: 24/7", ""]
    write("/llms.txt", "\n".join(lines))

    print("%d pagina's gegenereerd" % len(pages))


if __name__ == "__main__":
    main()
