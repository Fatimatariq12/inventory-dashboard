
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Inventory Management Dashboard",
    page_icon="📦",
    layout="wide"
)

# Dashboard heading
st.title("📦 Inventory Management Dashboard")
st.write("Welcome to your Inventory Management System.")

# Load inventory data
try:
    df = pd.read_csv("inventory.csv")

    st.subheader("Inventory Items")

    # Create two columns for filters
    col1, col2 = st.columns(2)

    # Get unique categories
    categories = sorted(
        df["Category"].dropna().unique().tolist()
    )

    # Category dropdown
    with col1:
        selected_category = st.selectbox(
            "Category",
            ["All Categories"] + categories
        )

    # Search input
    with col2:
        search_text = st.text_input(
            "Search",
            placeholder="Search by item name..."
        )

    # Apply category filter
    filtered_df = df.copy()

    if selected_category != "All Categories":
        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    # Apply search filter
    if search_text:
        filtered_df = filtered_df[
            filtered_df["Name"].astype(str).str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    # Display filtered data
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # Display record count
    st.write(
        f"Total inventory records: {len(filtered_df)}"
    )

    # Show message if no results
    if filtered_df.empty:
        st.warning("No matching inventory items found.")

except FileNotFoundError:
    st.error("inventory.csv file not found. Please check your project files.")

except KeyError as e:
    st.error(f"Missing required column in CSV: {e}")
