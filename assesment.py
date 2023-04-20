import requests as r
from dotenv import load_dotenv
import json
import os
from datetime import datetime, timedelta

load_dotenv()

GITHOUB_TOKEN = os.getenv("GIT_TOKEN")

owner = "yankils"
repo = "Simple-DevOps-Project"
now = datetime.now()
last_week = now-timedelta(days=7)
date_range= f'{last_week.strftime("%Y-%m-%d")}..{now.strftime("%Y-%m-%d")}'
url = f'https://api.github.com/repos/{owner}/{repo}/pulls?state=all&since={date_range}'

headers={
'Authorization': f'token {GITHOUB_TOKEN}'

}

response = r.get(url, headers=headers)

open_issues =0
closed_issues = 0
draft_issues =0
for issues in response.json():
    if issues['state'] == "open":
        open_issues +=1
    elif issues['state']=="closed":
        closed_issues +=1
    if issues["state"]=="draft":
        draft_issues +=1
print(f'opened issues: {open_issues}')
print(f'draft issues: {draft_issues}')
print(f'Closed issues: {closed_issues}')

