import pandas as pd
import streamlit as st

# Example Streamlit DataFrame
df = pd.DataFrame({
    'c1' : [1,2,3,4,5],
    'c2' : [10,20,30,40,50],
})

st.dataframe(data=df, width=500, height=150)

# Example Table
st.table(data=df)

# Example Metric()
st.metric(label="Temperature", value="28 °C", delta="1,2 °C")

# Example json()
st.json({
    'c1' : [1,2,3,4,5],
    'c2' : [10,20,30,40,50],
})

# Chart
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)