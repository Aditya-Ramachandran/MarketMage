import streamlit as st

st.set_page_config(page_title='MarketMage',layout='wide')

st.title('MarketMage')
st.markdown("_Unveiling Market Insights Through Data Magic_")
st.markdown('---')

st.sidebar.title('Navigator')
user_option = st.sidebar.selectbox('Choose One', ('About', 'Analytics'))

if user_option == 'About':
    st.write('About')
else:
    st.write('Analytics')