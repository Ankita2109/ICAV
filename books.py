from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Books(Resource):

    #@app.route('icav/books/all' , method=['GET'])
    def get(self):
        data = pd.read_csv('books.csv' , nrows = 3)
        data = data.to_dict('records')
        return {'data':data}, 200

class FetchBook(Resource) :
    def get(self):
        data = pd.read_csv('books.csv')
        data = data.to_dict('records')

        # id = request.args.get('id',None)
        # authors = request.args.get('authors',None)
        if 'id' in request.args:
            id = int(request.args['id'])
        # elif 'id' in request.args:
        #     id = request.args['id']
        else:
            return "Error: No id field provided. Please specify an author."

            # Create an empty list for our results
        results = []

        for book in data:
            if book['id'] == id :
                results.append(book)
            # elif book['id'] == id:
            #     results.append(book)
        return jsonify(results)


api.add_resource(Books, '/books')
api.add_resource(FetchBook, '/book/fetch' )
if __name__ == '__main__':
    app.debug =True
    app.run()