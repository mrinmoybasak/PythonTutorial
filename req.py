import requests

r = requests .get("https://financialmodelingprep.com/api/v3/profile/SBIN.NS?apikey=0fe8785daec81a82c31f1f0a3529fddc")
print(r.text)