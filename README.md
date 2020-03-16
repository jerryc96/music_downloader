# music_downloader
uploads/downloads music files from a remote server

To run:

`pip install -r requirements.txt` to install django, or `pip install django`



To run the server locally, run `python manage.py runserver` in the music_downloader dir.

Endpoint for uploading a file: `BASE_URL/downloader/upload`,

```buildoutcfg
request body:
 {
    file: file_object
 }
```

Endpoint for downloading a file: `BASE_URL/downloader/download/<filename>`

Use postman to make requests
