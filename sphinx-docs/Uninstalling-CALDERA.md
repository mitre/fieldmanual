# Uninstall CALDERA

To uninstall CALDERA, navigate to the directory where CALDERA was installed and recursively remove the directory using the following command: 
```
rm -rf caldera/
```

CALDERA may leave behind artifacts from deployment of agents and operations. Remove any remaining CALDERA agents, files, directories, or other artifacts left on your server and remote systems:
```
rm [ARTIFACT_NAME]
```

Generated reports and exfiled files are saved in `/tmp` on the server where CALDERA is installed.

Some examples of CALDERA artifacts left by agents (on server if agent ran locally, on clients if run remotely):
* **_sandcat.go_**: sandcat agent
* **_manx.go_**: manx agent 
* **_nohup.out_**: ouput file from deployment of certain sandcat and manx agents
