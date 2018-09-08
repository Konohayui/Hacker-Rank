select first, last from 
    (select a.start_date as first, min(b.end_date) as last 
    from 
    (select start_date from projects where start_date not in (select end_date from projects)) as a,
    (select end_date from projects where end_date not in (select start_date from projects)) as b
    where a.start_date < b.end_date
    group by a.start_date) as duration
order by datediff(last, first), first
