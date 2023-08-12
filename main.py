from db import setup, save_movie, get_all_movie

con, cur = setup()

#res = cur.execute("SELECT name FROM sqlite_master")
#print(res.fetchall())

# ambil inputan dari user
title = input("Masukkan judul movie : ")
year = int(input("Masukkan tahun movie: "))
score = float(input("Masukkan score movie : "))

save_movie(title, year, score)

get_all_movie()
