![Project Thumbnail](./images/peacekeeping_missions_compressed.gif)

# UN Peacekeeping Fatalities Visualization

This project visualizes the geography and intensity of UN peacekeeping missions based on registered fatalities.

## 🔍 Project Overview

Using a dataset of all known UN peacekeeper deaths, this project explores where and when missions have occurred and how fatal they have been over time. The data is processed with the help of OpenAI's GPT models and visualized using QGIS as an animated world map.

## 🛠 Tools & Technologies

- **Python** (pandas, requests, OpenAI API)
- **OpenAI GPT-4o** for data extraction and fact-checking
- **QGIS** for geographic visualization and animation
- **Jupyter Notebook** for development and documentation

## 🔧 Setup

This project uses environment variables (OpenAI API key).

To run the notebook:
1. Copy `#.env.example` to `.env`
2. Replace `your-api-key-here` with your actual OpenAI API key

If you'd prefer to use your own key, you can replace it manually in `preprocessing.py` or load it via a `.env` file.

If you don't have your own key, please message me for a demonstration key.

## Data Sources

- UN Peacekeeper Fatality Records (.csv) 
- Wikipedia (for mission locations and timelines, via GPT queries)
- QGIS World Borders shapefile (default)

## Key Steps

1. **Download & preprocess data**: The dataset is downloaded and mission details (start/end years and countries of operation) are extracted with GPT.
2. **Fact-checking**: Each mission's data is verified again using GPT to minimize hallucinations or errors. The resulting dataset is cleaned manually
3. **Data merging**: Mission data is joined with fatality counts by year.
4. **QGIS visualization**: Each mission is represented as a polygon, with annual fatality counts visualized through color-coding.
5. **Temporal animation**: The result is exported as an animated GIF, showing the evolution of missions and fatalities over time.

## 🎞 Final Output

A 40-second GIF illustrates:
- A rise in peacekeeping missions after the Cold War
- A strong concentration of missions in Africa
- Africa also being the region with the highest number of peacekeeper fatalities

## 📎 Files in This Repository

- `UN_peacekeeping_analysis.ipynb`: Full notebook with code, outputs, and analysis.
- `DPPADPOSS-FATALITIES.csv`: Original dataset. 
- `mission_year_fatalities.csv`: Final dataset used for temporal visualization.
- `UN_peacekeeping_missions_fatalities.zip`: Shapefile of UN peacekeeping missions with fatalities.
- `peacekeeping_missions.gif`: Final animation.
- `preprocessing.py`: Python code to be used with the notebook.
- `processing.py`: Python code to be used with the notebook.
- `#env.example`: example env file for OpenAI API key.
- `README.md`: Project overview and documentation.

## ✍️ Author

Ivan Divilkovskiy  
[LinkedIn](https://www.linkedin.com/in/ivandivilkovskiy) | [GitHub](https://github.com/iv-div)
