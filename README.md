## Remarcable Django Coding Assignment

In this project I created a simple Django backend that filtered products based on the user-defined search criteria and returned the result. The data model uses a one-to-many relationships for categories and a many-to-many relationship for tags, therefore allowing a product to have a single category but multiple tags. 

The admin UI allows for a simple way to quickly view the products on the backend with some basic filtering.

A template was created to allow the user to search for products on the frontend. This creates the ability to filter products via a description search, category dropdown, and tag selection.

### Setup and installation

1. Clone the repository directly from GitHub\
```git clone git@github.com:mohammadm10/remarcable_assignment.git```
2. Open the folder\
```cd remarcable_assignment```
3. Set up Virtual Environment\
Linux:\
```python3 -m venv venv```\
```source venv/bin/activate```\
Windows:\
```python -m venv venv```\
```.\venv\Scripts\activate```\
4. Install dependencies\
```pip install -r requirements.txt```
5. Initialize the database\
```python manage.py migrate```
6. Load the sample data\
```python manage.py loaddata db_dump.json```
7. Run the application\
```python manage.py runserver```
8. Open ```http://127.0.0.1:8000/products/``` in your browser 
9. Access the Admin Panel ```http://127.0.0.1:8000/admin/```\
To log in you will need to create a superuser account. This can be done using the following command: ```python manage.py createsuperuser```