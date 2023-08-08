from flask import Flask,request
from flask_restful import Resource, Api


app=Flask(__name__)
api= Api(app)

Database = {
    1 : {"name": "Divyaraj Chudasama"},
    2 : {"name": " Jainam Khakhhar"},
    3 : {"name":" Pratik Chaudhary"},
    4 : {"name":" Aryan Amalani"},
    5 : {"name":" Arya Ahjoliya"}

}

class Items (Resource):
    def get(self):
        return Database
    
#     def post(self):
#         data= request.json()
#         itemId=len(Database.keys())+1  
#         Database[itemId]={"name": data['name'] }
#         return Database
    
#     def put(self,id):
#         data=request.json()
#         Database[id]=data['name']
#         return Database
    
#     def delete(self,id):
#         del Database[id]
#         return Database
    
class Item (Resource):
    def get(self, id):
        return Database[id]
    

@app.route("/") 
def hello():
    return "<h1>Hello World</h1>"

@app.route("/item_post",methods=['POST'])
def Push_database():
        data= request.json
        itemId=len(Database.keys())+1  
        Database[itemId]={"name": data['name'] }
        return Database

@app.route("/item_put/<int:id>",methods=['PUT']) 
def Put_database(id):
        data=request.json
        Database[id]=data
        return Database

@app.route("/item_delete/<int:id>",methods=['DELETE'])
def Delete_database(id):
        del Database[id]
        return Database

# @app.route("/item_get",methods='GET')
# def Get_database():
#         return Database[id]   

api.add_resource(Items,"/items")
api.add_resource(Item,"/item/<int:id>")    

if __name__=='__main__':
    app.run(debug=True)