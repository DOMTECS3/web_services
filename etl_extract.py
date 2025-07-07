import pandas as pd

#Extract data from a CSV file
def extract_from_csv(filepath):
    """
    Extract data from a CSV file.
    
    Parameters:
    filepath (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the extracted data.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Extracted {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        print(f"Error extracting data from {filepath}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error     
def extract_from_csv(filepath):
    """Extract data from a CSV file."""
    df = pd.read_csv(filepath)
    print(f"Extracted {len(df)} rows from {filepath}")
    return df

# Example usage (remove or comment out in production):
# df = extract_from_csv('input_data.csv')
