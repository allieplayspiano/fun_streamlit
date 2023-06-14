import streamlit as st

st.set_page_config(page_title="Welcome to the Dublin Office!", page_icon=":tada:", layout="wide")
st.title("Welcome to the Dublin Office! :tada:")
st.header("Hi, I'm Allison!")
st.subheader("We are so excited to have you here :wave:")
st.write("I'm your friendly BSA from the GTM-Applications team. Come swing by anytime if you have a question!")
st.write("[Learn More about Snowflake here>](https://www.snowflake.com/en/)")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I've been working on")
    st.write("Status reporting, Billable Events, EDU Case Management and so much more!")
