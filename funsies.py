import streamlit
streamlit.header('Welcome to Dublin!')
giphy_logo_url = "https://media.giphy.com/media/bmQBu3aSF0DxadphkG/giphy.gif"
# giphy_logo_url = "/Users/alenka/Downloads/Logo_GIF1.gif"
logo_html = f'<img src="{giphy_logo_url}" alt="GIPHY Logo" width="200">'
st.markdown(logo_html, unsafe_allow_html=True)
#st.markdown(logo_html, unsafe_allow_html=True)

#logo_image = "/Users/alenka/Downloads/Logo2.png"
#st.sidebar.image(logo_html, width=100)
