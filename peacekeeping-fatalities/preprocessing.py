import pandas as pd
import requests
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Create a function for sending to openai
def send_to_chatgpt(model, text, temperature, max_tokens):
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {openai.api_key}"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": text}],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    response = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)
    response_json = response.json()
    return response_json['choices'][0]['message']['content']

# Load CSV
url = f'https://drive.google.com/uc?export=download&id=1YTJ2V4vfMRSBIkoGl17EUlgnDP-9vZMp'
df = pd.read_csv(url)

def get_mission_data(df, send_to_chatgpt):
    unique_missions = df['mission_acronym'].dropna().unique()

    prompt_template_country = (
        "You are given the name of a UN mission, commission, or other form of organisation. You should search this acronym on Wikipedia and return the name or names "
        "of the countries where this mission operated. Return just the name of the country or names "
        "of countries delimited by commas if the mission operated in several countries. \n\nMission name: {}"
    )
    prompt_template_start = (
        "You are given the name of a UN mission, commission, or other form of organisation. Research and return the year "
        "in which this mission started. Return just the year. \n\nMission name: {}"
    )
    prompt_template_end = (
        "You are given the name of a UN mission, commission, or other form of organisation. You should return the year "
        "in which this mission ended. If the mission is ongoing, return the word 'ongoing'. Return just the year or the word 'ongoing'.\n\nMission name: {}"
    )

    results = []

    for mission in unique_missions:
        try:
            prompt_country = prompt_template_country.format(mission)
            country = send_to_chatgpt(model="gpt-4o", text=prompt_country, temperature=0, max_tokens=600).strip()
        except Exception as e:
            country = f"Error: {str(e)}"

        try:
            prompt_start = prompt_template_start.format(mission)
            start_year = send_to_chatgpt(model="gpt-4o", text=prompt_start, temperature=0, max_tokens=40).strip()
        except Exception as e:
            start_year = f"Error: {str(e)}"

        try:
            prompt_end = prompt_template_end.format(mission)
            end_year = send_to_chatgpt(model="gpt-4o", text=prompt_end, temperature=0, max_tokens=40).strip()
        except Exception as e:
            end_year = f"Error: {str(e)}"

        results.append({
            "mission_acronym": mission,
            "countries_of_operation": country,
            "start_year": start_year,
            "end_year": end_year
        })

    return pd.DataFrame(results)

mission_data = get_mission_data(df, send_to_chatgpt)


def check_data_with_chatgpt(row, send_to_chatgpt):
    # Check if any part of the row contains "no data"
    if 'no data' in row.values:
        return "CHECK: missing data"
    
    prompt = (
        f"Please verify the geography and timeline data for the following UN mission:\n"
        f"Mission Acronym: {row['mission_acronym']}\n"
        f"Countries of Operation: {row['countries_of_operation']}\n"
        f"Start Year: {row['start_year']}\n"
        f"End Year: {row['end_year']}\n\n"
        "Is the information correct? If yes, reply with 'OK'. If the countries of operation or start or end year are incorrect, reply with 'CHECK'. "
        "Provide corrections"
    )

    try:
        response = send_to_chatgpt(model="gpt-4o", text=prompt, temperature=0, max_tokens=150).strip()
        # Check if the response contains "OK" or "CHECK" and capture any additional comments
        if "OK" in response:
            return f"OK: {response}"
        else:
            return f"CHECK: {response}"
    except Exception as e:
        return f"Error: {str(e)}"

def add_verification_column(mission_data, send_to_chatgpt):
    # Apply the check to each row and add the verification column
    mission_data['data_check'] = mission_data.apply(check_data_with_chatgpt, axis=1, send_to_chatgpt=send_to_chatgpt)
    return mission_data

# Adding the verification column before exporting to Excel
mission_data = add_verification_column(mission_data, send_to_chatgpt)

# Export the DataFrame to Excel with the new column
mission_data.to_excel("mission_countries_years_with_check.xlsx", index=False)

# Print the updated DataFrame for inspection
print("\n--- Updated Mission Data with Verification Column ---")
print(mission_data)