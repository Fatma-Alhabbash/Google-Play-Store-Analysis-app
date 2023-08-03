import streamlit as st
import pandas as pd

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

st.header('About the App')
st.markdown('''
This app is created to analyze the Google Play Store data using veruious techniques and visualizations.
This app will contain three sections:
    <li>Uni-column Analysis: Analyzing each column separately in a single visualization.</li>
    <li>Bi-column Analysis: Utilize visualizations in order to analyze the correlation between two columns.</li>
    <li>Multi-column Analysis: Utilize visualizations in order to analyze the correlation between more than two columns.</li>
''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.header('About the Data')
st.markdown('''
This data from Kaggle <a href="https://www.kaggle.com/datasets/lava18/google-play-store-apps">Google Play Store Apps</a>
            . This information was scraped from the Google Play Store and consists of 13 columns. <br>
            The Play Store apps data has enormous potential to drive app-making businesses to success. <br>
            Actionable insights can be drawn for developers to work on and capture the Android market!
''', unsafe_allow_html=True)
st.markdown('''
<h4>Here's the meta data about each column in the data:</h4>
    <ol>
    <li>App: The name of the mobile application listed on the Google Play Store.</li>   
    <li>Category: The category to which the app belongs, such as 'Art & Design', 'Entertainment', 'Education', etc.</li>
    <li>Rating: The user rating of the app, ranging from 1 to 5. This represents the average rating given by users who have downloaded and used the app.</li>
    <li>Reviews: The number of user reviews for the app. This indicates the total count of reviews written by users on the Google Play Store.</li>
    <li>Size: The size of the app, representing the amount of storage space it occupies on a device.</li>
    <li>Installs: The number of times the app has been installed on Android devices. This provides an estimate of the app's popularity.</li>
    <li>Type: The type of app, either 'Free' or 'Paid'.</li>
    <li>Price: The price of the app, if it is a paid app. It is given in the local currency.</li>
    <li>Content Rating: The age group for which the app is appropriate. For example, 'Everyone', 'Teen', 'Mature 17+', etc.</li>
    <li>Genres: The genre(s) of the app, such as 'Action', 'Puzzle', 'Arcade', etc.</li>
    <li>Last Updated: The date when the app was last updated on the Google Play Store.</li>
    <li>Current Ver: The current version of the app available on the Google Play Store.</li>
    <li>Android Ver: The minimum Android version required to run the app.</li>
    </ol>
''', unsafe_allow_html=True)


# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('googleplaystore.csv')
    return df

df = load_data()

# Display Data
st.header('Data')
if st.checkbox('Show Data'):
    st.write(df)