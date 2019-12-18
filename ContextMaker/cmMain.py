# coding:utf-8
import sys
import ContextMaker as cm

def main(args):
    """メイン"""
    # コンテキスト生成
    #me = cm.ContextMaker(args)
    me = cm.ContextMaker("sample.json")
    ctx = me.getContext("name1")
    
    # コンテキストからアドオン取得
    addon = ctx.getAddon02()
    # アドオン適用
    print(ctx.addonPush(addon, "add_on_name_01", 0))

if __name__ == "__main__":
    main(sys.argv)
