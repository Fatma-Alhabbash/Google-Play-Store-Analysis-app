import streamlit as st
import pandas as pd
import helper_

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('Google_Play.png')
    with col3:
        st.write(' ')

st.markdown("<h2 style='text-align: center; color: #3399FF;'>Google Play Store Data Analysis</h2>"
            , unsafe_allow_html=True)

# Load Data
df = helper_.load_data()

st.markdown("<h3'>Uni Column Analysis</h3>", unsafe_allow_html=True)

# Column selection
column_option = st.selectbox('Select column to visualize it', df.columns)

numerical_cols = df.select_dtypes(exclude='object').columns
categorical_cols = df.select_dtypes(include='object').columns

if column_option in numerical_cols:
    figure = helper_.univariate_num(df, column_option)
    st.plotly_chart(figure)

elif column_option in categorical_cols:
    figure = helper_.univariate_cat(df, column_option)
    st.plotly_chart(figure)

