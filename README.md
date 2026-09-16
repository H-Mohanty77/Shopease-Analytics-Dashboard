# Shopease-Analytics-Dashboard
A Python-based interactive analytics dashboard built with Streamlit to analyze ShopEase order and customer data.

The project provides interactive data filtering, business insights, statistical analysis, visualizations, and hypothesis testing through a user-friendly dashboard.

##Project Overview

ShopEase Analytics Dashboard is designed to explore and analyze e-commerce order data.

Users can interact with the dashboard using filters such as:

City
Product Category
Gender
Order Status
Customer Age
Unit Price

The dashboard dynamically updates the results based on the selected filters.

✨ Features
📊 Interactive Dashboard
Dynamic filtering of customer and order data
KPI cards showing key business metrics
Interactive tabs for different types of analysis
📈 Data Visualization

The dashboard includes:

Revenue by Category
Orders by City
Total Amount Distribution
Boxplot of Amount by Category
Rating Distribution
Correlation Heatmap
Unit Price vs Total Amount Scatter Plot
📋 Statistical Analysis

The project includes descriptive statistics for numerical variables such as:

Customer Age
Quantity
Unit Price
Discount
Rating
Total Amount

It also provides categorical summaries for:

Gender
City
Category
Payment Method
Order Status
🔬 Inferential Statistics

The dashboard performs several statistical tests:

Independent Samples t-test
ANOVA
Chi-square test
Pearson correlation

These tests are used to explore relationships and differences within the dataset.

📥 Data Export

Users can download the currently filtered dataset as a CSV file directly from the dashboard.

🛠️ Technologies Used
Python
Streamlit
Pandas
NumPy
Matplotlib
Seaborn
SciPy
Statsmodels
📁 Project Structure
ShopEase-Analytics/
│
├── app.py
├── Group 9_Python_Project.ipynb
├── requirements.txt
├── shopease_cleaned.csv
├── shopease_raw_orders.csv
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
2. Navigate to the project folder
cd YOUR-REPOSITORY
3. Install the required libraries
pip install -r requirements.txt
🚀 Running the Dashboard

Run the following command in your terminal:

streamlit run app.py

Streamlit will start the application and provide a local URL that you can open in your browser.

📊 Dashboard KPIs

The dashboard displays four key metrics:

KPI	Description
💰 Total Revenue	Sum of total order amounts
🛒 Total Orders	Number of filtered orders
💵 Average Order Value	Average total amount per order
⭐ Average Rating	Average customer rating
🔍 Statistical Tests
Independent Samples t-test

Compares the Total Amount between male and female customers.

ANOVA

Examines differences in Total Amount across product categories.

Chi-square Test

Examines the relationship between Gender and Order Status.

Pearson Correlation

Measures the relationship between Unit Price and Total Amount.

📂 Dataset

The project uses ShopEase order data containing customer, order, product, pricing, rating, and delivery-related information.

The dashboard loads the cleaned dataset and converts the order and delivery date fields into datetime format for analysis.

🎯 Project Objectives

The main objectives of this project are to:

Analyze ShopEase customer and order data.
Identify patterns in revenue and orders.
Explore customer ratings and purchasing behavior.
Analyze relationships between numerical variables.
Apply statistical techniques to business data.
Build an interactive dashboard for data exploration.
Allow users to filter and download relevant data.
👥 Group 9

Python Project — Group 9

This project was developed as part of an academic Python/data analytics project.

📜 License

This project is intended for educational and academic purposes.
