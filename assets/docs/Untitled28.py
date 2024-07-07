#!/usr/bin/env python
# coding: utf-8

# In[1]:


1import pandas as pd
import numpy as np
import os


# In[2]:


#get a list of all files in the directory


# In[3]:


directory = r'C:\Users\mbogu\Downloads\newfolder\nawa_for_you'


# In[4]:


files = [file for file in os.listdir(directory)]


# In[5]:


#create an empty dataframe to store concatenated data


# In[6]:


summer_winter_data = pd.DataFrame()


# In[7]:


#iterate over every file in directory


# In[8]:


for file in files:
    print(file)
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)
    summer_winter_data = pd.concat([summer_winter_data, df])
    summer_winter_data.to_csv("all_months_data.csv", index=False)


# In[9]:


summer_winter_data_copy = summer_winter_data.copy()


# In[10]:


summer_winter_data_copy.shape


# In[11]:


summer_winter_data_copy.info


# In[12]:


summer_winter_data_copy.index


# In[13]:


summer_winter_data_copy.columns


# In[14]:


summer_winter_data_copy.dtypes


# In[15]:


summer_winter_data_copy.duplicated()


# In[16]:


duplicates = summer_winter_data_copy.duplicated()


# In[17]:


summer_winter_data.head()


# # Drop the first column

# In[18]:


summer_winter_data_copy.head()


# In[19]:


summer_winter_data_copy.drop(columns=['Unnamed: 0'], inplace=True)


# In[20]:


summer_winter_data_copy.head()


# # Team

# In[21]:


summer_winter_data_copy['Team'].unique()


# In[22]:


summer_winter_data_copy.drop(columns = ['Team'], inplace = True)


# In[23]:


summer_winter_data_copy.head()


# # Drop the Games column

# In[24]:


summer_winter_data_copy.drop(columns = ['Games'],  inplace = True)


# In[25]:


summer_winter_data_copy.head()


# # Age

# In[26]:


#change the age column from a float to an integer


# In[27]:


#check whether there is any missing value in Age column


# In[28]:


summer_winter_data_copy['Age'].isna().sum()


# In[29]:


find_missing_rows = summer_winter_data_copy[summer_winter_data_copy['Age'].isna()]
print(find_missing_rows)


# In[30]:


find_missing_rows['NOC'].unique()


# In[31]:


countries_with_nan = find_missing_rows['NOC'].unique()


# In[32]:


temp_data = summer_winter_data_copy.copy()


# In[33]:


df = pd.DataFrame(temp_data)

# 

# Filter the DataFrame based on the countries in the array
filtered_df = df[df['NOC'].isin(countries_with_nan)]

# Calculate the mean of the 'Age' column, ignoring NaN values
mean_age = filtered_df['Age'].mean().round(0)

print("Mean age for countries with NaN values:", mean_age)


# In[34]:


summer_winter_data_copy['Age'] = summer_winter_data_copy['Age'].fillna(25.0)


# In[35]:


summer_winter_data_copy['Age'].isna().sum()


# In[44]:


summer_winter_data_copy['Age'] = summer_winter_data_copy['Age'].astype(int)


# In[36]:


summer_winter_data_copy.head()


# # NOC

# In[37]:


summer_winter_data_copy['NOC'].unique()


# In[38]:


pip install pycountry


# In[39]:


import pycountry


# In[40]:


abbreviations_array = summer_winter_data_copy['NOC'].unique()
def lengthen_country_abbreviations(abbreviations):
    lengthened_names = []
    for abbreviation in abbreviations:
        try:
            country = pycountry.countries.lookup(abbreviation)
            if country:
                lengthened_names.append((abbreviation, country.name))
        except LookupError:
            pass  # Handle non-existent abbreviations gracefully
    return lengthened_names  # Add a return statement to return the list of abbreviation-expansion pairs

lengthened_names = lengthen_country_abbreviations(abbreviations_array)

# Example usage
for abbreviation, expanded_name in lengthened_names:
    print(f"{expanded_name}({abbreviation})")


# In[41]:


