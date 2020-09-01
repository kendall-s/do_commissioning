#!/usr/bin/env python
# coding: utf-8

# # This notebook contains the code for plotting the Dissolved Oxygen Commissioning plots

# ### Two new dissolved oxygen instruments were purchased from Scripps - these new instruments were subsequently taken on in2020_e01 for commissioning. The data below was collected on the voyage where all 3 instruments (2 new, 1 old) were setup in the same laboratory space and operated in parallel.

# #### Imports and style sets:

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import seawater as sw
import scipy.stats as sci_st

sns.set(style="whitegrid") # I like this
mpl.rc('font', family='serif') # Cast serif as the font
mpl.rc('figure', figsize=[8, 5]) # Set fig size to something more fitting for A4 word doc


# ### Variables for locations of datafiles (in same order as headings)

# In[3]:


INDEPENDENT_IODATE_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/independent_iodate.csv'
DEP_1_DEEP_REPLICATES_SINGLE_NISKINS_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/dep_1_deep_replicates_single_niskins.csv'
DEP_1_DEEP_REPLICATES_SHARED_NISKINS_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/dep_1_deep_replicates_shared_niskins.csv'
ATMOSPHERIC_DIFF_INSTRUMENTS_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/atmospheric_diff_instruments.csv'
ATMOSPHERIC_ONE_INSTRUMENT_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/atmospheric_one_instrument.csv'
PROFILE_COMPARISON_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/profile_comparison.csv'
DEP_2_DEEP_REPLICATES_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/dep_2_deep_replicates.csv'

COMBINED_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/combined.csv'


# ---

# ## 3.1 Independent Iodate Standards 

# In[4]:


iodate_df = pd.read_csv(INDEPENDENT_IODATE_DATA)


# In[5]:


iodate_df.head()


# ### 3.1.1 Iodate Standards across Instruments Boxplot

# In[6]:


