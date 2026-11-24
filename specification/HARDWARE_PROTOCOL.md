# Hardware protocol
Windows PowerShell:
```powershell
nvidia-smi
Get-CimInstance Win32_Processor | Select Name,NumberOfCores,NumberOfLogicalProcessors
Get-CimInstance Win32_PhysicalMemory | Select Capacity,Speed
nvidia-smi --query-gpu=temperature.gpu,utilization.gpu,memory.used,memory.total,power.draw,fan.speed --format=csv -l 2
```
100% GPU in ollama ps means model placement, not GPU utilization. No overclock or voltage changes. Inspect cooling and idle temperatures; first runs short and supervised. Aim below 75 C; monitor 75–80 C; stop at 80 C or earlier if unstable, unusual noise, artifacts or driver errors. These are conservative experimental thresholds, not manufacturer limits. No guarantee of hardware safety; some sensors may be unavailable. Optional supported power-limit reduction only, not necessary. Stop generation, then ollama stop MODEL; exit Ollama if needed.
Install https://ollama.com/download/windows and verify driver compatibility at https://docs.ollama.com/gpu . Close GPU-heavy apps.
