import requests, sys

try:
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events"
    responce = requests.get(url)
    if responce.status_code == 200:
        data = responce.json()
        for event in data:
            event_type = event['type']  # Тип події (PushEvent, WatchEvent тощо)
            repo_name = event['repo']['name']  # Назва репозиторію
            if event_type == "PushEvent":
                num_commits = len(event['payload'].get('commits', []))
                print(f"- Pushed {num_commits} commits to {repo_name}")
            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")
            elif event_type == "IssuesEvent":
                print(f"- {event['payload']['action'].capitalize()} an issue in {repo_name}")
            else:
                print(f"- {event_type} in {repo_name}")
    elif responce.status_code == 40:
        print(f"Error: User '{username}' not found. Please check the spelling.")
    elif responce.status_code == 403:
        print("Error: API rate limit exceeded. Try again in an hour or use a personal access token.")
except IndexError:
    print('IndexError, please follow main.py [username]')