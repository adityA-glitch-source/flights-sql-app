import streamlit as st
st.sidebar.title('Flights Analytics')
user_options = st.sidebar.selectbox('Menu',['select one','check flights','Analytics'])
if user_options == 'check flights':
    st.title('check Flights')
elif user_options == 'Analytics':
    st.title('Analytics')
else:
    pass