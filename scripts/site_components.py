"""Shared static components used by both homepages and all writing pages."""

X_URL = 'https://x.com/zzhontheway'
VISITOR_STATS_URL = 'https://s01.flagcounter.com/more/nO2k'
# The provider issued this counter specifically during this site's setup.
# One shared image request counts a pageview; do not add a second tracking pixel.
VISITOR_MAP_URL = 'https://s01.flagcounter.com/map/nO2k/size_m/txt_202D29/border_F8F7F3/pageviews_1/viewers_0/flags_0/'


def visitor_stats(locale):
    copy = {
        'en': {
            'label': 'Site visitors',
            'title': 'Readers around the world',
            'description': 'Page views and visitor countries across the English and Chinese editions.',
            'since': 'Counting from September 28, 2026.',
            'details': 'View visitor statistics',
            'alt': 'World map of visitor countries with the cumulative pageview count, provided by Flag Counter',
            'note': 'Locations are approximate. The map and count update about every five minutes.',
            'privacy': 'Privacy policy',
        },
        'zh': {
            'label': '访问统计',
            'title': '来自世界各地的读者',
            'description': '中英文网站共同累计的访问量，以及访客来源国家与地区。',
            'since': '自 2026 年 9 月 28 日起统计。',
            'details': '查看详细访问统计',
            'alt': '访客来源世界地图与累计页面访问量，由 Flag Counter 提供',
            'note': '地理位置为近似估算，地图与计数约每五分钟更新一次。',
            'privacy': '隐私说明',
        },
    }[locale]
    return f'''<section id="visitors" class="wrap visitor-stats" aria-labelledby="visitors-title">
  <div class="visitor-copy">
    <p class="eyebrow">{copy['label']}</p>
    <h2 id="visitors-title">{copy['title']}</h2>
    <p>{copy['description']}</p>
    <p class="visitor-since">{copy['since']}</p>
    <a class="text-link" href="{VISITOR_STATS_URL}">{copy['details']} <span aria-hidden="true">↗</span></a>
  </div>
  <figure class="visitor-map">
    <a href="{VISITOR_STATS_URL}" aria-label="{copy['details']}">
      <img src="{VISITOR_MAP_URL}" width="600" height="291" alt="{copy['alt']}" loading="eager" decoding="async" fetchpriority="low" referrerpolicy="origin">
    </a>
    <figcaption>{copy['note']} <a href="https://flagcounter.com/">Flag Counter</a> · <a href="https://flagcounter.com/privacy.html">{copy['privacy']}</a></figcaption>
  </figure>
</section>'''
