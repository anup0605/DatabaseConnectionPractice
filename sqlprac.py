import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", database="sql_practice", password="mysql0605",
                              use_pure=True)
    print(mydb.is_connected())

    query = "show databases"

    cursor = mydb.cursor()
    cursor.execute(query)
    fetchData = cursor.fetchall()
    for result in fetchData:
        print(result)

    print("query execution done")
    mydb.close()
except Exception as e:
    print(str(e))
