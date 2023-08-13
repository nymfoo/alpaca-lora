import requests

# The name of the repo to copy.
repo_name = "my-repo"

# The token to use to authenticate with the Hugging Face Hub API.
token = "YOUR_TOKEN"

# The URL of the Hugging Face Hub API.
url = "https://api.huggingface.co/hub/repos"

# Create the request object.
request = requests.post(
    url,
    json={
        "name": repo_name,
        "clone_from": "huggingface/transformers",
    },
    headers={"Authorization": f"Bearer {token}"},
)

# Check the response status code.
if request.status_code == 200:
    # The repo was successfully copied.
    print("Repo successfully copied.")
else:
    # An error occurred.
    print(request.status_code)
    print(request.content)