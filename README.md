# password-generator

Generate a secure, NIST-aligned password and copy it to the clipboard. Uses the
`secrets` module for cryptographically strong randomness.

## What it does

- Generates a password with a 12-character minimum (NIST SP 800-63B guidance for
  machine-generated secrets)
- Optional uppercase, digits, and special characters, with a guarantee that at
  least one of each requested class is present
- Reports a rough strength rating (Weak / Moderate / Strong / Very Strong) based
  on length, character diversity, and uniqueness
- Copies the result to the clipboard

## Requirements

- Python 3.8+
- [`pyperclip`](https://pypi.org/project/pyperclip/) for clipboard support

```bash
pip install pyperclip
```

## Usage

```bash
python3 password-generator.py
```

To change length or character classes, edit the `length`, `use_uppercase`,
`use_numbers`, and `use_special_chars` values near the bottom of the script.

## License

MIT. See [LICENSE](LICENSE).
