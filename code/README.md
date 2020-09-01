
# This notebook contains the code for plotting the Dissolved Oxygen Commissioning plots

### Two new dissolved oxygen instruments were purchased from Scripps - these new instruments were subsequently taken on in2020_e01 for commissioning. The data below was collected on the voyage where all 3 instruments (2 new, 1 old) were setup in the same laboratory space and operated in parallel.

#### Imports and style sets:


```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import seawater as sw
import scipy.stats as sci_st

sns.set(style="whitegrid") # I like this
mpl.rc('font', family='serif') # Cast Segoe UI font onto all plot text
mpl.rc('figure', figsize=[8, 5]) # Set fig size to something more fitting for A4 word doc
```

### Variables for locations of datafiles (in same order as headings)


```python
INDEPENDENT_IODATE_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/independent_iodate.csv'
DEP_1_DEEP_REPLICATES_SINGLE_NISKINS_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/dep_1_deep_replicates_single_niskins.csv'
DEP_1_DEEP_REPLICATES_SHARED_NISKINS_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/dep_1_deep_replicates_shared_niskins.csv'
ATMOSPHERIC_DIFF_INSTRUMENTS_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/atmospheric_diff_instruments.csv'
ATMOSPHERIC_ONE_INSTRUMENT_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/atmospheric_one_instrument.csv'
PROFILE_COMPARISON_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/profile_comparison.csv'
DEP_2_DEEP_REPLICATES_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/dep_2_deep_replicates.csv'

COMBINED_DATA = 'https://raw.githubusercontent.com/kendall-s/do_commissioning/master/data/combined.csv'
```

---

## 3.1 Independent Iodate Standards 


```python
iodate_df = pd.read_csv(INDEPENDENT_IODATE_DATA)
```


```python
iodate_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51524</td>
      <td>0.51529</td>
      <td>4.964</td>
      <td>19.46</td>
      <td>20</td>
      <td>2.450</td>
      <td>155700</td>
      <td>221.5632</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51495</td>
      <td>0.51496</td>
      <td>4.960</td>
      <td>19.86</td>
      <td>20</td>
      <td>2.412</td>
      <td>160520</td>
      <td>221.4292</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51513</td>
      <td>0.51514</td>
      <td>4.962</td>
      <td>19.86</td>
      <td>20</td>
      <td>2.427</td>
      <td>161045</td>
      <td>221.5186</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51485</td>
      <td>0.51486</td>
      <td>4.959</td>
      <td>19.91</td>
      <td>20</td>
      <td>2.424</td>
      <td>161648</td>
      <td>221.3846</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New B</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.61870</td>
      <td>0.61877</td>
      <td>4.960</td>
      <td>19.40</td>
      <td>20</td>
      <td>2.358</td>
      <td>160025</td>
      <td>221.5632</td>
    </tr>
  </tbody>
</table>
</div>



### 3.1.1 Iodate Standards across Instruments Boxplot


```python
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
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/independent_iodate_standards.svg)


### 3.1.2 Iodate Standards Descriptive Statistics


