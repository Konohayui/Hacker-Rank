select x, y from functions
group by x, y
having count(*) > 1
union all
select a.x, a.y from functions as a
inner join functions as b on ((a.x = b.y and a.y = b.x) and a.x < a.y)
order by x
