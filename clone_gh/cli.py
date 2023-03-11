import json
import os
import requests
import git
import argparse


def clone_starred_repos(username, language=None, output_dir=None, access_token_file=None):
    # Github API endpoint
    url = f"https://api.github.com/users/{username}/starred"

    # Load Github access token from file if provided
    if access_token_file is not None:
        with open(access_token_file, 'r') as f:
            access_token = f.readline().strip()
        headers = {'Authorization': 'token ' + access_token}
    else:
        headers = None

    # List to store all starred repositories
    starred_repos = []

    # Make initial API request to get first page of starred repositories
    response = requests.get(url, headers=headers)

    # Loop through the response and add each repository to the list
    while response.status_code == 200:
        starred_repos += response.json()

        # Check if there are more pages of results
        if 'next' in response.links.keys():
            # Make another API request for the next page of results
            url = response.links['next']['url']
            response = requests.get(url, headers=headers)
        else:
            # No more results to fetch
            break

    # print("Starred", starred_repos)

    # Loop through the list of starred repositories and clone each one
    for repo in starred_repos:
        if language is None or repo['language'] == language:
            repo_name = repo['name']
            repo_owner = repo['owner']['login']
            repo_url = repo['clone_url']
            if output_dir is None:
                output_dir = os.getcwd()
            cloned_folder_name = os.path.join(repo_owner, repo_name)
            cloned_folder_path = os.path.join(output_dir, cloned_folder_name)
            print(f"Cloning repository {repo_name} from user {repo_owner}...")
            git.Repo.clone_from(repo_url, cloned_folder_path)


def clone_user_repos(username, language=None, output_dir=None, access_token_file=None):
    # Github API endpoint
    url = f"https://api.github.com/users/{username}/repos"

    # Load Github access token from file if provided
    if access_token_file is not None:
        with open(access_token_file, 'r') as f:
            access_token = f.readline().strip()
        headers = {'Authorization': 'token ' + access_token}
    else:
        headers = None

    # List to store all repositories
    user_repos = []

    # Make initial API request to get first page of repositories
    response = requests.get(url, headers=headers)

    # Loop through the response and add each repository to the list
    while response.status_code == 200:
        user_repos += response.json()

        # Check if there are more pages of results
        if 'next' in response.links.keys():
            # Make another API request for the next page of results
            url = response.links['next']['url']
            response = requests.get(url, headers=headers)
        else:
            # No more results to fetch
            break

    # Loop through the list of repositories and clone each one
    for repo in user_repos:
        if language is None or repo['language'] == language:
            repo_name = repo['name']
            repo_url = repo['clone_url']
            if output_dir is None:
                output_dir = os.getcwd()
            cloned_folder_path = os.path.join(output_dir, username, repo_name)
            print(f"Cloning repository {repo_name} from user {username}...")
            git.Repo.clone_from(repo_url, cloned_folder_path)



def get_language_alias_map():
    cache_file = 'languages.json'
    package_dir = os.path.dirname(os.path.abspath(__file__))
    pkg_cache_file = os.path.join(package_dir, 'languages.json')
    response = requests.get('https://api.github.com/languages')
    if response.ok:
        languages = response.json()
    elif os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            languages = json.load(f)
    elif os.path.exists(pkg_cache_file):
        with open(cache_file, 'r') as f:
            languages = json.load(f)
    else:
        languages = []

    # Create a mapping of aliases to primary names
    alias_map = {}
    for language in languages:
        name = language['name']
        aliases = language.get('aliases', [])
        alias_map[name] = name
        for alias in aliases:
            alias_map[alias] = name

    return alias_map



def main():
    parser = argparse.ArgumentParser(
        description='Clone Github repositories for a given user. Supports cloning of liked repositories and all public repositories. Filters by programming language if specified.')
    parser.add_argument('username', type=str, help='Github username')
    parser.add_argument('--language', '-l', type=str, default=None, help='Programming language to filter by')
    parser.add_argument('--output_dir', '-o', type=str, default=None, help='Output directory for cloned repositories')
    parser.add_argument('--access_token_file', '-a', type=str, default=None, help='File containing Github access token')
    parser.add_argument('--task', '-t', type=str, default='likes', help='Task to perform: likes or repos')
    args = parser.parse_args()

    alias_map = get_language_alias_map()
    language = alias_map[args.language]

    if args.task == 'likes':
        clone_starred_repos(args.username, language, args.output_dir, args.access_token_file)
    elif args.task == 'repos':
        clone_user_repos(args.username, language, args.output_dir, args.access_token_file)
    else:
        print('Invalid task specified. Please specify either "likes" or "repos".')

if __name__ == '__main__':
    main()

