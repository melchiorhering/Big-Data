import os

from dagster import Definitions

from .assets import extraction_assets, loading_assets, transformation_assets
from .jobs import extract_data, load_data, transform_data
from .resources import LOCAL_RESOURCE

# Loads all assets
all_assets = [
    *extraction_assets,
    *transformation_assets,
    *loading_assets,
]


# Set's the resources based on the deployment
resources_by_deployment_name = {"local": LOCAL_RESOURCE}
deployment_name = os.environ.get("DAGSTER_DEPLOYMENT", "local")

# Defines the Dasgter definitions
defs = Definitions(
    assets=all_assets,
    resources=resources_by_deployment_name[deployment_name],
    jobs=[extract_data, transform_data, load_data],
    # schedules=[core_assets_schedule],
    # sensors=all_sensors,
)
