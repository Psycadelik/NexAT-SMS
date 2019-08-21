# SMS Client Api

###### This is an sms service that provides endpoints for sending sms via either Nexmo or AfricasTalking

Here's the basic directory structure;
```
├── app
│   ├── config.py
│   ├── __init__.py
├── README.md
├── requirements.txt
├── test
│   └── __init__.py
└── app.py
|__ Dockerfile
|__ .env
|__ docker-compose.yml
|__ .travis.yml

```

### Project Set up
- clone this repository
- cd into project folder
- create a virtual environment i.e `virtualenv venv`
- activate virtual environment i.e `source venv/bin/activate`
- run `pip install -r requirements.txt`
- create a .env file in the root of the project and add the following:
   
   `export NEXMO_API_KEY=`  
    `export NEXMO_API_SECRET=`  
    `export AT_USERNAME=`   
    ` export AT_API_KEY=`   
    ` export AT_SHORTCODE=` 
- run unit tests : `python -m unittest discover`
- start the project : `python app.py`
- open postman and navigate to the url : `http://127.0.0.1:5000/sendsms`
- add the payload as json: 

     `{`              
            `"provider": "nexmo(or africastalking)",`           
            `"sms": "your message"`,    
            `"recipient": 254723123456`        
      `}`   



