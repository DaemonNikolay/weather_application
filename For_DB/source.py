import requests
import datetime
import locale
import constant
import time


def sleep():
    time.sleep(86400)


def insert(date, day, t_morning, t_afternoon, t_evening, t_night, precipitation, himidity, pressure, direction_wind,
           speed_wind, cloud):
    import insert_to_db

    # sql1 = """UPDATE `NOVOSIBIRSK` SET `Date`="22-01-2017",`Day`="среда",`t_Morning`=10,`t_Afternoon`=15,`t_Evening`=20,`t_Night`=25,`Precipitation`="снег",`Himidity`=90,`Pressure`=17,`Direction_wind`="восток",`Speed_wind`=44,`Cloud`=55 WHERE 1"""

    # sql_insert = """INSERT INTO NOVOSIBIRSK (`Date`, `day`, `t_Morning`,`t_Afternoon`,  `t_Evening`, `t_Night`, `Precipitation`,`Himidity`, `Pressure`, `Direction_wind`, `Speed_wind`, `Cloud` )
    #                 VALUES ('%s', '%s', %d, %d, %d, %d, '%s', %d, %d, '%s', %f, %d)""" % (
    #     date, day, t_morning, t_afternoon, t_evening, t_night, precipitation, himidity, pressure, direction_wind,
    #     speed_wind, cloud)

    insert_to_db.insert(date, day, t_morning, t_afternoon, t_evening, t_night, precipitation, himidity, pressure,
                        direction_wind, speed_wind, cloud)


def weather_all(n):
    x = 10
    y = 10

    udate = j['list'][n]['dt']
    # date = datetime.datetime.fromtimestamp(int(udate)).strftime('%d.%m.%Y')
    date = datetime.datetime.fromtimestamp(int(udate)).strftime('%Y-%m-%d')
    day = datetime.datetime.fromtimestamp(int(udate)).strftime('%A')
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

    temp_min = int(float(temp_min) - 273.15)
    temp_max = int(float(temp_max) - 273.15)
    temp_morn = int(float(temp_morn) - 273.15)
    temp_day = int(float(temp_day) - 273.15)
    temp_eve = int(float(temp_eve) - 273.15)
    temp_night = int(float(temp_night) - 273.15)

    temp_pressure = int(temp_pressure * 0.75006375541921)

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

    insert(date = date,
           day = day,
           t_morning = temp_morn,
           t_afternoon = temp_day,
           t_evening = temp_eve,
           t_night = temp_night,
           precipitation = weather,
           himidity = temp_humidity,
           pressure = temp_pressure,
           direction_wind = direction_of_the_wind,
           speed_wind = temp_speed_wind,
           cloud = temp_clouds)

    # print('Дата: ', date)
    # print("Утренняя температура: ", type(temp_morn))
    # print("Дневная температура: ", type(temp_day))
    # print("Вечерняя температура: ", type(temp_eve))
    # print("Ночная температура: ", type(temp_night))
    # print("Осадки: ", type(weather))
    # print("Влажность: ", type(temp_humidity))
    # print("Давление: ", type(temp_pressure))
    # print("Направление ветра: ", type(direction_of_the_wind))
    # print("Скорость ветра: ", type(temp_speed_wind))
    # print("Облачность: ", type(temp_clouds))
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


while True:

    token_open_weather_api = constant.token_open_weather_api

    locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
    # locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

    print('Введите город: ')
    # city = 'Новосибирск'
    city = 'Новосибирск'

    print('Какой срок: "Сегодня", "Завтра", "Неделя" или "2 недели"')
    days = '2 недели'.lower()

    temp_address = str('http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city + '&cnt=' + str(
        14) + '&appid=066bdda4bf6b0e5d4d2980b47a95119d')

    response = requests.get(temp_address)

    j = response.json()
    n = 0

    response.close()

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

    print("Расчёт завершён!")

    sleep()
