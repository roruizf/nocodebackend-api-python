import requests
import json
import pandas as pd


def create_record(instance, secret_key, data, table_name):
    """
    Create a new record in the database.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    data (dict): A dictionary containing the record information with column names as keys and values as values.
    table_name (str): The name of the table where the record will be created.

    Returns:
    dict: The response from the API.
    """
    url = f"https://api.nocodebackend.com/create/{table_name}?Instance={instance}"

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {secret_key}'
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def read_records(instance, secret_key, table_name):
    """
    Reads all records from the NoCodeBackend API.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name from which to read records.

    Returns:
    dict or None: The JSON response from the API, or None if an error occurs.
    """
    url = f'https://api.nocodebackend.com/read/{table_name}?Instance={instance}'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {secret_key}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None


def read_record_by_id(instance, secret_key, table_name, record_id):
    """
    Reads a specific record by ID from the NoCodeBackend API.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name from which to read the record.
    record_id (int or str): The ID of the specific record to read.

    Returns:
    dict or None: The JSON response from the API, or None if an error occurs.
    """
    # Convert record_id to string if it's not already
    if isinstance(record_id, int):
        record_id = str(record_id)

    url = f'https://api.nocodebackend.com/read/{table_name}/{record_id}?Instance={instance}'
    headers = {'accept': 'application/json',
               'Authorization': f'Bearer {secret_key}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None


def filter_none_values(filters):
    """
    Filters out None values from the given dictionary.

    Parameters:
    filters (dict): A dictionary containing the filters.

    Returns:
    dict: A dictionary with None values removed.
    """
    return {key: value for key, value in filters.items() if value is not None}


def search_records(instance, secret_key, table_name, filters):
    """
    Searches for records based on the provided filters.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name in which to search for records.
    filters (dict): A dictionary containing the filters. None values will be ignored.

    Returns:
    dict or None: The JSON response from the API, or None if an error occurs.
    """
    # Filter out None values from the filters dictionary
    valid_filters = filter_none_values(filters)

    url = f'https://api.nocodebackend.com/search/{table_name}?Instance={instance}'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {secret_key}'
    }

    try:
        response = requests.post(url, headers=headers,
                                 data=json.dumps(valid_filters))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None


def update_record_by_id(instance, secret_key, table_name, record_id, data):
    """
    Updates a record by ID based on the provided data.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name in which to update the record.
    record_id (int or str): The ID of the specific record to update.    
    data (dict): A dictionary containing the data to update.

    Returns:
    dict or None: The JSON response from the API, or None if an error occurs.
    """
    # Convert record_id to string if it's not already
    if isinstance(record_id, int):
        record_id = str(record_id)

    url = f'https://api.nocodebackend.com/update/{table_name}/{record_id}?Instance={instance}'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {secret_key}'
    }

    try:
        response = requests.put(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None


def delete_record_by_id(instance, secret_key, table_name, record_id):
    """
    Deletes a record by ID based on the provided parameters.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name from which to delete the record.
    record_id (int or str): The ID of the specific record to delete.    

    Returns:
    dict or None: The JSON response from the API, or None if an error occurs.
    """
    # Convert record_id to string if it's not already
    if isinstance(record_id, int):
        record_id = str(record_id)

    url = f'https://api.nocodebackend.com/delete/{table_name}/{record_id}?Instance={instance}'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {secret_key}'
    }

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response (if any)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None


def search_ids(instance, secret_key, table_name, filters):
    """
    Searches for records based on the provided filters and extracts their IDs.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name in which to search for records.
    filters (dict): A dictionary containing the filters. None values will be ignored.

    Returns:
    dict or None: The JSON response from the API, or None if an error occurs.
    """
    records = search_records(instance, secret_key, table_name, filters)
    if records and 'data' in records:
        return {'status': 'success', 'data': [{'id': record.get('id')} for record in records['data']]}
    return None


def read_records_as_dataframe(instance, secret_key, table_name):
    """
    Reads all records from the NoCodeBackend API.
    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name from which to read records.

    Returns:
    pandas.DataFrame: A DataFrame containing the records from the specified table, 
                      or None if an error occurs or if the response is None.
    """
    try:
        response = read_records(instance, secret_key, table_name)
        if response is None:
            return None
        else:
            data = response.get('data', [])
            return pd.DataFrame(data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def search_records_as_dataframe(instance, secret_key, table_name, filters):
    """
    Searches for records based on the provided filters and returns them as a DataFrame.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name in which to search for records.
    filters (dict): A dictionary containing the filters. None values will be ignored.

    Returns:
    pandas.DataFrame: A DataFrame containing the records from the specified table, 
                      or None if an error occurs or if the response is None.
    """
    try:
        response = search_records(instance, secret_key, table_name, filters)
        if response is None:
            return None
        else:
            data = response.get('data', [])
            return pd.DataFrame(data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def search_ids_as_dataframe(instance, secret_key, table_name, filters):
    """
    Searches for records based on the provided filters and returns their IDs as a DataFrame.

    Parameters:
    instance (str): The instance ID of the database.
    secret_key (str): The secret key for authentication.
    table_name (str): The table name in which to search for records.
    filters (dict): A dictionary containing the filters. None values will be ignored.

    Returns:
    pandas.DataFrame: A DataFrame containing the IDs of the records from the specified table, 
                      or None if an error occurs or if the response is None.
    """
    try:
        response = search_ids(instance, secret_key, table_name, filters)
        if response is None:
            return None
        else:
            data = response.get('data', [])
            return pd.DataFrame(data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
