import yaml
import mustache_template as mustache_template

message = mustache_template.rendered

# issues = yaml.safe_load(message)

with open('../config/actually_running/create_issues.yml', 'w') as file:
	prime_service = yaml.dump(message, file)

