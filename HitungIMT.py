# Rumus Hitung IMT : (berat/tinggi**2)

A = float(input("masukan berat badan :"))
B = float(input("masukan tinggi badan :"))
IMT = A / B ** 2

print("IMT = ", IMT)
if IMT <= 16.9:
    print("Kurus")
elif IMT >= 28.5:
    print("Gemuk")
else:
    print("Normal")
