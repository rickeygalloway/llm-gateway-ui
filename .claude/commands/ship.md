Run all quality checks and report results before committing or opening a PR.

## Steps

Run each check in order. If a step fails, report the output and stop — do not proceed to the next step.

1. **Lint**: `ruff check .`
2. **Format check**: `ruff format --check .`
3. **Type check**: `mypy .`
4. **Tests**: `pytest`

## Output format

For each step, print one of:
- `✓ lint` — passed
- `✗ lint — N issues` — failed, followed by the raw output

If all steps pass, end with:
> All checks passed. Safe to commit.

If any step fails, end with:
> Stopped at <step>. Fix the issues above before committing.
