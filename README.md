# olympic_data

```python
1import pandas as pd
import numpy as np
import os
```


```python
#get a list of all files in the directory
```


```python
directory = r'C:\Users\mbogu\Downloads\newfolder\nawa_for_you'
```


```python
files = [file for file in os.listdir(directory)]
```


```python
#create an empty dataframe to store concatenated data
```


```python
summer_winter_data = pd.DataFrame()
```


```python
#iterate over every file in directory
```


```python
for file in files:
    print(file)
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)
    summer_winter_data = pd.concat([summer_winter_data, df])
    summer_winter_data.to_csv("all_months_data.csv", index=False)
```

    Athletes_summer_games.csv
    Athletes_winter_games.csv
    


```python
summer_winter_data_copy = summer_winter_data.copy()
```


```python
summer_winter_data_copy.shape
```




    (239985, 13)




```python
summer_winter_data_copy.info
```




    <bound method DataFrame.info of        Unnamed: 0                            Name Sex   Age     Team  NOC  \
    0              29  Einar Ferdinand "Einari" Aalto   M  26.0  Finland  FIN   
    1              49         Paavo Johannes Aaltonen   M  32.0  Finland  FIN   
    2              50         Paavo Johannes Aaltonen   M  32.0  Finland  FIN   
    3              51         Paavo Johannes Aaltonen   M  32.0  Finland  FIN   
    4              52         Paavo Johannes Aaltonen   M  32.0  Finland  FIN   
    ...           ...                             ...  ..   ...      ...  ...   
    45195      270930          Stepan Olegovich Zuyev   M  25.0   Russia  RUS   
    45196      270966              Kristaps Zvejnieks   M  21.0   Latvia  LAT   
    45197      270967              Kristaps Zvejnieks   M  21.0   Latvia  LAT   
    45198      271112                        Piotr ya   M  27.0   Poland  POL   
    45199      271113                        Piotr ya   M  27.0   Poland  POL   
    
                 Games  Year  Season      City          Sport  \
    0      1952 Summer  1952  Summer  Helsinki       Swimming   
    1      1952 Summer  1952  Summer  Helsinki     Gymnastics   
    2      1952 Summer  1952  Summer  Helsinki     Gymnastics   
    3      1952 Summer  1952  Summer  Helsinki     Gymnastics   
    4      1952 Summer  1952  Summer  Helsinki     Gymnastics   
    ...            ...   ...     ...       ...            ...   
    45195  2014 Winter  2014  Winter     Sochi  Alpine Skiing   
    45196  2014 Winter  2014  Winter     Sochi  Alpine Skiing   
    45197  2014 Winter  2014  Winter     Sochi  Alpine Skiing   
    45198  2014 Winter  2014  Winter     Sochi    Ski Jumping   
    45199  2014 Winter  2014  Winter     Sochi    Ski Jumping   
    
                                              Event   Medal  
    0           Swimming Men's 400 metres Freestyle     NaN  
    1        Gymnastics Men's Individual All-Around     NaN  
    2              Gymnastics Men's Team All-Around  Bronze  
    3               Gymnastics Men's Floor Exercise     NaN  
    4                  Gymnastics Men's Horse Vault     NaN  
    ...                                         ...     ...  
    45195                Alpine Skiing Men's Slalom     NaN  
    45196          Alpine Skiing Men's Giant Slalom     NaN  
    45197                Alpine Skiing Men's Slalom     NaN  
    45198  Ski Jumping Men's Large Hill, Individual     NaN  
    45199        Ski Jumping Men's Large Hill, Team     NaN  
    
    [239985 rows x 13 columns]>




```python
summer_winter_data_copy.index
```




    Index([    0,     1,     2,     3,     4,     5,     6,     7,     8,     9,
           ...
           45190, 45191, 45192, 45193, 45194, 45195, 45196, 45197, 45198, 45199],
          dtype='int64', length=239985)




```python
summer_winter_data_copy.columns
```




    Index(['Unnamed: 0', 'Name', 'Sex', 'Age', 'Team', 'NOC', 'Games', 'Year',
           'Season', 'City', 'Sport', 'Event', 'Medal'],
          dtype='object')




```python
summer_winter_data_copy.dtypes
```




    Unnamed: 0      int64
    Name           object
    Sex            object
    Age           float64
    Team           object
    NOC            object
    Games          object
    Year            int64
    Season         object
    City           object
    Sport          object
    Event          object
    Medal          object
    dtype: object




```python
summer_winter_data_copy.duplicated()
```




    0        False
    1        False
    2        False
    3        False
    4        False
             ...  
    45195    False
    45196    False
    45197    False
    45198    False
    45199    False
    Length: 239985, dtype: bool




```python
duplicates = summer_winter_data_copy.duplicated()
```


