import mysql.connector
import pandas as pd
# membuat koneksi ke db financial di https://relational.fit.cvut.cz/dataset/Financial
my_conn = mysql.connector.connect(host="relational.fit.cvut.cz",
                                  port=3306,
                                  user="guest",
                                  passwd="relational",
                                  database="financial",
                                  use_pure=True)

# buatlah query sql untuk membaca tabel loan
my_query = """
SELECT * FROM loan
"""

# gunakanlah .read_sql_query untuk membaca tabel load
df_loan = pd.read_sql_query(my_query, my_conn)
# tampilkan 5 data teratas 
print(df_loan.head(5)) 