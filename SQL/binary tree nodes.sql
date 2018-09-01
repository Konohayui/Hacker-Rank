
select N,
    case when tree.P is null then "Root"
         when (select count(*) from BST sub where sub.P = tree.N) > 0 then "Inner" else "Leaf"
    end
from BST tree
order by N
