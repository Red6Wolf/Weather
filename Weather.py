import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
       #pprint(data)

        city = data["name"]
        cur_weather = data ["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        visibility = data ["visibility"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]

        print(f"Погода в городе: {city}\nТемпература:{cur_weather}C°\n"
              f"Влажность: {humidity}%\nДавление:{pressure}мм.рт.ст\n"
              f"Ветер: {wind}м/с\nВидимость: {visibility}\n"
              f"Минимальная температура: {temp_min}C°\nМаксимальная температура: {temp_max}C°\n"
              )
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': open_weather_token})
        data = res.json()

        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': open_weather_token})
        data = res.json()
        print("\n\nПрогноз погоды на неделю:")
        for i in data['list']:
            print("Дата:", i['dt_txt'], "\r\nТемпература", '{0:+3.0f}'.format(i['main']['temp']),
                  "\r\nПогодные условия:", i['weather'][0]['description'],
                  "\r\nВетер:",i['wind']['speed'],
                  "\r\nВидимость:",i['visibility'])
            print("____________________________")
            print("Хорошего дня. До свидания!")


    except Exception as ex:
        print(ex)
        print("Неправильное название города")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