noc_mapping = {'FIN': 'Finland (FIN)',
               'NOR': 'Norway (NOR)',
               'EGY': 'Egypt(EGY)', 
               'FRA': 'France(FRA)',
               'PAK': 'Pakistan(PAK)',
               'MON': 'Monaco(MON)', 'ESP': 'Spain(ESP)',
'SWE': 'Sweden(SWE)',
               'ROU': 'Romania(ROU)',

       'TUR': 'Türkiye(TUR)',
               'ARG': 'Argentina(ARG)',
'URU': 'Uruguay(URU)', 'GHA': 'Ghana(GHA)',
               'DEN': 'Denmark',
               'HUN': 'Hungary(HUN)', 
               'CAN': 'Canada(CAN)',
               'POL': 'Poland(POL)', 
               'GER': 'Germany(GER)',
               'BRA': 'Brazil(BRA)',
               'USA': 'United States(USA)',
               'CHI': 'Chile(CHI)',
               'IRI': 'Iran(IRI)',
               'AUS': 'Australia(AUS)',
               'ITA': 'Italy(ITA)',
               'CUB': 'Cuba(CUB)',
               'NGR': 'Nigeria(NGR)',
               'AUT': 'Austria(AUT)',
       'NED': 'Netherlands(NED)',
               'SUI': 'Switzerland(SUI)',
               'BAH': 'Bahamas(BAH)',
               'URS': 'Soviet Union(URS)',
               'BEL': 'Belgium(BEL)',
               'GBR': 'United Kingdom(GBR)',
               'MEX': 'Mexico(MEX)',
               'POR': 'Portugal(POR)',
               'VEN': 'Venezuela, Bolivarian Republic of(VEN)',
       'ISR': 'Israel',
               'RSA': 'South africa(RSA)',
               'LUX': 'Luxembourg(LUX)',
               'BUL': 'Bulgaria(BUL)',
               'PUR': 'Puerto Rico(PUR)',
               'SAA': 'Saar(SAA)',
               'IND': 'India(IND)',
               'JPN': 'Japan(JPN)',
               'GRE': 'Greece(GRE)',
       'NZL': 'New Zealand(NZL)',
               'PHI': 'Philippines(PHI)',
               'TCH': 'Czechoslovakia(TCH)',
               'YUG': 'Yugoslavia(YUG)',
               'BER': 'Bermuda(BER)',
               'GUA': 'Guatemala(GUA)',
               'SGP': 'Singapore(SGP)',
               'ISL': 'Iceland(ISL)',
               'AHO': 'Netherland Antilles(AHO)',
       'IRL': 'Ireland(IRL)',
               'VNM': 'Vietnam(VNM)',
               'PAN': 'Panama(PAN)',
               'HKG': 'Hong Kong(HKG)',
               'LIB': 'Lebanon(LIB)',
               'KOR': 'Korea, Republic of(KOR)',
               'SRI': 'Sri Lanka(SRI)',
               'JAM': 'Jamaica(JAM)',
               'LIE': 'Liechtenstein(LIE)',
       'TTO': 'Trinidad and Tobago(TTO)',
               'THA': 'Thailand(THA)',
               'MYA': 'Myanmar(MYA)',
               'GUY': 'Guyana(GUY)',
               'INA': 'Indonesia(INA)',
               'CHN': 'China(CHN)',
               'AFG': 'Afghanistan(AFG)',
               'MAL': 'Malaya(MAL)',
               'KEN': 'Kenya(KEN)',
       'COL': 'Colombia(COL)',
               'ETH': 'Ethiopia(ETH)',
               'PER': 'Peru(PER)',
               'FIJ': 'Fiji(FIJ)',
               'NBO': 'North Borneo(NBO)',
               'TPE': 'Chinese Taipei(TPE)',
               'UGA': 'Uganda(UGA)',
               'CAM': 'Cambodia(CAM)',
               'LBR': 'Liberia(LBR)',
       'UAR': 'United Arab Republic(UAR)',
               'SUD': 'Sudan(SUD)',
               'BEL': 'Belgium(BEL)',
               'IRQ': 'Iraq(IRQ)',
               'MAR': 'Morocco(MAR)',
               'TUN': 'Tunisia(TUN)',
               'RHO': 'Rhodesia(RHO)',
               'WIF': 'West Indies Federation(WIF)',
               'MLT': 'Malta(MLT)',
               'SMR': 'San Marino(SMR)',
       'ZIM': 'Zimbabwe(ZIM)',
               'HAI': 'Haiti(HAI)',
               'TAN': 'Tanzania(TAN)',
               'CIV': 'Côte Ivoire(CIV)',
               'MAS': 'Malaysia(MAS)',
               'ZAM': 'Zambia(ZAM)',
               'MGL': 'Mongolia(MGL)',
               'CRC': 'Costa Rica(CRC)',
               'MLI': 'Mali(MLI)',
       'NIG': 'Niger(NIG)',
       'SEN': 'Senegal(SEN)',
       'CGO': 'Republic of the Congo(CGO)',
       'NEP': 'Nepal(NEP)',
       'CHA': 'Chad(CHA)',
       'BOL': 'Bolivia, Plurinational State of(BOL)',
       'ALG': 'Algeria(ALG)',
       'CMR': 'Cameroon(CMR)',
       'MAD': 'Madagascar(MAD)',
       'DOM': 'Dominican Republic(DOM)',
       'ESA': 'El Savador(ESA)',
       'FRG': 'West Germany(FRG)',
       'GDR': 'East Germany(GDR)',
       'ECU': 'Ecuador(ECU)',
       'BIZ': 'Belize(BIZ)',
       'NCA': 'Nicaragua(NCA)',
       'SYR': 'Syrian Arab Republic(SYR)',
       'GUI': 'Guinea(GUI)',
       'HON': 'Honduras(HON)',
       'COD': 'Congo, The Democratic Republic of the(COD)',
       'ISV': 'Virgin Islands(ISV)',
       'BAR': 'Barbados(BAR)',
       'SLE': 'Sierra Leone(SLE)',
       'PAR': 'Paraguay(PAR)',
       'KUW': 'Kuwait(KUW)',
       'LBA': 'Libya(LBA)',
       'CAF': 'Central African Republic(CAF)',
       'SUR': 'Suriname(SUR)',
       'SOM': 'Somalia(SOM)',
       'TOG': 'Togo(TOG)',
       'BEN': 'Benin(BEN)',
       'KSA': 'Saudi Arabia(KSA)',
       'BUR': 'BUrkina Faso(BUR)',
       'MAW': 'Malawi(MAW)',
       'PRK': 'Korea, Democratic Peoples Republic of(PRK)',
       'ALB': 'Albania(ALB)',
       'SWZ': 'Eswatini(SWZ)',
       'GAB': 'Gabon(GAB)',
       'LES': 'Lesotho(LES)',
       'ANT': 'Antigua and Barbuda(ANT)',
       'PNG': 'Papua New Guinea(PNG)',
       'AND': 'Andorra(AND)',
       'CAY': 'Caymand Islands(CAY)',
       'SEY': 'Seychelles(SEY)',
       'MOZ': 'Mozambique(MOZ)',
       'CYP': 'Cyprus(CYP)',
       'LAO': 'Lao Peoples Democratic Republic(LAO)',
       'ANG': 'Angola(ANG)',
       'BOT': 'Botswana(BOT)',
       'VIE': 'Vietnam(VIE)',
       'JOR': 'Jordan(JOR)',
       'BRN': 'Brunei Darussalam(BRN)',
       'UAE': 'United Arab Emirates(UAE)',
       'QAT': 'Qatar(QAT)',
       'OMA': 'Oman(OMA)',
       'YAR': 'North Yemen(YAR)',
       'MRI': 'Mauritius(MRI)', 
       'SOL': 'Solomon Islands(SOL)',
       'SAM': 'Samoa(SAM)',
       'IVB': 'British Virgin Islands(IVB)',
       'GRN': 'Grenada(GRN)',
       'GEQ': 'Equatorial Guinea(GEQ)',
       'RWA': 'Rwanda(RWA)',
       'GAM': 'The Gambia(GAM)',
       'DJI': 'Djibouti(DJI)',
       'BHU': 'Bhutan(BHU)',
       'BAN': 'Bangladesh(BAN)',
       'MTN': 'Mauritania(MTN)',
       'TGA': 'Tonga(TGA)',
       'MDV': 'Maldives(MDV)',
       'VIN': 'Saint Vincent and Grenadines(VIN)',
       'YMD': 'South Yemen(YMD)',
       'GUM': 'Guam(GUM)',
       'VAN': 'Vanuatu(VAN)',
       'ASA': 'American Samoa(ASA)',
       'ARU': 'Aruba(ARU)',
       'COK': 'Cook Islands(COK)',
       'EST': 'Estonia(EST)',
       'EUN': 'Unified Team(EUN)',
       'YEM': 'Yemen(YEM)',
       'CRO': 'Croatia(CRO)',
       'IOA': 'Independent Olympic Athelete(IOA)]',
       'LTU': 'Lithuania(LTU)',
       'LAT': 'Latvia(LAT)',
       'SLO': 'Slovenia(SLO)',
       'BIH': 'Bosnia and Herzegovina(BIH)',
       'NAM': 'Namibia(NAM)',
       'COM': 'Comoros(COM)',
       'BRU': 'Brunei(BRU)',
       'AZE': 'Azerbaijan(AZE)',
       'UZB': 'Uzbekistan(UZB)',
       'GEO': 'Georgia(GEO)',
       'PLE': 'Palestine(PLE)',
       'KAZ': 'Kazakhstan(KAZ)',
       'UKR': 'Ukraine(UKR)', 
       'RUS': 'Russian Federation(RUS)', 
       'DMA': 'Dominica(DMA)',
       'BLR': 'Belarus(BLR)',
       'KGZ': 'Kyrgyzstan(KGZ)',
       'MDA': 'Moldova, Republic of(MDA)',
       'GBS': 'Guinea-Buissau(GBS)',
       'CPV': 'Cape Verde(CPV)',
       'TKM': 'Turkmenistan(TKM)',
       'ARM': 'Armenia(ARM)',
       'STP': 'Sao Tome and Principe(STP)',
       'CZE': 'Czechia(CZE)',
       'SVK': 'Slovakia(SVK)',
       'LCA': 'Saint Lucia(LCA)',
       'SKN': 'Saint Kitts and Nevis(SKN)',
       'SCG': 'Serbia and Montenegro(SCG)', 
       'TJK': 'Tajikistan(TJK)',
       'MKD': 'North Macedonia(MKD)',
       'NRU': 'Nauru(NRU)',
       'BDI': 'Burundi(BDI)',
       'PLW': 'Palau(PLW)',
       'ERI': 'Eritrea(ERI)',
       'FSM': 'Micronesia, Federated States of(FSM)',
       'TLS': 'Timor-Leste(TLS)', 
       'KIR': 'Kiribati(KIR)', 
       'SRB': 'Serbia(SRB)',
       'MNE': 'Montenegro(MNE)', 
       'MHL': 'Marshall Islands(MHL)', 
       'TUV': 'Tuvalu(TUV)', 
       'ROT': 'Refugee Olympic Athletes(ROT)',
       'KOS': 'Kosovo(KOS)', 
       'SSD': 'South Sudan(SSD)',
       'ROC': 'Republic of China(ROC)',
       'EOR': 'Refugee Olympic Athletes(ROT)',
       'LBN': 'Lebanon(LBN)'}


