def tampilkan_menu():
    print("=== Menu Top-Up Game ===")
    print("1. Top-Up 10.000")
    print("2. Top-Up 25.000")
    print("3. Top-Up 50.000")
    print("4. Top-Up 100.000")
    print("0. Keluar")

def pilih_metode_pembayaran():
    print("\nPilih Metode Pembayaran:")
    print("1. Transfer Bank")
    print("2. E-Wallet")
    print("3. Pulsa")
    metode = input("Masukkan pilihan metode pembayaran (1-3): ")
    metode_dict = {
        "1": "Transfer Bank",
        "2": "E-Wallet",
        "3": "Pulsa"
    }
    return metode_dict.get(metode, None)

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan top-up: ")

        nominal_dict = {
            "1": 10000,
            "2": 25000,
            "3": 50000,
            "4": 100000
        }

        if pilihan == "0":
            print("Terima kasih telah menggunakan layanan top-up.")
            break

        nominal = nominal_dict.get(pilihan, None)
        if nominal is None:
            print("Pilihan tidak valid, silakan coba lagi.\n")
            continue

        metode = pilih_metode_pembayaran()
        if metode is None:
            print("Metode pembayaran tidak valid, silakan coba lagi.\n")
            continue

        print(f"\nTop-up sebesar Rp{nominal:,} berhasil melalui {metode}.")
        print("Terima kasih telah melakukan top-up!\n")

if __name__ == "__main__":
    main()
