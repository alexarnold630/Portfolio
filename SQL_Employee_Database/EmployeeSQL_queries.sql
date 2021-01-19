-DATA ANALYSIS--

SELECT * FROM "Departments";
SELECT * FROM "Dept_Emp";
SELECT * FROM "Dept_Manager";
SELECT * FROM "Employees";
SELECT * FROM "Salaries";
SELECT * FROM "Titles";

--1. List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM "Employees" as e 
JOIN "Salaries" as s ON e.emp_no = s.emp_no;
;

--2. List first name, last name, and hire date for employees who were hired in 1986.
SELECT first_name, last_name, hire_date
FROM "Employees"
WHERE hire_date BETWEEN '01-01-1986' AND '01-01-1987'
ORDER BY hire_date asc
;

--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
SELECT d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name
FROM "Dept_Manager" as dm
JOIN "Departments" as d on dm.dept_no = d.dept_no
JOIN "Employees" as e on dm.emp_no = e.emp_no
ORDER BY dept_no asc, e.last_name asc

--4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM "Dept_Emp" as de
JOIN "Employees" as e ON de.emp_no = e.emp_no
JOIN "Departments" as d ON de.dept_no = d.dept_no
ORDER BY e.emp_no asc

--5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name, last_name, sex
FROM "Employees"
WHERE first_name = 'Hercules' AND last_name like 'B%'
ORDER BY last_name asc
;

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT de.emp_no, e.last_name, e.first_name, d.dept_name
FROM "Dept_Emp" as de
JOIN "Employees" as e ON de.emp_no = e.emp_no
JOIN "Departments" as d ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Sales'
ORDER BY e.last_name asc
;

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM "Dept_Emp" as de
JOIN "Employees" as e ON de.emp_no = e.emp_no
JOIN "Departments" as d ON de.dept_no = d.dept_no
ORDER BY d.dept_name, e.last_name asc

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, count(*) as name_count
FROM "Employees"
GROUP BY last_name
ORDER BY name_count desc
	