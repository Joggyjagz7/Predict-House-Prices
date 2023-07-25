import streamlit as st

st.title('Dream House Predictor')

st.subheader('Upload the Picture of your Dream House and get a predicted price.')

uploaded_file = st.file_uploader("Choose an image")

st.button(label="Upload your House Image ")
