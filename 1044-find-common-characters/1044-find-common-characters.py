class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        output=[]

        for i in range(len(words[0])):
            bool=True
            for j in range(1,len(words)):
            
                if words[0][i] not in words[j]:
                    bool=False
                    break
            if bool == True:
                output.append(words[0][i])
                temp=words[0][i]
                for k in range(len(words)):
                    
                    words[k]=words[k].replace(temp,"*",1)
                    
        return output