# In[42]:


summer_winter_data_copy['NOC'] = summer_winter_data_copy['NOC'].replace(noc_mapping)


# In[76]:


summer_winter_data_copy.rename(columns={'Team Country': 'Team_Country'}, inplace=True)


# In[77]:


summer_winter_data_copy.head()


# # Medal

# In[70]:


summer_winter_data_copy['Medal'].fillna('No Medal', inplace=True)


# In[78]:


summer_winter_data_copy.head()


# In[66]:


summer_winter_data_copy.reset_index(drop=True, inplace=True)
summer_winter_data_copy.index += 1
print(summer_winter_data_copy)


# In[67]:


summer_winter_data_copy.head()


# # City

# In[80]:


summer_winter_data_copy.rename(columns = {'City': 'Host_ City_Country'}, inplace= True)


# In[84]:


summer_winter_data_copy.head(40)


# In[83]:


summer_winter_data_copy['Host_ City_Country'].unique()


# In[88]:


host_city_country_mapping = {'Helsinki': 'Helsinki, Finland', 
                             'Melbourne': 'Melbourne, Australia',
                             'Stockholm': 'Stockholm, Sweden',
                             'Roma': 'Roma, Italy',
                             'Tokyo': 'Tokyo, Japan',
       'Mexico City': 'Mexico City, Mexico',
                             'Munich': 'Munich, Germany',
                             'Montreal': 'Montreal, Canada',
                             'Moskva': 'Moskva, Russia',
                             'Los Angeles': 'Los Angeles, United States of America',
       'Seoul': 'Seoul, South Korea',
                             'Barcelona': 'Barcelona, Spain',
                             'Atlanta': 'Atlanta, United States of America',
                             'Sydney':  'Sydney, Australia',
                             'Athina': 'Athens, Greece',
                             'Beijing': 'Beijing, China',
       'London': 'London, United Kingdom',
                             'Rio de Janeiro': 'Rio de Janeiro, Brazil',
                             'Oslo': 'Oslo, Norway',
                             "Cortina d'Ampezzo":  "Cortina d'Ampezzo, Italy",
       'Squaw Valley': 'Squaw Valley, United States of America',
                             'Innsbruck': 'Innsbruck, Austria',
                             'Grenoble': 'Grenoble, France',
                             'Sapporo': 'Sapporo, Japan',
                             'Lake Placid': 'New York, United States of America',
       'Sarajevo': 'Sarajevo, Bosnia and Herzegovina',
                             'Calgary': 'Calgary, Canada',
                             'Albertville': 'Albertville, France',
                             'Lillehammer': 'Lillehammer, Norway',
                             'Nagano': 'Nagano, Japan',
       'Salt Lake City': 'Utah, United States of America',
                             'Torino': 'Turin, Italy',
                             'Vancouver': 'Vancouver, Canada',
                             'Sochi': 'Sochi, Russia'}


# In[89]:


summer_winter_data_copy['Host_ City_Country'] = summer_winter_data_copy['Host_ City_Country'].replace(host_city_country_mapping)


# In[95]:


summer_winter_data_copy.head()


# In[78]:


summer_winter_data_copy.drop(columns = ['Sex', 'Age'], inplace = True)


# In[150]:


summer_winter_data_copy.head()


# In[81]:





# In[ ]:




