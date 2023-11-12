import requests


#サーバURL
url = "http://133.89.44.20:"

#ポート番号
port = "49152"

#翻訳元の言語コード
input_code = "jpn_Jpan"

#翻訳先の言語コード
output_code = "eng_Latn"

#最大生成トークン数(MAX=1000がおススメ)
max_length = 2000



def main():
    #text = input("Please input text: ")
    #if text == "":
    text = """一気に寒くなった。
布団が私を離してくれない。"""
    #textに翻訳したい文章を入れる
    try:
        response = requests.get(url + port + "/items/?text=" + text + "&input_code=" + input_code + "&output_code=" + output_code + "&max_length=" + str(max_length) )
        print("input text:" + text.replace("\n",""))
        print("response text: " + response.text)
    except Exception as e:
        print("Error: ", e)



if __name__ == "__main__":
    main()
