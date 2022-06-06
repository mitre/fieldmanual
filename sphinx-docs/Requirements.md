# Requirements

Requirements are a mechanism used by CALDERA to determine whether an ability should be run in the course of an
operation. By default, CALDERA supplies several requirements [within the Stockpile plugin](https://github.com/mitre/stockpile/tree/master/app/requirements)
that can be used by an ability to ensure the ability only runs when the facts being used by the ability command meet
certain criteria.

Requirements are defined in a Python module and are then referenced inside an ability. All requirements must be provided
at least a `source` fact to enforce the defined requirement on. Depending on the requirement module, a requirement
module may also need an `edge` value and a `target` fact to be provided as arguments to enforce the defined requirement.

## Example

Let's look at the **Impersonate User** ability from Stockpile as an example.

```yaml
- id: 3796a00b-b11d-4731-b4ca-275a07d83299
  name: Impersonate user
  description: Run an application as a different user
  tactic: execution
  technique:
    attack_id: T1059.001
    name: "Command and Scripting Interpreter: PowerShell"
  platforms:
    windows:
      psh:
        command: |
          $job = Start-Job -ScriptBlock {
            $username = '#{host.user.name}';
            $password = '#{host.user.password}';
            $securePassword = ConvertTo-SecureString $password -AsPlainText -Force;
            $credential = New-Object System.Management.Automation.PSCredential $username, $securePassword;
            Start-Process Notepad.exe -NoNewWindow -PassThru -Credential $credential;
          };
          Receive-Job -Job $job -Wait;
  requirements:
    - plugins.stockpile.app.requirements.paw_provenance:
      - source: host.user.name
    - plugins.stockpile.app.requirements.basic:
      - source: host.user.name
        edge: has_password
        target: host.user.password
```

Notice in the ability command, two facts `host.user.name` and `host.user.password` will be used. The `paw_provenance`
requirement enforces that only `host.user.name` facts that were discovered by the agent running the ability can be used
(i.e. fact originated from the same `paw`). In the scenario this ability is run against two agents on two different
hosts where multiple `host.user.name` and `host.user.password` facts were discovered, the `paw_provenance` prevents
`host.user.name` and `host.user.password` facts discovered by the second agent on the second host from being used by
the first agent on the first host. Thus, the agent would only be able to use the `host.user.name` and
`host.user.password` facts that it discovered itself, emulating the natural operation flow of an adversary (they would
not be able to use information that they did not discover themselves).

Additionally, the `basic` requirement enforces that only `host.user.name` facts with an existing `has_password`
relationship to an existing `host.user.password` fact may be used. Brute forcing all available combinations of
`host.user.name` facts and `host.user.password` facts could result in high numbers of failed login attempts or locking
out an account entirely. The `basic` requirement ensures that the user and password combination used has a high chance
of success since the combination's relationship has already been established by a previous ability.

The combined effect these requirements have ensures that the CALDERA operation will only attempt reliable combinations
of `host.user.name` and `host.user.password` facts specific to the agent running the ability, instead of arbitrarily
attempting all possible combinations of `host.user.name` and `host.user.password` facts available to the agent.
