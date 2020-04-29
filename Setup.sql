-- SCHEMA

CREATE TABLE company
(
    cid INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY(cid)
);

CREATE TABLE employee
(
    cid INT,
    ssn INT(9),
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40),
    job_title VARCHAR(40),
    wage DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (cid, ssn)
);

CREATE TABLE account
(
    cid INT,
    ssn INT(9),
    username VARCHAR(20),
    pass VARCHAR(30),
    role VARCHAR(10),
    PRIMARY KEY(cid, username)
);


CREATE TABLE project
(
    cid INT,
    projname VARCHAR(40) NOT NULL,
    pid INT AUTO_INCREMENT,
    PRIMARY KEY (pid)
);

CREATE TABLE log
(
    log_id INT AUTO_INCREMENT,
    username VARCHAR(20),
    time TIMESTAMP,
    pid INT,
    hours INT,
    PRIMARY KEY (log_id)
);

CREATE TABLE assignment
(
    pid INT,
    cid INT,
    ssn INT(9),
    PRIMARY KEY (pid, cid, ssn)
);


ALTER TABLE employee
ADD FOREIGN KEY (cid)
REFERENCES company(cid);


ALTER TABLE account
ADD FOREIGN KEY (cid)
REFERENCES company(cid);


ALTER TABLE log
ADD FOREIGN KEY (pid)
REFERENCES project(pid);

ALTER TABLE assignment
ADD FOREIGN KEY (pid)
REFERENCES project(pid);




-- DROP TABLE log;
-- DROP TABLE project;
-- DROP TABLE account;
-- DROP TABLE employee;
-- DROP TABLE company;




