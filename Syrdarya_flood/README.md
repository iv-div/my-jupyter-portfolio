# Syrdarya Flood – Dam Collapse Impact Analysis

## 🔍 Project Overview  
This project analyzes the geographic extent and land-use impact of the **May 2020 Sardoba reservoir dam collapse** in Uzbekistan, which released approximately 500 million m³ of water. The resulting flood affected the Syrdarya River basin in Uzbekistan and Kazakhstan, causing fatalities, mass displacement, and significant agricultural losses.  

Using **satellite imagery, GIS processing, and statistical analysis**, this project quantifies flooded areas, assesses damage by land type, and highlights spatial patterns of impact.  

The analysis combines **Google Earth Engine (GEE)** for remote sensing, **QGIS** for spatial processing and visualization, and **Python** for data analysis and plotting.

![Mirzaabad flooding](/images/Mirzaabad_flood.gif)

*Flood in Mirzaabad District. Satellite image Sentinel2:*
[Side-by-side slider](https://iv-div.github.io/my-jupyter-portfolio/Syrdarya_flood/side_by_side/)


---

## 🛠 Tools & Technologies  
- **Python**: `pandas`, `matplotlib`, `numpy` – data processing & visualization  
- **Google Earth Engine (GEE)** – satellite image retrieval and preprocessing  
- **QGIS** – GIS analysis, land cover classification, shapefile processing, and map creation  
- **Jupyter Notebook** – interactive development and documentation  
- **Leaflet** ([leafletjs.com](https://leafletjs.com/)) – web-based map display for slider visualization  
- **Slider.js** – image comparison functionality, integrated into Leaflet Slider functionality powered by [Leaflet-Compare by phloose](https://github.com/phloose/leaflet-compare), based on Leaflet.SideBySide by Digital Democracy.

---

## 📊 Data Sources & Credits  

### Satellite Imagery  
- **Landsat 7 & Landsat 8** – U.S. Geological Survey (USGS) / NASA via Google Earth Engine  
- **Sentinel-2** – European Space Agency (ESA) via Google Earth Engine  

### Land Cover Data  
- **Copernicus Global Land Service – 2019 Land Cover Map** (European Space Agency / European Commission)  

### Water Coverage  
Global Surface Water dataset: [https://global-surface-water.appspot.com/](https://global-surface-water.appspot.com/)  
Pekel, J.-F., Cottam, A., Gorelick, N., & Belward, A. S. (2016). *High-resolution mapping of global surface water and its long-term changes.* Nature, 540, 418–422. [doi:10.1038/nature20584](https://doi.org/10.1038/nature20584)


### Administrative Boundaries  
- **Kazakhstan**: UNHCR from OpenStreetMap; Contributor: OCHA Field Information Services Section (FISS)  
- **Uzbekistan**: OCHA ROCCA, OpenStreetMap, Wambacher; Contributor: geoBoundaries  

### Background Maps  
- **OpenStreetMap** ([openstreetmap.org](https://www.openstreetmap.org/))  

---


## 📂 Repository Structure  
- **`Syrdarya_flood.ipynb`** – main analysis notebook  
- **`landsat_limitations.ipynb`** – auxiliary notebook on temporal coverage limitations  
- **`/images/`** – supporting maps, charts, and GIFs  
- **`/side_by_side/`** – Leaflet Side-by-Side plugin setup for imagery comparison  
- **`/data sources/`** – tabular and GIS datasets used in analysis  
  - **damage_by_landcover.csv** – flooded area by land cover type  
  - **flooded_area.csv** – aggregated flooded area statistics  
  - **land_use_stat.csv** – land use distribution statistics  
  - **SirdaryoADM1_Landsat_May2020_valid_coverage.csv** – satellite coverage per administrative unit  
  - **`/GIS sources/`** – shapefiles, rasters, and QGIS project  
    - `Sirdarya_AOI_shapefile.zip` – Area of Interest boundary  
    - `Syrdarya_with_attributes_shapefile.zip` – AOI with attributes  
    - `syrdarya_landcover_2019_30m.tiff` – Copernicus land cover raster  
    - `syrdarya_damage_2020.tiff` – flood extent raster (2020)  
    - `syrdarya_lasting_damage_2021.tiff` – flood extent raster (2021)  
    - `Syrdarya_flood.qgz` – QGIS project file  

---

## 📋 Key Steps  
1. **Data Acquisition**  
   - Download May 2020 and reference-year water coverage dataset (Global Surface Water) via **Google Earth Engine**  
   - Download Copernicus 2019 land cover data  
   - Prepare administrative boundaries  

2. **Preprocessing**  
   - Clip datasets to Syrdarya Region (Uzbekistan) & Turkistan Region (Kazakhstan)  

3. **Data Exploration**  
   - Count the areas of cropland, grassland, shrubland, and other land use classes
   - Identify the area of flooded zones by region and district

4. **Flooded Zone Analysis**  
   - Aggregate flooded area by land type

5. **Visualization**  
   - Produce static maps in QGIS  
   - Create animated GIF showing satellite coverage  
   - Implement **Leaflet Side-by-Side slider** for interactive before/after image comparison  


![Districts by flooding area](/images/AOI_flooded_area.png)
*Districts by flooding area*

---

## 🎞 Final Outputs  
- **Main Notebook**: `Syrdarya_flood.ipynb` – complete analysis with results and commentary  
- **Auxiliary Notebook**: `landsat_limitations.ipynb` – coverage analysis  
- **Static Maps & Charts**: `/images`  
- **Animated GIFs**: temporal satellite coverage   
- **Interactive Slider**: `/side_by_side` for web-based before/after comparisons  

---

## 📌 Key Findings  
- **Limited temporal coverage** of Landsat imagery means short-lived floods may be underrepresented  
- **Most affected districts**: Mirzaabad, Sirdarya, Akaltin (Uzbekistan) and Sozak, Shardara, Maktaaral (Kazakhstan)  
- **Land type impact**:  
  - Uzbekistan – flood damage equally affected cropland and grassland  
  - Kazakhstan – cropland damage proportionally lower, matching regional land use patterns  

![Flood damage by land use](/images/damage_by_landuse.png)
*Flood damage by land use and districts*

---

✍ **Author**  
Ivan Divilkovskiy  
[LinkedIn](https://www.linkedin.com/in/ivandivilkovskiy) | [GitHub](https://github.com/iv-div)  

