import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from datetime import datetime

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('googleplaystore.csv')

    #convert Last Updated column to datetime column

    df = df.drop(df[df['Last Updated'] == '1.0.19'].index)

    df = df.reset_index(drop=True)

    df['Last Updated'] = pd.to_datetime(df['Last Updated'], format="%B %d, %Y")

    df['Year'] = df['Last Updated'].dt.year

    # Convert "Reviewes" column , "min_Installs" column and "Price" column to numerical columns
    df['Reviews']=df['Reviews'].str.replace('M', '', regex=True)

    df['Reviews'] = pd.to_numeric(df['Reviews'])

    df['Price']=df['Price'].str.replace('$', '', regex=True)

    df = df[df['Price'] != 'Everyone'].copy()

    df['Price'] = pd.to_numeric(df['Price'])

    df = df[df['Type'] != '0'].copy()

    df['min_Installs']=df['Installs'].str.replace('[+,]', '', regex=True)

    df["min_Installs"] = pd.to_numeric(df["min_Installs"])
    return df

df = load_data()



def univariate_num(data, column):
    fig1 = px.histogram(data, x=column)

    fig2 = px.box(data, x=column)

    fig = make_subplots(rows=2, cols=1)

    fig.add_trace(fig1.data[0], row=1, col=1)

    fig.add_trace(fig2.data[0], row=2, col=1)

    fig.update_layout(title=f"Histogram and Box plot of {column}", showlegend=False, height=600, width=800)
    return fig


def univariate_cat(data, column):
    fig = px.bar(data[column].value_counts(), title=f'Bar plot of {column}', color = data[column].value_counts(),
                 labels={
        'index': f'{column}'})
    fig.update_layout(height=600, width=800)
    return fig


def type_rating_corr(data):
    dff=data.groupby(['Type'])['Rating'].mean()
    fig = px.bar(x=dff.index, y=dff.values, color=dff.index
             , title='The correlation between "Type" column and "Rating" column',
            labels = {'x':'Type', 'y': 'Rating'})
    return fig

def type_min_installs_bar(df):
    dff=df.groupby(['Type'])['min_Installs'].mean()
    fig = px.bar(x=dff.index, y=dff.values, color=dff.index, 
             title='The correlation between "Type" column and "min_Installs" column',
            labels = {'x':'Type', 'y': 'min_Installs'})
    return fig

def type_min_installs_pie(df):
    dff=df.groupby(['Type'])['min_Installs'].mean()
    y = dff.values
    mylabels = dff.index
    explode = (0, 0.5)
    fig, ax = plt.subplots()
    ax.pie(y, labels = mylabels, explode = explode, autopct='%1.1f%%')
    ax.legend()
    return fig

def type_Category_corr(df):
    grouped_data = df.groupby(['Category', 'Type']).size().reset_index(name='Count')

    fig = px.bar(grouped_data,
             x='Category',
             y='Count',
             color='Type',
             title='Type and Category Count',
             labels={'Category': 'Category', 'Count': 'Count'},
             category_orders={'Category': df['Category'].unique()},
             barmode='group'
             )

    return fig

def category_Content_Rating_corr(df):
    grouped_data = df.groupby(['Content Rating', 'Category']).size().reset_index(name='Count')

    fig = px.bar(grouped_data,
             x='Content Rating',
             y='Count',
             color='Category',
             title='Content Rating and Category Count',
             labels={'Content Rating': 'Content Rating', 'Count': 'Count'},
             category_orders={'Content Rating': df['Content Rating'].unique()},
             barmode='group'  
             )
    return fig

def category_min_installs_corr(df):
    data_grouped = df.groupby('Category')['min_Installs'].mean().sort_values(ascending=False)
    fig = px.bar(df, x=data_grouped.index, y=data_grouped.values, color=data_grouped.index,
            labels = {'x':'Category', 'y':'mean of min_installs'})
    return fig

def year_min_installs(df):
    Last_Updated_group = df.groupby('Year')['min_Installs'].mean().sort_values(ascending=False)
    fig = px.bar(Last_Updated_group,color = Last_Updated_group.index, 
             width=800, height=800)

    fig.update_layout(
    xaxis_title="Last Update date",
    yaxis_title="min_Installs"
    )

    return fig

def Android_Ver_Price_corr(df):
    fig = px.histogram(df, x='Android Ver', y='Price')
    return fig