```python
summer_winter_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team</th>
      <th>NOC</th>
      <th>Games</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>29</td>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>49</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>3</th>
      <td>51</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# Drop the first column


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team</th>
      <th>NOC</th>
      <th>Games</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>29</td>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>49</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>3</th>
      <td>51</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52</td>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
summer_winter_data_copy.drop(columns=['Unnamed: 0'], inplace=True)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team</th>
      <th>NOC</th>
      <th>Games</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# Team


```python
summer_winter_data_copy['Team'].unique()
```




    array(['Finland', 'Norway', 'Egypt', 'France', 'Pakistan', 'Monaco',
           'Spain', 'Sweden', 'Romania', 'Turkey', 'Argentina', 'Uruguay',
           'Ghana', 'Denmark', 'Hungary', 'Canada', 'Poland', 'Germany',
           'Brazil', 'United States', 'Chile', 'Iran', 'Australia', 'Italy',
           'Cuba', 'Nigeria', 'Austria', 'Netherlands', 'Switzerland',
           'Bahamas', 'Burevestnik', 'Soviet Union', 'Damoiselle', 'Belgium',
           'Great Britain', 'Mexico', 'Tornado', 'Portugal', 'Venezuela',
           'May Be VII', 'Israel', 'South Africa', 'Luxembourg', 'Bulgaria',
           'Puerto Rico', 'Saar', 'India', 'Japan', 'Greece', 'Elisabeth X',
           'New Zealand', 'Philippines', 'Czechoslovakia', 'Mirtala',
           'Hirondelle', 'Yugoslavia', 'Fortuna', 'Bermuda', 'Pan',
           'Guatemala', 'Sabre', 'Primorka', 'Sjhxa', 'Shoveller', 'Snude',
           'Tom Kyle', 'Singapore', 'Iceland', 'Trickson VI', 'Arcturus',
           'Netherlands Antilles', 'Ali-Baba IV', 'Vinha', 'Pampero',
           'Galatea II', 'Lotta IV', 'Ireland', 'Teresita', 'Eissero VI',
           'Complex II', 'Ylliam VIII', 'South Vietnam', 'Panama',
           'Hong Kong', 'Lebanon', 'South Korea', 'Jill', 'Tim-Tam III',
           'Uragan', 'Ciocca', 'Espadarte', 'Kurush IV', 'Virginie',
           'Girl Pat', 'Bu III', 'DeRuyter', 'Unique', 'Thalatta', 'Nirwana',
           'Llanoria', 'Sri Lanka', 'Tu-Fri', 'Encore', 'Jamaica', 'Gem III',
           '30. Februar', 'Paka V', 'Gullvinge', 'Korshun', 'Alcaid', 'Jet',
           'Hornet', 'Liechtenstein', 'Yeoman', 'Skidoo', 'Whirlaway',
           'Lucky Star', 'Escapade', 'Ralia', 'Trinidad and Tobago',
           'Thailand', 'Bem II', 'Myanmar', 'Djinn', 'Guyana', 'Titia',
           'Gustel X', 'Hojwa', 'Comanche', 'Marie-Tim', 'Merope',
           'Indonesia', 'China', 'Afghanistan', 'Druzhba', 'Malaya', 'Tip',
           'Kenya', 'Colombia', 'Bluebottle', 'Ethiopia', 'Peru',
           'Starlight III', 'Faneca', 'Fiji', 'Inca', 'Tichiboo', 'Tilly',
           'North Borneo', 'Chuckles', 'Slaghoken II', 'Nikh', 'Vision',
           'Covunco III', 'Rush IV', 'Buraddoo', 'Gilliatt V', 'Beaver',
           'Romolo', 'Twins VIII', 'Paula', 'Gam II', 'Chinese Taipei',
           'Kingfisher', 'Kon-Tiki', 'Jest', 'Red Dragon', 'Canopus',
           'Viking', 'Naiad', 'Spirit III', 'Uganda', 'Impala', 'Pam',
           'Gem IV', 'Kannibaltje', 'Xantippa', 'Cambodia', 'Rika II',
           'Aretusa', 'Pan II', 'Yeoman V', 'Tomahawk II', 'Liberia',
           'Rush V', 'Kathleen', 'Neptun II', 'Wendehals', 'Gustl XI',
           'Tineke', 'Manana', 'Tulilind', 'Merope III', 'Falcon IV',
           'United Arab Republic', 'Sudan', 'Iraq', 'Morocco', 'Yeoman VII',
           'Tunisia', 'Tajamar', 'Lett', 'Evita VI', 'Bronia', 'Rhodesia',
           'Grifo III', 'Damoiselle IV', 'Ciocca III', 'Dinah V', 'Circus',
           'Aletta', 'Sirene', 'Web II', 'West Indies Federation',
           'Posillipo III', 'Peri', 'Siames-Cat', 'Chok', 'Malta',
           'Calcinhas', 'Chamukina', 'Gabbiano', 'Ali-Baba VI', 'Snowten III',
           'Scram', 'Fantasio III', 'Tango', 'Espuma del Mar', 'Baccara',
           'Aldebaran II', 'Mari', 'San Marino', 'Yangon', 'Venilia',
           'SagaII', 'June Climene', 'Zimbabwe', 'Ballerina IV', 'Calypse II',
           'Galejan', 'Terrible', 'Rififi', 'Partenope', 'Bermudes', 'Meteor',
           'Vesania', 'Frip IV', 'Mad Dog', 'Bermudian', 'Pakaria',
           'Trintel II', 'Bella', 'May-Be 1960', 'Inga-Lill XXXXIII',
           'Nirefs', 'Oleander II', 'Cha-Cha III', 'Gem VII', 'Struten',
           'Skum', 'Mizar', 'Bajazzo', 'Patricia', 'Viktoriya',
           'Three Leaves', 'Pasodoble', 'Shrew II', 'Salamander', 'Daisy',
           'Balaton', 'Minotaur', 'Surprise', 'Boreas', 'Olimpia', 'Macky VI',
           'Tengiri', 'John B', 'Bim', 'Spirit VI', 'Olympion', 'Haiti',
           'Combine', 'Argo II', 'Zefyros', 'Bellatrix IX', 'Twinkle',
           'Persey', 'Pimm', 'Voloira II', 'Falcon VI', 'Astrid III',
           'Nokaut II', "Ma'Lindo", 'Harmony', 'Maid of Lebanon', 'Danaldo',
           'Ardilla', 'Vim III', 'Lasha', 'Hakahana', 'Sjovinge', 'Tanzania',
           "Cote d'Ivoire", 'Clementine V', 'Xolotl', 'Mutafo', 'Yeoman XII',
           'Malaysia', 'Olen', 'GyoshuII', 'Linglom', 'Zambia', 'Mongolia',
           'Costa Rica', 'Firebird II', 'Grifo IV', 'Bingo', 'Monica',
           'Widgeon', 'White Lady', 'Web III', 'Serendipity', 'Nausikaa 4',
           'Ali-Baba IX', 'Pigoule', 'Peri II', 'Pousse-Moi Pas VII', 'Mali',
           'Aldebaran', 'Gem', 'Cambria', 'Oleander XII', 'Phoenix',
           'Umberta V', 'Akatonbo', 'Niger', 'Diablo', 'Acipactli',
           'Aphrodite', 'Senegal', 'Guanahani', 'Congo (Brazzaville)',
           'Proteus II', 'Chaje II', 'Brigantia', 'Miss Denmark 1964',
           'Fram III', 'Miss Nippon V', 'Argeste', 'Tantalus', 'Tlaloc',
           'Alain IV', 'Nepal', 'Roy', 'Andromeda', 'Syndi', 'Vento Sul',
           'Miss Nippon IV', 'Kuling', 'Chad', 'Bolivia', 'MitaII',
           'Barco Deloro', 'Kalayaan', 'Hayama', 'Rush VII', 'Lucky',
           'Subbnboana', 'Algeria', 'State VI', 'Riccar', 'Bellatrix XIII',
           'Glisten', 'Grifone', 'Lady C', 'Cameroon', 'Barrenjoey', 'Maryke',
           'Pandora', 'Rampage', 'Humbug V', 'Almaz', 'Taifun', 'Madagascar',
           'Glider', 'Squid III', 'Dominican Republic', 'El Salvador',
           'West Germany', 'East Germany', 'Ecuador', 'Belize', 'Nicaragua',
           'Syria', 'Guinea', 'Honduras', 'Congo (Kinshasa)',
           'United States Virgin Islands', 'Barbados', 'Sierra Leone',
           'Paraguay', 'Kuwait', 'Libya', 'Central African Republic',
           'Suriname', 'Somalia', 'Togo', 'Benin', 'Saudi Arabia',
           'Great Britain-1', 'East Germany-1', 'Yugoslavia-1',
           'West Germany-1', 'Burkina Faso', 'Czechoslovakia-1',
           'United States-1', 'Malawi', 'Great Britain-2', 'United States-2',
           'East Germany-3', 'Poland-1', 'West Germany-2', 'North Korea',
           'West Germany-3', 'Czechoslovakia-2', 'Poland-2', 'Albania',
           'East Germany-2', 'Poland-3', 'Swaziland', 'Gabon',
           'Czechoslovakia-3', 'Lesotho', 'Yugoslavia-2',
           'Antigua and Barbuda', 'Papua New Guinea', 'Andorra',
           'Cayman Islands', 'Seychelles', 'Mozambique', 'Cyprus', 'Laos',
           'Angola', 'Botswana', 'Vietnam', 'Jordan', 'Bahrain',
           'United Arab Emirates', 'Qatar', 'Oman', 'North Yemen',
           'Mauritius', 'Solomon Islands', 'Samoa', 'British Virgin Islands',
           'Grenada', 'Equatorial Guinea', 'Rwanda', 'Gambia', 'Djibouti',
           'Bhutan', 'Bangladesh', 'Mauritania', 'Tonga', 'Maldives',
           'Saint Vincent and the Grenadines', 'Nigeria-2', 'South Yemen',
           'South Korea-2', 'Guam', 'Sweden-2', 'Hong Kong-1', 'China-1',
           'Chinese Taipei-1', 'Vanuatu', 'American Samoa', 'Aruba',
           'Chinese Taipei-2', 'China-2', 'Cook Islands', 'South Korea-1',
           'Sweden-1', 'Hong Kong-2', 'Japan-1', 'Nigeria-1', 'Japan-2',
           'Estonia', 'Unified Team', 'France-1', 'Yemen', 'Croatia',
           'Individual Olympic Athletes', 'Romania-2', 'Lithuania', 'Latvia',
           'Germany-1', 'France-3', 'Slovenia', 'Canada-2',
           'Bosnia and Herzegovina', 'Malaysia-1', 'North Korea-1',
           'Romania-1', 'Namibia', 'France-2', 'Bulgaria-2', 'Bulgaria-1',
           'Indonesia-1', 'Germany-2', 'Denmark-2', 'Germany-3', 'Canada-1',
           'North Korea-2', 'Indonesia-2', 'Japan-3', 'United States-3',
           'Unified Team-1', 'Unified Team-2', 'Denmark-1', 'Malaysia-2',
           'Comoros', 'Brunei', 'Azerbaijan', 'Uzbekistan', 'Georgia',
           'Palestine', 'Kazakhstan', 'Ukraine', 'Russia', 'Dominica',
           'Belarus', 'Kyrgyzstan', 'Moldova', 'Guinea Bissau', 'Cape Verde',
           'Turkmenistan', 'Armenia', 'Sao Tome and Principe',
           'Czech Republic', 'Slovakia', 'Saint Lucia',
           'Saint Kitts and Nevis', 'Serbia and Montenegro', 'Mauritius-2',
           'Tajikistan', 'Macedonia', 'Spain-1', 'Australia-2', 'Mauritius-1',
           'Australia-1', 'Nauru', 'Austria-1', 'Brazil-2', 'Burundi',
           'Netherlands-2', 'Austria-2', 'Brazil-1', 'Spain-2',
           'Netherlands-1', 'Czech Republic-1', 'Thailand-2', 'Slovakia-1',
           'Czech Republic-2', 'Slovakia-2', 'Thailand-1', 'Palau', 'Eritrea',
           'Argentina-2', 'Italy-1', 'Argentina-1', 'Italy-2', 'Norway-1',
           'Australia-3', 'Norway-2', 'Federated States of Micronesia',
           'Timor Leste', 'Russia-2', 'Greece-1', 'Hungary-1',
           'Switzerland-2', 'Singapore-2', 'Greece-2', 'Slovenia-1',
           'Russia-1', 'Switzerland-1', 'Hungary-2', 'Slovenia-2', 'Kiribati',
           'Singapore-1', 'Belarus-1', 'Mistral Hojris', 'Relampago',
           'Serbia', 'Whitini Star', 'Ukraine-2', 'Montenegro', 'Briar',
           'Gran Gesto', 'Elvis Va', 'Calimucho', 'Cuba-1',
           'Marshall Islands', 'Oxalis', 'Tuvalu', 'Cuba-2', 'Belarus-2',
           'Don Schufro', 'Lancet', 'Whisper', 'Clearwater', 'Bonaparte',
           'Mythilus', 'Rambo', 'Floresco', 'Ukraine-1', 'Brentina', 'Nadine',
           'Pop Art', 'Quando Quando', 'Diabolo St Maurice', 'Ravel',
           'Notavel', 'Galopin De La Font', 'Orion', 'Greenoaks Dundee',
           'Sunrise', 'Salinero', 'Satchmo', 'Solos Carex', 'Dow Jones',
           'China-3', 'Digby', 'India-1', 'Serbia-2', 'India-2', 'Latvia-1',
           'Latvia-2', 'Serbia-1', 'Refugee Olympic Athletes', 'Kosovo',
           'South Sudan', 'Republic of the Congo', 'Ivory Coast',
           'Refugee Olympic Team', 'Hong Kong, China', 'The Gambia',
           'North Macedonia', 'Democratic Republic of the Congo',
           'Guinea-Bissau', 'São Tomé and Príncipe', 'East Timor',
           'Virgin Islands', 'Eswatini', 'Belgium-1', 'Belgium-2',
           'Soviet Union-2', 'Soviet Union-1', 'Canada-3', 'Soviet Union-3',
           'Great Britain-3', 'Italy-3', 'United States Virgin Islands-1',
           'New Zealand-1', 'United States Virgin Islands-2', 'Portugal-2',
           'New Zealand-2', 'Portugal-1', 'Mexico-1', 'Mexico-2',
           'Puerto Rico-2', 'Monaco-1', 'Puerto Rico-1', 'Monaco-2',
           'Unified Team-3', 'Jamaica-2', 'Ireland-2', 'Ireland-1',
           'Jamaica-1', 'Russia-3', 'Uzbekistan-2', 'Uzbekistan-1',
           'Israel-2', 'Israel-1'], dtype=object)




```python
summer_winter_data_copy.drop(columns = ['Team'], inplace = True)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>NOC</th>
      <th>Games</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26.0</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952 Summer</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# Drop the Games column


