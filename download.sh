curl -vLJO -H 'Authorization: token 6c566b5b6d3dce17e0e6511892ea246a20fc69e5' https://api.github.com/repos/comaniac/artifact-test/actions/artifacts
LINK=`python3 -c "import json; data = json.load(open('artifacts', 'r')); i = data['artifacts'][0]['id']; print(f'https://api.github.com/repos/comaniac/artifact-test/actions/artifacts/{i}/zip')"`
curl -vLJO -H 'Authorization: token 6c566b5b6d3dce17e0e6511892ea246a20fc69e5' $LINK
