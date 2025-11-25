"""Generate the Madrigal rNPV Excel template with predefined sheets and headers."""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook

SHEET_HEADERS = {
    "Assumptions": [
        "Category",
        "Variable",
        "Description",
        "Unit",
        "Base",
        "Bear",
        "Bull",
        "Notes",
    ],
    "Epi_MarketSizing": [
        "Region",
        "Year",
        "Population_total",
        "MASLD_prevalence",
        "MASH_F2_F3_prevalence",
        "Diagnosed_rate",
        "Specialist_care_rate",
        "Notes",
    ],
    "Pricing_Access": [
        "Region",
        "Year",
        "List_price_per_year",
        "Gross_to_net_percent",
        "Net_price_per_year",
        "Rebate_notes",
        "Payer_restrictions",
        "Access_notes",
    ],
    "Penetration_Share": [
        "Region",
        "Year",
        "Eligible_population",
        "Rezdiffra_penetration_percent",
        "Treated_patients_Rezdiffra",
        "Competitor_penetration_percent",
        "Treated_patients_competitors",
        "Notes",
    ],
    "Revenue_Build": [
        "Region",
        "Year",
        "Treated_patients_Rezdiffra",
        "Average_duration_years",
        "Treatment_years",
        "Net_price_per_year",
        "Net_revenue_Rezdiffra",
        "Notes",
    ],
    "PnL_CF": [
        "Year",
        "Net_revenue_total",
        "COGS_percent",
        "COGS",
        "SGA_percent_of_sales",
        "SGA",
        "R&D",
        "Operating_income",
        "Free_cash_flow",
    ],
    "rNPV_EquityBridge": [
        "Year",
        "Free_cash_flow",
        "Discount_factor",
        "Discounted_FCF",
        "Cumulative_rNPV",
        "Probability_of_success",
        "Risk_adjusted_value",
        "Enterprise_value",
        "Equity_value_per_share",
    ],
    "Scenarios_Sensitivity": [
        "Scenario",
        "Variable",
        "Base_value",
        "Scenario_value",
        "Impact_on_rNPV",
        "Notes",
        "Rank",
        "Direction",
    ],
    "Notes_Log": [
        "Date",
        "Change_summary",
        "Rationale",
        "Author",
    ],
}


def create_template(output_path: Path) -> None:
    """Create and save the rNPV template workbook."""
    workbook = Workbook()
    default_sheet = workbook.active
    workbook.remove(default_sheet)

    for sheet_name, headers in SHEET_HEADERS.items():
        worksheet = workbook.create_sheet(title=sheet_name)
        worksheet.append(headers)

    workbook.save(output_path)
    print(f"Template saved to {output_path}")


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    output_path = script_dir / "madrigal_rnpv_model_template.xlsx"
    create_template(output_path)


if __name__ == "__main__":
    main()
