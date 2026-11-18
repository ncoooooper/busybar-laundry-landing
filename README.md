# Laundry Landing

Use a washer's measured power history to separate normal drum pauses from a finished cycle.

Choose the Home Assistant URL and a power sensor in W or kW. Put a read-only-access HA_TOKEN in the companion environment where available. Thresholds active_watts and idle_watts use watts. After observing an active cycle, continuous low power for settle_seconds is required. A mid-cycle wake-up cancels the countdown. Start the companion before the cycle.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
