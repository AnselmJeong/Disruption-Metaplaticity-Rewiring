# User Preferences & Interaction Rules

## Editing Scope
- **Strict Selection Enforcement**: When the user specifies a selection or a specific line range (e.g., "edit only the selected text" or "L241-L245"), the agent MUST NOT make any changes outside of that range.
- **No Collateral Improvements**: Avoid making "collateral" changes to headers, abbreviations (e.g., TRD, E/I), or styling in other parts of the document unless explicitly asked for the entire document. The agent should prioritize the user's focus over global document consistency in these specific requests.

## Terminology
- **Plasticity-promoting therapeutics**: Use "PPTs" instead of "NPETs".
- **Treatment-resistant depression**: Use "TRD" (abbreviated after the first mention in the introduction).
- **TrkB Receptor**: Use "TrkB" only (avoid redundant "receptor").
- **Excitatory-inhibitory**: Use "E/I".
- **Connectivity**: Use "FC" for functional and "SC" for structural connectivity after initial definition.
