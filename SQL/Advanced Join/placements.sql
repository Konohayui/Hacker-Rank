select s.name from students as s
join friends as f on s.id = f.id
join packages as p1 on p1.id = s.id
join packages as p2 on p2.id = f.friend_id
where p1.salary < p2.salary
order by p2.salary
