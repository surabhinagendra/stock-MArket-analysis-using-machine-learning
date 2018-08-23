import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2018-04-03&'
       'sortBy=popularity&'
       'apiKey=6912a4b71deb466881f582762e239b3a')

r = requests.get(url)

print (r.json)
