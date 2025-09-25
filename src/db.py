import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# ---------------- Users ----------------
def create_user(username: str, email: str, password: str):
    """Insert a new user into the users table"""
    data = {
        "username": username,
        "email": email,
        "password": password
    }
    response = supabase.table("users").insert(data).execute()
    return response


def get_user_by_email(email: str):
    """Fetch a user by email"""
    response = supabase.table("users").select("*").eq("email", email).execute()
    return response


# ---------------- Books ----------------
def add_book(title: str, author: str, description: str = None, cover_image: str = None):
    """Insert a new book"""
    data = {
        "title": title,
        "author": author,
        "description": description,
        "cover_image": cover_image
    }
    response = supabase.table("books").insert(data).execute()  # <- corrected table name
    return response


def get_all_books():
    """Fetch all books"""
    response = supabase.table("books").select("*").execute()  # <- corrected table name
    return response


# ---------------- Reviews ----------------
def add_review(user_id: int, book_id: int, rating: int, comment: str):
    """Insert a new review"""
    data = {
        "user_id": user_id,
        "book_id": book_id,
        "rating": rating,
        "comment": comment
    }
    response = supabase.table("reviews").insert(data).execute()
    return response


def get_reviews_for_book(book_id: int):
    """Fetch all reviews for a specific book"""
    response = supabase.table("reviews").select("*").eq("book_id", book_id).execute()
    return response
