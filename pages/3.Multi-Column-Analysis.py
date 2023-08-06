import streamlit as st
import pandas as pd
import helper_
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px

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

st.markdown("<h3>Multi Column Analysis</h3>", unsafe_allow_html=True)

# Heat Map
st.markdown("<h4>Heat Map</h4>", unsafe_allow_html=True)
plot_ = sns.heatmap(df.corr(), annot=True)
plt.savefig("heatmap.png")
st.image("heatmap.png")
os.remove("heatmap.png")

st.markdown(
    """<h4>Inferences:</h4>""",
    unsafe_allow_html=True)

st.markdown("<h7 style='color: #666;'>There is strong positive correlation between min_installs and Reviews columns.</h7>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# Pair Plot
st.markdown("<h4>Pair Plot</h4>", unsafe_allow_html=True)
plot = sns.pairplot(df)
st.pyplot(plot.fig)

# Change the format of numeric column
def format_changer(value):
    if value >= 1000000 or value <= -1000000:
        value /= 1000000
        return f"{value:.2f}M"
    else:
        return value

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h4>Category and Type vs min_Installs_mean</h4>", unsafe_allow_html=True)
grouped_data3 = df.groupby(['Category', 'Type'])['min_Installs'].mean().reset_index(name='min_Installs_mean')
mean_min_installs = df['min_Installs'].mean()
grouped_data3['mean_diff'] = grouped_data3['min_Installs_mean'] - mean_min_installs
grouped_data3['mean_diff'] = grouped_data3['mean_diff'].apply(format_changer)

fig = px.bar(grouped_data3,
             x='Category',
             y='min_Installs_mean', 
             color='Type',
             labels={'Category': 'Category', 'min_Installs_mean': 'Mean of min_Installs', 'Type': 'Type'},
             barmode='group',
             hover_data=['mean_diff'])

category_order = df['Category'].unique()
x_range = [-0.5, len(category_order) - 0.5]

fig.add_shape(type='line',
              x0=x_range[0], x1=x_range[1],
              y0=mean_min_installs, y1=mean_min_installs,
              line=dict(color='red', width=2)
              )

fig.update_xaxes(type='category', categoryorder='array', categoryarray=category_order)

st.plotly_chart(fig)

st.markdown(
    """
    <h4>Inferences:</h4>
    <ol style='color: #666;'>
        <li>Number of installations of free apps more than paid apps in all categories.</li>
        <li>Some free apps have mean of installs greater than the general mean of installs like Communication category.</li>
    </ol>
    """,
    unsafe_allow_html=True
)
