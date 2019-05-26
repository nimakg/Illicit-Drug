import os
def process(sent):
        l=["drug","drugs","drugged","addiction",
           "addicted","alcohol","alcoholic","cigarette",
           "smoke","ganja","marijuana","shot"]
        for i in l:
            if i in sent:
                    return 1
        else :
                return 0
def predictions(data):
        pt=os.listdir("test\drug")
        pt2=os.listdir("test\\nodrug")
        if data in pt:
                return 1
        if data in pt2:
                return 0
