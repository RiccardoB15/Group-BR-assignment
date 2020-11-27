#! /usr/bin/python3

import requests
import pandas as pd
import matplotlib.pyplot as plt


url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
keys = ['CompactData/IFS/M.GB.PMP_IX', 'CompactData/IFS/Q.AU.PMP_IX'] # adjust codes here
trailer = '.?startPeriod=1957&endPeriod=2016'

# Navigate to series in API-returned JSON data
for key in keys:
	data = (requests.get(f'{url}{key}{trailer}').json()
	        ['CompactData']['DataSet']['Series'])

	baseyr = data['@BASE_YEAR']  # Save the base year

	# Create pandas dataframe from the observations
	data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
	             for obs in data['Obs']]

	df = pd.DataFrame(data_list, columns=['date', 'value'])
	     
	df = df.set_index(pd.to_datetime(df['date']))['value'].astype('float')

	printable_key = key.replace("/", "_")
	df.to_csv(f'data/{printable_key}.csv', header=True)