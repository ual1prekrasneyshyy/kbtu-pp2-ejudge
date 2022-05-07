import psycopg2
import csv

contacts = []






def check_if_contact_exists(name: str) -> bool:
    cursor.execute(f'select * from contacts where name=\'{name}\'')

    if_contact_exists = cursor.fetchall()

    return len(if_contact_exists) > 0



connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='ual1prekrasneyshyy',
    database='phone_book_1_2'
)

cursor = connection.cursor()
choice = None


def find_contact_by_id(id: int):
    global contacts

    for contact in contacts:
        if contact[0] == id:
            return contact


while True:
    choice = input('PRESS [1] TO ADD OR UPDATE CONTACT\n'
                   'PRESS [2] TO FIND CONTACTS BY PATTERN\n'
                   'PRESS [3] TO VIEW FIRST 5 CONTACTS\n'
                   'PRESS [4] TO DELETE CONTACT\n'
                   'PRESS [0] TO EXIT\n')

    if choice == '1':
        name = input('Insert name: ')
        phone = input('Insert phone number: ')

        if not check_if_contact_exists(name):
            cursor.execute(f'insert into contacts (name, phone) values (\'{name}\', \'{phone}\')')
        else:
            cursor.execute(f'update contacts set phone=\'{phone}\' where name=\'{name}\'')

        connection.commit()

    elif choice == '2':

        pattern = input('Insert pattern: ')

        cursor.execute(f'select * from contacts where name like \'%{pattern}%\' or phone like \'%{pattern}%\';')

        contacts = cursor.fetchall()

        for c in contacts:
            print(c)


    elif choice == '3':
        cursor.execute(f'select * from contacts limit 5;')
        contacts = cursor.fetchall()

        for c in contacts:
            print(c)

    elif choice == '4':
        name = input(f'Insert name: ')
        if check_if_contact_exists(name):
            cursor.execute(f'delete from contacts where name=\'{name}\'')
            connection.commit()
            print('Contact has successfully been deleted!')
        else:
            print('Error!')

    elif choice == '0':
        break

    print('=' * 120)

# cursor.execute(sql_request)

# contacts = cursor.fetchall()

# print(contacts)

cursor.close()
connection.close()
