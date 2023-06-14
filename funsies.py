import streamlit as st
import pandas as pd
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title='Dublin Bay Area Guide', page_icon=':mountain:')

image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')
