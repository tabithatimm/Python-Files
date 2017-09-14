import requests
from lxml import objectify
from lxml import etree

#input variables
parameter = 'tavg'
state_num = '44'
division = '0'
month = '6'
periods = '6'
year = '2016'

#create string from variables
template1 = 'https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?'
template2 = 'parameter=%s&'
template2 = template2 + 'state=%s&div=%s&month=%s&'
template2 = template2 + 'periods[]=%s&year=%s'
insert_info = (parameter, state_num, division, month, periods, year)
template2 = template2 % insert_info
template_final = template1 + template2

response = requests.get(template_final).content

root = objectify.fromstring(response)

#data without identifiers
print 'ttimm'
print root.data['value']
print root.data['twentiethCenturyMean']
print root.data['lowRank']
print root.data['highRank']