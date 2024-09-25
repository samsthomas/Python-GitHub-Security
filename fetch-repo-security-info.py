import requests

username = 'samsthomas'

api_url = "https://api.github.com/"

repo_name = 'Branch-Test-Repo'

url = f"{api_url}users/{username}/repos/{repo_name}"

repo_data = requests.get(url)
print(repo_data.json())


# params = {
#     "has_wiki": True
#     "allow_update_branch": True
#     'description': 

#}


