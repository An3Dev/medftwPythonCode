# Import nessecary parts from flask and faker to generate random    # name and email.
from flask import Flask, request, jsonify
from faker import Faker
# To create and initialize a faker generator.
fake = Faker()
# Create the app object that will route our calls.
app = Flask(__name__)
# Add a single endpoint that we can use as an API to accept GET and # POST requests.
@app.route("/", methods=["POST", "GET"])
def index():
    # fake to create random name and email
    name = fake.name()
    email = fake.email()
    response = {
        "name": name,
        "email": email
    }
    # return name and email as a JSON httpresponse using jsonify
    return jsonify(response)

@app.route("/getlocation/<name>")
def test(name):
    
    response = {
        "name": name
    }
    print(name)
    return jsonify(response)

# When run from command line, start the server.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')