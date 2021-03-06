# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damagesAll(damage_data):
  conversion = {"M": 1000000,
               "B": 1000000000}

  updated_damages = []
  for data in damage_data:
    if data[-1] == 'B':
      data = float(data[:-1]) * conversion["B"] 
    elif data[-1] == 'M':
      data = float(data[:-1]) * conversion["M"]
    elif data == 'Damages not recorded' :
      data = 'Damages not recorded' 
    updated_damages.append(data)
  return updated_damages
#print(damagesAll(damages))
updated_damages = damagesAll(damages)


# write your construct hurricane dictionary function here:
def hurricanes(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_records = {}
  for x in range(len(names)):
    hurricane_records[names[x]] = {'Name': names[x], 'Month': months[x], 'Year': years[x], 'Max Sustained Wind': max_sustained_winds[x], 'Areas Affected': areas_affected[x], 'Damage': damages[x], 'Death': deaths[x]}
  return hurricane_records

hurricanes = hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)




# write your construct hurricane by year dictionary function here:

def hurricane_year(hurricanes):
  hurricane_year = {}
  for result in hurricanes.values():
    year = result['Year']
    if year not in hurricane_year:
      hurricane_year[year] = [result]
    else: 
      hurricane_year[year].append(result)
  return hurricane_year


print(hurricane_year(hurricanes))
# write your count affected areas function here:
def affected_areas_count(affected_areas):
  hurricane_affected_areas_count = {}
  for areas in affected_areas:
    for area in areas: 
      if area not in hurricane_affected_areas_count:
        hurricane_affected_areas_count[area] = 1
      else:
        hurricane_affected_areas_count[area] += 1
  return hurricane_affected_areas_count

count_affected_areas = affected_areas_count(areas_affected)






# write your find most affected area function here:
def most_affected_area(affected_areas_count):
  max_area = ""
  max_area_count = 0
  for area, count in affected_areas_count.items():
    if max_area_count < count:
      max_area = area
      max_area_count = count
  return "{max_area} is affected by most hurricanes by {max_area_count} times.".format(max_area = max_area, max_area_count = max_area_count)

# print(most_affected_area(count_affected_areas))





# write your greatest number of deaths function here:
def hurricane_deaths(hurricane_records):
  max_mortality_cane = ""
  max_mortality = 0
  for name, record in hurricane_records.items():
    if record["Death"] > max_mortality:
      max_mortality_cane = name
      max_mortality = record["Death"]
  return "{0} hurricane caused greatest number of  deaths. It caused {1} deaths.".format(max_mortality_cane, max_mortality)

#print(hurricane_deaths(hurricanes))



# write your catgeorize by mortality function here:


def rate_mortality_scale(hurricane_records):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  scale = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for record in hurricane_records.values():
    if record["Death"] == mortality_scale[0]:
        scale[0].append(record)
    if record["Death"] <= mortality_scale[1]:
        scale[1].append(record)
    if record["Death"] <= mortality_scale[2]:
        scale[2].append(record)
    if record["Death"] <= mortality_scale[3]:
        scale[3].append(record)
    if record["Death"] <= mortality_scale[4]:
        scale[4].append(record)
    if record["Death"] > mortality_scale[4]:
        scale[5].append(record)
  return scale
  
#print(rate_mortality_scale(hurricanes))

# write your greatest damage function here:

def max_hurricane_damage(hurricane_records):
  max_damage_hurricane = ""
  max_damage = 0
  for name, record in hurricane_records.items():
    if (record["Damage"] != 'Damages not recorded') and (record["Damage"] > max_damage):
      max_damage_hurricane = name
      max_damage = record["Damage"]
  return "{0} hurricane caused greatest daamages and it costs {1}.".format(max_damage_hurricane, max_damage)

#print(max_hurricane_damage(hurricanes))


# write your catgeorize by damage function here:




def damage_scale(hurricane_records):
  damage_scale = {0: 0, 1: 100000000,\
                   2: 1000000000,
                   3: 10000000000,
                   4: 50000000000}
  scale = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for record in hurricane_records:
    damage_cost = hurricanes[record]['Damage']
    if damage_cost != "Damages not recorded":
     if damage_cost == damage_scale[0]:
        scale[0].append(hurricanes[record])
     elif damage_cost > damage_scale[0] and damage_cost <= damage_scale[1]:
        scale[1].append(hurricanes[record])
     elif damage_cost > damage_scale[1] and damage_cost <= damage_scale[2]:
        scale[2].append(hurricanes[record])
     elif damage_cost > damage_scale[2] and damage_cost <= damage_scale[3]:
        scale[3].append(hurricanes[record])
     elif damage_cost > damage_scale[3] and damage_cost <= damage_scale[4]:
        scale[4].append(hurricanes[record])
     elif damage_cost > damage_scale[4]:
        scale[5].append(hurricanes[record])
  return scale
  
print(damage_scale(hurricanes))
# for x in damage_scale(hurricanes):
#   print(x)





