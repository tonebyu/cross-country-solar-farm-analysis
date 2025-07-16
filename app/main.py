import streamlit as st
from app.utils import load_data, plot_metric_boxplot, plot_avg_ghi_bar

st.title("🌞 Cross-Country Solar Insight Dashboard")

# Sidebar filters
country_options = ['Benin', 'Sierra Leone', 'Togo']
metric = st.selectbox("Select a metric", ['GHI', 'DNI', 'DHI'])
selected_countries = st.multiselect("Select countries", country_options, default=country_options)

# Load and filter data
df = load_data()
filtered_df = df[df['Country'].isin(selected_countries)]

# Show boxplot
st.pyplot(plot_metric_boxplot(filtered_df, metric))

# Show average GHI ranking bar chart
if metric == 'GHI':
    st.subheader("Average GHI by Country")
    st.pyplot(plot_avg_ghi_bar(filtered_df))
