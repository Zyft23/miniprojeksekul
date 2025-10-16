import datetime
import time
total_pulsa = 0
total_Ewallet = 0
total_aksesoris = 0
totalhargacase = 0
totalhargakabel = 0
hargatotalear = 0
nominalWalletdana = 0
nominalWalletgopay = 0
nominalWalletshopee = 0
list_hp = []
list_nominalhp = []
dana_list = []
dana_nominals = []
gopay_list = []
gopay_nominals = []
shopee_list = []
shopee_nominals = []
nama_akesoris = []
jumlah_aksesoris = []
harga_aksesoris = []
total_aksesoris = []
now = datetime.datetime.now()


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
            print("ketik batal untuk membatalkan")
            no_hp = input("masukan nomor hp(12 digit): ").lower()
            if no_hp == "batal":
                break
            elif no_hp.isdigit() and len(no_hp) ==12:
                nominal_pulsa = input("masukan nominal: ")
                if nominal_pulsa.isdigit():
                    list_hp.append(no_hp)
                    nominal_pulsa = int(nominal_pulsa)
                    list_nominalhp.append(nominal_pulsa)
                    total_pulsa += nominal_pulsa
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
                namawalletdana = "Dama"
                while True:
                    print("===Dana===")
                    print("ketik batal untuk membatalkan")
                    dana = input("masukkan Nomor Dana(12digit)").lower()
                    if dana == "batal":
                        break
                    elif dana.isdigit() and len(dana) == 12:
                        while True:
                            nominalWalletdana = input("masukkan Nominal")
                            if nominalWalletdana.isdigit():
                                nominalWalletdana = int(nominalWalletdana)
                                total_Ewallet += nominalWalletdana
                                dana_list.append(dana)
                                dana_nominals.append(nominalWalletdana)
                                break
                            else:
                                print("nominal tidak valid")
                        break
                    else:
                        print("nomor tidak valid")
            elif pilihan2 == 2:
                namawalletgopay = "Gopay"
                while True:
                    print("===GoPay===")
                    gopay = int(input("masukkan Nomor Gopay"))
                    if gopay.isdigit() and len(gopay) == 12:
                        break
                    else:
                        print("nomor tidak valid")
                nominalWalletgopay = int(input("masukkan Nominal"))
                total_Ewallet += nominalWalletgopay
                gopay_list.append(gopay)
                gopay_nominals.append(nominalWalletgopay)
            elif pilihan2 == 3:
                namawalletshopee = "shopeepay"
                while True:
                    print("===ShopeePay===")
                    shopeepay = int(input("masukkan Nomor ShopeePay"))
                    if shopeepay.isdigit() and len(shopeepay) == 12:
                        nominalWalletshopee = int(input("masukkan Nominal"))
                        total_Ewallet += nominalWalletshopee
                        shopee_list.append(shopeepay)
                        shopee_nominals.append(shopee_nominals)
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
                        namatype = "Type C"
                        hargaC = 10000
                        while True:
                            typeC = int(input("beli berapa banyak"))
                            if typeC.isdigit():
                                totalhargakabel += typeC * hargaC
                                nama_akesoris.append(namatype)
                                harga_aksesoris.append(hargaC)
                                jumlah_aksesoris.append(typeC)
                                total_aksesoris.append(typeC * hargaC)
                                break
                            else:
                                print("hanya menggunakan angka")
                    elif opsikabel == 2:
                        namatype = "Type Micro Usb"
                        hargamicro = 7500
                        while True:
                            micro = input("beli berapa banyak")
                            if micro.isdigit():
                                totalhargakabel += micro * hargamicro
                                nama_akesoris.append(namatype)
                                harga_aksesoris.append(hargamicro)
                                jumlah_aksesoris.append(micro)
                                total_aksesoris.append(micro * hargamicro)
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
                    opsiEar = int(input("Pilih dari 1-4: "))
                    if opsiEar == 1:
                        namaearlow = "Low Budger Earphone"
                        hargaear = 10000
                        lowear = int(input("beli berapa banyak"))
                        hargatotalear += lowear * hargaear
                    elif opsiEar == 2:
                        namaearmid = "Mid budget Earphone"
                        hargaear = 25000
                        midear = int(input("beli berapa banyak"))
                        hargatotalear += midear * hargaear
                    elif opsiEar == 3:
                        namaearhigh = "High budget Earphone"
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
                        namacase = "Xiaomi"
                        xcase = int(input("berapa banyak yg dibeli : "))
                        hargacasex = 5000
                        totalhargacase += xcase * hargacasex
                    elif opsicase == 2:
                        namacase = "Realme"
                        hargacaser = 4500
                        rcase = int(input("berapa banyak yg dibeli : "))
                        totalhargacase += rcase * hargacaser
                    elif opsicase == 3:
                        namacase = "Iphone"
                        hargacasei = 5500
                        icase = int(input("berapa banyak yg dibeli : "))
                        totalhargacase += icase * hargacasei
                    elif opsicase == 4:
                        break
            elif pilihan3 == 4:
                break
            else:
                print("tidak ada pilihan")
    elif pilihan == 4:
        total_aksesoris = totalhargacase + totalhargakabel + hargatotalear
        total = total_aksesoris + total_Ewallet + total_pulsa
        print("=" * 10)
        print("Zhamet cell")
        print("=" * 10)
        for j in range (len(list_hp)):
            print("Pulsa", j+1, " No : ", list_hp[j], "nominal :", list_nominalhp[j])
        print("-" * 10)
        print("E-Wallet:")
        for i in range(len(dana_list)):
            print("Dana", i+1," No : ", dana_list[i], "nominal :", dana_nominals[i] )
        print("  GoPay     : ", nominalWalletgopay)
        print("  ShopeePay : ", nominalWalletshopee)
        print("-" * 10)
        print("Aksesoris:")
        print("  Kabel Data : ", totalhargakabel)
        print("  Earphone   : ", hargatotalear)
        print("  Casing HP  : ", totalhargacase)
        print("-" * 10)
        print("TOTAL        : ", total)
        print(now)
        print("=" * 10)
        print("ありがとうございました")
        break
    else:
        print("tidak ada inpit")
