import streamlit as st
import pandas as pd
import json
import csv
#from snowflake.snowpark import Session


#st.write('Hello World!')
#connect to Snowflake
with open('creds.json') as f:
    connection_parameters = json.load(f)  
session = Session.builder.configs(connection_parameters).create()

file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
if file is not None:
    file_df = pd.read_csv(file, engine='python', sep=',',  quotechar='"')
    snowparkDf=session.write_pandas(file_df,file.name,auto_create_table = True, overwrite=True)
