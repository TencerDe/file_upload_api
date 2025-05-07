Django File Upload System with Authentication

This is a simple Django project I made where users can sign up, log in, and upload files. The uploaded files are visible to everyone on the homepage, and anyone can download them — even if they are not logged in.

---

Features

- User Signup/Login/Logout using Django built-in authentication system.
- Authenticated users can upload files.
- Anyone can view and download uploaded files without logging in.
- Each file shows the username of the person who uploaded it.
- REST APIs for:
  - Uploading files (POST request)
  - Getting public file list (GET request)
  - Getting files uploaded by the logged-in user (GET request)

---

How I Built It

1. I created a Django project and an app called uploads.
2. Created models for storing file data (title, file, user, upload date).
3. Used Django’s default authentication system for login/signup.
4. Used FileField to handle file uploads.
5. Added basic HTML templates without any CSS framework (simple, just for testing).
6. Created 3 API endpoints using Django REST Framework.
7. Finally, tested all pages manually with postman

---

How to Use It

1. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
2. Run the server:
  python manage.py runserver

3. Open http://127.0.0.1:8000/ in your browser.
4. Or ctrl+click on the link appeared in the terminal.

5. You can:
   Sign up
   Log in
   Upload files
   Download any file from homepage

API Endpoints
Method	URL	Description
POST	/api/upload/	Upload a file (login required)
GET	/api/public-files/	List all uploaded files
GET	/api/my-files/	List files uploaded by you

Errors I Faced & Fixed
1. Reverse for download not found
Problem: Homepage was showing an error when clicking on the download link.

Fix: I was using {% url 'download' file.id %} in the template but the correct URL name was 'download_file'.

Final Fix: Changed it to {% url 'download_file' file.id %}.

2. Username not showing with uploaded file
Problem: After uploading a file, I couldn’t see who uploaded it.

Fix: I wasn’t using {{ file.user.username }} in the template.

Final Fix: Added that line in home.html and now it works.

3. Forgot to create API views using Django REST Framework
Problem: I initially wrote normal Django views for APIs but the assignment needed REST APIs.

Fix: Added REST API views using @api_view decorators and returned Response() objects properly.

4. Path issues between app-level and project-level URLs
Problem: I was confused whether to add download URLs in project or app urls.py.

Fix: Moved all relevant paths to the app-level urls.py and imported them properly in the project urls.py.

API TESTUNG JSON DATA:

login
POST method will be used:
{
  "username": "testuser1",
  "password": "testpass123"
}

Upload file 
POST method here also:
Endpoint : /api/upload/
Headers values to be put: 
Content-Type: multipart/form-data
Authorization: Basic <base64encoded(username:password)>

DOWNLOADING UPLOADED FILES
GET method use
Endpoint :  /api/my-files/
Sample Json Data:
[
  {
    "id": 1,
    "title": "Report.pdf",
    "file_url": "http://127.0.0.1:8000/media/uploads/report.pdf",
    "uploaded_by": "testuser1",
    "uploaded_at": "2025-05-07T14:00:00Z"
  }
]

SEEING PUBLIC FILES:
GET method used