```python
iodate_df.groupby(['Instrument'])['O2µmol/L'].describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Instrument</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>New A</th>
      <td>4.0</td>
      <td>221.47390</td>
      <td>0.081538</td>
      <td>221.3846</td>
      <td>221.418050</td>
      <td>221.47390</td>
      <td>221.529750</td>
      <td>221.5632</td>
    </tr>
    <tr>
      <th>New B</th>
      <td>4.0</td>
      <td>221.68605</td>
      <td>0.336945</td>
      <td>221.4739</td>
      <td>221.507425</td>
      <td>221.54090</td>
      <td>221.719525</td>
      <td>222.1885</td>
    </tr>
    <tr>
      <th>Old</th>
      <td>4.0</td>
      <td>221.61905</td>
      <td>0.099029</td>
      <td>221.5186</td>
      <td>221.552050</td>
      <td>221.60785</td>
      <td>221.674850</td>
      <td>221.7419</td>
    </tr>
  </tbody>
</table>
</div>



---

## 3.2 Repeated Deep Sample Measurements: 1

### 3.2.1 Samples from One Niskin per Instrument


```python
deep_reps_single_df = pd.read_csv(DEP_1_DEEP_REPLICATES_SINGLE_NISKINS_DATA)
```


```python
deep_reps_single_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
      <th>RP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New A</td>
      <td>143</td>
      <td>145.25</td>
      <td>0.44525</td>
      <td>0.44526</td>
      <td>4.195</td>
      <td>19.88</td>
      <td>6.7</td>
      <td>2.423</td>
      <td>162322</td>
      <td>187.3082</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New A</td>
      <td>144</td>
      <td>146.25</td>
      <td>0.44776</td>
      <td>0.44777</td>
      <td>4.190</td>
      <td>19.84</td>
      <td>6.9</td>
      <td>2.471</td>
      <td>162637</td>
      <td>187.0403</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New A</td>
      <td>148</td>
      <td>143.04</td>
      <td>0.43883</td>
      <td>0.43884</td>
      <td>4.199</td>
      <td>19.90</td>
      <td>7.1</td>
      <td>2.405</td>
      <td>163229</td>
      <td>187.4869</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New A</td>
      <td>150</td>
      <td>140.86</td>
      <td>0.43107</td>
      <td>0.43108</td>
      <td>4.189</td>
      <td>19.84</td>
      <td>7.2</td>
      <td>2.389</td>
      <td>163558</td>
      <td>187.0403</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New A</td>
      <td>152</td>
      <td>145.03</td>
      <td>0.44393</td>
      <td>0.44395</td>
      <td>4.189</td>
      <td>19.82</td>
      <td>7.4</td>
      <td>2.393</td>
      <td>163904</td>
      <td>187.0403</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



#### 3.2.1.1 Samples from One Niskin Boxplot


```python
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
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/replicate_deep_samples_1_single.svg)


#### 3.2.1.2 Descriptive Statistics


```python
deep_reps_single_df.groupby(['Instrument'])['O2µmol/L'].describe()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Instrument</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>New A</th>
      <td>6.0</td>
      <td>187.196600</td>
      <td>0.186819</td>
      <td>187.0403</td>
      <td>187.040300</td>
      <td>187.15195</td>
      <td>187.297050</td>
      <td>187.4869</td>
    </tr>
    <tr>
      <th>New B</th>
      <td>6.0</td>
      <td>187.218917</td>
      <td>0.252660</td>
      <td>186.7276</td>
      <td>187.207775</td>
      <td>187.33055</td>
      <td>187.352900</td>
      <td>187.3976</td>
    </tr>
    <tr>
      <th>Old</th>
      <td>6.0</td>
      <td>187.181700</td>
      <td>0.099515</td>
      <td>187.0403</td>
      <td>187.129600</td>
      <td>187.17425</td>
      <td>187.252425</td>
      <td>187.3082</td>
    </tr>
  </tbody>
</table>
</div>



#### 3.2.1.3 T-Test Comparison of Means


```python
deep_reps_single_newa = deep_reps_single_df.loc[deep_reps_single_df['Instrument'] == 'New A']
deep_reps_single_newb = deep_reps_single_df.loc[deep_reps_single_df['Instrument'] == 'New B']
deep_reps_single_old = deep_reps_single_df.loc[deep_reps_single_df['Instrument'] == 'Old']
```

##### Compare New A to Old instrument


```python
result = sci_st.ttest_ind(deep_reps_single_newa['O2µmol/L'], deep_reps_single_old['O2µmol/L'])
print(f'Comparison of the New A instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance !')
```

    Comparison of the New A instrument to Old, p-value: 0.8665430859682957
    

##### Compare New B to Old instrument


```python
result = sci_st.ttest_ind(deep_reps_single_newb['O2µmol/L'], deep_reps_single_old['O2µmol/L'])
print(f'Comparison of the New B instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance !')
```

    Comparison of the New B instrument to Old, p-value: 0.7440286422028863
    

### 3.2.2 Samples from Two Niskins for all Instruments


```python
deep_reps_shared_df = pd.read_csv(DEP_1_DEEP_REPLICATES_SHARED_NISKINS_DATA)
```


