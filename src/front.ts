import type {Page} from "@shared/instrument";
import {rect, type Frame} from "@shared/surface";

export function marks(page: Page): Frame {
  if (page.caption !== "WASHER") return [];
  const stage = ["Standby","Washing","Settling","Finished"].indexOf(page.value);
  if (stage < 0) return [];
  return [0,1,2].map(i=>rect("stage"+i,53+i*6,8,4,6,
    i>=stage?"#30404AFF":stage===3?"#87DDBCFF":i===stage-1?"#F7C77BFF":"#668DA0FF"));
}
