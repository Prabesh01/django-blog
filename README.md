## Usage

- git clone https://github.com/Prabesh01/django-blog.git
- cd django-blog
- python -m venv dj
- ./dj/Scripts/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver [Press Ctrl+C to stop the server]

_Now, visit http://127.0.0.1:8000/ for the main site and http://127.0.0.1:8000/admin for admin panel_

## Populate with dummy data
_Not just dummy data, with this you can even turn the blog site into live news portal without any hassle_

### Create Users
- python manage.py shell
  - exec(open('news_authors.py').read())
  - exit()
  
### Create Posts
- python manage.py runcrons

_You may run this command once every 5 minutes or so to fetch latest news into your website_

## Misc Configurations

### Configure Email

_If you wish to use the Reset password feature, you have to provide your email server's (gmail in this case) credentials_

- Make sure 2 Factor Authorization (2FA) is enabled on your gmail account. [Link to enable it](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome)
- Generate a app Password for Mail service from [here](https://myaccount.google.com/apppasswords)
- Copy the given password and replace it with 'pass' at the last line of proj/settings.py file
- Replace 'mail@gmail.com' with your gmail address on second last line of the same file
- Restart the server and the email feature will hopefully work.

### Configure AWS
_For scalability, turn the debug off from settings.py, configure media and static folders accordingly for apache2/nginx and use AWS S3 instead of local storage_
- pip install boto3 django-storages
- settings.py:
    + installed apps: 'storages'
    + variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY_ID,AWS_STORAGE_BUCKET_NAME
    + AWS_S3_FILE_OVERWRITE=False
    + AWS_DEFAUL_ACL=None
    + DEFAULT_FILE_STORAGE='storages.backends.s3boto3.s3boto3storage'
  
_Completely remove the image scalling function save() in models.py and use lambda function to resize images on AWS. Alsom configure CORS settings on s3 accordingly_
