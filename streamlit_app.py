import streamlit as st
import pandas as pd


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = pd.read_json("datas.json", lines=True)
st.write(df)