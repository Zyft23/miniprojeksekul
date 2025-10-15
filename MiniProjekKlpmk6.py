total_pulsa = 0
total_Ewallet = 0
total_aksesoris = 0
while True:
    print("====Zhamet Chell====")
    print("1.Isi pulsa")
    print("2.Isi E-Wallet")
    print("3.Aksesoris")
    print("4.Selesai")
    pilihan = int(input("Pilih Dari angka 1-4"))
    if pilihan == 1:
        print("===Pulsa===")
        no_hp = (input("masukan nomor hp"))
        nominal_pulsa = int(input("masukan nominal"))
        total_pulsa += nominal_pulsa
    elif pilihan == 2:
        print("====E-Wallet====")
        print("1.Dana")
        print("2.GoPay")
        print("3.shopeePay")
        print("4.batal")
        while True:
            pilihan2 = int(input("Pilih Dari 1-3"))
            if pilihan2 == 1:
                print("===Dana===")
                dana = int(input("masukkan Nomor Dana"))
                nominalWallet = int(input("masukkan Nominal"))
                total_Ewallet += nominalWallet
            elif pilihan2 == 2:
                print("===GoPay===")
                gopay = int(input("masukkan Nomor Gopay"))
                nominalWallet = int(input("masukkan Nominal"))
                total_Ewallet += nominalWallet
            elif pilihan2 == 3:
                shopeepay = int(input("masukkan Nomor ShopeePay"))
                nominalWallet = int(input("masukkan Nominal"))
                total_Ewallet += nominalWallet
            elif pilihan2 == 4:
                break
            else:
                print("Tidak ada Pilihan tersebut")
    elif pilihan == 3:
        while True:
            print("====Aksesoris====")
            print("1.Kabel Data")
            print("2.Earphone")
            print("3.Casing Hp")
            pilihan3 = int(input("Pilih Aksesoris Dari 1-3"))
            if pilihan3 == 1:
                while True:
                    print("1.Type C")
                    print("2.Micro Usb")
                    print("3.Batal")
                    opsikabel = int(input("Pilih Tipe Kabel 1-2"))
                    if opsikabel == 1:
                        typeC = int(input("beli berapa banyak"))
                        hargaC = 10000
                        totalhargakabel += typeC * hargaC
                    elif opsikabel == 2:
                        micro = int(input("beli berapa banyak"))
                        hargamicro = 7500
                        totalhargakabel += micro * hargamicro
                    elif opsikabel == 3:
                        break
                    else:
                        print("tidak ada pilihan")
            elif pilihan3 == 2:
                while True:
                    print("1.Low budget")
                    print("2.Mid budget")
                    print("3.High Budget")
                    print("4.Batal")
                    opsiEar = int(input("Pilih Tier earphone 1-3"))
                    if opsiEar == 1:
                        hargaear = 10000
                        lowear = int(input("beli berapa banyak"))
                        hargatotalear += lowear * hargaear
                    elif opsiEar == 2:
                        hargaear = 25000
                        midear = int(input("beli berapa banyak"))
                        hargatotalear += midear * hargaear
                    elif opsiEar == 3:
                        hargaear = 50000
                        highear = int(input("beli berapa banyak"))
                        hargatotalear += highear * hargaear
                    elif opsiEar == 4:
                        break
                    else:
                        print("tidak ada pilihan")
            elif pilihan3 == 3:
                while True:
                    print("1.xiaomi")
                    print("2.realme")
                    print("3.iphone")
                    print("4.batal")
                    opsicase = int(input("Pilih merek"))
                    if opsicase == 1:
                        hargacasex = 5000
                        totalhargacase += xcase * hargacasex
                        xcase = int(input("berapa banyak yg dibeli"))
                    elif opsicase == 2:
                        hargacaser = 4500
                        rcase = int(input("berapa banyak yg dibeli"))
                        totalhargacase += rcase * hargacaser
                    elif opsicase == 3:
                        hargacasei = 5500
                        icase = int(input("berapa banyak yg dibeli"))
                        totalhargacase += icase * hargacasei