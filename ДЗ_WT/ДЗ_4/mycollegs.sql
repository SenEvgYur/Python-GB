-- create
CREATE TABLE MYCOLLEGS (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  adress TEXT NOT NULL
);

-- insert
INSERT INTO MYCOLLEGS VALUES (0001, 'Иванов Иван', 35, 'Москва');
INSERT INTO MYCOLLEGS VALUES (0002, 'Миронова Мария', 28, 'Калининград');
INSERT INTO MYCOLLEGS VALUES (0003, 'Сидоров Александр', 30, 'Новосибирск');
INSERT INTO MYCOLLEGS VALUES (0004, 'Ковалева Ольга', 31, 'Владивосток');
INSERT INTO MYCOLLEGS VALUES (0005, 'Павлов Константин', 40, 'Екатеринбург');

-- fetch 
SELECT * FROM MYCOLLEGS
