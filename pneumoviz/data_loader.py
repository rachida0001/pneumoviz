import pandas as pd
import pooch
from dotenv import load_dotenv
import os 


class DataLoader:
    def __init__(self):
        load_dotenv()  # load .env variables

        self.urls = {
            "child_deaths": os.getenv("CHILD_DEATHS_URL"),
            "vaccine_coverage": os.getenv("VACCINE_COVERAGE_URL"),
            "ihme_data": os.getenv("IHME_DATA_RL"),
            "immunization_schedule": os.getenv("IMMUNIZATION_SCHEDULE_URL"),
            "averted_deaths": os.getenv("AVERTED_DEATHS_URL"),
            "careseeking": os.getenv("CARESEEKING_URL"),
            "final_dose_share": os.getenv("FINAL_DOSE_SHARE_URL"),
        }

        
        self.dataframes = {}

    def download_all(self):
        for key, url in self.urls.items():
            path = pooch.retrieve(url=url, known_hash=None)
            self.dataframes[key] = pd.read_csv(path)
        return self.dataframes

# Usage
downloader = DataLoader()
dfs = downloader.download_all()

df_child_deaths = dfs["child_deaths"]
df_vaccine_coverage = dfs["vaccine_coverage"]
df_ihme_data = dfs["ihme_data"]
df_immunization_schedule = dfs["immunization_schedule"]
df_averted_deaths = dfs["averted_deaths"]
df_careseeking = dfs["careseeking"]
df_final_dose_share = dfs["final_dose_share"]