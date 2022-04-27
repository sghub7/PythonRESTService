from flask import Flask, request, json

import random
app= Flask(__name__)
@app.post("/invokeEngine")
def run_engine():
    print("***** Triggered Post Method *****")
    if request.is_json:
        _data = (request.get_json())

        runId=_data["run_id"]
        print(runId)
        data = json.dumps(_data)
        createRunFile(runId,data)
        return "Posted Successfully"
    return ({"error":"invalid data"})

def createRunFile(run_id,data):
    f = open("../data/"+str(run_id)+".new", "w")
    f.write(data)
    f.close()



