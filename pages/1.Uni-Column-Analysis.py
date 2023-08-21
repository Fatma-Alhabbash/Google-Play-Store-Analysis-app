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

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3>Uni Column Analysis</h3>", unsafe_allow_html=True)

# Column selection
column_option = st.selectbox('Select column to visualize it', df.columns)

numerical_cols = df.select_dtypes(exclude='object').columns
categorical_cols = df.select_dtypes(include='object').columns

if column_option in numerical_cols:
    figure = helper_.univariate_num(df, column_option)
    st.plotly_chart(figure)

    if column_option == "Reviews":
        st.markdown("<h4>Note:</h4>", unsafe_allow_html=True)
        st.markdown("<h7>Since the external points are arranged behind each other and numerous, they cannot be considered abnormal or incorrect. Therefore, I did not remove them.</h7>", unsafe_allow_html=True)
    
    if column_option == "Price":
        st.markdown("<h4>Note:</h4>", unsafe_allow_html=True)
        st.markdown("<h7>Due to the large number of free apps in the data, when the column Price is displayed, it indicates that there is something wrong with it.</h7>", unsafe_allow_html=True)

elif column_option in categorical_cols:
    figure = helper_.univariate_cat(df, column_option)
    st.plotly_chart(figure)

    if column_option == "App":
        if st.checkbox('Top 10 Apps'):
            figure = helper_.top_ten(df, column_option)
            st.plotly_chart(figure)

    elif column_option == "Category":
        if st.checkbox('Top 10 Categories'):
            figure = helper_.top_ten(df, column_option)
            st.plotly_chart(figure)

    elif column_option == "Genres":
        if st.checkbox('Top 10 Genres'):
            figure = helper_.top_ten(df, column_option)
            st.plotly_chart(figure)
