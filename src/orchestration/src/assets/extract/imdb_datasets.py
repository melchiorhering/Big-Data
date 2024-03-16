import polars as pl
import pyarrow as pa
from dagster import (
    MetadataValue,
    asset,
    get_dagster_logger,
)
from pyspark.sql import SparkSession
import urllib.request


# spark = (
#     SparkSession.builder.master("spark://spark:7077").appName("Dagster").getOrCreate()
# )


# def create_url(endpoint: str) -> str:
#     """
#     Create Url

#     :param str endpoint: download endpoint
#     :return str: full url
#     """
#     return f"https://datasets.imdbws.com/{endpoint}"


# def progress_callback(count, block_size, total_size):
#     percent = int(count * block_size * 100 / total_size)
#     print(f"Downloaded {percent}%")


# def download_file(url, filename):
#     urllib.request.urlretrieve(url, filename, reporthook=progress_callback)


# [
#     "name.basics.tsv.gz",
#     "title.akas.tsv.gz",
#     "title.basics.tsv.gz",
#     "title.crew.tsv.gz",
#     "title.episode.tsv.gz",
#     "title.principals.tsv.gz",
#     "title.ratings.tsv.gz",
# ]


# @asset(
#     name="imdb_name_basics",
#     io_manager_key="database_io_manager",
# )
# def imbd_name_basics(context) -> pl.DataFrame:
#     logger = get_dagster_logger()

#     # Create an instance of the IMDB class with the desired endpoint
#     download_url = create_url("name.basics.tsv.gz")

#     filepath = "../../../data/extra/name.basics.tsv.gz"
#     # Use the function to download the file
#     download_file(download_url, filepath)

#     # Read tsv file
#     spark_df = (
#         spark.read.format("csv")
#         .options(inferSchema="True", header="True", sep="\t")
#         .load(filepath)
#     )
#     spark_df.show()
#     df = pl.from_arrow(pa.Table.from_batches(spark_df._collect_as_arrow()))

#     context.add_output_metadata(
#         metadata={
#             "number_of_columns": MetadataValue.int(len(df.columns)),
#             "preview": MetadataValue.md(df.to_pandas().head().to_markdown()),
#         }
#     )

#     return df
