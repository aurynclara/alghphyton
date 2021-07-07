#input tanggal
import datetime

x = datetime.datetime.now()

#input gajipokok
GPokok = [0,2500000,4500000, 6500000]
TIstri = [0,0.01, 0.03, 0.05]

Nama = input("Masukkan Nama = ")
Golongan = input("Masukkan Golongan = ")
JenisKelamin = input("Masukkan Jenis Kelamin (Lakilaki/Perempuan) = ")
StatusKawin = input("Masukkan Status Kawin (Kawin/Belum) = ")

Gol = int(Golongan,0)

TunjanganIstri = 0
TunjanganAnak = 0

GaPok = GPokok[Gol]
TunIstri = TIstri[Gol]

#Cek tunjangan istri
if StatusKawin =="Kawin" and JenisKelamin=="Lakilaki":
    TunjanganIstri = GaPok*TunIstri

#cek tunjangan anak
if StatusKawin =="Kawin": 
    TunjanganAnak = 0.02*GaPok

#cek Gaji bruto
GajiBruto = GaPok + TunjanganAnak + TunjanganIstri

#cek biaya jabatan
BiayaJabatan = 0.5/100*GajiBruto

#cek iuran pensiun
IuranPensiun = 15500

#cek iuran organisasi
IuranOrg = 3500

#hitung gaji neto
GajiNeto = GajiBruto + BiayaJabatan + IuranPensiun + IuranOrg

print("             SLIP GAJI             ")
print("     Tanggal  : " + x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y"))
print("Nama             : " + Nama)
print("Golongan         : " + Golongan)
print("Jenis Kelamin    : " + JenisKelamin)
print("Status Kawin     : " + StatusKawin)
print("Gaji Pokok       : " + f"{GaPok:,d}")
print("Tunjangan Istri  : " + f"{int(TunjanganIstri):,d}")
print("Tunjangan Anak   : " + f"{int(TunjanganAnak):,d}")
print(">> Gaji Bruto    : " + f"{int(GajiBruto):,d}")
print("====================================")
print("Biaya Jabatan    : " + f"{int(BiayaJabatan):,d}")
print("Iuran Pensiun    : " + f"{int(IuranPensiun):,d}")
print("Iuran Organisasi : " + f"{int(IuranOrg):,d}")
print(">> Gaji Neto     : " + f"{int(GajiNeto):,d}")