# CfgDiff usage

## Input rules

Supported extensions: `.json`, `.yaml`, `.yml`, `.toml`, `.ini`, `.cfg`.
Ini comments starting with `#` or `;` are ignored.

## Output fields

Each line is `<path>: <message>`.

- `path` is the dotted key path from the config root.
- `message` is one of:
  - `value changed: <left> -> <right>`
  - `missing on left`
  - `missing on right`

## Exit codes

- `0` — identical configurations
- `1` — differences found
- `2` — bad input, missing file, or unsupported format

## CLI entry points

The package exposes two invocation paths:

- Installed command: `cfgdiff left.ini right.ini`
- Module invocation: `python -m cfgdiff left.ini right.ini`

Both paths share the same exit codes and output format.
