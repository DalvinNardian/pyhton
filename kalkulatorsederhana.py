print("=" * 25)
print("Operasi Matematika")
print("1. Tambah [+]")
print("2. kurang [-]")
print("3. kali [*]")
print("4. bagi [/]")
print("5. Modulus [%]")
print("=" * 25)

hitung = int(input("Pilih Operasi (1/2/3/4/5)"))
bil1 = int(input("Masukan Bilangan Pertama : "))
bil2 = int(input("Masukan Bilangan kedua : "))

print("=" * 25)
if hitung == 1:
    hasil = bil1 + bil2
    print(f'Hasil operasi dari {bil1} + {bil2} = {hasil}')
elif hitung == 2:
    hasil = bil1 - bil2
    print(f'Hasil operasi dari {bil1} - {bil2} = {hasil}')
elif hitung == 3:
    hasil = bil1 * bil2
    print(f'Hasil operasi dari {bil1} * {bil2} = {hasil}')
elif hitung == 4:
    hasil = bil1 / bil2
    print(f'Hasil operasi dari {bil1} / {bil2} = {hasil}')
elif hitung == 5:
    hasil = bil1 % bil2
    print(f'Hasil operasi dari {bil1} % {bil2} = {hasil}')
else:
    print('Tidak valid')
