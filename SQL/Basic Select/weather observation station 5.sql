
select city, length(city) as len from station order by len asc, city limit 1;
select city, length(city) as len from station order by len desc, city limit 1;
