import pandas as pd
# buat query
query="""
SELECT * FROM `bigquery-public-data.covid19_jhu_csse_eu.summary`
LIMIT 1000
"""

# baca data dari google big query 
df_covid = pd.read_gbq(query, project_id="XXXXXXXX")
# tampilkan 5 data teratas
print(df_covid.head(5))