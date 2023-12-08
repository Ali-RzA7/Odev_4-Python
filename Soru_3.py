"""
•	Bir metin verildiğinde bu metini yazacak tamsayı dizisini döndürün.
•	Girilen metinin tamamı küçük harflerden oluşacağını varsayın.
•	Boşluk karakteri 0’dır.
•	Rakamlara dikkat ediniz.

Example 1:
Input: text = “mekatek”
Output: [6, [3, 3], [5, 5], 2, 8, [3, 3], [5, 5]]
Açıklama: 

Example 2:
Input: text = “a c”
Output: [2, 0, [2, 2, 2]]
Açıklama: Boşluk karakteri 0 tuşundadır.

Example 3:
Input: text = “soru 3”
Output: [[7,7,7,7], [6,6,6], [7,7,7], [8,8], 0 [3,3,3,3]]
Açıklama: 7 rakamını tuşlamak için d -> e -> f -> 3 toplamda 4 kere 3 tuşuna basılmıştır.
"""
class Soru():
    global kombinasyon
    global cevap
    cevap = []
    kombinasyon = {
        2:'abc',  3:'def',
        4:'ghi',  5:'jkl',
        6:'mno',  7:'pqrs',
        8:'tuv',  9:'wxyz'
        }
    
    def çözüm(self, kelime):
        for değer in kelime:
            self._boşluk(değer)
            self._sayı(değer)
            self._harf(değer)
        return cevap
    
    def _boşluk(self, değer):
        if değer == " ":
            cevap.append(0)
            
    def _sayı(self, sayı):
        if sayı.isdigit():
            if int(sayı) == 7 or int(sayı) == 9:
                cevap.append([int(sayı)] * 5)
            else:
                cevap.append([int(sayı)] * 4)
        
    def _harf(self, değer):
        bulunan = []
        for i in range(2,10):
            harfler = kombinasyon.get(i)
            if değer in harfler:
                if harfler.find(değer) == 0:
                    cevap.append(i)
                else:
                    for j in range(harfler.find(değer)+1):
                        bulunan.append(i)
                    cevap.append(bulunan)
                break
ob1 = Soru()
print(ob1.çözüm("mekatek"))