```python
summer_winter_data_copy.drop(columns = ['Games'],  inplace = True)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>NOC</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# Age


```python
#change the age column from a float to an integer
```


```python
#check whether there is any missing value in Age column
```


```python
summer_winter_data_copy['Age'].isna().sum()
```




    2030




```python
find_missing_rows = summer_winter_data_copy[summer_winter_data_copy['Age'].isna()]
print(find_missing_rows)
```

                                    Name Sex  Age  NOC  Year  Season         City  \
    12              Ould Lamine Abdallah   M  NaN  FRA  1952  Summer     Helsinki   
    81                    Fahrettin Akba   M  NaN  TUR  1952  Summer     Helsinki   
    82                      Raif Akbulut   M  NaN  TUR  1952  Summer     Helsinki   
    84                         Avni Akgn   M  NaN  TUR  1952  Summer     Helsinki   
    85                        Erdoan Akn   M  NaN  TUR  1952  Summer     Helsinki   
    ...                              ...  ..  ...  ...   ...     ...          ...   
    19046  Christopher Paul "Chris" Lori   M  NaN  CAN  1992  Winter  Albertville   
    22280  Christopher Paul "Chris" Lori   M  NaN  CAN  1994  Winter  Lillehammer   
    22281  Christopher Paul "Chris" Lori   M  NaN  CAN  1994  Winter  Lillehammer   
    25656  Christopher Paul "Chris" Lori   M  NaN  CAN  1998  Winter       Nagano   
    25657  Christopher Paul "Chris" Lori   M  NaN  CAN  1998  Winter       Nagano   
    
               Sport                                     Event Medal  
    12     Athletics             Athletics Men's 10,000 metres   NaN  
    81     Wrestling    Wrestling Men's Flyweight, Greco-Roman   NaN  
    82     Wrestling  Wrestling Men's Lightweight, Greco-Roman   NaN  
    84     Athletics                 Athletics Men's Long Jump   NaN  
    85      Football                   Football Men's Football   NaN  
    ...          ...                                       ...   ...  
    19046  Bobsleigh                      Bobsleigh Men's Four   NaN  
    22280  Bobsleigh                       Bobsleigh Men's Two   NaN  
    22281  Bobsleigh                      Bobsleigh Men's Four   NaN  
    25656  Bobsleigh                       Bobsleigh Men's Two   NaN  
    25657  Bobsleigh                      Bobsleigh Men's Four   NaN  
    
    [2030 rows x 10 columns]
    


```python
find_missing_rows['NOC'].unique()
```




    array(['FRA', 'TUR', 'EGY', 'URS', 'IND', 'GRE', 'HUN', 'SUI', 'SGP',
           'CHI', 'MEX', 'VEN', 'BRA', 'ARG', 'LIB', 'BUL', 'KOR', 'GUA',
           'ITA', 'ROU', 'AUS', 'YUG', 'AFG', 'PHI', 'THA', 'MAL', 'KEN',
           'TCH', 'INA', 'MYA', 'POR', 'ETH', 'IRL', 'PAK', 'FIJ', 'COL',
           'CAN', 'RSA', 'TPE', 'PER', 'URU', 'JPN', 'PUR', 'IRI', 'NGR',
           'TTO', 'GUY', 'SRI', 'AUT', 'LBR', 'UGA', 'VNM', 'BEL', 'CUB',
           'HKG', 'BER', 'UAR', 'IRQ', 'MAR', 'SUD', 'ISR', 'GHA', 'CIV',
           'TUN', 'NIG', 'MAS', 'CAM', 'NEP', 'GUI', 'ISV', 'SYR', 'KUW',
           'LBA', 'CAF', 'SEN', 'TAN', 'ESP', 'ESA', 'MGL', 'PAN', 'BEN',
           'TOG', 'SUR', 'NCA', 'AHO', 'ANT', 'BIZ', 'CGO', 'ALG', 'MOZ',
           'CRC', 'ZAM', 'GBR', 'ECU', 'SLE', 'MLI', 'CMR', 'ZIM', 'DOM',
           'MAD', 'BRN', 'UAE', 'SOM', 'QAT', 'KSA', 'OMA', 'DJI', 'HON',
           'GAM', 'MTN', 'JAM', 'JOR', 'SOL', 'GRN', 'USA', 'BAR', 'PNG',
           'RWA', 'BUR', 'GUM', 'BOT', 'CHA', 'EUN', 'CAY', 'HAI', 'PRK'],
          dtype=object)




```python
countries_with_nan = find_missing_rows['NOC'].unique()
```


```python
temp_data = summer_winter_data_copy.copy()
```


```python
df = pd.DataFrame(temp_data)

