from flask import Flask, request, json

from utils import leave_comment

app = Flask(__name__)


@app.route('/githubPullRequest', methods=['POST'])
def comment_pull_request():
    data = request.json

    action_type = data['action']
    if action_type != "opened":
        return

    pull_request = data['pull_request']
    url = pull_request['url']

    leave_comment(url=url)

