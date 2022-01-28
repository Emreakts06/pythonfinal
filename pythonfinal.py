db = pymysql.connect(host='localhost',
                             user='yemeginiadi',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
yemek= db.cursor()

yemek = yemekk.execute('INSERT INTO kullanicilar VALUES()',())
db.commit()

print(str(yemek) + " yemek tarifi eklendi")

sonuc = yemek.execute('UPDATE kullanicilar SET yas = %s WHERE id = %s',())
db.commit()

print(str(yemek) + " yemek güncellendi")

sonuc = baglanti.execute('DELETE FROM kullanicilar WHERE id = %s',(1,))
db.commit()

print(str(yemek) + " yemek tarifi silindi")
