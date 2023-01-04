# This is DRF project 




## Command 
- pip install -r requirement.txt
- python manage.py runserser
- you got url http://127.0.0.1:/8000/

## admin password id 
- email :- admin@gmail.com
- password :- admin

### if you want to create user u can use admin panel or create user using api 

- on web follow link

- http://127.0.0.1:/8000/userApi/

# URLs

- http://127.0.0.1:/8000/gettoken/ email="email" password="password"

- - its return 2 JWT (json web token)  refresh token and access token , access token will expire after 10 min 


- for refresh your token 

- http://127.0.0.1:/8000/refresh/ refresh=" refresh token here "
 

- for get resquet

- http://127.0.0.1:/8000/images/ 'Authorization: access token here '

- for post resquet you have to pass image field value 

- http://127.0.0.1:/8000/images/ 'Authorization: access token here '

- - and its return you thamnail , medium,large and grayscale image


# I have put some snapshot of Thunder client while using this api 