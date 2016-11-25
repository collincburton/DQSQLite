import sqlite3
import pandas as pd
import math

conn = sqlite3.connect("factbook.db")
query = "select * from facts where area_land>0"
factbook = pd.read_sql_query(query, conn)

def project_population(df):
    growth_rate = df["population_growth"]/100
    final_population = df["population"]*math.e**(growth_rate * 35)
    #print(df[3])
    #return(final_population)
    return final_population



#factbook["2050_pop"]=factbook.apply(project_population, axis = 0)
#print(factbook.head())
factbook['pop_2050'] = factbook.apply(project_population, axis = 1)
factbook_sorted = factbook.sort("pop_2050", ascending = False)
print(factbook_sorted.head(10))
