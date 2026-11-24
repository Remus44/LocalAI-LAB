# LocalAI-LAB

Experimental evaluation of local language models as assistants to cloud coding agents. No hardware purchases or changes to existing workflows/KB.

## Start
Clone and open `docs/index.html` (Hungarian, offline, no build). For stable browser storage run `python -m http.server 8000 --bind 127.0.0.1 --directory docs`, open http://127.0.0.1:8000.
Export JSON, review for sensitive data, save as `results/progress.json` and commit. Import on another device. No automatic GitHub sync.

Eight phases: hardware, prompting, atomic benchmark, SliceBoard, remote inference, Serena, real pilot, decision. See specification and benchmarks. All results unmeasured. Never publish private source, credentials, logs or network details. License pending owner decision.
