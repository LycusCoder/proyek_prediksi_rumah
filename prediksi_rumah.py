# Script Prediksi Harga Rumah di Indonesia
# Oleh: Nourivex

# 1. Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# 2. Muat Dataset (skip baris bermasalah)
df = pd.read_csv("data/rumah_indonesia.csv", on_bad_lines='skip')

# 2.a Rename kolom agar mudah diakses
df = df.rename(columns={
    "harga (Rp)": "harga",
    "jarak_ke_kota (km)": "jarak_ke_kota"
})

# 2.b Konversi kolom 'harga' dari string ke integer
#     menghapus titik sebagai pemisah ribuan
df["harga"] = (
    df["harga"]
      .str.replace(r"\.", "", regex=True)
      .astype(int)
)

print("5 Baris Pertama Setelah Rename & Convert:")
print(df.head())

# 3. Pra-proses Data
# Tangani missing value (drop baris yang ada NA)
df.dropna(inplace=True)

# Encoding kolom kategorikal 'lokasi'
df = pd.get_dummies(df, columns=['lokasi'], drop_first=True)

# 4. Pemisahan Fitur dan Target
X = df.drop('harga', axis=1)
y = df['harga']

# Split data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Latih Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Evaluasi Model
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\nRMSE: {rmse:.2f} | R²: {r2:.4f}")

# 7. Visualisasi
# Plot 1: Aktual vs Prediksi
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel("Harga Aktual")
plt.ylabel("Harga Prediksi")
plt.title("Aktual vs Prediksi Harga Rumah")
plt.savefig("visualizations/aktual_vs_prediksi.png")
plt.close()

# Plot 2: Residual Analysis
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_pred, y=residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Prediksi")
plt.ylabel("Residual")
plt.title("Residual Plot")
plt.savefig("visualizations/residual_plot.png")
plt.close()

print("\nVisualisasi disimpan di folder 'visualizations/'.")
