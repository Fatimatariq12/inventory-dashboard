
import streamlit as st
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="Inventory Management System",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Inventory Management System")
st.write("Manage your inventory by adding and viewing products.")

# CSV file
CSV_FILE = "inventory.csv"

# Required columns
COLUMNS = ["Item ID", "Name", "Category", "Quantity", "Price"]


# Load inventory data
def load_data():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(CSV_FILE, index=False)
        return df

    df = pd.read_csv(CSV_FILE)

    # Check CSV columns
    if list(df.columns) != COLUMNS:
        st.error("CSV columns do not match the required format.")
        st.stop()

    return df


# Save inventory data
def save_data(df):
    df.to_csv(CSV_FILE, index=False)


# Two-column layout
left_col, right_col = st.columns([1, 2])

# --------------------------------
# LEFT SIDE: ADD ITEM FORM
# --------------------------------

with left_col:

    st.subheader("➕ Add New Item")

    with st.form("add_item_form"):

        item_id = st.text_input("Item ID")

        name = st.text_input("Item Name")

        category = st.text_input("Category")

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            step=1
        )

        price = st.number_input(
            "Price",
            min_value=0.01,
            step=0.01,
            format="%.2f"
        )

        submit = st.form_submit_button(
            "Add Item",
            use_container_width=True
        )

    # Form submission
    if submit:

        # Check required fields
        if not item_id.strip() or not name.strip() or not category.strip():
            st.error("Please fill in all fields.")

        else:

            df = load_data()

            # Check duplicate Item ID
            existing_ids = df["Item ID"].astype(str).str.strip()

            if item_id.strip() in existing_ids.values:

                st.error("This Item ID already exists!")

            else:

                # Create new item
                new_item = pd.DataFrame([{
                    "Item ID": item_id.strip(),
                    "Name": name.strip(),
                    "Category": category.strip(),
                    "Quantity": int(quantity),
                    "Price": float(price)
                }])

                # Append new item
                df = pd.concat(
                    [df, new_item],
                    ignore_index=True
                )

                # Save to CSV
                save_data(df)

                st.success("Item added successfully!")

                # Refresh app
                st.rerun()


# --------------------------------
# RIGHT SIDE: INVENTORY TABLE
# --------------------------------

with right_col:

    st.subheader("📋 Inventory Records")

    df = load_data()

    # Search
    search = st.text_input("🔍 Search by item name")

    # Category filter
    categories = ["All Categories"] + sorted(
        df["Category"].dropna().astype(str).unique().tolist()
    )

    selected_category = st.selectbox(
        "Filter by Category",
        categories
    )

    # Apply filters
    filtered_df = df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["Name"].astype(str).str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if selected_category != "All Categories":
        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    # Display table
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # Total records
    st.info(f"Total Inventory Items: {len(df)}")

    st.info(f"Displayed Items: {len(filtered_df)}")
