from typing import Optional
import polars as pl
import pyarrow as pa
import pyspark
import duckdb
from IPython.display import display


class DuckDBContext:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def __enter__(self) -> "DuckDBContext":
        self.conn = duckdb.connect(database=self.db_path, read_only=False)
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ) -> None:
        self.conn.close()

    def save_to_duckdb(self, df, table_name: str) -> None:
        # If the DataFrame is a Polars DataFrame, convert it to an Arrow table
        if isinstance(df, pl.DataFrame):
            df = pa.Table.from_pandas(df.to_pandas())
        # If the DataFrame is a Spark DataFrame, convert it to an Arrow table
        elif isinstance(df, pyspark.sql.DataFrame):
            df = pa.Table.from_batches(df._collect_as_arrow())
        # Convert the Arrow table to a DuckDB DataFrame
        df = self.conn.from_arrow(df)

        df.create(table_name)
        row_count = self.conn.query(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        print(f"CREATED TABLE: {table_name} WITH {row_count} ROWS!")

    def show_n(self, table_name: str, n: int = 10):
        try:
            result = self.conn.execute(f"SELECT * FROM {table_name} LIMIT {n}")

            print(result.pl())
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def show_tables_info(self, as_dataframe=False):
        try:
            # Query to get all table names in the database
            tables = self.conn.execute("SHOW TABLES;").fetchall()

            # Initialize an empty dictionary to store table info
            table_info_dict = {}

            for table in tables:
                # Get table name
                table_name = table[0]

                if as_dataframe:
                    # Query to get the first 5 rows of the table and convert it to a Polars DataFrame
                    table_data = self.conn.execute(
                        f"SELECT * FROM {table_name} LIMIT 5"
                    ).pl()

                    # Store the DataFrame in the dictionary
                    table_info_dict[table_name] = table_data

                    # Display the DataFrame in the notebook
                    print(f"Table: {table_name}")
                    display(table_data)
                else:
                    # Query to get information about the table
                    table_info = self.conn.execute(
                        f"PRAGMA table_info({table_name})"
                    ).fetchall()

                    print(f"Table: {table_name}")
                    print("Columns:")
                    for column in table_info:
                        print(f"  {column[1]} ({column[2]})")

            if as_dataframe:
                return table_info_dict

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
