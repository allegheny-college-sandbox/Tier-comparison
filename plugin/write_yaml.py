import yaml
import mustache_template as mustache_template

message = mustache_template.rendered

# issues = yaml.safe_load(message)

message = message.replace("\n", "<br>")

with open('../config/actually_running/create_issues.yml', 'w') as file:
	prime_service = yaml.dump(message, file)

