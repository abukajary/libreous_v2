CREATE TABLE Cart_Order
( product_id numeric(30) not null,
  book_id numeric(30) not null,
  user_id number(11, 0) not null,
  CONSTRAINT fk_order_books
    FOREIGN KEY (book_id)
    REFERENCES books(id),
    CONSTRAINT fk_order_user
    FOREIGN KEY (user_id)
    REFERENCES auth_user(id),
    total_price numeric(10) null
);
drop table books;
CREATE TABLE books
( id numeric(30) not null,
  book_img varchar(500) null,
  book_name varchar(50) not null,
  book_author numeric(30) not null,
  book_date date,
  book_stars number(5),
  book_price number(20),
  book_description varchar2(500) null,
  CONSTRAINT book_id PRIMARY KEY (id),
    CONSTRAINT fk_author
    FOREIGN KEY (book_author)
    REFERENCES book_authors(id)
);

desc auth_user