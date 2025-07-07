
# ETL pipeline orchestrator
from etl_extract import extract_from_csv
from etl_transform import clean_and_transform
from etl_load import load_to_csv

def run_etl(input_path, output_path):
    # Extract
    df = extract_from_csv(input_path)
    # Transform
    df_clean = clean_and_transform(df)
    # Load
    load_to_csv(df_clean, output_path)
    print("ETL pipeline completed.")

# Example usage
if __name__ == "__main__":
    run_etl('input_data.csv', 'output_data.csv')
