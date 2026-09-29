"""Show that the NIAC duration statements do not identify the published IRR.

Both schedules below stay inside the report's stated windows: development and
production inside four years, deployment inside the following two years, and
NASA funding inside five years. They are not candidate reproductions. A third
back-loaded schedule is included because some of its cases do not even have a
single IRR.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def _load():
    path = Path(__file__).with_name("model.py")
    spec = importlib.util.spec_from_file_location("sowers_model", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = _load()
    base = json.loads(Path(__file__).with_name("original_inputs.json").read_text(encoding="utf-8"))
    schedules = {
        "uniform_inside_stated_windows": {},
        "front_loaded_inside_stated_windows": {
            "development_weights": [1, 0, 0, 0],
            "production_weights": [1, 0, 0, 0],
            "transportation_weights": [0, 0, 0, 0, 1, 0],
            "nasa_investment_weights": [1, 0, 0, 0, 0],
        },
        "back_loaded_inside_stated_windows": {
            "development_weights": [0, 0, 0, 1],
            "production_weights": [0, 0, 0, 1],
            "transportation_weights": [0, 0, 0, 0, 0, 1],
            "nasa_investment_weights": [0, 0, 0, 0, 1],
        },
    }
    for name, overrides in schedules.items():
        print(name)
        for case in ("commercial", "ppp_lunar", "ppp_lunar_mars"):
            document = json.loads(json.dumps(base))
            document["case"] = case
            document["timing"] = "illustrative_uniform_annual"
            if overrides:
                document["timing_overrides"] = overrides
            timed = module.run(document)["timed_cash_flow"]
            print(
                " ",
                case,
                "company_irr",
                timed["company_irr_percent"],
                timed["company_irr_status"],
                "nasa_irr",
                timed["nasa_irr_percent"],
                timed["nasa_irr_status"],
            )


if __name__ == "__main__":
    main()
