# LocalAI-LAB

Experimental evaluation of local language models as assistants to cloud coding agents. No hardware purchases, no changes to existing development workflows or knowledge bases.

## Start here

Open `docs/index.html` in a browser after cloning this repository. The Hungarian dashboard contains the eight-phase experiment guide, checklists, prompts and measurement forms. No backend or build step is required. For a stable browser storage origin, optionally run `python -m http.server 8000 --bind 127.0.0.1 --directory docs` and open http://127.0.0.1:8000.

Export the dashboard state as JSON, review it for sensitive information, then save it as `results/progress.json` and commit it. Import that file on another device. Browser state is not automatically synchronized to GitHub.

## Scope

- P00 Hardware and environment
- P01 Model familiarization
- P02 Atomic benchmark
- P03 SliceBoard project benchmark
- P04 Remote inference
- P05 Serena A/B evaluation
- P06 Real project pilot
- P07 Evaluation and decision

See `specification/`, `benchmarks/`, `scripts/` and `results/`. All results are initially unmeasured. Never publish private source code, credentials, raw agent logs or private network details. Keep experimental workspaces outside tracked files. No license is granted until the owner chooses one.
