from github import Github

# GitHub personal access token
access_token = ''

# Create a PyGithub instance using the access token
g = Github(access_token)

try:
    # Get the authenticated user
    user = g.get_user()

    # Get the list of repositories
    repositories = user.get_repos()

    # Iterate over the repositories and print their names
    for repo in repositories:
        print(repo.name)

except Exception as e:
    print(f"An error occurred while listing the repositories: {str(e)}")