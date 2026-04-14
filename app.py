import streamlit as st
import numpy as np

st.title("Text Display and Dice Roll App")

text = st.text_input("Enter some text", "Hello World")

st.write(f"# {text}")

if st.button("Roll a dice!"):
    roll = np.random.randint(1, 9)
    st.write(f"Dice roll: {roll}")