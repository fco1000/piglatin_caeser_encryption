# Examples

This folder contains example input files and sample outputs you can use to exercise the CLI and engine.

- `sample_input.txt` — short test paragraph (also available at repository root).
- `gideon_story.txt` — longer input useful for stress-testing punctuation, hyphenation, and sentence variety.

To run an example with the Python CLI (PowerShell):

```powershell
python -m python_cli.main -i .\docs\examples\sample_input.txt -o .\docs\examples\sample_output.txt -k 5 -m encrypt
```
