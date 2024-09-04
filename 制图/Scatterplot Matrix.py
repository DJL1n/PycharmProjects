"""
作者：legionb
日期：2024年08月31日
"""
import seaborn as sns
sns.set_theme(style="ticks")

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")