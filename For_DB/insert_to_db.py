def insert(date, day, t_morning, t_afternoon, t_evening, t_night, precipitation, himidity, pressure, direction_wind,
           speed_wind, cloud):
    import pymysql
    import constant

    conn = pymysql.connect(host = constant.host,
                           user = constant.user,
                           passwd = constant.passwd,
                           db = constant.db,
                           charset = constant.charset,
                           init_command = constant.init_command
                           )
    cursor = conn.cursor()

    try:
        cursor.execute("""INSERT INTO NOVOSIBIRSK (`Date`, `day`, `t_Morning`,`t_Afternoon`,  `t_Evening`, `t_Night`, `Precipitation`,`Himidity`, `Pressure`, `Direction_wind`, `Speed_wind`, `Cloud` )
                    VALUES ('%s', '%s', %d, %d, %d, %d, '%s', %d, %d, '%s', %f, %d)""" % (
            date, day, t_morning, t_afternoon, t_evening, t_night, precipitation, himidity, pressure, direction_wind,
            speed_wind, cloud))
        conn.commit()
    except:

        # print(type(date))
        # print(type(t_morning))
        # print(type(t_afternoon))
        # print(type(t_evening))
        # print(type(t_night))
        # print(type(precipitation))
        # print(type(himidity))
        # print(type(pressure))
        # print(type(direction_wind))
        # print(type(speed_wind))
        # print(type(cloud))

        cursor.execute(
            """UPDATE NOVOSIBIRSK SET `t_Morning`=%d,`t_Afternoon`=%d,  `t_Evening`=%d, `t_Night`=%d, `Precipitation`='%s',`Himidity`=%d, `Pressure`='%s', `Direction_wind`='%s', `Speed_wind`=%f, `Cloud`='%s'  WHERE `Date`='%s'""" % (
                t_morning, t_afternoon, t_evening, t_night, precipitation, himidity, pressure,
                direction_wind,
                speed_wind,
                cloud, date))
        conn.commit()

    conn.close()
