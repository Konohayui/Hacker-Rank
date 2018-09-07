select h.hacker_id, h.name, count(c.challenge_id) as total
from hackers as h
join challenges as c on c.hacker_id = h.hacker_id
group by h.hacker_id, h.name
having total = 
            (select count(c2.challenge_id) as c_count from challenges as c2 
             group by c2.hacker_id 
             order by c_count desc
             limit 1)
    or total in (select distinct total2 from 
                (select h2.hacker_id, h2.name, count(c2.challenge_id) as total2
                from hackers as h2
                join challenges as c2 on h2.hacker_id = c2.hacker_id
                group by h2.hacker_id, h2.name) as total_count
            group by total2
            having count(total2) = 1)
order by total desc, h.hacker_id
