from dagster import asset, get_dagster_logger, MetadataValue
import requests
import polars as pl
import os

base_url = "https://datasets.imdbws.com/"

file_names = [
    "name.basics.tsv.gz",
    "title.akas.tsv.gz",
    "title.basics.tsv.gz",
    "title.crew.tsv.gz",
    "title.episode.tsv.gz",
    "title.principals.tsv.gz",
    "title.ratings.tsv.gz"
]

# Define a function to download and load data into a Polars DataFrame
def download_and_load(file_name: str) -> pl.DataFrame:
    url = f"{base_url}{file_name}"
    response = requests.get(url)
    response.raise_for_status()  # Ensure we catch any errors

    # Access TSV file, load it directly into Polars; we use a temporary file here
    temp_file_path = f"temp_{file_name}"
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(response.content)

    df = pl.read_csv(temp_file_path, has_header=True, truncate_ragged_lines=True, low_memory=True)
    os.remove(temp_file_path)  # Clean up the temporary file
    return df

# Create an asset for each IMDb file
for file_name in file_names:
    def create_asset_fn(file_name):
        @asset(name=f"imdb_{file_name.replace('.tsv.gz', '').replace('.', '_')}",
               io_manager_key="database_io_manager")
        def fetch_imdb_file(context):
            logger = get_dagster_logger()
            logger.info(f"Downloading and loading {file_name}")
            df = download_and_load(file_name)
            context.add_output_metadata(
                metadata={
                    "describe": MetadataValue.md(df.to_pandas().describe().to_markdown()),
                    "number_of_columns": MetadataValue.int(len(df.columns)),
                    "preview": MetadataValue.md(df.head().to_pandas().to_markdown()),
                    # The `MetadataValue` class has useful static methods to build Metadata
                    }
                )
            return df
        return fetch_imdb_file

    globals()[f"fetch_{file_name.replace('.tsv.gz', '').replace('.', '_')}"] = create_asset_fn(file_name)