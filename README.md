# 🎓 Aakash Daily — Executive Product Analytics Cockpit

An executive-level product analytics and decision cockpit built for **Aakash Daily**'s Monday Morning Executive Review. The dashboard monitors student engagement, exam habituation, curriculum progression, and marketing channel ROI across 6,112 enrolled students and 54,719 event touchpoints (1 September – 31 October 2026).

---



## 🚀 Key Executive Findings & Prioritized Actions

| # | Diagnostic Finding | Metric Reality | Root Cause / Analysis | Prioritized Action |
|---|-------------------|----------------|-----------------------|--------------------|
| 1 | **Severe Capsule Churn** | **34.3%** completion vs **60.0%** target | High initial intent (2,357 started) drops to 808 completed due to dense revision capsules without mid-way checkpoints. | **Action 1:** Break into 3-min micro-modules with 1-question checkpoints + 7 PM automated WhatsApp recovery nudge. |
| 2 | **WhatsApp ROI Inefficiency** | **₹2,303** CPAL vs **₹466** (Branch) & **₹0** (QR) | Consumes 94.5% of marketing spend (₹27.3L) to yield 3,013 installs, but only 1,186 ever perform a learning action. | **Action 2:** Reallocate 20% WhatsApp budget into high-converting branch and QR acquisition channels. |
| 3 | **Evening Prime-Time Habit** | **73%** of study between **7–11 PM** | Peak learning occurs at 9 PM (Hour 22). Zero scheduled product loops capitalize on this study window. | **Action 2:** Launch live "8 PM Daily Sprint" 5-question challenge for NEET/JEE cohorts. |

---

## 📊 North Star Metric: Weekly Active Learning Students (WALS)

- **Definition:** Unique students completing at least 1 practice test or learning capsule in a rolling 7-day period.
- **Why it matters:** Unlike vanity DAU/app opens (where 3.3 opens occurred per 1 learning action) or gross installs (which reflect ad spend, not engagement), WALS measures genuine academic habituation and test preparation readiness.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.10+
- **Frontend / Framework:** Streamlit
- **Data Ingestion & Processing:** Pandas, NumPy
- **Interactive Visualizations:** Plotly Express, Plotly Graph Objects

---

## 💻 Local Quickstart

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jigyasa0712/aakash-daily-dashboard.git
   cd aakash-daily-dashboard
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the dashboard:**
   ```bash
   streamlit run AakashDaily.py
   ```

---

## 📂 Repository File Structure

```
├── AakashDaily.py          # Main Streamlit analytics application
├── app.py                  # Entrypoint wrapper for Streamlit Cloud
├── requirements.txt        # Python dependency manifest
├── students.csv            # Student cohort demographic metadata
├── events.csv              # Student interaction and learning events
├── campaigns.csv           # Acquisition campaign spend and attribution
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation & executive briefing
```
