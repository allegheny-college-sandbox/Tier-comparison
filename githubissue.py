import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'EstebanMendez01'
PASSWORD = ''

# The repository to add this issue to
REPO_OWNER = 'CMPSC-203-Allegheny-College-Fall-2022'
REPO_NAME = 'Tier-comparison'

def make_github_issue(title, body=None, assignee=None, milestone=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    print(url)
    # Create an authenticated session to create the issue
    auth = requests.auth.HTTPDigestAuth(USERNAME, PASSWORD)
    #session = requests.session(auth=(USERNAME, PASSWORD))
    session = requests.session()
    session.auth = auth

    # Create our issue
    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'milestone': milestone,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', r.content)

make_github_issue('TEST', 'This is a test', 'EstebanMendez01', 1, ['bug'])