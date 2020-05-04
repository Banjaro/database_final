-- SCHEMA

CREATE TABLE company
(
    id INT AUTO_INCREMENT,
    company_name VARCHAR(64),
    description VARCHAR(400) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE employee
(
    id INT AUTO_INCREMENT,
    username VARCHAR(64),
    name VARCHAR(64) NOT NULL,
    password_hash VARCHAR(128),
    current_hours INT,
    job_title VARCHAR(64),
    hourly_wage INT NOT NULL,
    employer_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE product
(
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    description VARCHAR(300),
    manf_id INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE works_on
(
    product_id INT,
    employee_id INT,
    PRIMARY KEY (product_id, employee_id)
);


-- ALTER TABLE employee
-- ADD FOREIGN KEY (employer_id)
-- REFERENCES company(id);

-- ALTER TABLE product
-- ADD FOREIGN KEY (manf_id)
-- REFERENCES company(id);

ALTER TABLE works_on
ADD FOREIGN KEY (product_id)
REFERENCES product(id);

ALTER TABLE works_on
ADD FOREIGN KEY (employee_id)
REFERENCES employee(id);


INSERT INTO company(company_name,description) VALUES("Missouri S&T", "Founded in 1870 as one of the first technological institutions west of the Mississippi, we’ve been building on our heritage of discovery, creativity and innovation to equip and inspire today’s students to meet tomorrow’s great global challenges.");
INSERT INTO company(company_name,description) VALUES("Mc. Donalds", "Burgers, burgers, burgers.");
