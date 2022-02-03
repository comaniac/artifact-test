## Github Action Samples
This is just a repo that I use to experiment Github Actions.
All experimented actions will be added to this README with descriptions, so feel free to take any of them if that fits your needs.

### Artifacts
**Workflow File**: `.github/workflows/artifacts.yml`

**Description:** This workflow demonstrates that how to use artifacts at the subsequent jobs in the same run, and the other runs of this workflow.

### Work on any directory in container
**Workflow File**: `.github/workflows/symbolic.yml`

**Description:** This workflow demonstrates that how to access any directory in the workflow container using symbolic link. The requirement comes when you work on a Github Action in a container, Github Action does not allow you to access the directories outside of the workspace.

### Automatic Create Pull Requests
**Workflow File**: `.github/workflows/create-pull-request.yml`

**Description:** This workflow demonstrates how to automatically create a pull request using Github Action. This can be used to update submodules regularly, for example.

### Reuse CCache
**Workflow File**: `.github/workflows/reuse-ccache.yml`

**Description:** This workflow demonstrates how to reuse ccache crossing runs and nodes. Although Github Workflow re-assigns $HOME and ccache is able to maintain the cache under $HOME/.ccache, this cache can only be reused when running on the same runner. This workflow shows that ccache cache can be reused even on different runners by uploading the .ccache as an artifact in the current run, and download the artifact in the next run.

### Conditional Steps
**Workflow File**: `.github/workflows/modes.yml`

**Description:** This workflow demonstrates how to execute steps conditionally.

### Environment Variables
