class Solution:
    def frequencySort(self, s: str) -> str:
        d=dict()
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[[d[key],key] for key in d]
        l.sort(reverse=True)
        ans=[]
        for i in l:
            for j in range(i[0]):
                ans.append(i[1])
        return ''.join(ans)
