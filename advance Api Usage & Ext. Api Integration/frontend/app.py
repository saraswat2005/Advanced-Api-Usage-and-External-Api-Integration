from flask import Flask, jsonify, request
import openai

API_KEY = open("../backend/advoadvice/API_KEY", "r").read()
openai.api_key = API_KEY

chat_log = []

while True:
    user_message = input()
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        assistant_response = response['choices'][0]['message']['content']
        print("AdvoAdvice:",assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n" ).strip()})
# app = Flask(__name__)
#
# books = [
#     {"id": 1, "title": "Python Programming", "au    thor": "John Smith"},
#     {"id": 2, "title": "JavaScript Basics", "author": "Alice Johnson"}
# ]
#
# # Route to get all books
# @app.route('/api/books', methods=['GET'])
# def get_books():
#     return jsonify(books)
#
# # Route to get a specific book by ID
# @app.route('/api/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((book for book in books if book['id'] == book_id), None)
#     if book:
#         return jsonify(book)
#     else:
#         return jsonify({'error': 'Book not found'}), 404
#
# # Route to add a new book
# @app.route('/api/books', methods=['POST'])
# def add_book():
#     new_book = request.json
#     books.append(new_book)
#     return jsonify(new_book), 201
#
# if __name__ == '__main__':
#     app.run(debug=True)
