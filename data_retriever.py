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
    
    def get_avg_discount_per_segment(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT Segment, ROUND(AVG(Discount),2)
            FROM store_data
            GROUP BY Segment
            ORDER BY AVG(Discount) DESC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Segment', 1:"Average Discount"})
        return data
    
    def get_state_total_profit(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT State, SUM(Profit)
            FROM store_data
            GROUP BY State
            ORDER BY SUM(Profit) ASC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data =data.rename(columns={0:'State', 1:'Total Profit'})
        return data
    
    def get_profit_margin_per_subcategory(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT `Sub-Category`, SUM(Profit)/SUM(Sales)
            FROM store_data
            GROUP BY `Sub-Category`
            ORDER BY SUM(Profit)/SUM(Sales) DESC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Sub-Category', 1:'Profit Margin'})
        return data
    
    def get_avg_discount_per_subcategory_furniture(self):
        self.mycursor.execute('USE store')
        self.mycursor.execute("""
            SELECT `Sub-Category`, AVG(Discount)
            FROM store_data
            WHERE Category = 'Furniture'
            GROUP BY `Sub-Category`
            ORDER BY AVG(Discount);
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Sub-Category', 1:'Avg Discount'})
        return data
    
    def get_subcategory_highest_avg_discount(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT `Sub-Category`, AVG(Discount)
            FROM store_data
            GROUP BY `Sub-Category`
            ORDER BY AVG(Discount) DESC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Sub-Category', 1:'Avg Discount'})
        return data
    
    def get_segment_highest_avg_quantity_sold(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT Segment, AVG(Quantity)
            FROM store_data
            GROUP BY Segment
            ORDER BY AVG(Quantity) DESC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Segment', 1:'Avg Quantity'})
        return data

    def get_top_5_common_ship_modes(self):
        self.mycursor.execute('USE store')
        self.mycursor.execute("""
            SELECT `Ship Mode`, COUNT(*)
            FROM store_data
            GROUP BY `Ship Mode`
            ORDER BY COUNT(*) DESC LIMIT 5;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Ship Mode', 1:'Count'})
        return data

    def get_segment_lowest_avg_discount(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT Segment, AVG(Discount)
            FROM store_data
            GROUP BY Segment 
            ORDER BY AVG(Discount) ASC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Segment', 1:'Avg Discount'})
        return data

    def get_avg_sales_per_quantity_per_segment(self):
        self.mycursor.execute("USE store")
        self.mycursor.execute("""
            SELECT Segment, AVG(Sales/Quantity)
            FROM store_data
            GROUP BY Segment
            ORDER BY AVG(Sales/Quantity) DESC;
        """)
        data = self.mycursor.fetchall()
        data = pd.DataFrame(data)
        data = data.rename(columns={0:'Segment', 1:"Sales"})
        return data