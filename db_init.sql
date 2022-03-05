CREATE DATABASE whatabook;


CREATE USER 'whatabook_user'@'localhost'

    IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';


CREATE TABLE stores (store_id    INT    NOT NULL

    ,PRIMARY KEY (store_id)

    ,locale    VARCHAR (500)    NOT NULL);


CREATE TABLE books (book_id    INT    NOT NULL    AUTO_INCREMENT

    ,PRIMARY KEY (book_id)

    ,book_name    VARCHAR (200)    NOT NULL

    ,details    VARCHAR (500)

    ,author    VARCHAR (200)    NOT NULL

    );


CREATE TABLE users (user_id    INT    NOT NULL    AUTO_INCREMENT

    ,PRIMARY KEY (user_id)

    ,first_name    VARCHAR (75)    NOT NULL

    ,last_name    VARCHAR (75)    NOT NULL

    );


CREATE TABLE wishlists (wishlist_id    INT    NOT NULL    AUTO_INCREMENT

    ,PRIMARY KEY (wishlist_id)

    ,user_id    INT    NOT NULL

    ,FOREIGN KEY (user_id)

        REFERENCES users (user_id)

    ,book_id    INT    NOT NULL

    ,FOREIGN KEY (book_id)

        REFERENCES books (book_id)

    );


INSERT INTO stores (store_id, locale)

    VALUES (1, '27 Main St, Plymouth, NH, 03264');


INSERT INTO books (book_id, book_name, author)

    VALUES (1, 'Great Tales of Horror', 'H.P. Lovecraft')

    ,(2, 'The Fifth Elephant', 'Terry Pratchett')

    ,(3, 'Perfect Shadow', 'Brent Weeks')

    ,(4, 'The Alienist', 'Caleb Carr')

    ,(5, 'When We Were Orphans', 'Kazuo Ishiguro')

    ,(6, 'Songmaster', 'Orson Scott Card')

    ,(7, 'A Game of Thrones', 'George R.R. Martin')

    ,(8, 'The Four Agreements', 'Don Miguel Ruiz')

    ,(9, 'Frankenstein', 'Mary Shelley')

    ;


INSERT INTO users (user_id, first_name, last_name)

    VALUES (1, 'Roose', 'Brillis')

    ,(2, 'Jimothy', 'Jones')

    ,(3, 'Quonathan', 'Quimby')

    ;


INSERT INTO wishlists (wishlist_id, user_id, book_id)

    VALUES (1, 1, 3)

    ,(2, 2, 6)

    ,(3, 3, 9)

    ;