/*Create the summary view to include the results for all the tables*/
create view pop_summary as (
SELECT 
    birth_group.year,
    birth_group.district_code,
    birth_group.district_name,
    birth_group.neigbhor_code,
    birth_group.neigbhor_name,
    birth_group.number AS birth_number,
    death_group.number AS death_number,
    population_group.number AS total_num
FROM
	/*Group the birth table by year, district and neigbhor*/
    /*Take grouped data as the new birth_group table*/
    (SELECT 
        birth.year,
            birth.district_code,
            birth.district_name,
            birth.neigbhor_code,
            birth.neigbhor_name,
            SUM(birth.number) AS number
    FROM
        birth
    GROUP BY birth.year , birth.district_code , birth.district_name , birth.neigbhor_code , birth.neigbhor_name) birth_group,
	/*Group the death table by year, district and neigbhor*/
    /*Take the grouped data as the new death table*/
    (SELECT 
        death.year,
            death.district_code,
            death.district_name,
            death.neigbhor_code,
            death.neigbhor_name,
            SUM(death.number) AS number
    FROM
        death
    GROUP BY death.year , death.district_code , death.district_name , death.neigbhor_code , death.neigbhor_name) death_group,
	/*Group the population table by year, district and neigbhor*/
    /*Take the grouped data as the new population table*/
    (SELECT 
        population.year,
            population.district_code,
            population.district_name,
            population.neigbhor_code,
            population.neigbhor_name,
            SUM(population.number) AS number
    FROM
        population
    GROUP BY population.year , population.district_code , population.district_name , population.neigbhor_code , population.neigbhor_name) population_group
WHERE
    birth_group.district_code = death_group.district_code
        AND birth_group.neigbhor_code = death_group.neigbhor_code
        AND birth_group.year = death_group.year
        AND population_group.district_code = birth_group.district_code
        AND population_group.neigbhor_code = birth_group.neigbhor_code
        AND population_group.year = birth_group.year
);
