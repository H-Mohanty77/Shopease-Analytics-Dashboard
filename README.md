# 🛍️ ShopEase Analytics Dashboard

An interactive **Python-based data analytics dashboard** built using **Streamlit** to analyze ShopEase customer and order data.

---

## 📌 About the Project

The **ShopEase Analytics Dashboard** is an interactive data analysis project designed to explore customer behavior, order patterns, revenue, ratings, and other business-related insights.

The dashboard allows users to filter the dataset dynamically and analyze the resulting data through visualizations, descriptive statistics, and inferential statistical tests.

---

## 🚀 Features

* 🔍 Interactive data filtering
* 💰 Total Revenue analysis
* 🛒 Total Orders analysis
* 💵 Average Order Value
* ⭐ Average Customer Rating
* 📊 Revenue by Category
* 🏙️ Orders by City
* 📈 Distribution of Total Amount
* 📦 Category-wise Amount Analysis
* ⭐ Rating Distribution
* 🔗 Correlation Heatmap
* 📉 Unit Price vs Total Amount analysis
* 📋 Descriptive Statistics
* 🔬 Statistical Hypothesis Testing
* 📥 Download filtered data as CSV

---

## 📊 Dashboard Analysis

### Key Performance Indicators

The dashboard displays the following KPIs:

| Metric                 | Description                                      |
| ---------------------- | ------------------------------------------------ |
| 💰 Total Revenue       | Total revenue generated from the filtered orders |
| 🛒 Total Orders        | Number of orders in the filtered dataset         |
| 💵 Average Order Value | Average order amount                             |
| ⭐ Average Rating       | Average customer rating                          |

### Visualizations

The dashboard contains the following visualizations:

* **Revenue by Category**
* **Orders by City**
* **Total Amount Distribution**
* **Boxplot: Amount by Category**
* **Rating Distribution**
* **Correlation Heatmap**
* **Unit Price vs Total Amount Scatter Plot**

---

## 🔬 Statistical Analysis

The project applies multiple statistical techniques to understand relationships and differences within the data.

### Independent Samples t-test

Used to analyze whether there is a statistically significant difference in **Total Amount** between male and female customers.

### ANOVA

Used to analyze differences in **Total Amount** across different product categories.

### Chi-square Test

Used to examine the relationship between **Gender** and **Order Status**.

### Pearson Correlation

Used to measure the relationship between **Unit Price** and **Total Amount**.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Statsmodels

---

## 📂 Project Structure

```text
ShopEase-Analytics/
│
├── app.py
├── Group 9_Python_Project.ipynb
├── requirements.txt
├── shopease_cleaned.csv
├── shopease_raw_orders.csv
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the Project Folder

```bash
cd YOUR-REPOSITORY
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local URL where you can access the dashboard in your browser.

---

## 📁 Dataset

The project uses ShopEase order data containing information related to:

* Customer Age
* Gender
* City
* Category
* Quantity
* Unit Price
* Discount
* Rating
* Total Amount
* Payment Method
* Order Status
* Order Date
* Delivery Date

The dashboard uses the cleaned d
