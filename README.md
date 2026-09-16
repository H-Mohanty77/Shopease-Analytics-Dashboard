# 🛍️ ShopEase Analytics Dashboard

### 📊 Turning E-Commerce Data into Actionable Insights

> **Filter. Analyze. Visualize. Discover. 🚀**

An interactive **Python + Streamlit analytics dashboard** built to explore ShopEase customer, order, sales, pricing, and rating data.

---

## 🌟 About the Project

ShopEase Analytics transforms raw e-commerce data into an interactive dashboard that makes data easier to understand and analyze.

Users can apply filters, explore visualizations, view key business metrics, perform statistical analysis, and download filtered data from one platform.

### 🎯 Project Goal

To use **Python, Data Analytics, Visualization, and Statistics** to identify meaningful patterns in e-commerce data and present them through an interactive dashboard.

---

## ✨ Key Features

🔍 **Interactive Filters**
Filter data by City, Category, Gender, Order Status, Customer Age, and Unit Price.

💰 **Business KPIs**
Track Total Revenue, Total Orders, Average Order Value, and Average Rating.

📊 **Data Visualizations**
Explore revenue, orders, ratings, distributions, correlations, and category performance.

🔬 **Statistical Analysis**
Perform t-test, ANOVA, Chi-square, and Pearson correlation analysis.

📥 **Data Export**
Download the currently filtered dataset as a CSV file.

---

## 🎛️ Dashboard Filters

The dashboard provides filters for:

* 🏙️ City
* 📦 Category
* 👤 Gender
* 📋 Order Status
* 🎂 Customer Age
* 💵 Unit Price

All dashboard results update automatically according to the selected filters.

---

## 📊 Dashboard Visualizations

| Visualization            | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| 💰 Revenue by Category   | Compare revenue across categories        |
| 🏙️ Orders by City       | Analyze city-wise order distribution     |
| 📈 Amount Distribution   | Understand order amount patterns         |
| 📦 Category Boxplot      | Compare amount variations                |
| ⭐ Rating Distribution    | Explore customer rating patterns         |
| 🔗 Correlation Heatmap   | Identify relationships between variables |
| 📉 Price vs Total Amount | Explore pricing and sales relationships  |

---

## 🔬 Statistical Analysis

### 🧪 Independent Samples t-test

Examines the difference in **Total Amount** between male and female customers.

### 📊 ANOVA

Examines differences in **Total Amount** across product categories.

### 🔗 Chi-square Test

Examines the relationship between **Gender** and **Order Status**.

### 📈 Pearson Correlation

Measures the relationship between **Unit Price** and **Total Amount**.

---

## 🛠️ Tech Stack

* 🐍 Python
* 🎈 Streamlit
* 🐼 Pandas
* 🔢 NumPy
* 📊 Matplotlib
* 🎨 Seaborn
* 🧪 SciPy
* 📐 Statsmodels

---

## 📂 Project Structure

```text
ShopEase-Analytics-Dashboard/
│
├── app.py
├── Group_9_Python_Project.ipynb
├── requirements.txt
├── shopease_cleaned.csv
├── shopease_raw_orders.csv
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/H-Mohanty77/Shopease-Analytics-Dashboard.git
```

### 2️⃣ Navigate to the Project

```bash
cd Shopease-Analytics-Dashboard
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Dashboard 🚀

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 📁 Dataset

The project uses ShopEase order data containing information related to:

**Customer → Order → Product → Pricing → Rating → Delivery**

The cleaned dataset is used by the dashboard for analysis and visualization.

---

## 📋 Key Metrics

| Metric                 | Description                                 |
| ---------------------- | ------------------------------------------- |
| 💰 Total Revenue       | Total amount generated from filtered orders |
| 🛒 Total Orders        | Number of filtered orders                   |
| 💵 Average Order Value | Average order amount                        |
| ⭐ Average Rating       | Average customer rating                     |

---

## 🎯 Project Objectives

* 📊 Analyze e-commerce customer and order data
* 💡 Discover meaningful business patterns
* 💰 Understand revenue and sales performance
* 👥 Explore customer behavior
* ⭐ Analyze customer ratings
* 📦 Compare product categories
* 🏙️ Analyze city-wise orders
* 🔬 Apply statistical techniques
* 🖥️ Build an interactive dashboard
* 📥 Enable filtered data export

---

## 💡 Why This Project?

> **Raw data tells a story. Visualization helps us see it. 📊**

ShopEase Analytics combines **data analysis, visualization, business insights, and statistical testing** into one interactive platform.

This project demonstrates how Python can transform raw e-commerce data into useful and understandable insights.

---

## 🚀 Future Scope

* 🌐 Deploy the dashboard online
* 🤖 Add predictive analytics
* 📈 Add advanced visualizations
* 📱 Improve mobile responsiveness
* ⚡ Add real-time data updates
* 📊 Add additional business KPIs

---

## 👥 Project Information

**Python & Data Analytics Project**

Created as part of an academic project focused on **Python, Data Analysis, Visualization, and Statistics**.

---

## ⭐ Support

If you found this project interesting, consider giving the repository a ⭐ **Star**!

### Made with 🐍 Python + 📊 Data + 💡 Curiosity
