import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'status code: {r.status_code}')
response_dict = r.json()
print(f"total repositories {response_dict['total_count']}")
repo_dicts = response_dict['items']
#print(f"repositories returned {len(repo_dicts)}")
print(response_dict.keys())
repo_dict = repo_dicts[6]
#print(f"\nkeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

print('Selected information about repos')
for repo_dict in repo_dicts:
    print(f"\nname: {repo_dict['name']}")
    print(f"owner: {repo_dict['owner']['login']}")
    print(f"stars: {repo_dict['stargazers_count']}")
    print(f"repository: {repo_dict['html_url']}")
