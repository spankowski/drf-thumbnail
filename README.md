# drf-thumbnail
 DRF and thumbnails
Using Django REST Framework, write an API that allows any user to upload an image in PNG or JPG format.

You are allowed to use any libraries or base projects / cookie cutters you want (but using DRF is a hard requirement).

Skip the registration part, assume users are created via the admin panel.

# Requirements:
it should be possible to easily run the project. docker-compose is a plus
- users should be able to upload images via HTTP request [x] 
Endpoint: http://127.0.0.1:8000/api/upload

- users should be able to list their images [done]
Endpoint: http://127.0.0.1:8000/api/pictures

## there are three account tiers: Basic, Premium and Enterprise:
- users that have "Basic" plan after uploading an image get: [done]
a link to a thumbnail that's 200px in height
- users that have "Premium" plan get: [done]
a link to a thumbnail that's 200px in height
a link to a thumbnail that's 400px in height
a link to the originally uploaded image
- users that have "Enterprise" plan get [done]
a link to a thumbnail that's 200px in height
a link to a thumbnail that's 400px in height
a link to the originally uploaded image [done]
- ability to fetch a link that expires after a number of seconds (user can specify any number between 300 and 30000) [done]
## admins should be able to create arbitrary plans with the following things configurable:
- arbitrary thumbnail sizes [x]
- presence of the link to the originally uploaded file [x]
- ability to generate expiring links [x]
- admin UI should be done via django-admin [done]
## there should be no custom user UI (just browsable API from Django Rest Framework)
remember about:
- tests
- validation
- performance considerations (assume there can be a lot of images and the API is frequently accessed)
