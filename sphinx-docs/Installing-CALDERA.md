Installing CALDERA
================

## Requirements

* Linux or MacOS operating system
* Python 3.6.1+ (with Pip3)
* Google Chrome browser
* Recommended hardware to run on is 8GB+ RAM and 2+ CPUs

### Optional

* GoLang 1.13+ (for optimal agent functionality)

## Installation

Start by cloning this repository recursively, passing the desired version/release in x.x.x format. This will pull in all available plugins. If you clone master - or any non-release branch - you may experience bugs.
```
git clone https://github.com/mitre/caldera.git --recursive --branch x.x.x 
```

Next, install the PIP requirements:
```
sudo pip3 install -r requirements.txt
```

Finally, start the server:
```
python3 server.py --insecure
```

Once started, you should log into http://localhost:8888 using the credentials red/admin. Then go into Plugins -> Training and complete the capture-the-flag style training course to learn how to use the framework.
