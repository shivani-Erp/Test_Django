# Test_Django

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
git clone <repository-url>

2. Install the required dependencies:
pip install -r requirements.txt

3. Set up the Postgres database and configure environment variables.

4. Migrate the database schema:
python manage.py makemigrations     
python manage.py migrate

5. Run the development server:
python manage.py runserver
## Features

1. Login Page: Users can log in securely.

2. Upload Data Page: Users can upload a large volume CSV file (1GB) with a visual progress indicator.

3. Query Builder Page: Users can filter the uploaded data using a form and view the count of records based on applied filters.

4. Users Page: Admin users can manage other user accounts.
## Usage

1. Login: Log in to the application using your credentials.

2. Upload Data: Upload a CSV file with the provided form. Monitor the upload progress visually.

3. Query Builder: Filter the uploaded data using the form provided. View the count of records based on the applied filters.

4. Users: Admin users can manage other user accounts, including adding, editing, or deleting user accounts.
## Contributing

I welcome contributions from the community! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
