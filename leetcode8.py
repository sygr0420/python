class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        a = 0
        str1 = []
        str2 = ""
        the_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for i in range(0, len(str)):
            if str[i] == " ":
                if str1==[]:
                    continue
                else:
                    break
            elif str[i] == "-":
                if str1==[]:
                    a = 1
                else:
                    break
            elif str[i] == "+":
                if str1==[]:
                    a = 2
                else:
                    break
            elif str[i] in the_list:
                str1.append(str[i])
            else:
                break


        if str1==[]:
            return 0
        else:
            if a == 0 or a == 2:
                if  (-2) ** 31 <= int(str2.join(str1)) <=2 ** 31 - 1:
                    return int(str2.join(str1))
                else:
                    return  (2 ** 31)-1
            if a == 1:
                 if (-2) ** 31 <= int(str2.join(str1)) <=2 ** 31 - 1:
                    return -int(str2.join(str1))
                 else:
                    return (-2) ** 31
a=Solution()
print(a.myAtoi("-42"))