# coding: utf-8
import sys
import json

out_file = ".html"

test_json = {
    "str":"文字列",
    "int":1000
}

base_html = {
    "html_open":"<!DOCTYPE html><html lang='ja'>",
    "html_close":"</html>",
    "head_open":"<head>",
    "head_close":"</head>",
    "body_open":"<body>",
    "body_close":"</body>",
    "ulElement":"<ul><li>要素名</li><li>{key}</li><li>型</li><li>{type}</li><li>値</li><li>{value}</li></ul>",
    
}

def main(args):
    """main"""
    html_value_list = []
    # html固定部分body開始まで
    html_value_list.append(base_html["html_open"])
    html_value_list.append(base_html["head_open"])
    html_value_list.append(base_html["head_close"])
    html_value_list.append(base_html["body_open"])
    
    # 引数で渡されたjsonファイル読み込み
    #with open(args, encoding="utf-8") as json_file: 
    #    load_json = json.loads(json_file.read(), encoding="utf-8")
    
    # jsonの中身をulに設定
    for key in args:
        if(type(args[key]) is str):
            html_value_list.append(base_html["ulElement"].format(key=key,type="文字列",value=args[key]))
        elif(type(args[key]) is int):
            html_value_list.append(base_html["ulElement"].format(key=key,type="数値",value=args[key]))
    
    # html固定部分body終了から
    html_value_list.append(base_html["body_close"])
    html_value_list.append(base_html["html_close"])
    
    # 確認用
    for i in range(len(html_value_list)):
        print(html_value_list[i])
    #    pass
    
    # ファイル出力
    with open("outfile"+out_file, mode='w') as outFile:
        for j in range(len(html_value_list)):
            outFile.write(html_value_list[j]+"\n")

if __name__ == "__main__":
    #main(sys.argv)
    main(test_json)
