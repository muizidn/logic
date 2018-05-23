# API

## {{api}} = http://211.11.1.39/api

### RESPONSE PATTERN
__Success__
```json
{
    "apiVersion":"1.0",
    "status":"success",
    "data":{
        "id":1,
        "name":"Mosh"
    }
}
```
__Fail - User failable action__
```json
{
    "apiVersion":"1.0",
    "status": "fail",
    "data": {
        "password":"password can't empty"
    }
}
```
__Error - Server failable action__
```json
{
    "apiVersion":"1.0",
    "status":"error",
    "code": 404,
    "message":"Cannot access database",
}
```

### REGISTER
__POST__ *{{api}}/register?type=organizer/participant*
```json
{
    "email":"abc@a.com",
    "password":"wkwkwland",
    "profile": {
        "name":"Mosh"
    }
}
```

### LOGIN 
__POST__ *{{api}}/login?type=organizer/participant*

```json
{
    "email":"abc@a.com",
    "password":"wkwkland"
}
```

### LOGOUT
__POST__ *{{api}}/logout*
__HEADER__ Authorization: token

### EVENT
__GET__ *{{api}}/events*
__HEADER__ Authorization: token, Content-Type: application/json
Success
```json
{
    "apiVersion":"1.0",
    "status":"success",
    "data": [
        {
            "id":"-uuid-string-",
            "event":"Kajian bulanan",
            "date":"20-12-2012",
            "address":"Mecca, Saudi Arabia",
            "content":"Kajian mengenai adab terhadap orang tua",
            "preacher": {
                "name": "String",
                "date_birth": "12-12-2012",
                "email": "abc@def.com",
                "phone": "082878341703",
                "address": "Jogja"
            },
            "participants": [
                {
                    "name": "String",
                    "date_birth": "12-12-2012",
                    "email": "abc@def.com",
                    "phone": "082878341703",
                    "address": "Jogja"
                }
            ]
        }
     ]
}
```
__POST__ *{{api}}/events*
__HEADER__ Authorization: token, Content-Type: application/json
```json
{
    "event":"Kajian bulanan",
    "date":"20-12-2012",
    "address":"Mecca, Saudi Arabia",
    "content":"Kajian mengenai adab terhadap orang tua"
}
```

### PROFILE 
__GET__ *{{api}}/profile*
__HEADER__ Authorization: token, Content-Type: application/json
```json
{
    "apiVersion":"1.0",
    "status":"success",
    "data": {
      "name": "String",
      "date_birth": "12-12-2012",
      "email": "abc@def.com",
      "phone": "082878341703",
      "address": "Jogja"
    }
}
```

__PATCH/PUT__ *{{api}}/profile*
__HEADER__ Authorization: token, Content-Type: application/json
```json
{
    "name": "String",
    "date_birth": "12-12-2012",
    "email": "abc@def.com",
    "phone": "082878341703",
    "address": "Jogja"
}
```

### CHECK-IN
__GET__ *{{api}}/checkin?event={{event.id(UUID_String)}}*
__HEADER__ Authorization: token, Content-Type: application/json
```json
{
    "apiVersion":"1.0",
    "status":"success",
    "data": {
        "event":"Kajian bulan Ramandhan",
        "participants": [
            {
                "id":1,
                "qr_code": "hashed_encoded",
                "id_code":"generated_id"
            }
        ]
    }
}
```


