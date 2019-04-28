data = [
    ["Yusuf", 100000000],
    ["Eko", 30000],
    ["Anggoro", 120]
]
n = len(data)
#
# for j in range(n):
#
#     for k in range(0, n-j-1):
#         if data[k][1] > data[k+1][1]:
#             data[k][0], data[k+1][0] = data[k+1][0], data[k][0]
#             data[k][1], data[k+1][1] = data[k+1][1], data[k][1]
#
#
# for i in data:
#     print(i)

data_path = "data.txt"
dat = open("{}".format(data_path), "r")
with dat as file:
    for line in file:

        print(line.strip('\t').strip('\n').split(';'))
