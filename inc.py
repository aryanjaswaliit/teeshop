import requests

n = 0
while n < 100:
    #store url
    url = "https://teeshopper.in/store/MJartistic"
    header = {
        "User-Agent":"Nasa"
    }
    data = requests.get(url,headers=header)
    #print(data)
    n = n +1
    print(n)