# 

# Filter the DataFrame based on the countries in the array
filtered_df = df[df['NOC'].isin(countries_with_nan)]

# Calculate the mean of the 'Age' column, ignoring NaN values
mean_age = filtered_df['Age'].mean().round(0)

print("Mean age for countries with NaN values:", mean_age)
```

    Mean age for countries with NaN values: 25.0
    


```python
summer_winter_data_copy['Age'] = summer_winter_data_copy['Age'].fillna(25.0)
```


```python
summer_winter_data_copy['Age'].isna().sum()
```




    0




```python
summer_winter_data_copy['Age'] = summer_winter_data_copy['Age'].astype(int)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>NOC</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32.0</td>
      <td>FIN</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



# NOC


```python
summer_winter_data_copy['NOC'].unique()
```




    array(['FIN', 'NOR', 'EGY', 'FRA', 'PAK', 'MON', 'ESP', 'SWE', 'ROU',
           'TUR', 'ARG', 'URU', 'GHA', 'DEN', 'HUN', 'CAN', 'POL', 'GER',
           'BRA', 'USA', 'CHI', 'IRI', 'AUS', 'ITA', 'CUB', 'NGR', 'AUT',
           'NED', 'SUI', 'BAH', 'URS', 'BEL', 'GBR', 'MEX', 'POR', 'VEN',
           'ISR', 'RSA', 'LUX', 'BUL', 'PUR', 'SAA', 'IND', 'JPN', 'GRE',
           'NZL', 'PHI', 'TCH', 'YUG', 'BER', 'GUA', 'SGP', 'ISL', 'AHO',
           'IRL', 'VNM', 'PAN', 'HKG', 'LIB', 'KOR', 'SRI', 'JAM', 'LIE',
           'TTO', 'THA', 'MYA', 'GUY', 'INA', 'CHN', 'AFG', 'MAL', 'KEN',
           'COL', 'ETH', 'PER', 'FIJ', 'NBO', 'TPE', 'UGA', 'CAM', 'LBR',
           'UAR', 'SUD', 'IRQ', 'MAR', 'TUN', 'RHO', 'WIF', 'MLT', 'SMR',
           'ZIM', 'HAI', 'TAN', 'CIV', 'MAS', 'ZAM', 'MGL', 'CRC', 'MLI',
           'NIG', 'SEN', 'CGO', 'NEP', 'CHA', 'BOL', 'ALG', 'CMR', 'MAD',
           'DOM', 'ESA', 'FRG', 'GDR', 'ECU', 'BIZ', 'NCA', 'SYR', 'GUI',
           'HON', 'COD', 'ISV', 'BAR', 'SLE', 'PAR', 'KUW', 'LBA', 'CAF',
           'SUR', 'SOM', 'TOG', 'BEN', 'KSA', 'BUR', 'MAW', 'PRK', 'ALB',
           'SWZ', 'GAB', 'LES', 'ANT', 'PNG', 'AND', 'CAY', 'SEY', 'MOZ',
           'CYP', 'LAO', 'ANG', 'BOT', 'VIE', 'JOR', 'BRN', 'UAE', 'QAT',
           'OMA', 'YAR', 'MRI', 'SOL', 'SAM', 'IVB', 'GRN', 'GEQ', 'RWA',
           'GAM', 'DJI', 'BHU', 'BAN', 'MTN', 'TGA', 'MDV', 'VIN', 'YMD',
           'GUM', 'VAN', 'ASA', 'ARU', 'COK', 'EST', 'EUN', 'YEM', 'CRO',
           'IOA', 'LTU', 'LAT', 'SLO', 'BIH', 'NAM', 'COM', 'BRU', 'AZE',
           'UZB', 'GEO', 'PLE', 'KAZ', 'UKR', 'RUS', 'DMA', 'BLR', 'KGZ',
           'MDA', 'GBS', 'CPV', 'TKM', 'ARM', 'STP', 'CZE', 'SVK', 'LCA',
           'SKN', 'SCG', 'TJK', 'MKD', 'NRU', 'BDI', 'PLW', 'ERI', 'FSM',
           'TLS', 'KIR', 'SRB', 'MNE', 'MHL', 'TUV', 'ROT', 'KOS', 'SSD',
           'ROC', 'EOR', 'LBN'], dtype=object)




