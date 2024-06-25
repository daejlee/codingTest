# TC == O(n), SC == O(1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        revLst = list(str(int(a) + int(b))[::-1])
        for i in range(len(revLst) - 1):
            if int(revLst[i]) >= 2:
                revLst[i] = int(revLst[i]) - 2
                revLst[i + 1] = int(revLst[i + 1]) + 1
        if int(revLst[-1]) >= 2:
            revLst[-1] = int(revLst[-1]) - 2
            revLst.append(1)
        revLst = revLst[::-1]
        return "".join(str(x) for x in revLst)
