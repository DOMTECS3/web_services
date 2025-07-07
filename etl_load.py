# import pandas as pd

# def load_to_csv(df, output_path):
#     """Load DataFrame to a CSV file."""
#     df.to_csv(output_path, index=False)
#     print(f"Loaded data to {output_path}")

# # Example usage (remove or comment out in production):
# # load_to_csv(df, 'output_data.csv')


import pandas as pd
#Load DataFrame to a CSV file
def load_to_csv(df, output_path):
    """Load DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Loaded data to {output_path}")  