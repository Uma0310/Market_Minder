#Descriptio : This is stock market dashboeard to
# to show some data and stock price

#import libraries

import streamlit as st
import pandas as  pd
from PIL import Image

#add a Title and image
st.write("""
#Stock Market Web Application 
Visually show data from 2018-11-13 to 2023-11-12
""")

image = Image.open("./PROJECT/Image6.jpg")
st.image(image, use_column_width=True)

#create a sidebar header
st.sidebar.header('User Input')

#create a function to get the users input
def get_input():
    start_date= st.sidebar.text_input("Start Date","2018-11-13")
    end_date= st.sidebar.text_input("End Date","2023-11-12")
    stock_symbol= st.sidebar.text_input("Stock Symbol", "MARUTI")
    return start_date,end_date,stock_symbol

#Create a function to get the company name
def get_company_name(symbol):
    if symbol == 'MARUTI':
        return 'MARUTI'
    elif symbol == 'ASIANPAINT':
        return 'ASIANPAINT'
    elif symbol == 'BAJAJ-AUTO':
        return 'BAJAJ-AUTO'
    elif symbol == 'BHARTIARTL':
        return 'BHARTIARTL'
    elif symbol == 'HDFCBANK':
        return 'HDFCBANK'
    elif symbol == 'ICICIBANK':
        return 'ICICIBANK'
    elif symbol == 'INFY':
        return 'INFY'
    elif symbol == 'ITC':
        return 'ITC'
    elif symbol == 'KOTAKBANK':
        return 'KOTAKBANK'
    elif symbol == 'NESTLEIND':
        return 'NESTLEIND'
    elif symbol == 'POWERGRID':
        return 'POWERGRID'
    elif symbol == 'PVR':
        return 'PVR'
    elif symbol == 'RELIANCE':
        return 'RELIANCE'
    elif symbol == 'SBIN':
        return 'SBIN'
    elif symbol == 'TATAMOTORS':
        return 'TATAMOTORS'
    elif symbol == 'ULTRACEMCO':
        return 'ULTRACEMCO'
    elif symbol == 'TCS':
        return 'TCS'
    elif symbol == 'WIPRO':
        return 'WIPRO'
    elif symbol == 'LT':
        return 'LT'
    elif symbol == 'SUZLON':
        return 'SUZLON'
    
    

    else:
        'None'

#create a fun to get the company data and proper timeframe form users strt and end date
def get_data(symbol, start,end):

    #Load the data
    if symbol.upper() == 'MARUTI':
        df=pd.read_csv("./PROJECT/MARUTI.csv")
    elif symbol.upper() == 'ASIANPAINT':
        df=pd.read_csv("./PROJECT/ASIANPAINT.csv")
    elif symbol.upper() == 'BHARTIARTL':
        df=pd.read_csv("./PROJECT/BHARTIARTL.csv")
    elif symbol.upper() == 'HDFCBANK':
        df=pd.read_csv("./PROJECT/HDFCBANK.csv")
    elif symbol.upper() == 'ICICIBANK':
        df=pd.read_csv("./PROJECT/ICICIBANK.csv")
    elif symbol.upper() == 'INFY':
        df=pd.read_csv("./PROJECT/INFY.csv")
    elif symbol.upper() == 'ITC':
        df=pd.read_csv("./PROJECT/ITC.csv")
    elif symbol.upper() == 'KOTAKBANK':
        df=pd.read_csv("./PROJECT/KOTAKBANK.csv")
    elif symbol.upper() == 'NESTLEIND':
        df=pd.read_csv("./PROJECT/NESTLEIND.csv")
    elif symbol.upper() == 'POWERGRID':
        df=pd.read_csv("./PROJECT/POWERGRID.csv")
    elif symbol.upper() == 'PVR':
        df=pd.read_csv("./PROJECT/PVR.csv")
    elif symbol.upper() == 'RELIANCE':
        df=pd.read_csv("./PROJECT/RELIANCE.csv")
    elif symbol.upper() == 'SBIN':
        df=pd.read_csv("./PROJECT/SBIN.csv")
    elif symbol.upper() == 'TATAMOTORS':
        df=pd.read_csv("./PROJECT/TATAMOTORS.csv")
    elif symbol.upper() == 'ULTRACEMCO':
        df=pd.read_csv("./PROJECT/ULTRACEMCO.csv")
    elif symbol.upper() == 'HDFCBANK':
        df=pd.read_csv("./PROJECT/HDFCBANK.csv")
    elif symbol.upper() == 'BAJAJ-AUTO':
        df=pd.read_csv("./PROJECT/BAJAJ-AUTO.csv")
    elif symbol.upper() == 'TCS':
        df=pd.read_csv("./PROJECT/TCS.csv")
    elif symbol.upper() == 'WIPRO':
        df=pd.read_csv("./PROJECT/WIPRO.csv")
    elif symbol.upper() == 'LT':
        df=pd.read_csv("./PROJECT/LT.csv")
    elif symbol.upper() == 'SUZLON':
        df=pd.read_csv("./PROJECT/SUZLON.csv")

    else:
        df = pd.DataFrame(columns= ['Date','Open','High','Low','Close','Adj Close','Volume'])


    #Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    #set start and index rows both to 0
    start_row = 0
    end_row = 0

    #start the date form the top of the data set and go down to see if the 
    #to see if the start date is less than or eql to teh dataset

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    #Start from the bottom of the data set and go up to see if users
    #end date is grtr than or eql to the in the dataset

    for j in range (0, len(df)):
        if end >=pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 -j
            break

    #Set the index to be the date 
    df= df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row +1, :]


#Get the users input
start,end,symbol= get_input()
#Get the data
df=get_data(symbol,start,end)
#get the company name
company_name=get_company_name(symbol.upper())

#Display close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])


#Display volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

#Get statistic on the data
st.header('Data Statistics')
st.write(df.describe())