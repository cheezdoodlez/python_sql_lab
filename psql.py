import psycopg2

connection = psycopg2.connect(database = 'python_sql')

cursor = connection.cursor()


def add_employees(name, email, employer_id):
    cursor.execute('INSERT INTO employees (name, email, employer_id) VALUES (%s, %s, %s)', [name, email, employer_id])
    print('Added employee')
    
def update_employee():
    cursor.execute('UPDATE employees SET name = %s, email = %s, employer_id = %s WHERE id = %s', [update_name, update_email, update_employer_id, update_employee_id])
    print ('Employee updated')
    
def add_company(name, location):
    cursor.execute('INSERT INTO companies (name, location) VALUES (%s, %s)', [name, location])
    print('Added Company')

def update_company():
    cursor.execute('UPDATE companies SET name = %s, location = %s WHERE id = %s', [update_name, update_location, update_company_id])
    print ('Company updated')
    


def menu():
    print('Employee relationship management')
    print('1. Add employee')
    print('2. Show employees')
    print('3. Update employee')
    print('4. Delete employee')
    print('5. Add Company')
    print('6. Show Companies')
    print('7. Update Company')
    print('8. Delete Company')
    print('9. Employee Company relation')
    print('10. Exit')
menu()  

choice = input('Select command ')

if choice == '1':
    employer_id = input('Enter company id: ')
    name = input('Enter name: ')
    email = input('Enter email: ')
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
    employees_table = 'employees'
    cursor.execute(f"SELECT * FROM {employees_table};")
    employee_data = cursor.fetchall()
    print("\nTable Data:")
    for row in employee_data:
        print(row)
    update_employee_id = input('Select employee id: (First number shown) ')
    cursor.execute('SELECT id FROM employees WHERE id = %s',[update_employee_id])
    update_name = input('Enter name: ')
    update_email = input('Enter email: ')
    update_employer_id = input('Select employer id: ')
    update_employee()
elif choice == '4':
    employees_table = 'employees'
    cursor.execute(f"SELECT * FROM {employees_table};")
    employee_data = cursor.fetchall()
    print("\nTable Data:")
    for row in employee_data:
        print(row)
    employee_id = input('Select employee id to delete: (First number shown)')
    cursor.execute('DELETE FROM employees WHERE id = %s', [employee_id])
    print('Employee deleted')
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
    companies_table = 'companies'
    cursor.execute(f"SELECT * FROM {companies_table};")
    company_data = cursor.fetchall()
    print("\nTable Data:")
    for row in company_data:
        print(row)
    update_company_id = input('Select company id: (First number shown) ')
    cursor.execute('SELECT id FROM companies WHERE id = %s',[update_company_id])
    update_name = input('Enter name: ')
    update_location = input('Enter location: ')
    update_company()
elif choice == '8':
    companies_table = 'companies'
    cursor.execute(f"SELECT * FROM {companies_table};")
    company_data = cursor.fetchall()
    print("\nTable Data:")
    for row in company_data:
        print(row)
    company_id = input('Select company id to delete: (First number shown) ')
    cursor.execute('DELETE FROM companies WHERE id = %s', [company_id])
    print('Company deleted')
elif choice == '9':
    cursor.execute('SELECT * FROM employees JOIN companies on employees.employer_id = companies.id')
    combined_data = cursor.fetchall()
    print("\nRelationship Table Data:")
    for row in combined_data:
        print(row)
elif choice == '10':
    print('EXIT, LEAVE NOW >:(')
    # connection.close()
else:
    print('Invalid response, please run again')
    
    


connection.commit()

# cursor.execute('')


connection.close()