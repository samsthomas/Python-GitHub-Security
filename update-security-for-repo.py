import requests
import json

token = ''

HEADERS = {
    "Authorization": f"token {token}"
    }
#variables

username = 'samsthomas'
api_url = "https://api.github.com/"
repo_name = 'Branch-Test-Repo'
url = f"{api_url}repos/{username}/{repo_name}"

print ("The repo we are looking at is", repo_name )

#Check current settings for given repo and print them out

response = requests.get(url, headers = HEADERS)
response_data = response.json()

filtered_data = {
    "has_wiki": response_data.get("has_wiki"),
    "allow_update_branch": response_data.get("allow_update_branch"),
    "has_issues": response_data.get("has_issues"),
    "has_projects": response_data.get("has_projects"),
    "allow_squash_merge": response_data.get("allow_squash_merge"),
    "delete_branch_on_merge": response_data.get("delete_branch_on_merge"),
    "description": response_data.get("description")
}

print ("These are the current settings for", repo_name)
print (filtered_data)

#Update the desired settings 

print ("The settings will now been updated")

data = {
    "description": "updated description 1 time",
    "allow_update_branch": True,
    "has_wiki": True,
    "has_issues": True,
    "has_projects": True,
    "allow_squash_merge": True,
    "allow_auto_merge": True,
    "delete_branch_on_merge": True,

}

response_update = requests.patch(url, data=json.dumps(data), headers = HEADERS)



if response_update.status_code == 200:
    print("Repository updated successfully!")

    updated_data = response_update.json()

    filtered_response = {key: updated_data.get(key) for key in data.keys()}

    print("Updated fields:")
    print(json.dumps(filtered_response, indent=2))


    
else:
    print(f"Failed to update repository. Status code: {response.status_code}")
    print(response_update.text)


# /repos/{owner}/{repo}
