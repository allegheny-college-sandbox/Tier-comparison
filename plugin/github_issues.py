from sheetshuttle import github_interaction
import json
import os
from pathlib import Path

creds = {
    "gh_access_token": os.getenv("ISSUES")
}

with open(".creds.json","w") as fh:
    json.dump(creds, fh)

path = str(Path(os.path.abspath(__file__)).parents[1])
print(path)

my_manager = github_interaction.GithubManager(".creds.json", sources_dir= path + "/config/actually_running")
os.unlink(".creds.json")
# key_file="plugin/key.json", sources_dir="config/actually_running"
my_manager.collect_config()
print("collected config")
# All collected entries can be posted at once
# my_manager.post_all()
# print("posted all")
# OR they can be posted individually by type
my_manager.post_issues()
print("posted issues")
# my_manager.post_pull_requests()
# my_manager.post_files()
# yes
