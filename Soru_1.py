"""
•	Bir tamsayı dizisi ve bir tamsayı hedef verildiğinde, iki sayının indekslerini, toplamları hedefe eşit olacak şekilde döndürün. 
•	Her girdinin tam olarak bir çözümü olacağını varsayabilirsiniz ve aynı öğeyi iki kez kullanamazsınız.
•	Cevabı istediğiniz sırayla geri verebilirsiniz.
•	    2 <= nums.length <= 104
•	    -109 <= nums[i] <= 109
•	    -109 <= target <= 109

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Açıklama: nums[0] + nums[1] == 9, olduğu için çıktı [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
"""
class Soru():
    def Toplam(self, liste, sayı):
        for i in range(len(liste)):
            for j in range(i+1, len(liste)):
                if((i != j) and (liste[i]) + liste[j] == sayı):
                    return [i, j]
        return []
cevap = Soru()
print(cevap.Toplam([2,7,11,15], 9))