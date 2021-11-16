CREATE USER user_name WITH PASSWORD 'default_password';
alter role user_name set client_encoding to 'utf8';
alter role user_name set default_transaction_isolation to 'read committed';
alter role user_name set timezone to 'UTC';
create database stockf_db owner user_name;
\c db_stockf;