
def konversi():
    print("==========Konversi Suhu==========\n1.Celcius\t2.Fahreinheit\n3.Calvin\t4.Reamur\n")
    awal = int(input("Ubah dari : "))
    akhir = int(input("Ubah ke : "))
    suhu = int(input("Masukkan suhu : "))

    if(awal == 1 or awal == 3):
        k_awal = 5
        if(awal == 3):
            suhu -= 273.15
    elif(awal == 2):
        k_awal = 9
        suhu -= 32
    elif(awal == 4):
        k_awal = 4

    if(akhir == 1 or akhir == 3):
        k_akhir = 5
    elif(akhir == 2):
        k_akhir = 9
    elif(akhir == 4):
        k_akhir = 4

    suhu_akhir = (k_akhir/k_awal)*suhu
    if(akhir == 2):
        suhu_akhir += 32
    elif(akhir == 3):
        suhu_akhir += 273.15

    print("Suhu akhir adalah : {suhu}".format(suhu = suhu_akhir))

    
while(True):
    konversi()
    if(input("Repeat ? (Y/N)").strip().upper() != "Y"):
        break