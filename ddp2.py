ket  = '''
selamat datang diaplikasi perhitungan
silahkan pilih menu yang akan anda jalankan
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
'''
Choice = input(ket)

match Choice:
    case "1":
        print("kamu memilih 2 untuk menghitung luas persegi")
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas_keseluruhan_persegi = sisi * sisi

        print("Luas persegi:", luas_keseluruhan_persegi)
    case "2":
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari = float(input("Masukkan jari-jari lingkaran: "))
        luas =3.14*jari*jari

        print("Luas lingkaran:", luas)
    case "3":
        print("kamu memilih 2 untuk menghitung luas segitiga")
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas_segitiga = 0.5 * alas * tinggi

        print("Luas segitiga:", luas_segitiga)
    case _:
        print("salah pilih")