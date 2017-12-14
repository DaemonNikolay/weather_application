def insert(sql):
    import MySQLdb
    import constant

    conn = MySQLdb.connect(host=constant.host,
                           user=constant.user,
                           passwd=constant.passwd,
                           db=constant.db,
                           charset=constant.charset,
                           init_command=constant.init_command
                           )
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    conn.close()

