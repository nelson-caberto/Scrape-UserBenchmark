from lxml import html
import requests

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
headers = {'User-Agent': user_agent}
url = 'https://www.userbenchmark.com/page/developer'

response = requests.get(url, headers=headers)

page = html.fromstring(response.content)

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
headers = {'User-Agent': user_agent}
url = 'https://www.userbenchmark.com/page/developer'

response = requests.get(url, headers=headers)

page = html.fromstring(response.content)

