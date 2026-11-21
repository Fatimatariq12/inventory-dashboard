📦 Inventory Dashboard

Project Overview

The Inventory Dashboard is a simple inventory management application developed using Python, Streamlit, and Pandas. It displays inventory records in an interactive table, making it easier to view, search, filter and manage inventory information.

Features

- Display inventory items in a table.
- View Item ID, Name, Category, Quantity, and Price.
- Show the total number of inventory records.
- Search inventory items by name.
- Filter inventory items by category.
- Add new inventory items using an input form.
- Validate required input fields.
- Prevent duplicate Item IDs.
- Validate Quantity and Price.
- Automatically save new inventory records to a CSV file.
- Refresh the inventory table immediately after adding an item.
- Simple and user-friendly interface.

Technologies Used

- Python – Programming language.
- Streamlit – Web application framework.
- Pandas – Data handling and data analysis.
- CSV – Inventory data storage.
- GitHub – Version control and project hosting.
- Streamlit Community Cloud – Application deployment.

Project Structure

```text
inventory-dashboard/
│
├── app.py
├── inventory.csv
├── requirements.txt
├── README.md
└── .gitignore
```

Installation and Setup

1. Clone the Repository

```bash
git clone https://github.com/FatimaTariq12/inventory-dashboard.git
```

2. Navigate to the Project Folder

```bash
cd inventory-dashboard
```

3. Create a Virtual Environment

```bash
python -m venv .venv
```

4. Activate the Virtual Environment

```powershell
.venv\Scripts\Activate.ps1
```

5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

6. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Data Source

The application reads inventory information from `inventory.csv`, which contains inventory records. New items submitted through the Add-Item Form are appended to this CSV file.

Project Tasks and Implementation

Task 1: Project Setup and Initial Inventory Display

Features Implemented:

- Created the initial Streamlit application.
- Loaded inventory records from a CSV file using Pandas.
- Displayed inventory information in an interactive table.
- Displayed the total number of inventory records.

Status: Completed

Task 2: Category Filter and Search Functionality

Features Implemented:

- Added a category dropdown to filter inventory items.
- Added a search input to find items by name.
- Implemented case-insensitive searching.
- Combined category filtering and search functionality.
- Updated the inventory table dynamically based on user input.
- Added a message when no matching items are found.

Technologies Used:

- Python
- Streamlit
- Pandas

Status: Completed

Task 3: Add-Item Form and Streamlit Cloud Deployment

Features Implemented:

- Created an Add-Item Form using Streamlit.
- Added input fields for Item ID, Name, Category, Quantity, and Price.
- Implemented input validation for required fields.
- Prevented duplicate Item IDs.
- Added validation for Quantity and Price.
- Used Pandas to append new inventory records.
- Saved new records to the CSV file.
- Automatically refreshed the inventory table after successful submission.
- Prepared the application for deployment using Streamlit Community Cloud.

Technologies Used:

- Python
- Streamlit
- Pandas
- CSV
- GitHub
- Streamlit Community Cloud

Deployment URL:

https://inventory-dashboard-37fbjrpa9vtmzqkwzodjxd.streamlit.app/

Status:Completed.

How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```

Deployment

The application is deployed using Streamlit Community Cloud.

To deploy:

1. Create an account on Streamlit Community Cloud.
2. Connect your GitHub account.
3. Select the `inventory-dashboard` repository.
4. Select the `main` branch.
5. Set the main file path to `app.py`.
6. Click Deploy.


Author

Fatima Tariq 