```python
deep_reps_shared_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
      <th>RP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New A</td>
      <td>161</td>
      <td>144.68</td>
      <td>0.44360</td>
      <td>0.44343</td>
      <td>4.195</td>
      <td>21.84</td>
      <td>7.0</td>
      <td>2.074</td>
      <td>232544</td>
      <td>187.2636</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New A</td>
      <td>167</td>
      <td>144.39</td>
      <td>0.44349</td>
      <td>0.44331</td>
      <td>4.202</td>
      <td>21.88</td>
      <td>7.4</td>
      <td>2.132</td>
      <td>232834</td>
      <td>187.6209</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New A</td>
      <td>211</td>
      <td>144.58</td>
      <td>0.44272</td>
      <td>0.44254</td>
      <td>4.189</td>
      <td>21.95</td>
      <td>7.2</td>
      <td>2.137</td>
      <td>233205</td>
      <td>187.0403</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New A</td>
      <td>217</td>
      <td>141.62</td>
      <td>0.43344</td>
      <td>0.43327</td>
      <td>4.188</td>
      <td>21.94</td>
      <td>7.7</td>
      <td>2.083</td>
      <td>233501</td>
      <td>186.9956</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New B</td>
      <td>162</td>
      <td>145.50</td>
      <td>0.53636</td>
      <td>0.53638</td>
      <td>4.199</td>
      <td>19.81</td>
      <td>7.2</td>
      <td>2.270</td>
      <td>233544</td>
      <td>187.5762</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



#### 3.2.2.1 Samples from Shared Niskins Boxplot


```python
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
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/replicate_deep_samples_1_shared.svg)


#### 3.2.2.2 Descriptive Statistics


```python
deep_reps_shared_df.groupby(['Instrument'])['O2µmol/L'].describe()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Instrument</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>New A</th>
      <td>4.0</td>
      <td>187.230100</td>
      <td>0.285693</td>
      <td>186.9956</td>
      <td>187.029125</td>
      <td>187.15195</td>
      <td>187.352925</td>
      <td>187.6209</td>
    </tr>
    <tr>
      <th>New B</th>
      <td>4.0</td>
      <td>187.587350</td>
      <td>0.400103</td>
      <td>187.3082</td>
      <td>187.308200</td>
      <td>187.44220</td>
      <td>187.721350</td>
      <td>188.1568</td>
    </tr>
    <tr>
      <th>Old</th>
      <td>4.0</td>
      <td>187.565025</td>
      <td>0.511021</td>
      <td>187.1296</td>
      <td>187.263550</td>
      <td>187.41985</td>
      <td>187.721325</td>
      <td>188.2908</td>
    </tr>
  </tbody>
</table>
</div>



---

## 3.3 Atmospheric Saturated Sample: All Instruments


```python
atmospheric_all_df = pd.read_csv(ATMOSPHERIC_DIFF_INSTRUMENTS_DATA)
```


```python
atmospheric_all_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New A</td>
      <td>257</td>
      <td>138.61</td>
      <td>0.62271</td>
      <td>0.62247</td>
      <td>6.157</td>
      <td>21.86</td>
      <td>21.5</td>
      <td>2.030</td>
      <td>2101</td>
      <td>274.8438</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New A</td>
      <td>260</td>
      <td>140.86</td>
      <td>0.63292</td>
      <td>0.63285</td>
      <td>6.158</td>
      <td>20.50</td>
      <td>21.5</td>
      <td>2.009</td>
      <td>2318</td>
      <td>274.9331</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New A</td>
      <td>263</td>
      <td>137.65</td>
      <td>0.61726</td>
      <td>0.61720</td>
      <td>6.148</td>
      <td>20.49</td>
      <td>21.5</td>
      <td>2.053</td>
      <td>2617</td>
      <td>274.4418</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New A</td>
      <td>266</td>
      <td>142.77</td>
      <td>0.64096</td>
      <td>0.64089</td>
      <td>6.152</td>
      <td>20.48</td>
      <td>21.5</td>
      <td>2.017</td>
      <td>2934</td>
      <td>274.6205</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New B</td>
      <td>258</td>
      <td>138.45</td>
      <td>0.74709</td>
      <td>0.74689</td>
      <td>6.154</td>
      <td>21.31</td>
      <td>21.5</td>
      <td>2.232</td>
      <td>2951</td>
      <td>274.8885</td>
    </tr>
  </tbody>
</table>
</div>



### 3.3.1 Atmospheric Saturated Sample Boxplot (auto-scale)

