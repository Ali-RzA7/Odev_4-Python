"""
•	Bir m x n karakter panosu ve dizelerden oluşan bir kelime listesi verildiğinde, tahtadaki tüm kelimeleri döndürün. 
•	Her kelime, bitişik hücrelerin yatay veya dikey olarak komşu olduğu sıralı bitişik hücrelerin harflerinden oluşturulmalıdır. 
•	Aynı harf hücresi bir kelimede birden fazla kullanılamaz.
•	m == board.length
•	n == board[i].length
•	1 <= m, n <= 12
•	board[i][j] tamamı ingilizce küçük harflerden oluşmaktadır.
•	1 <= words.length <= 104
•	1 <= words[i].length <= 10
•	Words dizisi birbirini tekrarlamayan metinlerden oluşmaktadır.


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""
class Soru():
    def yol(self, pano, kelimeler):
        cevap = []
        for kelime in kelimeler:
            for i in range(len(pano)):
                for j in range(len(pano[0])):
                    if kelime[0] == pano[i][j]:
                        if self.arama(pano, kelime, i, j):
                            cevap.append(kelime)
        return cevap
    def arama(self, pano, kelime, satır, sütun, k = 0):
        if k == len(kelime):
            return True
        if satır >= len(pano) or satır < 0 or sütun >= len(pano[0]) or sütun < 0 or kelime[k] != pano[satır][sütun]:
            return False
        pano[satır][sütun] = "+"
        sonuç = self.arama(pano, kelime, satır+1, sütun, k+1) or self.arama(pano, kelime, satır-1, sütun, k+1) or self.arama(pano, kelime, satır, sütun+1, k+1) or self.arama(pano, kelime, satır, sütun-1, k+1) 
        pano[satır][sütun] = kelime[k]
        return sonuç
ob1 = Soru()
print(ob1.yol([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain", "aao", "iflvr"]))