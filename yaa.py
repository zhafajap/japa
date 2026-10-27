
def hitung_gaji(gaji_pokok, tunjangan, potongan):
    gaji_bersih = gaji_pokok + tunjangan - potongan
    return gaji_bersih

gaji = float(input("Masukkan gaji pokok: "))
tunjangan = float(input("Masukkan tunjangan: "))
potongan = float(input("Masukkan potongan: "))

hasil = hitung_gaji(gaji, tunjangan, potongan)

print("Gaji bersih: Rp", hasil)