```python
pip install pycountry
```

    Requirement already satisfied: pycountry in c:\users\mbogu\downloads\newfolder\lib\site-packages (23.12.11)
    Note: you may need to restart the kernel to use updated packages.
    


```python
import pycountry
```


```python
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
```

    Finland(FIN)
    Norway(NOR)
    Egypt(EGY)
    France(FRA)
    Pakistan(PAK)
    Spain(ESP)
    Sweden(SWE)
    Romania(ROU)
    Türkiye(TUR)
    Argentina(ARG)
    Ghana(GHA)
    Hungary(HUN)
    Canada(CAN)
    Poland(POL)
    Brazil(BRA)
    United States(USA)
    Australia(AUS)
    Italy(ITA)
    Cuba(CUB)
    Austria(AUT)
    Belgium(BEL)
    United Kingdom(GBR)
    Mexico(MEX)
    Venezuela, Bolivarian Republic of(VEN)
    Israel(ISR)
    Luxembourg(LUX)
    India(IND)
    Japan(JPN)
    New Zealand(NZL)
    Singapore(SGP)
    Iceland(ISL)
    Ireland(IRL)
    Viet Nam(VNM)
    Panama(PAN)
    Hong Kong(HKG)
    Korea, Republic of(KOR)
    Jamaica(JAM)
    Liechtenstein(LIE)
    Trinidad and Tobago(TTO)
    Thailand(THA)
    Guyana(GUY)
    China(CHN)
    Afghanistan(AFG)
    Kenya(KEN)
    Colombia(COL)
    Ethiopia(ETH)
    Peru(PER)
    Uganda(UGA)
    Liberia(LBR)
    Iraq(IRQ)
    Morocco(MAR)
    Tunisia(TUN)
    Malta(MLT)
    San Marino(SMR)
    Côte d'Ivoire(CIV)
    Mali(MLI)
    Senegal(SEN)
    Bolivia, Plurinational State of(BOL)
    Cameroon(CMR)
    Dominican Republic(DOM)
    Ecuador(ECU)
    Syrian Arab Republic(SYR)
    Congo, The Democratic Republic of the(COD)
    Sierra Leone(SLE)
    Central African Republic(CAF)
    Suriname(SUR)
    Somalia(SOM)
    Benin(BEN)
    Korea, Democratic People's Republic of(PRK)
    Albania(ALB)
    Eswatini(SWZ)
    Gabon(GAB)
    Papua New Guinea(PNG)
    Andorra(AND)
    Mozambique(MOZ)
    Cyprus(CYP)
    Lao People's Democratic Republic(LAO)
    Jordan(JOR)
    Brunei Darussalam(BRN)
    Qatar(QAT)
    Rwanda(RWA)
    Djibouti(DJI)
    Maldives(MDV)
    Guam(GUM)
    Cook Islands(COK)
    Estonia(EST)
    Yemen(YEM)
    Lithuania(LTU)
    Bosnia and Herzegovina(BIH)
    Namibia(NAM)
    Comoros(COM)
    Azerbaijan(AZE)
    Uzbekistan(UZB)
    Georgia(GEO)
    Kazakhstan(KAZ)
    Ukraine(UKR)
    Russian Federation(RUS)
    Dominica(DMA)
    Belarus(BLR)
    Kyrgyzstan(KGZ)
    Moldova, Republic of(MDA)
    Cabo Verde(CPV)
    Turkmenistan(TKM)
    Armenia(ARM)
    Sao Tome and Principe(STP)
    Czechia(CZE)
    Slovakia(SVK)
    Saint Lucia(LCA)
    Tajikistan(TJK)
    North Macedonia(MKD)
    Nauru(NRU)
    Burundi(BDI)
    Palau(PLW)
    Eritrea(ERI)
    Micronesia, Federated States of(FSM)
    Timor-Leste(TLS)
    Kiribati(KIR)
    Serbia(SRB)
    Montenegro(MNE)
    Marshall Islands(MHL)
    Tuvalu(TUV)
    South Sudan(SSD)
    Lebanon(LBN)
    


