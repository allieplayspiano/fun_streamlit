import streamlit as st

st.set_page_config(page_title="Welcome to the Dublin Office!", page_icon=":tada:", layout="wide")
st.title("Allison's 6 Month Mark :tada:")
st.subheader("Always learning, always striving, always delivering")
st.write("[Check out my LinkedIn Here>](https://www.linkedin.com/in/allison-fernandez-9519b095/)")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I've been working on")
    st.write("##")
    st.write("""
    Completed: Workday <> Financial Force PTO Integration
    - Automating the creation of PTO assignments within Financial Force in order free up to 25% of time per week for Resource Delivery Managers. (Current process takes 5-10 hours per RDM). 
   
    Phase I of II Complete: Rebillable Expenses Automation 
    Go-Live: July 13, 2023
    - Automatically syncing expenses submitted/approved in Workday for PS Engagements into Financial Force for billing, saving up to 8 hours a month for the PS Operations Team 

    """)
