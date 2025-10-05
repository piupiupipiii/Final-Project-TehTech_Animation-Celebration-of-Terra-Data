import requests
from datetime import date, timedelta
import os

USERNAME = "silvy.nur"
PASSWORD = "Pipicantik.1234"  # ganti ya
save_dir = r"C:\Users\ASUS\Downloads\NASA_FIRE"
os.makedirs(save_dir, exist_ok=True)

start_date = date(2015, 8, 1)
end_date = date(2015, 9, 30)

while start_date <= end_date:
    doy = start_date.timetuple().tm_yday
    year = start_date.year
    url = f"https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/details?path=archive/allData/61/MOD14A1/{year}/{doy:03d}/"
    
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    
    if response.status_code == 200:
        data = response.json()
        files = data.get("content", [])
        print(f"✅ {start_date} — {len(files)} file ditemukan")

        for f in files:
            if f["name"].endswith(".hdf"):
                file_url = f"https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD14A1/{year}/{doy:03d}/{f['name']}"
                file_path = os.path.join(save_dir, f["name"])

                if not os.path.exists(file_path):
                    print(f"⬇️  Downloading {f['name']} ...")
                    r = requests.get(file_url, auth=(USERNAME, PASSWORD), stream=True)
                    if r.status_code == 200:
                        with open(file_path, "wb") as f_out:
                            for chunk in r.iter_content(8192):
                                f_out.write(chunk)
                        print(f"   ✅ Selesai: {f['name']}")
                    else:
                        print(f"   ❌ Gagal download {f['name']} ({r.status_code})")
                else:
                    print(f"   ⚠️ Sudah ada: {f['name']}")
    else:
        print(f"❌ Tidak bisa akses {start_date} (status {response.status_code})")

    start_date += timedelta(days=8)
