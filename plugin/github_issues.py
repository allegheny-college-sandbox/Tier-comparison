from sheetshuttle import github_interaction

my_manager = github_interaction.GithubManager()
my_manager.collect_config()

# All collected entries can be posted at once
my_manager.post_all()

# OR they can be posted individually by type
my_manager.post_issues()
# my_manager.post_pull_requests()
# my_manager.post_files()