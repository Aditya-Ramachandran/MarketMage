import streamlit as st
from data_retriever import DB


db = DB()


st.set_page_config(page_title='MarketMage',layout='wide')

st.title('MarketMage')
st.markdown("_Unveiling Market Insights Through Data Magic_")
st.markdown('---')

st.sidebar.title('Navigator')
user_option = st.sidebar.selectbox('Choose One', ('About', 'Analytics'))

if user_option == 'About':
    st.write('About')
else:
    analysis_option = st.sidebar.radio('Choose Type of Analysis', ('Sales Analysis', 'Profit and Discount Analysis', 'Segment and Mode Analysis','Yearly Analysis'))

    if analysis_option == 'Sales Analysis':
        db.get_ship_mode_avg_sales()
        db.get_category_subcategory_profit()
        db.get_city_state_total_sales()
        db.get_region_category_avg_sales()
        db.get_avg_sales_per_quantity_segment()
