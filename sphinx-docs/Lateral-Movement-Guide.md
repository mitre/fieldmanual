Windows Lateral Movement Guide
======================

Using CALDERA's lateral movement and execution abilities, you can perform and test an adversary's capability to move 
laterally within your network. This guide will walk you through some of the necessary setup steps to get started with 
testing lateral movement in a Windows environment.  

## Setup

### Firewall Exceptions and Enabling File and Printer Sharing

The firewall of the target host should not be blocking UDP ports 137 and 138 and TCP ports 139 and 445. The firewall
should also allow inbound file and printer sharing. 

```
netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes
```

### User with Administrative Privileges

This guide will assume a user *with administrative privileges to the target host* has been compromised and that a CALDERA
agent has been spawned with this user's privileges. Scenarios where (1) the user has administrative privileges but is 
not a domain account and (2) the user has administrative privileges and is a domain account are addressed in the 
following sub sections.

#### Non-Domain Account
If the user with administrative privileges is *not* a domain account, remote UAC must be disabled on the target host by
updating the following value in the registry. The command below will overwrite the existing registry value or add the
vlaue if it doesn't already exist.
```
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```
After executing the above command, restart the host to apply the changes.


#### Domain Account
No additional setup should be necessary. 

### Additional Considerations

1. Ensure GPO/SRP or antivirus is not blocking remote access to shares.
2. Ensure at least ADMIN$, C$, and IPC$ shares exist on the target host.

## Lateral Movement Using CALDERA
Lateral movement can be a combination of two steps. The first requires confirmation of remote access to the next target 
host and the movement or upload of the remote access tool (RAT) executable to the host. The second part requires 
*execution* of the binary, which upon callback of the RAT on the new host would complete the lateral movement. 

Most of CALDERA's lateral movement and execution abilities found in Stockpile have fact or relationship requirements 
that must be satisfied. This information may be passed to the operation in two ways:
1. The fact and relationship information may be added to an operation's source. A new source can be created or this
information can be added to an already existing source as long as that source is used by the operation. When configuring
an operation, open the "**AUTONOMOUS**" drop down section and select "Use [insert source name] facts" to indicate to the 
operation that it should take in fact and relationship information from the selected source.
2. The fact and relationship information can be discovered by an operation. This requires additional abilities to be run
prior to the lateral movement and execution abilities to collect the necessary fact and relationship information 
necessary to satisfy the ability requirements. 

### Moving the Binary
There are several ways a binary can be moved or uploaded from one host to another. Some example methods used in 
CALDERA's lateral movement abilities include:
1. WinRM
2. SCP
3. wmic
4. SMB
5. psexec
 
Based on the tool used, additional permissions may need to be changed in order for users to conduct these actions 
remotely.

### Execution of the Binary
CALDERA's Stockpile execution abilities relevant to lateral movement mainly use wmic to remotely start the binary. Some 
additional execution methods include modifications to Windows services, scheduled tasks, and Registry Run keys or start 
up folder to execute the binary.

## Example Lateral Movement Profile
This section will walkthrough the necessary steps for proper execution of the Service Creation Lateral Movement
adversary profile. This section will assume successful setup from the previous sections mentioned in this guide and that
a 54ndc47 agent has been spawned with administrative privileges to the remote target host.
1. Go to `navigate` pane > `Advanced` > `sources`. This should open a new sources modal in the web GUI.
2. Click the toggle to create a new source. Enter "SC Source" as the source name. Then enter `remote.host.fqdn` as the 
fact trait and the FQDN of the target host you are looking to move laterally to as the fact value. Click `Save` once 
source configuration ahs been completed.
3. Go to `navigate` pane > `Campaigns` > `operations`. Click the toggle to create a new operation. Under 
`BASIC OPTIONS` select the group with the relevant agent and the Service Creation Lateral Movement profile. Under 
`AUTONOMOUS`, select `Use SC Source facts`. If the source created from the previous step is not available in the 
drop down, try refreshing the page. 
4. Once operation configurations have been completed, click `Start` to start the operation. **NOTE: this adversary
profile uses an ability that creates and starts a Windows service. Because the 54ndc47 executable will *not* respond
as an expected service executable would, it is assumed to have timed out/did not respond in a timely manner. CALDERA
will also therefore assume this ability has failed or timed out.**
5. Check the agents list for a new agent on the target host.  