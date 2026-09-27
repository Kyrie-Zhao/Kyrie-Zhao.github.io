#!/usr/bin/env python3
"""Render both editorial editions; GitHub Pages serves committed static HTML."""
import html
import json
import math
import re
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.etree import ElementTree as ET

import markdown
from markdown.extensions.toc import slugify_unicode
from site_components import X_URL, visitor_stats

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'content/writing'
BASE = 'https://bob-zhihe.github.io'
UPDATED = '2026-09-28'
FEATURED = ['did-memory-change-the-decision', 'a-citation-is-not-enough', 'dont-make-me-teach-my-ai-twice']
CATEGORIES = {
    'Technical Notes': 'technical-notes',
    'Personal AI': 'personal-ai',
    'Building Products': 'building-products',
}
LOCALES = {
    'en': {
        'prefix': '', 'language': 'en', 'og_locale': 'en_US', 'author': 'Zhihe (Bob) Zhao',
        'wordmark': 'Zhihe Zhao', 'skip': 'Skip to content', 'nav': 'Main navigation',
        'work': 'Current work', 'writing': 'Writing', 'research': 'Research', 'contact': 'Contact',
        'language_label': 'Language', 'footer_label': 'Footer', 'all_writing': 'All writing',
        'get_in_touch': 'Get in touch', 'back_to_top': 'Back to top ↑',
        'categories_label': 'Writing categories', 'breadcrumb': 'Breadcrumb',
        'toc_label': 'On this page', 'toc': 'In this article', 'article_text': 'Article text',
        'table_label': 'Comparison table', 'minutes': '{n} min read', 'count': '{n:02d} articles',
        'author_bio': '<strong>Zhihe (Bob) Zhao</strong> is the founder of AxiomsTen, building Spiro. His work explores personal AI, long-term memory, and how systems use an understanding of a person.',
        'about_author': 'About the author →', 'keep_reading': 'Keep reading', 'related': 'Connected questions',
        'description': 'Technical notes and essays on personal AI, memory, and building useful products.',
        'eyebrow': 'Notes from building',
        'intro': 'Personal AI, from the decisions inside a system to the person living with its results.',
        'start': 'Start here', 'start_title': 'What does it mean<br>to use a memory?',
        'home_title': 'Ideas, under examination.',
        'home_intro': 'Technical notes and essays on memory, personal AI, and building products people want to use.',
        'explore': 'Explore all {n} articles',
        'categories': {
            'Technical Notes': ('Technical Notes', 'Evidence, evaluation, and the systems behind personal AI.'),
            'Personal AI': ('Personal AI', 'Memory, expression, and the boundaries of understanding a person.'),
            'Building Products': ('Building Products', 'The work around a useful product: communication, adoption, and the business.'),
        },
    },
    'zh': {
        'prefix': '/zh', 'language': 'zh-CN', 'og_locale': 'zh_CN', 'author': '赵之赫（Bob）',
        'wordmark': '赵之赫', 'skip': '跳转到正文', 'nav': '主导航',
        'work': '现在在做', 'writing': '文章', 'research': '研究', 'contact': '联系',
        'language_label': '语言', 'footer_label': '页尾导航', 'all_writing': '全部文章',
        'get_in_touch': '联系我', 'back_to_top': '返回顶部 ↑',
        'categories_label': '文章分类', 'breadcrumb': '当前位置',
        'toc_label': '文章目录', 'toc': '本文目录', 'article_text': '文章正文',
        'table_label': '对照表', 'minutes': '阅读约 {n} 分钟', 'count': '{n:02d} 篇文章',
        'author_bio': '<strong>赵之赫（Bob）</strong>是 AxiomsTen 创始人，正在打造 Spiro。他关注个人 AI、长期记忆，以及系统如何将对一个人的理解用在具体事情上。',
        'about_author': '关于作者 →', 'keep_reading': '继续阅读', 'related': '也许你还想看',
        'description': '关于个人 AI、记忆与产品的技术笔记和随笔。',
        'eyebrow': '做产品时，也想这些问题',
        'intro': '从系统怎样作出一个决定，到这个决定怎样影响一个人的生活。',
        'start': '从这里读起', 'start_title': '记住了，<br>然后呢？',
        'home_title': '把正在想的问题，写下来。',
        'home_intro': '关于记忆、个人 AI，以及如何做出有用产品的技术笔记与随笔。',
        'explore': '阅读全部 {n} 篇文章',
        'categories': {
            'Technical Notes': ('技术笔记', '个人 AI 的证据、评估方法与系统设计。'),
            'Personal AI': ('个人 AI', '记忆、表达，以及理解一个人的边界。'),
            'Building Products': ('产品与创业', '一个有用的产品，还要解决沟通、持续使用和商业上的问题。'),
        },
    },
}
esc = html.escape


def alternate_links(path):
    return '\n'.join(f'<link rel="alternate" hreflang="{lang}" href="{BASE}{prefix}{path}">'
                     for lang, prefix in [('en', ''), ('zh-CN', '/zh'), ('x-default', '')])


def language_switch(locale, path):
    links = []
    for key, label in [('en', 'EN'), ('zh', '中文')]:
        cfg = LOCALES[key]
        current = ' aria-current="page"' if key == locale else ''
        links.append(f'<a href="{cfg["prefix"]}{path}" lang="{cfg["language"]}" hreflang="{cfg["language"]}"{current}>{label}</a>')
    return f'<nav class="language-switch" aria-label="{LOCALES[locale]["language_label"]}">' + ''.join(links) + '</nav>'


def load_posts():
    originals = json.loads((SOURCE / 'catalog.json').read_text())
    translations = json.loads((SOURCE / 'zh/catalog.json').read_text())
    en_slugs = {p['slug'] for p in originals}
    zh_by_slug = {p['slug']: p for p in translations}
    assert len(en_slugs) == len(originals), 'Duplicate English slug'
    assert len(zh_by_slug) == len(translations), 'Duplicate Chinese slug'
    assert en_slugs == set(zh_by_slug), 'Every article needs both language editions'
    result = {}
    for locale, cfg in LOCALES.items():
        posts = []
        for original in originals:
            p = original.copy()
            assert re.fullmatch('[a-z0-9-]+', p['slug'])
            assert p['category'] in CATEGORIES
            assert all(s in en_slugs and s != p['slug'] for s in p['related'])
            if locale == 'zh':
                p.update(zh_by_slug[p['slug']])
            datetime.strptime(p['date'], '%Y-%m-%d')
            directory = SOURCE / 'zh' if locale == 'zh' else SOURCE
            p['source'] = (directory / (p['slug'] + '.md')).read_text()
            assert p['source'].strip(), f'Empty article: {locale}/{p["slug"]}'
            words = len(re.findall(r"\b[a-zA-Z][\w’'-]*\b", p['source']))
            han = len(re.findall(r'[\u3400-\u9fff]', p['source']))
            p['minutes'] = max(1, math.ceil(words / 220 + han / 350))
            p['base_path'] = '/writing/' + p['slug'] + '/'
            p['path'] = cfg['prefix'] + p['base_path']
            posts.append(p)
        result[locale] = posts
    return result


def date_label(value, locale):
    d = datetime.strptime(value, '%Y-%m-%d')
    return f'{d.year} 年 {d.month} 月 {d.day} 日' if locale == 'zh' else f'{d:%B} {d.day}, {d.year}'


