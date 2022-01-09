#Marhani Wiji Ayu K - 5200411123
ram = int(input("Masukkan Kapasitas RAM(GB) :"))
petabit = int(input("Kapasitas Petabit(GB) :"))
os = int(input("Kapasitas RAM Sistem Operasi(GB) :"))
ramsatu = int(input("Kapasitas RAM(GB) Untuk Program 1 :"))
ramdua = int(input("Kapasitas RAM(GB) Untuk Program 2 :"))

#rumus perhitungan
kapasitaspetab = ram/petabit
totalram = os+ramsatu+ramdua
ramttpakai = ram - totalram
blok1 = ram/petabit
blok0 = ram - kapasitaspetab

print ("=======================================")
print ("Kapasitas RAM                   =",ram)
print ("Kapasitas Petabit               =",petabit)
print ("Kapasitas Perpetabit            =",kapasitaspetab)
print ("Total RAM Terpakai              =",totalram)
print ("Total RAM Tidak Terpakai        =",ramttpakai)
print ("Jumlah Blok Bernilai 1          =",blok1)
print ("Jumlah Blok Bernilai 0          =",blok0)