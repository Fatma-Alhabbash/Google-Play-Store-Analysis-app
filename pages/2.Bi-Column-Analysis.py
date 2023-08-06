import streamlit as st
import pandas as pd
import helper_
import matplotlib.pyplot as plt

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

st.markdown("<h3>Bi Column Analysis</h3>", unsafe_allow_html=True)

# Correlation with Type column
st.markdown("<h4>Select column to show its correlation with Type column</h4>"
            , unsafe_allow_html=True)

# Column selection 
column_option = st.selectbox('Select Column', ['Rating', 'min_Installs', 'Category'])

if column_option == 'Rating':
    figure = helper_.type_rating_corr(df)
    st.plotly_chart(figure)
    st.markdown("<h4>Inferences:</h4>", unsafe_allow_html=True)
    st.markdown("<h7 style='color: #666;'>The mean rating for Paid apps is slightly more than for free apps</h7>", unsafe_allow_html=True)

elif column_option == 'min_Installs':
    chart_type = st.radio(
    "Choose the type of the chart:",
    ('Bar chart', 'Pie chart'))
    if chart_type == 'Bar chart':
        figure = helper_.type_min_installs_bar(df)
        st.plotly_chart(figure)
        st.markdown("<h4>Inferences:</h4>", unsafe_allow_html=True)
        st.markdown("<h7 style='color: #666;'>Free apps received 99.4% of mean installations, whereas paid apps received only 0.6%. This means that there is a greater demand for free applications</h7>", unsafe_allow_html=True)

    else:
        figure = helper_.type_min_installs_pie(df)
        figure.set_size_inches(3,3.5)
        plt.legend(fontsize=5)
        plt.rc('font', size=5)
        st.pyplot(figure)
        st.markdown("<h4>Inferences:</h4>", unsafe_allow_html=True)
        st.markdown("<h7 style='color: #666;'>Free apps received 99.4% of mean installations, whereas paid apps received only 0.6%. This means that there is a greater demand for free applications</h7>", unsafe_allow_html=True)

else:
    figure = helper_.type_Category_corr(df)
    st.plotly_chart(figure)
    st.markdown("<h4>Inferences:</h4>", unsafe_allow_html=True)
    st.markdown("<h7 style='color: #666;'>In all categories free apps more than paid apps</h7>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Correlation with Category column
st.markdown("<h4>Select column to show its correlation with Category column</h4>"
            , unsafe_allow_html=True)

# Column selection
column_option2 = st.selectbox('Select Column', ['Content Rating', 'Type', 'min_Installs'])

if column_option2 == 'Content Rating':
    figure = helper_.category_Content_Rating_corr(df)
    st.plotly_chart(figure)
    st.markdown("""<h4>Inferences:</h4>
                <ol style='color: #666;'>
                <li>In Everyone content rating the most category used is Family category with count of 1529, and the second most category is Tools category with count of 835.</li>
                <li>In Teen content rating the most category used is Game category with count of 331.</li>
                </ol>""", unsafe_allow_html=True)

elif column_option2 == 'Type':
    figure = helper_.type_Category_corr(df)
    st.plotly_chart(figure)
    st.markdown("<h4>Inferences:</h4>", unsafe_allow_html=True)
    st.markdown("<h7 style='color: #666;'>In all categories free apps more than paid apps.</h7>", unsafe_allow_html=True)

else:
    figure = helper_.category_min_installs_corr(df)
    st.plotly_chart(figure)
    st.markdown("<h4>Inferences:</h4>", unsafe_allow_html=True)
    st.markdown("<h7 style='color: #666;'>Communication apps are the most commonly installed (65.98M installations). This means that these applications are the most famous and used</h7>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h4>Year column vs min_installs column</h4>"
            , unsafe_allow_html=True)

figure = helper_.year_min_installs(df)
st.plotly_chart(figure)
st.markdown(
    """
    <h4>Inferences:</h4>
    """,
    unsafe_allow_html=True
)

st.markdown("<h7 style='color: #666;'>The more recent the app update, the more app installs</h7>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h4>Histogram of Android Ver vs. Price</h4>"
            , unsafe_allow_html=True)

figure = helper_.Android_Ver_Price_corr(df)
st.plotly_chart(figure)
