import os
data = dict()
nilaiDisiplin = ""
def main():
    os.system('cls')
    print("-------------------- Masukkan Daftar Nilai --------------------\n")
    data["Nama"] = input("Nama \t\t\t= ")
    data["Nisn"] = input("Nisn \t\t\t= ")
    data["MaPel"] = input("Mata Pelajaran \t= ")
    data["nQuis1"] = input("Nilai Quis 1 \t= ")
    data["nQuis2"] = input("Nilai Quis 2 \t= ")
    data["Tugas"] = input("Nilai Tugas \t= ")
    data["UTS"] = input("Nilai UTS \t\t= ")
    data["UAS"] = input("Nilai UAS \t\t= ")

    print("-------------------- Hasil Daftar Nilai --------------------\n")
    print("Nama \t\t\t\t\t= " + data["Nama"])
    print("NISN \t\t\t\t\t= " + data["Nama"])
    print("Mata Pelajaran \t\t\t= " + data["Nama"])

    nqr  = int(data["nQuis1"]) + int(data["nQuis2"]) / 2
    print("Rata-Rata Nilai Quis \t= " + str(nqr))

    print("Nilai UTS \t\t\t\t= " + data["UTS"])
    print("Nilai UAS \t\t\t\t= " + data["UAS"])
    nq  = int(data["nQuis1"]) + int(data["nQuis2"])
    nt  = int(data["Tugas"])
    uts = int(data["UTS"])
    uas = int(data["UAS"])
    na  = (20/100*nq) + (25/100*nt) + (25/100*uts) + (30/100*uas)
    print("Nilai Akhir \t\t\t= " + str(na))

    if na >= 80:
        mutu = "A"
    elif na >= 70 and na < 80:
        mutu = "B"
    elif na >= 60 and na < 70:
        mutu = "C"
    elif na >= 50 and na < 60:
        mutu = "D"
    elif na < 50:
        mutu = "E"

    print("Huruf Mutu \t\t\t\t= " + mutu)


main()
ulang = input("Apakah Ingin Mengulang ? (y/n) ")
if ulang == "y" or input == "Y":
    main()
else:
    print("Selesai")
    exit()