```python
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

```


```python
summer_winter_data_copy['NOC'] = summer_winter_data_copy['NOC'].replace(noc_mapping)

```


```python
summer_winter_data_copy.rename(columns={'Team Country': 'Team_Country'}, inplace=True)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team_Country</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>No Medal</td>
    </tr>
  </tbody>
</table>
</div>



# Medal


```python
summer_winter_data_copy['Medal'].fillna('No Medal', inplace=True)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team_Country</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>No Medal</td>
    </tr>
  </tbody>
</table>
</div>




```python
summer_winter_data_copy.reset_index(drop=True, inplace=True)
summer_winter_data_copy.index += 1
print(summer_winter_data_copy)
```

                                      Name Sex  Age             Team Country  \
    1       Einar Ferdinand "Einari" Aalto   M   26            Finland (FIN)   
    2              Paavo Johannes Aaltonen   M   32            Finland (FIN)   
    3              Paavo Johannes Aaltonen   M   32            Finland (FIN)   
    4              Paavo Johannes Aaltonen   M   32            Finland (FIN)   
    5              Paavo Johannes Aaltonen   M   32            Finland (FIN)   
    ...                                ...  ..  ...                      ...   
    239981          Stepan Olegovich Zuyev   M   25  Russian Federation(RUS)   
    239982              Kristaps Zvejnieks   M   21              Latvia(LAT)   
    239983              Kristaps Zvejnieks   M   21              Latvia(LAT)   
    239984                        Piotr ya   M   27              Poland(POL)   
    239985                        Piotr ya   M   27              Poland(POL)   
    
            Year  Season      City          Sport  \
    1       1952  Summer  Helsinki       Swimming   
    2       1952  Summer  Helsinki     Gymnastics   
    3       1952  Summer  Helsinki     Gymnastics   
    4       1952  Summer  Helsinki     Gymnastics   
    5       1952  Summer  Helsinki     Gymnastics   
    ...      ...     ...       ...            ...   
    239981  2014  Winter     Sochi  Alpine Skiing   
    239982  2014  Winter     Sochi  Alpine Skiing   
    239983  2014  Winter     Sochi  Alpine Skiing   
    239984  2014  Winter     Sochi    Ski Jumping   
    239985  2014  Winter     Sochi    Ski Jumping   
    
                                               Event     Medal  
    1            Swimming Men's 400 metres Freestyle  No Medal  
    2         Gymnastics Men's Individual All-Around  No Medal  
    3               Gymnastics Men's Team All-Around    Bronze  
    4                Gymnastics Men's Floor Exercise  No Medal  
    5                   Gymnastics Men's Horse Vault  No Medal  
    ...                                          ...       ...  
    239981                Alpine Skiing Men's Slalom  No Medal  
    239982          Alpine Skiing Men's Giant Slalom  No Medal  
    239983                Alpine Skiing Men's Slalom  No Medal  
    239984  Ski Jumping Men's Large Hill, Individual  No Medal  
    239985        Ski Jumping Men's Large Hill, Team  No Medal  
    
    [239985 rows x 10 columns]
    


