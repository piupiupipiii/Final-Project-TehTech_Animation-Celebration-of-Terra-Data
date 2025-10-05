import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

# Read CSV
file_path = r"C:\Users\ASUS\Downloads\fire_archive_M-C61_669496.csv"
df = pd.read_csv(file_path)

# Plotting Map
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.set_extent([90, 145, -11, 6])  # Fokus ke Indonesia

# Plot hotspot points
plt.scatter(df['longitude'], df['latitude'], s=5, c='red', alpha=0.6, transform=ccrs.PlateCarree(), label='Hotspot')

plt.title('Distribution of MODIS Hotspots in Indonesia')
plt.legend()
plt.show()

