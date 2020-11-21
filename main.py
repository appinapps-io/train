import dbhelper

from flask import Flask,request,Response
from flask_cors import CORS
import json


app = Flask(__name__)

@app.route("/")
def index():
	return "Hello Api"



@app.route('/items/all')
def get_items_all():
	res_data = dbhelper.get_all_items()
	response = Response(res_data,mimetype='application/json')
	return response



#{'id':1,'title':'','date':'','time':'','status':''}

@app.route('/item/new',methods=['POST'])
def add_item():
	req_data = request.get_json()
	title = req_data['title']

	res_data = dbhelper.add_to_list(title)

	if res_data == None:
		response = Response("{'error':'item not added'}", status=400,mimetype='application/json')
		return response

	response = Response(json.dumps(res_data),mimetype='application/json')
	return response



@app.route('/item/update',methods=['PUT'])
def update_item():
	req_data = request.get_json()
	

	res_data = dbhelper.update_item(req_data)

	if res_data == None:
		response = Response("{'error':'item not updated'}", status=400,mimetype='application/json')
		return response

	response = Response(json.dumps(res_data),mimetype='application/json')
	return response


@app.route('/item/remove',methods=['DELETE'])
def delete_item():
	req_data = request.get_json()
	
	id = req_data['id']

	res_data = dbhelper.delete_item(id)

	if res_data == None:
		response = Response("{'error':'item not deleted'}", status=400,mimetype='application/json')
		return response

	response = Response(res_data,mimetype='application/json')
	return response



if __name__ == "__main__":
	CORS(app, resources=r'/*', allow_headers="Content-Type")
	app.run(debug=True,threaded=True)