```python
summer_winter_data_copy.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team Country</th>
      <th>Year</th>
      <th>Season</th>
      <th>City</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>No Medal</td>
    </tr>
  </tbody>
</table>
</div>



# City


```python
summer_winter_data_copy.rename(columns = {'City': 'Host_ City_Country'}, inplace= True)
```


```python
summer_winter_data_copy.head(40)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team_Country</th>
      <th>Year</th>
      <th>Season</th>
      <th>Host_ City_Country</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Parallel Bars</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horizontal Bar</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Rings</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Pommelled Horse</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Hans Aasns</td>
      <td>M</td>
      <td>49</td>
      <td>Norway (NOR)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Shooting</td>
      <td>Shooting Men's Trap</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Mohamed Fakhry Rifaat Abbas</td>
      <td>M</td>
      <td>19</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Diving</td>
      <td>Diving Men's Platform</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Youssef Mohamed Abbas</td>
      <td>M</td>
      <td>31</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Basketball</td>
      <td>Basketball Men's Basketball</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ould Lamine Abdallah</td>
      <td>M</td>
      <td>25</td>
      <td>France(FRA)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Athletics</td>
      <td>Athletics Men's 10,000 metres</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Abdelgani Hassan Abdel Fattah</td>
      <td>M</td>
      <td>31</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Athletics</td>
      <td>Athletics Men's Marathon</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Osman Abdel Hafeez</td>
      <td>M</td>
      <td>35</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's Foil, Team</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Osman Abdel Hafeez</td>
      <td>M</td>
      <td>35</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's epee, Team</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Dorri Abdel Kader Said</td>
      <td>M</td>
      <td>25</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Water Polo</td>
      <td>Water Polo Men's Water Polo</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Dorri Abdel Kader Said</td>
      <td>M</td>
      <td>25</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Swimming</td>
      <td>Swimming Men's 100 metres Freestyle</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Mohamed Ali Abdel Kerim</td>
      <td>M</td>
      <td>24</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Weightlifting</td>
      <td>Weightlifting Men's Light-Heavyweight</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Mohamed Fathallah Abdel Rahman</td>
      <td>M</td>
      <td>37</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's epee, Individual</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Mohamed Fathallah Abdel Rahman</td>
      <td>M</td>
      <td>37</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's epee, Team</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Mohamed Fathallah Abdel Rahman</td>
      <td>M</td>
      <td>37</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's Sabre, Individual</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Mohamed Fathallah Abdel Rahman</td>
      <td>M</td>
      <td>37</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's Sabre, Team</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Fathi Ali Abdel Rahman</td>
      <td>M</td>
      <td>20</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Boxing</td>
      <td>Boxing Men's Welterweight</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Ben Ahmed Abdelkrim</td>
      <td>M</td>
      <td>20</td>
      <td>France(FRA)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Athletics</td>
      <td>Athletics Men's 5,000 metres</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Ibrahim Abdrabbou</td>
      <td>M</td>
      <td>27</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Boxing</td>
      <td>Boxing Men's Bantamweight</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Qazi Abdul Waheed</td>
      <td>M</td>
      <td>30</td>
      <td>Pakistan(PAK)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Hockey</td>
      <td>Hockey Men's Hockey</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Roger Abel</td>
      <td>M</td>
      <td>52</td>
      <td>Monaco(MON)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Shooting</td>
      <td>Shooting Men's Small-Bore Rifle, Three Positio...</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Roger Abel</td>
      <td>M</td>
      <td>52</td>
      <td>Monaco(MON)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Shooting</td>
      <td>Shooting Men's Small-Bore Rifle, Prone, 50 metres</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Juan Luis Abelln Pallahi</td>
      <td>M</td>
      <td>19</td>
      <td>Spain(ESP)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Water Polo</td>
      <td>Water Polo Men's Water Polo</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Olof Viktor "Olle" berg</td>
      <td>M</td>
      <td>27</td>
      <td>Sweden(SWE)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Athletics</td>
      <td>Athletics Men's 1,500 metres</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Galal El-Din Abdel Meguid Abou El-Kheir</td>
      <td>M</td>
      <td>24</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Water Polo</td>
      <td>Water Polo Men's Water Polo</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Youssef Kamel Mohamed Abou Ouf</td>
      <td>M</td>
      <td>28</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Basketball</td>
      <td>Basketball Men's Basketball</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Ahmed Farid Abou-Shadi</td>
      <td>M</td>
      <td>42</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's Sabre, Individual</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Ahmed Farid Abou-Shadi</td>
      <td>M</td>
      <td>42</td>
      <td>Egypt(EGY)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Fencing</td>
      <td>Fencing Men's Sabre, Team</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Elisabeta Abrudeanu</td>
      <td>F</td>
      <td>26</td>
      <td>Romania(ROU)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Women's Individual All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Elisabeta Abrudeanu</td>
      <td>F</td>
      <td>26</td>
      <td>Romania(ROU)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Women's Team All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Elisabeta Abrudeanu</td>
      <td>F</td>
      <td>26</td>
      <td>Romania(ROU)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Women's Team Portable Apparatus</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Elisabeta Abrudeanu</td>
      <td>F</td>
      <td>26</td>
      <td>Romania(ROU)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Women's Floor Exercise</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Elisabeta Abrudeanu</td>
      <td>F</td>
      <td>26</td>
      <td>Romania(ROU)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki</td>
      <td>Gymnastics</td>
      <td>Gymnastics Women's Horse Vault</td>
      <td>No Medal</td>
    </tr>
  </tbody>
