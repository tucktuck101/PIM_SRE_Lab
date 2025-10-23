# TODO Task Template

Use this template to keep new TODO items consistent. The example below is modeled after task **[01] – `.markdownlint.yaml`**, so you can copy-paste and adjust the fields for future work.

```
## [NN] – `path/to/file_or_folder`
**Status:** Pending | In progress | Blocked | Ready to review | Completed | Needs follow-up
**Goal:** Short summary of the intended outcome.
**Acceptance Criteria:**  
- Bullet list of measurable checks or validator runs.  
- Include rule details, command names, or file expectations.  
- Add as many bullets as needed for reviewers to confirm completion.
**References:** Files, ADRs, or external docs that provide background.  
**Blocked by:** Dependencies, or `None` if ready to start.  
**Parent Task:** Link to parent or `N/A`.  
**Child Tasks:**  
**Note for GPT-Codex** Break larger work into sub-items (optional).
```

### Example – Based on Task 01

```
## [01] – `.markdownlint.yaml`
**Status:** Ready to review
**Goal:** Create baseline Markdown formatting rules for the repo.  
**Acceptance Criteria:**  
- `markdownlint` or `markdownlint-cli` runs with no errors on `README.md` or any sample doc.  
- Rules include: MD013 line length = 120, MD041 first-line heading required, ATX headings enforced, fenced code language required.  
- MD033 (inline HTML) disabled; all other rules enabled or justified inline.  
**References:** `docs/Vison_and_Scope.md`, `docs/02_Glossary.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:**  
**Note for GPT-Codex** Configure exceptions for Mermaid and tables if needed.
```
