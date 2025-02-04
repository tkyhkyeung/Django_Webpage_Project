The assignment focuses on creating and managing data models, handling data operations (import/export), and ensuring functionality through the Django admin panel.\
## Features
**Data Models**: Includes at least three Django models (Person, Product, Order) with relationships.\
**Sample Data:** Automatically populates the database with at least 20 records for each model using a custom script.\
**Data Cleaning and Formatting:** Provides a script to clean and format raw data.\
**Import/Export Functionality:** Includes scripts to import data into and export data from the database in CSV format.\
**Django Admin Integration:** All models and data are accessible through the Django admin panel.\

## File Structure
tky/\
├── myproject/             # Main Django project folder\
│   ├── settings.py        # Project settings\
│   ├── urls.py            # URL configurations\
│   └── ...\
├── webapp/                # Django app folder\
│   ├── models.py          # Data models\
│   ├── views.py           # Views for handling requests\
│   ├── admin.py           # Admin panel configurations\
│   └── ...
├── populate_data.py       # Script to populate the database with sample data\
├── data_cleaning.py       # Script to clean and format raw data\
├── data_import_export.py  # Script for importing/exporting data in CSV format\
└── README.md              # Project documentation (this file)\

## How to Run the Project
**1. Clone the Repository**\
`git clone git@github.com:tkyhkyeung/Django_Webpage_Project.git\
cd Django_Webpage_Project`\
**2. Set Up the Virtual Environment**\
`python3 -m venv venv\
source venv/bin/activate  # For macOS/Linux\
venv\Scripts\activate     # For Windows`\
**3. Install Dependencies**\
`pip install -r requirements.txt`\
**4. Apply Migrations and Populate Data**\
`python manage.py makemigrations\
python manage.py migrate\
python populate_data.py  # Populate the database with sample data`\
**5. Run the Server**\
`python manage.py runserver`\
Access the application at http://127.0.0.1:8000/.\
## Scripts
**1. Populate Data**\
Populates the database with at least 20 records for each model:\
`python populate_data.py`\
**2. Clean and Format Data**\
Cleans duplicate records and formats names:\
`python data_cleaning.py`\
**3. Import/Export Data**\
Export data to person_data.csv:\
`python data_import_export.py  # Exports by default.`\
Import data from person_data.csv:\
Uncomment the import_data() function in data_import_export.py and run:\
`python data_import_export.py`
## Django Admin Panel
To access the admin panel:
1. Create a superuser:
`python manage.py createsuperuser`
2. Visit http://127.0.0.1:8000/admin and log in.
