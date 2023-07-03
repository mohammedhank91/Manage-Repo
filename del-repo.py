
from github import Github

# GitHub personal access token
access_token = ''

# Prompt the user to enter the repository name
repository_name = input("Enter the name of the repository you want to delete: ")

# Create a PyGithub instance using the access token
g = Github(access_token)

try:
    # Get the authenticated user
    user = g.get_user()

    # Get the repository to delete
    repo = user.get_repo(repository_name)

    # Delete the repository
    repo.delete()

    print(f"Repository '{repository_name}' has been deleted successfully.")

except Exception as e:
    print(f"An error occurred while deleting the repository: {str(e)}")