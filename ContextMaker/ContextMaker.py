# coding:utf-8
import json

class ContextMaker:
    """"""
    
    def __init__(self, args):
        with open(args, encoding="utf-8") as openjson:
            self.loadjson = json.loads(openjson.read(), encoding="utf-8")
        self._instance_name = self.loadjson["context_name"]
        self._instance_body = self.loadjson["context_body"]
        self._active_cnt = {}
        for i in range(len(self._instance_body)):
            self._active_cnt[self._instance_body[i]["name"]] = 0
        self._active = {}
    
    def getContext(self, args):
        """"""
        for i in range(len(self._instance_body)):
            if(args == self._instance_body[i]["name"]):
                self._active_cnt[args] += 1
                self._active = self._instance_body[i]
                self._active["counter"] = self._active_cnt[args]
                return self
    
    def getAll(self):
        """設定中のコンテキスト"""
        return self._active
    
    def getName(self):
        """選択中コンテキストの名前"""
        return self._active["name"]
        
    def getAccesCounter(self):
        """コンテキストを選択した回数"""
        return self._active["counter"]
        
    def getMetaData(self):
        """選択中コンテキストのメタデータ"""
        return self._active["metadata"]
        
    def getAddin(self):
        """選択中コンテキストのアドイン"""
        return self._active["add_in"]
    
    def getAddinId(self):
        """選択中コンテキストのアドイン(id)"""
        return self._active["add_in"]["id"]
    
    def getAddinValue1(self):
        """選択中コンテキストのアドイン(value1)"""
        return self._active["add_in"]["value1"]
    
    def getAddinvalue2(self):
        """選択中コンテキストのアドイン(value2)"""
        return self._active["add_in"]["value2"]
    
    def getAddon01(self):
        """選択中コンテキストのアドオン(01)"""
        return self._active["add_on_01"]
    
    def getAddon02(self):
        """選択中コンテキストのアドオン(02)"""
        return self._active["add_on_02"]
    
    def addonPush(self, addon, name, number):
        """選択中コンテキストのアドオン適用"""
        target = self.getAddin()
        addonobj1 = {}
        addonobj2 = {}
        if(type(number) is int):
            addonobj1 = addon[number]["add_on_arry"]
        else:
            addonobj1 = addon[0]["add_on_arry"]
        
        for i in range(len(addonobj1)):
            if(name == addonobj1[i]["name"]):
                addonobj2 = addonobj1[i]
        
        if(addonobj2["id"] == "add_on_01"):
            return target[addonobj2["target"]] + addonobj2["property"]
        elif(addonobj2["id"] == "add_on_02"):
            return target[addonobj2["target"]] - addonobj2["property"]
        elif(addonobj2["id"] == "add_on_03"):
            return target[addonobj2["target"]] * addonobj2["property"]
