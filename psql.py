import psycopg2

connection = psycopg2.connect(database = 'python_sql')

cursor = connection.cursor()


def add_employees(name, email, employer_id):
    cursor.execute('INSERT INTO employees (name, email, employer_id) VALUES (%s, %s, %s)', [name, email, employer_id])
    print('Added employee')
    
def add_company(name, location):
    cursor.execute('INSERT INTO companies (name, location) VALUES (%s, %s)', [name, location])
    print('Added Company')


def menu():
    print('Employee relationship management')
    print('1. Add employee')
    print('2. Show employee')
    print('3. Update employee')
    print('4. Delete employee')
    print('5. Add Company')
    print('6. Show Company')
    print('7. Update Company')
    print('8. Delete Company')
    print('9. Employee Company relation')
    print('10. Exit')
menu()  

choice = input('Select command ')

if choice == '1':
    name = input('Enter name: ')
    email = input('Enter email: ')
    employer_id = input('Enter company id: ')
    add_employees(name, email, employer_id)
elif choice == '2':
    employees_table = 'employees'
    # cursor.execute(f'''
    #     SELECT column_name, data_type, is_nullable, character_maximum_length, 
    #     column_default
    #         FROM information_schema.columns
    #         WHERE table_name = %s
    #         ''', (employees_table,))
    # table_prop = cursor.fetchall()

    # print("Table Properties:")
    # for column in table_prop:
    #     print(f"Name: {column[0]}, Type: {column[1]}, Nullable: {column[2]}, Max Length: {column[3]}, Default: {column[4]}")
# Fetch and display table data
    cursor.execute(f"SELECT * FROM {employees_table};")
    employee_data = cursor.fetchall()
    print("\nTable Data:")
    for row in employee_data:
        print(row)
elif choice == '3':
    print('choice 3')
elif choice == '4':
    print('choice 4')
elif choice == '5':
    name = input('Company name: ')
    location = input('Company location: ')
    add_company(name, location)
elif choice == '6':
    companies_table = 'companies'
    # cursor.execute(f'''
    #     SELECT column_name, data_type, is_nullable, character_maximum_length, 
    #     column_default
    #         FROM information_schema.columns
    #         WHERE table_name = %s
    #         ''', (employees_table,))
    # table_prop = cursor.fetchall()

    # print("Table Properties:")
    # for column in table_prop:
    #     print(f"Name: {column[0]}, Type: {column[1]}, Nullable: {column[2]}, Max Length: {column[3]}, Default: {column[4]}")
# Fetch and display table data
    cursor.execute(f"SELECT * FROM {companies_table};")
    company_data = cursor.fetchall()
    print("\nTable Data:")
    for row in company_data:
        print(row)
elif choice == '7':
    print('choice 7')
elif choice == '8':
    print('choice 8')
elif choice == '9':
    cursor.execute('SELECT * FROM employees JOIN companies on employees.employer_id = companies.id')
    combined_data = cursor.fetchall()
    print("\nRelationship Table Data:")
    for row in combined_data:
        print(row)
elif choice == '10':
    print('EXIT, LEAVE NOW >:(')
else:
    print('Invalid response')
    
    


connection.commit()

# cursor.execute('')


connection.close()