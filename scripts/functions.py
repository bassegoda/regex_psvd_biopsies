import re 


def find_patterns(text, pattern_dict, prefix=""):
    """
    Find patterns in text using a dictionary of pattern names and regex patterns.
    
    Args:
        text (str): Text to search in
        pattern_dict (dict): Dictionary of pattern names and regex patterns
        prefix (str): Prefix to add to column names
        
    Returns:
        dict: Dictionary of pattern names and matches
    """
    if not isinstance(text, str):
        return {}
    
    results = {}
    for name, pattern in pattern_dict.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        results[f"{prefix}{name}"] = [match.group() for match in matches]
    
    return results


def process_patterns(df, column_name, pattern_dict, prefix=""):
    """
    Process a dataframe column to find patterns and create columns for results.
    
    Args:
        df (DataFrame): DataFrame to process
        column_name (str): Column to search in
        pattern_dict (dict): Dictionary of patterns to search for
        prefix (str): Prefix for output columns
        
    Returns:
        DataFrame: Processed DataFrame
    """
    # Apply the function to find patterns
    patterns_series = df[column_name].apply(
        lambda text: find_patterns(text, pattern_dict, prefix)
    )
    
    # Extract the results into new columns
    for name in pattern_dict.keys():
        col_name = f"{prefix}{name}"
        df[f"found_{col_name}"] = patterns_series.apply(
            lambda pattern_dict: pattern_dict.get(col_name, [])
        )
        df[f"has_{col_name}"] = df[f"found_{col_name}"].apply(
            lambda x: len(x) > 0
        )
    
    return df