#### Plot just initial box plot scaled to the measurements


```python
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
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/atmospheric_diff_instruments.svg)


### 3.3.2 Atmospheric Saturated Sample Boxplot (QC Control Lines)

#### Plot with lines to indicate various QC limits


```python
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
```


![png](output_45_0.png)


---

## 3.4 Atmospheric Saturated Sample: One Instrument


```python
atmospheric_one_df = pd.read_csv(ATMOSPHERIC_ONE_INSTRUMENT_DATA)
```


```python
atmospheric_one_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New B</td>
      <td>210</td>
      <td>143.84</td>
      <td>0.78354</td>
      <td>0.78332</td>
      <td>6.208</td>
      <td>21.38</td>
      <td>21.5</td>
      <td>2.320</td>
      <td>145535</td>
      <td>277.3895</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New B</td>
      <td>211</td>
      <td>144.58</td>
      <td>0.78712</td>
      <td>0.78686</td>
      <td>6.204</td>
      <td>21.60</td>
      <td>21.5</td>
      <td>2.327</td>
      <td>145744</td>
      <td>277.2108</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New B</td>
      <td>214</td>
      <td>146.67</td>
      <td>0.79938</td>
      <td>0.79910</td>
      <td>6.210</td>
      <td>21.70</td>
      <td>21.5</td>
      <td>2.344</td>
      <td>150012</td>
      <td>277.4788</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New B</td>
      <td>216</td>
      <td>144.35</td>
      <td>0.78570</td>
      <td>0.78541</td>
      <td>6.203</td>
      <td>21.77</td>
      <td>21.5</td>
      <td>2.306</td>
      <td>150236</td>
      <td>277.1662</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New B</td>
      <td>217</td>
      <td>141.62</td>
      <td>0.77087</td>
      <td>0.77058</td>
      <td>6.204</td>
      <td>21.83</td>
      <td>21.5</td>
      <td>2.287</td>
      <td>150440</td>
      <td>277.2108</td>
    </tr>
  </tbody>
</table>
</div>



### 3.4.1 Atmospheric Saturated Sample: Instrument New B (auto-scale)


```python
sns.lineplot(atmospheric_one_df.index, atmospheric_one_df['O2µmol/L'], lw=0, marker="o", ms=10)

plt.xlabel("Sample", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Saturated Sample: Instrument New B', fontsize=18)

plt.tight_layout()

plt.savefig('atmospheric_one_instrument.svg', format='svg')
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/atmospheric_one_instrument.svg)


### 3.4.2 Atmospheric Saturated Sample: Instrument New B (QC Control Limits)


```python
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
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/atmospheric_one_instrument_with_bars.svg)


### 3.4.3 Atmospheric Saturated Sample: Instrument New B Boxplot (QC Control Limits)


```python
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
```


![png](output_55_0.png)


---

## 3.5 Water Profile Comparison


```python
profile_comparison_df = pd.read_csv(PROFILE_COMPARISON_DATA)
```


```python
profile_comparison_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
      <th>RP</th>
      <th>Pressure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New A</td>
      <td>278</td>
      <td>142.48</td>
      <td>0.59621</td>
      <td>0.59623</td>
      <td>5.734</td>
      <td>19.83</td>
      <td>14.0</td>
      <td>2.282</td>
      <td>201954</td>
      <td>255.9969</td>
      <td>24</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New A</td>
      <td>276</td>
      <td>140.04</td>
      <td>0.58568</td>
      <td>0.58551</td>
      <td>5.730</td>
      <td>21.38</td>
      <td>14.1</td>
      <td>2.276</td>
      <td>202345</td>
      <td>255.8182</td>
      <td>23</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New A</td>
      <td>627</td>
      <td>145.60</td>
      <td>0.60911</td>
      <td>0.60893</td>
      <td>5.729</td>
      <td>21.45</td>
      <td>14.1</td>
      <td>2.299</td>
      <td>202606</td>
      <td>255.7735</td>
      <td>22</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New A</td>
      <td>625</td>
      <td>143.75</td>
      <td>0.60031</td>
      <td>0.60012</td>
      <td>5.720</td>
      <td>21.51</td>
      <td>13.9</td>
      <td>2.292</td>
      <td>203001</td>
      <td>255.3716</td>
      <td>21</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New A</td>
      <td>623</td>
      <td>140.11</td>
      <td>0.58475</td>
      <td>0.58456</td>
      <td>5.718</td>
      <td>21.53</td>
      <td>13.9</td>
      <td>2.258</td>
      <td>205345</td>
      <td>255.2823</td>
      <td>20</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>



### 3.5.1 Water Profile Plot


```python
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
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/profile_comparison.svg)


