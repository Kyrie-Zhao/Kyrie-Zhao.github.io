# Zhihe (Bob) Zhao — Personal homepage

A small, accessible static site for <https://bob-zhihe.github.io/>. No build step, package installation, JavaScript runtime, external fonts, analytics, or third-party scripts are required.

## Edit and preview

- `index.html`: biography, current work, publications, background, and contact.
- `assets/site.css`: responsive layout, typography, and print styles.
- `assets/images/zhihe-zhao.jpg`: portrait from the public CUHK profile.
- `docs/content-sources.md`: public sources and editorial decisions.
- `sitemap.xml`: canonical homepage and its last substantive update.

Run `python3 -m http.server 6088 --bind 127.0.0.1` from this directory and visit `http://127.0.0.1:6088/`. Root-relative paths require an HTTP preview, not opening `index.html` directly from the filesystem.

The `.nojekyll` marker tells GitHub Pages to serve the checked-in files directly. The inherited `index.md` template was removed because it would otherwise compete with `index.html` for the homepage. The old site's PDFs, publication directories, and supporting assets are preserved so existing links keep working. Legacy files are not the source of the new homepage.

## Maintenance

Keep career claims dated and linked to evidence. Distinguish ongoing research from published results; distinguish papers, posters, and workshop publications. The October 2023 CV is explicitly an archive. When adding a current CV, publish a separately dated file and update its label.

Before deployment, check desktop and mobile layouts, keyboard navigation, internal anchors, local assets, structured metadata, and publication links. Update `sitemap.xml` and the footer date only for substantive content changes.

`index.json`, `index.xml`, and `index.webmanifest` are maintained compatibility metadata for old search/feed/bookmark clients. Update their basic profile wording when the public identity changes; they no longer contain inherited template biographies.
