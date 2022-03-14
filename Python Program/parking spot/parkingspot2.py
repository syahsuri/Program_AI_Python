class kendaraan:

    def __init__(self, no_plat, merek, warna):
        self.no_plat = no_plat
        self.merek = merek
        self.warna = warna

    def __repr__(self):
        return f'{self.no_plat}, {self.merek}, {self.warna}'

class tempat_parkir:
    
    def __init__(self):
        self.mobil_bertambah = []
        self.tempat = 20
        self.info_kendaraan = {}
        self.tagihan = 0

    def spots_available(self):
        print(f"\nParkir Yang Tersedia Saat ini :") 
        return self.tempat

    def add_car(self, car):

        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1',
                        'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']

        if self.tempat > 0:

            self.mobil_bertambah.append(str(car).split(', '))

            self.tempat -= 1

            self.info_kendaraan = {'code': [], 'license plate': [], 'Model': [], 'Color': []}

            for index, i in enumerate(self.mobil_bertambah):
                
                self.info_kendaraan['code'].append(self.identifier[index])
                self.info_kendaraan['license plate'].append(i[0])
                self.info_kendaraan['Model'].append(i[1])
                self.info_kendaraan['Color'].append(i[2])
            return "car successfully added to the parking lot"

        else:
            print(f"We have {self.tempat} spots available. I am sorry ")

    def remove_car(self, given_code, bill_hours):

        past_len = len(self.info_kendaraan['code'])

        if given_code not in self.info_kendaraan['code']:
            print("We could not find your car. Are you sure you parked your car here? ")

        else:
            for index, value in enumerate(self.info_kendaraan['code']):
                if value == given_code:

                    print("\nNomor Plat Mobil:", self.info_kendaraan['license plate'][index])
                    print("Merek Mobil:", self.info_kendaraan['Model'][index])
                    print("Warna mobil :", self.info_kendaraan['Color'][index])

                    removed_car_index = self.info_kendaraan['code'].pop(index)
                    self.info_kendaraan['license plate'].pop(index)
                    self.info_kendaraan['Model'].pop(index)
                    self.info_kendaraan['Color'].pop(index)

                    self.tempat += 1

        if len(self.info_kendaraan['code']) < past_len:
            while True:

                if bill_hours.isnumeric():

                    list_of_time_and_code = [bill_hours, removed_car_index]
                    break

                else:
                    print("Your input must be an integer. Sample input: 5 ")

                bill_hours = input("Enter for how long you were on the parking lot in hours or 'q' to quit. Example input: 5  -->  ")

                if bill_hours in ['q', 'Q']:
                    break

            if int(list_of_time_and_code[0]) > 1:
                self.bill = int(list_of_time_and_code[0]) * 1500
                return f'Tagihan Anda adalah Rp.{self.bill}'
 
            else:
                self.tagihan = int(list_of_time_and_code[0]) * 50 + 10
                return f'Tagihan Anda adalah Rp.{self.tagihan}'

    def cars_in_parkspot(self):
            for i in self.info_kendaraan.items():
                print(i)



parking_spot = tempat_parkir()
print(parking_spot.spots_available())
parking_spot.add_car(kendaraan('BL245', 'Avanza', 'Hitam'))
parking_spot.add_car(kendaraan('BK478', 'Kijang', 'Putih'))
parking_spot.add_car(kendaraan('BL567', 'Vario', 'Merah Hitam'))
parking_spot.cars_in_parkspot()
print(parking_spot.remove_car('A1', '5'))
print(parking_spot.spots_available())