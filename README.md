# pvutils
Photovoltaic utils

* PVGIS is an [API](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/getting-started-pvgis/api-non-interactive-service_en) wrapper object that retrieves hourly solar radiation and photovoltaic system performance data from [PVGIS](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis_en) (Photovoltaic Geographical Information System). PVGIS provides information for any location in Europe and Africa, as well as a large part of Asia and America.
  - PVGIS.get_radiation_data() returns historical solar radiation data.
  - PVGIS.get_production_timeserie() retrieves the pandas time series object of the estimated PV generation.

### Install
```shell
pip install git+https://github.com/ellariel/pvutils.git
```

### Run
```shell
import pvutils
print(pvutils.PVGIS(local_cache_dir=None, verbose=True).get_production_timeserie())
```
