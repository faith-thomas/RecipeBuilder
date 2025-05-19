import streamlit as st

st.title("Recipe Builder")

user_input = st.text_input("List your ingredients here")
st.write("The ingredients you listed are: ", user_input)
