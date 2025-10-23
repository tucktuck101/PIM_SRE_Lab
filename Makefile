SHELL := /bin/sh

PYTHON ?= python3
MARKDOWNLINT ?= markdownlint
VALE ?= vale

.PHONY: help docs-frontmatter docs-markdown docs-style docs-links docs-headings docs-validate

help:
	@echo "Available targets:"
	@echo "  docs-frontmatter  Validate YAML front matter against schema"
	@echo "  docs-markdown     Run markdownlint on docs"
	@echo "  docs-style        Run Vale style checks"
	@echo "  docs-links        Validate internal Markdown links"
	@echo "  docs-headings     Check design doc heading order"
	@echo "  docs-validate     Run all documentation validators"

docs-frontmatter:
	$(PYTHON) tools/validate_frontmatter.py

docs-markdown:
	$(MARKDOWNLINT) docs

docs-style:
	$(VALE) docs

docs-links:
	tools/validate_links.sh

docs-headings:
	$(PYTHON) tools/check_headings_order.py

docs-validate: docs-frontmatter docs-markdown docs-style docs-links docs-headings
	@echo "Documentation validation complete"
