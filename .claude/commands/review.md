Review the code changes or file specified: $ARGUMENTS

If no argument is given, review all staged and unstaged changes (`git diff HEAD`).

## What to check

### Correctness
- Logic errors, off-by-one errors, unreachable code
- Missing return values or inconsistent return types

### Python conventions
- `from __future__ import annotations` at the top of every module
- No bare `except:` — catch specific exceptions or at minimum `except Exception as e`
- No mutable default arguments (e.g. `def f(x=[])`)
- No direct `os.getenv()` in application code — use the project's config module
- No hardcoded secrets, URLs, or magic numbers

### Code quality
- No unused imports
- No dead code (unreachable branches, unused variables)
- Functions and classes are focused — flag anything doing too many things

### Security
- No credentials, tokens, or keys in code or comments
- User input validated before use
- No `eval()` or `exec()` on untrusted input

### Tests
- New logic has test coverage
- Tests are isolated (no side effects on shared state)

## Output format

For each issue found:
- **file:line** — severity (`critical` / `warning` / `suggestion`)
- One sentence describing the problem
- A suggested fix (inline code if short, otherwise a diff block)

End with a **summary line**: `X critical · Y warnings · Z suggestions`
