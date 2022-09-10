import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


#set page configuration
st.set_page_config(page_title='Share prices for all companies in the Nairobi Securities Exchange',layout='wide')

#title
#st.title('Stock prices for all companies in the Nairobi Securities Exchange')


#sidebar
st.sidebar.title('Options')

#search
options = st.sidebar.selectbox('Which dashboard?',('Home','NewGold Exchange Traded Fund','Bamburi Cement',
'ARM Cement','BOC Kenya Limited',"Data Statistics"))

st.header(options)
if options == 'Home':
    st.subheader('What type of an investor are you? ')
    st.write('One of the major benefits of investing in the stock market is '
             'that investors get the chance to earn more money, '
             'if the stock market rises in value,'
             ' the prices of a particular stock can rise or fall. '
             'However, investors who have put their money in **_stable_ companies**'
             ' will see profit growth.'
             'Below are two graphs representing the top and bottom current companies in the Nairobi Securities Exchange by share price. ')
    stock = pd.read_csv('top1.csv')
    fig = px.bar(stock, x='company',y='Price',labels={'company': 'Companies', 'Price': 'Latest Price'},color='company',text="Price")
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    #plt.gca().set_ylim(ymax=2000)
    fig.update_xaxes(title_font=dict(size=18))
    fig.update_yaxes(title_font=dict(size=18))
    fig.update_layout(
        title_text='Current Top 10 Listed Companies by Share Price  ', title_x=0.4)

    st.plotly_chart(fig, use_container_width=True)

    stocks = pd.read_csv('bottom1.csv')
    fig = px.bar(stocks, x='company', y='Price', labels={'company': 'Companies', 'Price': 'Latest Price'},
                color='company', text="Price")
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    plt.gca().set_ylim(ymax=2)
    fig.update_xaxes(title_font=dict(size=18))
    fig.update_yaxes(title_font=dict(size=18))
    fig.update_layout(
        title_text='Current Bottom 10 Listed Companies by Share Price  ', title_x=0.4)

    st.plotly_chart(fig, use_container_width=True)

if options == 'NewGold Exchange Traded Fund':
    st.subheader('NewGold Exchange Trends')
    stocks = pd.read_csv('data.csv').query("company == 'NewGold Exchange Traded Fund'")
    fig = px.scatter(stocks, x='date', y='price', labels={'date': 'Date', 'price': 'Price'}, color='company')
    fig.update_xaxes(title_font=dict(size=18))
    fig.update_yaxes(title_font=dict(size=18))
    fig.update_layout(
        title_text='A scatter plot graph for the share prices of NewGold Exchange in 2020 ', title_x=0.4)

    st.plotly_chart(fig, use_container_width=True)



if options == 'Bamburi Cement':
    st.subheader('Bamburi Cement Trends')
    stocks = pd.read_csv('data.csv').query("company == 'Bamburi Cement Limited'")
    fig = px.scatter(stocks, x='date', y='price', labels={'date': 'Date', 'price': 'Price'}, color='company')
    fig.update_xaxes(title_font=dict(size=18))
    fig.update_yaxes(title_font=dict(size=18))
    fig.update_layout(
        title_text='A scatter plot graph for the share prices of Bamburi Cement in 2020 ', title_x=0.4)

    st.plotly_chart(fig, use_container_width=True)

if options == 'ARM Cement':
    st.subheader('ARM Cement Trends')
    stocks = pd.read_csv('data.csv').query("company == 'ARM Cement Limited'")
    fig = px.scatter(stocks, x='date', y='price',labels={'date': 'Date', 'price': 'Price'}, color='company')
    fig.update_xaxes(title_font=dict(size=18))
    fig.update_yaxes(title_font=dict(size=18))
    fig.update_layout(
        title_text='A scatter plot graph for the share prices of ARM Cement in 2020 ', title_x=0.4)

    st.plotly_chart(fig, use_container_width=True)

if options == 'BOC Kenya Limited':
    st.subheader('BOC Kenya Trends')
    stocks = pd.read_csv('data.csv').query("company == 'BOC Kenya Limited'")
    fig = px.scatter(stocks, x='date', y='price', labels={'date': 'Date', 'price': 'Price'}, color='company')
    fig.update_xaxes(title_font=dict(size=18))
    fig.update_yaxes(title_font=dict(size=18))
    fig.update_layout(
        title_text='A scatter plot graph for the share prices of BOC Kenya Limited in 2020 ', title_x=0.4)

    st.plotly_chart(fig, use_container_width=True)

if options == 'Data Statistics':
    st.subheader('Data Statistics ')
    st.write('Below is raw data of the share prices of all'
            ' the companies listed in the Nairobi Security Exchange '
            'that you can download.')
    stock = pd.read_csv('data.csv')
    st.dataframe(stock)
    st.download_button('Download',file_name='data.csv',data='stock')

