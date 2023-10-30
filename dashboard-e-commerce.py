import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

bystate_df = pd.read_csv('customer_state.csv')
payment_df = pd.read_csv('payment_type.csv')

st.header('E-Commerce Collection Dashboard :sparkles:')

st.subheader('Customer Demographics')

fig, ax = plt.subplots(figsize=(25, 10))

sns.barplot(x='total_customer', y='customer_state',
            data=bystate_df, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title('Number of Customer by State', fontsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=25)

st.pyplot(fig)

# Payment Visualization
st.subheader('Order Payments')

fig, ax = plt.subplots(figsize=(25, 10))

sns.barplot(x='order', y='payment_type',
            data=payment_df, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title('Payment Type by Order', fontsize=20)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)

st.pyplot(fig)