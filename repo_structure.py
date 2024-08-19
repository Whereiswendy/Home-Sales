import os

def summarize_repository(repo_path='.'):
    """
    Summarizes the repository structure by listing all files and directories.
    """
    print(f"Repository Summary for: {os.path.abspath(repo_path)}\n")
    for root, dirs, files in os.walk(repo_path):
        # Calculate the level of depth in the directory tree
        level = root.replace(repo_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

# Call the function to summarize the repository structure
summarize_repository()