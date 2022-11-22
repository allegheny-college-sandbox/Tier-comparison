import requests
import json

token = "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"

headers = {
	"Authorization" : "token {}".format(token)
}
data = {
	"title" : "Test",
	# "body" : "This is a test",
	# "assignee" : "tmiller-10",
	# "milestone" : 1,
	# "labels" : [bugs]
}

username = "tmiller-10"

Reponame = "Temperature-Conversion1"
url = "https://api.github.com/repos/tmiller-10/Temperature-Conversion1/issues"


print(url)
print(requests.post(url, data=json.dumps(data), headers=headers))
print("SUCCESS")