### 3.5.2 T-Test Comparison of means


```python
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
```

    For the tested depths, the t-test p-value is shown
    At depth: 5 the p-value is: 0.10839798708992938
    At depth: 40 the p-value is: 0.3026985172966608
    At depth: 800 the p-value is: 0.9008494336784751
    At depth: 1000 the p-value is: 0.8665430859682957
    

---

## 3.6 Repeated Deep Sample Measurements: 2


```python
deep_reps_two_df = pd.read_csv(DEP_2_DEEP_REPLICATES_DATA)
```


```python
deep_reps_two_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
      <th>RP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New A</td>
      <td>675</td>
      <td>135.77</td>
      <td>0.41383</td>
      <td>0.41379</td>
      <td>4.174</td>
      <td>20.46</td>
      <td>6.3</td>
      <td>2.085</td>
      <td>5547</td>
      <td>186.3257</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New A</td>
      <td>678</td>
      <td>139.77</td>
      <td>0.42626</td>
      <td>0.42625</td>
      <td>4.175</td>
      <td>20.12</td>
      <td>6.3</td>
      <td>2.443</td>
      <td>5948</td>
      <td>186.4150</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New A</td>
      <td>681</td>
      <td>141.76</td>
      <td>0.43149</td>
      <td>0.43148</td>
      <td>4.166</td>
      <td>20.18</td>
      <td>6.5</td>
      <td>2.452</td>
      <td>10147</td>
      <td>186.0131</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New A</td>
      <td>684</td>
      <td>138.61</td>
      <td>0.42143</td>
      <td>0.42141</td>
      <td>4.163</td>
      <td>20.24</td>
      <td>6.5</td>
      <td>2.407</td>
      <td>10343</td>
      <td>185.8344</td>
      <td>11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New A</td>
      <td>687</td>
      <td>141.65</td>
      <td>0.43127</td>
      <td>0.43125</td>
      <td>4.167</td>
      <td>20.27</td>
      <td>6.5</td>
      <td>2.439</td>
      <td>10624</td>
      <td>186.0577</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>



### 3.6.1 Deployment 2 Replicates Boxplot


```python
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
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/master/plots/replicate_deep_samples_2.svg)


### 3.6.2 T-Test Comparison of Means


```python
# Subset by instrument into new dataframes just for simplicity in next cells
deep_reps_two_newa = deep_reps_two_df.loc[deep_reps_two_df['Instrument'] == 'New A']
deep_reps_two_newb = deep_reps_two_df.loc[deep_reps_two_df['Instrument'] == 'New B']
deep_reps_two_old = deep_reps_two_df.loc[deep_reps_two_df['Instrument'] == 'Old']
```

#### Compare New A to the Old instrument


```python
result = sci_st.ttest_ind(deep_reps_two_newa['O2µmol/L'], deep_reps_two_old['O2µmol/L'])
print(f'Comparison of the New A instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance!')
```

    Comparison of the New A instrument to Old, p-value: 0.039304940051647204
    Significance!
    

#### Compare New B to Old instrument


```python
result = sci_st.ttest_ind(deep_reps_two_newb['O2µmol/L'], deep_reps_two_old['O2µmol/L'])
print(f'Comparison of the New B instrument to Old, p-value: {result[1]}')
if result[1] < 0.05:
    print('Significance!')
```

    Comparison of the New B instrument to Old, p-value: 0.11189671028378533
    

---

## 3.7 Experimental Meta Analysis


```python
combined_df = pd.read_csv(COMBINED_DATA)
```


