import pandas as pd
from dotenv import load_dotenv
import os

class DataProcessor:
    """Class to process datasets loaded into pandas DataFrames.
    
    Methods:
        process_child_deaths(df): Processes the child deaths DataFrame.
        process_vaccine_coverage(df): Processes the vaccine coverage DataFrame.
    """
    
    @staticmethod
    # clean and process data child deaths
    def process_child_deaths(df):
        """Processes the child deaths DataFrame by cleaning and transforming data.
        
        Args:
            df (pd.DataFrame): The raw child deaths DataFrame.
        Returns:
            pd.DataFrame: The processed child deaths DataFrame.
        """
        # drop columns Streptococcus non-pneumonia-non-meningitis deaths (aged under-5) and Streptococcus meningitis deaths (aged under-5)
        df = df.drop(columns=["Streptococcus non-pneumonia-non-meningitis deaths (aged under-5)", "Streptococcus meningitis deaths (aged under-5)"])
        # rename column Streptococcus pneumonia deaths (aged under-5) to Deaths
        df = df.rename(columns={"Streptococcus pneumonia deaths (aged under-5)": "Deaths"})
        # drop wolrd from dataframe
        df = df[df['Entity'] != 'World']
        # map countries to continents
        continent_mapping = {
        # Africa
        'Algeria': 'Africa', 'Angola': 'Africa', 'Benin': 'Africa', 'Botswana': 'Africa',
        'Burkina Faso': 'Africa', 'Burundi': 'Africa', 'Cabo Verde': 'Africa',
        "Cote d'Ivoire": 'Africa', 'Cameroon': 'Africa', 'Central African Republic': 'Africa',
        'Chad': 'Africa', 'Comoros': 'Africa', 'Congo': 'Africa',
        'Democratic Republic of Congo': 'Africa', 'Djibouti': 'Africa',
        'Egypt': 'Africa', 'Equatorial Guinea': 'Africa', 'Eritrea': 'Africa',
        'Eswatini': 'Africa', 'Ethiopia': 'Africa', 'Gabon': 'Africa', 'Gambia': 'Africa',
        'Ghana': 'Africa', 'Guinea': 'Africa', 'Guinea-Bissau': 'Africa',
        'Kenya': 'Africa', 'Lesotho': 'Africa', 'Liberia': 'Africa', 'Libya': 'Africa',
        'Madagascar': 'Africa', 'Malawi': 'Africa', 'Mali': 'Africa', 'Mauritania': 'Africa',
        'Mauritius': 'Africa', 'Morocco': 'Africa', 'Mozambique': 'Africa',
        'Namibia': 'Africa', 'Niger': 'Africa', 'Nigeria': 'Africa',
        'Rwanda': 'Africa', 'Sao Tome and Principe': 'Africa', 'Senegal': 'Africa',
        'Seychelles': 'Africa', 'Sierra Leone': 'Africa', 'Somalia': 'Africa',
        'South Africa': 'Africa', 'South Sudan': 'Africa', 'Sudan': 'Africa',
        'Tanzania': 'Africa', 'Togo': 'Africa', 'Tunisia': 'Africa', 'Uganda': 'Africa',
        'Zambia': 'Africa', 'Zimbabwe': 'Africa',

        # Asia
        'Afghanistan': 'Asia', 'Armenia': 'Asia', 'Azerbaijan': 'Asia', 'Bahrain': 'Asia',
        'Bangladesh': 'Asia', 'Bhutan': 'Asia', 'Brunei': 'Asia', 'Cambodia': 'Asia',
        'China': 'Asia', 'Cyprus': 'Asia', 'East Timor': 'Asia', 'Georgia': 'Asia',
        'India': 'Asia', 'Indonesia': 'Asia', 'Iran': 'Asia', 'Iraq': 'Asia',
        'Israel': 'Asia', 'Japan': 'Asia', 'Jordan': 'Asia', 'Kazakhstan': 'Asia',
        'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia', 'Laos': 'Asia', 'Lebanon': 'Asia',
        'Malaysia': 'Asia', 'Maldives': 'Asia', 'Mongolia': 'Asia', 'Myanmar': 'Asia',
        'Nepal': 'Asia', 'North Korea': 'Asia', 'Oman': 'Asia', 'Pakistan': 'Asia',
        'Philippines': 'Asia', 'Qatar': 'Asia', 'Saudi Arabia': 'Asia', 'Singapore': 'Asia',
        'South Korea': 'Asia', 'Sri Lanka': 'Asia', 'Syria': 'Asia',
        'Tajikistan': 'Asia', 'Thailand': 'Asia', 'Turkey': 'Asia', 'Turkmenistan': 'Asia',
        'United Arab Emirates': 'Asia', 'Uzbekistan': 'Asia', 'Vietnam': 'Asia', 'Yemen': 'Asia',

        # Europe
        'Albania': 'Europe', 'Andorra': 'Europe', 'Austria': 'Europe', 'Belarus': 'Europe',
        'Belgium': 'Europe', 'Bosnia and Herzegovina': 'Europe', 'Bulgaria': 'Europe',
        'Croatia': 'Europe', 'Czechia': 'Europe', 'Denmark': 'Europe', 'Estonia': 'Europe',
        'Finland': 'Europe', 'France': 'Europe', 'Germany': 'Europe', 'Greece': 'Europe',
        'Hungary': 'Europe', 'Iceland': 'Europe', 'Ireland': 'Europe', 'Italy': 'Europe',
        'Latvia': 'Europe', 'Lithuania': 'Europe', 'Luxembourg': 'Europe',
        'Malta': 'Europe', 'Moldova': 'Europe', 'Monaco': 'Europe', 'Montenegro': 'Europe',
        'Netherlands': 'Europe', 'North Macedonia': 'Europe', 'Norway': 'Europe',
        'Poland': 'Europe', 'Portugal': 'Europe', 'Romania': 'Europe', 'Russia': 'Europe',
        'Serbia': 'Europe', 'Slovakia': 'Europe', 'Slovenia': 'Europe', 'Spain': 'Europe',
        'Sweden': 'Europe', 'Switzerland': 'Europe', 'Ukraine': 'Europe',
        'United Kingdom': 'Europe',

        # North America
        'Antigua and Barbuda': 'North America', 'Bahamas': 'North America',
        'Barbados': 'North America', 'Belize': 'North America', 'Canada': 'North America',
        'Costa Rica': 'North America', 'Cuba': 'North America', 'Dominica': 'North America',
        'Dominican Republic': 'North America', 'El Salvador': 'North America',
        'Grenada': 'North America', 'Guatemala': 'North America', 'Haiti': 'North America',
        'Honduras': 'North America', 'Jamaica': 'North America', 'Mexico': 'North America',
        'Nicaragua': 'North America', 'Panama': 'North America', 'Saint Kitts and Nevis': 'North America',
        'Saint Lucia': 'North America', 'Saint Vincent and the Grenadines': 'North America',
        'Trinidad and Tobago': 'North America', 'United States': 'North America',

        # South America
        'Argentina': 'South America', 'Bolivia': 'South America', 'Brazil': 'South America',
        'Chile': 'South America', 'Colombia': 'South America', 'Ecuador': 'South America',
        'Guyana': 'South America', 'Paraguay': 'South America', 'Peru': 'South America',
        'Suriname': 'South America', 'Uruguay': 'South America', 'Venezuela': 'South America',
        # Oceania
        'Australia': 'Oceania', 'Fiji': 'Oceania', 'Kiribati': 'Oceania',
        'Marshall Islands': 'Oceania', 'Micronesia (country)': 'Oceania',
        'Nauru': 'Oceania', 'New Zealand': 'Oceania', 'Palau': 'Oceania',
        'Papua New Guinea': 'Oceania', 'Samoa': 'Oceania', 'Solomon Islands': 'Oceania',
        'Tonga': 'Oceania', 'Tuvalu': 'Oceania', 'Vanuatu': 'Oceania'
        }
        df['Continent'] = df['Entity'].map(continent_mapping)
    
        return df.reset_index(drop=True)
    

    @staticmethod
    # clean and process data vaccine coverage
    def process_vaccine_coverage(df):
        """"
        Processes the vaccine coverage DataFrame by cleaning and transforming data.
        Args:
            
            df (pd.DataFrame): The raw vaccine coverage DataFrame.
        Returns:    
            pd.DataFrame: The processed vaccine coverage DataFrame.
        """
        # rename column Share of one-year-olds who have had the third dose of the pneumococcal conjugate vaccine to Vaccine_Coverage
        df = df.rename(columns={"Share of one-year-olds who have had the third dose of the pneumococcal conjugate vaccine": "Vaccine_Coverage"})
        # drop rows with NaN values in Vaccine_Coverage column
        df = df.dropna(subset=["Vaccine_Coverage"])
        # drop h columns not needed
        df = df.drop(columns=["World regions according to OWID", "Share of one-year-olds who have had three doses of the diphtheria, tetanus and pertussis vaccine"])
        return df
    

if __name__ == "__main__":
    # Example usage
    processor = DataProcessor()
    # Assuming df_child_deaths is already loaded as a pandas DataFrame
    # processed_df = processor.process_child_deaths(df_child_deaths)
    pass