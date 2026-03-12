#!/usr/bin/env python3
"""
Phase 3: Enhanced Visualizations, Export, and Alerts
"""

import json

HTML_FILE = "/tmp/ccr-explorer-update/phase3/index.html"
OUTPUT_FILE = "/tmp/ccr-explorer-update/phase3/index.html"

with open(HTML_FILE, 'r') as f:
    html = f.read()

# 1. Update title
html = html.replace('Phase 2', 'Phase 3 - Enhanced')

# 2. Add Phase 3 CSS
phase3_css = """

/* Phase 3: Export & Alerts */
.export-section {
    margin: 20px 0;
    padding: 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
}

.export-section h4 {
    margin-bottom: 12px;
}

.export-buttons {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.export-btn {
    padding: 10px 20px;
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 8px;
}

.export-btn:hover {
    opacity: 0.9;
}

.export-btn.secondary {
    background: var(--accent-light);
    color: var(--text);
}

/* Phase 3: Alert System */
.alert-panel {
    display: none;
    position: fixed;
    top: 20px;
    right: 20px;
    width: 350px;
    background: var(--surface);
    border: 1px solid var(--risk-high);
    border-radius: var(--radius);
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    z-index: 1000;
    padding: 20px;
}

.alert-panel.active {
    display: block;
}

.alert-panel h4 {
    color: var(--risk-high);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.alert-item {
    padding: 12px;
    background: #fef2f2;
    border-left: 3px solid var(--risk-high);
    margin: 8px 0;
    border-radius: 4px;
}

.alert-item .ticker {
    font-weight: 600;
}

.alert-item .risk {
    color: var(--risk-high);
    font-size: 0.85rem;
}

.alert-close {
    position: absolute;
    top: 12px;
    right: 12px;
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    color: var(--text-muted);
}

/* Phase 3: Enhanced Charts */
.chart-controls {
    display: flex;
    gap: 12px;
    margin: 16px 0;
    flex-wrap: wrap;
}

.chart-control-group {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.chart-control-group label {
    font-size: 0.8rem;
    color: var(--text-muted);
}

.chart-control-group select {
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--surface);
    font-size: 0.9rem;
}

/* Phase 3: Industry Analysis */
.industry-section {
    margin: 20px 0;
    padding: 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
}

.industry-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
    margin-top: 16px;
}

.industry-card {
    padding: 16px;
    background: var(--bg);
    border-radius: var(--radius);
    text-align: center;
}

.industry-card .name {
    font-weight: 600;
    margin-bottom: 8px;
}

.industry-card .count {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--accent);
}

.industry-card .avg-risk {
    font-size: 0.85rem;
    color: var(--text-muted);
}

/* Phase 3: Timeline View */
.timeline-container {
    margin: 20px 0;
    padding: 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
}

.timeline-item {
    display: flex;
    align-items: flex-start;
    padding: 12px 0;
    border-bottom: 1px solid var(--border);
}

.timeline-item:last-child {
    border-bottom: none;
}

.timeline-date {
    min-width: 80px;
    font-weight: 600;
    color: var(--text-muted);
}

.timeline-content {
    flex: 1;
}

.timeline-ticker {
    font-weight: 600;
}

.timeline-type {
    font-size: 0.85rem;
    color: var(--risk-high);
}

/* Phase 3: Stats Cards */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 16px;
    margin: 20px 0;
}

.stat-card {
    padding: 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    text-align: center;
}

.stat-card .value {
    font-size: 2rem;
    font-weight: 600;
    color: var(--accent);
}

.stat-card .label {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 4px;
}

.stat-card.warning .value {
    color: var(--risk-high);
}
"""

# Find </style> and insert CSS before it
html = html.replace('</style>', phase3_css + '\n</style>')

# 3. Add Phase 3 HTML sections
phase3_html = '''
  <!-- Phase 3: Stats Overview -->
  <div class="stats-grid" id="statsGrid">
    <div class="stat-card">
      <div class="value" id="statTotal">503</div>
      <div class="label">Total Companies</div>
    </div>
    <div class="stat-card warning">
      <div class="value" id="statHighRisk">0</div>
      <div class="label">High Risk (>70%)</div>
    </div>
    <div class="stat-card">
      <div class="value" id="statMediumRisk">0</div>
      <div class="label">Medium Risk (30-70%)</div>
    </div>
    <div class="stat-card">
      <div class="value" id="statLowRisk">0</div>
      <div class="label">Low Risk (<30%)</div>
    </div>
    <div class="stat-card">
      <div class="value" id="statProsecuted">24</div>
      <div class="label">Prosecuted</div>
    </div>
    <div class="stat-card">
      <div class="value" id="statDimensions">57</div>
      <div class="label">Dimensions</div>
    </div>
  </div>

  <!-- Phase 3: Export Section -->
  <div class="export-section">
    <h4>📥 Export Data</h4>
    <div class="export-buttons">
      <button class="export-btn" onclick="exportToCSV()">
        <span>📊</span> Export All Companies (CSV)
      </button>
      <button class="export-btn secondary" onclick="exportHighRisk()">
        <span>⚠️</span> Export High Risk
      </button>
      <button class="export-btn secondary" onclick="exportProsecuted()">
        <span>🔴</span> Export Prosecuted
      </button>
    </div>
  </div>

  <!-- Phase 3: Enhanced Temporal Controls -->
  <div class="chart-controls">
    <div class="chart-control-group">
      <label>Primary Dimension</label>
      <select id="primaryDimension" onchange="updateTemporalChart()">
        <option value="CCR_composite">CCR Composite</option>
        <option value="Big5 Agreeableness">Big5 Agreeableness</option>
        <option value="Big5 Conscientiousness">Big5 Conscientiousness</option>
        <option value="Dark Triad Machiavellianism">Dark Triad Machiavellianism</option>
        <option value="Moral Disengagement Displacement Of Responsibility">Moral Disengagement</option>
        <option value="Organizational Justice Distributive Justice">Org Justice</option>
        <option value="Ethical Leadership Integrity">Ethical Leadership</option>
      </select>
    </div>
    <div class="chart-control-group">
      <label>Comparison Dimension</label>
      <select id="compareDimension" onchange="updateTemporalChart()">
        <option value="">None</option>
        <option value="Big5 Agreeableness">Big5 Agreeableness</option>
        <option value="Big5 Conscientiousness">Big5 Conscientiousness</option>
        <option value="Dark Triad Machiavellianism">Dark Triad Machiavellianism</option>
        <option value="Moral Disengagement Displacement Of Responsibility">Moral Disengagement</option>
      </select>
    </div>
    <div class="chart-control-group">
      <label>Chart Type</label>
      <select id="chartType" onchange="updateTemporalChart()">
        <option value="line">Line</option>
        <option value="bar">Bar</option>
        <option value="radar">Radar</option>
      </select>
    </div>
  </div>

  <!-- Phase 3: Alert Panel -->
  <div class="alert-panel" id="alertPanel">
    <button class="alert-close" onclick="closeAlertPanel()">×</button>
    <h4>⚠️ High Risk Alerts</h4>
    <div id="alertList"></div>
    <button class="btn" style="width: 100%; margin-top: 12px;" onclick="checkAllAlerts()">
      Refresh Alerts
    </button>
  </div>

  <!-- Phase 3: Timeline View -->
  <div class="timeline-container" id="timelineContainer" style="display: none;">
    <h4>📅 Prosecution Timeline</h4>
    <div id="timelineList"></div>
  </div>
</main>'''

html = html.replace('</main>', phase3_html)

# 4. Add Phase 3 JavaScript
phase3_js = '''

// Phase 3: Stats
function updateStats() {
    if (!DATA) return;
    
    const firms = DATA.firms;
    const highRisk = firms.filter(f => f.risk_score > 0.7).length;
    const mediumRisk = firms.filter(f => f.risk_score > 0.3 && f.risk_score <= 0.7).length;
    const lowRisk = firms.filter(f => f.risk_score <= 0.3).length;
    const prosecuted = firms.filter(f => f.prosecuted === 1).length;
    
    document.getElementById('statTotal').textContent = firms.length;
    document.getElementById('statHighRisk').textContent = highRisk;
    document.getElementById('statMediumRisk').textContent = mediumRisk;
    document.getElementById('statLowRisk').textContent = lowRisk;
    document.getElementById('statProsecuted').textContent = prosecuted;
}

// Phase 3: Export Functions
function exportToCSV() {
    if (!DATA) return;
    
    const firms = DATA.firms;
    const headers = Object.keys(firms[0]);
    const csv = [
        headers.join(','),
        ...firms.map(f => headers.map(h => {
            const val = f[h];
            if (typeof val === 'string' && val.includes(',')) {
                return `"${val}"`;
            }
            return val;
        }).join(','))
    ].join('\\n');
    
    downloadFile(csv, 'ccr_explorer_all_companies.csv', 'text/csv');
}

function exportHighRisk() {
    if (!DATA) return;
    
    const firms = DATA.firms.filter(f => f.risk_score > 0.7);
    if (firms.length === 0) {
        alert('No high risk companies found');
        return;
    }
    
    const headers = Object.keys(firms[0]);
    const csv = [
        headers.join(','),
        ...firms.map(f => headers.map(h => f[h]).join(','))
    ].join('\\n');
    
    downloadFile(csv, 'ccr_explorer_high_risk.csv', 'text/csv');
}

function exportProsecuted() {
    if (!DATA) return;
    
    const firms = DATA.firms.filter(f => f.prosecuted === 1);
    if (firms.length === 0) {
        alert('No prosecuted companies found');
        return;
    }
    
    const headers = Object.keys(firms[0]);
    const csv = [
        headers.join(','),
        ...firms.map(f => headers.map(h => f[h]).join(','))
    ].join('\\n');
    
    downloadFile(csv, 'ccr_explorer_prosecuted.csv', 'text/csv');
}

function downloadFile(content, filename, type) {
    const blob = new Blob([content], { type });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Phase 3: Enhanced Temporal Chart
function updateTemporalChart() {
    if (!TEMPORAL_DATA) {
        loadTemporalData().then(() => updateTemporalChart());
        return;
    }
    
    const selectedTicker = document.querySelector('.company-card.active')?.dataset?.ticker;
    if (!selectedTicker) return;
    
    const primaryDim = document.getElementById('primaryDimension').value;
    const compareDim = document.getElementById('compareDimension').value;
    const chartType = document.getElementById('chartType').value;
    
    const companyData = TEMPORAL_DATA.quarterly_data.filter(d => d.ticker === selectedTicker);
    if (companyData.length === 0) return;
    
    companyData.sort((a, b) => {
        if (a.year !== b.year) return a.year - b.year;
        return a.quarter - b.quarter;
    });
    
    const labels = companyData.map(d => `${d.year} Q${d.quarter}`);
    const primaryData = companyData.map(d => d[primaryDim] || 0);
    
    const datasets = [{
        label: primaryDim,
        data: primaryData,
        borderColor: '#2d2d2d',
        backgroundColor: 'rgba(45, 45, 45, 0.1)',
        borderWidth: 2,
        fill: true
    }];
    
    if (compareDim) {
        datasets.push({
            label: compareDim,
            data: companyData.map(d => d[compareDim] || 0),
            borderColor: '#c0392b',
            backgroundColor: 'rgba(192, 57, 43, 0.1)',
            borderWidth: 2,
            fill: true
        });
    }
    
    const ctx = document.getElementById('temporalChart').getContext('2d');
    
    if (temporalChartInstance) {
        temporalChartInstance.destroy();
    }
    
    temporalChartInstance = new Chart(ctx, {
        type: chartType,
        data: { labels, datasets },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: `${selectedTicker} - ${primaryDim}${compareDim ? ' vs ' + compareDim : ''}`
                }
            }
        }
    });
}

// Phase 3: Alert System
let alertCheckInterval = null;

function showAlertPanel() {
    document.getElementById('alertPanel').classList.add('active');
    checkAllAlerts();
    
    // Auto-refresh every 30 seconds
    if (!alertCheckInterval) {
        alertCheckInterval = setInterval(checkAllAlerts, 30000);
    }
}

function closeAlertPanel() {
    document.getElementById('alertPanel').classList.remove('active');
}

function checkAllAlerts() {
    if (!DATA) return;
    
    const highRisk = DATA.firms
        .filter(f => f.risk_score > 0.7)
        .sort((a, b) => b.risk_score - a.risk_score)
        .slice(0, 10);
    
    const alertList = document.getElementById('alertList');
    
    if (highRisk.length === 0) {
        alertList.innerHTML = '<p style="color: var(--text-muted);">No high risk alerts at this time.</p>';
        return;
    }
    
    alertList.innerHTML = highRisk.map(f => `
        <div class="alert-item">
            <div class="ticker">${f.ticker}</div>
            <div class="risk">Risk Score: ${(f.risk_score * 100).toFixed(1)}%</div>
            ${f.prosecuted ? '<div class="timeline-type">⚠️ Previously Prosecuted</div>' : ''}
        </div>
    `).join('');
}

// Initialize Phase 3
document.addEventListener('DOMContentLoaded', function() {
    updateStats();
    
    // Auto-show alerts after 3 seconds
    setTimeout(showAlertPanel, 3000);
});
'''

# Find </script> and add JS before it
html = html.replace('</script>', phase3_js + '\n</script>')

# Save updated HTML
with open(OUTPUT_FILE, 'w') as f:
    f.write(html)

print("✓ Phase 3 HTML created successfully!")
print(f"✓ Output: {OUTPUT_FILE}")