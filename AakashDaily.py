# ─────────────────────────────────────────────────────────────
# Aakash Daily — Executive Product Analytics Cockpit
# Built for Monday Morning Product Review
# ─────────────────────────────────────────────────────────────

import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── PAGE CONFIG ──
st.set_page_config(
    page_title="Aakash Daily | Executive Product Cockpit",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CUSTOM CSS STYLING (MODERN EXECUTIVE THEME) ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Optimized page margins */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 96% !important;
}

/* Executive Hero Banner */
.hero-card {
    background: linear-gradient(135deg, rgba(30, 58, 138, 0.08) 0%, rgba(37, 99, 235, 0.04) 100%);
    border: 1px solid rgba(37, 99, 235, 0.2);
    border-radius: 16px;
    padding: 22px 28px;
    margin-bottom: 24px;
    box-shadow: 0 4px 20px -4px rgba(37, 99, 235, 0.06);
}
.hero-badge {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #2563eb;
    background: rgba(37, 99, 235, 0.12);
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 8px;
}
.hero-title {
    font-size: 2.1rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    line-height: 1.2;
    margin-bottom: 4px;
}
.hero-sub {
    font-size: 0.95rem;
    opacity: 0.85;
    margin-bottom: 14px;
}
.hero-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.hero-chip {
    font-size: 0.8rem;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 8px;
    background: rgba(148, 163, 184, 0.12);
    border: 1px solid rgba(148, 163, 184, 0.25);
}
.hero-chip-live {
    background: rgba(16, 185, 129, 0.12);
    border-color: rgba(16, 185, 129, 0.35);
    color: #059669;
    font-weight: 600;
}

