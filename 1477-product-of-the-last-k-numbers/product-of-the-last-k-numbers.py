class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.pre = []
        
    def add(self, num: int) -> None:
        self.arr.append(num)
        if num == 0:
            self.pre = []
        elif len(self.pre) == 0:
            self.pre.append(num)
        else:
            self.pre.append(self.pre[-1] * num)
        
        # print("prefix arr: ", self.pre)

        
        
    def getProduct(self, k: int) -> int:

        lenPre = len(self.pre)
        left = (lenPre-1) - k
       
        # print("---")
        # print("k : ", k)
        # print("self.pre : ", self.pre)
        # print("self.arr : ", self.arr)

        if k > lenPre:
            # print(" 0 ")
            return 0
        if k == lenPre:
            return self.pre[-1]
            # print("last element : ", self.pre[-1])
        right = (lenPre-1)
        # print("left and right : ", left, right)
        # print("answer : ", self.pre[lenPre-1] // self.pre[left])

        return self.pre[right] // self.pre[left]