sns.boxplot(iodate_df['Instrument'], iodate_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Independent Iodate Standard', fontsize=18)

plt.tight_layout()

# Comment or include next two lines if wanting to scale chart for all
#data_mean = iodate_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('independent_iodate_standards.svg', format='svg')


# ### 3.1.2 Iodate Standards Descriptive Statistics

# In[7]:


iodate_df.groupby(['Instrument'])['O2µmol/L'].describe()


# ---

# ## 3.2 Repeated Deep Sample Measurements: 1

# ### 3.2.1 Samples from One Niskin per Instrument

# In[8]:


deep_reps_single_df = pd.read_csv(DEP_1_DEEP_REPLICATES_SINGLE_NISKINS_DATA)


# In[9]:


deep_reps_single_df.head()


# #### 3.2.1.1 Samples from One Niskin Boxplot

# In[10]:


sns.boxplot(deep_reps_single_df['Instrument'], deep_reps_single_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('D1 Replicate Samples: 1 Niskin ea', fontsize=18)

plt.tight_layout()

# Comment or include next two lines if wanting to scale chart for all
#data_mean = deep_reps_single_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('replicate_deep_samples_1_single.svg', format='svg')


# #### 3.2.1.2 Descriptive Statistics

# In[11]:


deep_reps_single_df.groupby(['Instrument'])['O2µmol/L'].describe()


# #### 3.2.1.3 T-Test Comparison of Means

# In[12]:


deep_reps_single_newa = deep_reps_single_df.loc[deep_reps_single_df['Instrument'] == 'New A']
deep_reps_single_newb = deep_reps_single_df.loc[deep_reps_single_df['Instrument'] == 'New B']
deep_reps_single_old = deep_reps_single_df.loc[deep_reps_single_df['Instrument'] == 'Old']


# ##### Compare New A to Old instrument

# In[13]:


result = sci_st.ttest_ind(deep_reps_single_newa['O2µmol/L'], deep_reps_single_old['O2µmol/L'])
print(f'Comparison of the New A instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance !')


# ##### Compare New B to Old instrument

# In[14]:


result = sci_st.ttest_ind(deep_reps_single_newb['O2µmol/L'], deep_reps_single_old['O2µmol/L'])
print(f'Comparison of the New B instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance !')


# ### 3.2.2 Samples from Two Niskins for all Instruments

# In[15]:


deep_reps_shared_df = pd.read_csv(DEP_1_DEEP_REPLICATES_SHARED_NISKINS_DATA)


# In[16]:


deep_reps_shared_df.head()


# #### 3.2.2.1 Samples from Shared Niskins Boxplot

# In[17]:


sns.boxplot(deep_reps_shared_df['Instrument'], deep_reps_shared_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('D1 Replicate Samples: 2 Niskin shared', fontsize=18)

plt.tight_layout()

# Comment or include next two lines if wanting to scale chart for all
#data_mean = deep_reps_shared_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('replicate_deep_samples_1_shared.svg', format='svg')


# #### 3.2.2.2 Descriptive Statistics

# In[18]:


deep_reps_shared_df.groupby(['Instrument'])['O2µmol/L'].describe()


# ---

# ## 3.3 Atmospheric Saturated Sample: All Instruments

# In[19]:


atmospheric_all_df = pd.read_csv(ATMOSPHERIC_DIFF_INSTRUMENTS_DATA)


# In[20]:


atmospheric_all_df.head()


# ### 3.3.1 Atmospheric Saturated Sample Boxplot (auto-scale)

# #### Plot just initial box plot scaled to the measurements

# In[21]:


sns.boxplot(atmospheric_all_df['Instrument'], atmospheric_all_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Saturated Sample', fontsize=18)

plt.tight_layout()

# Comment or include next two lines if wanting to scale chart for all
#data_mean = atmospheric_all_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('atmospheric_diff_instruments.svg', format='svg')


# ### 3.3.2 Atmospheric Saturated Sample Boxplot (QC Control Lines)

# #### Plot with lines to indicate various QC limits

# In[22]:


sns.boxplot(atmospheric_all_df['Instrument'], atmospheric_all_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Saturated Sample w/QC Bars', fontsize=18)

# Calculate the theoretical saturation
MEASURED_SALINITY = 0
MEASURED_TEMPERATURE = 21.5
max_saturation = sw.satO2(MEASURED_SALINITY, MEASURED_TEMPERATURE)
max_saturation_mol = max_saturation * 44.66

max_saturation_mol_1pct = max_saturation_mol * 0.01

# Plot the calculated saturation as a line on the chart
plt.plot([-0.5, 2.5], [max_saturation_mol, max_saturation_mol], color="#32a858")

# Plot the 1% upper and lower lines
plt.plot([-0.5, 2.5], [max_saturation_mol-max_saturation_mol_1pct, max_saturation_mol-max_saturation_mol_1pct], color="#2c5aa3")
plt.plot([-0.5, 2.5], [max_saturation_mol+max_saturation_mol_1pct, max_saturation_mol+max_saturation_mol_1pct], color="#2c5aa3")

# Plot the +- 1uM upper and lower lines
plt.plot([-0.5, 2.5], [max_saturation_mol-1, max_saturation_mol-1], color="#2c9fa3")
plt.plot([-0.5, 2.5], [max_saturation_mol+1, max_saturation_mol+1], color="#2c9fa3")

# Plot the annotations
plt.annotate('+1µM', xy=(2.28, max_saturation_mol+1-0.25))
plt.annotate('+1%', xy=(2.32, max_saturation_mol+max_saturation_mol_1pct-0.25))
plt.annotate('Calc. Sat.', xy=(2.14, max_saturation_mol-0.25))

plt.tight_layout()

# Comment or include next two lines if wanting to scale chart for all
#data_mean = atmospheric_all_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('atmospheric_diff_instruments_with_bars.svg', format='svg')


# ### 3.3.3 Descriptive Statistics

# In[23]:


atmospheric_all_df.groupby(['Instrument'])['O2µmol/L'].describe()


# ---

# ## 3.4 Atmospheric Saturated Sample: One Instrument

# In[24]:


atmospheric_one_df = pd.read_csv(ATMOSPHERIC_ONE_INSTRUMENT_DATA)


# In[25]:


atmospheric_one_df.head()


# ### 3.4.1 Atmospheric Saturated Sample: Instrument New B (auto-scale)

# In[26]:


sns.lineplot(atmospheric_one_df.index, atmospheric_one_df['O2µmol/L'], lw=0, marker="o", ms=10)

plt.xlabel("Sample", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Saturated Sample: Instrument New B', fontsize=18)

plt.tight_layout()

plt.savefig('atmospheric_one_instrument.svg', format='svg')


# ### 3.4.2 Atmospheric Saturated Sample: Instrument New B (QC Control Limits)

# In[27]:


sns.lineplot(atmospheric_one_df.index, atmospheric_one_df['O2µmol/L'], lw=0, marker="o", ms=10)

plt.xlabel("Sample", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Saturated Sample: Instrument New B', fontsize=18)

plt.tight_layout()

# Calculate the theoretical saturation
MEASURED_SALINITY = 0
MEASURED_TEMPERATURE = 21.5
max_saturation = sw.satO2(MEASURED_SALINITY, MEASURED_TEMPERATURE)
max_saturation_mol = max_saturation * 44.66

max_saturation_mol_1pct = max_saturation_mol * 0.01

# Plot the calculated saturation as a line on the chart
plt.plot([-1, 13], [max_saturation_mol, max_saturation_mol], color="#32a858")

# Plot the 1% upper and lower lines
plt.plot([-1, 13], [max_saturation_mol-max_saturation_mol_1pct, max_saturation_mol-max_saturation_mol_1pct], color="#2c5aa3")
plt.plot([-1, 13], [max_saturation_mol+max_saturation_mol_1pct, max_saturation_mol+max_saturation_mol_1pct], color="#2c5aa3")

# Plot the +- 1uM upper and lower lines
plt.plot([-1, 13], [max_saturation_mol-1, max_saturation_mol-1], color="#2c9fa3")
plt.plot([-1, 13], [max_saturation_mol+1, max_saturation_mol+1], color="#2c9fa3")

# Plot the annotations
plt.annotate('+1µM', xy=(12, max_saturation_mol+1-0.25))
plt.annotate('+1%', xy=(12.18, max_saturation_mol+max_saturation_mol_1pct-0.25))
plt.annotate('Calc. Sat.', xy=(11.4, max_saturation_mol-0.25))

plt.xlim(-1, 13)

plt.savefig('atmospheric_one_instrument_with_bars.svg', format='svg')


# ### 3.4.3 Atmospheric Saturated Sample: Instrument New B Boxplot (QC Control Limits)

# In[28]:


sns.boxplot(atmospheric_one_df['Instrument'], atmospheric_one_df['O2µmol/L'])

plt.xlabel("Sample", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Saturated Sample: Instrument New B', fontsize=18)

plt.tight_layout()

# Calculate the theoretical saturation
MEASURED_SALINITY = 0
MEASURED_TEMPERATURE = 21.5
max_saturation = sw.satO2(MEASURED_SALINITY, MEASURED_TEMPERATURE)
max_saturation_mol = max_saturation * 44.66

max_saturation_mol_1pct = max_saturation_mol * 0.01

# Plot the calculated saturation as a line on the chart
plt.plot([-0.5, 0.5], [max_saturation_mol, max_saturation_mol], color="#32a858")

# Plot the 1% upper and lower lines
plt.plot([-0.5, 0.5], [max_saturation_mol-max_saturation_mol_1pct, max_saturation_mol-max_saturation_mol_1pct], color="#2c5aa3")
plt.plot([-0.5, 0.5], [max_saturation_mol+max_saturation_mol_1pct, max_saturation_mol+max_saturation_mol_1pct], color="#2c5aa3")

# Plot the +- 1uM upper and lower lines
plt.plot([-0.5, 0.5], [max_saturation_mol-1, max_saturation_mol-1], color="#2c9fa3")
plt.plot([-0.5, 0.5], [max_saturation_mol+1, max_saturation_mol+1], color="#2c9fa3")

# Plot the annotations
plt.annotate('+1µM', xy=(0.42, max_saturation_mol+1-0.25))
plt.annotate('+1%', xy=(0.44, max_saturation_mol+max_saturation_mol_1pct-0.25))
plt.annotate('Calc. Sat.', xy=(0.38, max_saturation_mol-0.23))

# Comment or include next two lines if wanting to scale chart for all
#data_mean = atmospheric_one_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('atmospheric_one_instrument_with_bars-boxplot-version.svg', format='svg')


# ### 3.4.4 Descriptive Statistics

# In[29]:


atmospheric_one_df['O2µmol/L'].describe()


# ---

# ## 3.5 Water Profile Comparison

# In[30]:


profile_comparison_df = pd.read_csv(PROFILE_COMPARISON_DATA)


# In[31]:


profile_comparison_df.head()


# ### 3.5.1 Water Profile Plot

# In[32]:


instrument_new_a_df = profile_comparison_df.loc[profile_comparison_df['Instrument'] == 'New A']
instrument_old_df = profile_comparison_df.loc[profile_comparison_df['Instrument'] == 'Old']

plt.plot(instrument_new_a_df['O2µmol/L'], instrument_new_a_df['Pressure'], lw=0, marker="o", ms=14, mfc="none", mew=1.5, label="New A")

plt.plot(instrument_old_df['O2µmol/L'], instrument_old_df['Pressure'], lw=0, marker=".", ms=16, mfc="none", mew=1.5, label="Old")

plt.xlabel("Concentration (uM)", fontsize=16)
plt.ylabel("Pressure (db)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Profile Comparison', fontsize=18)

plt.legend()

plt.gca().invert_yaxis()

fig = mpl.pyplot.gcf()
fig.set_size_inches(5, 8)

plt.tight_layout()

plt.savefig('profile_comparison.svg', format='svg')


# ### 3.5.2 T-Test Comparison of means

# In[33]:


results_dict = {}
depths_to_test = [5, 40, 800, 1000]
for depth in depths_to_test:
    instrument_a_depth_subset = instrument_new_a_df.loc[instrument_new_a_df['Pressure'] == depth]
    instrument_old_depth_subset = instrument_old_df.loc[instrument_old_df['Pressure'] == depth]
    result = sci_st.ttest_ind(instrument_a_depth_subset['O2µmol/L'], instrument_old_depth_subset['O2µmol/L'])
    results_dict[depth] = result[1]

print("For the tested depths, the t-test p-value is shown")
for key in results_dict:
    print(f'At depth: {key} the p-value is: {results_dict[key]}')


# ---

# ## 3.6 Repeated Deep Sample Measurements: 2

# In[34]:


deep_reps_two_df = pd.read_csv(DEP_2_DEEP_REPLICATES_DATA)


# In[35]:


deep_reps_two_df.head()


# ### 3.6.1 Deployment 2 Replicates Boxplot

# In[36]:


sns.boxplot(deep_reps_two_df['Instrument'], deep_reps_two_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('D2 Replicate Samples', fontsize=18)

plt.tight_layout()

# Comment or include next two lines if wanting to scale chart for all
#data_mean = deep_reps_two_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('replicate_deep_samples_2.svg', format='svg')


# ### 3.6.2 Descriptive Statistics

# In[37]:


deep_reps_two_df.groupby(['Instrument'])['O2µmol/L'].median()


# ### 3.6.3 T-Test Comparison of Means

# In[38]:


# Subset by instrument into new dataframes just for simplicity in next cells
deep_reps_two_newa = deep_reps_two_df.loc[deep_reps_two_df['Instrument'] == 'New A']
deep_reps_two_newb = deep_reps_two_df.loc[deep_reps_two_df['Instrument'] == 'New B']
deep_reps_two_old = deep_reps_two_df.loc[deep_reps_two_df['Instrument'] == 'Old']


# #### Compare New A to the Old instrument

# In[39]:


result = sci_st.ttest_ind(deep_reps_two_newa['O2µmol/L'], deep_reps_two_old['O2µmol/L'])
print(f'Comparison of the New A instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance!')


# #### Compare New B to Old instrument

# In[40]:


result = sci_st.ttest_ind(deep_reps_two_newb['O2µmol/L'], deep_reps_two_old['O2µmol/L'])
print(f'Comparison of the New B instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance!')


# #### Compare New A to New B

# In[48]:


result = sci_st.ttest_ind(deep_reps_two_newa['O2µmol/L'], deep_reps_two_newb['O2µmol/L'])
print(f'Comparison of the New A instrument to New B, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance!')


# ---

# ## 3.7 Experimental Meta Analysis

# In[41]:


combined_df = pd.read_csv(COMBINED_DATA)


# In[42]:


combined_df.head()


# ### 3.7.1 Calculation of Mean Standard Deviation

# In[43]:


# Take out the profile experiment as it will skew the data, unless pressure is included as an additional "groupby"
excl_profile = combined_df.loc[combined_df['Experiment'] != "Profile_Comp"]
# Group by Instrument then Experiment type then show descriptive stats 
excl_profile.groupby(['Instrument', 'Experiment'])['O2µmol/L'].describe()


# In[44]:


# Get final standard deviation 
excl_profile.groupby(['Instrument', 'Experiment'])['O2µmol/L'].std().groupby(['Instrument']).mean()


# ### 3.7.2 F-Test for Difference in Variances

# In[45]:


# Take out the profile experiment as it will skew the data, unless pressure is included as an additional "groupby"
excl_profile = combined_df.loc[combined_df['Experiment'] != "Profile_Comp"]
excl_atmosB = excl_profile.loc[excl_profile['Experiment'] != "Atmos_NewB"]

# Group by Instrument then Experiment type then show descriptive stats 
grouped_st_devs = excl_atmosB.groupby(['Instrument', 'Experiment'])['O2µmol/L'].std()


# In[46]:


grouped_st_devs


# In[47]:


sci_st.f_oneway(grouped_st_devs['New A'].values, grouped_st_devs['New B'].values, grouped_st_devs['Old'].values)


# In[ ]:




