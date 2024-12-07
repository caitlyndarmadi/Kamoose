for i in range(5):
    meme_dict = {
                "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
                "LOL": "Tanggapan umum terhadap sesuatu yang lucu", 
                "ROFL" : "tanggapan terhadap lelucon",
    "SHEESH" : "sedikit ketidaksetujuan",
    "CREEPY" : "menakutkan, tidak menyenangkan",
    "AGGRO" : "untuk menjadi agresif/marah", 
                }
    print("Halo, selamat datang ke kamus kodland!")
    word = input("Ketik kata yang tidak Kamu mengerti:").upper()
    if word in meme_dict.keys():
        print("Arti dari", word, "adalah:", meme_dict[word])
    else:
        print("Maaf, kata", word, "tidak ditemukan dalam kamus.")
