# GitHub Streak Keeper

This Python script automates the process of keeping your GitHub streak alive by creating random files, committing them to a GitHub repository, and then pushing the changes to your GitHub branch. It also cleans up the created files after they are pushed.

## Features

- Automatically generates a random file with random content.
- Adds the generated file to Git, commits it with a pre-defined message, and pushes it to a specified branch.
- Deletes the random file locally after committing and pushing.

## Prerequisites

Before using the script, ensure the following:

1. Python 3 is installed on your system.
2. Git is installed and properly configured.
3. You have cloned your GitHub repository to your local machine.
4. Your GitHub credentials are cached, or you have set up SSH keys to allow pushing changes without manual authentication.

## Setup

1. Clone this repository or download the script.
2. Update the following configurations in the script to match your setup:
   - `repo_path`: Replace with the path to your local GitHub repository.
   - `branch_name`: Replace with the name of the branch where you want to push the changes (default is `main`).
   - `commit_message`: Customize the commit message if desired.

## Usage

1. Navigate to the directory containing the script.
2. Run the script with the following command:
   ```bash
   python dailyCommit.py
