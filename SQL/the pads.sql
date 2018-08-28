select concat(Name, '(', left(occupation, 1) ,')') as name_with_occ 
from occupations order by name_with_occ;

select concat('There are a total of ', count(occupation), ' ', lower(occupation), 's.') 
from occupations group by occupation
order by count(occupation), occupation;

