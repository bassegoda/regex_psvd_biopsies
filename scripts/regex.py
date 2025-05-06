import re
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "..", "data", "biopsies_df.csv")
df = pd.read_csv(csv_path)

# Patterns for each entity
patterns = {
    "hiperplasia_nodular_regenerativa": r"[Hh]iperpl[aà]sia\s+nodular\s+regenerativa",
    "cirrosi_portal_incompleta": r"[Cc]irrosi[s]?\s+portal\s?incomple[r]?ta",
    "venopatia_portal_obliterativa": r"[Vv]enopat[ií]a\s+portal\s+obliterativa",
    "esclerosi_hepatoportal": r"[Ee]sclerosi[s]?\s+hepatoportal",
    "fibrosi_septal_incompleta": r"[Ff]ibrosi[s]?\s+septal\s+incompleta",
    "herniacio_vasos_venosos_periportals": r"[Hh]erniac[ií][oó][n]?\s+(?:de\s+)?vasos\s+venosos\s+periportals?",
    "cavernomatosi": r"[Cc]avernomat[oó]s[o]?[s]?",
    "flebosclerosi": r"flebosclerosi[s]?",
    "esclerosi_venosa": r"esclerosi[s]?\s?venosa",
    "venopenia": r"venop[èe]nia",
    "dilatacio_sinusoidal": r"dilataci[óo][n]?\s?sinuso[iï]dal",
    "pseudoangiomatos": r"[p]?seudoangiomat[óo]s[o]?[s]?",
    "peliosis": r"peliosi[s]?",
    "no_zonal": r"no[-]?zonal",
    "estenosi": r"estenosi[s]?"

}

# Example function to find matches in text
def find_entities(text):
    if not isinstance(text, str):
        return {}
    results = {}
    for entity_name, pattern in patterns.items():
        # re.finditer returns a match object with information of what was matched and where
        matches = re.finditer(pattern, text, re.IGNORECASE)
        # The group function access the entired matched string. 
        results[entity_name] = [match.group() for match in matches] 
    return results

def process_dataframe_column(df, column_name):
    # Apply the find_entities function to each row in the specified column
    entities_series = df[column_name].apply(find_entities)
    
    # Create a new DataFrame with one column per entity type
    for entity_name in patterns.keys():
        # Create a new column with a list of matches for each entity type
        df[f"found_{entity_name}"] = entities_series.apply(
            lambda results: results.get(entity_name, [])
        )
        
        # Optional: Add a column with just True/False if the entity was found
        df[f"has_{entity_name}"] = df[f"found_{entity_name}"].apply(
            lambda x: len(x) > 0
        )
    
    return df

df = process_dataframe_column(df, "Diagnóstico")
df.to_csv("results.csv")
print(df.head(5))

for pattern in patterns.keys():
    print(pattern)