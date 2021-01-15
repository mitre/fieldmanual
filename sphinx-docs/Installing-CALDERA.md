# Installing CALDERA

## Requirements

* Linux or MacOS operating system
* Python 3.6.1+ (with pip3)

### Recommended

* GoLang 1.13+ (for optimal agent functionality)
* Google Chrome browser 
* Hardware: 8GB+ RAM and 2+ CPUs

## Installation

Start by cloning the CALDERA repository recursively, pulling all available plugins. It is recommended to pass the desired [version/release](https://github.com/mitre/caldera/releases) (should be in x.x.x format). Cloning any non-release branch, including master, may result in bugs.

```
git clone https://github.com/mitre/caldera.git --recursive --branch x.x.x
cd caldera
```

Next, install the pip requirements:

``` 
sudo pip3 install -r requirements.txt
```

Finally, start the server:

```
python3 server.py
```

Once started, log in to http://localhost:8888 with the `red` using the password found in the `conf/local.yml` file (this file will be generated on server start).

To learn how to use CALDERA, navigate to the Training plugin and complete the capture-the-flag style course.

## Docker Deployment

CALDERA can be installed and run in a Docker container.

Start by cloning the CALDERA repository recursively, passing the desired version/release in x.x.x format:

```
git clone https://github.com/mitre/caldera.git --recursive --branch x.x.x
cd caldera
```

Next, build a container:

```
docker build . -t caldera:server
```

Finally, run the docker CALDERA server:

```
docker run -p 7010:7010 -p 7011:7011 -p 7012:7012 -p 8888:8888 caldera:server
```

## Offline Installation

It is possible to use pip to install CALDERA on a server without internet access. Dependencies will be downloaded to a machine with internet access, then copied to the offline server and installed.

To minimize issues with this approach, the internet machine's platform and Python version should match the offline server. For example, if the offline server runs Python 3.6 on Ubuntu 20.04, then the machine with internet access should run Python 3.6 and Ubuntu 20.04.

Run the following commands on the machine with internet access. These commands will clone the CALDERA repository recursively (passing the desired version/release in x.x.x format) and download the dependencies using pip:

```
git clone https://github.com/mitre/caldera.git --recursive --branch x.x.x
mkdir caldera/python_deps
pip3 download -r caldera/requirements.txt --dest caldera/python_deps
```

The `caldera` directory now needs to be copied to the offline server (via `scp`, sneakernet, etc).

On the offline server, the dependencies can then be installed with `pip3`:

```
pip3 install -r caldera/requirements.txt --no-index --find-links caldera/python_deps
```

CALDERA can then be started as usual on the offline server:

```
cd caldera
python3 server.py
```
