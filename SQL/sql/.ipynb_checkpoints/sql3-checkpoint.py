create table category(
   id int PRIMARY_KEY AUTO_INCREMENT,
   category_name varchar(255)

)

create table product(
    id int AUTO_INCREMENT PRIMARY KEY,
    category_id int ,
    FOREIGN KEY (category_id) REFERENCES category(id)

)


insert into category (category_name) values("home")


select * from Students

insert into Students(name) values("umesh")


CREATE TABLE Students(
id int IDENTITY(101, 1) PRIMARY KEY, 
name varchar(255)
);


CREATE TABLE Persons (
    id int NOT NULL,
    age int,
    PRIMARY KEY (id)
);

insert into Persons(age) values(5)


CREATE TABLE Persons (
    id int AUTO_INCREMENT,
    name varchar(255),
    PRIMARY KEY (id)
)


select * from Customers where age between 20 and 25 order by age desc limit 1 offset 1


select * from Products where Price =(select max(Price) from Products)

select * from Products where Price =(select Price from Products order by Price desc limit 1 offset 1)


### Final Quer #####

create table category (
    id int AUTO_INCREMENT,
    name varchar(255),
    PRIMARY key(id)
  )

insert into category(name) VALUES("umesh")



create table product(
  id int AUTO_INCREMENT,
  product_name varchar(255),
  category_id int REFERENCES category(id),
  FOREIGN KEY(category_id)
)



#### primary key and foreign key #####

create table category (
    id int AUTO_INCREMENT,
    name varchar(255),
    PRIMARY key(id)
  )



create table product(
    id int AUTO_INCREMENT,
    category_id int,
    product_name varchar(255),
    PRIMARY KEY(id),
    FOREIGN KEY(category_id) REFERENCES category(id)


)


## Left Join

select category.id,category.name,product.id,product.category_id 
FROM category left join product on category.id = product.category_id;


## inner Join

select category.id,category.name,product.id,product.category_id 
FROM category left join product on category.id = product.category_id;



### Create query  ###

create table employee(
   id int AUTO_INCREMENT,
   name varchar(255),
   salary int,
   PRIMARY KEY(id)

)


#  Only run below query sql server and ms access
SELECT TOP 30 PERCENT * FROM employee
ORDER BY salary DESC;


## Alter table

alter table employee add column post varchar(255)


# Group by

SELECT post,count(post) FROM `employee` GROUP BY post;


# AVG

SELECT AVG(salary) FROM `employee`;

SELECT post,AVG(salary) FROM `employee` GROUP BY post;

SELECT post,AVG(salary) FROM `employee` where salary > 6000 GROUP BY post 


# between

select * from employee WHERE salary BETWEEN 200000 and 400000;


# In operator

select * from employee WHERE salary in(200000,400000);


# Second highest salary

SELECT * FROM `employee` order by salary desc limit 1 offset 1;



Alter table product add COLUMN product_name varchar(255);


https://www.youtube.com/watch?v=0t1b2pfTLVo&list=PLyTI7CpFS6wUgBDEVkSG0guFwunnHZXZ4&index=5




*