```python
combined_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Experiment</th>
      <th>Instrument</th>
      <th>Bottle</th>
      <th>FlaskVol</th>
      <th>RawTitre</th>
      <th>Titre20</th>
      <th>O2ml/L</th>
      <th>ThioTemp</th>
      <th>DrawTemp</th>
      <th>EndVolts</th>
      <th>TitreTime</th>
      <th>O2µmol/L</th>
      <th>RP</th>
      <th>Pressure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Iodate</td>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51524</td>
      <td>0.51529</td>
      <td>4.964</td>
      <td>19.46</td>
      <td>20.0</td>
      <td>2.450</td>
      <td>155700</td>
      <td>221.5632</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Iodate</td>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51495</td>
      <td>0.51496</td>
      <td>4.960</td>
      <td>19.86</td>
      <td>20.0</td>
      <td>2.412</td>
      <td>160520</td>
      <td>221.4292</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Iodate</td>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51513</td>
      <td>0.51514</td>
      <td>4.962</td>
      <td>19.86</td>
      <td>20.0</td>
      <td>2.427</td>
      <td>161045</td>
      <td>221.5186</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Iodate</td>
      <td>New A</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.51485</td>
      <td>0.51486</td>
      <td>4.959</td>
      <td>19.91</td>
      <td>20.0</td>
      <td>2.424</td>
      <td>161648</td>
      <td>221.3846</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Iodate</td>
      <td>New B</td>
      <td>200</td>
      <td>142.19</td>
      <td>0.61870</td>
      <td>0.61877</td>
      <td>4.960</td>
      <td>19.40</td>
      <td>20.0</td>
      <td>2.358</td>
      <td>160025</td>
      <td>221.5632</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 3.7.1 Calculation of Mean Standard Deviation


```python
# Take out the profile experiment as it will skew the data, unless pressure is included as an additional "groupby"
excl_profile = combined_df.loc[combined_df['Experiment'] != "Profile_Comp"]
# Group by Instrument then Experiment type then show descriptive stats 
excl_profile.groupby(['Instrument', 'Experiment'])['O2µmol/L'].describe()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Instrument</th>
      <th>Experiment</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">New A</th>
      <th>Atmos_All</th>
      <td>4.0</td>
      <td>274.709800</td>
      <td>0.221824</td>
      <td>274.4418</td>
      <td>274.575825</td>
      <td>274.73215</td>
      <td>274.866125</td>
      <td>274.9331</td>
    </tr>
    <tr>
      <th>Dep1_Reps_Shared</th>
      <td>4.0</td>
      <td>187.230100</td>
      <td>0.285693</td>
      <td>186.9956</td>
      <td>187.029125</td>
      <td>187.15195</td>
      <td>187.352925</td>
      <td>187.6209</td>
    </tr>
    <tr>
      <th>Dep1_Reps_Single</th>
      <td>6.0</td>
      <td>187.196600</td>
      <td>0.186819</td>
      <td>187.0403</td>
      <td>187.040300</td>
      <td>187.15195</td>
      <td>187.297050</td>
      <td>187.4869</td>
    </tr>
    <tr>
      <th>Dep2_Reps</th>
      <td>8.0</td>
      <td>186.024225</td>
      <td>0.245500</td>
      <td>185.7004</td>
      <td>185.834400</td>
      <td>186.01310</td>
      <td>186.124700</td>
      <td>186.4150</td>
    </tr>
    <tr>
      <th>Iodate</th>
      <td>4.0</td>
      <td>221.473900</td>
      <td>0.081538</td>
      <td>221.3846</td>
      <td>221.418050</td>
      <td>221.47390</td>
      <td>221.529750</td>
      <td>221.5632</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">New B</th>
      <th>Atmos_All</th>
      <td>4.0</td>
      <td>274.854975</td>
      <td>0.111670</td>
      <td>274.7098</td>
      <td>274.810300</td>
      <td>274.86615</td>
      <td>274.910825</td>
      <td>274.9778</td>
    </tr>
    <tr>
      <th>Atmos_NewB</th>
      <td>12.0</td>
      <td>277.095450</td>
      <td>0.209874</td>
      <td>276.8089</td>
      <td>276.965175</td>
      <td>277.07680</td>
      <td>277.210800</td>
      <td>277.4788</td>
    </tr>
    <tr>
      <th>Dep1_Reps_Shared</th>
      <td>4.0</td>
      <td>187.587350</td>
      <td>0.400103</td>
      <td>187.3082</td>
      <td>187.308200</td>
      <td>187.44220</td>
      <td>187.721350</td>
      <td>188.1568</td>
    </tr>
    <tr>
      <th>Dep1_Reps_Single</th>
      <td>6.0</td>
      <td>187.218917</td>
      <td>0.252660</td>
      <td>186.7276</td>
      <td>187.207775</td>
      <td>187.33055</td>
      <td>187.352900</td>
      <td>187.3976</td>
    </tr>
    <tr>
      <th>Dep2_Reps</th>
      <td>8.0</td>
      <td>186.180538</td>
      <td>0.136615</td>
      <td>185.8791</td>
      <td>186.147000</td>
      <td>186.21405</td>
      <td>186.247550</td>
      <td>186.3257</td>
    </tr>
    <tr>
      <th>Iodate</th>
      <td>4.0</td>
      <td>221.686050</td>
      <td>0.336945</td>
      <td>221.4739</td>
      <td>221.507425</td>
      <td>221.54090</td>
      <td>221.719525</td>
      <td>222.1885</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Old</th>
      <th>Atmos_All</th>
      <td>4.0</td>
      <td>274.832650</td>
      <td>0.056200</td>
      <td>274.7545</td>
      <td>274.821475</td>
      <td>274.84380</td>
      <td>274.854975</td>
      <td>274.8885</td>
    </tr>
    <tr>
      <th>Dep1_Reps_Shared</th>
      <td>4.0</td>
      <td>187.565025</td>
      <td>0.511021</td>
      <td>187.1296</td>
      <td>187.263550</td>
      <td>187.41985</td>
      <td>187.721325</td>
      <td>188.2908</td>
    </tr>
    <tr>
      <th>Dep1_Reps_Single</th>
      <td>6.0</td>
      <td>187.181700</td>
      <td>0.099515</td>
      <td>187.0403</td>
      <td>187.129600</td>
      <td>187.17425</td>
      <td>187.252425</td>
      <td>187.3082</td>
    </tr>
    <tr>
      <th>Dep2_Reps</th>
      <td>8.0</td>
      <td>186.565750</td>
      <td>0.627521</td>
      <td>186.0577</td>
      <td>186.169375</td>
      <td>186.30335</td>
      <td>186.705325</td>
      <td>187.8442</td>
    </tr>
    <tr>
      <th>Iodate</th>
      <td>4.0</td>
      <td>221.619050</td>
      <td>0.099029</td>
      <td>221.5186</td>
      <td>221.552050</td>
      <td>221.60785</td>
      <td>221.674850</td>
      <td>221.7419</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Get final standard deviation 
