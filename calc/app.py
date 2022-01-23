from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

OPERATIONs = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult
}

@app.route("math/<operation>")
def test_all_in_one(operation):
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPERATION[operation](a,b)

    return str(result)


