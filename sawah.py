panjangLahan = float(input("Masukkan panjang lahan: "))
lebarLahan = float(input("Masukkan lebar lahan: "))
pupukBiasanya = int(input("Masukkan jumlah pupuk biasanya: "))

luasLahan = panjangLahan * lebarLahan
jumlahBibit = (panjangLahan / 0.2) * (lebarLahan / 0.2)
kebutuhanPupuk = luasLahan * 400
if pupukBiasanya >= kebutuhanPupuk:
  print("Jumlah pupuk sudah mencukupi")
else:
  tambahanPupuk = kebutuhanPupuk - pupukBiasanya
print("Luas lahan adalah ", luasLahan, "meter persegi")
print("Jumlah bibit yang dibutuhkan adalah ", jumlahBibit)
print("Pupuk yang dibutuhkan dalam sekali pemupukan adalah ", kebutuhanPupuk, "gram")
print("pupuk yang dibutuhkan sampai panen adalah ", kebutuhanPupuk * 4)

#ini komentar
