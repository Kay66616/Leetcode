class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        for num in str(n):
            sum += int(num)
            product *= int(num)
        return product-sum
