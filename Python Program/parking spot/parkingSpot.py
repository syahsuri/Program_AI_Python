class kendaraan:
    def __init__(self, nomor_plat, merek, warna):
        self.nomor_plat = nomor_plat
        self.merek = merek
        self.warna = warna

    def __repr__(self):
        return f'{self.nomor_plat},{self.merek},{self.warna}'

class TempatParkir:
    def __init__(self):
        self.Tambah_mobil = []
        self.spot = 20
        self.mobil_info = {}
        self.tagihan = 0

    def tempat_yang_tersedia(self):
        return f'Tempat Parkir Yang Tersedia : {self.spot}'

    def add_car(self, mobil):
        
        self.identifikasi = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1',
                            'K1','L1','M1','N1','O1','P1','Q1','R1','S1','T1']

        if self.spot > 0 :
            self.Tambah_mobil.append(str(mobil).split(', '))
            self.spot -= 1
            self.mobil_info = {'code': [], 'nomor lisensi': [], 'merek': [], 'Warna': []}

            for index, i in enumerate(self.Tambah_mobil):
                self.mobil_info['code'].append(self.identifikasi[index])
                self.mobil_info['nomor lisensi'].append(i[0])
                self.mobil_info['merek'].append(i[1])
                self.mobil_info['warna'].append(i[2])
            return "Kendaraan Berhasil Diparkir"
        
        else:
            print(f"Mohon Maaf Parkir Yang Tersedia Saat ini {self.spots}")
        
    def remove_mobil(self, given_code, tagihan_perjam):
          past_len = len(self.mobil_info['code'])

          if given_code not in self.mobil_info['code']:
            print("Mobil Tidak ditemukan !!")

          else:
            for index, value in enumerate(self.mobil_info['code']):
                if value == given_code:  
                 print("Nomor Plat Mobil:", self.mobil_info['nomor Plat'][index])
                 print("Merek Mobil:", self.mobil_info['merek'][index])
                 print("Warna mobil :", self.mobil_info['warna'][index])

                removed_car_index = self.mobil_info['code'].pop(index)
                self.mobil_info['nomor plat'].pop(index)
                self.mobil_info['merek'].pop(index)
                self.mobil_info['warna'].pop(index)

                self.spots += 1
            
            if len(self.mobil_info['code']) < past_len:
                while True:
                       
                     if tagihan_perjam.isnumeric():
                         
                        list_of_time_and_code = [tagihan_perjam, removed_car_index]
                        break
                    
                     else:
                        print("Your input must be an integer. Sample input: 5 ")
                    
                        tagihan_perjam = input("Berapa jam anda akan parkir ? or 'q' to quit. Example input: 5  -->  ")
                    
                     if tagihan_perjam in ['q', 'Q']:
                        break

                if int(list_of_time_and_code[0]) < 20:
                    self.tagihan = int(list_of_time_and_code[0]) * 5
                    return f'Total Tagihan ${self.tagihan}'
            
                else:
                    self.tagihan = int(list_of_time_and_code[0]) * 5 + 100
                    return f'Total Tagihan ${self.tagihan}'

def kendaraan_ditempat_parkiran(self):
            for i in self.mobil_info.items():
                print(i)

Parking_spot = TempatParkir()
print(Parking_spot.tempat_yang_tersedia())
Parking_spot.add_car(kendaraan('LVG34', 'Ferrari', 'Red'))







