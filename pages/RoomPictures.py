import streamlit as st
from PIL import Image

#画像
image = Image.open('./data/inaman.png')
st.image(image, width=600)