def head(title, description, path, locale, article=None):
    cfg = LOCALES[locale]
    prefix = cfg['prefix']
    url = BASE + prefix + path
    meta = ''
    if article:
        data = {'@context': 'https://schema.org', '@type': 'BlogPosting',
                'headline': title, 'description': description,
                'author': {'@type': 'Person', 'name': 'Zhihe (Bob) Zhao', 'url': BASE + '/'},
                'datePublished': article['date'], 'dateModified': UPDATED,
                'mainEntityOfPage': url, 'inLanguage': cfg['language'],
                'articleSection': cfg['categories'][article['category']][0]}
        other = 'en' if locale == 'zh' else 'zh'
        data['translationOfWork' if locale == 'zh' else 'workTranslation'] = {
            '@type': 'BlogPosting', '@id': BASE + LOCALES[other]['prefix'] + path,
            'inLanguage': LOCALES[other]['language']}
        meta = f'<meta property="article:published_time" content="{article["date"]}">\n'
        meta += '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
    current = '' if article else ' aria-current="page"'
    return f'''<!doctype html>
<html lang="{cfg['language']}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — {cfg['author']}</title>
<meta name="description" content="{esc(description, quote=True)}">
<meta name="author" content="{cfg['author']}"><meta name="theme-color" content="#f8f7f3">
<link rel="canonical" href="{url}">
{alternate_links(path)}
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css"><link rel="stylesheet" href="/assets/writing.css">
<link rel="alternate" type="application/rss+xml" title="{cfg['author']} — {cfg['writing']}" href="{prefix}/writing/feed.xml">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:title" content="{esc(title, quote=True)}"><meta property="og:description" content="{esc(description, quote=True)}">
<meta property="og:url" content="{url}"><meta property="og:site_name" content="{cfg['author']}">
<meta property="og:locale" content="{cfg['og_locale']}">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{esc(title, quote=True)}">
<meta name="twitter:description" content="{esc(description, quote=True)}">{meta}
</head><body id="top"><a class="skip-link" href="#main">{cfg['skip']}</a>
<header class="site-header"><div class="wrap header-inner">
<a class="wordmark" href="{prefix}/">{cfg['wordmark']}<span lang="en">Bob</span></a>
<div class="header-controls"><nav aria-label="{cfg['nav']}"><a href="{prefix}/#work">{cfg['work']}</a><a href="{prefix}/writing/"{current}>{cfg['writing']}</a><a href="{prefix}/#featured">{cfg['research']}</a><a href="{prefix}/#contact">{cfg['contact']}</a></nav>
{language_switch(locale, path)}</div></div></header>'''


def footer(locale):
    c = LOCALES[locale]
    prefix = c['prefix']
    return visitor_stats(locale) + f'''<footer class="wrap writing-footer"><p>© 2026 {c['author']}</p><nav aria-label="{c['footer_label']}"><a href="{X_URL}" rel="me">X <span aria-hidden="true">↗</span></a><a href="{prefix}/writing/">{c['all_writing']}</a><a href="{prefix}/writing/feed.xml">RSS</a><a href="{prefix}/#contact">{c['get_in_touch']}</a><a href="#top">{c['back_to_top']}</a></nav></footer></body></html>'''


def row(p, locale, featured=False):
    cfg = LOCALES[locale]
    return f'''<article class="writing-entry{' is-featured' if featured else ''}">
<p class="writing-meta">{esc(cfg['categories'][p['category']][0])} <span>· {cfg['minutes'].format(n=p['minutes'])}</span></p>
<h3><a href="{p['path']}">{esc(p['title'])}</a></h3>
<p class="writing-summary">{esc(p['description'])}</p></article>'''


def category_nav(posts, locale):
    c = LOCALES[locale]
    return f'<nav class="category-nav" aria-label="{c["categories_label"]}">' + ''.join(
        f'<a href="{c["prefix"]}/writing/#{slug}">{esc(c["categories"][name][0])} <span>{sum(p["category"] == name for p in posts)}</span></a>'
        for name, slug in CATEGORIES.items()) + '</nav>'


