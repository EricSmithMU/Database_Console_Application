#query ClassicModels database - November 9, 2021
import mysql.connector

def print_menu():
    print(" _________________ ")
    print("|   SQL Queries   |")
    print("|    Main Menu    |")
    print("|_________________|")
    print(" -Choose an option-")
    print("1. Get Number of Employees in The Americas")
    print("2. Get Number of Managers per Department")
    print("3. Get the Department With the Most Dependents")
    print("4. Get the Number of Hires From 1997")
    print("5. Get the Total Salary for the Finance Department")
    print("6. Get the Job Title With the Highest Salary")
    print("7. Get Information of Employees With No Children")
    print("8. Get Countries With No Locations")
    print("9. Exit Application")
    return

def get_user_choice():
    print_menu()
    choice = int(input("Enter Choice: "))
    return choice

def get_employees_per_region(mycursor):
    #create query
    sql_query = "Select * From EmployeesPerRegion Where region_name = 'Americas';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nRegion: {record[0]} | Number of Employees: {record[1]}\n")
    
    return


def get_managers(mycursor):
    #create query
    sql_query = "Select department_name, COUNT(first_name) 'Number of Managers' From managers Group By department_name;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nDapartment: {record[0]} | Number of Managers: {record[1]}\n")
    
    return


def get_dependents_by_department(mycursor):
    #create query
    sql_query = "Select * From DependentsByDepartment Order By dependents DESC Limit 1;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nDapartment: {record[0]} | Number of Dependents: {record[1]}\n")
    
    return


def get_hires_by_year(mycursor):
    #create query
    sql_query = "Select * From HiresByYear Where hire_date = 1997;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nYear: {record[0]} | Number of Hires: {record[1]}\n")
    
    return


def get_salary_by_department(mycursor):
    #create query
    sql_query = "Select * From SalaryByDepartment Where department_name = 'Finance';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nDepartment: {record[0]} | Salary Total: {record[1]}\n")
    
    return


def get_salary_by_job_title(mycursor):
    #create query
    sql_query = "Select * From SalaryByJobTitle Order By salary DESC Limit 1;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nJob Title: {record[0]} | Salary: {record[1]}\n")
    
    return


def get_employee_dependents(mycursor):
    #create query
    sql_query = "Select * From EmployeeDependents Where dependents = 0;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nName: {record[0]} {record[1]} | Email: {record[2]} | Phone: {record[3]} | Number of Dependents: {record[4]}\n")
    
    return


def get_country_location(mycursor):
    #create query
    sql_query = "Select * From CountryLocation Where locations = 0;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print(f"\nCountry: {record[0]} | Number of Locations: {record[1]}\n")
    
    return



def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="finalproject"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):
        try:
            user_choice = get_user_choice()
            if(user_choice == 1):
                get_employees_per_region(mycursor)
            elif(user_choice == 2):
                get_managers(mycursor)
            elif(user_choice == 3):
                get_dependents_by_department(mycursor)
            elif(user_choice == 4):
                get_hires_by_year(mycursor)
            elif(user_choice == 5):
                get_salary_by_department(mycursor)
            elif(user_choice == 6):
                get_salary_by_job_title(mycursor)
            elif(user_choice == 7):
                get_employee_dependents(mycursor)
            elif(user_choice == 8):
                get_country_location(mycursor)       
            elif(user_choice == 9):
                print("Bye Bye!!!")
                break
            else:
                print("Please Enter A Valid Option ( 1 - 9 )")
        except Exception as err:
            print("Please Enter A Valid Option ( 1 - 9 )")

main()