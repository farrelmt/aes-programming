import logging
import os
import socket
import time
import datetime


def get_targets():
    targets = dict()
    targets[
        'rec1'] = '127.0.0.1'
    # Line diatas bisa diganti ke IP Target kalau Beda PC
    return targets


def send_file(ip):
    waktu_awal = datetime.datetime.now()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    namafile = "bart.png"
    ukuran = os.stat(namafile).st_size

    fp = open('bart.png', 'rb')
    k = fp.read()
    # variabel k diencrpyt disini baru dikirim
    terkirim = 0
    for x in k:
        k_bytes = bytes([x])
        # Setting Port disini
        sock.sendto(k_bytes, (ip, 5025))
        terkirim = terkirim + 1
        print(k_bytes, f"terkirim {terkirim} of {ukuran} ")
    waktu_process = datetime.datetime.now() - waktu_awal
    waktu_akhir = datetime.datetime.now()
    logging.warning(f"writing {namafile} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")