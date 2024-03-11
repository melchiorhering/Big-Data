from typing import Union

import pandas as pd
import polars as pl
import streamlit as st
from custom.database import get_table_as_dataframe, get_table_info
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm

# Page Styling
st.set_page_config(page_title="Big-Data | Homepage", layout="wide", page_icon="🚒")


# Establish communication between pygwalker and streamlit
init_streamlit_comm()


def main():
    # Adding a sidebar for navigation

    _, _, col3, _, _ = st.columns(5)
    with col3:
        st.image(
            "images/brandweer-logo-zoom.png",
        )

    # Storm Selection
    # st.sidebar.image("./images/brandweer-logo-simple.png", width=40)
    page = st.sidebar.selectbox("Choose a page", ["View Tables", "Usage Guide"])

    # Path to your DuckDB file
    db_file_path = "BIGDATA.duckdb"

    if page == "View Tables":
        view_tables_page(db_file_path)
    elif page == "Usage Guide":
        usage_guide_page()


@st.cache_resource
def get_pyg_renderer(df: Union[pl.DataFrame, pd.DataFrame]) -> StreamlitRenderer:
    # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
    return StreamlitRenderer(df, spec="./gw_config.json", debug=False)


def showcase_data(df: Union[pl.DataFrame, pd.DataFrame]):
    st.header("Use PyGWalker To Analyze data")
    renderer = get_pyg_renderer(df)
    # Render your data exploration interface. Developers can use it to build charts by drag and drop.
    renderer.render_explore(width=1600)


def view_tables_page(db_file_path):
    st.title("DuckDB Tables Viewer")

    table_info = get_table_info(db_file_path).to_pandas()

    if not table_info.empty:
        st.write("Table Information:")
        st.dataframe(table_info, use_container_width=True)

        # Create two columns for input
        col1, col2 = st.columns(2)

        with col1:
            schema = st.selectbox(
                "Select a schema!",
                tuple(table_info["schema"].unique()),
                index=None,
                placeholder="Select schema...",
            )

            st.write("You selected:", schema)

        with col2:
            # Filter to only retrieve the right schema and (table)name combinations
            df = table_info[table_info["schema"] == schema]

            table = st.selectbox(
                "Select a table!",
                tuple(df["name"].unique()),
                index=None,
                placeholder="Select table...",
            )
            st.write("You selected:", table)

        if schema and table:
            df = get_table_as_dataframe(db_file_path, schema, table).to_pandas()
            if not df.empty:  # Changed this line
                showcase_data(df)

            else:
                st.write(
                    "⚠️ - No table information found in the database.",
                )


def usage_guide_page():
    st.title("Usage Guide for Retrieving Data")

    st.markdown(
        """
    ## How to Retrieve Data
    To retrieve data from a specific table in the DuckDB database, use the `get_table_as_dataframe` function.

    ### Function Syntax
    ```python
    get_table_as_dataframe(db_file_path, schema, table_name)
    ```

    - `schema`: The schema name used for the table.
    - `table_name`: The name of the table you want to retrieve data from.

    ### Example
    ```python
    data_frame = get_table_as_dataframe(<db_file_path>, <schema>, <your_table_name>)
    print(data_frame)
    ```

    ### Important Notes
    - Ensure that the table name is correct and exists in the database.
    - Always close the connection after you are done retrieving data to avoid database locking issues.
    - Handle exceptions properly to catch and understand any errors during database operations.

    ## Common Pitfalls
    - Forgetting to close the database connection.
    - Misspelling the table name.
    - Not handling exceptions, which may lead to a lack of understanding of what went wrong during the operation.
    """
    )


if __name__ == "__main__":
    main()
