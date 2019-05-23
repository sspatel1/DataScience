create view umployment_data as (
SELECT 
    u.year,
    u.district_code,
    u.district_name,
    u.neigbhor_code,
    u.neigbhor_name,
    SUM(u.number)
FROM
    unemployment u
GROUP BY u.year , u.district_code , u.district_name , u.neigbhor_code , u.neigbhor_name
order by u.year , u.district_code , u.neigbhor_code
);