from dagster import load_assets_from_package_module

from . import extract, load, transform

EXTRACT = "extraction"
TRANSFORM = "transformation"
LOAD = "loading"


extraction_assets = load_assets_from_package_module(
    package_module=extract, group_name=EXTRACT
)

transformation_assets = load_assets_from_package_module(
    package_module=transform, group_name=TRANSFORM
)

loading_assets = load_assets_from_package_module(package_module=load, group_name=LOAD)
