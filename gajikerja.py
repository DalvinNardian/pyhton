JK = float(input("Masukan Jml Jam Kerja : "))
JL = float(input("Masukan Jml Jam Lembur : "))
TH = float(input("Masukan Jml Tidak Hadir : "))

TJK = JK * 15000
TJL = JL * 10000
TTH = TH * 100000
uangmakan = JK * 10000 / 8
totalgaji = TJK + TJL - TTH

if totalgaji <= 0:
    print("tidak ada gaji")
else:
    print("gaji anda : ", totalgaji)

print("uang makan : ", uangmakan)
