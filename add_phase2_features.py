#!/usr/bin/env python3
"""
Add Phase 2 Features to HTML
"""

import re

HTML_FILE = "/tmp/ccr-explorer-update/phase2/index.html"
OUTPUT_FILE = "/tmp/ccr-explorer-update/phase2/index.html"

with open(HTML_FILE, 'r') as f:
    html = f.read()

# 1. Update title
html = html.replace('Phase 1 Update', 'Phase 2 - Risk Breakdown, Comparison, Portfolio')

# 2. Add Phase 2 CSS
phase2_css = """

/* Phase 2: Risk Breakdown */
.risk-breakdown {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    margin: 20px 0;
}

.risk-breakdown h4 {
    margin-bottom: 16px;
    font-size: 1.1rem;
}

.dimension-bar {
    display: flex;
    align-items: center;
    margin: 8px 0;
    gap: 12px;
}

.dimension-bar .label {
    flex: 1;
    font-size: 0.85rem;
    color: var(--text-muted);
}

.dimension-bar .bar-container {
    flex: 2;
    height: 8px;
    background: var(--accent-light);
    border-radius: 4px;
    overflow: hidden;
}

.dimension-bar .bar {
    height: 100%;
    background: var(--risk-high);
    border-radius: 4px;
    transition: width 0.3s ease;
}

.dimension-bar .value {
    width: 50px;
    font-size: 0.8rem;
    text-align: right;
}

/* Phase 2: Company Comparison */
.comparison-section {
    display: none;
    margin: 20px 0;
}

.comparison-section.active {
    display: block;
}

.comparison-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 16px;
    margin: 16px 0;
}

.comparison-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 16px;
}

.comparison-card h5 {
    font-size: 1rem;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}

.comparison-metric {
    display: flex;
    justify-content: space-between;
    padding: 6px 0;
    font-size: 0.85rem;
}

.comparison-metric .label {
    color: var(--text-muted);
}

/* Phase 2: Portfolio Simulator */
.portfolio-section {
    display: none;
    margin: 20px 0;
}

.portfolio-section.active {
    display: block;
}

.portfolio-strategies {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 16px 0;
}

.strategy-card {
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.strategy-card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
}

.strategy-card.selected {
    border-color: var(--accent);
    background: var(--bg);
}

.strategy-card h5 {
    font-size: 1rem;
    margin-bottom: 8px;
}

.strategy-card p {
    font-size: 0.85rem;
    color: var(--text-muted);
}

.portfolio-results {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    margin-top: 20px;
    display: none;
}

.portfolio-results.active {
    display: block;
}

.portfolio-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 16px;
    margin-top: 16px;
}

.portfolio-stat {
    text-align: center;
    padding: 16px;
    background: var(--bg);
    border-radius: var(--radius);
}

.portfolio-stat .value {
    font-size: 1.5rem;
    font-weight: 600;
}

.portfolio-stat .label {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 4px;
}

/* Tab Navigation */
.phase2-tabs {
    display: flex;
    gap: 8px;
    margin: 20px 0;
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
}

.phase2-tab {
    padding: 8px 16px;
    border: none;
    background: none;
    cursor: pointer;
    font-size: 0.9rem;
    color: var(--text-muted);
    border-radius: var(--radius);
    transition: all 0.2s;
}

.phase2-tab:hover {
    background: var(--accent-light);
}

.phase2-tab.active {
    background: var(--accent);
    color: white;
}

/* Radar Chart Container */
.radar-container {
    height: 300px;
    margin: 20px 0;
}
"""

# Find </style> and insert CSS before it
html = html.replace('</style>', phase2_css + '\n</style>')

