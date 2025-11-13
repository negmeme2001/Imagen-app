# scripts/auto_rev.py
"""
Automated Code Review Script
Author: Mohamed Negm
"""

import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load .env if run locally

# __define-ocg__ variable for commit SHA
commit_sha = os.getenv("GITHUB_SHA")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_LLM = os.getenv("OPENROUTER_LLM", "deepseek/deepseek-r1-0528:free")
GITHUB_API_KEY = os.getenv("G_API_KEY")
GITHUB_REPO = os.getenv("G_REPO")

_client = OpenAI(api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")

def get_latest_commit_diff():
    """Fetch diff for latest commit"""
    headers = {"Authorization": f"Bearer {GITHUB_API_KEY}"}
    url = f"https://api.github.com/repos/{GITHUB_REPO}/commits/{commit_sha}"
    print(f"Fetching diff for commit: {commit_sha}")
    response = requests.get(url, headers=headers)
    data = response.json()
    diffs = []
    for f in data.get("files", []):
        patch = f.get("patch")
        if patch:
            diffs.append(f"File: {f['filename']}\n{patch}")
    return "\n\n".join(diffs)

def get_review_from_llm(diff_text):
    """Send diff to OpenRouter model for review"""
    response = _client.chat.completions.create(
        model=OPENROUTER_LLM,
        messages=[
            {
                "role": "user",
                "content": f"Review the following code diff:\n\n{diff_text}"
            }
        ]
    )
    return response.choices[0].message.content

def post_review_comment(body):
    """Post review as a comment on the commit"""
    headers = {
        "Authorization": f"Bearer {GITHUB_API_KEY}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/repos/{GITHUB_REPO}/commits/{commit_sha}/comments"
    data = {"body": body}

    print(f"📤 Posting review comment to: {url}")
    resp = requests.post(url, headers=headers, json=data)

    print(f"Response status: {resp.status_code}")
    print(f"Response body: {resp.text}")

    if resp.status_code == 201:
        print("✅ Review comment successfully posted!")
    else:
        print("⚠️ Failed to post review comment.")

if __name__ == "__main__":
    diff_text = get_latest_commit_diff()
    if not diff_text:
        print("No code changes found in this commit.")
    else:
        review = get_review_from_llm(diff_text)
        post_review_comment(review)
        print("✅ Review posted successfully!")