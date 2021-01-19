# Employee Database: A Mystery in Two Parts

## Background
Conduct a research project on employees of the corporation from the 1980s and 1990s. All that remain of the database of employees from that period are six CSV files.

Design the tables to hold data in the CSVs, import the CSVs into a SQL database, and answer questions about the data. In other words perform:
1. Data Modeling
2. Data Engineering
3. Data Analysis

## Objectives

### Data Modeling
Inspect the CSVs and sketch out an ERD of the tables.

![ERD Diagram](QuickDBD-EmployeeSQL.png)

### Data Engineering
- Use the information to create a table schema for each of the six CSV files. Remember to specify data types, primary keys, foreign keys, and other constraints.
- Import each CSV file into the corresponding SQL table. 

### Data Analysis
Once there is a complete database, do the following:
1. List the following details of each employee: employee number, last name, first name, sex, and salary.
1. List first name, last name, and hire date for employees who were hired in 1986.
1. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
1. List the department of each employee with the following information: employee number, last name, first name, and department name.
1. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
1. List all employees in the Sales department, including their employee number, last name, first name, and department name.
1. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
1. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
