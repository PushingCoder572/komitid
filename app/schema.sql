drop table if exists users;
create table users (
    id integer primary key,
    name text not null,
    password text not null
);