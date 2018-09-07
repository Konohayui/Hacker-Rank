select h.hacker_id, h.name
from submissions as s
join challenges as c on c.challenge_id = s.challenge_id
join hackers as h on h.hacker_id = s.hacker_id
join difficulty as d on d.difficulty_level = c.difficulty_level
where s.score = d.score
group by h.hacker_id, h.name
having count(h.hacker_id) > 1
order by count(h.hacker_id) desc, h.hacker_id asc
