# Book Review

A web application where users can register, log in, search for books via an external API (like Google Books API), save them in your database, and write reviews. Users can browse books and see community reviews, similar to Goodreads, but books are added dynamically via API.

# Pages & Features
🔹 1. Homepage (index.html)

Shows all books saved in your database.

Each book card shows title, author, average rating, and a “View Details” button.

🔹 2. Register & Login (register.html, login.html)

Users can create accounts and log in.

Passwords stored securely with hashing.

🔹 3. Search Book (search.html)

User enters book name → Flask sends request to Google Books API.

Shows search results: title, author, cover, description.

User can click “Add to My Library” → saves book to your database.

🔹 4. Book Details (book.html)

Shows book info + all reviews for that book.

Logged-in users can add a review + rating.

Average rating is calculated dynamically.

🔹 5. User Dashboard (dashboard.html)

Shows all reviews submitted by the logged-in user.

🔹 6. Logout

Ends session and redirects to homepage.


# Project Structure
 Book-Review/
 |
 |--src/
 |     |--logic.py  #Business logic and task
 operations
 |  |--db.py  #Database operation
 |
 |--api/        #Backend API
 |   |__main.py  #FastAPI endpoints
 |
 |--frontend/       #FrontEnd application
 |     |__app.py   #Streamlit Web interface
 |
 |__requiremts.txt  # python dependencies
 |
 |__README.md  # Project documentation
 |
 |__.env   # Python variables  


 ## Quick start

 ### Prerequiremets

 -Python 3.8 or higher
 -A supabase account
 -Git(push,cloning)

 ## 1. clone or Download the project
 # option 1: Clone with git
 git clone <repository link>

 # option 2: Download and extract the zip file

 ### 2. Install Dependencies
  # Install all required pyhton packages
  pip install -r requirements.txt

  ### 3.Set up  Supabase Database
  1.Create a Supabase project:

  2.Create the Tasks Table:
    -Go to the sql Editor in your Supabase
    dashboard
    -Run this sql command:
    --sql

    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
    );

3.**GET your credentials:

### 4.Configure Enviroonment variables

 1. Create a .env filr in the project root
 
 2. Add Supabase Credentials to .env :
 SUPABASE_URL=your project url
 SUPABSE_KEY=your_anon_key_here


### 5.Run the Application
## Streamlit Frontend
streamlit run frontend/app.py
The app will open in your browser at http://localhost:8501

## FastApI Backend
 cd api
 pyhton main.py
 The Api will be available  at http://localhost:8000


 # How to use
 # Technical Details
 # Technologies used

** Backend: Python (Flask)

Database: SQLite (or PostgreSQL for advanced)

Frontend: HTML, CSS, Bootstrap, JavaScript

Authentication: Flask-Login

External API: Google Books API (to fetch book details dynamically)

### key components
 
 1. **src/db.py**:Database operations Handle all CRUD operations with supabase

 2. **src/login.py**:Business logic -Task validation and processing

 ## Troubleshooting
 ## Common Issues

 ## Future Enhancemts

 Ideas for extending this project:




 ## Support
 Mobile No:9182187600
 email:indunamani600@gmail.com