import subprocess

commands=[
[
"az",
"cosmosdb",
"show",
"--name",
"{}".format(subprocess.getoutput("echo $COSMOS_ACCOUNT")),
"--resource-group",
"{}".format(subprocess.getoutput("echo $RESOURCE_GROUP")),
"--output",
"table"
]
]

for cmd in commands:
    subprocess.run(cmd)
