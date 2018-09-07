select h.hacker_id, h.name, sum(m.score) as total
from (select hacker_id, challenge_id, max(score) as score from submissions
     group by hacker_id, challenge_id) as m
join hackers as h on h.hacker_id = m.hacker_id
group by h.hacker_id, h.name
having total > 0
order by total desc, h.hacker_id asc 
