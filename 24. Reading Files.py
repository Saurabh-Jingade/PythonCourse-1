employee_file = open("Text file for reading in python.txt", "r" )
for employee in employee_file.readlines():
    print (employee)

employee_file.close()