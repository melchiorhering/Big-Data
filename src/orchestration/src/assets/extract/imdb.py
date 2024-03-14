import pandas as pd
import polars as pl
from dagster import AssetExecutionContext, MetadataValue, asset


@asset(
    name="imdb_train",
    io_manager_key="database_io_manager",  # Addition: `io_manager_key` specified
)
def imdb_train(context: AssetExecutionContext) -> pl.DataFrame:
    """
    Loads local IMDb train dataset

    :return pl.DataFrame: IMDb Train Dataset
    """
    df = pl.read_csv(
        "../../data/train-*.csv",
        use_pyarrow=True,
        null_values=["\\N"],
        try_parse_dates=True,
    )
    context.add_output_metadata(
        metadata={
            "describe": MetadataValue.md(df.to_pandas().describe().to_markdown()),
            "number_of_columns": MetadataValue.int(len(df.columns)),
            "preview": MetadataValue.md(df.head().to_pandas().to_markdown()),
            # The `MetadataValue` class has useful static methods to build Metadata
        }
    )
    return df


# @asset(
#     name="imdb_directing",
#     io_manager_key="database_io_manager"
# )
# def imdb_directing(context: AssetExecutionContext) -> pl.DataFrame:
#     """
#     Loads local IMDb directing.json file

#     :return pl.DataFrame: IMDb Directing Dataset
#     """
#     df = pl.read_json("../../data/directing.json")

#     context.add_output_metadata(
#         metadata={
#             "describe": MetadataValue.md(df.to_pandas().describe().to_markdown()),
#             "number_of_columns": MetadataValue.int(len(df.columns)),
#             "preview": MetadataValue.md(df.head().to_pandas().to_markdown()),
#             # Utilizing MetadataValue class for structured metadata
#         }
#     )
#     return df