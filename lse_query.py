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

query2 = """
SELECT TICode, AVG(TradePrice) AS AvgPrice 
FROM trade_reports 
GROUP BY TICode 
ORDER BY AvgPrice DESC;
"""

cursor.execute(query2)
avg_price = cursor.fetchone() # [i] here chooses the column, i = 1 here because we have chopped the line into size of 2

query3 = """
SELECT * FROM trade_reports 
ORDER BY TradeDate DESC, TradeTime DESC 
LIMIT 1;
"""

cursor.execute(query3)
last_trade = cursor.fetchone()[0]


print(f"Total Cancelled Orders: {cancelled_orders}")
print(f"Average Trade Price: {avg_price}")
print(f"Last Trade Message Sequence Number: {last_trade}")


cursor.close()
conn.close()