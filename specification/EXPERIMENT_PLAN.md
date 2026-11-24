# LocalAI Lab – protocol v0.1
Goal: reduce cloud capacity per accepted task without quality loss, using existing hardware only (Ryzen 6C/12T, 16 GB RAM, GTX 1660 presumed 6 GB; verify).
P00: inventory, idle temperature, Ollama installation, serial smoke tests 3B/4B/7B.
P01: interactive prompts, context and output limits, HTTP metrics.
P02: eight atomic tasks per model, clean sessions, identical input, record first attempt before one correction.
P03: SliceBoard, two milestones/four slices, identical starter, external acceptance tests, fresh session each slice; preserve failed runs and distinguish reference-assisted continuation.
P04: LAN inference only, restrict firewall to laptop, no Internet exposure; verify from Mint.
P05: independent Serena A/B on a disposable repository copy, Claude and Codex separately; identical task, commit, model/effort and comparable cache state. Record onboarding and tool overhead.
P06: historical replay then live atomic task in isolated workspace, cloud review and deterministic gates.
P07: compare complete cloud cost (preparation, review, correction, fallback) to cloud-only baseline. No KB edits or integration until explicit approval.
Stop any phase on instability or unsafe scope. Negative outcomes are valid. No automatic routing, no purchases.
