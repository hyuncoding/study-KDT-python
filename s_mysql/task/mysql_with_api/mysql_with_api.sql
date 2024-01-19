use test;

create table tbl_member(
    email varchar(255) primary key,
    password varchar(255) not null,
    name varchar(255) not null,
    phone varchar(255) not null
);

select * from tbl_member;
commit;

create table tbl_product(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    price int default 0,
    created_date datetime
);

select * from tbl_product;


insert into tbl_product(name, price, created_date)
values ('키보드', 15000, '2024-01-17T17:22:00');

insert into tbl_product(name, price, created_date)
values ('자두', 500, '2024-01-17T17:22:00');

insert into tbl_product(name, price, created_date)
values ('바나나', 3000, '2024-01-17T17:22:00');

insert into tbl_product(name, price, created_date)
values ('수박', 5000, '2024-01-17T17:22:00');

insert into tbl_product(name, price, created_date)
values ('모니터', 33000, '2024-01-17T17:22:00');

insert into tbl_product(name, price, created_date)
values ('키보드', 15000, '2024-01-17T17:22:00');

insert into tbl_member(email, password, name, phone)
values('hds1234@gmail.com', '1234', '한동석', '01012341234');

insert into tbl_member(email, password, name, phone)
values('hyunstwolte@gmail.com', '1234', '양현', '01050119661');

insert into tbl_member(email, password, name, phone)
values('iki980411@naver.com', '1234', '조관익', '01039690009');

insert into tbl_member(email, password, name, phone)
values('soo982181@naver.com', '1234', '김수빈', '01087203796');


select * from tbl_member;

create table tbl_translation(
    id bigint auto_increment primary key,
    original_message varchar(255) not null,
    translated_message varchar(255) not null,
    created_date datetime default current_timestamp
);

create table tbl_image(
    id bigint auto_increment primary key,
    image_name varchar(255) not null,
    image_text varchar(255) not null,
    created_date datetime default current_timestamp
);

select * from tbl_image;

