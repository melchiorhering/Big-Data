import duckdb
import polars as pl
import streamlit as st


# Function to connect and perform a query on DuckDB
def perform_query_on_duckdb(file_path, query) -> pl.DataFrame:
    try:
        with duckdb.connect(database=file_path, read_only=False) as conn:
            return conn.execute(query).pl()
    except Exception as e:
        st.error(f"Error performing query on DuckDB: {e}")
        return pl.DataFrame()


# Function to get table information
def get_table_info(file_path: str) -> pl.DataFrame:
    query = "SHOW ALL TABLES;"
    return perform_query_on_duckdb(file_path, query).drop("temporary", "database")


# Function to get a table as DataFrame
def get_table_as_dataframe(
    file_path: str, schema: str, table_name: str
) -> pl.DataFrame:
    query = f"SELECT * FROM {schema}.{table_name};"
    return perform_query_on_duckdb(file_path, query)
