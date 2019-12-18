# coding:utf-8
base_json = {
    "id":"json_id",
    "event":[
        {
            "id":"event_id_01",
            "param":[
                {
                    "name":"param_id_01_p01",
                    "command":"command1001",
                    "value":"1001"
                },
                {
                    "name":"param_id_01_p02",
                    "command":"command1002",
                    "value":"1002"
                },
                {
                    "name":"param_id_01_p03",
                    "command":"command1003",
                    "value":"1003"
                }
            ]
        },
        {
            "id":"event_id_02",
            "param":[
                {
                    "name":"param_id_02_p01",
                    "command":"command2001",
                    "value":"2001"
                },
                {
                    "name":"param_id_02_p02",
                    "command":"command2002",
                    "value":"2002"
                },
                {
                    "name":"param_id_01_p03",
                    "command":"command2003",
                    "value":"2003"
                }
            ]
        },
        {
            "id":"event_id_03",
            "param":[
                {
                    "name":"param_id_03_p01",
                    "command":"command3001",
                    "value":"3001"
                },
                {
                    "name":"param_id_03_p02",
                    "command":"command3002",
                    "value":"3002"
                },
                {
                    "name":"param_id_01_p03",
                    "command":"command3003",
                    "value":"3003"
                }
            ]
        }
    ]
}

class DoSON():
    """"""
    def __init__(self, args):
        u"""初期化"""
        self.json = args
    
    def getJson(self):
        u"""json取得\n
        json>"""
        return self.json
    
    def getJsonId(self):
        u"""json id取得\n
        json>id"""
        return self.json["id"]
    
    def getJsonEventList(self):
        u"""json event取得\n
        json>event"""
        return self.json["event"]
        
    def getJsonEvent(self, args):
        u"""json event取得(位置指定)\n
        args = int:必須\n
        json>event[n, ...]"""
        return self.json["event"][args]
    
    def getJsonEventId(self, args):
        u"""json event id取得(位置指定)\n
        args = int:必須\n
        json>event[n, ...]<id"""
        return self.json["event"][args]["id"]
    
    def getJsonEventParamList(self, args):
        u"""json event param取得(位置指定)\n
        args = int:必須\n
        json>event[n, ...]<param[n, ...]"""
        return self.json["event"][args]["param"]
    
    def getJsonEventParam(self, arg1, arg2):
        u"""json event param取得(位置指定)\n
        arg1 = int:必須\n
        arg2 = name:必須\n
        json>event[n, ...]<param[n, ...]"""
        for i in list(range(len(self.json["event"][arg1]["param"]))):
            if(self.json["event"][arg1]["param"][i]["name"] == arg2):
                return self.json["event"][arg1]["param"][i]

def main():
    u""""""
    jObj = DoSON(base_json)
    print(jObj.getJsonEventList())
    print("-------------------------")
    print(jObj.getJsonEventParam(0, "param_id_01_p02"))
    
if __name__ == "__main__":
    main()
