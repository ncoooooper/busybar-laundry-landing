"""Confirm the end of a washer cycle from a read-only Home Assistant power sensor."""
import json,os,time,urllib.parse,urllib.request
from serve import page
INTERVAL=15
def watts(o):
    host=o["home_assistant"].rstrip("/");sensor=o["entity"]
    req=urllib.request.Request(host+"/api/states/"+urllib.parse.quote(sensor,safe="."),headers={"Authorization":"Bearer "+os.environ["HA_TOKEN"]})
    with urllib.request.urlopen(req,timeout=6) as response:entity=json.load(response)
    power=float(entity["state"]);unit=entity.get("attributes",{}).get("unit_of_measurement","W")
    if unit not in ("W","kW"):raise ValueError("Select a power sensor")
    return power*(1000 if unit=="kW" else 1)
def observe(power,now,o,m):
    high=float(o.get("active_watts",20));low=float(o.get("idle_watts",3));wait=float(o.get("settle_seconds",180))
    if high<=low or wait<=0:raise ValueError("Set active above idle and a positive settling time")
    if power>=high:
        if m.get("state") not in ("Washing","Settling"):m["start"]=now
        m.update(state="Washing",since=None)
    elif m.get("state") in ("Washing","Settling"):
        if power<=low:
            if m.get("since") is None:m["since"]=now
            m["state"]="Finished" if now-m["since"]>=wait else "Settling"
        else:m.update(state="Washing",since=None)
    state=m.get("state","Standby");remain=max(0,wait-(now-m["since"])) if state=="Settling" else None
    return dict(state=state,key=state,alert=state=="Finished",pages=[
       page("WASHER",state,f"Power {power:g} W",f"Wait {int(remain)}s" if remain is not None else "Read-only smart plug"),
       page("LOAD",f"{power:g}W",f"Active above {high:g} W",f"Confirm idle for {wait:g}s")])
def snapshot(o,m):return observe(watts(o),time.monotonic(),o,m)
