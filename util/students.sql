create table students(
    ID INT PRIMARY KEY NOT NULL UNIQUE,
    f_name varchar(25) NOT NULL,
    l_name varchar(25) NOT NULL,
    birthday date
);

Insert into students values (01, 'Chris', 'Hedrick', '0990-03-29');
Insert into students values (02, 'John', 'Doe', '1996-05-28');
Insert into students values (03, 'Jane', 'Crocker', '1996-10-01');
