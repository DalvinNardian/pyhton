print("Pilih Bangun")
print("1. Bangun Datar")
print("2. Bangun Ruang")

A = int(input("Pilih Bangunan : "))
if A == 1:
    print("Bangun Datar")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Trapesium")
    print("6. Belah Ketupat")

    datar = int(input("Silahkan pilih nomor (1/2/3) :"))
    if datar == 1:
        sisi = int(input("Masukan sisi :"))

        Luas = sisi * sisi
        Keliling = 4*sisi

        print("Sisi Persegi :", sisi)
        print("Luas Persegi :", Luas)
        print("Keliling Persegi :", Keliling)
    elif datar == 2:
        P = int(input("Masukan Panjang :"))
        L = int(input("Masukan Lebar :"))

        Luas = P * L
        Keliling = (2 * P) + (2 * L)

        print("Panjang : ", P, "Lebar : ", L)
        print("Luas Persegi Panjang :", Luas)
        print("Keliling Persegi Panjang :", Keliling)
    elif datar == 3:
        print("1. Mencari Luas")
        print("2. Mencari Keliling")
        Cari = int(input("Pilih Nomor (1/2)"))
        if Cari == 1:
            Alas = int(input("Masukan Alas :"))
            Tinggi = int(input("Masukkan Tinggi :"))
            Luas = (Alas * Tinggi) / 2

            print("Alas :", Alas, "Tinggi :", Tinggi)
            print("Luas Segitiga :", Luas)
        else:
            A = int(input("Masukan sisi A :"))
            B = int(input("Masukan sisi B :"))
            C = int(input("Masukan sisi C :"))
            Keliling = A + B + C
            print("Sisi A :", A, "Sisi B :", B, "Sisi C :", C)
            print("Keliling Segitiga :", Keliling)
    else:
        print("1. Mencari Luas")
        print("2. Mencari Keliling")
        Cari = int(input("Pilih Nomor (1/2)"))
        if Cari == 1:
            Alas = int(input("Masukkan Alas :"))
            Tinggi = int(input("Masukkan Tinggi:"))

            Luas = Alas * Tinggi
            print("Alas :", Alas, "Tinggi :", Tinggi)
            print("Luas Jajar Genjang :",  Luas)
        else:
            A = int(input("Masukkan Sisi A:"))
            B = int(input("Masukkan Sisi B:"))
            C = int(input("Masukkan Sisi C:"))
            D = int(input("Masukkan Sisi D:"))

            Keliling = A + B + C + D
            print("Sisi A :", A, "Sisi B :", B, "Sisi C :", C, "Sisi D :", D)
            print("Keliling Jajar Genjang :", Keliling)
else:
    print("=" * 4, "Bangun Ruang", "=" * 4)
    print("1. Kubus")
    print("2. Balok")
    print("3. Bola")

    print("=" * 25)
    A = int(input("Pilih Bangun Ruang : "))
    if A == 1:
        Rusuk = int(input("Masukan Rusuk : "))

        Luas = 6 * Rusuk**2
        Volume = Rusuk**3
        print("Rusuk : ", Rusuk)
        print("Luas Kubus : ", Luas)
        print("Volume : ", Volume)
    elif A == 2:
        p = int(input("Masukan Panjang : "))
        l = int(input("Masukan Lebar : "))
        t = int(input("Masukan Tinggi : "))

        Luas = (2*p*l) + (2*p*t) + (2*l*t)
        Volume = p * l * t

        print("Panjang Balok : ", p)
        print("Lebar Balok : ", l)
        print("Tinggi Balok : ", t)
        print("Luas Balok : ", Luas)
        print("Volume Balok : ", Volume)
    else:
        phi = 3.14
        R = int(input("Masukan jari - jari : "))

        Luas = 4 * phi * R**2
        Volume = 4/3 * phi * R**3

        print("Jari - jari Bola : ")
        print("Luas Bola : ", Luas)
        print("Volume Bola : ", Volume)
