from main import create_tables
from sql_app.crud import get_or_create_character
from sql_app.crud import get_or_create_superpower
from sql_app.session import SessionLocal


create_tables()
db = SessionLocal()

c1 = get_or_create_character(db, "Tonyn", "Stallone")
c2 = get_or_create_character(db, "Arnaldor", "Shuatseneguer")

get_or_create_superpower(db, "Taladoken", 3, "DSDP", c1)
get_or_create_superpower(db, "Remuyuken", 2, "SDK", c1)
get_or_create_superpower(db, "Remuyuken", 3, "SAK", c2)
get_or_create_superpower(db, "Taladoken", 3, "ASAP", c2)
