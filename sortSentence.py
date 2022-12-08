class Solution:
    def sortSentence(self, s: str) -> str:
        words = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        s = s.replace(" ", "")
        begin = 0
        for i in range(len(s)):
            try:
                j = int(s[i]) - 1
                words[j] = s[begin: i]
                begin = i + 1
            except:
                continue
        ind = 0
        sent = ""
        while ind < len(words) and words[ind] != 0:
            sent += words[ind]
            sent += " "
            ind += 1
        sent = sent[:len(sent) - 1]
        return sent
