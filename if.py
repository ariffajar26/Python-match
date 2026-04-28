 while True :
    kode = input("masukan kode barang : ")

    match kode :
        case "A01" :
            print("nama barang : Snack")
            print("harga : 10000")
        case "A02" :
            print("nama barang : Minuman")
            print("harga : 8000")
        case "B01" :
            print("nama barang : mie instan")
            print("harga : 3000")
        case "B02" :
            print("nama barang : Sabun")
            print("harga : 5000")
        case "C01" :
            print("nama barang : shampoo")
            print("harga : 12000")
        case "keluar" :
            print("terimakasih")
            break
        case _ :
            print("kode tidak ada")