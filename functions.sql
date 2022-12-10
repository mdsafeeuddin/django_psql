SELECT UPPER(first_name)
FROM employees;

SELECT LENGTH(first_name), LOWER(department)
FROM employees;

SELECT '     HELLO THERE	    ';

SELECT TRIM('    HELLO THERE     ');

SELECT LENGTH(TRIM('    HELLO THERE     '));

SELECT first_name || last_name
FROM employees;

SELECT first_name ||' '|| last_name full_name
FROM employees;

SELECT first_name ||' '|| last_name full_name, (salary > 140000) is_highly_paid
FROM employees
ORDER BY salary desc;

SELECT department, ('Clothing' IN (department, first_name))
FROM employees;

