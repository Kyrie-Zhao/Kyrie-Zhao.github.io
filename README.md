# Zhihe (Bob) Zhao — Personal homepage

A small, accessible static site for <https://bob-zhihe.github.io/>. GitHub Pages serves the checked-in HTML directly. Visitors need no JavaScript. The writing collection is generated locally from Markdown; no external fonts, analytics, or third-party scripts are used.

## Edit and preview

- `index.html`: biography, current work, previously built products, publications, background, recognition, selected coverage, and contact.
- `assets/site.css`: responsive layout, typography, and print styles.
- `assets/images/bob-homepage.jpg`: author-selected portrait.
- `docs/content-sources.md`: public sources and editorial decisions.
- `sitemap.xml`: canonical homepage, writing directory, and article URLs.

Run `python3 -m http.server 6088 --bind 127.0.0.1` from this directory and visit `http://127.0.0.1:6088/`. Root-relative paths require an HTTP preview, not opening `index.html` directly from the filesystem.

The `.nojekyll` marker tells GitHub Pages to serve the checked-in files directly. The inherited `index.md` template was removed because it would otherwise compete with `index.html` for the homepage. The old site's PDFs, publication directories, and supporting assets are preserved so existing links keep working. Legacy files are not the source of the new homepage.

## Maintenance

Keep career claims dated and linked to evidence. Distinguish ongoing research from published results; distinguish papers, posters, and workshop publications. The October 2023 CV is explicitly an archive. When adding a current CV, publish a separately dated file and update its label.

For coverage, distinguish founder profiles, official company features, product news, and later reporting after departure. Keep Nuna/PieX and Collie R1 under the previous ThingX chapter. Company funding and team products must not become claims of sole personal achievement. Source dates and limits are recorded in `docs/content-sources.md`.

Before deployment, check desktop and mobile layouts, keyboard navigation, internal anchors, local assets, structured metadata, and publication links. Update `sitemap.xml` and the footer date only for substantive content changes.

`index.json`, `index.xml`, and `index.webmanifest` are maintained compatibility metadata for old search/feed/bookmark clients. Update their basic profile wording when the public identity changes; they no longer contain inherited template biographies.

## Writing collection

- Edit full English articles in `content/writing/*.md`.
- Edit titles, summaries, categories, dates, related articles, and order in `content/writing/catalog.json`.
- Install the local rendering dependency with `python3 -m pip install -r requirements-writing.txt`.
- Run `python3 scripts/build_writing.py`. Commit both sources and generated output.
- Generated output: `writing/`, the marked Writing section in `index.html`, `sitemap.xml`, `index.json`, and RSS feeds. Do not hand-edit generated article HTML.
- `assets/writing.css` extends the existing design for the directory, article typography, responsive tables, and navigation.
- The public collection contains complete English essays and technical notes, not internal whitepapers or patent disclosures. Synthetic examples and proposed methods must remain labeled. Do not convert design proposals into measured results when editing.

The root RSS endpoint now mirrors the writing feed so existing subscribers receive new articles. Historic publication assets remain unchanged.
