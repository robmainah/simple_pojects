<h2>Installation Guide</h2>
<br>
<p>1. Clone project</p>
<br>
<p>2. cd to project folder</p>
<br>
<p>3. Delete sqlite file if exists</p>
<br>
<p>4. Install project packages. pip install < requirements.txt</p>
<br>
<p>5. Migrate database tables. Run in cmd:</p>
<br>
<ul>
    <li><i>python manage.py makemigrations</i></li>
    <li><i>python manage.py migrate</i></li>
</ul>
<p>Create a site admin user: python manage.py createsuperuser and type admin(is easy to remember) and fill in the rest</p>
<br>
<p>Run server: <i>python manage.py runserver</i></p>
<br>
<p>Go to <i>127.0.0.1:8000</i></p>
<br>
<p>For the hostel project a student can register and then login</p>
<br>
<br>
<h3>For the hostel admin they shall login using the admin user account</h3>
<p>For the attendance system, the student is added by admin and they can later login.</p>
<br>
<p>After creating a student the default password is: <i><strong>password</strong></i> but the email is the student's email</p>
<br>
