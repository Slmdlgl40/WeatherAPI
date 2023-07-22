import requests

while True:

    try:
        city = input("Lütfen şehrinizi baş harfi büyük olacak şekilde yazın(çıkmak için 'q' ya basın): ")
        if city == "q":
            break
        else:
            link = "http://api.weatherapi.com/v1/current.json?key=3b9f373c0373497c85c212548232207&q=" + city + "&aqi=no"
            response = requests.get(link)
            result = response.json()
            print("Şehir: ", result["location"]["name"])
            print("Sıcaklık: ", result["current"]["temp_c"])
    except:
        print("Lütfen geçerli bir şehir girin")