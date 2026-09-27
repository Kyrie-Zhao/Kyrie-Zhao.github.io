# Zhihe (Bob) Zhao — Personal homepage

A small, accessible bilingual static site for <https://bob-zhihe.github.io/>. English lives at `/`; Simplified Chinese lives at `/zh/`. GitHub Pages serves the checked-in HTML directly. Visitors need no JavaScript. The writing collection is generated locally from Markdown; no external fonts, analytics, or third-party scripts are used.

## Edit and preview

- `index.html`: biography, current work, previously built products, publications, background, recognition, selected coverage, and contact.
- `zh/index.html`: the complete Chinese homepage, maintained alongside the English page.
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
- Edit full Chinese translations in `content/writing/zh/*.md` and localized titles, summaries, and publication dates in `content/writing/zh/catalog.json`. Slugs pair the editions; category membership, related articles, and order come from the English catalog.
- Install the local rendering dependency with `python3 -m pip install -r requirements-writing.txt`.
- Run `python3 scripts/build_writing.py`. Commit both sources and generated output.
- Generated output: `writing/`, `zh/writing/`, marked article highlights and language links in both homepages, the bilingual `sitemap.xml`, locale-specific search indexes, and RSS feeds. Do not hand-edit generated article HTML.
- `assets/writing.css` extends the existing design for the directory, article typography, responsive tables, and navigation.
- The public collection contains complete English essays and technical notes, not internal whitepapers or patent disclosures. Synthetic examples and proposed methods must remain labeled. Do not convert design proposals into measured results when editing.

The root RSS endpoint now mirrors the writing feed so existing subscribers receive new articles. Historic publication assets remain unchanged.

## Language editions

The header's `EN / 中文` links switch to the same page or article in the other language. All ordinary Chinese navigation stays under `/zh/`. Keep each edition's own canonical URL and reciprocal `hreflang` links; English is the `x-default`. The language is chosen explicitly, with no automatic redirects, translation service, browser storage, or client-side state.

The build requires matching article slugs and nonempty source files in both languages. New articles need both editions before publication. Chinese reading estimates count Chinese characters as well as Latin words. Publication dates describe each edition's release; the Chinese launch is 28 September 2026. Update `UPDATED` in the build script when publishing substantive changes.

Translate arguments, examples, uncertainty, and source boundaries in full. Write natural Chinese rather than matching English word order. Keep original paper titles, product names, and source links where they identify external work. Do not turn proposals or hypothetical examples into measured results.
