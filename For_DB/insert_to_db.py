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
        cursor.execute(
            """UPDATE NOVOSIBIRSK SET `t_Morning`=%s,`t_Afternoon`=%s,  `t_Evening`=%s, `t_Night`=%s, `Precipitation`='%s',`Himidity`=%s, `Pressure`=%s, `Direction_wind`='%s', `Speed_wind`=%f, `Cloud`=%s  WHERE `Date`='%s'""" % (
                date, t_morning, t_afternoon, t_evening, t_night, precipitation, himidity, pressure,
                direction_wind,
                speed_wind,
                cloud))
        conn.commit()

    conn.close()
