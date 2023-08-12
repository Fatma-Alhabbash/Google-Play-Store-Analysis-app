import streamlit as st
import pandas as pd
import helper_

# Header
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

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3>Conclusion</h3>", unsafe_allow_html=True)

# Load Data
df = helper_.load_data()

column_option = st.selectbox('Top 10', ['App', 'Category', 'Genres'])
if column_option == "App":
    figure = helper_.top_ten(df, column_option)
    st.plotly_chart(figure)

elif column_option == "Category":
    figure = helper_.top_ten(df, column_option)
    st.plotly_chart(figure)

elif column_option == "Genres":
    figure = helper_.top_ten(df, column_option)
    st.plotly_chart(figure)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h4>Conclusion of Bi-Column Analysis</h4>", unsafe_allow_html=True)
st.markdown("""<ol>
                <li>The mean rating for Paid apps is slightly more than for free apps.</li>
                <li>Apps that are free are more popular, receiving 99.4% of mean installations, while apps that are paid receive only 0.6%.</li>
                <li>In Everyone content rating the most category used is Family category with count of 1529, and the second most category is Tools category with count of 835.</li>
                <li>In Teen content rating the most category used is Game category with count of 331.</li>
                <li>Communication apps are the most famous and used, as it recieved 65.98M installations.</li>
                <li>Installs of an app are higher when the update is recent.</li>
                </ol>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h4>Conclusion of Multi-Column Analysis</h4>", unsafe_allow_html=True)
st.markdown("""<ol>
                <li>There is strong positive correlation between min_installs and Reviews columns.</li>
                <li>Number of installations of free apps more than paid apps in all categories.</li>
                </ol>""", unsafe_allow_html=True)