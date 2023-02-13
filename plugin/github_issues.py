from sheetshuttle import github_interaction

my_manager = github_interaction.GithubManager(key_file="plugin/key.json", sources_dir="config/actually_running")
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