import pandas as pd

# URLs for data
url_missions = 'https://drive.google.com/uc?export=download&id=1SZgPl5hS7UHwdS8DKiUMrsT5GqMmQPCM'
url_countries = 'https://drive.google.com/uc?export=download&id=1RJtogT44ejo8jEv4f3rt-zpAauXUXjjV'
url_casualties = 'https://drive.google.com/uc?export=download&id=10aIygNb5I5LXXCJgEDKZr064keo9QM2K'

# Load data
missions_df = pd.read_excel(url_missions)
countries_df = pd.read_excel(url_countries)
casualties_df = pd.read_csv(url_casualties)


def check_country_names(missions, countries):
    """Check for country name mismatches between missions and reference countries."""
    all_countries = set()
    for entry in missions["countries_of_operation"].dropna():
        all_countries.update([c.strip() for c in entry.split(",")])
    reference_countries = set(countries["NAME"].dropna().unique())

    missing = sorted([c for c in all_countries if c not in reference_countries])
    if missing:
        print("Missing countries:")
        for country in missing:
            print("-", country)
    else:
        print("All country names match.")


def replace_country_names(missions):
    """Replace mismatched country names using a predefined mapping."""
    replacements = {
        "Bosnia and Herzegovina": "Bosnia and Herz.",
        "Central African Republic": "Central African Rep.",
        "Democratic Republic of the Congo": "Dem. Rep. Congo",
        "East Timor": "Timor-Leste",
        "North Macedonia": "Macedonia",
        "South Sudan": "S. Sudan",
        "The Gambia": "Gambia",
        "Western Sahara": "W. Sahara"
    }

    def replace_func(text):
        if pd.isna(text):
            return text
        countries = [c.strip() for c in text.split(",")]
        updated = [replacements.get(c, c) for c in countries]
        return ", ".join(updated)

    missions["countries_of_operation"] = missions["countries_of_operation"].apply(replace_func)
    missions[["mission_acronym", "countries_of_operation"]].to_csv("missions_countries_for_qgis.csv", index=False)
    print("Saved missions_countries_for_qgis.csv")


def create_mission_year_fatalities(missions, casualties):
    """Create a table of fatalities per mission and year, including mission activity status."""
    # Normalize year columns
    missions["end_year"] = missions["end_year"].replace(r"(?i)^ongoing$", "2025", regex=True)
    missions["start_year"] = pd.to_numeric(missions["start_year"], errors="coerce").astype("Int64")
    missions["end_year"] = pd.to_numeric(missions["end_year"], errors="coerce").astype("Int64")

    # Process casualty data
    casualties["year"] = pd.to_datetime(casualties["incident_date"], errors='coerce').dt.year
    fatality_counts = casualties.groupby(["mission_acronym", "year"]).size().reset_index(name="fatalities")

    # Generate yearly mission table
    years = list(range(1947, 2026))
    rows = []

    for _, row in missions.iterrows():
        mission = row["mission_acronym"]
        countries = row["countries_of_operation"]
        start = row["start_year"]
        end = row["end_year"]

        for year in years:
            active = 1 if pd.notna(start) and pd.notna(end) and start <= year <= end else 0
            fatalities = fatality_counts.query("mission_acronym == @mission and year == @year")["fatalities"]
            date = pd.to_datetime(f"{year}-04-12")
            rows.append({
                "date": date,
                "mission_acronym": mission,
                "countries_of_operation": countries,
                "active_operation": active,
                "fatalities": int(fatalities.iloc[0]) if not fatalities.empty else 0
            })

    output_df = pd.DataFrame(rows)
    output_df.to_csv("mission_year_fatalities.csv", index=False)
    print("Saved mission_year_fatalities.csv")


# Execute steps in order
check_country_names(missions_df, countries_df)
replace_country_names(missions_df)
create_mission_year_fatalities(missions_df, casualties_df)
