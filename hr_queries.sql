--Final Project
--#1
Create View EmployeesPerRegion AS
Select r.region_name, COUNT(e.employee_id) AS "Number of Employees"
From regions r, countries c, locations l, departments d, employees e
Where e.department_id = d.department_id AND d.location_id = l.location_id AND l.country_id = c.country_id AND c.region_id =r.region_id
Group By r.region_name;

--#1a
Select *
From EmployeesPerRegion
Where region_name = "Americas";

--#2
Create View managers AS
Select e.first_name, e.last_name, e.phone_number, e.email, j.job_title, d.department_name
From employees e, jobs j, departments d
Where j.job_id = e.job_id AND e.department_id = d.department_id AND j.job_title LIKE "%Manager%"
Group By e.employee_id;

--#2a
Select department_name, COUNT(first_name) "Number of Managers"
From managers
Group By department_name;

--#3
Create View DependentsByDepartment AS
Select da.department_name, COUNT(de.dependent_id) AS "dependents"
From employees e, dependents de, departments da
Where de.employee_id = e.employee_id AND e.department_id = da.department_id
Group By da.department_id;

--#3a
Select *
From DependentsByDepartment
Order By dependents DESC
Limit 1;

--#4
Create View HiresByYear AS
Select YEAR(hire_date) AS "hire_date", COUNT(employee_id) AS "hires"
From employees
Group By YEAR(hire_date);

--#4a
Select *
From HiresByYear
Where hire_date = 1997;

--#5
Create View SalaryByDepartment AS
Select d.department_name, SUM(e.salary) AS "salary"
From departments d, employees e
Where d.department_id = e.department_id 
Group By d.department_name;

--#5a
Select *
From SalaryByDepartment
Where department_name = "Finance"; 

--#6
Create View SalaryByJobTitle AS
Select j.job_title, SUM(e.salary) as "salary"
From jobs j, employees e
Where j.job_id = e.job_id
Group By j.job_title;

--#6a
Select *
From SalaryByJobTitle
Order By salary DESC
Limit 1;

--#7
Create View EmployeeDependents AS
Select e.first_name, e.last_name, e.email, e.phone_number, COUNT(d.dependent_id) AS "dependents"
From employees e
Left Join dependents d ON e.employee_id = d.employee_id
Group By e.employee_id;

--#7a
Select *
From EmployeeDependents
Where dependents = 0;

--#8
Create View CountryLocation AS
Select c.country_name, COUNT(l.location_id) AS "locations"
From countries c
Left Join locations l ON c.country_id = l.country_id
Group By c.country_name;

--#8a
Select *
From CountryLocation
Where locations = 0;