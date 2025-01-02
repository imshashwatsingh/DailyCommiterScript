import os
import random
import string
import subprocess
from datetime import datetime

# Configurations
repo_path = "C:\\Users\\lenovo\\Desktop\\GScript"  # Replace with the path to your GitHub repo
commit_message = "Daily update: Keep my GitHub streak alive!"
branch_name = "main"  # Replace with your branch name

def create_random_file():
    """Create a random file with some content."""
    filename = f"file_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    file_path = os.path.join(repo_path, filename)
    random_content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    with open(file_path, 'w') as f:
        f.write(random_content)
    return filename

def git_command(*args):
    """Run a Git command."""
    result = subprocess.run(["git"] + list(args), cwd=repo_path, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {' '.join(args)}")
        print(result.stderr)
    return result

def main():
    os.chdir(repo_path)
    
    # Create a random file
    filename = create_random_file()
    print(f"Created file: {filename}")

    # Add file to Git
    git_command("add", filename)
    
    # Commit changes
    git_command("commit", "-m", commit_message)
    print(f"Committed changes with message: '{commit_message}'")
    
    # Push to GitHub
    git_command("push", "origin", branch_name)
    print(f"Pushed changes to branch: {branch_name}")
    
    # Delete the file after committing
    file_path = os.path.join(repo_path, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file: {filename}")
    else:
        print(f"File not found for deletion: {filename}")

if __name__ == "__main__":
    main()
