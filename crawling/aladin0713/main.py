import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             port=3307,
                             user='root',
                             password='1234',
                             database='baemin',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `user_tb`"
        cursor.execute(sql)
        result = cursor.fetchall()
        for re in result:
            print(re["user_name"])