def render_edition(posts, locale):
    c = LOCALES[locale]
    prefix = c['prefix']
    by_slug = {p['slug']: p for p in posts}
    writing = ROOT / prefix.strip('/') / 'writing'
    writing.mkdir(parents=True, exist_ok=True)
    for p in posts:
        toc_config = {'permalink': False}
        if locale == 'zh':
            toc_config['slugify'] = slugify_unicode
        renderer = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists'], extension_configs={'toc': toc_config})
        body = renderer.convert(p['source'])
        body = body.replace('<table>', f'<div class="table-scroll" role="region" aria-label="{c["table_label"]}" tabindex="0"><table>').replace('</table>', '</table></div>')
        cat = CATEGORIES[p['category']]
        cat_label = c['categories'][p['category']][0]
        page = head(p['title'], p['description'], p['base_path'], locale, p)
        page += f'''<main id="main" class="wrap article-main">
<nav class="breadcrumbs" aria-label="{c['breadcrumb']}"><a href="{prefix}/writing/">{c['writing']}</a><span aria-hidden="true">/</span><a href="{prefix}/writing/#{cat}">{cat_label}</a></nav>
<header class="article-header"><p class="eyebrow">{cat_label}</p><h1>{esc(p['title'])}</h1>
<p class="article-deck">{esc(p['description'])}</p>
<p class="article-byline">{c['author']} <span>·</span> <time datetime="{p['date']}">{date_label(p['date'], locale)}</time> <span>·</span> {c['minutes'].format(n=p['minutes'])}</p></header>
<div class="article-layout"><aside class="article-toc" aria-label="{c['toc_label']}"><p>{c['toc']}</p>{renderer.toc}</aside>
<article class="article-body" aria-label="{c['article_text']}">{body}
<div class="article-author"><p>{c['author_bio']}</p><a href="{prefix}/">{c['about_author']}</a></div></article></div>
<section class="related-writing" aria-labelledby="related-title"><p class="eyebrow">{c['keep_reading']}</p><h2 id="related-title">{c['related']}</h2><div class="related-grid">{''.join(row(by_slug[s], locale) for s in p['related'])}</div></section></main>'''
        dest = ROOT / p['path'].strip('/')
        dest.mkdir(parents=True, exist_ok=True)
        (dest / 'index.html').write_text(page + footer(locale))
    page = head(c['writing'], c['description'], '/writing/', locale)
    page += f'''<main id="main" class="wrap writing-main"><header class="writing-heading"><p class="eyebrow">{c['eyebrow']}</p><h1>{c['writing']}</h1><p class="writing-intro">{c['intro']}</p></header>'''
    page += category_nav(posts, locale)
    page += f'<section class="writing-start" aria-labelledby="start-title"><div><p class="eyebrow">{c["start"]}</p><h2 id="start-title">{c["start_title"]}</h2></div>' + row(by_slug[FEATURED[0]], locale, True) + '</section>'
    for name, slug in CATEGORIES.items():
        label, description = c['categories'][name]
        count = sum(p['category'] == name for p in posts)
        page += f'<section class="writing-category" id="{slug}" aria-labelledby="{slug}-title"><div class="category-heading"><p class="eyebrow">{c["count"].format(n=count)}</p><h2 id="{slug}-title">{label}</h2><p>{description}</p></div><div class="category-entries">'
        page += ''.join(row(p, locale) for p in posts if p['category'] == name)
        page += '</div></section>'
    (writing / 'index.html').write_text(page + '</main>' + footer(locale))
    update_home(posts, locale)
    write_feed(posts, locale, writing)
    write_search(posts, locale)


def update_home(posts, locale):
    c = LOCALES[locale]
    home = ROOT / c['prefix'].strip('/') / 'index.html'
    source = home.read_text()
    by_slug = {p['slug']: p for p in posts}
    section = f'''<!-- WRITING:START -->
    <section id="writing" class="section" aria-labelledby="writing-title">
      <div class="section-label"><span class="number">02</span>{c['writing']}</div>
      <div class="section-body"><h2 id="writing-title">{c['home_title']}</h2>
      <p class="section-lead">{c['home_intro']}</p>'''
    section += category_nav(posts, locale) + ''.join(row(by_slug[x], locale) for x in FEATURED)
    section += f'<a class="text-link writing-all" href="{c["prefix"]}/writing/">{c["explore"].format(n=len(posts))} <span aria-hidden="true">→</span></a></div></section>\n    <!-- WRITING:END -->'
    for name, replacement in [('WRITING', section), ('LANGUAGE', '<!-- LANGUAGE:START -->' + language_switch(locale, '/') + '<!-- LANGUAGE:END -->'), ('ALTERNATES', '<!-- ALTERNATES:START -->\n' + alternate_links('/') + '\n  <!-- ALTERNATES:END -->'), ('VISITORS', '<!-- VISITORS:START -->\n' + visitor_stats(locale) + '\n  <!-- VISITORS:END -->')]:
        pattern = rf'<!-- {name}:START -->.*?<!-- {name}:END -->'
        source, count = re.subn(pattern, lambda _: replacement, source, flags=re.S)
        assert count == 1, f'{home}: expected one {name} marker'
    home.write_text(source)