/* KPI Custom Cards */
.kpi-card {
    background: var(--secondary-background-color, #ffffff);
    border: 1px solid rgba(148, 163, 184, 0.22);
    border-radius: 14px;
    padding: 16px 18px;
    transition: all 0.2s ease-in-out;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 145px;
}
.kpi-card:hover {
    transform: translateY(-2px);
    border-color: rgba(37, 99, 235, 0.45);
    box-shadow: 0 8px 24px rgba(37, 99, 235, 0.1);
}
.kpi-tag {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    opacity: 0.75;
    margin-bottom: 4px;
}
.kpi-val {
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    line-height: 1.1;
    margin-bottom: 8px;
}
.kpi-sub {
    font-size: 0.78rem;
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
    margin-bottom: 8px;
}
.kpi-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 0.74rem;
}
.badge-green { background: rgba(16, 185, 129, 0.16); color: #059669; }
.badge-red   { background: rgba(239, 68, 68, 0.16); color: #dc2626; }
.badge-amber { background: rgba(245, 158, 11, 0.16); color: #d97706; }
.badge-blue  { background: rgba(37, 99, 235, 0.16); color: #2563eb; }

.kpi-progress-bg {
    width: 100%;
    height: 5px;
    background: rgba(148, 163, 184, 0.2);
    border-radius: 3px;
    overflow: hidden;
}
.kpi-progress-bar {
    height: 100%;
    border-radius: 3px;
}

/* Section Header */
.section-title {
    font-size: 1.25rem;
    font-weight: 700;
    letter-spacing: -0.3px;
    margin: 20px 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Insight & Action Cards */
.insight-card {
    background: var(--secondary-background-color, #ffffff);
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, 0.2);
    padding: 16px 20px;
    margin-bottom: 14px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.insight-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}
.border-red   { border-left: 4px solid #ef4444 !important; }
.border-amber { border-left: 4px solid #f59e0b !important; }
.border-blue  { border-left: 4px solid #2563eb !important; }

.insight-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    flex-wrap: wrap;
    gap: 6px;
}
.pill {
    font-size: 0.72rem;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 0.5px;
}
.pill-red     { background: rgba(239, 68, 68, 0.14); color: #dc2626; }
.pill-amber   { background: rgba(245, 158, 11, 0.14); color: #d97706; }
.pill-blue    { background: rgba(37, 99, 235, 0.14); color: #2563eb; }
.pill-emerald { background: rgba(16, 185, 129, 0.14); color: #059669; }

.pill-metric {
    font-size: 0.78rem;
    font-weight: 700;
    background: rgba(148, 163, 184, 0.18);
    padding: 2px 8px;
    border-radius: 6px;
}
.insight-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 8px;
    line-height: 1.3;
}
.insight-body {
    font-size: 0.88rem;
    line-height: 1.55;
    opacity: 0.92;
}
.insight-callout {
    display: block;
    margin-top: 8px;
    padding: 8px 12px;
    border-radius: 8px;
    background: rgba(148, 163, 184, 0.1);
    font-size: 0.84rem;
}

.action-card {
    background: var(--secondary-background-color, #ffffff);
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-left: 4px solid #10b981 !important;
    padding: 16px 20px;
    margin-bottom: 14px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.action-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(16, 185, 129, 0.08);
}
.action-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    flex-wrap: wrap;
    gap: 6px;
}
.target-badge {
    font-size: 0.78rem;
    font-weight: 700;
    color: #059669;
    background: rgba(16, 185, 129, 0.15);
    padding: 3px 10px;
    border-radius: 8px;
}
.action-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 8px;
    line-height: 1.3;
}
.action-body {
    font-size: 0.88rem;
    line-height: 1.55;
    opacity: 0.92;
}
.action-body ul {
    margin: 6px 0 10px 18px;
    padding: 0;
}
.expected-impact {
    background: rgba(16, 185, 129, 0.1);
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 0.84rem;
    color: #065f46;
}

/* Sidebar targets styling */
.target-tile {
    background: rgba(148, 163, 184, 0.1);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.83rem;
}
.target-val {
    font-weight: 700;
    color: #2563eb;
}

/* Methodology Cards */
.memo-card {
    background: var(--secondary-background-color, #ffffff);
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 12px;
    padding: 18px 20px;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# ── DATA INGESTION & PIPELINE ──
# Dynamic path resolution: supports Streamlit Cloud, relative repo root, and local fallback
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else "."

def resolve_data_path():
    candidates = [
        ".",                                                       # repo root (Streamlit Cloud default)
        SCRIPT_DIR,                                                # script directory
        os.path.join(SCRIPT_DIR, "data"),                          # data subfolder
        "data",                                                    # relative data subfolder
        r"c:\Users\Dell\Downloads\Aakash_Daily_Assignment_Data (1)" # local fallback
    ]
    for c in candidates:
        if os.path.exists(os.path.join(c, "students.csv")):
            return c
    return "."

DATA = resolve_data_path()

@st.cache_data
def load_data():
    students  = pd.read_csv(os.path.join(DATA, "students.csv"))
    events    = pd.read_csv(os.path.join(DATA, "events.csv"))
    campaigns = pd.read_csv(os.path.join(DATA, "campaigns.csv"))

    # Fix date data types
    events['event_time']     = pd.to_datetime(events['event_time'])
    students['install_date'] = pd.to_datetime(students['install_date'])
    campaigns['date']        = pd.to_datetime(campaigns['date'])

    # Join student metadata onto events without multiplying rows
    meta = students.set_index('student_id')[['install_date', 'stream', 'city_tier', 'source', 'platform', 'class']]
    events = events.join(meta, on='student_id')

    # Derived temporal metrics
    events['days_since_install'] = (events['event_time'].dt.normalize() - events['install_date']).dt.days
    events['hour'] = events['event_time'].dt.hour
    events['week'] = events['event_time'].dt.to_period('W').apply(lambda r: r.start_time)

    return students, events, campaigns

students, events, campaigns = load_data()

# Core constants
LEARNING = ['practice_test_submitted', 'capsule_completed']
TOTAL_INSTALLS = len(students)

# ── SIDEBAR FILTERS ──
with st.sidebar:
    st.markdown("### 🅰️ Aakash Daily Controls")
    st.caption("Slice student cohorts across demographics:")

    sel_tier = st.multiselect(
        "City Tier",
        options=['Tier 1', 'Tier 2', 'Tier 3'],
        default=['Tier 1', 'Tier 2', 'Tier 3']
    )

    sel_stream = st.multiselect(
        "Exam Stream",
        options=['NEET', 'JEE', 'Foundation'],
        default=['NEET', 'JEE', 'Foundation']
    )

    sel_class = st.multiselect(
        "Class",
        options=[9, 10, 11, 12],
        default=[9, 10, 11, 12]
    )

    sel_platform = st.multiselect(
        "Platform",
        options=['Android', 'iOS'],
        default=['Android', 'iOS']
    )

    st.divider()
    st.markdown("#### 🎯 Benchmark Governance (Assumed)")
    
    st.markdown("""
    <div class="target-tile"><span>WALS Target</span><span class="target-val">1,000 / wk</span></div>
    <div class="target-tile"><span>D7 Retention</span><span class="target-val">18.0%</span></div>
    <div class="target-tile"><span>Test Submit Rate</span><span class="target-val">85.0%</span></div>
    <div class="target-tile"><span>Capsule Completion</span><span class="target-val">60.0%</span></div>
    <div class="target-tile"><span>Max Acceptable CPAL</span><span class="target-val">₹1,000</span></div>
    """, unsafe_allow_html=True)
    st.caption("Assumptions calibrated against standard high-stakes test-prep benchmarks in Indian EdTech.")

# ── APPLY FILTERING ──
filtered_students = students[
    students['city_tier'].isin(sel_tier) &
    students['stream'].isin(sel_stream) &
    students['class'].isin(sel_class) &
    students['platform'].isin(sel_platform)
]

filtered_ids = set(filtered_students['student_id'])
filtered_events = events[events['student_id'].isin(filtered_ids)]

# ── KPI CALCULATIONS ──
n_installs = len(filtered_students)

# North Star Metric: WALS
wals_data = (
    filtered_events[filtered_events['event_name'].isin(LEARNING)]
    .groupby('week')['student_id'].nunique()
    .reset_index()
    .rename(columns={'student_id': 'wals'})
    .sort_values('week')
)
current_wals = int(wals_data['wals'].iloc[-1]) if len(wals_data) >= 1 else 0
prev_wals    = int(wals_data['wals'].iloc[-2]) if len(wals_data) >= 2 else current_wals
wals_delta   = round((current_wals - prev_wals) / max(prev_wals, 1) * 100, 1)

# D7 Retention
d7_count = filtered_events[filtered_events['days_since_install'] == 7]['student_id'].nunique()
d7_pct   = round(d7_count / max(n_installs, 1) * 100, 1)

# Practice Test Funnel
created   = filtered_events[filtered_events['event_name'] == 'practice_test_created']['student_id'].nunique()
submitted = filtered_events[filtered_events['event_name'] == 'practice_test_submitted']['student_id'].nunique()
test_rate = round(submitted / max(created, 1) * 100, 1)

# Capsule Completion
cap_start = filtered_events[filtered_events['event_name'] == 'capsule_started']['student_id'].nunique()
cap_done  = filtered_events[filtered_events['event_name'] == 'capsule_completed']['student_id'].nunique()
cap_rate  = round(cap_done / max(cap_start, 1) * 100, 1)

# ── EXECUTIVE HERO HEADER ──
st.markdown(f"""
<div class="hero-card">
    <div class="hero-badge">🎓 AAKASH EDTECH • PRODUCT ANALYTICS BRIEFING</div>
    <div class="hero-title">Aakash Daily <span style="font-weight:400; opacity:0.85;">| Executive Product Cockpit</span></div>
    <div class="hero-sub">Monday Morning Product Review • Engagement, Exam Habituation & Growth Funnel Performance</div>
    <div class="hero-chips">
        <span class="hero-chip">📅 1 Sep – 31 Oct 2026</span>
        <span class="hero-chip">👥 {TOTAL_INSTALLS:,} Enrolled Base</span>
        <span class="hero-chip">⚡ {len(events):,} Total Events</span>
        <span class="hero-chip">🎯 Active Slices: {n_installs:,} Students ({n_installs/TOTAL_INSTALLS*100:.1f}%)</span>
        <span class="hero-chip hero-chip-live">🟢 Pipeline Active</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── 1. EXECUTIVE KPI COCKPIT (CUSTOM DESIGNED TILES) ──
st.markdown('<div class="section-title">📊 Executive KPI Cockpit (2-Minute Scan)</div>', unsafe_allow_html=True)

k1, k2, k3, k4, k5 = st.columns(5)

# Card 1: WALS
wals_prog = min(100.0, max(0.0, (current_wals / 1000.0) * 100.0))
k1.markdown(f"""
<div class="kpi-card">
    <div>
        <div class="kpi-tag">⭐ NORTH STAR METRIC</div>
        <div class="kpi-val">{current_wals:,}</div>
        <div class="kpi-sub">
            <span class="kpi-badge badge-green">{wals_delta:+}% WoW</span>
            <span>Target: 1,000 WALS</span>
        </div>
    </div>
    <div>
        <div class="kpi-progress-bg">
            <div class="kpi-progress-bar" style="width: {wals_prog:.1f}%; background: linear-gradient(90deg, #2563eb, #38bdf8);"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Card 2: Installs
cohort_pct = round(n_installs / TOTAL_INSTALLS * 100, 1)
k2.markdown(f"""
<div class="kpi-card">
    <div>
        <div class="kpi-tag">📥 FILTERED COHORT</div>
        <div class="kpi-val">{n_installs:,}</div>
        <div class="kpi-sub">
            <span class="kpi-badge badge-blue">{cohort_pct}%</span>
            <span>of Total Student Base</span>
        </div>
    </div>
    <div>
        <div class="kpi-progress-bg">
            <div class="kpi-progress-bar" style="width: {cohort_pct}%; background: #3b82f6;"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Card 3: D7 Retention
d7_diff = round(d7_pct - 18.0, 1)
d7_badge = "badge-green" if d7_diff >= 0 else "badge-red"
d7_prog = min(100.0, max(0.0, (d7_pct / 18.0) * 100.0))
k3.markdown(f"""
<div class="kpi-card">
    <div>
        <div class="kpi-tag">📅 D7 RETENTION</div>
        <div class="kpi-val">{d7_pct}%</div>
        <div class="kpi-sub">
            <span class="kpi-badge {d7_badge}">{d7_diff:+}%</span>
            <span>vs Target 18.0%</span>
        </div>
    </div>
    <div>
        <div class="kpi-progress-bg">
            <div class="kpi-progress-bar" style="width: {d7_prog:.1f}%; background: #ef4444;"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Card 4: Test Submit Rate
test_diff = round(test_rate - 85.0, 1)
test_badge = "badge-green" if test_diff >= 0 else "badge-red"
test_prog = min(100.0, max(0.0, (test_rate / 85.0) * 100.0))
k4.markdown(f"""
<div class="kpi-card">
    <div>
        <div class="kpi-tag">📝 TEST SUBMIT RATE</div>
        <div class="kpi-val">{test_rate}%</div>
        <div class="kpi-sub">
            <span class="kpi-badge {test_badge}">{test_diff:+}%</span>
            <span>vs Target 85.0%</span>
        </div>
    </div>
    <div>
        <div class="kpi-progress-bg">
            <div class="kpi-progress-bar" style="width: {test_prog:.1f}%; background: #10b981;"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Card 5: Capsule Completion
cap_diff = round(cap_rate - 60.0, 1)
cap_badge = "badge-green" if cap_diff >= 0 else "badge-red"
cap_prog = min(100.0, max(0.0, (cap_rate / 60.0) * 100.0))
k5.markdown(f"""
<div class="kpi-card">
    <div>
        <div class="kpi-tag">🎯 CAPSULE COMPLETION</div>
        <div class="kpi-val">{cap_rate}%</div>
        <div class="kpi-sub">
            <span class="kpi-badge {cap_badge}">{cap_diff:+}%</span>
            <span>vs Target 60.0%</span>
        </div>
    </div>
    <div>
        <div class="kpi-progress-bg">
            <div class="kpi-progress-bar" style="width: {cap_prog:.1f}%; background: #f59e0b;"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("ℹ️ *Explicit Targets (Assumed): D7 Retention: 18.0% • Practice Test Submission: 85.0% • Capsule Completion: 60.0% • WALS Target: 1,000.*")

# ── 2. WHAT I SEE BOX (EXECUTIVE INTELLIGENCE PANEL) ──
st.markdown('<div class="section-title">🔍 Executive Intelligence: 3 Diagnostic Findings & 2 Prioritized Decisions</div>', unsafe_allow_html=True)

col_find, col_act = st.columns([3, 2])

with col_find:
    st.markdown("""
    <div class="insight-card border-red">
        <div class="insight-header">
            <span class="pill pill-red">🚨 CRITICAL FRICTION POINT</span>
            <span class="pill-metric">34.3% Completion Rate</span>
        </div>
        <div class="insight-title">1. Severe Capsule Abandonment (65.7% Churn)</div>
        <div class="insight-body">
            <strong>2,357</strong> students start a capsule, but only <strong>808</strong> finish. In sharp contrast, <strong>90.9%</strong> of tests created are submitted.<br>
            <span class="insight-callout"><strong>Root Cause:</strong> Practice intent is proven high, but revision capsules are cognitively dense and lack mid-way checkpoints, triggering mid-session abandonment.</span>
        </div>
    </div>

    <div class="insight-card border-amber">
        <div class="insight-header">
            <span class="pill pill-amber">💸 MARKETING INEFFICIENCY</span>
            <span class="pill-metric">₹2,303 Cost / Active Learner</span>
        </div>
        <div class="insight-title">2. WhatsApp Acquisition Quality Deficit</div>
        <div class="insight-body">
            WhatsApp consumes <strong>94.5%</strong> of marketing spend (₹27.3L) to produce 3,013 installs, but only <strong>1,186</strong> ever perform a learning action.<br>
            <span class="insight-callout"><strong>Quality Contrast:</strong> <code>branch_link</code> acquires active learners at <strong>₹466 CPAL</strong>, and <code>website_qr</code> delivers 127 active learners at <strong>₹0 spend</strong>.</span>
        </div>
    </div>

    <div class="insight-card border-blue">
        <div class="insight-header">
            <span class="pill pill-blue">🌙 UNTAPPED HABIT LOOP</span>
            <span class="pill-metric">73% Study at 7–11 PM</span>
        </div>
        <div class="insight-title">3. Predictable Evening Habit Prime-Time</div>
        <div class="insight-body">
            Daily learning activity surges to a sharp <strong>9 PM peak (Hour 22)</strong>. Morning hours remain near zero.<br>
            <span class="insight-callout"><strong>Product Gap:</strong> Currently, zero scheduled product loops (such as live daily timed sprints or streak reminders) capitalize on this student routine.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_act:
    st.markdown("""
    <div class="action-card border-emerald">
        <div class="action-header">
            <span class="pill pill-emerald">⚡ ACTION 1 • PRODUCT UX SPRINT</span>
            <span class="target-badge">🎯 Goal: 34.3% → 60.0%</span>
        </div>
        <div class="action-title">3-Minute Capsule Chunking + Automated WhatsApp Nudge</div>
        <div class="action-body">
            <ul>
                <li><strong>Micro-Chunking:</strong> Chunk revision capsules into 3-minute modules with mandatory 1-question checkpoints.</li>
                <li><strong>Recovery Nudge:</strong> If a student exits mid-way, trigger an automated WhatsApp nudge at 7 PM to resume.</li>
            </ul>
            <div class="expected-impact"><strong>Target Impact:</strong> Unblock mid-session cognitive fatigue and double capsule completion.</div>
        </div>
    </div>

    <div class="action-card border-emerald">
        <div class="action-header">
            <span class="pill pill-emerald">🚀 ACTION 2 • GROWTH & CAPITAL REALLOCATION</span>
            <span class="target-badge">🎯 Goal: D7 18% | CPAL < ₹1,500</span>
        </div>
        <div class="action-title">Launch "8 PM Daily Sprint" & Shift 20% WhatsApp Budget</div>
        <div class="action-body">
            <ul>
                <li><strong>8 PM Evening Sprint:</strong> Launch a 5-question daily challenge every evening at 8 PM for NEET/JEE cohorts.</li>
                <li><strong>Budget Rebalancing:</strong> Reallocate 20% of WhatsApp budget into high-ROI branch and QR acquisition channels.</li>
            </ul>
            <div class="expected-impact"><strong>Target Impact:</strong> Improve D7 Retention from 11.6% → 18.0% and reduce blended CPAL under ₹1,500.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── HELPER: UNIFIED PLOTLY THEME ──
def apply_plotly_theme(fig, height=380):
    fig.update_layout(
        template="plotly_white",
        font=dict(family="Inter, -apple-system, sans-serif", size=12, color="#334155"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=35, b=20),
        height=height,
        hoverlabel=dict(
            bgcolor="#0f172a",
            font_size=12,
            font_color="#ffffff",
            font_family="Inter, sans-serif"
        )
    )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(226, 232, 240, 0.7)",
        zeroline=False,
        tickfont=dict(color="#64748b", size=11)
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(226, 232, 240, 0.7)",
        zeroline=False,
        tickfont=dict(color="#64748b", size=11)
    )
    return fig

# ── 3. DETAILED ANALYTIC TABS ──
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 North Star & Habit Funnel",
    "🔄 Retention & Study Patterns",
    "💰 Campaign Quality & CPAL",
    "⭐ North Star Note & Governance"
])

# ── TAB 1: North Star & Funnel ──
with tab1:
    c_left, c_right = st.columns(2)

    with c_left:
        st.subheader("WALS Weekly Trend (North Star)")
        fig_wals = make_subplots(specs=[[{"secondary_y": True}]])
        
        # WALS Line with smooth spline and area glow
        fig_wals.add_trace(
            go.Scatter(
                x=wals_data['week'], y=wals_data['wals'],
                name='WALS', mode='lines+markers',
                line=dict(color='#2563eb', width=3.5, shape='spline'),
                marker=dict(size=7, color='#2563eb', line=dict(width=2, color='#ffffff')),
                fill='tozeroy',
                fillcolor='rgba(37, 99, 235, 0.08)'
            ),
            secondary_y=False
        )
        
        wals_data['wow'] = wals_data['wals'].pct_change() * 100
        fig_wals.add_trace(
            go.Bar(
                x=wals_data['week'], y=wals_data['wow'],
                name='WoW Growth %', opacity=0.55,
                marker=dict(color='#10b981', line=dict(color='#059669', width=1))
            ),
            secondary_y=True
        )
        
        # Target threshold
        fig_wals.add_hline(
            y=1000, line_dash="dash", line_color="#f59e0b",
            annotation_text="🎯 Target: 1,000 WALS",
            annotation_position="top left",
            annotation_font=dict(color="#b45309", size=11, family="Inter"),
            secondary_y=False
        )
        
        fig_wals.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.03, xanchor="right", x=1),
            hovermode="x unified"
        )
        fig_wals.update_yaxes(title_text="Active Students", secondary_y=False)
        fig_wals.update_yaxes(title_text="WoW Growth %", secondary_y=True, showgrid=False)
        apply_plotly_theme(fig_wals, height=380)
        st.plotly_chart(fig_wals, use_container_width=True)

    with c_right:
        st.subheader("Exam Habit Activation Funnel")
        f_labels = ['1. Installed', '2. Test Created', '3. Test Submitted', '4. Capsule Started', '5. Capsule Completed']
        f_vals = [n_installs, created, submitted, cap_start, cap_done]
        
        fig_funnel = go.Figure(go.Funnel(
            y=f_labels, x=f_vals,
            textinfo="value+percent initial",
            marker=dict(
                color=["#2563eb", "#3b82f6", "#10b981", "#f59e0b", "#ef4444"],
                line=dict(width=1, color="rgba(255, 255, 255, 0.6)")
            ),
            connector=dict(line=dict(color="rgba(148, 163, 184, 0.5)", width=1.5))
        ))
        apply_plotly_theme(fig_funnel, height=380)
        st.plotly_chart(fig_funnel, use_container_width=True)

# ── TAB 2: Retention & Study Patterns ──
with tab2:
    col_ret, col_hours = st.columns(2)

    with col_ret:
        st.subheader("Retention Decay by City Tier (D1, D7, D30)")
        ret_data = []
        for tier in ['Tier 1', 'Tier 2', 'Tier 3']:
            tier_total = len(filtered_students[filtered_students['city_tier'] == tier])
            if tier_total == 0:
                continue
            for day, lbl in [(1, 'D1'), (7, 'D7'), (30, 'D30')]:
                ret_count = filtered_events[
                    (filtered_events['city_tier'] == tier) &
                    (filtered_events['days_since_install'] == day)
                ]['student_id'].nunique()
                ret_data.append({
                    'Tier': tier, 'Day': lbl,
                    'Rate %': round(ret_count / tier_total * 100, 1)
                })
        
        ret_df = pd.DataFrame(ret_data)
        if not ret_df.empty:
            fig_ret = px.bar(
                ret_df, x='Day', y='Rate %', color='Tier',
                barmode='group', text_auto='.1f',
                color_discrete_map={
                    'Tier 1': '#2563eb',
                    'Tier 2': '#0d9488',
                    'Tier 3': '#f59e0b'
                }
            )
            fig_ret.add_hline(
                y=18, line_dash="dash", line_color="#ef4444",
                annotation_text="🎯 D7 Benchmark: 18%",
                annotation_position="top left",
                annotation_font=dict(color="#dc2626", size=11, family="Inter")
            )
            apply_plotly_theme(fig_ret, height=380)
            st.plotly_chart(fig_ret, use_container_width=True)

    with col_hours:
        st.subheader("Peak Study Hours (1 to 24)")
        hourly_df = (
            filtered_events[filtered_events['event_name'].isin(LEARNING)]
            .groupby('hour').size().reset_index(name='learning_actions')
        )
        hourly_df['hour_24'] = hourly_df['hour'] + 1
        
        fig_hours = px.bar(
            hourly_df, x='hour_24', y='learning_actions',
            labels={'hour_24': 'Hour of Day (1–24)', 'learning_actions': 'Learning Actions'},
            color='learning_actions', color_continuous_scale='Purp'
        )
        fig_hours.add_vrect(
            x0=18.5, x1=23.5, fillcolor="#fef3c7", opacity=0.35,
            line_width=1.5, line_color="#f59e0b",
            annotation_text="🌙 Prime Study Window (7–11 PM: 73% Actions)",
            annotation_position="top left",
            annotation_font=dict(color="#b45309", size=11, family="Inter")
        )
        fig_hours.update_coloraxes(showscale=False)
        apply_plotly_theme(fig_hours, height=380)
        st.plotly_chart(fig_hours, use_container_width=True)

# ── TAB 3: Campaign Quality & CPAL ──
with tab3:
    st.subheader("Acquisition Quality: CPI vs CPAL (Cost per Active Learner)")
    
    camp_summary = campaigns.groupby('channel').agg(
        total_spend=('spend_inr', 'sum'),
        total_installs=('installs_attributed', 'sum')
    ).reset_index()
    camp_summary['CPI'] = camp_summary['total_spend'] / camp_summary['total_installs'].clip(lower=1)
    
    active_by_source = (
        filtered_events[filtered_events['event_name'].isin(LEARNING)]
        .groupby('source')['student_id'].nunique()
        .reset_index().rename(columns={'source': 'channel', 'student_id': 'active_learners'})
    )
    camp_summary = camp_summary.merge(active_by_source, on='channel', how='left').fillna({'active_learners': 0})
    camp_summary['CPAL'] = camp_summary['total_spend'] / camp_summary['active_learners'].clip(lower=1)
    
    channel_colors = {
        'whatsapp': '#ef4444',
        'branch_link': '#10b981',
        'website_qr': '#06b6d4',
        'organic': '#6366f1',
        'referral': '#f59e0b'
    }
    
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Standard View: Cost Per Install (CPI)")
        fig_cpi = px.bar(
            camp_summary, x='channel', y='CPI',
            color='channel', text_auto='.0f',
            color_discrete_map=channel_colors
        )
        fig_cpi.update_layout(showlegend=False)
        apply_plotly_theme(fig_cpi, height=350)
        st.plotly_chart(fig_cpi, use_container_width=True)
        
    with col2:
        st.caption("Quality-Adjusted View: Cost Per Active Learner (CPAL)")
        fig_cpal = px.bar(
            camp_summary, x='channel', y='CPAL',
            color='channel', text_auto='.0f',
            color_discrete_map=channel_colors
        )
        fig_cpal.add_hline(
            y=1000, line_dash="dash", line_color="#10b981",
            annotation_text="🎯 Target Ceiling (₹1,000)",
            annotation_position="top right",
            annotation_font=dict(color="#047857", size=11, family="Inter")
        )
        fig_cpal.update_layout(showlegend=False)
        apply_plotly_theme(fig_cpal, height=350)
        st.plotly_chart(fig_cpal, use_container_width=True)
        
    st.markdown("""
    <div style="background: rgba(148, 163, 184, 0.1); border-left: 4px solid #2563eb; border-radius: 8px; padding: 14px 18px; margin-top: 10px;">
        <strong>💡 Strategic Acquisition Takeaway:</strong> WhatsApp drives high raw volume but at an unsustainable <strong>₹2,303 per active learner</strong>. In contrast, <code>branch_link</code> acquires active learners for just <strong>₹466 CPAL</strong>, and <code>website_qr</code> delivers 127 active learners at <strong>₹0 spend</strong>.
    </div>
    """, unsafe_allow_html=True)

# ── TAB 4: North Star Rationale & Methodology ──
with tab4:
    st.subheader("⭐ North Star Metric Rationale & Governance")
    
    st.markdown("""
    <div class="memo-card" style="border-left: 4px solid #2563eb;">
        <h4 style="margin: 0 0 8px 0; color: #2563eb;">Selected North Star: Weekly Active Learning Students (WALS)</h4>
        <p style="margin: 0; line-height: 1.6;">
            <strong>Definition:</strong> Unique students completing at least 1 practice test or learning capsule in a rolling 7-day period.<br>
            <strong>Academic Habituation Rationale:</strong> In high-stakes exam preparation (NEET/JEE/Foundation), intermittent app opens provide zero academic value. WALS ties directly to core exam habituation, curriculum progression, and long-term retention.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### ❌ Evaluated Metrics That Were Deliberately Rejected")
    r1, r2, r3 = st.columns(3)
    
    with r1:
        st.markdown("""
        <div class="memo-card">
            <h5 style="color: #ef4444; margin: 0 0 6px 0;">1. DAU / App Opens</h5>
            <span class="pill pill-red">Superficial Vanity Metric</span>
            <p style="font-size: 0.85rem; line-height: 1.5; margin-top: 8px;">
                25,672 app opens masked only 7,763 learning actions (3.3 opens per learning event). Opening an app does not prepare students for NEET/JEE.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with r2:
        st.markdown("""
        <div class="memo-card">
            <h5 style="color: #ef4444; margin: 0 0 6px 0;">2. Total App Installs</h5>
            <span class="pill pill-red">Acquisition Vanity Metric</span>
            <p style="font-size: 0.85rem; line-height: 1.5; margin-top: 8px;">
                6,112 total installs produced only 954 WALS in Week 9 (15.6% activation). App installs reflect ad spend, not product-market fit.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with r3:
        st.markdown("""
        <div class="memo-card">
            <h5 style="color: #ef4444; margin: 0 0 6px 0;">3. Total Tests Submitted</h5>
            <span class="pill pill-red">Power-User Skew</span>
            <p style="font-size: 0.85rem; line-height: 1.5; margin-top: 8px;">
                Heavily biased by the top 5% power-users taking 15+ tests, obscuring high churn and drop-off across the broader student cohort.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("#### 📋 Stated Business Assumptions & Governance")
    st.markdown("""
    <div class="memo-card">
        <ol style="margin: 0 0 0 18px; line-height: 1.6; font-size: 0.88rem;">
            <li><strong>EdTech Benchmark Calibration:</strong> In the absence of historical internal targets, the D7 retention benchmark was set at <strong>18.0%</strong>, test submission at <strong>85.0%</strong>, and capsule completion at <strong>60.0%</strong>.</li>
            <li><strong>Active Learner Definition:</strong> Defined strictly as any student generating <code>practice_test_submitted</code> or <code>capsule_completed</code> events. Passive <code>video_started</code> and <code>app_open</code> events are excluded.</li>
            <li><strong>Acquisition Attribution:</strong> Campaign spend is attributed to initial installs and subsequent learning events using primary acquisition source tagging.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
