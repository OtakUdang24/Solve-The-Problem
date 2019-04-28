from os import system
from time import sleep
from prettytable import PrettyTable

# # define our clear function
# def clear():
#
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
#
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')

def menu():
    system('clear')
    menu = PrettyTable()
    menu.field_names = [" No", "Pilih Pengurutan Ascending atau Descending"]
    menu.add_row(["1.", "Ascending"])
    menu.add_row(["2.", "Descending"])
    print(menu)

def asc(arr):
    arr = arr
    # print(arr)
    print("Diurutkan secara Ascending ")
    n = len(arr)
    for i in range(n):
        # 0
        for j in range(0, n-i-1):
            # print("a " + str(j))
            # 0
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for j in range(n):
        print(arr[j])
    print("============================================================")

def desc(arr):
    arr = arr
    print("Diurutkan secara Descending ")
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for j in range(n):
        print(arr[j])
    print("============================================================")

if __name__ == '__main__':
    choice = True
    menu()
    choice = int(input("Masukkan pilihan anda <1 atau 2>: "))
    sleep(1)
    while choice:
        if choice == 1:
            arr = []
            jarr = int(input("Masukkan banyak elemen array = "))
            sleep(1)
            for a in range(jarr):
                inpus = int(input("Elemen ke - " + str(a+1) + " = "))
                sleep(1)
                arr.append(inpus)
            sleep(2)
            asc(arr)
            kembali = input("Kembali ke Menu Utama : pilih [Y/N] ")
            sleep(1)
            if kembali == "Y" or kembali == "y":
                menu()
                choice = int(input("Masukkan pilihan anda <1 atau 2>: "))
                sleep(1)
            elif kembali == "n" or kembali == "N":
                exit()
        elif choice == 2:
            arr = []
            jarr = int(input("Masukkan banyak elemen array = "))
            sleep(1)
            for a in range(jarr):
                inpus = int(input("Elemen ke - " + str(a+1) + " = "))
                sleep(1)
                arr.append(inpus)
            sleep(2)
            desc(arr)
            kembali = input("Kembali ke Menu Utama : pilih [Y/N] ")
            sleep(1)
            if kembali == "Y" or kembali == "y":
                menu()
                choice = int(input("Masukkan pilihan anda <1 atau 2>: "))
                sleep(1)
            elif kembali == "n" or kembali == "N":
                exit()
