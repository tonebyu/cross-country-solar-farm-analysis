import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv("../data/combined_cleaned.csv")

def plot_metric_boxplot(df, metric):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Country', y=metric, ax=ax, palette='Set2')
    ax.set_title(f'{metric} Comparison')
    return fig

def plot_avg_ghi_bar(df):
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots()
    sns.barplot(x=avg_ghi.values, y=avg_ghi.index, ax=ax, palette='viridis')
    ax.set_xlabel("Average GHI (W/m²)")
    ax.set_title("Average GHI by Country")
    return fig
