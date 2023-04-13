class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        n = len(strs)
        res = str(n)
        for s in strs:
            res += "alus" + s
        # print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = s.split("alus")
        res = []
        for i in range(1, int(strs[0]) + 1):
            res.append(strs[i])
        # print(res)
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))