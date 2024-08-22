import pandas as pd
from tabulate import tabulate as tb
import numpy as np
def read_csv_to_df(file_path):
    """
    Reads a CSV file into a pandas DataFrame.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data in file {file_path}.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing file {file_path}: {e}")
        return None

def describe_df(df):
    """
    Describes a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to describe.

    Returns:
    None
    """
    if not isinstance(df, pd.DataFrame):
        print("Error: Input is not a pandas DataFrame.")
        return

    # Get the DataFrame shape
    rows, cols = df.shape
    print(f"Shape: {rows} rows, {cols} columns")

    # Get the data types of each column
    print("\nData Types:")
    print(df.dtypes)

    # Get the summary statistics for numeric columns
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        print("\nSummary Statistics:")
        print(numeric_df.describe())

    # Get the unique values for categorical columns
    categorical_df = df.select_dtypes(include=['object'])
    if not categorical_df.empty:
        print("\nUnique Values for Categorical Columns:")
        for col in categorical_df.columns:
            print(f"{col}: {df[col].nunique()} unique values")

    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("\nMissing Values:")
        print(missing_values)
    else:
        print("\nNo missing values found.")
import pandas as pd

def summary_statistics(df):
    """
    Generates summary statistics for a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to generate summary statistics for.

    Returns:
    None
    """
    # Check if input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input is not a pandas DataFrame.")

    # Check for empty DataFrame
    if df.empty:
        print("Error: DataFrame is empty.")
        return

    # Get the summary statistics for numeric columns
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        print("Summary Statistics:")
        print(numeric_df.describe())
    else:
        print("No numeric columns found.")

    # Get the summary statistics for non-numeric columns
    non_numeric_df = df.select_dtypes(exclude=['int64', 'float64'])
    if not non_numeric_df.empty:
        print("\nNon-Numeric Columns:")
        for col in non_numeric_df.columns:
            print(f"Column: {col}")
            print(non_numeric_df[col].value_counts())
            print()
    else:
        print("No non-numeric columns found.")




def check_missing_values(df):
    """
    Checks for missing values in a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to check for missing values.

    Returns:
    None
    """
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("Missing Values:")
        print(missing_values[missing_values > 0])
    else:
        print("No missing values found.")

def check_outliers(df):
    """
    Checks for outliers in numeric columns of a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to check for outliers.

    Returns:
    None
    """
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        print("\nOutliers:")
        for col in numeric_df.columns:
            q1 = numeric_df[col].quantile(0.25)
            q3 = numeric_df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = numeric_df[(numeric_df[col] < lower_bound) | (numeric_df[col] > upper_bound)]
            if not outliers.empty:
                print(f"Column: {col}")
                print(outliers)
            else:
                print(f"No outliers found in column: {col}")
    else:
        print("No numeric columns found.")

def check_incorrect_entries(df):
    """
    Checks for incorrect entries (e.g., negative values where only positive should exist) in a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to check for incorrect entries.

    Returns:
    None
    """
    print("\nIncorrect Entries:")
    for col in df.columns:
        if df[col].dtype.kind in 'bifc':
            # Check for negative values in columns that should not have them
            if (df[col] < 0).any():
                print(f"Column: {col} has negative values.")
            else:
                print(f"No negative values found in column: {col}")
        elif df[col].dtype.kind == 'O':
            # Check for invalid categories in categorical columns
            if df[col].isnull().any():
                print(f"Column: {col} has missing values.")
            else:
                print(f"No missing values found in column: {col}")
        else:
            print(f"Column: {col} has no incorrect entries.")

# def data_quality_check(df):
#     """
#     Performs a data quality check on a pandas DataFrame.

#     Args:
#     df (pd.DataFrame): The DataFrame to perform data quality check on.

#     Returns:
#     None
#     """
#     check_outliers(df)
#     check_incorrect_entries(df)

