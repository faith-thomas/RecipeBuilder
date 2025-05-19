import streamlit as st

st.title("Recipe Builder")

user_input = st.text_input("List your ingredients here")


if user_input:
    st.write("The ingredients you listed are: ", user_input)
    
    st.subheader("Choose your style of recipe!")
    user_input2 = st.text_input("Pick a style that you want to create with your ingredients")
    
    if user_input2:
        st.write("The style you choose is: ", user_input2)
    

