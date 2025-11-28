import pandas as pd
import pooch
from dotenv import load_dotenv
import os 


load_dotenv() # charger les variables depuis .env

child_deaths_url = os.getenv("child_deaths_url")
vaccine_coverage_url = os.getenv("vaccine_coverage_url")
ihme_data_url = os.getenv("ihme_data_rl")
immunization_schedule_url = os.getenv("immunization_schedule_url")
averted_deaths_url = os.getenv("averted_deaths_url")
careseeking_url = os.getenv("careseeking_url")
final_dose_share_url = os.getenv("final_dose_share_url")


child_deaths_path = pooch.retrieve(url=child_deaths_url, known_hash=None)
vaccine_coverage_path = pooch.retrieve(url=vaccine_coverage_url, known_hash=None)
ihme_data_path = pooch.retrieve(url=ihme_data_url, known_hash=None)
immunization_schedule_path = pooch.retrieve(url=immunization_schedule_url, known_hash=None)
averted_deaths_path = pooch.retrieve(url=averted_deaths_url, known_hash=None)
careseeking_path = pooch.retrieve(url=careseeking_url, known_hash=None)
final_dose_share_path = pooch.retrieve(url=final_dose_share_url, known_hash=None)


df_child_deaths = pd.read_csv(child_deaths_path)
df_vaccine_coverage = pd.read_csv(vaccine_coverage_path)
df_ihme_data = pd.read_csv(ihme_data_path)
df_immunization_schedule = pd.read_csv(immunization_schedule_path)
df_averted_deaths = pd.read_csv(averted_deaths_path)
df_careseeking = pd.read_csv(careseeking_path)
df_final_dose_share = pd.read_csv(final_dose_share_path)