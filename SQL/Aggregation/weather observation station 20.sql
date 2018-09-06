select round(s1.lat_n, 4) from station s1, station s2
group by s1.lat_n
having sum(sign(1-sign(s2.lat_n - s1.lat_n))) = (count(*) + 1)/2

-- SELECT x.val from data x, data y
-- GROUP BY x.val
-- HAVING SUM(SIGN(1-SIGN(y.val-x.val))) = (COUNT(*)+1)/2
