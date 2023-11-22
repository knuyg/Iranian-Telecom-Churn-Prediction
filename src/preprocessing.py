def rename_features(feature_name: str) -> str:
    """Properly renames the features of a given dataset

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is False)

    Returns
    -------
    str
        a list of strings representing the header columns
    """


    # Get rid of the leading and trailing whitespaces
    new_name = feature_name.strip()

    # Lower case only
    new_name = new_name.lower()

    # Replace the double spaces with only one
    new_name = new_name.replace('  ', ' ')

    # Finally replace the spaces with underscores
    new_name = new_name.replace(' ', '_')

    return new_name
