import streamlit as st
import backend as be
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5, step=1,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))

st.subheader(f"{option} for next {days} days in {place}")

be.get_data(place, days, option)


dates = ['2025-01-01', '2025-01-02', '2025-01-03']
temperatures = [10, 20, 30]

figure = px.line(x=dates, y=temperatures, labels={"x" : "Date", "y" : "Temperature"})

st.plotly_chart(figure)
