import requests
import json
#ipaddress = input("Enter IP Address : ")
ipaddress='8.8.8.8'
ipaddress='81.65.151.83'

iprequest = requests.get(f"http://ip-api.com/json/{ipaddress}")
if iprequest.status_code == 200: 
    ipdata = json.loads(iprequest.text)
    if ipdata["status"]=="success":
        print("Country", ipdata["country"],
ipdata["countryCode"])

print("Region :", ipdata["region"], ipdata["regionName"])
print("City", ipdata["city"])
print("Zip :", ipdata["zip"])
lat = ipdata["lat"]
lon = ipdata["lon"]
print("location :", lat, ",", lon)