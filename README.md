# Inventory Dashboard

Project Overview
The Inventory Dashboard is a simple inventory management application developed using Python, Streamlit, and Pandas. It displays inventory records in an interactive table, making it easier to view and manage basic inventory information.

Features
- Display inventory items in a table.
- View item ID, name, category, quantity, and price.
- Show the total number of inventory records.
- Simple and user-friendly interface.

Technologies Used
- **Python** – Programming language
- **Streamlit** – Web application framework
- **Pandas** – Data handling and data analysis
- **CSV** – Inventory data storage

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
```powershell
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
The application reads inventory information from `inventory.csv`, which contains sample inventory records.

Project Status
Task 1: Project Setup and Initial Inventory Display – Completed

