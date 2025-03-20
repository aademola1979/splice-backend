from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import table, column, select, text
my_table = table("my_table", column("x"), column("y"))
insert_stmt = insert(my_table).values(x="foo")
insert_stmt = insert_stmt.on_conflict_do_nothing(index_elements=["y"])
print(insert_stmt)
our_table = select(text('namem, dabce FROM user' ))
print(our_table)

from sqlalchemy.dialects import postgresql
print(insert_stmt.compile(dialect=postgresql.dialect()))