from stanfordcorenlp import StanfordCoreNLP
from pypinyin import lazy_pinyin, Style
import pypinyin

nlp = StanfordCoreNLP(r'E:\software\stanford-corenlp-full-2018-02-27\stanford-corenlp-full-2018-02-27',lang='zh')

#输入：审核人名单（一个列表），一句话。
#输出：如果匹配到，返回匹配的名字（一个元组）；如果没匹配到，返回0；

def name_match(aditor_list,employer_sentence):
    def aditor_transform(chinese_aditor_nameList):
        pinyin_aditor_nameList = []
        for chinese_aditor_name in chinese_aditor_nameList:
            pinyin_aditor_name = tuple(lazy_pinyin(chinese_aditor_name))
            chinese_name = tuple(chinese_aditor_name)
            pinyin_aditor_name = pinyin_aditor_name + chinese_name
            pinyin_aditor_nameList.append(pinyin_aditor_name)
        #print(pinyin_aditor_nameList)
        return pinyin_aditor_nameList

    def employer_transform(sentence):
        sentence_list = nlp.ner(sentence)
        chinese_employer_nameList = []
        for nameEntity in sentence_list:
            if nameEntity[1] == 'PERSON':
                chinese_employer_nameList.append(nameEntity[0])
        pinyin_employer_nameList = []
        for chinese_employer_name in chinese_employer_nameList:
            pinyin_employer_name = tuple(lazy_pinyin(chinese_employer_name))
            pinyin_employer_nameList.append(pinyin_employer_name)

       # print(pinyin_employer_nameList)
        return pinyin_employer_nameList

    def minDistance(words1, words2):
        m = len(words1)
        n = len(words2)
        if m == 0:
            return n
        if n == 0:
            return m
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): dp[i][0] = i
        for j in range(1, n + 1): dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if words1[i - 1] == words2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        # print(dp)
       # print(dp[m][n])
        return dp[m][n]
    aditors=aditor_transform(aditor_list)
    employers=employer_transform(employer_sentence)
    for aditor in aditors:
        for employer in employers:
            #print("jin ru  shuang xun huan")
            #print(len(aditor))
            #print(len(employer))
            if (len(aditor)/2)!=len(employer):
                #print("name bu deng chang")
                continue
            else:
                distance=0
                for index in range(0,len(employer)):
                     distance=distance+minDistance(aditor[index],employer[index])
                     #我的print(distance)
                if distance<len(employer):
                    return aditor[len(employer):]
    return 0



Aditor=['赵冬月','崔宝亮','张亚伟','张玉岚','吴学哲']
s=input()
result=name_match(Aditor,s)
if result==0:
    print("没找到.")
else:
    print(result)


nlp.close()