
import streamlit as st
import pandas as pd
import json
import csv
import snowflake.connector

#connect to Snowflake
#with open('creds.json') as f:
#    connection_parameters = json.load(f)  
#session = Session.builder.configs(connection_parameters).create()

# Connection parameters
snowflake_user = "sgupta"
snowflake_password = "snowflakeSg@54321"
snowflake_account = "oyb62571"
snowflake_warehouse = "COMPUTE_WH"
snowflake_database = "STREAMLIT_TEST"
snowflake_schema = "DATA"

# Establish connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)

# Create cursor
cursor = conn.cursor()

file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
if file is not None:
    file_df = pd.read_csv(file, engine='python', sep=',',  quotechar='"')
    snowparkDf=cursor.write_pandas(file_df,file.name,auto_create_table = True, overwrite=True)

    #print(file_df)

# Commit the changes
conn.commit()

# Close the connection
conn.close()    