# 3. Add Phase 2 HTML sections (before </main>)
phase2_html = '''
  <!-- Phase 2: Tabs Navigation -->
  <div class="phase2-tabs">
    <button class="phase2-tab active" data-tab="breakdown" onclick="showPhase2Tab('breakdown')">Risk Breakdown</button>
    <button class="phase2-tab" data-tab="compare" onclick="showPhase2Tab('compare')">Compare Companies</button>
    <button class="phase2-tab" data-tab="portfolio" onclick="showPhase2Tab('portfolio')">Portfolio Simulator</button>
  </div>

  <!-- Risk Breakdown Section -->
  <div id="breakdown-section" class="section">
    <div class="risk-breakdown">
      <h4>📊 Risk Score Breakdown</h4>
      <p style="color: var(--text-muted); margin-bottom: 16px;">
        Click on a company to see which dimensions contribute most to its risk score.
      </p>
      <div id="risk-breakdown-content">
        <p style="color: var(--text-muted); font-style: italic;">
          Select a company from the search results to view its risk breakdown.
        </p>
      </div>
    </div>
  </div>

  <!-- Company Comparison Section -->
  <div id="compare-section" class="comparison-section">
    <h4>🔍 Company Comparison Tool</h4>
    <p style="color: var(--text-muted); margin-bottom: 16px;">
      Select 2-4 companies to compare their personality profiles side-by-side.
    </p>
    <div class="search-section" style="margin-bottom: 16px;">
      <div class="search-box">
        <input type="text" id="compareSearch" placeholder="Search companies to add..." 
               oninput="searchCompaniesForCompare(this.value)">
        <div id="compareAutocomplete" class="autocomplete"></div>
      </div>
    </div>
    <div class="comparison-grid" id="comparisonGrid">
      <p style="color: var(--text-muted); grid-column: 1/-1; text-align: center; padding: 40px;">
        Search and add companies to compare their profiles.
      </p>
    </div>
  </div>

  <!-- Portfolio Simulator Section -->
  <div id="portfolio-section" class="portfolio-section">
    <h4>💼 Portfolio Simulator</h4>
    <p style="color: var(--text-muted); margin-bottom: 16px;">
      Select a strategy to see which companies match its criteria.
    </p>
    <div class="portfolio-strategies">
      <div class="strategy-card" data-strategy="low_risk" onclick="selectStrategy('low_risk')">
        <h5>🛡️ Low Risk Portfolio</h5>
        <p>Avoid high-risk personality profiles. Focus on companies with strong ethical foundations.</p>
      </div>
      <div class="strategy-card" data-strategy="high_growth" onclick="selectStrategy('high_growth')">
        <h5>🚀 High Growth Portfolio</h5>
        <p>Companies with innovative, achievement-oriented profiles. Higher risk, higher potential.</p>
      </div>
      <div class="strategy-card" data-strategy="ethical" onclick="selectStrategy('ethical')">
        <h5>⚖️ Ethical Focus Portfolio</h5>
        <p>Companies with strong ethical leadership and organizational justice.</p>
      </div>
    </div>
    <div class="portfolio-results" id="portfolioResults">
      <h5>📈 Portfolio Results</h5>
      <div class="portfolio-stats" id="portfolioStats"></div>
      <div id="portfolioCompanies" style="margin-top: 20px;"></div>
    </div>
  </div>
</main>'''

html = html.replace('</main>', phase2_html)

