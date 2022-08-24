# library_project

The library project includes 2 apps: user_app and book_app
The user app handles authentication affairs such as SignUp, Login and Logout. It contains 2 model classes (both inheriting from django built-in User): Member model and Staff (librarian) model. 
The book app keeps data about Categories, Books and Rented books in its tables. It also renders and shows "Book List" page for authenticated members.
Both apps also include admin panel config.


To run the project please:
1. activate the virtualenv
2. instal the requirements (pip install -r requirements.txt)
3. run the web application by command "python manage.py runserver"
4. enter localhost:8000 (or 127.0.0.1:8000) in your browser address bar (to access admin panel please add "/admin" at the end of address)

you can login to system using following information for test:

admin(superuser) with all permissions:
	username: admin
	password: admin
	

staff user (in admin panel) with limited permissions for members and books:
	username: staff1 (or staff2 or staff3)
	password: 1234!@#$

member user (in the website login page):
	username: mohammad
	password: 1234!@#$
	

note: the project code is also available in my Github account repositories: https://github.com/M-Naghavi-2022/library_project
