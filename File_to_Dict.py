employee_file = open("employee.txt", "a+") 
employee_dict = {}

choice = str(input("Want to add more names: Y/N: ")).strip().upper()
updated_choice = (choice == 'Y')

while updated_choice:
    name = str(input('Enter the name and profession you want to add to the file: '))
    employee_file.write('\n' + name + '\n')
    choice = str(input("Want to add more names: Y/N: ")).strip().upper()
    updated_choice = (choice == 'Y')

employee_file.seek(0)

for employee in employee_file:
    employee.strip() # to remove blank spaces
    if employee:
        parts = employee.split(maxsplit=1) # maxsplit only splits to the frist space ex Tanishq ML Engineer ---> ['Tanishq', 'ML Engineer']

        if len(parts) == 2: # it checks if the parts contain to strings or not 
            name , profession = parts 
            employee_dict[name] = profession.strip().lstrip('-').strip()

print(employee_dict)

employee_file.close()
