#!/usr/bin/env python3
"""Render the English writing collection. GitHub Pages serves committed HTML."""
import html
import json
import math
import re
from pathlib import Path
from xml.etree import ElementTree as ET
import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'content/writing'
BASE = 'https://bob-zhihe.github.io'
CATEGORIES = {
    'Technical Notes': ('technical-notes', 'Evidence, evaluation, and the systems behind personal AI.'),
    'Personal AI': ('personal-ai', 'Memory, expression, and the boundaries of understanding a person.'),
    'Building Products': ('building-products', 'The work around a useful product: communication, adoption, and the business.'),
}
FEATURED = ['did-memory-change-the-decision', 'a-citation-is-not-enough', 'dont-make-me-teach-my-ai-twice']
esc = html.escape
posts = json.loads((SOURCE / 'catalog.json').read_text())
by_slug = {p['slug']: p for p in posts}
assert len(by_slug) == len(posts), 'Duplicate article slug'
for p in posts:
    assert re.fullmatch('[a-z0-9-]+', p['slug'])
    assert p['category'] in CATEGORIES
    assert all(s in by_slug and s != p['slug'] for s in p['related'])
    p['source'] = (SOURCE / (p['slug'] + '.md')).read_text()
    p['minutes'] = max(1, math.ceil(len(re.findall(r"\b[\w’'-]+\b", p['source'])) / 220))
    p['path'] = '/writing/' + p['slug'] + '/'


def head(title, description, path, article=None):
    meta = ''
    if article:
        data = {'@context': 'https://schema.org', '@type': 'BlogPosting',
                'headline': article['title'], 'description': article['description'],
                'author': {'@type': 'Person', 'name': 'Zhihe (Bob) Zhao', 'url': BASE + '/'},
                'datePublished': article['date'], 'dateModified': article['date'],
                'mainEntityOfPage': BASE + path, 'inLanguage': 'en',
                'articleSection': article['category']}
        meta = '<meta property="article:published_time" content="' + article['date'] + '">\n'
        meta += '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — Zhihe (Bob) Zhao</title>
<meta name="description" content="{esc(description, quote=True)}">
<meta name="author" content="Zhihe (Bob) Zhao"><meta name="theme-color" content="#f8f7f3">
<link rel="canonical" href="{BASE}{path}"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css"><link rel="stylesheet" href="/assets/writing.css">
<link rel="alternate" type="application/rss+xml" title="Zhihe Zhao — Writing" href="/writing/feed.xml">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:title" content="{esc(title, quote=True)}"><meta property="og:description" content="{esc(description, quote=True)}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:site_name" content="Zhihe (Bob) Zhao">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{esc(title, quote=True)}">
<meta name="twitter:description" content="{esc(description, quote=True)}">{meta}
</head><body id="top"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner">
<a class="wordmark" href="/">Zhihe Zhao<span>Bob</span></a>
<nav aria-label="Main navigation"><a href="/#work">Current work</a><a href="/writing/" aria-current="{'false' if article else 'page'}">Writing</a><a href="/#featured">Research</a><a href="/#contact">Contact</a></nav>
</div></header>'''


def footer():
    return '''<footer class="wrap writing-footer"><p>© 2026 Zhihe (Bob) Zhao</p><nav aria-label="Footer"><a href="/writing/">All writing</a><a href="/writing/feed.xml">RSS</a><a href="/#contact">Get in touch</a><a href="#top">Back to top ↑</a></nav></footer></body></html>'''


def row(p, featured=False):
    return f'''<article class="writing-entry{' is-featured' if featured else ''}">
<p class="writing-meta">{esc(p['category'])} <span>· {p['minutes']} min read</span></p>
<h3><a href="{p['path']}">{esc(p['title'])}</a></h3>
<p class="writing-summary">{esc(p['description'])}</p></article>'''


def category_nav():
    return '<nav class="category-nav" aria-label="Writing categories">' + ''.join(
        f'<a href="/writing/#{slug}">{esc(name)} <span>{sum(p["category"] == name for p in posts)}</span></a>'
        for name, (slug, _) in CATEGORIES.items()) + '</nav>'


writing = ROOT / 'writing'
writing.mkdir(exist_ok=True)
for p in posts:
    renderer = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists'], extension_configs={'toc': {'permalink': False}})
    body = renderer.convert(p['source'])
    body = body.replace('<table>', '<div class="table-scroll" role="region" aria-label="Comparison table" tabindex="0"><table>').replace('</table>', '</table></div>')
    page = head(p['title'], p['description'], p['path'], p)
    cat = CATEGORIES[p['category']][0]
    page += f'''<main id="main" class="wrap article-main">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/writing/">Writing</a><span aria-hidden="true">/</span><a href="/writing/#{cat}">{esc(p['category'])}</a></nav>
