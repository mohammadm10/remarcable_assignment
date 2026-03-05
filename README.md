## Remarcable Django Coding Assignment

In this project I created a simple Django backend that filtered products based on the user-defined search criteria and returned the result. The data model uses a one-to-many relationships for categories and a many-to-many relationship for tags, therefore allowing a product to have a single category but multiple tags. 

The admin UI allows for a simple way to quickly view the products on the backend with some basic filtering.

A template was created to allow the user to search for products on the frontend. This creates the ability to filter products via a description search, category dropdown, and tag selection.

### Setup and installation

1. Clone the repository directly from GitHub
```git clone git@github.com:mohammadm10/remarcable_assignment.git```
2. Open the folder
```cd remarcable_assignment```
3. Initialize the database
```python manage.py migrate```
4. Load the sample data
```python manage.py loaddata db_dump.json```
5. Run the application
```python manage.py runserver```
6. Open ```http://127.0.0.1:8000/products/``` in your browser 