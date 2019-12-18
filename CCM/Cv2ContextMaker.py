# coding:utf-8
import os
import json
import pylint
import cv2
from datetime import datetime

class Cv2ContextMaker:
    """"""
    def __init__(self, args):
        # 引数で渡されたjsonを格納
        with open(args, encoding="utf-8") as openjson:
            self._loadjson = json.loads(openjson.read(), encoding="utf-8")
        self._name = self._loadjson["context_name"]
        self._body = self._loadjson["context_body"]
        self._datekey = datetime.now().strftime("%Y%m%d%H%M%S")
        self._workdir = "/workspaces/wwork/CCM/work_{}/".format(self._datekey)
        self._outdir = "/workspaces/wwork/CCM/out_{}/".format(self._datekey)

    def getContext(self, args):
        """"""
        for i in range(len(self._body)):
            if(args == self._body[i]["id"]):
                self._active = self._body[i]
                self._id = self._active["id"]
                self._inputfile_name = self._active["input_file"]
                self._outfile_name = "{}_{}_{}.{}".format(self._active["output_file"], self._datekey, self._id, self._active["output_type"])
                self._outer_width = self._active["outer_property"]["width"]
                self._outer_height = self._active["outer_property"]["height"]
                self._image_add_on = self._active["image_add_on"]
                self._sound_add_on = self._active["sound_add_on"]
                return self

    def getAll(self):
        """コンテキスト"""
        return self._loadjson
    
    def getId(self):
        """設定中のコンテキストid"""
        return self._id

    def getActive(self):
        """設定中のコンテキスト"""
        return self._active
    
    def getInputFileName(self):
        """インプットファイル名取得"""
        return self._inputfile_name

    def getOutFileName(self):
        """アウトファイル名取得"""
        return self._outfile_name
        
    def getMoveWidth(self):
        """動画wideth"""
        return self._outer_width
    
    def getMoveHeight(self):
        """動画wideth"""
        return self._outer_height
        
    def getMetaData(self):
        """選択中コンテキストのメタデータ"""
        return self._active["metadata"]
    
    def getImageAddOn(self):
        """画像加工情報"""
        return self._image_add_on
    
    def getSoundAddOn(self):
        """音声加工情報"""
        return self._sound_add_on
    
    def createDir(self):
        """作業ディレクトリ生成"""
        os.mkdir(self._workdir)
        os.mkdir(self._outdir)
    
    def createMoveFrame(self, args):
        """動画フレーム出力"""
        i = 0
        cap = cv2.VideoCapture(args)
        while(cap.isOpened()):
            flag, frame = cap.read()
            if flag == False:
                break
            cv2.imwrite("{}_{}_{}.{}",format(self._workdir, self.getId(), str(i).zfill(6)), frame)
            i += 1
        cap.release()

        