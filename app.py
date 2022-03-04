import json

from flask import Flask, send_file, make_response, request, jsonify, Response

class APIResult():
    status = "fail"
    message = ""

    def __init__(self, status = "fail", message = "") -> None:
        self.status = status
        self.message = message

    def toJSON(self):
        return Response(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4), mimetype='application/json')

app = Flask(__name__)

# get example
@app.route('/setString', methods=['get'])
def G_setString():
    s = request.args.get('data')
    _result = APIResult()
    if s is None:
        _result.status = "fail"
        _result.message = f"[GET] str is None"
    else:
        _result.status = "success"
        _result.message = f"[GET] set string: {s}"

        path = 'output.txt'
        f = open(path, 'w')
        f.write(s)
        f.close()

    return _result.toJSON()

# post example
@app.route('/setString', methods=['post'])
def P_setString():
    s = request.values.get('data')
    _result = APIResult()
    if s is None:
        _result.status = "fail"
        _result.message = f"[POST] str is None"
    else:
        _result.status = "success"
        _result.message = f"[POST] set string: {s}"

        path = 'output.txt'
        f = open(path, 'w')
        f.write(s)
        f.close()

    return _result.toJSON()

if __name__=="__main__":
    app.run(host='192.168.1.100', port=5000)
