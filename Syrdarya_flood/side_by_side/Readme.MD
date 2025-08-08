# Mirzaabad Flood Damage Slider Map

This page shows a side-by-side (swipe) comparison of Sentinel-2 satellite imagery for the Mirzaabad district of Uzbekistan.  
It illustrates the **May 2020 flood damage** by comparing imagery from:

- **Left:** May 2019 (pre-flood)  
- **Right:** May 2020 (post-flood)  

## Demo

Open the interactive map here:  
[**View Slider Map**](https://iv-div.github.io/my-jupyter-portfolio/Syrdarya_flood/side_by_side/)

Move the vertical slider to reveal changes between the two dates.

---

## Data Sources

- **Satellite imagery:** [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)  
  - Source: European Space Agency (ESA) via Copernicus Open Access Hub  
  - Bands and visualization prepared in QGIS
- **Geographic bounds:** Mirzaabad district, Uzbekistan  
  - EPSG:32642 (WGS 84 / UTM zone 42N)  

---

## Tools & Libraries Used

- **[Leaflet](https://leafletjs.com/)** — An open-source JavaScript library for interactive maps.  
  - © 2010–2024 Vladimir Agafonkin, [Leaflet contributors](https://github.com/Leaflet/Leaflet/graphs/contributors)  
  - Licensed under the BSD 2-Clause License
- **[Leaflet-Compare](https://github.com/digidem/leaflet-compare)** — A plugin for swipe/compare controls in Leaflet maps.  
  - © 2014–2019 Development Seed, Mapbox, Digidem  
  - Licensed under the ISC License
- **[OpenStreetMap](https://www.openstreetmap.org)** — Base map tiles © OpenStreetMap contributors, licensed under the ODbL.

---

## How It Works

1. The two Sentinel-2 images are prepared as **PNG overlays** in QGIS, cropped to the exact same geographic extent.
2. The images are loaded into **two separate Leaflet panes**.
3. The [Leaflet-Compare](https://github.com/digidem/leaflet-compare) control creates an interactive vertical slider to reveal one image over the other.

---

## License

This project’s code is released under the MIT License.  
Image data remains © ESA / Copernicus and is used here for illustrative purposes under the terms of the Copernicus data policy.
