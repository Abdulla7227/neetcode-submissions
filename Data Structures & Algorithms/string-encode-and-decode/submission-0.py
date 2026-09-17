class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s

        return encoded 

    def decode(self, s: str) -> List[str]:

        decoded = []
        start = 0

        while start < len(s):
            delimiter = s.find("#", start)
            length = int(s[start:delimiter])

            word = s[delimiter + 1 : delimiter + 1 + length]
            decoded.append(word)

            start = delimiter + 1 + length

        return decoded
