import requests

url = "https://studious-xylophone-7v9pwv55qxpw2wxwr-8000.app.github.dev/"

# ejemplo request en GET
r = requests.get(url)
print(r.text)

# ejemplo request en POST
r = requests.post(
    url + "encolar", json={"nombre": "Juan", "productos": ["manzana", "pera"], "Documento": 12345}
)
print(r.text)
