import sqlite3
#print (dir(sqlite3))
conn = sqlite3.connect("modcom.db")
c = conn.cursor()
# Create table

c.execute('''CREATE TABLE stock
             (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
c.execute("INSERT INTO stock VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
conn.commit()
for row in c.execute('SELECT * FROM stock ORDER BY price'):
        print(row)