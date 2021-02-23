# Operation Results

After an operation runs, you can export the results in an operation report JSON file.

## Operation Report
The operation report JSON consists of a single dictionary with the following keys and values:
- `name`: String representing the name of the operation
- `host_group`: JSON list of dictionary objects containing information about an agent in the operation. 
- `start`: String representing the operation start time in YYYY-MM-DD HH:MM:SS format.
- `steps`: nested JSON dict that maps agent paw strings to an inner dict which maps the string key `steps` to a list of dict objects. Each innermost dict contains information about a step that the agent took during the operation:
    - `ability_id`: String representing the UUID of the corresponding ability for the command. (e.g. `90c2efaa-8205-480d-8bb6-61d90dbaf81b`)
    - `command`: String containing the base64 encoding of the command that was run.
    - `delegated`: Timestamp string in YYYY-MM-DD HH:MM:SS format that indicates when the operation made the link available for collection
    - `run`: Timestamp string in YYYY-MM-DD HH:MM:SS format that indicates when the agent submitted the execution results for the command.
    - `status`: Int representing the status code for the command.
    - `platform`: String representing the operating system on which the command was run.
    - `executor`: String representing which agent executor was used for the command (e.g. `psh` for PowerShell).
    - `pid`: Int representing the process ID for running the command.
    - `description`: String representing the command description, taken from the corresponding ability description.
    - `name`: String representing the command nae, taken from the corresponding ability name.
    - `attack`: JSON dict containing ATT&CK-related information for the command, based on the ATT&CK information provided by the corresponding ability:
        - `tactic`: ATT&CK tactic for the command ability.
        - `technique_name`: Full ATT&CK technique name for the command.
        - `technique_id`: ATT&CK technique ID for the command (e.g. `T1005`)
    - `output`: optional field. Contains the output generated when running the command. Only appears if the user selected the `include agent output` option when downloading the report.
- `finish`: Timestamp string in YYYY-MM-DD HH:MM:SS format that indicates when the operation finished.
- `planner`: Name of the planner used for the operation.
- `adversary`: JSON dict containing information about the adversary used in the operation
    - `atomic_ordering`: List of strings that contain the ability IDs for the adversary.
    - `objective`: objective UUID string for the adversary.
    - `tags`: List of adversary tags
    - `name`: Adversary name
    - `description`: Adversary description
    - `adversary_id`: Adversary UUID string
- `jitter`: String containing the min/max jitter values.
- `objectives`: JSON dict containing information about the operation objective.
- `facts`: list of dict objects, where each dict represents a fact used or collected in the operation.
- `skipped_abilities`: list of JSON dicts that map an agent paw to a list of inner dicts, each representing a skipped ability.
    - `reason`: Indicates why the ability was skipped (e.g. `Wrong Platform`)
    - `reason_id`: ID number for the reason why the ability was skipped.
    - `ability_id`: UUID string for the skipped ability
    - `ability_name`: Name of the skipped ability.

To download an operation report manually, users can click the "Download Report" button under the operation drop-down list in the operation modal. To include the command output, select the `include agent output` checkbox.