excl_profile.groupby(['Instrument', 'Experiment'])['O2µmol/L'].std().groupby(['Instrument']).mean()
```




    Instrument
    New A    0.204275
    New B    0.241311
    Old      0.278657
    Name: O2µmol/L, dtype: float64



### 3.7.2 F-Test for Difference in Variances


```python
# Take out the profile experiment as it will skew the data, unless pressure is included as an additional "groupby"
excl_profile = combined_df.loc[combined_df['Experiment'] != "Profile_Comp"]
excl_atmosB = excl_profile.loc[excl_profile['Experiment'] != "Atmos_NewB"]

# Group by Instrument then Experiment type then show descriptive stats 
grouped_st_devs = excl_atmosB.groupby(['Instrument', 'Experiment'])['O2µmol/L'].std()
```


```python
grouped_st_devs
```




    Instrument  Experiment      
    New A       Atmos_All           0.221824
                Dep1_Reps_Shared    0.285693
                Dep1_Reps_Single    0.186819
                Dep2_Reps           0.245500
                Iodate              0.081538
    New B       Atmos_All           0.111670
                Dep1_Reps_Shared    0.400103
                Dep1_Reps_Single    0.252660
                Dep2_Reps           0.136615
                Iodate              0.336945
    Old         Atmos_All           0.056200
                Dep1_Reps_Shared    0.511021
                Dep1_Reps_Single    0.099515
                Dep2_Reps           0.627521
                Iodate              0.099029
    Name: O2µmol/L, dtype: float64




```python
sci_st.f_oneway(grouped_st_devs['New A'].values, grouped_st_devs['New B'].values, grouped_st_devs['Old'].values)
```




    F_onewayResult(statistic=0.22295493881859532, pvalue=0.8033921150555711)




```python

```
