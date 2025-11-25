# Valuation notes – Madrigal (MDGL)

## 1. High-level framework
- Model built as single-asset (Rezdiffra) P&L plus corporate cost layer; rNPV discounting through 2040 using 10.5% WACC equivalent.
- Use MAESTRO-NASH as base case plus MAESTRO-NASH Outcomes probability stack (70% base, 20% bull, 10% bear) to risk-adjust commercialization tail.
- Separate US vs Ex-US cash flows to reflect staggered launches and royalty/pass-through assumptions.

## 2. Key revenue drivers
- Epidemiology funnel anchored to `analysis/02_market_sizing_scratchpad.py` assumptions (US MASLD prevalence 25%, F2/F3 share 12%, 15% diagnosed, 65% specialist access).
- Uptake: Base ramps to ~140k US treated patients by FY2032 (~12% of eligible F2/F3), bull pushes to 200k as GLP-1 combos de-risk biopsies; bear caps at 70k due to payer friction.
- Pricing: List ~$47k/yr with blended gross-to-net 28% base (reflecting Medicare mix); bull assumes step-down to 25% once outcomes data hit, bear 35%.

## 3. Margin and cost structure assumptions
- COGS modeled at 8% of net sales currently (API/DP at Lonza/Catalent) trending to 6% with scale.
- SG&A troughing at ~$900M (field force, DTC) then 22% of sales long term; R&D steady ~$350M until outcomes data, tailing to $200M post full approval.
- Implied steady-state EBIT margin ~45% in base scenario, 50% bull, 35% bear.

## 4. Risk treatment and probabilities
- Base scenario PoS 70% through 2030 (reflecting need for MAESTRO-NASH Outcomes success); bull 85% once first interim hits; bear 40% if outcomes slip or GLP-1 supplant demand.
- Additional risk haircut (5–10%) applied to Ex-US launches for regulatory/payer lag.
- Manufacturing scale-up and reimbursement execution tracked via quarterly KPIs; assumption that <5% of covered lives require biopsy by FY2025 maintained.

## 5. Scenario design (bear/base/bull)
- Bear: slower adoption, biopsy requirement persists, GTN 35%, PoS 40%, cap net revenue ~$4B peak, EV ~$4.5B.
- Base: adoption tied to specialist centers + non-invasive eligibility by 2026, GTN 28%, PoS 70%, peak net ~$7B, EV ~$9.5B.
- Bull: positive outcomes early, combination strategies expand TAM, GTN 25%, PoS 85%, peak net ~$10B, EV ~$14B.
- Scenario mix weights set at 20/60/20 (bear/base/bull) pending new catalysts.

## 6. Sensitivity analysis priorities
- Eligible patient pool (diagnosis + specialist access) drives >35% of variance—track FibroScan/ELF adoption and PCP referral funnels.
- Gross-to-net trajectory second-most sensitive (20% of variance); monitor payer updates each quarter.
- Treatment duration per patient (~10% variance): base uses 0.9 treatment-years/patient; outcomes data could extend.
- Price elasticity vs GLP-1 combos: scenario toggles for eventual rebate war in F3; need close watch on Novo/Eli readouts.
