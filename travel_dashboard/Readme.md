# Travel Data Dashboard – Power BI with UN Maps Visual

This repository contains a Power BI dashboard that visualizes sample travel data using the **UN custom map visualization tool (UN Maps for Power BI)**.

The dashboard integrates financial analysis with interactive geographic route visualization.

![UN Travel Dashboard Preview](travel_dashboard/travel%20data%20dashboard%20example%201.jpg)

---

## 🔍 Project Overview

This project demonstrates how structured travel data can be transformed into an interactive analytical dashboard combining:

- Financial aggregation (trip costs, totals by traveler)
- Temporal filtering (date range slicer)
- Geographic route visualization using the UN Maps custom visual
---

## 🗺 Core Visualization: UN Maps (Custom UN Visual)

Unlike standard Power BI map visuals, this dashboard uses the **UN Maps Power BI custom visual**, 
Note that this visual requires UN authentication.

---

## 🛠 Tools & Technologies

- **Power BI Desktop**
- **UN Maps Power BI custom visual**
- DAX measures for cost aggregation
- Power Query (M) for data preprocessing
- Date slicers and interactive filtering

---

## 🔐 Required Authorization (Important)

The UN Maps visual requires authentication via a UN account.

When opening the dashboard:

1. Click the map visual.
2. Authorize using your UN account.
3. A browser tab will open.
4. The browser page may remain blank — this is normal.
5. Return to Power BI and wait for the map to load.

Once authorized, the map will become active.

---

## 🧭 How to Build Routes in the Map

To visualize travel routes:

1. Click the **menu button** (top-left corner of the map).
2. Open the **Layers** menu.
3. Adjust zoom.
4. Open the **Routes** menu.
5. Enable:
   - "Draw lines between points"
   - Optional: geodesic lines
6. Select styling options.
7. Apply changes.

Routes will render dynamically between origin and destination coordinates.

---

## 🎯 Key Insights Enabled

This dashboard can be used to:

- Identify high-cost travelers
- Detect concentrated travel corridors
- Monitor geographic distribution of travel
- Analyze temporal changes in travel patterns
- Support budget transparency and planning

---

## ⚠ Notes

- The UN Maps visual requires UN authentication.
- The report must be opened in Power BI Desktop.
- The browser window appearing during login may remain blank — this is expected behavior.

---

## ✍️ Author

Ivan Divilkovskiy  
LinkedIn | GitHub  
