total_pulsa = 0
total_Ewallet = 0
hargaakesoris = 0
nominal = 0
itp = []
list_hp = []
list_nominalhp = []
listnowallet = []
listwallertnominal = []
listnamawallet = []
Tharga_aksesoris = []
nama_aksesoris = []
jumlah_aksesoris = []


while True:
    print("====Zhamet Chell====")
    print("1.Isi pulsa")
    print("2.Isi E-Wallet")
    print("3.Aksesoris")
    print("4.Selesai")
    pilihan = input("Pilih layanan : ")
    if pilihan.isdigit():
        pilihan = int(pilihan)
        if pilihan == 1:
            while True:
                print("===Pulsa===")
                print("ketik batal untuk membatalkan")
                no_hp = input("masukkan Nomor Pulsa (12 digit) : ").lower()
                if no_hp == "batal":
                    break
                elif no_hp.isdigit() and len(no_hp) ==12:
                    nominal = input("masukan nominal : ")
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
                pilihan = input("Pilih E-Wallet: ")
                if pilihan.isdigit():
                    pilihan = int(pilihan)
                    if pilihan == 1:
                        namawallet = "Dana"
                        while True:
                            print("===Dana===")
                            print("ketik batal untuk membatalkan")
                            dana = input("masukkan Nomor Dana (12 digit) : ").lower()
                            if dana == "batal":
                                break
                            elif dana.isdigit() and len(dana) == 12:
                                while True:
                                    nominal = input("masukkan Nominal : ")
                                    if nominal.isdigit():
                                        nominal = int(nominal)
                                        if nominal > 0:
                                            total_Ewallet += nominal
                                            listnowallet.append(dana)
                                            listwallertnominal.append(nominal)
                                            listnamawallet.append(namawallet)
                                            break
                                        else:
                                            print("nominal harus berupa angka")
                                    else:
                                        print("nominal tidak valid")
                                break
                            else:
                                print("nomor tidak valid")
                    elif pilihan == 2:
                        namawallet = "Gopay"
                        while True:
                            print("===GoPay===")
                            print("ketik batal untuk membatalkan")
                            gopay = input("masukkan Nomor Gopay (12 digit) : ").lower()
                            if gopay == "batal":
                                break
                            elif gopay.isdigit() and len(gopay) == 12:
                                nominal = input("masukkan Nominal : ")
                                if nominal.isdigit():
                                    nominal = int(nominal)
                                    if nominal > 0:
                                        total_Ewallet += nominal
                                        listnowallet.append(gopay)
                                        listwallertnominal.append(nominal)
                                        listnamawallet.append(namawallet)
                                        break
                                    else:
                                        print("nominal harus berupa angka")
                                else:
                                    print("hanya berupa angka")
                            else:
                                print("nomor tidak valid")
                    elif pilihan == 3:
                        namawallet = "shopeepay"
                        while True:
                            print("===ShopeePay===")
                            print("ketik batal untuk membatalkan")
                            shopeepay = input("masukkan Nomor ShopeePay (12 digit) : ").lower()
                            if shopeepay == "batal":
                                break
                            elif shopeepay.isdigit() and len(shopeepay) == 12:
                                nominal = input("masukkan Nominal : ")
                                if nominal.isdigit():
                                    nominal = int(nominal)
                                    if nominal > 0:
                                        total_Ewallet += nominal
                                        listnowallet.append(shopeepay)
                                        listwallertnominal.append(nominal)
                                        listnamawallet.append(namawallet)
                                        break
                                    else:
                                        print("nominal harus berupa angka")
                                else:
                                    print("harus berupa angka")
                            else:
                                print("nomor tidak valid")
                    elif pilihan == 4:
                        break
                    else:
                        print("Tidak ada Pilihan tersebut")
                else:
                    print("pilihan berupa angka")
        elif pilihan == 3:
            while True:
                print("====Aksesoris====")
                print("1.Kabel Data")
                print("2.Earphone")
                print("3.Casing Hp")
                print("4.batal")
                pilihan = input("Pilih Aksesoris : ")
                if pilihan.isdigit():
                    pilihan = int(pilihan)
                    if pilihan == 1:
                        while True:
                            print("1.Type C - Rp 10.000")
                            print("2.Micro Usb - Rp 7.500")
                            print("3.Batal")
                            pilihan = input("Pilih Tipe Kabel : ")
                            if pilihan.isdigit():
                                pilihan = int(pilihan)
                                if pilihan == 1:
                                    namaakse = "Type C"
                                    harga = 10000
                                    while True:
                                        jumlah = input("beli berapa banyak : ").lower()
                                        if jumlah == "batal":
                                            break
                                        elif jumlah.isdigit():
                                            jumlah = int(jumlah)
                                            hargaakesoris += jumlah * harga
                                            nama_aksesoris.append(namaakse)
                                            Tharga_aksesoris.append(jumlah * harga)
                                            jumlah_aksesoris.append(jumlah)
                                            break
                                        else:
                                            print("hanya menggunakan angka")
                                elif pilihan == 2:
                                    namaakse = "Type Micro Usb"
                                    harga = 7500
                                    while True:
                                        jumlah = input("beli berapa banyak : ").lower()
                                        if jumlah == "batal":
                                            break
                                        elif jumlah.isdigit():
                                            jumlah = int(jumlah)
                                            hargaakesoris += jumlah * harga
                                            nama_aksesoris.append(namaakse)
                                            Tharga_aksesoris.append(jumlah * harga)
                                            jumlah_aksesoris.append(jumlah)
                                            break
                                        else:
                                            print("hanya menggunakan angka")
                                elif pilihan == 3:
                                    break
                                else:
                                    print("tidak ada pilihan")
                            else:
                                print("harus berupa angka")
                    elif pilihan == 2:
                        while True:
                            print("1.Low budget - Rp 10.000")
                            print("2.Mid budget - Rp 25.000")
                            print("3.High Budget - Rp 50.000")
                            print("4.Batal")
                            pilihan = input("Pilih dari 1-4 :")
                            if pilihan.isdigit():
                                pilihan = int(pilihan)
                                if pilihan == 1:
                                    namaakse = "Low Budger Earphone"
                                    harga = 10000
                                    jumlah = input("beli berapa banyak : ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        hargaakesoris += jumlah * harga
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        break
                                    else:
                                        print("harus berupa angka")
                                elif pilihan == 2:
                                    namaakse = "Mid budget Earphone"
                                    harga = 25000
                                    jumlah = input("beli berapa banyak : ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("harus berupa angka")
                                elif pilihan == 3:
                                    namaakse = "High budget Earphone"
                                    harga = 50000
                                    jumlah = input("beli berapa banyak : ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("harus berupa angka")
                                elif pilihan == 4:
                                    break
                                else:
                                    print("tidak ada pilihan")
                            else:
                                print("harus berupa angka")
                    elif pilihan == 3:
                        while True:
                            print("1.xiaomi - Rp 5.000")
                            print("2.realme - Rp 4.500")
                            print("3.iphone - Rp 5.500")
                            print("4.batal")
                            pilihan = input("Pilih merek : ")
                            if pilihan.isdigit():
                                pilihan = int(pilihan)
                                if pilihan == 1:
                                    namaakse = "Casexiaomi"
                                    harga = 5000
                                    jumlah = input("berapa banyak yg dibeli : ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        hargaakesoris += jumlah * harga
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        break
                                    else:
                                        print("jumlah harus angka")
                                elif pilihan == 2:
                                    namaakse = "CaseRealme"
                                    harga = 4500
                                    jumlah = input("berapa banyak yg dibeli : ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("jumlah harus berupa angka")
                                elif pilihan == 3:
                                    namaakse = "Case Iphone"
                                    harga = 5500
                                    jumlah = input("berapa banyak yg dibeli : ")
                                    if jumlah.isdigit():
                                        jumlah = int(jumlah)
                                        nama_aksesoris.append(namaakse)
                                        jumlah_aksesoris.append(jumlah)
                                        Tharga_aksesoris.append(jumlah * harga)
                                        hargaakesoris += jumlah * harga
                                        break
                                    else:
                                        print("harus berupa angka")
                                elif pilihan == 4:
                                    break
                            else:
                                print("harus berupa angka")
                    elif pilihan == 4:
                        break
                    else:
                        print("tidak ada pilihan")
        elif pilihan == 4:
            total = hargaakesoris + total_Ewallet + total_pulsa
            print("=" * 10)
            print("Zhamet cell")
            print("=" * 10)
            for p in range (len(list_hp)):
                print("Pulsa")
                print( p+1, " No : ", list_hp[p], "nominal :", list_nominalhp[p])
            print("-" * 10)
            print("E-Wallet:")
            for e in range(len(listnowallet)):
                print(e+1 , listnamawallet[e] ," No : ", listnowallet[e], "nominal :", listwallertnominal[e])
            print("-" * 10)
            print("Aksesoris")
            print("-" * 10)
            for a in range (len(nama_aksesoris)):
                print(a+1, nama_aksesoris[a], "|", jumlah_aksesoris[a], "|" , "Rp",Tharga_aksesoris[a])
            print("-" * 10)
            print("total : ", total)
            print("-" * 10)
            print("ありがとうございました")
            break
        else:
            print("tidak ada pilihan")
    else:
        print("harus berupa angka")
