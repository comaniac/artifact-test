"""A simple script to download the latest Github action artifacts."""
import json
import os
import sys


def main(artifact_name, token):
    """Download the latest artifact."""
    os.system(
        f"curl -vLJO -H 'Authorization: token {token}' "
        "https://api.github.com/repos/comaniac/artifact-test/actions/artifacts"
    )

    if not os.path.exists("artifacts"):
        print("Failed to download artifacts")
        sys.exit(0)

    with open("artifacts", "r") as filep:
        data = json.load(filep)

    artifact_url = None
    for artifact in data["artifacts"]:
        if artifact["name"] != artifact_name:
            continue
        artifact_url = artifact["archive_download_url"]
        break

    if artifact_url is None:
        print("Artifact not found")
        sys.exit(0)

    os.system(f"curl -vLJO -H 'Authorization: token {token}' {artifact_url}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: download_latest_artifact.py <artifact_name> <personal access token>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])

