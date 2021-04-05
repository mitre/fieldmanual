# Operation Results

After an operation runs, you can export the results in two different JSON formats: an operation report or operation event logs.

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
      "contact": "HTTP",
      "proxy_receivers": {},
      "display_name": "WORKSTATION1$BYZANTIUM\\Carlomagno",
      "available_contacts": [
        "HTTP"
      ],
      "location": "C:\\Users\\Public\\sandcat.exe",
      "pid": 5896,
      "paw": "pertbn",
      "server": "http://192.168.137.1:8888",
      "links": [
        {
          "status": 0,
          "visibility": {
            "score": 50,
            "adjustments": []
          },
          "pid": "1684",
          "paw": "pertbn",
          "deadman": false,
          "ability": {
            "access": {},
            "payloads": [],
            "executor": "psh",
            "tactic": "defense-evasion",
            "singleton": false,
            "variations": [],
            "timeout": 60,
            "code": null,
            "ability_id": "43b3754c-def4-4699-a673-1d85648fda6a",
            "additional_info": {},
            "uploads": [],
            "description": "Stop terminal from logging history",
            "language": null,
            "buckets": [
              "defense-evasion"
            ],
            "name": "Avoid logs",
            "requirements": [],
            "build_target": null,
            "privilege": null,
            "test": "Q2xlYXItSGlzdG9yeTtDbGVhcg==",
            "platform": "windows",
            "technique_id": "T1070.003",
            "cleanup": [],
            "technique_name": "Indicator Removal on Host: Clear Command History",
            "repeatable": false,
            "parsers": []
          },
          "command": "Q2xlYXItSGlzdG9yeTtDbGVhcg==",
          "score": 0,
          "collect": "2021-02-23 11:48:33",
          "host": "WORKSTATION1",
          "output": "False",
          "unique": "949138",
          "pin": 0,
          "id": 949138,
          "decide": "2021-02-23 11:48:33",
          "jitter": 0,
          "facts": [],
          "cleanup": 0,
          "finish": "2021-02-23 11:48:34"
        }
      ],
      "sleep_max": 5,
      "pending_contact": "HTTP",
      "ppid": 2624,
      "sleep_min": 5,
      "origin_link_id": 0,
      "host": "WORKSTATION1",
      "trusted": true,
      "group": "red",
      "architecture": "amd64",
      "deadman_enabled": true,
      "privilege": "Elevated",
      "created": "2021-02-23 11:48:33",
      "username": "BYZANTIUM\\Carlomagno",
      "platform": "windows",
      "last_seen": "2021-02-23 11:54:37",
      "proxy_chain": [],
      "watchdog": 0,
      "executors": [
        "psh",
        "cmd"
      ],
      "exe_name": "sandcat.exe"
    }
  ],
  "start": "2021-02-23 11:50:12",
  "steps": {
    "pertbn": {
      "steps": [
        {
          "ability_id": "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
          "command": "R2V0LUNoaWxkSXRlbSBDOlxVc2VycyAtUmVjdXJzZSAtSW5jbHVkZSAqLnBuZyAtRXJyb3JBY3Rpb24gJ1NpbGVudGx5Q29udGludWUnIHwgZm9yZWFjaCB7JF8uRnVsbE5hbWV9IHwgU2VsZWN0LU9iamVjdCAtZmlyc3QgNTtleGl0IDA7",
          "delegated": "2021-02-23 11:50:12",
          "run": "2021-02-23 11:50:14",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 7016,
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
          "delegated": "2021-02-23 11:50:17",
          "run": "2021-02-23 11:50:21",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 1048,
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
          "delegated": "2021-02-23 11:50:22",
          "run": "2021-02-23 11:50:27",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 5964,
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
          "delegated": "2021-02-23 11:50:32",
          "run": "2021-02-23 11:50:37",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 3212,
          "description": "create a directory for exfil staging",
          "name": "Create staging directory",
          "attack": {
            "tactic": "collection",
            "technique_name": "Data Staged: Local Data Staging",
            "technique_id": "T1074.001"
          },
          "output": "C:\\Users\\carlomagno\\staged"
        },
        {
          "ability_id": "6469befa-748a-4b9c-a96d-f191fde47d89",
          "command": "UmVtb3ZlLUl0ZW0gLVBhdGggInN0YWdlZCIgLXJlY3Vyc2U=",
          "delegated": "2021-02-23 11:50:42",
          "run": "2021-02-23 11:50:44",
          "status": 0,
          "platform": "windows",
          "executor": "psh",
          "pid": 6184,
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
  "finish": "2021-02-23 11:50:45",
  "planner": "atomic",
  "adversary": {
    "atomic_ordering": [
      "1f7ff232-ebf8-42bf-a3c4-657855794cfe",
      "d69e8660-62c9-431e-87eb-8cf6bd4e35cf",
      "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
      "6469befa-748a-4b9c-a96d-f191fde47d89"
    ],
    "description": "A collection adversary",
    "has_repeatable_abilities": false,
    "adversary_id": "5d3e170e-f1b8-49f9-9ee1-c51605552a08",
    "tags": [],
    "name": "Collection",
    "objective": "495a9828-cab1-44dd-a0ca-66e58177d8cc"
  },
  "jitter": "4/8",
  "objectives": {
    "percentage": 0,
    "description": "This is a default objective that runs forever.",
    "name": "default",
    "goals": [
      {
        "target": "exhaustion",
        "count": 1048576,
        "value": "complete",
        "achieved": false,
        "operator": "=="
      }
    ],
    "id": "495a9828-cab1-44dd-a0ca-66e58177d8cc"
  },
  "facts": [
    {
      "score": 1,
      "technique_id": "",
      "collected_by": "",
      "value": "wav",
      "trait": "file.sensitive.extension",
      "unique": "file.sensitive.extensionwav"
    },
    {
      "score": 1,
      "technique_id": "",
      "collected_by": "",
      "value": "yml",
      "trait": "file.sensitive.extension",
      "unique": "file.sensitive.extensionyml"
    },
    {
      "score": 1,
      "technique_id": "",
      "collected_by": "",
      "value": "png",
      "trait": "file.sensitive.extension",
      "unique": "file.sensitive.extensionpng"
    },
    {
      "score": 1,
      "technique_id": "",
      "collected_by": "",
      "value": "keyloggedsite.com",
      "trait": "server.malicious.url",
      "unique": "server.malicious.urlkeyloggedsite.com"
    },
    {
      "score": 1,
      "technique_id": "T1074.001",
      "collected_by": "pertbn",
      "value": "C:\\Users\\carlomagno\\staged",
      "trait": "host.dir.staged",
      "unique": "host.dir.stagedC:\\Users\\carlomagno\\staged"
    }
  ],
  "skipped_abilities": [
    {
      "pertbn": [
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

## Operation Event Logs
The operation event logs JSON file can be downloaded via the `Download event logs` button on the operations modal after selecting an operation from the drop-down menu. To include command output, users should select the `include agent output` option. Operation event logs will also be automatically written to disk when an operation completes - see the section on [automatic event log generation](#automatic-event-log-generation).

The event logs JSON is a list of dictionary objects, where each dictionary represents an event that occurred during the operation (i.e. each link/command). Users can think of this as a "flattened" version of the operation steps displayed in the traditional report JSON format. However, not all of the operation or agent metadata from the operation report is included in the operation event logs. The event logs do not include operation facts, nor do they include operation links/commands that were skipped either manually or because certain requirements were not met (e.g. missing facts or insufficient privileges). The event log JSON format makes it more convenient to import into databases or SIEM tools.

The event dictionary has the following keys and values:
- `command`: base64-encoded command that was executed
- `delegated_timestamp`: Timestamp string in YYYY-MM-DD HH:MM:SS format that indicates when the operation made the link available for collection
- `collected_timestamp`: Timestamp in YYYY-MM-DD HH:MM:SS format that indicates when the agent collected the link available for collection
- `finished_timestamp`: Timestamp in YYYY-MM-DD HH:MM:SS format that indicates when the agent submitted the link execution results to the C2 server.
- `status`: link execution status
- `platform`: target platform for the agent running the link (e.g. "windows")
- `executor`: executor used to run the link command (e.g. "psh" for powershell)
- `pid`: process ID for the link
- `agent_metadata`: dictionary containing the following information for the agent that ran the link:
    - `paw`
    - `group`
    - `architecture`
    - `username`
    - `location`
    - `pid`
    - `ppid`
    - `privilege`
    - `host`
    - `contact`
    - `created`
- `ability_metadata`: dictionary containing the following information about the link ability:
    - `ability_id`
    - `ability_name`
    - `ability_description`
- `operation_metadata`: dictionary containing the following information about the operation that generated the link event:
    - `operation_name`
    - `operation_start`: operation start time in YYYY-MM-DD HH:MM:SS format
    - `operation_adversary`: name of the adversary used in the operation
- `attack_metadata`: dictionary containing the following ATT&CK information for the ability associated with the link:
    - `tactic`
    - `technique_id`
    - `technique_name`
- `output`: if the user selected `include agent output` when downloading the operation event logs, this field will contain the agent-provided output from running the link command.

Below is a sample output for operation event logs:
```json
[
  {
    "command": "R2V0LUNoaWxkSXRlbSBDOlxVc2VycyAtUmVjdXJzZSAtSW5jbHVkZSAqLnBuZyAtRXJyb3JBY3Rpb24gJ1NpbGVudGx5Q29udGludWUnIHwgZm9yZWFjaCB7JF8uRnVsbE5hbWV9IHwgU2VsZWN0LU9iamVjdCAtZmlyc3QgNTtleGl0IDA7",
    "delegated_timestamp": "2021-02-23 11:50:12",
    "collected_timestamp": "2021-02-23 11:50:14",
    "finished_timestamp": "2021-02-23 11:50:14",
    "status": 0,
    "platform": "windows",
    "executor": "psh",
    "pid": 7016,
    "agent_metadata": {
      "paw": "pertbn",
      "group": "red",
      "architecture": "amd64",
      "username": "BYZANTIUM\\Carlomagno",
      "location": "C:\\Users\\Public\\sandcat.exe",
      "pid": 5896,
      "ppid": 2624,
      "privilege": "Elevated",
      "host": "WORKSTATION1",
      "contact": "HTTP",
      "created": "2021-02-23 11:48:33"
    },
    "ability_metadata": {
      "ability_id": "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
      "ability_name": "Find files",
      "ability_description": "Locate files deemed sensitive"
    },
    "operation_metadata": {
      "operation_name": "My Operation",
      "operation_start": "2021-02-23 11:50:12",
      "operation_adversary": "Collection"
    },
    "attack_metadata": {
      "tactic": "collection",
      "technique_name": "Data from Local System",
      "technique_id": "T1005"
    }
  },
  {
    "command": "R2V0LUNoaWxkSXRlbSBDOlxVc2VycyAtUmVjdXJzZSAtSW5jbHVkZSAqLnltbCAtRXJyb3JBY3Rpb24gJ1NpbGVudGx5Q29udGludWUnIHwgZm9yZWFjaCB7JF8uRnVsbE5hbWV9IHwgU2VsZWN0LU9iamVjdCAtZmlyc3QgNTtleGl0IDA7",
    "delegated_timestamp": "2021-02-23 11:50:17",
    "collected_timestamp": "2021-02-23 11:50:21",
    "finished_timestamp": "2021-02-23 11:50:21",
    "status": 0,
    "platform": "windows",
    "executor": "psh",
    "pid": 1048,
    "agent_metadata": {
      "paw": "pertbn",
      "group": "red",
      "architecture": "amd64",
      "username": "BYZANTIUM\\Carlomagno",
      "location": "C:\\Users\\Public\\sandcat.exe",
      "pid": 5896,
      "ppid": 2624,
      "privilege": "Elevated",
      "host": "WORKSTATION1",
      "contact": "HTTP",
      "created": "2021-02-23 11:48:33"
    },
    "ability_metadata": {
      "ability_id": "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
      "ability_name": "Find files",
      "ability_description": "Locate files deemed sensitive"
    },
    "operation_metadata": {
      "operation_name": "My Operation",
      "operation_start": "2021-02-23 11:50:12",
      "operation_adversary": "Collection"
    },
    "attack_metadata": {
      "tactic": "collection",
      "technique_name": "Data from Local System",
      "technique_id": "T1005"
    }
  },
  {
    "command": "R2V0LUNoaWxkSXRlbSBDOlxVc2VycyAtUmVjdXJzZSAtSW5jbHVkZSAqLndhdiAtRXJyb3JBY3Rpb24gJ1NpbGVudGx5Q29udGludWUnIHwgZm9yZWFjaCB7JF8uRnVsbE5hbWV9IHwgU2VsZWN0LU9iamVjdCAtZmlyc3QgNTtleGl0IDA7",
    "delegated_timestamp": "2021-02-23 11:50:22",
    "collected_timestamp": "2021-02-23 11:50:27",
    "finished_timestamp": "2021-02-23 11:50:27",
    "status": 0,
    "platform": "windows",
    "executor": "psh",
    "pid": 5964,
    "agent_metadata": {
      "paw": "pertbn",
      "group": "red",
      "architecture": "amd64",
      "username": "BYZANTIUM\\Carlomagno",
      "location": "C:\\Users\\Public\\sandcat.exe",
      "pid": 5896,
      "ppid": 2624,
      "privilege": "Elevated",
      "host": "WORKSTATION1",
      "contact": "HTTP",
      "created": "2021-02-23 11:48:33"
    },
    "ability_metadata": {
      "ability_id": "90c2efaa-8205-480d-8bb6-61d90dbaf81b",
      "ability_name": "Find files",
      "ability_description": "Locate files deemed sensitive"
    },
    "operation_metadata": {
      "operation_name": "My Operation",
      "operation_start": "2021-02-23 11:50:12",
      "operation_adversary": "Collection"
    },
    "attack_metadata": {
      "tactic": "collection",
      "technique_name": "Data from Local System",
      "technique_id": "T1005"
    }
  },
  {
    "command": "TmV3LUl0ZW0gLVBhdGggIi4iIC1OYW1lICJzdGFnZWQiIC1JdGVtVHlwZSAiZGlyZWN0b3J5IiAtRm9yY2UgfCBmb3JlYWNoIHskXy5GdWxsTmFtZX0gfCBTZWxlY3QtT2JqZWN0",
    "delegated_timestamp": "2021-02-23 11:50:32",
    "collected_timestamp": "2021-02-23 11:50:37",
    "finished_timestamp": "2021-02-23 11:50:37",
    "status": 0,
    "platform": "windows",
    "executor": "psh",
    "pid": 3212,
    "agent_metadata": {
      "paw": "pertbn",
      "group": "red",
      "architecture": "amd64",
      "username": "BYZANTIUM\\Carlomagno",
      "location": "C:\\Users\\Public\\sandcat.exe",
      "pid": 5896,
      "ppid": 2624,
      "privilege": "Elevated",
      "host": "WORKSTATION1",
      "contact": "HTTP",
      "created": "2021-02-23 11:48:33"
    },
    "ability_metadata": {
      "ability_id": "6469befa-748a-4b9c-a96d-f191fde47d89",
      "ability_name": "Create staging directory",
      "ability_description": "create a directory for exfil staging"
    },
    "operation_metadata": {
      "operation_name": "My Operation",
      "operation_start": "2021-02-23 11:50:12",
      "operation_adversary": "Collection"
    },
    "attack_metadata": {
      "tactic": "collection",
      "technique_name": "Data Staged: Local Data Staging",
      "technique_id": "T1074.001"
    },
    "output": "C:\\Users\\carlomagno\\staged"
  },
  {
    "command": "UmVtb3ZlLUl0ZW0gLVBhdGggInN0YWdlZCIgLXJlY3Vyc2U=",
    "delegated_timestamp": "2021-02-23 11:50:42",
    "collected_timestamp": "2021-02-23 11:50:44",
    "finished_timestamp": "2021-02-23 11:50:44",
    "status": 0,
    "platform": "windows",
    "executor": "psh",
    "pid": 6184,
    "agent_metadata": {
      "paw": "pertbn",
      "group": "red",
      "architecture": "amd64",
      "username": "BYZANTIUM\\Carlomagno",
      "location": "C:\\Users\\Public\\sandcat.exe",
      "pid": 5896,
      "ppid": 2624,
      "privilege": "Elevated",
      "host": "WORKSTATION1",
      "contact": "HTTP",
      "created": "2021-02-23 11:48:33"
    },
    "ability_metadata": {
      "ability_id": "6469befa-748a-4b9c-a96d-f191fde47d89",
      "ability_name": "Create staging directory",
      "ability_description": "create a directory for exfil staging"
    },
    "operation_metadata": {
      "operation_name": "My Operation",
      "operation_start": "2021-02-23 11:50:12",
      "operation_adversary": "Collection"
    },
    "attack_metadata": {
      "tactic": "collection",
      "technique_name": "Data Staged: Local Data Staging",
      "technique_id": "T1074.001"
    }
  }
]
```

### Automatic Event Log Generation
When an operation terminates, the corresponding event logs will be written to disk in the same format as if they were manually requested for download. These event logs will contain command output and will be unencrypted on disk. Each operation will have its own event logs written to a separate file in the directory `$reports_dir/event_logs`, where `$reports_dir` is the `reports_dir` entry in the CALDERA configuration file. The filename will be of the format `operation_$id.json`, where `$id` is the unique ID of the operation.