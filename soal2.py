# kata = input('Masukan kata : ')
# panjangKata = len(kata)

# def segitigaKata (kata): 
#     # hasil = ''
#     for row in range(panjangKata):
#         if panjangKata >= 4: 
            
#         else: 
#             print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
#         for col in range(row+1):
#             print(kata[col], end = '')
#         print()
# print(segitigaKata(kata))
#================================================================================


# def segitigakata(kata):
kata = ("Purwadhika Startup and Coding School @BSD").replace (' ', '')
listKata = list(kata)

x = []
for a in range(len(listKata)):
    y = int((a*(a+1))/2)
    x.append (y)

n = 0 
if len(listKata) not in x:
    print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    n = x.index(len(listKata))

def hurufMaju(n):   
    no = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(listKata[no], end=" ")  
            no = no + 1
        print("\r") 

def hurufMundur(n):   
    nom = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print(listKata[nom], end=" ")  
            nom = nom + 1
        print("\r") 
       
hurufMaju(n)
hurufMundur(n)



