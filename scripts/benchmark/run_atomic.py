"""Run one raw local model prompt, no code execution. Python 3.10+."""
import argparse
import json
import pathlib
import urllib.request
import datetime

def main():
    p = argparse.ArgumentParser()
    p.add_argument("model")
    p.add_argument("prompt", type=pathlib.Path)
    p.add_argument("output", type=pathlib.Path)
    p.add_argument("--url", default="http://127.0.0.1:11434")
    p.add_argument("--context", type=int, default=4096)
    p.add_argument("--timeout", type=int, default=180)
    p.add_argument("--think", choices=["default","on","off"], default="default")
    a = p.parse_args()
    payload = {"model":a.model,"prompt":a.prompt.read_text(encoding="utf-8"),"stream":False,"keep_alive":"2m","options":{"num_ctx":a.context,"num_predict":1024,"temperature":0.2,"seed":42}}
    if a.think != "default":
        payload["think"] = a.think == "on"
    req = urllib.request.Request(a.url.rstrip("/")+"/api/generate",data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=a.timeout) as res:
        result=json.load(res)
    duration=result.get("eval_duration") or 0
    record={"timestamp":datetime.datetime.now(datetime.timezone.utc).isoformat(),"task":a.prompt.name,"model":a.model,"settings":payload["options"],"think":a.think,"generation_tps":result.get("eval_count",0)*1e9/duration if duration else None,"response":result}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open("x",encoding="utf-8") as f:
        json.dump(record,f,ensure_ascii=False,indent=2)
    print("Saved",a.output,"tokens/s",record["generation_tps"])

if __name__=="__main__":
    main()
