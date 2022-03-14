from distutils.util import change_root


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
    print("Total Harga untuk ", num_items , "Adalah Rp", total_amount)
    payment = int(input("Masukan Uang Pembayaran Rp."))
    change = payment - total_amount
    print("Terima Kasih Telah Berbelanja . Kembalianya Rp.", change)