</table>
</div>




```python
summer_winter_data_copy['Host_ City_Country'].unique()
```




    array(['Helsinki', 'Melbourne', 'Stockholm', 'Roma', 'Tokyo',
           'Mexico City', 'Munich', 'Montreal', 'Moskva', 'Los Angeles',
           'Seoul', 'Barcelona', 'Atlanta', 'Sydney', 'Athina', 'Beijing',
           'London', 'Rio de Janeiro', 'Oslo', "Cortina d'Ampezzo",
           'Squaw Valley', 'Innsbruck', 'Grenoble', 'Sapporo', 'Lake Placid',
           'Sarajevo', 'Calgary', 'Albertville', 'Lillehammer', 'Nagano',
           'Salt Lake City', 'Torino', 'Vancouver', 'Sochi'], dtype=object)




```python
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
```


```python
summer_winter_data_copy['Host_ City_Country'] = summer_winter_data_copy['Host_ City_Country'].replace(host_city_country_mapping)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Team_Country</th>
      <th>Year</th>
      <th>Season</th>
      <th>Host_ City_Country</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Einar Ferdinand "Einari" Aalto</td>
      <td>M</td>
      <td>26</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Paavo Johannes Aaltonen</td>
      <td>M</td>
      <td>32</td>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>No Medal</td>
    </tr>
  </tbody>
</table>
</div>




```python
summer_winter_data_copy.drop(columns = ['Sex', 'Age'], inplace = True)
```


```python
summer_winter_data_copy.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NOC</th>
      <th>Year</th>
      <th>Season</th>
      <th>Host_ City_Country</th>
      <th>Sport</th>
      <th>Event</th>
      <th>Medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Swimming</td>
      <td>Swimming Men's 400 metres Freestyle</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Individual All-Around</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Team All-Around</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Floor Exercise</td>
      <td>No Medal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Finland (FIN)</td>
      <td>1952</td>
      <td>Summer</td>
      <td>Helsinki, Finland</td>
      <td>Gymnastics</td>
      <td>Gymnastics Men's Horse Vault</td>
      <td>No Medal</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```
