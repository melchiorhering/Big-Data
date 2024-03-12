# Big Data

Run this project using Docker and [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) or use [Poetry](https://python-poetry.org/).

## Instructions

Here are the combined instructions for setting up and running a devcontainer in Visual Studio Code on both Windows (with WSL2 backend) and MacOS:

1. **Install Docker Desktop:**

   - For Windows/Mac: Download Docker Desktop from [Docker official website](https://www.docker.com/products/docker-desktop) and install it. If you're using Windows, make sure to [enable WSL 2 backend](https://docs.docker.com/docker-for-windows/wsl/).

2. **Install Visual Studio Code:**

   - Download Visual Studio Code from the [official website](https://code.visualstudio.com/download) and install it.

3. **Login into GitHub:**

   - Open Visual Studio Code.
   - Click on the `Accounts` button that appears in the sidebar.
   - Click on the `Sign in to GitHub.com` button.
   - Follow the prompts in the browser to complete the sign in process.

4. **Install the Remote - Containers extension:**

   - Open Visual Studio Code.
   - Click on the Extensions view icon on the Sidebar (or press `Ctrl+Shift+X` on Windows, `Cmd+Shift+X` on MacOS).
   - Search for `Remote - Containers`.
   - Click on the Install button.

5. **Open the project in a devcontainer:**
   - Open the command palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on MacOS) and run the `Remote-Containers: Reopen in Container...` command.
   - Select the project folder and click on the `Open` button.
   - A new window will open, and the devcontainer will start building. This might take a few minutes.

Please note that starting up the container for the first time may take a while as it needs to download and install all the necessary components.

Now, you're running your project inside a devcontainer in Visual Studio Code!

## Poetry

**Adding packages with Poetry:**

- Open the terminal in Visual Studio Code.
- Run `poetry add <package-name>` to add a new package to your project. Replace `<package-name>` with the name of the package you want to add.

**Using the Poetry shell:**

- Open the terminal in Visual Studio Code.
- Run `poetry shell` to start a new shell session with the virtual environment activated.

## Notebooks

You can find and create Jupyter notebooks in the `src/notebooks/` directory.

To work with a notebook inside Visual Studio Code:

1. Navigate to the `src/notebooks/` directory in the Explorer pane.
2. Click on the notebook file you want to open, or create a new one by right-clicking in the Explorer pane and selecting `New File`. Name your file with a `.ipynb` extension.
3. The notebook will open in a new tab, and you can start working with it directly in Visual Studio Code.
4. To select the Poetry kernel, go to the 'Kernel' menu in the toolbar, click on 'Change kernel', then under 'Python Environments', select the kernel named something like `big-data-<someweird-code>`.

Note: To work with Jupyter notebooks in Visual Studio Code, you may need to install the `Python` and `Jupyter` extensions. You can do this by clicking on the Extensions view icon on the Sidebar (or press `Ctrl+Shift+X` on Windows, `Cmd+Shift+X` on MacOS), then search for and install the `Python` and `Jupyter` extensions.

## Tools Used

### `Backend`

<table style="width:100%">
  <tr>
    <td style="width:50%; text-align:center;"><a href="https://dagster.io/"><img src="./images/dagster-primary-horizontal.png" alt="Dagster" title="Dagster.io" style="width:60%"/></a></td>
  </tr>
</table>

### `Other`

<table style="width:100%">
  <tr>
    <td style="width:33%; text-align:center;"><a href="https://python-poetry.org/"><img src="./images/poetry-logo.png" alt="Poetry" title="Poetry" style="width:60%"/></a></td>
    <td style="width:33%; text-align:center;"><a href="https://pola.rs/"><img src="./images/polars.png" alt="Polars" title="Polars" style="width:80%"/></a></td>
    <td style="width:33%; text-align:center;"><a href="https://duckdb.org/"><img src="./images/duckdb.png" alt="DuckDB" title="DuckDB" style="width:60%"/></a></td>
  </tr>
</table>

## Diagram

![Project Solution Diagram](./images/Project-Solution-Diagram.svg)
