import streamlit as st
from data_retriever import DB
from plotter import Plot


db = DB()
plot = Plot()


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

    col1, col2 = st.columns(2)

    if analysis_option == 'Sales Analysis':
        data = db.get_ship_mode_avg_sales()
        plot.plot_pie_chart(data, names='Shipment', values='Avg Sales', title='Pie Chart of Ship Mode and Avg Sales')
        
        data2 = db.get_category_subcategory_profit()
        plot.plot_grouped_bar(data2, x='Category', y='Profit', color='Sub-Category', title='Profit by Category and Sub-Category')

        data3 = db.get_city_state_total_sales()
        plot.plot_bar_chart(data3,y='State', x='Total Sales', title='Sales by State')

        data4 = db.get_region_category_avg_sales()
        plot.plot_grouped_bar(data4,x='Category', y='Avg Sales', color='Region')

        data5 = db.get_avg_sales_per_quantity_segment()
        plot.plot_bar_chart(data5, x='Segment', y='Avg Sales', title='Average Sales Per Quantity')
    

    if analysis_option == 'Profit and Discount Analysis':
        data = db.get_avg_discount_per_segment()
        plot.plot_bar_chart(data, x='Segment', y='Average Discount', title='Average Discount Per Segment')

        data2 = db.get_state_total_profit()
        plot.plot_bar_chart(data2, y='State', x='Total Profit', title='Profit per State')

        data3 = db.get_profit_margin_per_subcategory()
        plot.plot_bar_chart(data3, y='Sub-Category', x='Profit Margin', title='Profit Margin per sub-category')

        data4 = db.get_avg_discount_per_subcategory_furniture()
        plot.plot_bar_chart(data4, y='Sub-Category', x='Avg Discount', title='Average Discount per sub-category')
