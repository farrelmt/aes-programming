from library import get_targets,send_file
import time
import datetime
import threading




def send_semua():
    texec = dict()
    targets = get_targets()

    catat_awal = datetime.datetime.now()
    for k in targets:
        print(f"mengirim ke {k} di {targets[k]}")
        # waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi send gambar secara multithread
        texec[k] = threading.Thread(target=send_file, args=(targets[k],))
        texec[k].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in targets:
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    send_semua()