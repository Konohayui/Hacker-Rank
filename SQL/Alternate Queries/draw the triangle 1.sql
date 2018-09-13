select repeat('* ', @numbers:= @numbers - 1)
from information_schema.tables, (select @numbers:= 21) as t limit 20
