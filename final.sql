create table employees(id number, emp_name varchar2(50), emp_email varchar2(50), constraint country_id primary key(id));
desc BIN$4Pn/1cEhQNy5S0SWAsp43A==$0

select * from book_authors







select * from BIN$4Pn/1cEhQNy5S0SWAsp43A==$0

select * from tab

drop table books

create table book_authors(
id number,
author_name varchar2(50),
author_surname varchar2(50),
PRIMARY KEY (id) 
);

create table books(
id number,
book_img varchar(500),
book_name varchar(50),
book_author_id number,
book_date date,
book_stars number,
CONSTRAINT fk_bookAutor
    FOREIGN KEY (book_author_id)
    REFERENCES book_authors(id)
);

grant all privileges to djangoxe;
commit;


select * from USER_ROLE_PRIVS where USERNAME='djangoxe';
select * from USER_TAB_PRIVS where Grantee = 'djangoxe';
select * from USER_SYS_PRIVS where USERNAME = 'djangoxe';

SELECT * FROM USER_SYS_PRIVS; 
SELECT * FROM USER_TAB_PRIVS; 
SELECT * FROM USER_ROLE_PRIVS;

ALTER SESSION SET CURRENT_SCHEMA=djangoxe
