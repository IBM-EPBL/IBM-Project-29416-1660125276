from flask import Flask, redirect, url_for, request,render_template,json
import os

app = Flask(__name__)

food_items = {"1":"rice", "2":"beans", "3":"yam", "4":"plantain", "5":"potatoes", "6":"wheat"}


@app.route('/data',methods = ['POST', 'GET'])
def api():
   if request.method == 'GET':
      return food_items

   if request.method =='POST':
       data = request.json
       food_items.update(data)
       return "Data is inserted"
           
@app.route("/data/<id>", methods=["PUT"])
def update(id):
    data = request.form['item']
    food_items[str(id)]=data
    return "Data updated" 

@app.route("/data/<id>", methods=["DELETE"])
def delete(id):
    food_items.pop(str(id))
    return "Data Deleted"       



if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
