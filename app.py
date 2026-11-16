
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Inventory Dashboard",
    page_icon="📦",
    layout="wide"
)

# Page heading
st.title("Inventory Dashboard")
st.write("Welcome to the Inventory Management System")

# Load CSV file
try:
    df = pd.read_csv("inventory.csv")

    # Display inventory
    st.subheader("Inventory Items")
    st.dataframe(df, use_container_width=True)

    # Show total records
    st.write(f"Total inventory records: {len(df)}")

except FileNotFoundError:
    st.error("inventory.csv file not found.")