<header class="article-header"><p class="eyebrow">{esc(p['category'])}</p><h1>{esc(p['title'])}</h1>
<p class="article-deck">{esc(p['description'])}</p>
<p class="article-byline">Zhihe (Bob) Zhao <span>·</span> <time datetime="{p['date']}">September 27, 2026</time> <span>·</span> {p['minutes']} min read</p></header>
<div class="article-layout"><aside class="article-toc" aria-label="On this page"><p>In this article</p>{renderer.toc}</aside>
<article class="article-body" aria-label="Article text">{body}
<div class="article-author"><p><strong>Zhihe (Bob) Zhao</strong> is the founder of AxiomsTen, building Spiro. His work explores personal AI, long-term memory, and how systems use an understanding of a person.</p><a href="/">About the author →</a></div></article></div>
<section class="related-writing" aria-labelledby="related-title"><p class="eyebrow">Keep reading</p><h2 id="related-title">Connected questions</h2><div class="related-grid">{''.join(row(by_slug[s]) for s in p['related'])}</div></section></main>'''
    dest = ROOT / p['path'].strip('/')
    dest.mkdir(parents=True, exist_ok=True)
    (dest / 'index.html').write_text(page + footer())

page = head('Writing', 'Technical notes and essays on personal AI, memory, and building useful products.', '/writing/')
page += '''<main id="main" class="wrap writing-main"><header class="writing-heading"><p class="eyebrow">Notes from building</p><h1>Writing</h1><p class="writing-intro">Personal AI, from the decisions inside a system to the person living with its results.</p></header>'''
page += category_nav()
page += '<section class="writing-start" aria-labelledby="start-title"><div><p class="eyebrow">Start here</p><h2 id="start-title">What does it mean<br>to use a memory?</h2></div>' + row(by_slug[FEATURED[0]], True) + '</section>'
for name, (slug, description) in CATEGORIES.items():
    page += f'<section class="writing-category" id="{slug}" aria-labelledby="{slug}-title"><div class="category-heading"><p class="eyebrow">{sum(p["category"] == name for p in posts):02d} articles</p><h2 id="{slug}-title">{name}</h2><p>{description}</p></div><div class="category-entries">'
    page += ''.join(row(p) for p in posts if p['category'] == name)
    page += '</div></section>'
page += '</main>'
(writing / 'index.html').write_text(page + footer())

home = ROOT / 'index.html'
s = home.read_text()
if '/assets/writing.css' not in s:
    s = s.replace('<link rel="stylesheet" href="/assets/site.css">', '<link rel="stylesheet" href="/assets/site.css">\n  <link rel="stylesheet" href="/assets/writing.css">\n  <link rel="alternate" type="application/rss+xml" title="Zhihe Zhao — Writing" href="/writing/feed.xml">')
s = s.replace('<a href="#work">Current work</a><a href="#featured">', '<a href="#work">Current work</a><a href="/writing/">Writing</a><a href="#featured">')
section = '''<!-- WRITING:START -->
    <section id="writing" class="section" aria-labelledby="writing-title">
      <div class="section-label"><span class="number">02</span>Writing</div>
      <div class="section-body"><h2 id="writing-title">Ideas, under examination.</h2>
      <p class="section-lead">Technical notes and essays on memory, personal AI, and building products people want to use.</p>'''
section += category_nav() + ''.join(row(by_slug[x]) for x in FEATURED)
section += '<a class="text-link writing-all" href="/writing/">Explore all 14 articles <span aria-hidden="true">→</span></a></div></section>\n    <!-- WRITING:END -->'
if '<!-- WRITING:START -->' in s:
    s = re.sub(r'<!-- WRITING:START -->.*?<!-- WRITING:END -->', lambda _: section, s, flags=re.S)
else:
    s = s.replace('    <section id="featured"', '    ' + section + '\n\n    <section id="featured"')
    for old,new,label in [('02','03','Selected research'),('03','04','Background'),('04','05','Recognition'),('05','06','Get in touch')]:
        s = s.replace(f'<span class="number">{old}</span>{label}', f'<span class="number">{new}</span>{label}')
home.write_text(s)

# XML serializers escape article titles and URLs correctly.
rss = ET.Element('rss', version='2.0')
channel = ET.SubElement(rss,'channel')
for key,value in [('title','Zhihe (Bob) Zhao — Writing'),('link',BASE+'/writing/'),('description','Technical notes and essays on personal AI, memory, and building products.'),('language','en')]:
    ET.SubElement(channel,key).text=value
for p in posts:
    item=ET.SubElement(channel,'item')
    for key,value in [('title',p['title']),('link',BASE+p['path']),('guid',BASE+p['path']),('description',p['description']),('category',p['category']),('pubDate','Sun, 27 Sep 2026 00:00:00 +0000')]:
        ET.SubElement(item,key).text=value
rss_bytes=ET.tostring(rss,encoding='utf-8',xml_declaration=True)
(writing/'feed.xml').write_bytes(rss_bytes)
(ROOT/'index.xml').write_bytes(rss_bytes)

ns='http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('',ns)
site_map=ET.Element('{'+ns+'}urlset')
for path in ['/', '/writing/']+[p['path'] for p in posts]:
    url=ET.SubElement(site_map,'{'+ns+'}url')
    ET.SubElement(url,'{'+ns+'}loc').text=BASE+path
    ET.SubElement(url,'{'+ns+'}lastmod').text='2026-09-27'
(ROOT/'sitemap.xml').write_bytes(ET.tostring(site_map,encoding='utf-8',xml_declaration=True))
search=json.loads((ROOT/'index.json').read_text())
search=[p for p in search if not p.get('permalink','').startswith(BASE+'/writing/')]
search += [dict(title=p['title'],summary=p['description'],permalink=BASE+p['path'],content=re.sub(r'[#*`>]', '',p['source'])) for p in posts]
(ROOT/'index.json').write_text(json.dumps(search,ensure_ascii=False,indent=2)+'\n')
print(f'Rendered {len(posts)} articles, directory, homepage section, sitemap, search index, and feeds.')
