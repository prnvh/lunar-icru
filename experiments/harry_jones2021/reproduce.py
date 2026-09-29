"""Generate forward results and a separate comparison; no fitted parameters."""
from pathlib import Path
import hashlib
import json
from model import run

HERE = Path(__file__).resolve().parent


def main():
    case = json.loads((HERE / "native_case.json").read_text())
    calculated = run(case)
    reported = json.loads((HERE / "reported_outputs.json").read_text())
    comparisons = []
    for i, row in enumerate(calculated["rows"]):
        for name, label in (("oxygen_pilot", "oxygen"), ("oxygen_production", "oxygen"),
                            ("hydrogen", "hydrogen"), ("recycling", "recycling")):
            b = row["processes"][name]["branches"]["table_behavior_inference"]
            errors = {k: b[k + "_musd"] - reported[label][k][i]
                      for k in ("plant", "launch", "operations", "lcc")}
            comparisons.append({"rate_t_per_year": row["rate_t_per_year"], "process": name,
                                "branch": "table_behavior_inference", "error_musd": errors,
                                "all_cells_within_half_musd": all(abs(x) <= .5 for x in errors.values())})
        e = row["processes"]["earth_supply"]
        errors = {"containers": e["container_cost_eq18_musd"] - reported["earth_supply"]["containers"][i],
                  "launch": e["launch_musd"] - reported["earth_supply"]["launch"][i],
                  "lcc": e["lcc_eq18_musd"] - reported["earth_supply"]["lcc"][i]}
        comparisons.append({"rate_t_per_year": row["rate_t_per_year"], "process": "earth_supply",
                            "branch": "literal_eq18", "error_musd": errors,
                            "all_cells_within_half_musd": all(abs(x) <= .5 for x in errors.values())})
    (HERE / "forward_results.json").write_text(json.dumps(calculated, indent=2) + "\n")
    (HERE / "comparison.json").write_text(json.dumps(comparisons, indent=2) + "\n")
    for x in comparisons:
        print(x["rate_t_per_year"], x["process"], x["all_cells_within_half_musd"],
              {k: round(v, 4) for k, v in x["error_musd"].items()})


if __name__ == "__main__":
    main()
