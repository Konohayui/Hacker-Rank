select ct.contest_id, ct.hacker_id, ct.name,
        sum(total_submissions) as total_submissions,
        sum(total_accepted_submissions) as total_accepted_submissions,
        sum(total_views) as total_views,
        sum(total_unique_views) as total_unique_views
from contests as ct
left join colleges as co on co.contest_id = ct.contest_id
left join challenges as ch on ch.college_id = co.college_id
left join (select challenge_id, sum(total_views) as total_views, 
                  sum(total_unique_views) as total_unique_views
            from view_stats
            group by challenge_id) as vs
    on vs.challenge_id = ch.challenge_id
left join (select challenge_id, sum(total_submissions) as total_submissions,
                sum(total_accepted_submissions) as total_accepted_submissions
            from submission_stats
            group by challenge_id) as ss
    on ss.challenge_id = ch.challenge_id
group by ct.contest_id, ct.hacker_id, ct.name
having (total_submissions + total_accepted_submissions + total_views + total_unique_views) > 0
order by ct.contest_id