Below is an example operation report JSON:
```json
{
  "name": "My Operation",
  "host_group": [
    {
      "platform": "windows",
      "pid": 7096,
      "group": "red",
      "display_name": "WORKSTATION1$BYZANTIUM\\Carlomagno",
      "sleep_min": 5,
      "proxy_receivers": {},
      "watchdog": 0,
      "origin_link_id": 0,
      "proxy_chain": [],
      "privilege": "Elevated",
      "created": "2021-02-23 11:03:04",
      "username": "BYZANTIUM\\Carlomagno",
      "contact": "HTTP",
      "architecture": "amd64",
      "deadman_enabled": true,
      "sleep_max": 5,
      "available_contacts": [
        "HTTP"
      ],
      "ppid": 2624,
      "last_seen": "2021-02-23 11:11:26",
      "paw": "buuxxb",
      "trusted": true,
      "exe_name": "sandcat.exe",
      "executors": [
        "cmd",
        "psh"
      ],
      "links": [
        {
          "cleanup": 0,
          "visibility": {
            "adjustments": [],
            "score": 50
          },
          "pid": "5080",
          "facts": [],
          "score": 0,
          "collect": "2021-02-23 11:03:04",
          "pin": 0,
          "output": "False",
          "finish": "2021-02-23 11:03:05",
          "id": 471619,
          "unique": "471619",
          "command": "Q2xlYXItSGlzdG9yeTtDbGVhcg==",
          "status": 0,
          "decide": "2021-02-23 11:03:04",
          "deadman": false,
          "paw": "buuxxb",
          "jitter": 0,
          "host": "WORKSTATION1",
          "ability": {
            "cleanup": [],
            "platform": "windows",
            "code": null,
            "repeatable": false,
            "name": "Avoid logs",
            "technique_name": "Indicator Removal on Host: Clear Command History",
            "singleton": false,
            "build_target": null,
            "variations": [],
            "technique_id": "T1070.003",
            "privilege": null,
            "buckets": [
              "defense-evasion"
            ],
            "access": {},
            "parsers": [],
            "tactic": "defense-evasion",
            "additional_info": {},
            "language": null,
            "ability_id": "43b3754c-def4-4699-a673-1d85648fda6a",
            "uploads": [],
            "description": "Stop terminal from logging history",
            "payloads": [],
            "requirements": [],
            "test": "Q2xlYXItSGlzdG9yeTtDbGVhcg==",
            "executor": "psh",
            "timeout": 60
          }
        }
      ],
      "server": "http://192.168.137.1:8888",
      "pending_contact": "HTTP",
      "host": "WORKSTATION1",
      "location": "C:\\Users\\Public\\sandcat.exe"
    }
  ],
  "start": "2021-02-23 11:10:42",
  "steps": {
    "buuxxb": {
      "steps": [
        {
          "ability_id": "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
          "command": "R2V0LUNoaWxkSXRlbSBDOlxVc2VycyAtUmVjdXJzZSAtSW5jbHVkZSAqLnBuZyAtRXJyb3JBY3Rpb24gJ1NpbGVudGx5Q29udGludWUnIHwgZm9yZWFjaCB7JF8uRnVsbE5hbWV9IHwgU2VsZWN0LU9iamVjdCAtZmlyc3QgNTtleGl0IDA7",
          "delegated": "2021-02-23 11:10:42",
          "run": "2021-02-23 11:10:46",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 5332,
          "description": "Locate files deemed sensitive",
          "name": "Find files",
          "attack": {
            "tactic": "collection",
            "technique_name": "Data from Local System",
            "technique_id": "T1005"
          }
        },
        {
          "ability_id": "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
          "command": "R2V0LUNoaWxkSXRlbSBDOlxVc2VycyAtUmVjdXJzZSAtSW5jbHVkZSAqLnltbCAtRXJyb3JBY3Rpb24gJ1NpbGVudGx5Q29udGludWUnIHwgZm9yZWFjaCB7JF8uRnVsbE5hbWV9IHwgU2VsZWN0LU9iamVjdCAtZmlyc3QgNTtleGl0IDA7",
          "delegated": "2021-02-23 11:10:47",
          "run": "2021-02-23 11:10:52",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 4372,
          "description": "Locate files deemed sensitive",
          "name": "Find files",
          "attack": {
            "tactic": "collection",
            "technique_name": "Data from Local System",
            "technique_id": "T1005"
          }
        },
        {
          "ability_id": "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
          "command": "R2V0LUNoaWxkSXRlbSBDOlxVc2VycyAtUmVjdXJzZSAtSW5jbHVkZSAqLndhdiAtRXJyb3JBY3Rpb24gJ1NpbGVudGx5Q29udGludWUnIHwgZm9yZWFjaCB7JF8uRnVsbE5hbWV9IHwgU2VsZWN0LU9iamVjdCAtZmlyc3QgNTtleGl0IDA7",
          "delegated": "2021-02-23 11:10:52",
          "run": "2021-02-23 11:10:57",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 7020,
          "description": "Locate files deemed sensitive",
          "name": "Find files",
          "attack": {
            "tactic": "collection",
            "technique_name": "Data from Local System",
            "technique_id": "T1005"
          }
        },
        {
          "ability_id": "6469befa-748a-4b9c-a96d-f191fde47d89",
          "command": "TmV3LUl0ZW0gLVBhdGggIi4iIC1OYW1lICJzdGFnZWQiIC1JdGVtVHlwZSAiZGlyZWN0b3J5IiAtRm9yY2UgfCBmb3JlYWNoIHskXy5GdWxsTmFtZX0gfCBTZWxlY3QtT2JqZWN0",
          "delegated": "2021-02-23 11:10:57",
          "run": "2021-02-23 11:11:02",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 4224,
          "description": "create a directory for exfil staging",
          "name": "Create staging directory",
          "attack": {
            "tactic": "collection",
            "technique_name": "Data Staged: Local Data Staging",
            "technique_id": "T1074.001"
          }
        },
        {
          "ability_id": "6469befa-748a-4b9c-a96d-f191fde47d89",
          "command": "UmVtb3ZlLUl0ZW0gLVBhdGggInN0YWdlZCIgLXJlY3Vyc2U=",
          "delegated": "2021-02-23 11:11:07",
          "run": "2021-02-23 11:11:09",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 4948,
          "description": "create a directory for exfil staging",
          "name": "Create staging directory",
          "attack": {
            "tactic": "collection",
            "technique_name": "Data Staged: Local Data Staging",
            "technique_id": "T1074.001"
          }
        }
      ]
    }
  },
  "finish": "2021-02-23 11:11:10",
  "planner": "atomic",
  "adversary": {
    "atomic_ordering": [
      "1f7ff232-ebf8-42bf-a3c4-657855794cfe",
      "d69e8660-62c9-431e-87eb-8cf6bd4e35cf",
      "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
      "6469befa-748a-4b9c-a96d-f191fde47d89"
    ],
    "objective": "495a9828-cab1-44dd-a0ca-66e58177d8cc",
    "tags": [],
    "name": "Collection",
    "description": "A collection adversary",
    "adversary_id": "5d3e170e-f1b8-49f9-9ee1-c51605552a08"
  },
  "jitter": "4/8",
  "objectives": {
    "name": "default",
    "percentage": 0,
    "description": "This is a default objective that runs forever.",
    "goals": [
      {
        "count": 1048576,
        "operator": "==",
        "value": "complete",
        "target": "exhaustion",
        "achieved": false
      }
    ],
    "id": "495a9828-cab1-44dd-a0ca-66e58177d8cc"
  },
  "facts": [
    {
      "trait": "file.sensitive.extension",
      "value": "wav",
      "technique_id": "",
      "unique": "file.sensitive.extensionwav",
      "score": 1,
      "collected_by": ""
    },
    {
      "trait": "file.sensitive.extension",
      "value": "yml",
      "technique_id": "",
      "unique": "file.sensitive.extensionyml",
      "score": 1,
      "collected_by": ""
    },
    {
      "trait": "file.sensitive.extension",
      "value": "png",
      "technique_id": "",
      "unique": "file.sensitive.extensionpng",
      "score": 1,
      "collected_by": ""
    },
    {
      "trait": "server.malicious.url",
      "value": "keyloggedsite.com",
      "technique_id": "",
      "unique": "server.malicious.urlkeyloggedsite.com",
      "score": 1,
      "collected_by": ""
    },
    {
      "trait": "host.dir.staged",
      "value": "C:\\Users\\carlomagno\\staged",
      "technique_id": "T1074.001",
      "unique": "host.dir.stagedC:\\Users\\carlomagno\\staged",
      "score": 1,
      "collected_by": "buuxxb"
    }
  ],
  "skipped_abilities": [
    {
      "buuxxb": [
        {
          "reason": "Wrong platform",
          "reason_id": 0,
          "ability_id": "1f7ff232-ebf8-42bf-a3c4-657855794cfe",
          "ability_name": "Find company emails"
        },
        {
          "reason": "Wrong platform",
          "reason_id": 0,
          "ability_id": "d69e8660-62c9-431e-87eb-8cf6bd4e35cf",
          "ability_name": "Find IP addresses"
        }
      ]
    }
  ]
}
```