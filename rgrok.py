import requests

def rgrok(target, after = None):
    params = { "after": after } if after else {}
    response = requests.get(f"https://reddit.com/r/{target}/top.json?t=all", headers = { 'User-Agent': 'your-neighborhood-bot' }, params=params)
    response_data = response.json()['data']
    posts = [p['data'] for p in response_data['children']]
    urls = [p['url'] for p in posts]
    search_terms = ["redd.it", "imgur"]
    displayable_urls = [u for u in urls if True in [s in u for s in search_terms]]
    last = posts[-1]['name']
    return { "urls": displayable_urls, "last": last }
