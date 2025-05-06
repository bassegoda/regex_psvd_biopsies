import re
import os
import pandas as pd
from patterns import patterns

# 1. Load the CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "..", "data", "biopsies_df.csv")
df = pd.read_csv(csv_path)

# 2. Clean the dataset
df.drop(['Servicio Peticionario', 'Servicio'], axis=1, inplace=True)
df = df.drop_duplicates().reset_index(drop=True)

# 3. Define function to find patterns
def find_entities(text):
    if not isinstance(text, str):
        return {}
    results = {}
    for entity_name, pattern in patterns.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        results[entity_name] = [match.group() for match in matches]
    return results

# 4. Combine the two text columns into one for analysis
df['combined_text'] = df['Diagnóstico'].fillna('') + ' ' + df['Micro'].fillna('')

# 5. Process the combined column
def process_dataframe_column(df, column_name):
    entities_series = df[column_name].apply(find_entities)
    for entity_name in patterns.keys():
        df[f"found_{entity_name}"] = entities_series.apply(lambda results: results.get(entity_name, []))
        df[f"has_{entity_name}"] = df[f"found_{entity_name}"].apply(lambda x: len(x) > 0)
    return df

df = process_dataframe_column(df, "combined_text")

# 6. Filter rows where at least one pattern matched
bool_columns = df.select_dtypes(include='bool').columns
df['any_true'] = df[bool_columns].any(axis=1)
filtered_df = df.loc[df['any_true'] == True]

# 7. Clean up extra columns before saving
cols_to_drop = [col for col in filtered_df.columns if col.startswith('has')]
filtered_df.drop(columns=cols_to_drop, inplace=True)

# 8. Save results
result_path = os.path.join(script_dir, "..", "data", "results.csv")
filtered_df.to_csv(result_path)

# 9. Output info
print("----------  Processed dataset! ----------------")
print("Original dataset length: {}".format(len(df)))
print("Any pattern matching: {}".format(len(filtered_df)))