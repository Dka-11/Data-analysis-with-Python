# Text Input
import streamlit as st
# ===================
# == Input Widgets ==
# ===================

name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama', name)

# Text Area Input
text = st.text_area('Feedback')
st.write('Feedback : ', text)

# Number Input
number = st.number_input(label='umur')
st.write('Umur: ', int(number), 'tahun')

# Date Input
import datetime

date = st.date_input(label="Tanggal Lahir", min_value=datetime.date(1900,1,1))

st.write('Tanggal Lahir:',date)

# File Upload
import pandas as pd

uploaded_file = st.file_uploader('Choose a CSV file')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
# Camera Input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)
    
# ====================
# == Button Widgets ==
# ====================

# Button
if st.button('Say hello'):
    st.write('Hello there')
    
# Check box
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')
    
# Radio Button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

# Select Box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Multi select
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Slider
