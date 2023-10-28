# pvutils
Photovoltaic utils

* pvgis.PVGIS is an API wrapper object that retrieves hourly solar radiation and photovoltaic system performance data from [PVGIS](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis_en) (Photovoltaic Geographical Information System). PVGIS provides information for any location in Europe and Africa, as well as a large part of Asia and America.

### Install
```shell
pip install git+https://github.com/ellariel/pvutils.git
```

### Run
```shell
from pvutils.pvgis import PVGIS
print(PVGIS(local_cache_dir=None, verbose=True).get_production_timeserie())
```