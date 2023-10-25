kendaraan = ["Honda Beat", "Sepeda Motor", "110 cc", "Merah Muda", "2"]
merk_kendaraan = "Honda"
harga_kendaraan = "Rp 15.000.000"
tipe_kendaraan = "Baru"

indeks_kendaraan = kendaraan.index("Sepeda Motor")

kendaraan.insert(indeks_kendaraan + 1, merk_kendaraan)

kendaraan.append(harga_kendaraan)
kendaraan.append(tipe_kendaraan)

print(kendaraan)