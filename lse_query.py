import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="Vedant1711",  
    database="lse_high_freq"
)

cursor = conn.cursor()

query = "SELECT COUNT(*) FROM order_history WHERE OrderActionType = 'D';"
cursor.execute(query)
cancelled_orders = cursor.fetchone()[0]

print(f"Total Cancelled Orders: {cancelled_orders}")

cursor.close()
conn.close()