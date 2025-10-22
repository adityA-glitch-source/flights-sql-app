import streamlit as st
import pandas as pd
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px
db = DB()


st.sidebar.title('Flights Analytics')
user_options = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])


if user_options == 'Check Flights':
    st.title('🔍 Check Flights')

    col1, col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        Source = st.selectbox('Source',sorted(city))
    with col2:
       Destination = st.selectbox('Destination',sorted(city))
    if st.button('Search'):
        results = db.fetch_all_flights(Source, Destination)

        st.dataframe(results)





elif user_options == 'Analytics':
    st.title('📊 Analytics')
    airline,frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


else:
    # Landing / About Page
    st.markdown("<h1 style='text-align:center;'>✈️ Flight Insights App</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:gray;'>Explore Real-Time Flight Data & Analytics</h4>",
                unsafe_allow_html=True)
    st.write("---")

    # Three-column info cards with darker colors
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='background-color:#0288D1; color:white; padding:25px; border-radius:15px; text-align:center'>
            <p style='font-size:50px;'>✈️</p>
            <h3>Explore Flights</h3>
            <p>Access <b>real-time flight data</b> from a <b>live AWS dataset</b>. Select source and destination to view routes, airlines, and dates.</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div style='background-color:#F57C00; color:white; padding:25px; border-radius:15px; text-align:center'>
            <p style='font-size:50px;'>📊</p>
            <h3>Analytics</h3>
            <p>Interactive visualizations:  
            - Airline Share 🛫  
            - Busiest Airports 🏙️  
            - Daily Flight Trends 📅</p>
            </div>
            """, unsafe_allow_html=True)

    with col3:
        st.markdown(
            """
            <div style='background-color:#388E3C; color:white; padding:25px; border-radius:15px; text-align:center'>
            <p style='font-size:50px;'>🛠️</p>
            <h3>Tech Stack</h3>
            <p>Built with <b>Streamlit</b>, <b>Python</b>, and <b>MySQL</b>. Cloud-hosted AWS dataset + interactive visualizations for a smooth experience.</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    st.info("👉 Use the **sidebar** to explore flights or view analytics!")
