from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
  if request.method == 'POST':
    message = request.get_json()

    print("i got a meassage")

    print(message, "\n")
    return Response('OK', status=200)
  else:
    return '<h1>hello worls</h1>'


if __name__ == "__main__":
  app.run(debug=True, port=8080)
