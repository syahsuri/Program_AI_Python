num_items = 0
total_amount = 0
amount = int (input("Masukan Harga Belanjaan = Rp."))

while amount != -1:
    num_items += 1
    total_amount += amount
    amount = int (input("Masukan Harga Belanjaan = Rp."))

if num_items == 0:
    print("Kamu tidak membeli apa apa . Selamat Tinggal")
else:
    print("Total Harga untuk ",num_items , "Barang Adalah Rp", total_amount)
    payment = int(input("Masukan Uang Pembayaran  Rp."))
    kembalian = payment - total_amount
    print("Terima Kasih Telah Berbelanja . Kembalianya Rp.",kembalian)

uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
jumlah_pecahan = {}
sisa = kembalian
print('\nInput uang {},  Pecahan yang kita butuhkan yaitu: '.format(kembalian))
for pecahan in uang_pecahan:
    if sisa < pecahan:
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - ( pecahan * banyak_pecahan )
    print('pecahan {} : {}'.format(pecahan, banyak_pecahan),' Lembar')