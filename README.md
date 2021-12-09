# File Upload to google Drive

**Screeshot in `./screenshots`**

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/devraj4522/fileUpload.git
$ cd sample-django-app
```

1. Set Environment varible for `SECRET_KEY` and `GD_PATH`
2. Set google cloud api for google drive
3. Add gd.json file to the server with environment variables
4. Upload some data
5. `/details` to view data upoaded to `Google Drive APU`

```python
pip install -r requirements.txt
python manage.py createsuperuser

python manage.py makemigeration

python manage.py migrate
```
