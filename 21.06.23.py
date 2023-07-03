import psycopg2

#TODO берет данные из БД и записывает в текстовый файл
def func_one():
    file_path = 'data.txt'
    connection = psycopg2.connect(dbname="hw", host="localhost", user="postgres", password="Asnk1101lk", port="5432")
    cursor = connection.cursor()

    query = "SELECT column1, column2, column3, column4 FROM my_table"
    cursor.execute(query)
    rows = cursor.fetchall()

    with open(file_path, 'w') as file:
        for row in rows:
            line = ';'.join(str(value) for value in row) + '\n'
            file.write(line)

    cursor.close()
    connection.close()

#TODO берает данные из текстового файла и отправлять в БД

def func_two():
    file_path = 'hw.txt'
    connection = psycopg2.connect(dbname="hw", host="localhost", user="postgres", password="Asnk1101lk", port="5432")
    cursor = connection.cursor()

    with open(file_path, 'r') as file:
       cursor.copy_from(file, 'my_table', sep=';')

# Применение изменений
    connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    #func_one()
    func_two()

