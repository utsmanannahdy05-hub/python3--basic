import requests
print("masukan nama kota:")
tanggal = input()
kota = input = ()
url ="https://api.aladhan.com/v1/timingsByCity/28-08-2025?city=Jakarta&country=Indonesia&method=5"
response = requests.get(url)   # HTTP GET
data_json = response.json()    # KONVERSI KE JSON 
print(data_json['data']['timings'])

jadwal_shalat = data_json['data']['timings']
tgl_hijri = data_json['data']['date']['hijri']['date']
print(f"tgl hijriah: {tgl_hijri}")
print("jadwal shalat:")
print(f"-> magrib: {jadwal_shalat['fajr']}")
print(f"-> magrib: {jadwal_shalat['Maghrib']}")