import streamlit as st
import pandas as pd
import help

df = pd.read_csv('hospitals.csv')
gdf = pd.read_csv('GovernmentSchemes.csv', encoding='windows-1252')

st.sidebar.image(
    '16.jpg')
user_menu = st.sidebar.radio(
    'Search for',
    ('Hospitals in state', 'Hospitals in city', 'Pincode','All government schemes','Government schemes in State')
)

if user_menu == 'Hospitals in state':
    st.sidebar.header('State')
    state = help.search_state(df)

    selected_state = st.sidebar.selectbox("Select state", state)

    statewise_hospitals = help.fetch_state_hospital(df, selected_state)
    st.title("Hospitals in " + selected_state)
    st.table(statewise_hospitals)

if user_menu == 'Hospitals in city':
    st.sidebar.header('City')
    city = help.search_city(df)

    selected_city = st.sidebar.selectbox("Select state", city)

    citywise_hospitals = help.fetch_city_hospital(df, selected_city)
    st.title("Hospitals in " + selected_city)
    st.table(citywise_hospitals)

if user_menu == 'Pincode':
    st.sidebar.header('Pincode')
    pin = help.search_pincode(df)

    selected_pincode = st.sidebar.selectbox("Select Pincode", pin)

    pin_hospitals = help.fetch_pin_hospital(df, selected_pincode)
    st.title("Hospitals with area pincode " + str(int(selected_pincode)))
    st.table(pin_hospitals[['State','City','Hospital']])

if user_menu == 'All government schemes':
    st.sidebar.header('All government schemes in India')
    allGS = help.search_allgs(gdf)

    allGovschemes = help.fetch_all_govschemes(gdf)
    st.title("All the government schemes in India")
    st.table(allGovschemes[['State','Scheme','Details','Eligibility','Website/Apply at']])

if user_menu == 'Government schemes in State':
    st.sidebar.header('Government schemes')
    sgs = help.search_stategs(gdf)

    selected_stategs = st.sidebar.selectbox("Select state", sgs)

    statewise_gs = help.fetch_state_gs(gdf, selected_stategs)
    st.title("Government schemes in " + selected_stategs)
    st.table(statewise_gs[['Scheme','Details','Eligibility','Website/Apply at']])