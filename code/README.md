
# This notebook contains the code for plotting the Dissolved Oxygen Commissioning plots

### Two new dissolved oxygen instruments were purchased from Scripps - these new instruments were subsequently taken on in2020_e01 for commissioning. The data below was collected on the voyage where all 3 instruments (2 new, 1 old) were setup in the same laboratory space and operated in parallel.

#### Imports and style sets:


```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import seawater as sw

sns.set(style="whitegrid") # I like this
mpl.rc('font', family='serif') # Cast Segoe UI font onto all plot text
mpl.rc('figure', figsize=[8, 5]) # Set fig size to something more fitting for A4 word doc
```

---

## 1.1 Independent Iodate Standards


```python
iodate_df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\independent_iodate.csv")
```


```python
iodate_df.head()
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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/independent_iodate_standards.svg)


---

## 1.2 Repeated Deep Sample Measurements: 1

### 1.2.1 Samples from One Niskin per Instrument


```python
deep_reps_single_df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\dep_1_deep_replicates_single_niskins.csv")
```


```python
deep_reps_single_df.head()
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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/replicate_deep_samples_1_single.svg)


### 1.2.2 Samples from Two Niskins for all Instruments


```python
deep_reps_shared_df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\dep_1_deep_replicates_shared_niskins.csv")
```


```python
deep_reps_shared_df.head()
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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/replicate_deep_samples_1_shared.svg)


---

## 1.3 Atmospheric Sample: All Instruments


```python
atmospheric_all_df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\atmospheric_diff_instruments.csv")
```


```python
atmospheric_all_df.head()
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



### Plot just initial box plot scaled to the measurements


```python
sns.boxplot(atmospheric_all_df['Instrument'], atmospheric_all_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Sample', fontsize=18)

plt.tight_layout()

# Comment or include next two lines if wanting to scale chart for all
#data_mean = atmospheric_all_df['O2µmol/L'].mean()
#plt.ylim(data_mean-2, data_mean+2)

plt.savefig('atmospheric_diff_instruments.svg', format='svg')
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/atmospheric_diff_instruments.svg)


### Plot with lines to indicate various QC limits


```python
sns.boxplot(atmospheric_all_df['Instrument'], atmospheric_all_df['O2µmol/L'])

plt.xlabel("Instrument", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Sample w/QC Bars', fontsize=18)

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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/atmospheric_diff_instruments_with_bars.svg)


---

## 1.4 Atmospheric Sample: One Instrument


```python
atmospheric_one_df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\atmospheric_one_instrument.csv")
```


```python
atmospheric_one_df.head()
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




```python
sns.lineplot(atmospheric_one_df.index, atmospheric_one_df['O2µmol/L'], lw=0, marker="o", ms=10)

plt.xlabel("Sample", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Sample: Instrument New B', fontsize=18)

plt.tight_layout()

plt.savefig('atmospheric_one_instrument.svg', format='svg')
```


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/atmospheric_one_instrument.svg)



```python
sns.lineplot(atmospheric_one_df.index, atmospheric_one_df['O2µmol/L'], lw=0, marker="o", ms=10)

plt.xlabel("Sample", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Sample: Instrument New B', fontsize=18)

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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/atmospheric_one_instrument_with_bars.svg)



```python
sns.boxplot(atmospheric_one_df['Instrument'], atmospheric_one_df['O2µmol/L'])

plt.xlabel("Sample", fontsize=16)
plt.ylabel("Concentration (uM)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=12)
plt.title('Atmospheric Sample: Instrument New B', fontsize=18)

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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/atmospheric_one_instrument_with_bars-boxplot-version.svg)


---

## 1.5 Water Profile Comparison


```python
profile_comparison_df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\profile_comparison.csv")
```


```python
profile_comparison_df.head()
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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/profile_comparison.svg)


### More to add here on the probability testing

---

## 1.6 Repeated Deep Sample Measurements: 2


```python
deep_reps_two_df = pd.read_csv(r"C:\Users\she384\Documents\DO Commissioning\repo\data\dep_2_deep_replicates.csv")
```


```python
deep_reps_two_df.head()
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


![png](https://raw.githubusercontent.com/kendall-s/do_commissioning/6de482a4f40a3fffaad9e3d86eb9547ffdda24c1/plots/replicate_deep_samples_2.svg)



```python

```
