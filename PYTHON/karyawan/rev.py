choice = '0'
    nlist = []
    data = dataTxt.readlines()
    while choice == '0':
        os.system('cls')
        menu()
        choice2 = input("No: ")
        if choice2 == '1':
            if tambahData() == '0':
                choice2 = '10'
        if choice2 == '2':
            if daftarKaryawan() == '0':
                choice2 = 'index'
        if choice2 == '3':
            inp = input("Search ... ")
            SearchPegawai(inp)
            if input("Kembali : (0) ") == '0':
                choice2 = 'index'
        if choice2 == '4':
            for a in data:
                test = a.strip().split(';')
                nlist.append(test)
            bubbleSort(nlist)
            x = PrettyTable()
            x.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
            ad = 0

            for line in nlist:
                x.add_row(line)
            print(x)
            if input("Kembali :  (0) ") == '0':
                choice2 = 'index'
        if choice2 == '5':
            choice = '5'
        if choice2 == '10':
            if tambahData() == '0':
                choice2 = '10'
            elif tambahData() == '1':
                choice2 = 'index'    












    while loop:
        menu()
        choice = input("Enter your choice [1-5] :")
        if choice == '1':
            os.system('cls')
            tambahData()
            loop = False
        if choice == '2':
            os.system('cls')
            daftarKaryawan()
            loop = False
        if choice == '3':
            os.system('cls')
            inp = input("Search ... ")
            SearchPegawai(inp)
            loop = False
        if choice == '4':
            os.system('cls')
            refresh()
            loop = False           




            def refresh():
    nlist = []
    data = dataTxt.readlines()
    for a in data:
        test = a.strip().split(';')
        nlist.append(test)
        bubbleSort(nlist)
        x = PrettyTable()
        x.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
        ad = 0

    return nlist                    



        while choice == '0':
        os.system('cls')
        menu()
        choice2 = input("No: ")
        if choice2 == '1':
            if tambahData() == '0':
                choice2 = '10'
        if choice2 == '2':
            if daftarKaryawan() == '0':
                choice2 = 'index'
        if choice2 == '3':
            inp = input("Search ... ")
            SearchPegawai(inp)
            if input("Kembali : (0) ") == '0':
                choice2 = 'index'
        if choice2 == '4':
            nlist = []
            data = dataTxt.readlines()
            for a in data:
                test = a.strip().split(';')
                nlist.append(test)
            bubbleSort(nlist)
            x = PrettyTable()
            x.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
            ad = 0

            for line in nlist:
                x.add_row(line)
            print(x)
            if input("Kembali :  (0) ") == '0':
                choice2 = 'index'
        if choice2 == '5':
            choice = '5'
        if choice2 == '10':
            if tambahData() == '0':
                choice2 = '10'
            elif tambahData() == '1':
                choice2 = 'index'





                if choice2 == '2':
            if daftarKaryawan() == '0':
                choice2 = 'index'
        if choice2 == '3':
            inp = input("Search ... ")
            SearchPegawai(inp)
            if input("Kembali : (0) ") == '0':
                choice2 = 'index'
        if choice2 == '4':
            nlist = []
            data = dataTxt.readlines()
            for a in data:
                test = a.strip().split(';')
                nlist.append(test)
            bubbleSort(nlist)
            x = PrettyTable()
            x.field_names = ["NIP", "Nama", "Tanggal Lahir", "Gaji Pokok", "Tanggungan"]
            ad = 0

            for line in nlist:
                x.add_row(line)
            print(x)
            if input("Kembali :  (0) ") == '0':
                choice2 = 'index'


            if nlist[i][3]<nlist[i-1][3]:
                temp = nlist[i][3]
                nlist[i][3] = nlist[i+1][3]
                nlist[i+1][3] = temp
