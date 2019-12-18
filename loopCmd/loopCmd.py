# coding:utf-8
# jsonを読み込んで関数生成
import os
import json

py_path = os.getcwd() + "\\" # py実行ディレクトリ
app_path = "loopCmd\\" # アプリ名
resource_path = "resource.json" # resourceファイル名
jsons = {} # jsonfile格納用
actionList = [] # 関数リスト
resultExecute = [] # 実行結果

def readFile(_arg1, _arg2):
    u"""jsonファイル読込
    _arg1 = py実行ディレクトリ+アプリ名
    _arg2 = 取得対処ファイル名(場合によってディレクトリ階層追加)
    return = json
    """
    loadjson = {}
    with open(_arg1 + _arg2, encoding="utf-8") as openjson:
        loadjson = json.loads(openjson.read(), encoding="utf-8")

    return loadjson

def readFileAll(_arg1, _arg2):
    u"""resource.jsonに記載された全ファイル読込
    _arg1 = py実行ディレクトリ+アプリ名
    _arg2 = resourceファイル名
    return = json
    """
    openjson = {} # ファイル読込用
    loadjson = {} # json格納用

    # resourceファイル取得
    with open(_arg1 + _arg2, encoding="utf-8") as openjson:
        loadjson["resource"] = json.loads(openjson.read(), encoding="utf-8")
    # resourceファイルに設定したファイル分繰り返し
    for key in loadjson["resource"]:
        with open(_arg1 + loadjson["resource"][key]["path"] + loadjson["resource"][key]["name"]
        + loadjson["resource"][key]["type"], encoding="utf-8") as openjson:
            loadjson[key] = json.loads(openjson.read(), encoding="utf-8")

    return loadjson

def addBlank(_arg1, _arg2):
    u"""半角ブランクを追加
    _arg1 = 文字列
    _arg2 = s:先頭, e:末尾, se:前後
    return = 文字列
    """
    if("s"==_arg2):
        return " " + _arg1
    elif("e"==_arg2):
        return _arg1 + " "
    elif("se"==_arg2):
        return " " + _arg1 + " "
    else:
        return _arg1

def printStr(_arg):
    u"""文字列出力
    _arg = 辞書
    return = 文字列
    """
    # モードで処理分岐
    if(_arg["mode"] == "nomal"):
        print(_arg["value"])
    elif(_arg["mode"] == "list"):
        for i in _arg["value"]:
            print(i)
    return "printStr(" + _arg["mode"] + "):" + _arg["name"]

def calculation(_arg):
    u"""計算
    _arg = 辞書
    return = 文字列
    """
    # モードで処理分岐
    if(_arg["mode"] == "plus"):
        print("足し算:",format(sum(_arg["value"])))
    elif(_arg["mode"] == "minus"):
        print("引き算:",format(sum(_arg["value"])))
    return "calculation(" + _arg["mode"] + "):" + _arg["name"]

def setAction(_arg):
    u"""関数セット
    _arg = 辞書
    return = list
    """
    actions = []
    for key in _arg:
        if(_arg[key]["action"] == "printStr"):
            wk = {}
            wk["action"] = printStr
            wk["arg"] = _arg[key]
            actions.append(wk)
        elif(_arg[key]["action"] == "calculation"):
            wk = {}
            wk["action"] = calculation
            wk["arg"] = _arg[key]
            actions.append(wk)
    
    return actions

def execute(_arg):
    u"""関数リストを順次実行
    _arg = 関数リスト
    return = list
    """
    resultset = []
    for i in _arg:
        resultset.append(i["action"](i["arg"]))

    return resultset

def main():
    u"""メイン処理"""
    global jsons
    global actionList
    global resultExecute
    
    print("main:start")
    # ファイル取得
    jsons = readFileAll(py_path + app_path, resource_path)
    # 関数セット
    actionList = setAction(jsons["target"])
    # 関数実行
    resultExecute = execute(actionList)

    print(resultExecute)
    print("main:end")

if __name__ == "__main__":
    main()