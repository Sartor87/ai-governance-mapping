# OPA / Rego policies

Policy-as-code enforcement of the machine-checkable controls in
[`../unified_controls.csv`](../unified_controls.csv). Evaluated with
[conftest](https://www.conftest.dev) (which embeds Open Policy Agent).

## Run

```bash
conftest test examples/sample_input.json -p controls/policies
```

`governance.rego` denies when a required control (encryption, input/output
moderation, audit logging, access control, rate limiting) is neither
`satisfied` nor explicitly `not_applicable`, and when a `satisfied` control
carries no `evidence`.

## Input shape

```json
{ "controls": { "AIGOV-003": { "status": "satisfied", "evidence": "KMS" } } }
```

Wire `conftest test` into CI to block deploys that drop a required control.
