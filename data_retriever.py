import mysql.connector
import pandas as pd
import streamlit as st

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user="root",
                password=""
            )
            self.mycursor = self.conn.cursor()
            print('Connection Established!')
        except:
            print('Connection Failed')

    def get_ship_mode_avg_sales(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
        SELECT `Ship Mode` ,AVG(Sales) FROM store_data
        GROUP BY `Ship Mode`
        ORDER BY AVG(Sales) DESC;
    """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data.rename(columns={0:'Shipment',1:'Avg Sales'}, inplace=True)
        return data
    
    def get_category_subcategory_profit(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT Category, `Sub-Category`, MAX(Profit) AS MaxProfit
            FROM store_data
            GROUP BY Category, `Sub-Category`
            ORDER BY MaxProfit DESC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data.rename(columns={0:'Category', 1:'Sub-Category', 2:'Profit'}, inplace=True)
        return data
    
    def get_city_state_total_sales(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT State, ROUND(SUM(Sales),2) 
            FROM store_data
            GROUP BY State
            ORDER BY SUM(Sales) ASC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data.rename(columns={0:'State', 1:'Total Sales'},inplace=True)
        return data
    
    def get_region_category_avg_sales(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT Region, Category, AVG(Sales)
            FROM store_data
            GROUP BY Region, Category
            ORDER BY AVG(Sales) DESC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Region', 1:'Category', 2:'Avg Sales'})
        return data
    
    def get_avg_sales_per_quantity_segment(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT Segment, AVG(Sales / Quantity)
            FROM store_data
            GROUP BY Segment;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Segment', 1:'Avg Sales'})
        return data