import streamlit as st
from altair import condition

import backend as be
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5, step=1,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))

st.subheader(f"{option} for next {days} days in {place}")

if place:
    try:
        filtered_data = be.get_data(place, days)



        if (option == "Temperature"):
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x" : "Date", "y" : "Temperature"})

            st.plotly_chart(figure)

        if (option == "Sky"):

            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png" }
            sky_type = [dict["weather"][0]["main"] for dict in filtered_data]
            sky_images = [images[condition] for condition in sky_type]
            dates = [dict["dt_txt"] for dict in filtered_data]
            st.image(sky_images, width=75,caption=dates)
    except KeyError:
        st.write("No data to display"
                 "Invalid place selected")