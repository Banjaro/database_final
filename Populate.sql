-- UPDATE company
-- SET username ='admin'
-- WHERE cid = 1;

INSERT INTO company(name) VALUES('Sunshine');
INSERT INTO company(name) VALUES('Triggerfish');
INSERT INTO company(name) VALUES('McDonalds');
INSERT INTO company(name) VALUES('Ya Moms House');
INSERT INTO company(name) VALUES('Cheddars');
INSERT INTO company(name) VALUES('China');
INSERT INTO company(name) VALUES('Russia');
SELECT * FROM company;

INSERT INTO account VALUES(1,NULL,'admin','Password',"Admin");
INSERT INTO account VALUES(2,NULL,'admin','admin',"Admin");
INSERT INTO account VALUES(2,NULL,'user','admin',"User");
INSERT INTO account VALUES(3,NULL,'admin','admin',"Admin");
INSERT INTO account VALUES(4,NULL,'admin','admin',"Admin");
INSERT INTO account VALUES(5,NULL,'admin','admin',"Admin");
INSERT INTO account VALUES(6,NULL,'admin','admin',"Admin");
INSERT INTO account VALUES(6,NULL,'user','admin',"User");
SELECT * FROM account;

INSERT INTO employee VALUES(1, 111111111, 'Ryan', 'Copeland', 'Intern', 20);
INSERT INTO employee VALUES(2, 111111111, 'Ryan', 'Copeland', 'Intern', 20);
INSERT INTO employee VALUES(3, 222222222, 'Ronald', 'McDonald', 'Owner', 200);
INSERT INTO employee VALUES(4, 333333333, 'Ya', 'Mum', 'Prostitute', 1);
INSERT INTO employee VALUES(4, 444444444, 'Ya', 'Dad', 'Pimp', 100);
SELECT * FROM employee;

INSERT INTO account VALUES(1,111111111,'Ryan','Password',"Admin");
INSERT INTO account VALUES(2,111111111,'Ryan','Password',"Admin");
INSERT INTO account VALUES(3,222222222,'Ronald','admin',"User");
INSERT INTO account VALUES(4,333333333,'Mom','Password',"User");
INSERT INTO account VALUES(4,444444444,'Dad','Password',"User");
SELECT * FROM account
ORDER BY ssn ASC;

INSERT INTO project(cid, projname) VALUES(1,"Main Project");
SELECT * FROM project;

INSERT INTO assignment(pid, cid, ssn) VALUES (1, 1, 111111111);
SELECT * FROM assignment;

INSERT INTO log(username, time, pid, hours) VALUES ("Ryan", "2020-04-26 18:00:00", 1, 100);
SELECT * FROM log;


DELETE FROM account WHERE cid >= 1;
DELETE FROM company WHERE cid >= 1;