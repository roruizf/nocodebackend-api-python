# NoCodeBackend API Functions

This file contains Python functions that interact with the NoCodeBackend API. These functions allow you to perform various operations such as reading, searching, updating, and deleting records in your database. Each function is designed to handle authentication, error handling, and data processing to make API interactions straightforward.

## Table of Contents

- [NoCodeBackend API Functions](#nocodebackend-api-functions)
  - [Table of Contents](#table-of-contents)
  - [Functions](#functions)
    - [create\_record](#create_record)
    - [read\_records](#read_records)
    - [read\_record\_by\_id](#read_record_by_id)
    - [filter\_none\_values](#filter_none_values)
    - [search\_records](#search_records)
    - [update\_record\_by\_id](#update_record_by_id)
    - [delete\_record\_by\_id](#delete_record_by_id)
    - [search\_ids](#search_ids)
    - [read\_records\_as\_dataframe](#read_records_as_dataframe)
    - [search\_records\_as\_dataframe](#search_records_as_dataframe)
    - [search\_ids\_as\_dataframe](#search_ids_as_dataframe)

---

## Functions

### create_record

**Description:** 
Creates a new record in the specified table by sending the provided data to the API.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `data (dict)`: A dictionary containing the data for the new record.
- `table_name (str)`: The name of the table where the record will be created.

**Returns:**
- `dict or None`: The JSON response from the API, or `None` if an error occurs.

### read_records

**Description:** 
Reads all records from the specified table.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table from which to read records.

**Returns:**
- `dict or None`: The JSON response from the API, or `None` if an error occurs.

### read_record_by_id

**Description:** 
Reads a specific record by its ID from the specified table.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table from which to read the record.
- `record_id (int or str)`: The ID of the record to read.

**Returns:**
- `dict or None`: The JSON response from the API, or `None` if an error occurs.

### filter_none_values

**Description:** 
Removes `None` values from the provided dictionary.

**Parameters:**
- `filters (dict)`: A dictionary containing key-value pairs, where some values might be `None`.

**Returns:**
- `dict`: A dictionary with all `None` values removed.

### search_records

**Description:** 
Searches for records in the specified table based on the provided filters.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table in which to search for records.
- `filters (dict)`: A dictionary containing the filters for the search. `None` values are ignored.

**Returns:**
- `dict or None`: The JSON response from the API, or `None` if an error occurs.

### update_record_by_id

**Description:** 
Updates a specific record by its ID in the specified table with the provided data.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table in which to update the record.
- `record_id (int or str)`: The ID of the record to update.
- `data (dict)`: A dictionary containing the data to update the record.

**Returns:**
- `dict or None`: The JSON response from the API, or `None` if an error occurs.

### delete_record_by_id

**Description:** 
Deletes a specific record by its ID from the specified table.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table from which to delete the record.
- `record_id (int or str)`: The ID of the record to delete.

**Returns:**
- `dict or None`: The JSON response from the API, or `None` if an error occurs.

### search_ids

**Description:** 
Searches for records in the specified table based on the provided filters and returns only their IDs.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table in which to search for records.
- `filters (dict)`: A dictionary containing the filters for the search. `None` values are ignored.

**Returns:**
- `dict or None`: A dictionary containing the IDs of the records matching the filters, or `None` if an error occurs.

### read_records_as_dataframe

**Description:** 
Reads all records from the specified table and returns them as a pandas DataFrame.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table from which to read records.

**Returns:**
- `pandas.DataFrame or None`: A DataFrame containing the records from the specified table, or `None` if an error occurs.

### search_records_as_dataframe

**Description:** 
Searches for records in the specified table based on the provided filters and returns them as a pandas DataFrame.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table in which to search for records.
- `filters (dict)`: A dictionary containing the filters for the search. `None` values are ignored.

**Returns:**
- `pandas.DataFrame or None`: A DataFrame containing the records matching the filters, or `None` if an error occurs.

### search_ids_as_dataframe

**Description:** 
Searches for records in the specified table based on the provided filters and returns only their IDs as a pandas DataFrame.

**Parameters:**
- `instance (str)`: The instance ID of the database.
- `secret_key (str)`: The secret key for authentication.
- `table_name (str)`: The name of the table in which to search for records.
- `filters (dict)`: A dictionary containing the filters for the search. `None` values are ignored.

**Returns:**
- `pandas.DataFrame or None`: A DataFrame containing the IDs of the records matching the filters, or `None` if an error occurs.