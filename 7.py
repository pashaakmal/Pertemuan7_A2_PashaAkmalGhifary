teks_awal = input()
faktor_pengganda = int(input())

teks_hasil = ""

for karakter in teks_awal:
    teks_hasil += karakter * faktor_pengganda

print(teks_hasil)
