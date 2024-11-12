import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
df = pd.read_csv('weather_data.csv')

# Convert timestamp to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Create the time step plot
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Temperature'], label='Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.show()
