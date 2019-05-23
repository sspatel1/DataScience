/*Create table queries*/
CREATE TABLE birth (
    year INT,
    district_code INT,
    district_name TEXT,
    neigbhor_code INT,
    neigbhor_name TEXT,
    gender TEXT,
    number INT,
    age TEXT
);

CREATE TABLE death (
    year INT,
    district_code INT,
    district_name TEXT,
    neigbhor_code INT,
    neigbhor_name TEXT,
    age TEXT,
    number INT
);

CREATE TABLE population (
    year INT,
    district_code INT,
    district_name TEXT,
    neigbhor_code INT,
    neigbhor_name TEXT,
    gender TEXT,
    age TEXT,
    number INT
);

CREATE TABLE unemployment (
    year INT,
    district_code INT,
    district_name TEXT,
    neigbhor_code INT,
    neigbhor_name TEXT,
    number INT
);
