print("=======Konversi Temperatur=======")
def konversi():
    def KonversiC():
        def kalkulatorrc(awal):
            r = awal
            r = float(r)
            c = r*(5/4)
            return c

        def kalkulatorkc(awal):
            k = awal
            k = float(k)
            c = k-273.15
            return c

        def kalkulatorfc(awal):
            f = awal
            f = float(f)
            c = (f-32)*(5/9)
            return c

        print("===========Pilih Konversi============\n"
              "1. Remamur Ke Celcius\n"
              "2. Kelvin Ke Celcius\n"
              "3. Fahrenheit Ke Celcius\n")
        select = int(input("Pilih Operasi 1, 2, 3 :"))
        awal = float(input("Masukkan Suhu awal: "))

        if select == 1:
            print("=======Reamur Ke Celcius=======")
            print("Suhu =", kalkulatorrc(awal), "°C")
        elif select == 2:
            print("=======Kelvin Ke Celcius=======")
            print("Suhu =", kalkulatorkc(awal), "°C")
        elif select == 3:
            print("=======Fahrenheit Ke Celcius=======")
            print("Suhu =", kalkulatorfc(awal), "°C")
        else:
            print("Invalid input")

    def KonversiR():
        def kalkulatorcr(awal):
            c = awal
            c = float(c)
            r = c*(4/5)
            return r

        def kalkulatorkr(awal):
            k = awal
            k = float(k)
            r = (k+273.15) * (4 / 5)
            return r

        def kalkulatorfr(awal):
            f = awal
            f = float(f)
            r = (f+32) * (9 / 4)
            return r

        print("===========Pilih Konversi============\n"
              "1. Celcius Ke Reamur\n"
              "2. Kelvin Ke Reamur\n"
              "3. Fahrenheit Ke Reamur\n")
        select = int(input("Pilih Operasi 1, 2, 3 :"))
        awal = float(input("Masukkan Suhu awal: "))

        if select == 1:
            print("=======Celcius Ke Reamur=======")
            print("Suhu =", kalkulatorcr(awal), "°C")
        elif select == 2:
            print("=======Kelvin Ke Reamur=======")
            print("Suhu =", kalkulatorkr(awal), "°C")
        elif select == 3:
            print("=======Fahrenheit Ke Reamur=======")
            print("Suhu =", kalkulatorfr(awal), "°C")
        else:
            print("Invalid input")

    def KonversiK():
        def kalkulatorrk(awal):
            r = awal
            r = float(r)
            k = (r-273.15)*(4/5)
            return k

        def kalkulatorck(awal):
            c = awal
            c = float(c)
            k = c+273.15
            return k

        def kalkulatorfk(awal):
            f = awal
            f = float(f)
            k = (f-32)*(5/9) + 273.15
            return k

        print("===========Pilih Konversi============\n"
              "1. Remamur Ke Kelvin\n"
              "2. Celcius Ke Kelvin\n"
              "3. Fahrenheit Ke Kelvin\n")
        select = int(input("Pilih Operasi 1, 2, 3 :"))
        awal = float(input("Masukkan Suhu awal: "))

        if select == 1:
            print("=======Reamur Ke Kelvin=======")
            print("Suhu =", kalkulatorrk(awal), "°C")
        elif select == 2:
            print("=======Celcius Ke Kelvin=======")
            print("Suhu =", kalkulatorck(awal), "°C")
        elif select == 3:
            print("=======Fahrenheit Ke Kelvin=======")
            print("Suhu =", kalkulatorfk(awal), "°C")
        else:
            print("Invalid input")

    def KonversiF():
        def kalkulatorrf(awal):
            r = awal
            r = float(r)
            f = (r-32)*(5/9)
            return f

        def kalkulatorkf(awal):
            k = awal
            k = float(k)
            f = (k-273.15)*(9/5) + 32
            return f

        def kalkulatorcf(awal):
            c = awal
            c = float(c)
            f = (c*(9/5)) + 32
            return f

        print("===========Pilih Konversi============\n"
              "1. Remamur Ke Fahrenheit\n"
              "2. Kelvin Ke Fahrenheit\n"
              "3. Celcius Ke Fahrenheit\n")
        select = int(input("Pilih Operasi 1, 2, 3 :"))
        awal = float(input("Masukkan Suhu awal: "))

        if select == 1:
            print("=======Reamur Ke Fahrenheit=======")
            print("Suhu =", kalkulatorrf(awal), "°C")
        elif select == 2:
            print("=======Kelvin Ke Fahrenheit=======")
            print("Suhu =", kalkulatorkf(awal), "°C")
        elif select == 3:
            print("=======Celcius Ke Fahrenheit=======")
            print("Suhu =", kalkulatorcf(awal), "°C")
        else:
            print("Invalid input")

    print("===========Pilih Konversi============\n"
          "1. Konversi Ke Celcius\n"
          "2. Konversi Ke Reamur\n"
          "3. Konversi Ke Kelvin\n"
          "4. Konnversi Ke Fahrenheit\n")
    select = int(input("Pilih Operasi 1, 2, 3, 4 :"))
    if select == 1:
        KonversiC()
    elif select == 2:
        KonversiR()
    elif select == 3:
        KonversiK()
    elif select == 4:
        KonversiF()
    else:
        print("Invalid input")


while True:
    konversi()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
