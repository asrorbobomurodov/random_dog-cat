import requests

def get_dog():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    return response.json()['url']

def get_cat():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    return response.json()[0]['url']

def get_fox():
    url = 'https://randomfox.ca/floof/'
    r = requests.get(url)
    return r.json()['image']


