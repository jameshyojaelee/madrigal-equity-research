"""Quick scratchpad for MASH epidemiology and eligible population calculations."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict


@dataclass
class EpiAssumption:
    region: str
    year: int
    population_total: float
    masld_prevalence: float
    mash_f2_f3_prevalence: float
    diagnosed_rate: float
    specialist_care_rate: float


def eligible_population(epi: EpiAssumption) -> Dict[str, float]:
    masld_count = epi.population_total * epi.masld_prevalence
    mash_f2_f3_count = masld_count * epi.mash_f2_f3_prevalence
    diagnosed_count = mash_f2_f3_count * epi.diagnosed_rate
    specialist_care_count = diagnosed_count * epi.specialist_care_rate

    return {
        "region": epi.region,
        "year": epi.year,
        "mash_f2_f3_count": mash_f2_f3_count,
        "diagnosed_count": diagnosed_count,
        "specialist_care_count": specialist_care_count,
    }


def format_table(results: List[Dict[str, float]]) -> str:
    headers = [
        "Region",
        "Year",
        "MASH F2-F3",
        "Diagnosed",
        "Specialist care",
    ]
    lines = [" | ".join(headers), " | ".join(["-" * len(h) for h in headers])]
    for item in results:
        line = " | ".join(
            [
                f"{item['region']}",
                f"{item['year']}",
                f"{item['mash_f2_f3_count']:.0f}",
                f"{item['diagnosed_count']:.0f}",
                f"{item['specialist_care_count']:.0f}",
            ]
        )
        lines.append(line)
    return "\n".join(lines)


def main() -> None:
    data_root = Path(__file__).resolve().parent
    _ = data_root  # Placeholder to hint where CSV inputs would live later.

    assumptions = [
        EpiAssumption("US", 2024, 260_000_000, 0.25, 0.12, 0.15, 0.65),
        EpiAssumption("EU5", 2024, 325_000_000, 0.24, 0.10, 0.12, 0.55),
        EpiAssumption("Japan", 2024, 100_000_000, 0.23, 0.09, 0.18, 0.70),
    ]

    results = [eligible_population(epi) for epi in assumptions]
    print(format_table(results))


if __name__ == "__main__":
    main()
