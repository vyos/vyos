.PHONY:
verify-definitions:
	find data/interface-definitions/ -type f -print | xargs scripts/verify-schema.py schema/interface_definition.rng

.PHONY:
all:
	verify-definitions
