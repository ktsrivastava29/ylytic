# RestaurantApi
*** 
### Description
***
<!-- RestaurantApi is the server side developed for a mobile application whose
main objective is to manage user, dishes and drinks information.
It's developed using Python 3.x, Flask, MongoDB and Pymongo.
The server exposes a REST API allowing operate with web services. -->
***
### Endpoints
Index
* / ==> method==GET 
* * return:     {success: success, "message": message} 

Users
* /login ==> method==POST
* * param:      {"email": email, "password": password}
* * return:     {success: success, "message": message}
* /singup ==> method==POST
* * param:      {  
                    "username": username,  
                    "email": email,  
                    "password": password,  
                    "status": status,  
                    "photo": photo  
                }
* * return:     {success: success, "message": message}

Plates
* /data/plates ==> method==GET
* * return:     {  
                    success: success,  
                    message: [{  
                           "name": name,  
                           "kind": kind,  
                           "price": price,  
                           "preparation_time":preparation_time,  
                           "photo": photo,  
                    }]
                }
* /data/plates ==> method==POST
* * param:      {  
                    "name": name,  
                    "kind": kind,  
                    "price": price,  
                    "preparation_time": preparation_time,  
                    "photo": photo  
                }
* * return:     {success: success, "message": message}

Drinks
* /data/drinks ==> method==GET
* * return:     {  
                   success: success,  
                   message: [{  
                        "name": name,  
                       "price": price,  
                       "photo": photo,  
                   }]  
                }
* /data/drinks ==> method==POST
* * param:      {  
                    "name": name,  
                    "price": price,  
                    "photo": photo  
                }
* * return:     {success: success, "message": message}
***
### Requirements
* Python 3.x
* MongoDB
* Flask
* Pymongo