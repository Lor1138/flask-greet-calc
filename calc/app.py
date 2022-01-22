from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

OPERATION = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult
}

@app.route("math/<operations>")
def test_all_in_one(operations):
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPERATION[operations](a,b)


