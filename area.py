import sqlite3
conn = sqlite3.connect("factbook.db")

c = conn.cursor()
query = "select name, sum(area_land), sum(area_water), sum(area_land)/sum(area_water) from facts group by name order by 4;"
c.execute(query)
print(c.fetchall())
