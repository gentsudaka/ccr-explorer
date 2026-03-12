#!/usr/bin/env python3
"""
Phase 2: Add Risk Breakdown, Comparison Tool, and Portfolio Simulator
"""

import json
import os

OUTPUT_DIR = "/tmp/ccr-explorer-update/phase2"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 60)
print("PHASE 2: RISK BREAKDOWN, COMPARISON, PORTFOLIO")
print("=" * 60)

# Load dimension importance
with open('/tmp/ccr-explorer-update/phase2/dimension_importance.json', 'r') as f:
    dim_importance = json.load(f)

# Load dashboard data
with open('/home/gen/.openclaw/workspace/ccr-explorer-phase1/dashboard_data.json', 'r') as f:
    dashboard_data = json.load(f)

print(f"\n✓ Loaded {len(dim_importance)} dimension importance values")
print(f"✓ Loaded {len(dashboard_data['firms'])} companies")

# Create enhanced dashboard data with dimension importance
for firm in dashboard_data['firms']:
    # Add dimension contributions
    contributions = {}
    for dim, importance in dim_importance.items():
        # Find matching dimension in firm data
        for firm_dim, firm_value in firm.items():
            if firm_dim.lower().replace(' ', '_') == dim.lower().replace(' ', '_'):
                contributions[dim] = importance * firm_value
                break
    
    # Store top contributing dimensions
    firm['dimension_contributions'] = dict(sorted(contributions.items(), 
                                                  key=lambda x: x[1], 
                                                  reverse=True)[:10])

# Update metadata
dashboard_data['metadata']['phase'] = "Phase 2 - Risk Breakdown, Comparison, Portfolio"
dashboard_data['metadata']['dimension_importance'] = dim_importance

# Save enhanced dashboard
with open(f'{OUTPUT_DIR}/dashboard_data.json', 'w') as f:
    json.dump(dashboard_data, f, indent=2)

print(f"✓ Saved enhanced dashboard data")

# Create portfolio data
portfolio_data = {
    "strategies": [
        {
            "id": "low_risk",
            "name": "Low Risk Portfolio",
            "description": "Avoid high-risk personality profiles",
            "filters": {
                "max_risk_score": 0.25,
                "min_organizational_justice": 0.3,
                "max_moral_disengagement": 0.3
            }
        },
        {
            "id": "high_growth",
            "name": "High Growth Portfolio", 
            "description": "Companies with innovative, aggressive profiles",
            "filters": {
                "min_innovation": 0.4,
                "min_achievement": 0.4,
                "max_risk_score": 0.5
            }
        },
        {
            "id": "ethical",
            "name": "Ethical Focus Portfolio",
            "description": "Companies with strong ethical leadership",
            "filters": {
                "min_ethical_leadership": 0.4,
                "min_organizational_justice": 0.4,
                "min_empathy": 0.3
            }
        }
    ],
    "backtest_periods": [
        {"name": "1 Year", "quarters": 4},
        {"name": "3 Years", "quarters": 12},
        {"name": "5 Years", "quarters": 20}
    ]
}

with open(f'{OUTPUT_DIR}/portfolio_strategies.json', 'w') as f:
    json.dump(portfolio_data, f, indent=2)

print(f"✓ Saved portfolio strategies")

print("\n" + "=" * 60)
print("PHASE 2 DATA PREPARATION COMPLETE")
print("=" * 60)

print(f"\n📁 Output files in {OUTPUT_DIR}:")
print(f"   • dashboard_data.json (enhanced)")
print(f"   • portfolio_strategies.json")
print(f"   • dimension_importance.json")

print(f"\n🚀 Next: Creating Phase 2 HTML with:")
print(f"   1. Risk Score Breakdown Panel")
print(f"   2. Company Comparison Tool")
print(f"   3. Portfolio Simulator")
