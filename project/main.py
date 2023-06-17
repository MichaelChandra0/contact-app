import time
import os
import json
from settings import Settings

class PeriodicTable:
    
    def __init__(self):
        self.active = True

    def clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def welcome(self):
        self.clear_screen()
        print("Tabel Periodik")

    def run(self):
        self.welcome()
        self.menu()
        self.pilihan()

    def menu(self):
        print("1. Melihat tabel.\n2. Mengubah Tabel.\n3. Mencari element.\n4. Menghapus Element.\n5. Menambah Element.\nq. Quit.")


    def pilihan(self):
        pilihan = input("Mauskkan Pilihan : ")
        if pilihan == "1":
            self.clear_screen()
            tabel = self.settings.elements
            print("Melihat Tabel Periodik")
            print(f"Nama Element:\t\tNomor Atom:\t\tGolongan:\t\tPeriode:")
            for nama, info in tabel.items():
                print(f"{nama}\t\t{info['Nomor atom'].title()}\t\t{info['Golongan'].title()}\t\t{info['Periode'].title()}")


        elif pilihan == "2":
            pass
        elif pilihan == "3":
            pass
        elif pilihan == "4":
            pass
        elif pilihan == "5":
            pass
        elif pilihan.lower() == "q":
            keluar = input("Apakah kamu yakin ingin keluar ? (y/n)")
            if keluar.lower() == "y":
                print("Program akan ditutup dalam 2 detik")
                time.sleep(2)
                self.clear_screen()
            elif keluar.lower() == "n":
                PeriodicTable().run()
            else:
                PeriodicTable().run()
                
                
                
            

PeriodicTable().run()
    


        
        