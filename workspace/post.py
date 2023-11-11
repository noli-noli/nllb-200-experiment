import requests


#サーバURL
url = "http://133.89.44.4:"

#ポート番号
port = "49152"

#言語コード
lang_code = "eng_Latn"

#最大生成トークン数
max_length = 10000



def main():
    text = input("Please input text: ")
    if text == "":
        text = """昨今の大規模言語モデルの進化は凄まじく早い。約1ヶ月毎に新しいモデルが公開されている。また、それらを動かす為の条件も非常に厳しく定義されており、最新のGPGPUが無いと動作不可能等ざらである。"""
    #textに翻訳したい文章を入れる
    try:
        response = requests.get(url + port + "/items/?text=" + text + "&lange_code=" + lang_code + "&max_length=" + str(max_length))
        print("response text: " + response.text)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
