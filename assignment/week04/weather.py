import requests
import json

cityname = ["Seoul", "London"]  # 서울과 런던 날씨

for city in cityname:  # 반복문 통해서 차례로 접근

    apikey = "08c77c7a150db354dd462c2e2ffcbd77"  # key는 비밀!
    lang = "kr"  # 한국어 설정
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

    result = requests.get(api)
    data = json.loads(result.text)
    # print(result)

    print(data["name"], "의 날씨입니다.")
    print("날씨는 ", data["weather"][0]["description"], "입니다.")
    print("현재 온도는 ", data["main"]["temp"], "입니다.")
    print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
    print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
    print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
    print("기압은 ", data["main"]["pressure"], "입니다.")
    print("습도는 ", data["main"]["humidity"], "입니다.\n")
