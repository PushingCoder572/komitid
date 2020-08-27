drop table if exists  posts;
    create table users (
        id integer primary key autoincrement,
        name text not null,
        content text not null

);
