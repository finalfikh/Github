kata = input("Input: ")
temp = ""

for i in range(len(kata)-1, -1, -1): #Looping dari karakter / huruf terakhir
    temp+=kata[i]

print("Output: ", end="")
if(kata == temp): #Pengecekan kondisi dengan membandingkan kedua variabel
    print("True")
else:
    print("False")
