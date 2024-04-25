# Personal Blog

This is the backend of the personal blog project. The project is created using Django.

## Configuration

---

### Database

Database is created on *PostgreSQL* in *version 16*, but it should work with 
other versions as well.

1. Edit pg_hba.conf file:

    [Download PostgreSQL](https://www.postgresql.org/download/)
    
    In order to avoid you need to edit the file *pg_hba.conf* in the PostgreSQL root directory.

    - Windows: `C:\Program Files\PostgreSQL\16\data\pg_hba.conf`
    - Linux: `/etc/postgresql/16/main/pg_hba.conf`
    - MacOS: `/Library/PostgreSQL/16/data/pg_hba.conf`
   
    At the end of the file, modify the column METHOD by adding trust instead of scram-sha-256 or md5 as follows:

    ```
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    # "local" is for Unix domain socket connections only
    local   all             all                                     trust
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            trust
    # IPv6 local connections:
    host    all             all             ::1/128                 trust
    # Allow replication connections from localhost, by a user with the
    # replication privilege.
    local   replication     all                                     trust
    host    replication     all             127.0.0.1/32            trust
    host    replication     all             ::1/128                 trust
    ```

2. Restart PostgreSQL service:

    - Windows: `services.msc`
    - Linux: `sudo service postgresql restart`
    - MacOS: `sudo service postgresql restart`

3. Create role and database: 

    1. Open *psql* terminal.
    2. Create role with password using following command:
        ```sql
        CREATE ROLE admin_blog WITH LOGIN ENCRYPTED PASSWORD 'yamaha321';
        ```
    3. Create database using following command:
        ```sql
        CREATE DATABASE blog_db WITH OWNER admin_blog;
        ```
    4. Grant all privileges to the role:
        ```sql
        GRANT ALL PRIVILEGES ON DATABASE blog_db TO admin_blog;
        ```
    5. Exit the terminal:
        ```sql
        \q
        ```

---

### Run Project

---