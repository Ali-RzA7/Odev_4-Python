"""
•	Bir tamsayı dizisi verildiğinde, tüm üçlüleri [sayılar[i], sayılar[j], sayılar[k]] döndürün; öyle ki i != j, i != k ve j != k ve sayılar[i] + sayılar[j] + sayılar[k] == 0. 
•	Çözüm kümesinin yinelenen üçlüler içermemesi gerektiğine dikkat edin.
•	3 <= nums.length <= 3000
•	-105 <= nums[i] <= 105
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Açıklama: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
Farklı üçlüler [-1,0,1] ve [-1,-1,2]'dir.
Çıkış sırasının ve üçlülerin sırasının önemli olmadığına dikkat edin.

Example 2:
Input: nums = [0,1,1]
Output: []
Açıklama: Mümkün olan tek üçlünün toplamı 0'a eşit değildir.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
"""
class Soru():
    def bulma(self, liste):
        liste.sort()
        cevap = []

        for i in range(len(liste)-2):
            if liste[i] > 0:
                break
            if i > 0 and liste[i] == liste[i-1]:
                continue
            j = i + 1
            k = len(liste) - 1
            while j < k:
                toplam = liste[i] + liste[j] + liste[k]
                if toplam < 0:
                    j += 1
                elif toplam > 0:
                    k-=1
                else:
                    sayılar = [liste[i], liste[j], liste[k]]
                    cevap.append(sayılar)
                    while (j < k) and (liste[j] == liste[j+1]):
                        j += 1
                    while j < k and liste[k] == liste[k-1]:
                        k-=1
                    j += 1
                    k -= 1
        return cevap
obj1 = Soru()
print(obj1.bulma([-1,0,1,2,-1,-4]))