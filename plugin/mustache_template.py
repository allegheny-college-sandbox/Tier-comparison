import pystache

template = """
# Create an issue
# labels are optional
- type: issue
  action: create
  repo: {{ repoName }}
  title: {{ issueTitle }}
  body: {{ issueBody }}
  labels:
    {{#labels}}
    - {{.}}
    {{/labels}}
"""

data = {
    "repoName": "CMPSC-203-Allegheny-College-Fall-2022/Tier-comparison",
    "issueTitle": "Green Tier",
    "issueBody": "This is the green tier. You are doing great!",
    "labels": [
        "SheetShuttle",
        "Automated"
    ]
}

renderer = pystache.Renderer()
rendered = renderer.render(template, data)
print(rendered)