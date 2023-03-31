from flask import Flask,jsonify, request

app = Flask(__name__)

"data" = [
    {
        'contact':'9398088182'
        'name': u'yuktha',
        'id': u'0012', 
        'done': False
    },
    {    'contact':'9398088182'
        'name': u'yuktha',
        'id': u'0012', 
        'done': False
      
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
        contact={
            'id':tasks[-1][id] +1,
            'name':request.json['name'],
        'contact':request.json.get['contact',""], 
        'done': False
      

        }

      get_task.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)