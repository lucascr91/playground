CREATE TABLE workers (id INT, name VARCHAR(100), sex VARCHAR(100), age VARCHAR(100));
INSERT INTO workers (id,name,sex,age)
VALUES (1,"W. White","male",54);
INSERT INTO workers (id,name,sex,age)
VALUES (2,"Hank Schroder","male",51);
INSERT INTO workers (id,name,sex,age)
VALUES (2,"Gus Fring","male",50);
INSERT INTO workers (id,name,sex,age)
VALUES (1,"Skyler","male",44);

CREATE TABLE firms (id INT, name VARCHAR(100), capital INT);
INSERT INTO firms (id,name,capital)
VALUES (1,"Bank Warburg",13051);
INSERT INTO firms (id,name,capital)
VALUES (2,"Atlas Security Information",42094);

MERGE firms AS TARGET
USING workers AS SOURCE 
ON (TARGET.id = SOURCE.id) 

-- SELECT * FROM workers;
-- SELECT * FROM workers WHERE id IN (SELECT id FROM firms);

DROP TABLE firms;
DROP TABLE workers;