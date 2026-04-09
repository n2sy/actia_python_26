import json

dict = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "café",
    "email": "français",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {"lat": "-37.3159", "lng": "81.1496"},
    },
}

data = {}
with open("infos.json", "w") as f:
    json.dump(dict, f, indent=4, ensure_ascii=False)

with open("infos.json", "r") as f:
    data = json.load(f)
    print(data)
