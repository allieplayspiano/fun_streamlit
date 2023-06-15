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
   
    Phase I of II Complete: Rebillable Expenses Automation \n
    Go-Live: July 13, 2023
    - Automatically syncing expenses submitted/approved in Workday for PS Engagements into Financial Force for billing, saving up to 8 hours a month for the PS Operations Team 

    In Flight: Billable Events
    - Eliminating the manual back-and-forth reconciliation process at month end to ultimately create Billable Events that will be picked up in the SnowBridge integration.

    In Flight: Status Reporting \n
    Potential Snow-on-Snow Use Case
    - Integrating disparate data sources (FinancialForce, Snowhouse, Tableau, etc) in order to automatically generate status reports for PS Engagements, which will ultimately save up to 3 hours/week per RSA in order to free up more time for engagements.

    In Flight: PS and EDU Case Management
    - While there is a standardized process for EDU case management, it lacks maturity. PS doesn’t have a current process for logging cases for customers. This project will standardize and streamline the PS and EDU Case Management process to increase time to resolution and increase Customer Satisfaction.

    """)
    with right_column: 
      image_path = "Users/alfernandez/Desktop/worker.jpeg"
      
