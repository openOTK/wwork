# coding:utf-8
import sys
import Cv2ContextMaker as ccm

def main(args):
    """メイン"""
    # コンテキスト生成
    #me = ccm.Cv2ContextMaker(args)
    _c = ccm.Cv2ContextMaker("/workspaces/wwork/CCM/sample2.json")
    _ctx = _c.getContext(0)
    _ctx.createDir()
    _ctx.createMoveFrame(_ctx.getInputFileName())

if __name__ == "__main__":
    main(sys.argv)
