total_pulsa = 0
total_Ewallet = 0
hargaakesoris = 0
nominal = 0
list_hp = []
list_nominalhp = []
listnowallet = []
listwallertnominal = []
listnamawallet = []
nama_akesoris = []
harga_aksesoris = []
nama_aksesoris = []
jumlah_aksesoris = []


while True:
    print("====Zhamet Chell====")
    print("1.Isi pulsa")
    print("2.Isi E-Wallet")
    print("3.Aksesoris")
    print("4.Selesai")
    pilihan = int(input("Pilih Dari angka 1-4"))
    if pilihan == 1:
        while True:
            print("===Pulsa===")
            print("Masukkan nomor hp (12Digit)")
            print("ketik batal untuk membatalkan")
            no_hp = input(" : ").lower()
            if no_hp == "batal":
                break
            elif no_hp.isdigit() and len(no_hp) ==12:
                nominal = input("masukan nominal: ")
                if nominal.isdigit():
                    list_hp.append(no_hp)
                    nominal = int(nominal)
                    list_nominalhp.append(nominal)
                    total_pulsa += nominal
                    break
                else:
                    print("nominal harus berupa angka")
            else:
                print("nomor tidak valid")
    elif pilihan == 2:
        while True:
            print("====E-Wallet====")
            print("1.Dana")
            print("2.GoPay")
            print("3.shopeePay")
            print("4.batal")
            pilihan2 = int(input("Pilih Dari 1-4"))
            if pilihan2 == 1:
                namawallet = "Dama"
                while True:
                    print("===Dana===")
                    print("ketik batal untuk membatalkan")
                    dana = input("masukkan Nomor Dana(12digit)").lower()
                    if dana == "batal":
                        break
                    elif dana.isdigit() and len(dana) == 12:
                        while True:
                            nominal = input("masukkan Nominal")
                            if nominal.isdigit():
                                nominal = int(nominal)
                                total_Ewallet += nominal
                                listnowallet.append(dana)
                                listwallertnominal.append(nominal)
                                listnamawallet.append(namawallet)
                                break
                            else:
                                print("nominal tidak valid")
                        break
                    else:
                        print("nomor tidak valid")
            elif pilihan2 == 2:
                namawallet = "Gopay"
                while True:
                    print("===GoPay===")
                    gopay = input("masukkan Nomor Gopay")
                    if gopay.isdigit() and len(gopay) == 12:
                        nominal = input("masukkan Nominal")
                        if nominal.isdigit():
                            nominal = int(nominal)
                            total_Ewallet += nominal
                            listnowallet.append(gopay)
                            listwallertnominal.append(nominal)
                            listnamawallet.append(namawallet)
                            break
                        else:
                            print("hanya berupa angka")
                    else:
                        print("nomor tidak valid")
            elif pilihan2 == 3:
                namawallet = "shopeepay"
                while True:
                    print("===ShopeePay===")
                    shopeepay = int(input("masukkan Nomor ShopeePay"))
                    if shopeepay.isdigit() and len(shopeepay) == 12:
                        nominal = int(input("masukkan Nominal"))
                        total_Ewallet += nominal
                        listnowallet.append(shopeepay)
                        listwallertnominal.append(nominal)
                        listnamawallet.append(namawallet)
                        break
                    else:
                        print("nomor tidak valid")
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
            print("4.batal")
            pilihan3 = int(input("Pilih Aksesoris Dari 1-3"))
            if pilihan3 == 1:
                while True:
                    print("1.Type C")
                    print("2.Micro Usb")
                    print("3.Batal")
                    opsikabel = int(input("Pilih Tipe Kabel 1-2"))
                    if opsikabel == 1:
                        namaakse = "Type C"
                        hargaC = 10000
                        while True:
                            typeC = input("beli berapa banyak")
                            if typeC.isdigit():
                                typeC = int(typeC)
                                hargaakesoris += typeC * hargaC
                                nama_aksesoris.append(namaakse)
                                harga_aksesoris.append(typeC * hargaC)
                                jumlah_aksesoris.append(typeC)
                                break
                            else:
                                print("hanya menggunakan angka")
                    elif opsikabel == 2:
                        namaakse = "Type Micro Usb"
                        hargamicro = 7500
                        while True:
                            micro = input("beli berapa banyak")
                            if micro.isdigit():
                                totalhargakabel += micro * hargamicro
                                nama_aksesoris.append(namaakse)
                                harga_aksesoris.append(micro * hargamicro)
                                jumlah_aksesoris.append(micro)
                                break
                            else:
                                print("hanya menggunakan angka")
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
                    opsiEar = input("Pilih dari 1-4: ")
                    if opsiEar.isdigit():
                        if opsiEar == 1:
                            namaakse = "Low Budger Earphone"
                            hargaear = 10000
                            lowear = input("beli berapa banyak")
                            if lowear.isdigit():
                                lowear = int(lowear)
                                hargatotalear += lowear * hargaear
                            else:
                                print("harus berupa angka")
                        elif opsiEar == 2:
                            namaakse = "Mid budget Earphone"
                            hargaear = 25000
                            midear = int(input("beli berapa banyak"))
                            hargatotalear += midear * hargaear
                        elif opsiEar == 3:
                            namaakse = "High budget Earphone"
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
                    opsicase = int(input("Pilih merek : "))
                    if opsicase == 1:
                        namaakse = "Xiaomi"
                        xcase = int(input("berapa banyak yg dibeli : "))
                        hargacasex = 5000
                        hargaakesoris += xcase * hargacasex
                    elif opsicase == 2:
                        namaakse = "Realme"
                        hargacaser = 4500
                        rcase = int(input("berapa banyak yg dibeli : "))
                        hargaakesoris += rcase * hargacaser
                    elif opsicase == 3:
                        namaakse = "Iphone"
                        hargacasei = 5500
                        icase = int(input("berapa banyak yg dibeli : "))
                        hargaakesoris += icase * hargacasei
                    elif opsicase == 4:
                        break
            elif pilihan3 == 4:
                break
            else:
                print("tidak ada pilihan")
    elif pilihan == 4:
        total = hargaakesoris + total_Ewallet + total_pulsa
        print("=" * 10)
        print("Zhamet cell")
        print("=" * 10)
        for p in range (len(list_hp)):
            print("Pulsa", p+1, " No : ", list_hp[p], "nominal :", list_nominalhp[p])
            break
        print("-" * 10)
        print("E-Wallet:")
        for e in range(len(listnowallet)):
            print(e+1 , listnamawallet[e] ," No : ", listnowallet[e], "nominal :", listwallertnominal[e])
        print("-" * 10)
        print("akesoris")
        for a in range (len(nama_aksesoris)):
            print(a+1, nama_aksesoris[a], jumlah_aksesoris[a], harga_aksesoris[a])
        print("-" * 10)
        print(total)
        print("-" * 10)
        break
    else:
        print("tidak ada inpit")
