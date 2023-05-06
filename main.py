import streamlit as st

st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days: ", min_value=1, max_value=5,
                 help="Select a number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

