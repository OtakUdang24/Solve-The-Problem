kalimat = []
updKal  = []
hasil   = []

inpJKas = int(input("Jumlah Kasus : "))

def split(word):
    return [char for char in word]

for a in range(inpJKas):
    jumKel = int(input("Jumlah Kalimat : "))
    inpKal = input("Input Kalimat : ")
    kalimat.append(inpKal.split(' '))
    if len(kalimat[a]) > jumKel or len(kalimat[a]) < jumKel:
        print("Error :{")
        exit()
    # Looping berdasarkan banyak kalimat
    for b in range(len(kalimat[a])):
        kal = split(kalimat[a][b])
        # print(kal)
        kalVal = []
        # Looping berdasarkan banyak kata di satu kalimat
        for c in range(len(kal)):
            # print(kal[c])
            if kal[c] == '0':
                kalVal.append("o")
            elif kal[c] == '1':
                kalVal.append("i")
            elif kal[c] == '2':
                kalVal.append("z")
            elif kal[c] == '3':
                kalVal.append("e")
            elif kal[c] == '4':
                kalVal.append("a")
            elif kal[c] == '5':
                kalVal.append("s")
            elif kal[c] == '6':
                kalVal.append("g")
            elif kal[c] == '7':
                kalVal.append("t")
            elif kal[c] == '8':
                kalVal.append("b")
            elif kal[c] == '9`':
                kalVal.append("q")
            else:
                kalVal.append(kal[c])
        updKal.append(kalVal)
    txt = ''
    updKal.reverse()
    kasusFix = []
    for ii in range(len(updKal)):
        for dd in range(len(updKal[ii])):
            txt += updKal[ii][dd]
            # print(updKal[ii][dd])
            # print(updKal[ii])
        txt += " "
    kasusFix.append("Kasus #" + str(a+1) + ": ")
    kasusFix.append(txt)
    hasil.append(kasusFix)
    updKal = []

for d in range(len(hasil)):
    for e in range(len(hasil[d])):
        print(hasil[d][e], end="")
    print(end="\n")











































        # print(kalVal)
        # updKal.append(kalVal)

        # break
# print(updKal)












    # for i in range(len(kalimat[a])):
    # for t in range(len(updKal[a])):
        # print(t)
        # for k in range(len(updKal[t])):
        #     print(updKal[t][k])
        # print(updKal[b][t])
            # print(updKal[b][t])
        # print(kalVal)
        # print(kalVal[b])
    # for t in range(len(kalVal[b])):
    #     print(kalVal[c][t])
        # updKal.append(kalVal)
        # kalVal = []
        # for dd in range(len(kalVal[a])):
        #     print(kalVal[dd][dd])
    # updKal.reverse()
    # print(updKal)
    # hasil.append("Kasus #" + str(a+1) + ": ")
    # fx = []
    # for d in range(len(updKal)):
    #     dd = []
    #     for e in range(len(updKal[d])):
    #         dd.append(updKal[d][e])
    #     hasil.append(dd)
        # fx.append()
        # print(end=" ")
            # fx.append(updKal[a][d])
            # print(updKal[a][d], end="")
    # print(fx)
    # for d in range(len(updKal[a])):
    #     for e in range(len(updKal[d])):
    #         print(updKal[d][e], end="")
    #     print(" ")

# print(hasil)

# tinggal reverse
# for aa in range(len(updKal)):
#     for bb in range(len(updKal[aa])):
#         print(updKal[aa][bb], end="")
#     print(end=" ")
# print(updKal)
# print(len(kalimat[a]))
