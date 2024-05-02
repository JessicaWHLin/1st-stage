## Task 2: Create database and table in your MySQL server
#### 2.1 Create a new database named website.
- ```
  CREATE DATABASE website;
  ```
  ![sth wrong](image/task2_1.png)
#### 2.2 Create a new table named member, in the website database
- ``` 
  create table website.member(
    -> id bigint auto_increment primary key,
    -> name varchar(255) not null,
    -> username varchar(255) not null,
    -> password varchar(255) not null,
    -> follower_count int unsigned not null default 0,
    -> time datetime not null default current_timestamp
    -> );
    ```
  ![sth wrong](image/task2_2.png)
---
## Task 3 : SQL CRUD
#### 3.1 INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
- ``` 
  insert into website.member(name,username,password)values('test','test','test'); 

  insert into website.member(name,username,password)values
  -> ('Lily','lily','lily123'),
  -> ('Amy','amy','amy123'),
  -> ('John','john','john123'),
  -> ('Kelly','kelly','kelly123');
  ```
  ![sth wrong](image/task3_1_1.png)
  ![sth wrong](image/task3_1_2.png)
#### 3.2 SELECT all rows from the member table.
- ```
  select * from website.member;
  ```
  ![sth wrong](image/task3_2.png)
#### 3.3 SELECT all rows from the member table, in descending order of time.
- ```
  select * from website.member
    -> order by time desc;
  ```
  ![sth wrong](image/task3_3.png)
#### 3.4 SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
- ```
   select * from website.member order by time desc limit 3 offset 1;
   ```
  ![sth wrong](image/task3_4.png)
#### 3.5 SELECT rows where username equals to test.
- ```
  select * from website.member
    -> where username = 'test';
  ```
  ![sth wrong](image/task3_5.png)
#### 3.6 SELECT rows where name includes the es keyword.
- ```
   select * from website.member where name like '%es%';
   ```
  ![sth wrong](image/task3_6.png)
#### 3.7 SELECT rows where both username and password equal to test.
- ```
   select * from website.member where username = 'test' and password = 'test';
   ```
  ![sth wrong](image/task3_7.png)
#### 3.8 UPDATE data in name column to test2 where username equals to test.
- ```
  update website.member
    -> set name = 'test2'
    -> where username= 'test';
  ```
  ![sth wrong](image/task3_8.png)
---
## Task 4 : SQL Aggregation Functions
#### 4.1 SELECT how many rows from the member table.
- ```
   select count(*)
    -> from website.member;
  ```
  ![sth wrong](image/task4_1.png)
#### 4.2 SELECT the sum of follower_count of all the rows from the member table.
- ```
  select sum(follower_count) from website.member;
  ```
  ![sth wrong](image/task4_2.png)
#### 4.3 SELECT the average of follower_count of all the rows from the member table.
- ```
   select avg(follower_count) from website.member;
  ```
  ![sth wrong](image/task4_3.png)
#### 4.4 SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
- ```
   select avg(follower_count)
    -> from(
    -> select follower_count
    -> from website.member
    -> order by follower_count desc
    -> limit 2
    -> ) as subquery;
    ```
  ![sth wrong](image/task4_4_1.png)
  ![sth wrong](image/task4_4_2.png)
---
## Task 5 : SQL JOIN
####  5.1 Create a new table named message, in the website database.
- ```
   create table website.message(
    -> id bigint auto_increment primary key,
    -> member_id bigint not null,
    -> foreign key(member_id) references member(id),
    -> content varchar(255) not null,
    -> like_count int unsigned not null default 0,
    -> time datetime not null default current_timestamp
    -> );
    ```
  ![sth wrong](image/task5_1.png)
#### 5.2 SELECT all messages, including sender names. We have to JOIN the member table to get that.
- ```
   select message.*, member.name as sender_name
    -> from website.message
    -> join website.member on message.member_id = member.id;
    ```
  ![sth wrong](image/task5_2_1.png)
  ![sth wrong](image/task5_2_2.png)
####  5.3 SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
- ```
  select message.*, member.name as sender_name
    -> from website.message
    -> join website.member on message.member_id = member.id
    -> where member.username = 'test';
    ```
  ![sth wrong](image/task5_3.png)
####  5.4 Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
- ```
   select avg(message.like_count) as avg_like_count
    -> from website.message
    -> join website.member on message.member_id = member.id
    -> where member.username = 'test';
    ```
  ![sth wrong](image/task5_4.png)
####  5.5 Use SELECT, SQL Aggregation Functions with JOIN, get the average like count of messages GROUP BY sender username.
- ```
  select avg(message.like_count) as avg_like_count, member.username
    -> from website.message
    -> join website.member on message.member_id = member.id
    -> group by member.username;
    ```
  ![sth wrong](image/task5_5.png)