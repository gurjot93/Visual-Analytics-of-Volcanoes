# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 01:47:09 2019

@author: gurjo
"""

import pandas as pd

def convert(datasets):
    for dataset in datasets:
        df_processed=pd.DataFrame()
        results_in_list=[]
        values=[]
        country=[]
        years=[]
        df=pd.read_csv(dataset+".csv")
        for column in df:
            years.append(column)
            results_in_list.append(df[column].values.tolist())
    
        for i in range(0,len(results_in_list[0])):
            country_name=""
            for j in results_in_list:
                if type(j[i]) is str:
                    country_name=j[i]
                else:
                    country.append(country_name)
                    values.append(j[i])
        years.remove('country')
        years=years*len(results_in_list[0])
        df_processed['Country']=country
        df_processed['Year']=years
        df_processed[dataset]=values
        df_processed.to_csv("Processed_"+dataset+".csv", index=False)
    
datasets=["cervical_cancer_number_of_new_female_cases","co2_intensity_of_economic_output_kg_co2_per_2011_ppp_of_gdp","cumulative_co2_emissions_tonnes","earthquake_affected_annual_number","flood_affected_annual_number","food_supply_kilocalories_per_person_and_day","literacy_rate_adult_total_percent_of_people_ages_15_and_above","literacy_rate_youth_total_percent_of_people_ages_15_24","liver_cancer_number_of_new_male_cases","murder_total_deaths","number_of_people_in_poverty","population_growth_annual_percent","rural_poverty_percent_rural_people_below_national_rural","tsunami_affected_annual_number","urban_population_growth_annual_percent","urban_poverty_percent_urban_people_below_national_urban","wood_removal_cubic_meters"]
#datasets=["cervical_cancer_number_of_new_female_cases","co2_intensity_of_economic_output_kg_co2_per_2011_ppp_of_gdp"]
convert(datasets)



df1=pd.read_csv("Processed_cervical_cancer_number_of_new_female_cases.csv")
df2=pd.read_csv("Processed_co2_intensity_of_economic_output_kg_co2_per_2011_ppp_of_gdp.csv")
df3=pd.read_csv("Processed_cumulative_co2_emissions_tonnes.csv")
df4=pd.read_csv("Processed_earthquake_affected_annual_number.csv")
df5=pd.read_csv("Processed_flood_affected_annual_number.csv")
df6=pd.read_csv("Processed_food_supply_kilocalories_per_person_and_day.csv")
df7=pd.read_csv("Processed_literacy_rate_adult_total_percent_of_people_ages_15_and_above.csv")
df8=pd.read_csv("Processed_literacy_rate_youth_total_percent_of_people_ages_15_24.csv")
df9=pd.read_csv("Processed_liver_cancer_number_of_new_male_cases.csv")
df10=pd.read_csv("Processed_murder_total_deaths.csv")
df11=pd.read_csv("Processed_number_of_people_in_poverty.csv")
df12=pd.read_csv("Processed_population_growth_annual_percent.csv")
df13=pd.read_csv("Processed_rural_poverty_percent_rural_people_below_national_rural.csv")
df14=pd.read_csv("Processed_tsunami_affected_annual_number.csv")
df15=pd.read_csv("Processed_urban_population_growth_annual_percent.csv")
df16=pd.read_csv("Processed_urban_poverty_percent_urban_people_below_national_urban.csv")
df17=pd.read_csv("Processed_wood_removal_cubic_meters.csv")
intersected_df1 = pd.merge(df1, df2, how='inner')
intersected_df2 = pd.merge(df3, df9, how='inner')
intersected_df3 = pd.merge(df5, df6, how='inner')
intersected_df4 = pd.merge(df7, df8, how='inner')

intersected_df9 = pd.merge(intersected_df1, intersected_df2, how='inner')
intersected_df10 = pd.merge(intersected_df3, intersected_df4, how='inner')

final = pd.merge(intersected_df9, intersected_df10, how='inner')
final.to_csv("Final_Dataset.csv",index=False)
