# API

## {{api}} = http://211.11.1.39/api

### RESPONSE PATTERN
__Success__
```json
{
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
    "status": "fail",
    "data": {
        "password":"password can't empty"
    }
}
```
__Error - Server failable action__
```json
{
    "status":"error",
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
__RESPONSE__
```json
{
    "status":"success",
    "data": {
        "name":"Mosh",
        "email":"abc@a.com",
        "date_birth": "",
        "phone":"",
        "address":""
    }
}
```

### LOGIN 
__POST__ *{{api}}/login*

```json
{
    "email":"abc@a.com",
    "password":"wkwkland"
}
```

__RESPONSE__
```json
{
    "status": "success",
    "data": {
        "key": "Bearer {{token}}"
    }
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
__RESPONSE__
```json
{
    "status":"success",
    "data": {
        "event":"Kajian bulanan",
        "date":"20-12-2012",
        "address":"Mecca, Saudi Arabia",
        "content":"Kajian mengenai adab terhadap orang tua",
        "preacher": {
            "name": "User",
            "date_birth": "12-12-2012",
            "email": "abc@def.com",
            "phone": "082878341703",
            "address": "Jogja"
        },
        "participants": []
    }
}
```

### PROFILE 
__GET__ *{{api}}/profile*
__HEADER__ Authorization: token, Content-Type: application/json
```json
{
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

### EVENT REGISTRATION
__POST__ *{{api}}/event/{{event.id(UUID_String)}}/register*
__HEADER__ Authorization: token, Content-Type: application/json
```json
{
    "status":"success",
    "data": {
        "id":"UUID EVENT",
        "email":"participant email"
    }
}
```

### CHECK-IN
__GET__ *{{api}}/checkin?event={{event.id(UUID_String)}}*
__HEADER__ Authorization: token, Content-Type: application/json
```json
{
    "status":"success",
    "data": {
        "event":"Kajian bulan Ramandhan",
        "participants": [
            {
                "id":1,
                "qr_code": "81d573b187606082a0d0027d... (sha256)",
                "user": {
                    "name":"Marzuki",
                    "date_birth": "12-12-2012"
                }
            },{
                "id":2,
                "qr_code": "793d47112fbc60bdbc6739... (sha256)",
                "user": {
                    "name":"DeathStar",
                    "date_birth": "12-12-2013"
                }
            }
        ]
    }
}
```
