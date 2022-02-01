KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Здоровье'}
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.926374693.1592849458; _ym_uid=1592849458836139512; _ym_d=1643722900; _gid=GA1.2.575228220.1643722900; hl=ru; fl=ru; _ym_isad=2; __gads=ID=d5d3ec31f3626681:T=1643722900:S=ALNI_MZo6tbe6TTbR4MeLkK7DbWYLVVoaA; _fbp=fb.1.1643723044372.1106360802; habr_web_home=ARTICLES_LIST_ALL; cto_bundle=pMMqlV9mTHJocjglMkI0ZkRFVGpSaFpiNEV6WEc4eUJkNmJHJTJCSGFleVR4ZlZ4MmtwSlFuSG5WdTNCRXpCbSUyRm9xRmVKaEJ5UjRHYTRpSng0SEtvMGJFc1Q3YVZETGlPYzBHU3U0c0owdXVoJTJCMiUyRkwydG5hbnc2ayUyQiUyQnolMkJyYjlYRUklMkJoRGE4ZjlOdkhRVWp3cDAzb09aWE1qZDFlS2clM0QlM0Q',
            'Host': 'habr.com',
            'If-None-Match': 'W/"3b1c6-EW89rQbxWFkz3nvkFcL3GvbM5mw"',
            'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36}'}
import requests
from bs4 import BeautifulSoup

ret = requests.get('https://habr.com/ru/all/', headers=HEADERS)
soup = BeautifulSoup(ret.text, 'html.parser')

posts = soup.find_all('article')
for post in posts:
    title = post.find('h2')
    hubs = post.find_all('a', class_='tm-article-snippet__hubs-item-link')
    post_hubs = [hub.find('span').text for hub in hubs]
    descript = post.find(class_='tm-article-body tm-article-snippet__lead').text
    descript_list = str(descript).split(' ')
    all_descript = set(descript_list+title.text.split(' ')+post_hubs)

    if all_descript & KEYWORDS:
        href_of = 'https://habr.com' + str(title.find('a')['href'])
        date_of = post.find(class_='tm-article-snippet__datetime-published').text
        print(date_of, title.text, href_of)


