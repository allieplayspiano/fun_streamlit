import streamlit as st
import pandas as pd
from PIL import Image
pip install folium

# Set page title and favicon
st.set_page_config(page_title='Dublin Bay Area Guide', page_icon=':mountain:')

import folium

# Create a map centered at Dublin, California
map_dublin = folium.Map(location=[37.7022, -121.9358], zoom_start=12)

# Add a marker at Dublin, California
folium.Marker(location=[37.7022, -121.9358], popup="Dublin, California").add_to(map_dublin)

# Display the map
map_dublin.save("dublin_map.html")