def write_feed(posts, locale, writing):
    c = LOCALES[locale]
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')
    for key, value in [('title', c['author'] + ' — ' + c['writing']), ('link', BASE + c['prefix'] + '/writing/'), ('description', c['description']), ('language', c['language'])]:
        ET.SubElement(channel, key).text = value
    for p in posts:
        item = ET.SubElement(channel, 'item')
        published = datetime.strptime(p['date'], '%Y-%m-%d').replace(tzinfo=timezone.utc)
        for key, value in [('title', p['title']), ('link', BASE + p['path']), ('guid', BASE + p['path']), ('description', p['description']), ('category', c['categories'][p['category']][0]), ('pubDate', format_datetime(published))]:
            ET.SubElement(item, key).text = value
    data = ET.tostring(rss, encoding='utf-8', xml_declaration=True)
    (writing / 'feed.xml').write_bytes(data)
    (writing.parent / 'index.xml').write_bytes(data)


def write_search(posts, locale):
    c = LOCALES[locale]
    if locale == 'en':
        previous = json.loads((ROOT / 'index.json').read_text())
        profile = next(p for p in previous if p.get('relpermalink') == '/')
    else:
        profile = {'authors': ['赵之赫'], 'title': c['author'], 'permalink': BASE + '/zh/', 'relpermalink': '/zh/', 'type': 'page',
                   'summary': 'AxiomsTen 创始人兼 CEO，正在打造 Spiro。2025 年获香港中文大学博士学位。',
                   'content': '赵之赫（Bob），AxiomsTen 创始人兼 CEO，正在打造 Spiro，关注个人 AI、长期记忆与理解具体情境的智能体。2025 年获香港中文大学博士学位，研究高效 AI 系统。此前共同创办 ThingX 并担任 CEO，与团队参与打造 Nuna（原名 PieX）和 Collie R1。2024 年入选福布斯中国 30 Under 30。'}
    search = [{**profile, 'language': c['language']}]
    search += [dict(title=p['title'], summary=p['description'], permalink=BASE + p['path'], content=re.sub(r'[#*`>]', '', p['source']), language=c['language']) for p in posts]
    (ROOT / c['prefix'].strip('/') / 'index.json').write_text(json.dumps(search, ensure_ascii=False, indent=2) + '\n')


def write_sitemap(editions):
    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    xhtml = 'http://www.w3.org/1999/xhtml'
    ET.register_namespace('', ns)
    ET.register_namespace('xhtml', xhtml)
    sitemap = ET.Element('{' + ns + '}urlset')
    base_paths = ['/', '/writing/'] + [p['base_path'] for p in editions['en']]
    for cfg in LOCALES.values():
        for path in base_paths:
            url = ET.SubElement(sitemap, '{' + ns + '}url')
            ET.SubElement(url, '{' + ns + '}loc').text = BASE + cfg['prefix'] + path
            ET.SubElement(url, '{' + ns + '}lastmod').text = UPDATED
            for lang, prefix in [('en', ''), ('zh-CN', '/zh'), ('x-default', '')]:
                ET.SubElement(url, '{' + xhtml + '}link', rel='alternate', hreflang=lang, href=BASE + prefix + path)
    (ROOT / 'sitemap.xml').write_bytes(ET.tostring(sitemap, encoding='utf-8', xml_declaration=True))


def main():
    editions = load_posts()
    for locale, posts in editions.items():
        render_edition(posts, locale)
    write_sitemap(editions)
    print(f'Rendered {sum(map(len, editions.values()))} articles in {len(editions)} languages, directories, homepage sections, feeds, search indexes, and sitemap.')


if __name__ == '__main__':
    main()
