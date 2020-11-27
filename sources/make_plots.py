import matplotlib.pyplot as plt
import pandas as pd

plt.close('all')

df = pd.read_csv("data/CompactData_IFS_M.GB.PMP_IX.csv")
df = df.set_index(pd.to_datetime(df['date']))['value'].astype('float')
title = f'Import Prices'
recentdt = df.index[-1].strftime('%B %Y')
recentval = round(df[-1], 1)
recent = f'Most recent: {recentdt}: {recentval}'
source = 'Source: IMF IFS'

# Basic plot
plot0 = df.plot(title=title,  label='UK', colormap='Set1')
plot0.set_xlabel(f'{recent}; {source}')

df = pd.read_csv("data/CompactData_IFS_Q.AU.PMP_IX.csv")
df = df.set_index(pd.to_datetime(df['date']))['value'].astype('float')


# Basic plot
plot1 = df.plot(title=title, label='AU', colormap='gray')
plot1.set_xlabel(f'{recent}; {source}')

plt.legend()

plt.savefig("figures/plot.png")




plt.close('all')
hist = df.hist(bins=30, color='#228B22', rwidth=0.85)
plt.title("Import volumes distribution (AU)")
plt.xlabel('Volume (USD millions)')
plt.ylabel('Frequency')
plt.savefig("figures/histo.png")