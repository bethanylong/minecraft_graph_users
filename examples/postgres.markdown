Postgres example
----------------

```
CREATE ROLE mc_stats WITH LOGIN ENCRYPTED PASSWORD 'choose_a_better_password_than_this';
CREATE DATABASE mc_stats WITH OWNER mc_stats;
\c mc_stats
CREATE TABLE clients (id SERIAL, date timestamp default now(), number integer NOT NULL);
GRANT INSERT,SELECT ON clients TO mc_stats;
GRANT UPDATE ON clients_id_seq TO mc_stats;
CREATE ROLE mc_stats_frontend WITH LOGIN ENCRYPTED PASSWORD 'exercise_your_creativity';
GRANT SELECT ON clients TO mc_stats_frontend;
```
