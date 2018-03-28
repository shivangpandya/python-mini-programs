import bs4,requests

def AmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('#priceblock_ourprice')
    return elems[0].text.strip()



price = AmazonPrice('https://www.amazon.in/Soundpeats-Lightweight-Wireless-Sports-Headset/dp/B00LP6CFEC/ref=sr_1_2?ie=UTF8&qid=1520544988&sr=8-2&keywords=soundpeats')
print('The price is ' +price)
