import myTextMining as tm
from myTextMining import okt_tokenizer


def main() :
    filename = input("검색 할 파일명 : ").strip()+('_news.json')
    # print(filename)
    #저장된 데이터 로딩
    dataList = tm.loadSavedData_JSON(filename, 'description')
    # 감성 분석하기
    predict_result = tm.sentimentAnalysis_ko(dataList)
    tm.visualizeSA_Text(predict_result)
    keyword = filename.split("_")[0]
    tm.visualizeSA_WordCloud(keyword, dataList, predict_result)

if __name__ == '__main__':
    main()

