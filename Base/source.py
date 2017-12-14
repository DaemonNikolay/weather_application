token_open_weather_api = '066bdda4bf6b0e5d4d2980b47a95119d'

import requests
import datetime
import locale
from PIL import (Image,
                 ImageDraw,
                 ImageFont)

locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
# locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

print('Введите город: ')
# city = input()
city = 'Novosibirsk'

print('Какой срок: "Сегодня", "Завтра", "Неделя" или "2 недели"')
# days = input()
days = '2 недели'

temp_address = str('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city + '&cnt=' + str(
    14) + '&appid=066bdda4bf6b0e5d4d2980b47a95119d')
print(temp_address)
# print('address: ', temp_address, '\n\n')

proxies = {'http': 'http://st_nik:ubgjnfkfvec123@ci.nsu.ru:3128/'}
response = requests.get(temp_address, proxies = proxies)

j = response.json()
# print(j)
# print('\n\n\n')
n = 0


def weather_all(n):
    img = Image.new("RGB", (400, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)
    x = 10
    y = 10

    udate = j['list'][n]['dt']
    date = datetime.datetime.fromtimestamp(int(udate)).strftime('%d.%m.%Y - %A')
    temp_min = j["list"][n]["temp"]["min"]
    temp_max = j["list"][n]["temp"]["max"]
    temp_morn = j["list"][n]["temp"]["morn"]
    temp_day = j["list"][n]["temp"]["day"]
    temp_eve = j["list"][n]["temp"]["eve"]
    temp_night = j["list"][n]["temp"]["night"]

    temp_humidity = j["list"][n]["humidity"]
    temp_pressure = j["list"][n]["pressure"]
    temp_speed_wind = j["list"][n]["speed"]
    temp_clouds = j["list"][n]["clouds"]

    direction_of_the_wind = j["list"][n]["deg"]

    weather = j['list'][n]["weather"][0]["description"]

    temp_min = str(int(float(temp_min) - 273.15)) + chr(176) + 'C'
    temp_max = str(int(float(temp_max) - 273.15)) + chr(176) + 'C'
    temp_morn = str(int(float(temp_morn) - 273.15)) + chr(176) + 'C'
    temp_day = str(int(float(temp_day) - 273.15)) + chr(176) + 'C'
    temp_eve = str(int(float(temp_eve) - 273.15)) + chr(176) + 'C'
    temp_night = str(int(float(temp_night) - 273.15)) + chr(176) + 'C'

    temp_humidity = str(temp_humidity) + chr(37)
    temp_pressure = str(int(temp_pressure * 0.75006375541921)) + ' мм р.т.'
    temp_clouds = str(temp_clouds) + chr(37)
    temp_speed_wind = str(temp_speed_wind) + ' м/с'

    direction_of_the_wind = wind_direction_conversion(direction_of_the_wind)

    weather = weather_lang_Russian(weather)

    slovar = {"Город: ": city,
              "Дата: ": date,
              "Утро: ": temp_morn,
              "День: ": temp_day,
              "Вечер: ": temp_eve,
              "Ночь: ": temp_night,
              "Осадки: ": weather,
              "Влажность: ": temp_humidity,
              "Давление: ": temp_pressure,
              "Направление ветра: ": direction_of_the_wind,
              "Скорость ветра: ": temp_speed_wind,
              "Облачность: ": temp_clouds
              }

    for key, value in slovar.items():
        # print(key, value)
        format_file = str(date) + '.png'
        draw.text((x, y), str(key + value), fill = "white", font = font)
        img.save(format_file, "PNG")

        y += 40

    img.close()
    # print('Дата: ', date)
    # print("Минимальная температура: ", temp_min)
    # print("Максимальная температура: ", temp_max)
    # print("Утренняя температура: ", temp_morn)
    # print("Дневная температура: ", temp_day)
    # print("Вечерняя температура: ", temp_eve)
    # print("Ночная температура: ", temp_night)
    # print("Осадки: ", weather)
    # print("Влажность: ", temp_humidity)
    # print("Давление: ", temp_pressure)
    # print("Направление ветра: ", direction_of_the_wind)
    # print("Скорость ветра: ", temp_speed_wind)
    # print("Облачность: ", temp_clouds)
    # print("----------------------\n\n")


def weather_lang_Russian(weather_lang):
    if (weather_lang == 'sky is clear'):
        temp_weather = 'Небо чистое'
        return temp_weather
    elif (weather_lang == 'light rain'):
        temp_weather = 'Лёгкий дождь'
        return temp_weather
    elif (weather_lang == 'moderate rain'):
        temp_weather = 'Умеренный дождь'
        return temp_weather
    elif (weather_lang == 'heavy intensity rain'):
        temp_weather = 'Сильный дождь'
        return temp_weather
    elif (weather_lang == 'few clouds'):
        temp_weather = 'Малая облачность'
        return temp_weather
    elif (weather_lang == 'light snow'):
        temp_weather = 'Лёгкий снег'
        return temp_weather
    elif (weather_lang == 'snow'):
        temp_weather = 'Снег'
        return temp_weather

    elif (weather_lang == 'broken clouds'):
        temp_weather = 'Местами облачно'
        return temp_weather
    elif (weather_lang == 'overcast clouds'):
        temp_weather = 'Пасмурно'
        return temp_weather
    elif (weather_lang == 'scattered clouds'):
        temp_weather = 'Перестые облака'
        return temp_weather
    elif (weather_lang == 'scattered clouds'):
        temp_weather = 'Перестые облака'
        return temp_weather

    else:
        return weather_lang


def wind_direction_conversion(wind):
    if (wind <= 10) or (wind >= 350):
        temp_wind_direction = 'Северный'
        return temp_wind_direction
    elif ((wind >= 80) and (wind <= 100)):
        temp_wind_direction = 'Восточный'
        return temp_wind_direction
    elif ((wind >= 170) and (wind <= 190)):
        temp_wind_direction = 'Южный'
        return temp_wind_direction
    elif ((wind >= 260) and (wind <= 280)):
        temp_wind_direction = 'Западный'
        return temp_wind_direction

    elif ((wind > 10) and (wind < 80)):
        temp_wind_direction = 'Северо-восточный'
        return temp_wind_direction
    elif ((wind > 100) and (wind < 170)):
        temp_wind_direction = 'Юго-восточный'
        return temp_wind_direction
    elif ((wind > 190) and (wind < 260)):
        temp_wind_direction = 'Юго-западный'
        return temp_wind_direction
    elif ((wind > 280) and (wind < 350)):
        temp_wind_direction = 'Северо-западный'
        return temp_wind_direction

    else:
        temp_wind_direction = 'Направление: ' + str(wind) + chr(176)
        return temp_wind_direction


if days == "Неделя".lower():
    while n < 7:
        weather_all(n)
        n = n + 1

elif days == '2 недели':
    while n < 14:
        weather_all(n)
        n = n + 1

elif days == 'Завтра'.lower():
    weather_all(1)

elif days == 'Сегодня'.lower():
    weather_all(0)

input('Расчёт прогноза завершён!\nДля выхода нажмите клавишу!')
