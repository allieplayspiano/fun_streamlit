import streamlit as st

st.set_page_config(page_title="Welcome to the Dublin Office!", page_icon=":tada:", layout="wide")
st.title("Allison's 6 Month Mark :woman_office_worker:")
st.subheader("Always learning, always striving, always delivering")
st.write("[Check out my LinkedIn Here>](https://www.linkedin.com/in/allison-fernandez-9519b095/)")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I've been working on")
    st.write("Status reporting, Billable Events, EDU Case Management and so much more!")
