import os
import pandas as pd
from patterns import patterns
from functions import process_patterns
from excluding_patterns import excluding_patterns

# 1. Load the CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "..", "data", "biopsies_df.csv")
df = pd.read_csv(csv_path)

# 2. Clean the dataset
df.drop(['Servicio Peticionario', 'Servicio'], axis=1, inplace=True)
df = df.drop_duplicates().reset_index(drop=True)

# 3. Combine the two text columns into one for analysis
df['combined_text'] = df['Diagnóstico'].fillna('') + ' ' + df['Micro'].fillna('')


# 3a. Process target patterns
df = process_patterns(df, "combined_text", patterns)

# 3b. Process exclusion patterns
df = process_patterns(df, "combined_text", excluding_patterns, prefix="excl_")

# 4. Check if any exclusion pattern is found
excl_bool_columns = [col for col in df.columns if col.startswith('has_excl_')]
df['any_exclusion'] = df[excl_bool_columns].any(axis=1)

# 5. Check if any target pattern is found
target_bool_columns = [col for col in df.columns if col.startswith('has_') 
                      and not col.startswith('has_excl_')]

df['any_target'] = df[target_bool_columns].any(axis=1)

# Get matches that have target patterns and no exclusion patterns
final_matches_df = df[(df['any_target']) & (~df['any_exclusion'])]

# 8. Save results
result_path_csv = os.path.join(script_dir, "..", "output", "results_without_exclusions.csv")
result_path_xlsx = os.path.join(script_dir, "..", "output", "results_without_exclusions.xlsx")
final_matches_df.to_csv(result_path_csv)
final_matches_df.to_excel(result_path_xlsx)


# 9. Description of the columns extracted - improved version
print("\nDetailed analysis per column (after exclusions):")

# Create a dataframe to store the analysis results
analysis_results = []

for column in target_bool_columns:
    # Get the counts and calculate frequency
    true_count = final_matches_df[column].sum()
    total_count = len(final_matches_df)
    true_freq = (true_count / total_count) * 100 if total_count > 0 else 0
    
    # Store the results
    analysis_results.append({
        'Column': column,
        'True_Count': true_count,
        'False_Count': total_count - true_count,
        'True_Percentage': f"{true_freq:.2f}%"
    })
    
    # Also print to console in a more concise way
    print(f"{column}: {true_count} True ({true_freq:.2f}%)")

# Convert to dataframe
analysis_df = pd.DataFrame(analysis_results)

# Display the dataframe
print("\nAnalysis Results DataFrame:")
print(analysis_df)

# Save the analysis to a separate file if needed
analysis_path = os.path.join(script_dir, "..", "output", "pattern_analysis.csv")
analysis_df.to_csv(analysis_path, index=False)


# 10. Output info
print("----------  Processed dataset with exclusions! ----------------")
print(f"Original dataset length: {len(df)}")
print(f"Matches before exclusions: {len(df[df['any_target']])}")
print(f"Matches after exclusions: {len(final_matches_df)}")
excluded_count = len(df[(df['any_target']) & (df['any_exclusion'])])
print(f"Number of cases excluded: {excluded_count}")