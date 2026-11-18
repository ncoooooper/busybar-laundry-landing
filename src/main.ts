import {marks} from "./front";
import {instrument} from "@shared/instrument";

instrument({
  marks,
  "title": "LAUNDRY LANDING",
  "primary": "Laundry Landing",
  "accent": "#78C8DD",
  "cadence": 15000,
  "motion": {enabled:false},
  "setup": "Start companion/serve.py"
});
