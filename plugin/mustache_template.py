import ruamel.yaml
import pystache
import argparse
import os

# Define command line argument parser
parser = argparse.ArgumentParser(description='Create GitHub issues for different tiers.')
parser.add_argument('tier', type=str, choices=['green', 'yellow', 'red'], help='The tier to create the issue for.')
args = parser.parse_args()

# Define the YAML template
template = """
# Create an issue
# labels are optional
- type: issue
  action: create
  repo: {{ repoName }}
  title: {{ issueTitle }}
  body: "{{ issueBody }}"
  labels:
    {{#labels}}
    - {{.}}
    {{/labels}}
"""

# Load the data for the specified tier
if args.tier == 'green':
    data = {
        "repoName": "allegheny-college-sandbox/Tier-tester",
        "issueTitle": "Green Tier",
        "issueBody": open(os.path.abspath("/templates/green_tier.md")).read(),
        "labels": [
            "SheetShuttle",
            "Automated"
        ]
    }
elif args.tier == 'yellow':
    data = {
        "repoName": "allegheny-college-sandbox/Tier-tester",
        "issueTitle": "Yellow Tier",
        "issueBody": open(os.path.abspath("/templates/yellow_tier.md")).read(),
        "labels": [
            "SheetShuttle",
            "Automated"
        ]
    }
else:
    data = {
        "repoName": "allegheny-college-sandbox/Tier-tester",
        "issueTitle": "Red Tier",
        "issueBody": open(os.path.abspath("/templates/red_tier.md")).read(),
        "labels": [
            "SheetShuttle",
            "Automated"
        ]
    }

# Render the template with the specified data
renderer = pystache.Renderer()
message = renderer.render(template, data)

# Set up the YAML dumper
yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True
yaml.explicit_start = True
yaml.explicit_end = True

# Dump the YAML to a file
with open('../config/actually_running/create_issues.yml', 'w') as file:
    yaml.dump(yaml.load(message), file)
