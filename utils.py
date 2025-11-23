# utils.py

import numpy as np
import pandas as pd  

def generate_random_sales(min_val, max_val, size):
    """
    Generate a NumPy array of random integers between min_val and max_val (inclusive)
    with the given size.
    """
    return np.random.randint(min_val, max_val + 1, size=size)

def add_total_sales(df, product_columns):
    """
    Add a 'Total_Sales' column to the DataFrame by summing the given product columns.
    """
    df['Total_Sales'] = df[product_columns].sum(axis=1)
    return df

def add_average_sales(df, product_columns):
    """
    Add an 'Average_Sales' column to the DataFrame by averaging the given product columns.
    """
    df['Average_Sales'] = df[product_columns].mean(axis=1)
    return df

def add_mom_growth(df):
    """
    Add a 'Month_over_Month_Growth' column to the DataFrame based on 'Total_Sales'.
    """
    df['Month_over_Month_Growth'] = df['Total_Sales'].pct_change() * 100
    return df



def map_month_to_quarter(df, month_column='Month', quarter_column='Quarter'):
    """
    Add a column to the DataFrame mapping month names to quarters (Q1-Q4).
    
    Parameters:
    - df: pandas DataFrame
    - month_column: name of the column containing month strings (e.g., 'Jan')
    - quarter_column: name of the new column to store the quarter
    """
    def month_to_quarter(month_str):
        if month_str in ['Jan', 'Feb', 'Mar']:
            return 'Q1'
        elif month_str in ['Apr', 'May', 'Jun']:
            return 'Q2'
        elif month_str in ['Jul', 'Aug', 'Sep']:
            return 'Q3'
        else:
            return 'Q4'
    
    df[quarter_column] = df[month_column].apply(month_to_quarter)
    return df




def add_max_sales_product(df, product_columns, column_name='Max_Sales_Product'):
    """
    Add a column to the DataFrame with the product that has the highest sales each row (month).
    """
    df[column_name] = df[product_columns].idxmax(axis=1)
    return df

def add_min_sales_product(df, product_columns, column_name='Min_Sales_Product'):
    """
    Add a column to the DataFrame with the product that has the lowest sales each row (month).
    """
    df[column_name] = df[product_columns].idxmin(axis=1)
    return df




def pivot_avg_sales_per_quarter(df, product_columns, quarter_column='Quarter'):
    """
    Compute average sales per quarter for each product and total sales.
    
    Returns a new DataFrame.
    """
    return df.groupby(quarter_column)[product_columns + ['Total_Sales']].mean().reset_index()

def pivot_total_sales_per_quarter(df, product_columns, quarter_column='Quarter'):
    """
    Compute total sales per quarter for each product and total sales.
    
    Returns a new DataFrame.
    """
    return df.groupby(quarter_column)[product_columns + ['Total_Sales']].sum().reset_index()

def save_summaries_to_single_csv(avg_df, total_df, filename='data/output.csv'):
    """
    Save average and total sales summaries in a single CSV file.
    
    Adds a 'Type' column to distinguish Average vs Total.
    """
    avg_df = avg_df.copy()
    total_df = total_df.copy()
    
    avg_df['Type'] = 'Average'
    total_df['Type'] = 'Total'
    
    # Concatenate vertically
    combined_df = pd.concat([avg_df, total_df], ignore_index=True)
    
    #  reorder columns so 'Type' comes first
    cols = ['Type'] + [c for c in combined_df.columns if c != 'Type']
    combined_df = combined_df[cols]
    
    # Save to CSV
    combined_df.to_csv(filename, index=False)
    
    return combined_df  k



def best_month(df, month_column='Month', total_column='Total_Sales'):
    """
    Returns the month with the highest total sales.
    """
    idx = df[total_column].idxmax()
    return df.loc[idx, month_column], df.loc[idx, total_column]

def best_product(df, product_columns):
    """
    Returns the product with the highest cumulative annual sales.
    """
    total_per_product = df[product_columns].sum()
    best = total_per_product.idxmax()
    best_value = total_per_product.max()
    return best, best_value

def best_quarter(df, quarter_column='Quarter', total_column='Total_Sales'):
    """
    Returns the quarter with the highest total sales.
    """
    total_per_quarter = df.groupby(quarter_column)[total_column].sum()
    best = total_per_quarter.idxmax()
    best_value = total_per_quarter.max()
    return best, best_value