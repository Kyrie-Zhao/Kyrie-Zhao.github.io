"""Shared static components used by both homepages and all writing pages."""

X_URL = 'https://x.com/zzhontheway'
# Keep the same counter across all pages; the image includes the pageview total.
VISITOR_MAP_URL = 'https://s01.flagcounter.com/map/nO2k/size_m/txt_202D29/border_F8F7F3/pageviews_1/viewers_0/flags_0/'


def visitor_stats(locale):
    alt = {
        'en': 'World map of visitor countries and total page views',
        'zh': '全球访客地图与累计访问量',
    }[locale]
    return f'''<div id="visitors" class="wrap visitor-stats">
  <img class="visitor-map" src="{VISITOR_MAP_URL}" width="600" height="291" alt="{alt}" loading="eager" decoding="async" fetchpriority="low" referrerpolicy="origin">
</div>'''
