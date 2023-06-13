import streamlit as st
import pandas as pd
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title='Dublin Bay Area Guide', page_icon=':mountain:')

# Load cafe, restaurant, and hike data
cafes_data = pd.read_csv('cafes.csv')  # Replace 'cafes.csv' with the actual path to your cafes data file
restaurants_data = pd.read_csv('restaurants.csv')  # Replace 'restaurants.csv' with the actual path to your restaurants data file
hikes_data = pd.read_csv('hikes.csv')  # Replace 'hikes.csv' with the actual path to your hikes data file

# Load images
cafe_image = Image.open('cafe_image.jpg')  # Replace 'cafe_image.jpg' with the actual path to your cafe image
restaurant_image = Image.open('restaurant_image.jpg')  # Replace 'restaurant_image.jpg' with the actual path to your restaurant image
hike_image = Image.open('hike_image.jpg')  # Replace 'hike_image.jpg' with the actual path to your hike image

# Create sidebar selection
selected_category = st.sidebar.selectbox('Select Category', ('Cafes', 'Restaurants', 'Hikes'))

if selected_category == 'Cafes':
    st.image(cafe_image, use_column_width=True)
    st.header('Cafes in Dublin Bay Area')
    st.dataframe(cafes_data)

elif selected_category == 'Restaurants':
    st.image(restaurant_image, use_column_width=True)
    st.header('Restaurants in Dublin Bay Area')
    st.dataframe(restaurants_data)

elif selected_category == 'Hikes':
    st.image(hike_image, use_column_width=True)
    st.header('Hikes in Dublin Bay Area')
    st.dataframe(hikes_data)
