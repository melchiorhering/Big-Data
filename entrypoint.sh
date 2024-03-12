#!/bin/bash

# Define the URL of the GitHub repository
REPO_URL="https://github.com/hazourahh/big-data-course-2024-projects.git"

# Define the directory where the data will be stored
DATA_DIR="./data"

# Create the data directory if it doesn't exist
mkdir -p $DATA_DIR

# Change to the data directory
cd $DATA_DIR

# Clone the repository
git clone --no-checkout $REPO_URL temp

# Change to the repository directory
cd temp

# Initialize the sparse-checkout feature
git sparse-checkout init --cone

# Set the sparse-checkout feature to only include the imdb directory
git sparse-checkout set imdb

# Checkout the files
git checkout

# Move the files from the imdb directory to the ./data directory
mv imdb/* ..

# Go back to the ./data directory
cd ..

# Remove the temporary directory
rm -rf temp

# Keep the container running - this is a common pattern for Devcontainers
tail -f /dev/null
