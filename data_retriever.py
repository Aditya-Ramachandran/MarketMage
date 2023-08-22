import mysql.connector
import pandas as pd
import streamlit as st

class DB:
    def __init__(self):
    # connecting to the server
        try: 
            self.conn = mysql.connector.connect(
                host = '127.0.0.1', 
                user = "root",
                password =""
            )
            self.mycursor = self.conn.cursor()
            print('Connection Established!')
        except: 
            print('Connection Failed')