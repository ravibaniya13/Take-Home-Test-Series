import pandas as pd

def check_missing_values(df):
    missing_values = df.isnull().sum()
    missing_summary = missing_values[missing_values > 0]
    return missing_summary
def check_duplicates(df):
    duplicate_rows = df[df.duplicated()]
    return duplicate_rows

def detect_outliers(df):
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    outliers = {}
    for col in numerical_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers_in_col = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outliers[col] = outliers_in_col
    return outliers

def generate_summary_report(df, output_file):
    with open(output_file, "w") as f:
        f.write("Data Quality Report:\n\n")
        missing_summary = check_missing_values(df)
        f.write("Missing Values:\n")
        if not missing_summary.empty:
            f.write(f"{missing_summary}\n")
        else:
            f.write("No missing values found.\n")
        f.write("\n")

        duplicates = check_duplicates(df)
        f.write(f"Duplicate Rows: {len(duplicates)}\n")
        if len(duplicates) > 0:
            f.write("Sample duplicate rows:\n")
            f.write(f"{duplicates.head().to_string()}\n")
        f.write("\n")

        outliers = detect_outliers(df)
        f.write("Outliers Detected:\n")
        for col, outlier_df in outliers.items():
            f.write(f"{col}: {len(outlier_df)} rows\n")
        if not outliers:
            f.write("No outliers detected.\n")

    print(f"\nSummary report has been saved to '{output_file}'.")

if __name__ == "__main__":
    try:
        df = pd.read_csv('E-commerce Dataset.csv')
        generate_summary_report(df, "data_quality_report.txt")
    except FileNotFoundError:
        print("Error: Dataset file not found. Please provide the correct path.")
