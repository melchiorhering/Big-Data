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
