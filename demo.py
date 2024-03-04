import streamlit as st
import pandas as pd
import json
import csv
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

#connect to Snowflake
#with open('creds.json') as f:
#    connection_parameters = json.load(f)  
#session = Session.builder.configs(connection_parameters).create()

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

#st.title("User Input Demo")
# Text input widget
entered_username = st.text_input("Enter Username:")

#st.title("User Input Demo")
# Text input widget
entered_password = st.text_input("Enter Password:")
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')


# Connection parameters
snowflake_user = entered_username
snowflake_password = entered_password
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

file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
if file is not None:
    file_df = pd.read_csv(file, engine='python', sep=',',  quotechar='"')
    snowparkDf=write_pandas(conn, file_df,file.name,auto_create_table = True, overwrite=True)

    #print(file_df)


# Close the connection
conn.close()    
