from dagster import AssetSelection, define_asset_job

from .assets import EXTRACT, TRANSFORM, LOAD

extract_data = define_asset_job(
    "extract_data", selection=AssetSelection.groups(EXTRACT)
)
transform_data = define_asset_job(
    "transform_data", selection=AssetSelection.groups(TRANSFORM)
)

load_data = define_asset_job("load_data", selection=AssetSelection.groups(LOAD))