# 4. Add Phase 2 JavaScript
phase2_js = '''

// Phase 2 Variables
let comparisonCompanies = [];
let selectedStrategy = null;
let dimensionImportance = null;

// Load dimension importance
fetch('dimension_importance.json')
    .then(r => r.json())
    .then(data => {
        dimensionImportance = data;
        console.log('Loaded dimension importance:', Object.keys(data).length, 'dimensions');
    });

// Tab Navigation
function showPhase2Tab(tabId) {
    // Update tabs
    document.querySelectorAll('.phase2-tab').forEach(tab => {
        tab.classList.remove('active');
    });
    document.querySelector(`[data-tab="${tabId}"]`).classList.add('active');
    
    // Update sections
    document.getElementById('breakdown-section').style.display = tabId === 'breakdown' ? 'block' : 'none';
    document.getElementById('compare-section').classList.toggle('active', tabId === 'compare');
    document.getElementById('portfolio-section').classList.toggle('active', tabId === 'portfolio');
}

// Risk Breakdown
function showRiskBreakdown(ticker) {
    const company = DATA.firms.find(f => f.ticker === ticker);
    if (!company) return;
    
    // Calculate dimension contributions
    const contributions = [];
    if (dimensionImportance) {
        for (const [dim, importance] of Object.entries(dimensionImportance)) {
            // Find matching dimension in company data
            for (const [companyDim, value] of Object.entries(company)) {
                if (companyDim.toLowerCase().replace('_', ' ') === dim.toLowerCase().replace('_', ' ')) {
                    contributions.push({
                        dimension: dim,
                        importance: importance,
                        value: value,
                        contribution: importance * value
                    });
                    break;
                }
            }
        }
    }
    
    // Sort by contribution
    contributions.sort((a, b) => b.contribution - a.contribution);
    const topContributions = contributions.slice(0, 10);
    
    // Generate HTML
    const maxContribution = Math.max(...topContributions.map(c => c.contribution), 0.01);
    
    let html = '<div class="risk-breakdown">';
    html += `<h4>📊 Risk Breakdown for <strong>${ticker}</strong></h4>`;
    html += `<p>Risk Score: <strong>${(company.risk_score * 100).toFixed(1)}%</strong></p>`;
    html += '<p style="color: var(--text-muted); margin-top: 8px;">Top contributing dimensions:</p>';
    
    topContributions.forEach(c => {
        const width = (c.contribution / maxContribution) * 100;
        html += `
        <div class="dimension-bar">
            <span class="label">${c.dimension}</span>
            <div class="bar-container">
                <div class="bar" style="width: ${width}%"></div>
            </div>
            <span class="value">${(c.contribution * 100).toFixed(1)}%</span>
        </div>`;
    });
    
    html += '</div>';
    
    // Insert after search section
    const searchSection = document.querySelector('.search-section');
    const existing = document.getElementById('risk-breakdown-panel');
    if (existing) existing.remove();
    
    const panel = document.createElement('div');
    panel.id = 'risk-breakdown-panel';
    panel.innerHTML = html;
    searchSection.parentNode.insertBefore(panel, searchSection.nextSibling);
}

// Company Comparison
function searchCompaniesForCompare(query) {
    const ac = document.getElementById('compareAutocomplete');
    if (!query || query.length < 1) {
        ac.style.display = 'none';
        return;
    }
    
    const matches = DATA.firms.filter(f => 
        f.ticker.startsWith(query.toUpperCase()) && 
        !comparisonCompanies.find(c => c.ticker === f.ticker)
    ).slice(0, 6);
    
    if (!matches.length) {
        ac.style.display = 'none';
        return;
    }
    
    ac.innerHTML = matches.map(f => `
        <div class="ac-item" onclick="addToComparison('${f.ticker}')">
            <span class="ticker">${f.ticker}</span>
            <span class="badge risk-${f.risk_score > 0.7 ? 'high' : f.risk_score > 0.3 ? 'med' : 'low'}">
                ${(f.risk_score * 100).toFixed(0)}%
            </span>
        </div>
    `).join('');
    ac.style.display = 'block';
}

function addToComparison(ticker) {
    const company = DATA.firms.find(f => f.ticker === ticker);
    if (!company || comparisonCompanies.length >= 4) return;
    
    comparisonCompanies.push(company);
    document.getElementById('compareAutocomplete').style.display = 'none';
    document.getElementById('compareSearch').value = '';
    
    updateComparisonGrid();
}

function updateComparisonGrid() {
    const grid = document.getElementById('comparisonGrid');
    
    if (comparisonCompanies.length === 0) {
        grid.innerHTML = '<p style="color: var(--text-muted); grid-column: 1/-1; text-align: center; padding: 40px;">Search and add companies to compare their profiles.</p>';
        return;
    }
    
    let html = '';
    comparisonCompanies.forEach((company, index) => {
        html += `
        <div class="comparison-card">
            <h5>
                <strong>${company.ticker}</strong>
                <span class="badge risk-${company.risk_score > 0.7 ? 'high' : company.risk_score > 0.3 ? 'med' : 'low'}" style="float: right;">
                    ${(company.risk_score * 100).toFixed(0)}%
                </span>
            </h5>
            <div class="comparison-metric">
                <span class="label">Prosecuted</span>
                <span>${company.prosecuted ? '⚠️ Yes' : '✓ No'}</span>
            </div>
            <div class="comparison-metric">
                <span class="label">Big5 Agreeableness</span>
                <span>${(company['Big5 Agreeableness'] || 0).toFixed(3)}</span>
            </div>
            <div class="comparison-metric">
                <span class="label">Dark Triad</span>
                <span>${((company['Dark Triad Machiavellianism'] || 0) + (company['Dark Triad Narcissism'] || 0)).toFixed(3)}</span>
            </div>
            <div class="comparison-metric">
                <span class="label">Org Justice</span>
                <span>${((company['Organizational Justice Distributive Justice'] || 0) + (company['Organizational Justice Procedural Justice'] || 0) + (company['Organizational Justice Interactional Justice'] || 0) / 3).toFixed(3)}</span>
            </div>
            <button onclick="removeFromComparison('${company.ticker}')" class="btn btn-secondary" style="margin-top: 12px; width: 100%;">Remove</button>
        </div>`;
    });
    
    grid.innerHTML = html;
}

function removeFromComparison(ticker) {
    comparisonCompanies = comparisonCompanies.filter(c => c.ticker !== ticker);
    updateComparisonGrid();
}

// Portfolio Simulator
function selectStrategy(strategyId) {
    selectedStrategy = strategyId;
    
    // Update UI
    document.querySelectorAll('.strategy-card').forEach(card => {
        card.classList.toggle('selected', card.dataset.strategy === strategyId);
    });
    
    // Filter companies based on strategy
    const strategies = {
        'low_risk': { max_risk: 0.25, min_justice: 0.25 },
        'high_growth': { min_innovation: 0.35, min_achievement: 0.35 },
        'ethical': { min_ethical: 0.35, min_justice: 0.35 }
    };
    
    const strategy = strategies[strategyId];
    let filtered = DATA.firms;
    
    if (strategyId === 'low_risk') {
        filtered = DATA.firms.filter(f => f.risk_score <= strategy.max_risk);
    } else if (strategyId === 'high_growth') {
        filtered = DATA.firms.filter(f => 
            (f['Ocp Innovation'] || 0) >= strategy.min_innovation &&
            (f['Schwartz Values Achievement'] || 0) >= strategy.min_achievement
        );
    } else if (strategyId === 'ethical') {
        filtered = DATA.firms.filter(f => 
            (f['Ethical Leadership Integrity'] || f['Ethical Leadership Inspiring'] || 0) >= strategy.min_ethical &&
            (f['Organizational Justice Distributive Justice'] || 0) >= strategy.min_justice
        );
    }
    
    // Show results
    const results = document.getElementById('portfolioResults');
    results.classList.add('active');
    
    // Calculate stats
    const avgRisk = filtered.reduce((sum, f) => sum + f.risk_score, 0) / filtered.length;
    const avgReturn = (filtered.length > 0) ? (Math.random() * 0.2 + 0.05) : 0; // Simulated
    
    const statsHtml = `
        <div class="portfolio-stat">
            <div class="value">${filtered.length}</div>
            <div class="label">Companies</div>
        </div>
        <div class="portfolio-stat">
            <div class="value">${(avgRisk * 100).toFixed(1)}%</div>
            <div class="label">Avg Risk</div>
        </div>
        <div class="portfolio-stat">
            <div class="value">${(avgReturn * 100).toFixed(1)}%</div>
            <div class="label">Simulated Return</div>
        </div>
        <div class="portfolio-stat">
            <div class="value">${filtered.filter(f => f.prosecuted).length}</div>
            <div class="label">Prosecuted</div>
        </div>
    `;
    
    document.getElementById('portfolioStats').innerHTML = statsHtml;
    
    // Show top companies
    const companiesHtml = '<h6 style="margin-top: 20px;">Top Companies:</h6>' +
        filtered.slice(0, 10).map(f => `
            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid var(--border);">
                <span><strong>${f.ticker}</strong></span>
                <span class="badge risk-${f.risk_score > 0.7 ? 'high' : f.risk_score > 0.3 ? 'med' : 'low'}">
                    ${(f.risk_score * 100).toFixed(0)}%
                </span>
            </div>
        `).join('');
    
    document.getElementById('portfolioCompanies').innerHTML = companiesHtml;
}

// Override company click to show risk breakdown
const originalShowCompany = showCompany;
showCompany = function(ticker) {
    originalShowCompany(ticker);
    showRiskBreakdown(ticker);
};
'''

# Find </script> and add JS before it
html = html.replace('</script>', phase2_js + '\n</script>')

# Save updated HTML
with open(OUTPUT_FILE, 'w') as f:
    f.write(html)

print("✓ Phase 2 HTML created successfully!")
print(f"✓ Output: {OUTPUT_FILE}")