select repeat('* ', @numbers:= @numbers + 1)
from information_schema.tables, (select @numbers:= 0) as t limit 20
