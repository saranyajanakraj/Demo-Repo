import sys
#import psycopg2
import redshift_connector

conn = redshift_connector.connect(
        host="redshift-cluster-1.cjtsvnr1c5fa.ap-south-1.redshift.amazonaws.com",
        database="dev",
        user="awsuser",
        password="Awsadmin1")

cur = conn.cursor()
print('connected')
cur.execute("select * from category")
rows = cur.fetchall()
print(rows)

conn.close()
