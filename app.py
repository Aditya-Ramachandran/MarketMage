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

    st.header('About')
    st.write('Meet MarketMage: Your personal supermarket sales analyzer. This mini project employs Python and SQL to offer a real-time snapshot of sales trends, profit margins, and regional patterns across a variety of store locations. The app\'s intuitive interface transforms raw data into actionable insights, making it a valuable tool for swift decision-making. Dive into the world of business analysis with MarketMage, where data-driven insights are just a click away.')

    st.write('MarketMage is a small yet impactful project that fuses Python and SQL to fetch and process real-time data from different supermarket branches. This combination of technical tools allows MarketMage to uncover valuable insights from the data, revealing sales trends and profit margins. The user-friendly interface makes it easy to explore these insights, with the added visual flair provided by Plotly\'s visualizations.')
    st.write('Looking ahead, MarketMage could even evolve to include predictive features for smarter restocking decisions, showcasing its potential to provide practical support beyond its current scope.')

    st.subheader('Data Flow and Visualization')
    st.write('- MarketMage\'s data flow is designed for efficiency, beginning with SQL queries to fetch sales data from diverse store locations stored in a MySQL database.')
    st.write('- Python takes charge of data manipulation and processing, transforming raw information into valuable insights.')
    st.write('- The processed data is dynamically visualized using Plotly, creating interactive charts that showcase sales trends, profit margins, and regional patterns.')
    st.write('- This seamless interface empowers users to effortlessly explore and glean insights from the data, enhancing decision-making for supermarket operations.')

else:
    analysis_option = st.sidebar.radio('Choose Type of Analysis', ('Sales Analysis', 'Profit and Discount Analysis', 'Segment and Mode Analysis'))

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

    if analysis_option == 'Segment and Mode Analysis':
        data = db.get_segment_highest_avg_quantity_sold()
        plot.plot_bar_chart(data, x = 'Segment', y='Avg Quantity', title='Avg Quantity Sold per Segment')

        data2 = db.get_top_5_common_ship_modes()
        plot.plot_pie_chart(data2, names='Ship Mode', values='Count', title='Common Shipping Modes')

        data3 = db.get_segment_lowest_avg_discount()
        plot.plot_bar_chart(data3, x='Segment', y='Avg Discount', title='Average Discounts Across Segments')

        data4 = db.get_avg_sales_per_quantity_per_segment()
        plot.plot_pie_chart(data4, names='Segment', values='Sales', title='Average Sales Per Quantity')
