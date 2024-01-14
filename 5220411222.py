#ACEP SAEPULOH FATAH
#5220411222

import mysql.connector
import os
import datetime
from random import random
from prettytable import PrettyTable
import time



class KursusProgram:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="data_kursus"
        )
        self.cursor = self.db.cursor()

    def menu_kursus(self):
        print("---------------------------------------------------------")
        print("|===================== menu kursus =====================|")
        print("---------------------------------------------------------\n")
        lanjut = True
        while lanjut:
            print("--------------------------------------------------------")
            print("=> Daftar Menu \n")
            print(" 1. Daftar kursus")
            print(" 2. Daftar pendaftar")
            print(" 3. Pembayaran")
            print(" 4. Cari data pendaftar")
            print(" 5. Hapus pendaftaran")
            print(" 0. Keluar\n")
            print("--------------------------------------------------------\n")
            pilih = int(input("Menu yang anda pilih 1/2/3/4/5/0 ? : "))
            os.system('cls')
            if pilih == 1:
                print()
                self.daftar()
            elif pilih == 2:
                print()
                self.lihat_pendaftar()
            elif pilih == 3:
                print()
                self.transaksi()
            elif pilih == 4:
                print()
                self.cari_data()
            elif pilih == 5:
                print()
                self.hapus()
            elif pilih == 0:
                exit()
            else:
                lanjut = False
                break

    def daftar(self):
        id = 3
        kursus = ["Data Scientist      ", "Software Development", "Web Development     "]
        biaya = ["2.000.000", "1.500.000", "1.250.000"]

        print("""
============== daftar kursus =============""")
        print("""
==========================================
|  id  |       kursus        |   biaya   |
==========================================""")
        for v in range(id):
            kolom_1 = str(v + 1)
            kolom_2 = str(kursus[v])
            kolom_3 = str(biaya[v])

            print('| ' + kolom_1 + (5 - len(kolom_1)) * ' '
                + '| ' + kolom_2 + (11 - len(kolom_2)) * ' '
                + '| ' + kolom_3 + (10 - len(kolom_3)) * ' ' + '|')
        print("==========================================")
        print()
        print()

        nama = input("nama pendaftar: ")
        jenis = input("jenis kursus: ")
        biaya = int(input("biaya: "))

        if biaya <= 2000000:
            print()
            print("pendaftaran berhasil diproses ! \n")
        else:
            print()
            print("pendaftaran gagal ! \n")

        sql = "INSERT INTO pendaftar (nama, jenis_kursus, biaya) VALUES (%s,%s, %s)"
        values = [
            (nama, jenis, biaya)
        ]

        for val in values:
            self.cursor.execute(sql, val)
            self.db.commit()
        
        self.loading()

    def lihat_pendaftar(self):
        select_query = "SELECT * FROM pendaftar"
        self.cursor.execute(select_query)
        result = self.cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["No", "Nama pendaftar", "Jenis Kursus", "Biaya", "Status"]

        for row in result:
            table.add_row([row[0], row[1], row[2], row[3], row[4]])

        print("\n      --------    Data Pendaftaran   -------".center(36))
        print(table)

    def transaksi(self):
        lanjut = True
        while lanjut:
            self.lihat_pendaftar()
            print(48 * "=")
            keyword = input("masukan data nama: ")
            print(48 * "=")
            os.system('cls')
            sql = "SELECT * FROM pendaftar WHERE  no LIKE %s OR nama LIKE %s OR jenis_kursus LIKE %s OR biaya LIKE %s OR status_pembayaran LIKE %s "
            val = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
            self.cursor.execute(sql, val)
            results = self.cursor.fetchall()

            if self.cursor.rowcount < 0:
                print("mohon maaf data itu tidak ada")
            else:
                table = PrettyTable()
                table.field_names = ["ID", "Nama", "Jenis Kursus", "Biaya", "Status"]
                
                for data in results:
                    table.add_row(data)
                
                print(table)
                self.db.commit()

            print(48 * "-")
            print(" Inputan Data ".center(48, "="))
            np = input("nama pendaftar: ")
            jenis = input("jenis kursus: ")
            biaya = int(input("biaya: "))
            uang = int(input("Masukan jumlah uang : "))
            hutang = uang - biaya
            kembalian = uang - biaya
            n = 1
            while n == n:
                break
            for i in range(n):
                bil = random() % 0.5
            print()
            print()
            
            self.loading()
            status_pembayaran = 'Belum Bayar'
            
            if uang == biaya:
                print(48 * "=")
                print("---------------Transaksi berhasil---------------")
                print("|""nama                          :", np)
                print("|""jenis kursus                  :", jenis)
                print("|""Uang                          : Rp.", uang)
                print("|""biaya                         : Rp.", biaya)
                print(48 * "_")
                print("|""refund                        : Rp. 0", 0)
                print(48 * "=")
                status_pembayaran = 'Sudah Bayar'
                print("|""Kode Transaksi: ", bil)
                print(48 * "=")
                print(datetime.datetime.now())
                print(48 * "=")
                keluar = input("Lanjut transaksi ? y / n : ")
                print(48 * "=")
                if keluar == "y":
                    lanjut
                else:
                    lanjut = False
                    break
                os.system('cls')
            elif uang < biaya:
                print(48 * "=")
                print("--------------Transaksi dibatalkan---------------")
                print("|""nama                          :", np)
                print("|""jenis kursus                  :", jenis)
                print("|""Uang                          : Rp.", uang)
                print("|""biaya                         : Rp.", biaya)
                print(48 * "_")
                print("|""uang kurang                   : Rp.", hutang)
                print(48 * "=")
                status_pembayaran = 'Belum Bayar'
                print("|""Kode Transaksi: ", bil)
                print(48 * "=")
                print(datetime.datetime.now())
                print(48 * "=")
                keluar = input("Lanjut transaksi ? y / n : ")
                print(48 * "=")
                if keluar == "y":
                    lanjut
                else:
                    lanjut = False
                    break
                os.system('cls')
            elif uang > biaya:
                print(48 * "=")
                print("---------------Transaksi berhasil---------------")
                print("|""nama                          :", np)
                print("|""jenis kursus                  :", jenis)
                print("|""Uang                          : Rp.", uang)
                print("|""biaya                         : Rp.", biaya)
                print(48 * "_")
                print("|""refund                        : Rp.", kembalian)
                print(48 * "=")
                status_pembayaran = 'Sudah Bayar'
                print("|""Kode Transaksi: ", bil)
                print(48 * "=")
                print(datetime.datetime.now())
                print(48 * "=")
                print()
                keluar = input("Lanjut transaksi ? y / n : ")
                print(48 * "=")
                if keluar == "y":
                    lanjut
                else:
                    lanjut = False
                    break
            
            update_query = "UPDATE pendaftar SET status_pembayaran = %s WHERE nama = %s"
            update_values = (status_pembayaran, np)
            self.cursor.execute(update_query, update_values)
            self.db.commit()
            os.system('cls')

    def cari_data(self):
            keyword = input("Data yang dicari: ")
            sql = "SELECT * FROM pendaftar WHERE nama LIKE %s OR jenis_kursus LIKE %s OR biaya LIKE %s "
            val = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
            self.cursor.execute(sql, val)
            results = self.cursor.fetchall()

            self.loading()
            if self.cursor.rowcount < 0:
                print("mohon maaf data itu tidak ada")
            else:
                table = PrettyTable()
                table.field_names = ["ID", "Nama", "Jenis Kursus", "Biaya", "Status"]
                
                for data in results:
                    table.add_row([data[0], data[1], data[2], data[3], data[4]])

                print(table)
                self.db.commit()


    def hapus(self):
        print("--------------------------------------------------------")
        print("|================= hapus pendaftaran ==================|")
        print("--------------------------------------------------------\n")
        self.lihat_pendaftar()
        print()
        pilih = input("Masukan nama pendaftar : ")
        jml = len(pilih)
        if jml <= 10:
            print()
            print("data sedang diproses ! \n")
        else:
            print()
            print("tidak ada data, digagalkan !\n")
        print()
        sql = "DELETE FROM pendaftar WHERE nama=%s"
        values = (pilih,)
        self.cursor.execute(sql, values)

        self.db.commit()
        self.loading()
        
    def loading(self):
        print("Loading...", end='', flush=True)
        animation = "|/-\\"
        for i in range(25):
            time.sleep(0.1)
            print(f"\b{animation[i % len(animation)]}", end='', flush=True)
        print("\b Berhasil!")


if __name__ == "__main__":
    kursus_program = KursusProgram()
    while True:
        kursus_program.menu_kursus()
        os.system('cls')
