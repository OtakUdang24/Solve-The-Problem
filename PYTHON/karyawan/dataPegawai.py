from prettytable import PrettyTable
import os
import re
from io import StringIO
from operator import itemgetter


# ======================== MENU ========================
# menu = PrettyTable()
# menu.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
# print(menu)

# ======================== VAR =========================
# global data_path
# data_path = "data.txt"
# dataTxt = open("{}".format(data_path), "r")
# ======================== VAR =========================
# ======================== MENU ========================
def menu():
    menu = PrettyTable()
    menu.field_names = ["NO", "Menu"]
    menu.add_row(["1", "Masukkan Data"])
    menu.add_row(["2", "Daftar Karyawan"])
    menu.add_row(["3", "Cari Data"])
    menu.add_row(["4", "Shrt Data"])
    menu.add_row(["5", "Keluar"])
    print(menu)
# ======================== MENU ========================
# ======================== TAMBAH DATA ========================
def tambahData():
    os.system('cls')
    data = []
    item = [
        'Masukkan NIP\t: ',
        'Masukkan Nama\t: ',
        'Masukkan TanggalLahir\t: ',
        'Masukkan GajiPokok\t: ',
        'Masukkan Tanggungan\t: '
    ]
    maxLengthList = 5
    a = 0
    while a < maxLengthList:
        isi = input(item[a])
        data.append(isi)
        a += 1

    txt = data[0]+";"+data[1]+";"+data[2]+";"+data[3]+";"+data[4];
    os.system('cls')
    print("======================= KONFIRMASI DATA =======================")
    print("Nip : "+data[0]+"\n")
    print("Nama : "+data[1]+"\n")
    print("TanggalLahir : "+data[2]+"\n")
    print("GajiPokok : "+data[3]+"\n")
    print("Tanggungan : "+data[4]+"\n")
    tambah = input("Apakah sudah benar ? (y/n) : ")
    if tambah == 'n':
        tambahData()
    elif tambah == 'y':
        f = open("data.txt", "a")
        f.write(txt+"\r")
        f.close()
        main()
# ======================== TAMBAH DATA ========================
# ======================== SEARCH ========================
def SearchPegawai(inp):
    data_path = "data.txt"
    dat = open("{}".format(data_path), "r")
    search = PrettyTable()
    search.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
    s = inp
    with dat as file:
        for line in file:
            if s in line[0]:
                search.add_row(line.strip('\t').strip('\n').split(";"))
        print(search)
    dat.close()
# ======================== SEARCH ========================
# ======================== SORTIR ========================
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if int(nlist[i][3]) > int(nlist[i-1][3]):
                temp = nlist[i][3]
                nlist[i][3] = nlist[i+1][3]
                nlist[i+1][3] = temp
# ======================== SORTIR ========================
# ======================== DAFTAR KARYAWAN ========================
def daftarKaryawan():
    data_path = "data.txt"
    dataTxt = open("{}".format(data_path), "r")
    daftar = PrettyTable()
    daftar.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
    for line in dataTxt.readlines():
        daftar.add_row(line.strip('\t').strip('\n').split(";"))
    print(daftar)
    if input("Kembali :  (0) ") == '0':
        main()
    dataTxt.close()
# ======================== DAFTAR KARYAWAN ========================
# ======================== CALL FUNC ========================
def main():
    loop = True
    while loop:
        os.system('cls')
        menu()
        choice2 = input("No: ")
        if choice2 == '1':
            tambahData()
            loop = False
        if choice2 == '2':
            daftarKaryawan()
            loop = False
        if choice2 == '3':
            inp = input("Search... ")
            SearchPegawai(inp)
            loop = False
        if choice2 == '4':
            nlist = []
            data_path = "data.txt"
            dataTxt = open("{}".format(data_path), "r")
            data = dataTxt.readlines()
            for a in data:
                test = a.strip().split(';')
                nlist.append(test)
            nlist.sort(key=lambda x: x[3], reverse=True)
            x = PrettyTable()
            x.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
            for line in nlist:
                x.add_row(line)
            print(x)
            if input("Kembali :  (0) ") == '0':
                main()
            dataTxt.close()
            loop = False
        if choice2 == '5':
            exit()

# sort list with key
# nlist.sort(key=takeSecond)
# print('Sorted list:', nlist)
# bubbleSort(nlist)

main()

# menu()
# if input("No: ") == '1':
#     os.system('cls')
#     if tambahData() == 1:
#         os.system('cls')
#         menu()
#         if



# if no == '1':
#     os.system('cls')
#     if tambahData() == 0:
#         os.system('cls')
#         menu()
#     else:
#         os.system('cls')
#         menu()
#         elif no == '2':\
#             os.system('cls')
#         daftarKaryawan()
#         elif no == '3':\
#             os.system('cls')
#         search = input(" Search ... ")
#         SearchPegawai(search)
# ======================== CALL FUNC ========================

# def search(inu):
#     with dataTxt as a:
#         b = a.read()
#     b.find('asd')
#     print(b)
#     if 'asd' in open(data_path).read():
#         print("ok")
#
#     inp = input('Masukkan ')
#     SearchPegawai(inp)
#     x = dataTxt.readlines()
# ======================== SEARCH ========================



# ======================== SORTIR ========================
# # bubleSort(alist)
# # print(alist)
# def bubbleSort(nlist):
#     # print(nlist)
#     for passnum in range(len(nlist)-1,0,-1):
#         for i in range(passnum):
#             if nlist[i][3]<nlist[i-1][3]:
#                 temp = nlist[i][3]
#                 nlist[i][3] = nlist[i+1][3]
#                 nlist[i+1][3] = temp
#
# nlist = []
# for a in x:
#     # print(a.split())
#     test = a.strip().split(';')
#     nlist.append(test)
# bubbleSort(nlist)
# x = PrettyTable()
# x.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
# ad = 0
# for line in nlist:
#     x.add_row(line)
# print(x)












# print('Return type:', np.sort())
# print(sorted(b, key=itemgetter(3) ,reverse=True))
# for c in b:
    # print(c)
    # mat = np.array(c)
    # mat_sort = mat[mat[:5,3].argsort()]
    # sorted(mat, key=itemgetter(0))
    # print(mat)
    # print(c.sort(axis=2))
    # a = sort(b, key=itemgetter(1), reverse=True)
    # print(a)
    # i += 1
















# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')


# cls()
# with open("data.txt", "r") as f:
#     for line in f.readline():
#         print(line)

# x = PrettyTable()
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#
#
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
#
# print(x)
# f = open("data.txt", "a")
# f.write("Woops! I have deleted the content! \r")

# NIP,NAMA,date,gajipokok,tanggungan

# sort_key = lambda line: int(line.split(None, 1)[0])
# i = 0
# j = 0
# alist = []
# for a in x:
#     # print(a.split())
#     test = a.strip().split(';')
#     alist.append(test)
#
