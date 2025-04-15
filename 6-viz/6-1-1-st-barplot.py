import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
pengo = sns.load_dataset("penguins")
pengo['count'] = 1 # Add a column with the value 1 to count each row

st.dataframe(pengo)
# create a subplot and assign to the variable series1
figure, series1 = plt.subplots()

sns.barplot(data=pengo, x="species", 
            y="count", 
            hue="species", 
            estimator="sum", 
            ax=series1).set_title("Total Count by Species")
st.pyplot(figure)
