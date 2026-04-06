class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dic={}
        window_dic={}
        if len(s1)>len(s2):
            return False
        for r in range (len(s1)):
            s1_dic[s1[r]] =s1_dic.get(s1[r],0)+1
            window_dic[s2[r]]=window_dic.get(s2[r],0)+1
        if s1_dic==window_dic:
            return True
        for r in range (len(s1),len(s2)):
            window_dic[s2[r]]=window_dic.get(s2[r],0)+1
            window_dic[s2[r-len(s1)]]-=1
            if window_dic[s2[r-len(s1)]] == 0: del window_dic[s2[r-len(s1)]]
            if s1_dic==window_dic:
                return True
        return False


        