inpPertama  = int(input())
inpBilBul   = []
inpBanBol   = []
pertanyaan  = []
main        = []

for a in range(inpPertama):
    st = "Kasus #" + str(a+1) + ":"
    main.append(st)
    inp = input()
    split = inp.split(' ')
    if (len(split) > 2 or len(split) < 2):
        print("Error :(")
        exit()
    else:
        inpBilBul.append(split)
    inp2 = input()
    split2 = inp2.split(' ')
    if (len(split2) > int(inpBilBul[a][0]) or len(split2) < int(inpBilBul[a][0])):
        print("Errors :(" + str(len(split2)))
        exit()
    else:
        inpBanBol.append(split2)
    for b in range(int(inpBilBul[a][1])):
        inp3 = input()
        split3 = inp3.split(' ')
        if(len(split3) > 2 or len(split3) < 2):
            print("Error :(")
            exit()
        else:
            pertanyaan.append(split3)
    for ad in range(len(pertanyaan)):
        dd = 0
        for da in range(len(inpBanBol[a])):
            if int(inpBanBol[a][da]) > int(pertanyaan[ad][0]) and int(inpBanBol[a][da]) < int(pertanyaan[ad][1]):
                dd += 1
        main.append(dd)
        dd = 0
    pertanyaan = []

for i in range(len(main)):
    print(main[i])
