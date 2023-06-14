import streamlit as st
import pandas as pd
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title='Dublin Bay Area Guide', page_icon=':mountain:')

# Load cafe, restaurant, and hike data
cafes_data = pd.read_csv(r'/Users/alfernandez/Documents/cafes.csv')  # Replace 'cafes.csv' with the actual path to your cafes data file
