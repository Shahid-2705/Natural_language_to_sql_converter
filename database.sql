CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    city VARCHAR(50)
);

INSERT INTO employees (id, name, department, salary, city) VALUES
(1, 'Alice Smith', 'HR', 60000, 'New York'),
(2, 'Bob Johnson', 'Engineering', 80000, 'San Francisco'),
(3, 'Charlie Brown', 'Sales', 55000, 'Chicago'),
(4, 'David Lee', 'Marketing', 65000, 'Los Angeles'),
(5, 'Eve Wilson', 'Engineering', 85000, 'Seattle'),
(6, 'Frank Miller', 'Sales', 52000, 'Boston'),
(7, 'Grace Davis', 'HR', 62000, 'Austin'),
(8, 'Hank Moore', 'Engineering', 78000, 'Denver'),
(9, 'Ivy Taylor', 'Marketing', 67000, 'Miami'),
(10, 'Jack White', 'Sales', 54000, 'Phoenix'),
(11, 'Liam Scott', 'Engineering', 90000, 'San Jose'),
(12, 'Mia Green', 'HR', 61000, 'Atlanta');
