package main

# Policy-as-code for the machine-checkable governance controls.
# Evaluate with conftest (https://www.conftest.dev):
#   conftest test examples/sample_input.json -p controls/policies
#
# Input shape (see examples/sample_input.json):
#   { "controls": { "AIGOV-003": { "status": "satisfied" }, ... } }

import rego.v1

# Controls that must be enforced in code for any deployed LLM system.
required_controls := {
	"AIGOV-003", # encryption at rest
	"AIGOV-006", # prompt-injection / input moderation
	"AIGOV-007", # output handling / content safety
	"AIGOV-009", # audit logging
	"AIGOV-010", # access control / least privilege
	"AIGOV-015", # rate limiting / resource controls
}

satisfied(id) if input.controls[id].status == "satisfied"

waived(id) if input.controls[id].status == "not_applicable"

# Deny when a required control is neither satisfied nor explicitly waived.
deny contains msg if {
	some id in required_controls
	not satisfied(id)
	not waived(id)
	msg := sprintf("required control %v is not satisfied or waived", [id])
}

# A satisfied control must carry evidence.
deny contains msg if {
	some id in required_controls
	satisfied(id)
	not input.controls[id].evidence
	msg := sprintf("control %v is marked satisfied but has no evidence", [id])
}
