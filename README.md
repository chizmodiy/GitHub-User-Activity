# GitHub User Activity CLI
**Project URL:** [https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)
https://roadmap.sh/projects/github-user-activity/solutions?u=69c179b133a0ad7a57349ad7

A simple Command Line Interface (CLI) application that fetches the recent activity of a GitHub user using the GitHub API and displays it in the terminal.

This project was built to practice API consumption, handling JSON data, and building functional CLI tools in Python.

## 🚀 Features

- **Fetch Activity**: Retrieves the latest public events for any GitHub user.
- **Human-Readable Output**: Converts technical API event types into clear descriptions (e.g., "Pushed 3 commits to...").
- **Error Handling**: Gracefully handles invalid usernames (404), API rate limits (403), and missing arguments.
- **Zero External Dependencies**: Uses standard Python libraries to interact with the GitHub API.

## 🛠 Tech Stack

- **Language**: Python 3.10+
- **Modules**: `sys`, `json`, `requests` (or `urllib.request`)

## 📂 Installation & Usage

1. Clone or download this repository.
2. Open your terminal in the project directory.
3. Run the script by providing a GitHub username as an argument:

```bash
python main.py <username>
