from flask import Flask
from flask import jsonify
from flask import request
from json import dumps
from pymongo import MongoClient

import os
import controllers.database_controller as db_controller
import controllers.images_controler as img_controller

app = Flask(__name__)

# Create mongo client
mongo_client = MongoClient('localhost', 27017)

# Connect to database RestaurantDB
restaurant_db = mongo_client.RestaurantDB

# Connect to users collection
users_collection = restaurant_db.users

# Connect to drinks collection
drinks_collection = restaurant_db.drinks

# Connect to plates collection
plates_collection = restaurant_db.plates

# Define URL folder to save images
main_folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0: -1]
user_imgs = os.path.join('/'.join(main_folder), 'static', 'images', 'user/')
drink_imgs = os.path.join('/'.join(main_folder), 'static', 'images', 'drinks/')
plate_imgs = os.path.join('/'.join(main_folder), 'static', 'images', 'plates/')


# GET
@app.route('/')
def hello_world():
    """
    :return: JSON: {"success": success, "message": message}
    """
    success = True
    message = 'Restaurant App index'
    # print(user_images)
    # print(drinks_images)
    # print(plates_images)
    return jsonify({
        "success": success,
        "message": message
    })


# POST
@app.route('/login', methods=['POST'])
def login():
    """
    :param: JSON: {"email": email, "password": password}
    :return: JSON: {"success": success, "message": message}
    """
    json = request.get_json()
    success, message = db_controller.login_user(users_collection, json)
    return jsonify({
        "success": success,
        "message": message
    })


# POST
@app.route('/singup', methods=['POST'])
def singup():
    """
    :param: JSON: {
                    "username": username,
                    "email": email,
                    "password": password,
                    "status": status,
                    "photo": photo
              }
    :return: JSON: {"success": success, "message": message}
    """
    json = request.get_json()
    url_photo = img_controller.decode__image(
        user_imgs, json['email'], json['photo']
    )
    success, message = db_controller.insert_user(
        users_collection, json, url_photo
    )
    return jsonify(success, message)


# POST
@app.route('/data/user', methods=['POST'])
def find_user():
    """
    :param: JSON: {
                    "name": name,
                    "kind": kind,
                    "price": price,
                    "preparation_time": preparation_time,
                    "photo": photo
              }
    :return: JSON: {message}
    """
    json = request.get_json()
    success, message = db_controller.find_user(users_collection, json)
    if success:
        photo = img_controller.encoder_base64_image(message['photo'])
        message['photo'] = photo
    return jsonify(message)


# GET
@app.route('/data/plates')
def get_all_plates():
    """
    :param:
    :return: JSON: {message}
    """
    success, message = db_controller.get_plates(plates_collection)
    if success:
        for item in message:
            photo = img_controller.encoder_base64_image(item['photo'])
            item['photo'] = photo
    return jsonify(message)


# GET
@app.route('/data/drinks')
def get_all_drinks():
    """
    :param:
    :return: JSON: {message}
    """
    success, message = db_controller.get_drinks(drinks_collection)
    if success:
        for item in message:
            photo = img_controller.encoder_base64_image(item['photo'])
            item['photo'] = photo
    return jsonify(message)


# POST
@app.route('/data/plates', methods=['POST'])
def save_plate():
    """
    :param: JSON: {
                    "name": name,
                    "kind": kind,
                    "price": price,
                    "preparation_time": preparation_time,
                    "photo": photo
              }
    :return: JSON: {"success": success, "message": message}
    """
    json = request.get_json()
    url_photo = img_controller.decode__image(
        plate_imgs, json['name'], json['photo']
    )
    success, message = db_controller.insert_plate(
        plates_collection, json, url_photo
    )
    return jsonify({
        "success": success,
        "message": message
    })

@app.route('/data/customer', methods=['GET'])
def customers_table():
    json = request.get_json()
    customers_table = json['customers']
    numOfcustomer = json['numOfcustomer']
    if((numOfcustomer%2==0) and (numOfcustomer<=12)):

        return jsonify({
        "success": "success",
        "message": "allowed"
        })

@app.route('/data/time', methods=['GET'])
def reservation_time():
    
    json = request.get_json()
    time = json['time']
    if((time >=17) and (time>=23)):

        return jsonify({
        "success": "success",
        "message": "allowed"
        })

# POST
@app.route('/data/drinks', methods=['POST'])
def save_drink():
    """
    :param: JSON: {
                    "name": name,
                    "price": price,
                    "photo": photo
              }
    :return: JSON: {"success": success, "message": message}
    """
    json = request.get_json()
    url_photo = img_controller.decode__image(
        drink_imgs, json['name'], json['photo']
    )
    success, message = db_controller.insert_drink(
        drinks_collection, json, url_photo
    )
    return jsonify({
        "success": success,
        "message": message
    })


# GET ERROR
@app.errorhandler(404)
def page_not_found(error):
    """
    :param error:
    :return: JSON: {"success": success, "message": message}
    """
    success = False
    message = str(error)

    return jsonify({
        "success": success,
        "message": message
    }), 404


# GET ERROR
@app.errorhandler(500)
def server_error(error):
    """
    :param error:
    :return: JSON: {"success": success, "message": message}
    """
    success = False
    message = str(error)

    return jsonify({
        "success": success,
        "message": message
    }), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
