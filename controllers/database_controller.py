"""
controller_database define all operations whit mongodb database
insert, search, update and delete fields from database
"""

# user_images_path = './images/users/'
# drink_images_path = './images/drinks/'
# plate_images_path = './images/plates/'


def login_user(collection, json) -> tuple:
    success = False
    try:
        email = json['email']
        password = json['password']
    except Exception as e:
        print(e)
        message = 'You should type username and password'
    else:
        try:
            user_response = collection.find_one({'email': email})
        except Exception as e:
            print(e)
            message = str(e)
        else:
            if user_response is not None:
                if user_response['password'] == password:
                    success = True
                    message = 'Correct credentials'
                else:
                    message = 'Incorrect password'
            else:
                message = 'Incorrect username'
    return success, message


def insert_user(collection, json, url_photo: str) -> tuple:
    success = False
    try:
        username = json['username']
        email = json['email']
        password = json['password']
        status = json['status']
        photo = url_photo
    except Exception as e:
        print(e)
        message = 'All inputs are required',
    else:
        try:
            collection.insert(
               {
                   'username': username,
                   'email': email,
                   'password': password,
                   'status': status,
                   'photo': photo
               }
            )
        except Exception as e:
            print(e)
            message = str(e)
        else:
            success = True
            message = 'User save successfully'
    return success, message


def find_user(collection, json) -> tuple:
    success = False
    try:
        email = json['email']
    except Exception as e:
        print(e)
        message = 'An error has occurred'
    else:
        try:
            user = collection.find_one(
               {
                   'email': email
               }
            )
        except Exception as e:
            print(e)
            message = str(e)
        else:
            success = True
            message = {
                "username": user['username'],
                "email": user['email'],
                "password": user['password'],
                "status": user['status'],
                "photo": user['photo']
            }
    return success, message


def get_plates(collection) -> tuple:
    success = False
    try:
        plates_response = collection.find()
    except Exception as e:
        print(e)
        message = str(e)
    else:
        success = True
        if plates_response.count() > 0:
            plates = []
            for plate in plates_response:
                plate = {
                    'name': plate['name'],
                    'kind': plate['kind'],
                    'price': plate['price'],
                    'preparation_time': plate['preparation_time'],
                    'photo': plate['photo']
                }
                plates.append(plate)
            message = plates
        else:
            message = 'There is no plates yet'
    return success, message


def get_drinks(collection) -> tuple:
    success = False
    try:
        drinks_response = collection.find()
    except Exception as e:
        print(e)
        message = str(e)
    else:
        success = True
        if drinks_response.count() > 0:
            drinks = []
            for drink in drinks_response:
                drink = {
                    'name': drink['name'],
                    'price': drink['price'],
                    'photo': drink['photo']
                }
                drinks.append(drink)
            message = drinks
        else:
            message = 'There is no drinks yet'
    return success, message


def insert_plate(collection, json, url_photo: str):
    success = False
    try:
        name = json['name']
        kind = json['kind']
        price = json['price']
        preparation_time = json['preparation_time']
    except Exception as e:
        print(e)
        message = 'All inputs are required'
    else:
        try:
            collection.insert(
               {
                   'name': name,
                   'kind': kind,
                   'price': price,
                   'preparation_time': preparation_time,
                   'photo': url_photo
               }
            )
        except Exception as e:
            print(e)
            message = str(e)
        else:
            success = True
            message = 'Plate save successfully'
    return success, message


def insert_drink(collection, json, url_photo: str):
    success = False
    try:
        name = json['name']
        price = json['price']
    except Exception as e:
        print(e)
        message = 'All inputs are required'
    else:
        try:
            collection.insert(
               {
                   'name': name,
                   'price': price,
                   'photo': url_photo
               }
            )
        except Exception as e:
            print(e)
            message = str(e)
        else:
            success = True
            message = 'Drink save successfully'
    return success, message
