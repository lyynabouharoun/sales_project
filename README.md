# Sales Data Analysis Project

## **Project Overview**

This project demonstrates a full workflow of **generating, processing, analyzing, and visualizing sales data** using Python.
It simulates monthly sales for four products over a year and provides insights through metrics and visualizations.

---

## **Project Structure**

* `notebook.ipynb` → main execution file for the workflow.
* `utils.py` → contains all helper functions for data generation, processing, and analysis.
* `data/` → stores the CSV files:

  * `initial.csv` → raw generated data
  * `final.csv` → processed data with additional metrics
  * `output.csv` → quarterly summaries
* `plots/` → stores all generated visualizations (line chart, stacked bar, heatmap, boxplot)

---

## **Functions Overview (utils.py)**

### **Data Generation**

* `generate_random_sales(min_val, max_val, size)` → generates random integer sales in a range **inclusive of max_val**.

### **Data Processing**

* `add_total_sales(df, product_columns)` → adds `Total_Sales` column.
* `add_average_sales(df, product_columns)` → adds `Average_Sales` column.
* `add_mom_growth(df)` → calculates month-over-month growth in `%`.
* `map_month_to_quarter(df, month_column)` → assigns months to Q1–Q4.
* `add_max_sales_product(df, product_columns)` → identifies product with highest sales each month.
* `add_min_sales_product(df, product_columns)` → identifies product with lowest sales each month.

### **Quarterly Analysis**

* `pivot_avg_sales_per_quarter(df, product_columns)` → average sales per product per quarter.
* `pivot_total_sales_per_quarter(df, product_columns)` → total sales per product per quarter.
* `save_summaries_to_single_csv(avg_df, total_df)` → combines and saves average + total summaries.

### **Performance Metrics**

* `best_month(df)` → returns month with highest sales.
* `best_product(df, product_columns)` → returns product with highest total yearly sales.
* `best_quarter(df)` → returns quarter with highest total sales.

---

## **Workflow**

1. **Generate Data:**

   * Random sales for 4 products over 12 months.
   * Save to `initial.csv`.

2. **Process Data:**

   * Compute total, average, and month-over-month growth.
   * Map months to quarters.
   * Identify max and min sales products per month.
   * Save to `final.csv`.

3. **Quarterly Summaries:**

   * Compute average and total sales per quarter.
   * Save combined summary in `output.csv`.

4. **Analysis:**

   * Identify **best month**, **best product**, **best quarter**.

5. **Visualization:**

   * Line charts, stacked bar charts, heatmaps, and boxplots.
   * Insights: Product_A is strongest, Q3 has peak sales, some variability in Product_C and D.

---

## **Why Functions**

* Reusable and modular → easy to maintain and expand.
* Clean notebook → easy to read and follow workflow.
* Real-world style → matches professional data analysis pipelines.

---

## **Results Summary**

* **Best Month:** September (244 units)

* **Best Product:** Product_A (894 units/year)

* **Best Quarter:** Q3 (677 units)

* Visualizations show monthly trends, contributions per product, and sales distributions.

---

## **Requirements**

* Python 3.x
* Packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `IPython`

---

## **Usage**

1. Clone the repository.
2. Install required packages:

```bash
pip install pandas numpy matplotli
```
