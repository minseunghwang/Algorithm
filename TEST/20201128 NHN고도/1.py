class Solution:
    def solution(self, goods):
        s = 0
        tmp = 0
        for i in range(len(goods)):
            if goods[i] < 50:
                tmp += goods[i]
                if tmp >= 50:
                    s += (tmp - 10)
                    tmp = 0
            else:
                s += (goods[i] - 10)
        s += tmp

        return s