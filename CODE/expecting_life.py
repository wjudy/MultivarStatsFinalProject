# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from statistics import mean


# data = pd.read_csv("Life Expectancy Data.csv")
# cols = data.columns

# """
# Number unique values in each column
# """
# col_unique_counts = {}
# for c in cols:
#     col_unique_counts[c] = len(set(data[c]))
# print(col_unique_counts)



# years = list(set(data['Year']))
# countries = list(set(data['Country']))

# """
# Figure out which data is missing for each year
# """
# missing_per_year = pd.DataFrame(0, index=years, columns = cols)
# for y in years:
#     year_df = data[data['Year'] == y]
#     for c in cols:
#         df = year_df[c]
#         prev_len = df.shape[0]
#         new_len = df[df.notnull()].shape[0]
#         missing_per_year.loc[y,c] = prev_len - new_len
# missing_per_year.to_csv('Missing_Data_Year_v_Col.csv')

# """
# Figure out which data is missing for each country
# """
# missing_per_country = pd.DataFrame(0,index=countries, columns=cols)
# for country in countries:
#     country_df = data[data['Country'] == country]
#     for c in cols:
#         df = country_df[c]
#         prev_len = df.shape[0]
#         new_len = df[df.notnull()].shape[0]
#         missing_per_country.loc[country,c] = prev_len - new_len
# missing_per_country.to_csv("Missing_Data_Country_v_Col.csv")



# pre_removal_len = data.shape[0]
# cleaned_df = pd.DataFrame(data)
# for c in cols:
#     df = cleaned_df[c]
#     cleaned_df = cleaned_df[df.notnull()]

# post_removal_len = cleaned_df.shape[0]
# print(pre_removal_len, post_removal_len)
    
# quit()
# """
# Seperate data into per year
# """
# data_by_year = {}
# avg_lifespans = []
# avg_populations = []
# row_removals = []
# for y in years:
#     new_df = data[data['Year'] == y]
#     data_by_year[y] = new_df
#     # avg_lifespans.append(mean(new_df['Life expectancy ']))
#     # removed_blank_pops = new_df[new_df['Population'].notnull()]
#     # avg_populations.append(mean(removed_blank_pops['Population']))
# count_removed = []
# for y in years:
#     data = data_by_year[y]
#     og_len = data.shape[0]
#     cols = data.columns
#     for c in cols:
#         data = data[pd.notnull(data[c])]
#     count_removed.append(og_len - data.shape[0])


# print(count_removed)
# quit()



# print(avg_populations)
    

# plt.scatter(years, avg_lifespans)
# plt.xlabel('Year')
# plt.ylabel('Life Expectancy')
# plt.title('Global Life Expectancy vs. Year')
# plt.show()

# plt.scatter(years, avg_populations)
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.title('Global Mean population vs. Year')
# plt.show()


# def summarize_findings(df, country):
#     country_df = df[df['Country'] == country]
#     cols = country_df.columns 

import pandas as pd
import seaborn as sns


life_exp = pd.read_csv('Life Expectancy Data.csv')
print(life_exp.shape)
life_exp = life_exp.dropna()
print(life_exp.shape)

sns.histplot(life_exp['Life expectancy '].dropna(), kde=True, color='orange')

quit()
cmap = sns.diverging_palette(500, 10, as_cmap=True)
sns.heatmap(life_exp.corr(), cmap=cmap, center=0, annot=False, square=True);
quit()

fig = px.scatter(to_bubble, x='GDP', y='Life expectancy',
                 size='Population', color='Continent',
                 hover_name='Country', log_x=True, size_max=40)
fig.show()

for continent, ax in zip(set(life_exp['Continent']), axs.flat):
    continents = life_exp[life_exp['Continent'] == continent]
    sns.regplot(x = continents['GDP'],y = continents['Life expectancy'], color = 'red', ax = ax).set_title(continent)
plt.tight_layout()    
plt.show()