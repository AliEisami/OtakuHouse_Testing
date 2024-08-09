from jira import JIRA, JIRAError
from infra.secret_provider import SecretProvider

jira_api_token = SecretProvider.load_from_file()['jira_token']

# JIRA Server URL
jira_url = 'https://alieisami.atlassian.net'

# API Token Authentication
auth_jira = JIRA(
    basic_auth=('alieisami@gmail.com', jira_api_token),
    options={'server': jira_url}
)


def create_issue(summary, description, project_key, issue_type="Bug"):
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
    }

    try:
        new_issue = auth_jira.create_issue(fields=issue_dict)
        print(f"Issue created: {new_issue.key}")
        return new_issue.key
    except JIRAError as e:
        print(f"Failed to create issue: {e.status_code} {e.text}")
        print(f"Response headers: {e.response.headers}")
        print(f"Response text: {e.response.text}")
        return None
