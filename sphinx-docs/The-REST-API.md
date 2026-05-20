# The REST API

### /api/rest

# Authentication & Base URL
Interact with core Caldera resources via standardized REST API v2 endpoints prefixed with /api/v2.

Requests directed to remote interfaces require API key authorization via the KEY HTTP header. 
You may change the default API Key in the `conf/default.yml` (or local.yml if using --secure flag) using plain text. The API Key will be replaced with an encrypted key for security purposes at server runtime.
For documentation purposes default API Key will be replaced with $API_Key, use your own configured API Key.
 If executing local development or automated testing directly against localhost, the header authorization requirement may be bypassed depending on environment configurations.

# The REST API v2

This documentation covers the modern Caldera REST API v2. The legacy `/api/rest` routing endpoint has been deprecated however some API v1 endpoints still work. 
Full interactive OpenAPI v2 documentation can also be explored dynamically by scrolling to the bottom of the Caldera navigation menu and selecting ["api docs"](http://localhost:8888/api/docs).

# CURL
You may use CURL command line flag in your request. Below are a few examples:

### 1. Request Methods & Headers
These flags control the metadata and the specific action type sent to the target server.

| Flag | Long Form | Purpose | Example |
| --- | --- | --- | --- |
| -X | --request | Specifies the custom HTTP method to use. | -X DELETE |
| -H | --header | Sends custom HTTP headers (like Authentication or content-Type). | -H "KEY: $API_KEY" |
| -A | --user-agent | Sets a custom User-Agent string to identify your request client. | -A "Caldera-Testing-Script" |
| -b | --cookie | Sends a cookie to the server (can be a string or a file). | -b "session=abc123token" |

### 2. Sending Data

When making POST, PUT, or PATCH requests, you use these flags to attach data to the body of your HTTP request.

| Flag | Long Form | Purpose | Example |
| --- | --- | --- | --- |
| -d | --data | Sends data in the body of the request (defaults to sending -X POST automatically if used) | -d \{"name":"test"}
| -F | --form | Submits multipart form data, primarily used for uploading files. | -F "file=@path/to/file.exe" |
| -T | --upload-file | Directly uploads a file to a desgnated URL path (often uses PUT) | -T local_config.yml |

### 3. Response & Output Handling
| Flag | Long Form | Purpose | Example |
| --- | --- | --- | --- |
| -i | --include | Prints the HTTP response headers along with the actual data payload. | curl -i http://localhost:8888 |
| -o | --output | Saves the response body directly to a specified file instead of printing it to the console. | -o agent_profile.json |
| -O | --remote-name | Saves the file locally using the same filename as the remote resource. | -O http://server/file.zip |
| -s | --silent | Mutes curl's progress meter and error messages (highly recommended for scripts). | curl -s http://localhost:8888 |
| -w | --write-out | Displays specific internal extraction variables after a completed transfer (e.g., HTTP status codes). | curl -w "%{http_code}" http://localhost:8888 |

Here are the available REST API functions:

## Agents

Manage deployed implant sessions, query operational parameters, or task direct raw executions.

### View All Agents
Retrieve records and operational states for all active or dead agents.

```bash
curl -H "KEY: $API_KEY" \
-X GET http://localhost:8888/api/v2/agents \
-H "Accept: application/json"
```

#### DELETE

Delete any agent. 
```bash
curl -X GET \
  -H "KEY: $API_KEY" \
  -H "Accept: application/json" \
  http://localhost:8888/api/v2/agents/$AGENT_PAW
```

#### POST

View the abilities a given agent could execute.
```bash
curl -X GET \
  -H "KEY: $API_KEY" \
  -H "Accept: application/json" \
  http://localhost:8888/api/v2/abilities
```

Execute a given ability against an agent, outside the scope of an operation. 
```bash
curl -H "KEY: $API_KEY" \
-X POST http://localhost:8888/plugin/access/exploit \
-d '{"paw":"$PAW","ability_id":"$ABILITY_UUID","obfuscator":"plain-text"}'
```
> You can optionally POST an obfuscator and/or a facts dictionary with key/value pairs to fill in any variables the chosen ability requires.
```bash
{"paw":"$PAW","ability_id":"$ABILITY_ID","obfuscator":"base64","facts":[{"trait":"username","value":"admin"},{"trait":"password", "value":"123"}]}
```

#### GET
Retrieve all stored agents.

```bash
curl -H "KEY:$API_KEY" -X GET http://localhost:8888/api/v2/agents -H accept: application/json
```
## Adversaries

View all abilities for a specific adversary_id (the UUID of the adversary).
```bash
curl -H "KEY:$API_KEY" 'http://localhost:8888/api/rest' -H 'Content-Type: application/json' -d '{"index":"adversaries","adversary_id":"$adversary_id"}'
```

View all abilities for all adversaries.
```bash
curl -H "KEY:$API_KEY" 'http://localhost:8888/api/rest' -H 'Content-Type: application/json' -d '{"index":"adversaries"}'
```

## Operations

View all operations
```bash
curl -H "KEY: $API_KEY" 'http://localhost:8888/api/v2/operations' -H 'accept: application/json'
```
#### DELETE
Delete any operation. Operation ID must be a integer.
```bash
curl -H "KEY:$API_KEY" \
-X 'DELETE' \
'http://localhost:8888/api/v2/operations/$Operation-UUID' \
-H 'accept: application/json'
```

#### PATCH

Change the state of any operation. In addition to finished, you can also use: paused, run_one_link or running.
```bash
curl -X PATCH \
  -H "KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"state": "finished"}' \
  http://localhost:8888/api/v2/operations/$Operation-UUID
```

Because the schema accepts ``partial=True``, you don't have to send all three fields at once. You can mix and match based on what you need to change:

Resume an operation: ```-d '{"state": "running"}'```

Turn off autonomous mode: ```-d '{"autonomous": false}'```

Update multiple fields at once: ```-d '{"state": "running", "autonomous": true}'```

#### PUT

Create a new operation. All that is required is the operation name, similar to creating a new operation
in the browser.
```bash
curl -X PUT -H "KEY:$API_KEY" http://localhost:8888/api/rest -d '{"index":"operations","name":"testoperation1"}'
```
Optionally, you can include:

1) group (defaults to empty string)
2) adversary_id (defaults to empty string)
3) planner (defaults to *batch*)
4) source (defaults to *basic*')
5) jitter (defaults to *2/8*)
6) obfuscator (defaults to *plain-text*)
7) visibility (defaults to *50*)
8) autonomous (defaults to *1*)
9) phases_enabled (defaults to *1*)
10) auto_close (defaults to *0*)

To learn more about these options, read the "What is an operation?" documentation section.           

## /file/upload

Files can be uploaded (see [Exfiltration](Exfiltration.md#exfiltrating-files)) to Caldera by POST'ing a file to the /file/upload endpoint. Uploaded files will be put in the exfil_dir location specified in the default.yml file.

The `X-Request-Id` header should be set to `<agent_hostname>-<agent_paw_print>`. 

#### Example (linux)
```bash
curl -F 'data=@path/to/file' --header "X-Request-Id:`hostname`-#{paw}" http://server_ip:8888/file/upload
```

## /file/download

Files can be downloaded from Caldera through the /file/download endpoint. This endpoint requires an HTTP header called "file" with the file name as the value. When a file is requested, Caldera will look inside each of the payload directories listed in the local.yml file until it finds a file matching the name.

Files can also be downloaded indirectly through the [payload block of an ability](Learning-the-terminology.md).

> Additionally, the [Sandcat plugin](Plugin-library.md) delivery commands utilize the file download endpoint to drop the agent on a host

#### Example
```bash
curl -X POST -H "file:wifi.sh" http://localhost:8888/file/download > wifi.sh
```
