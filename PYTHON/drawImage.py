import math

def drawImage(p):
    bakol = p-1 #banyak kolom
    # print(bakol)
    onehalf = math.floor(p/2)
    # print(onehalf)
    # baris itu horizontal, kolom itu vertical
    for baris in range(p):
        # kolom
        for kolom in range(p):
            # baris
            if baris == 0 or baris == bakol:
                if kolom == 0 or kolom == bakol:
                    print("* ", end=" ")
                elif kolom == onehalf:
                    print("* ", end=" ")
                else:
                    print("= ", end=" ")
            else:
                if kolom == onehalf or baris == onehalf:
                    print("* ", end=" ")
                else:
                    print("= ", end=" ")
        print("\n")
drawImage(11)
