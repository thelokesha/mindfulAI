import os
import requests
import json
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_tables():
    # Get Supabase credentials from environment variables
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        logger.error("Error: SUPABASE_URL or SUPABASE_KEY environment variables not set.")
        return False
    
    # Define the API URL for creating tables in Supabase
    api_url = f"{supabase_url}/rest/v1/"
    
    # Set up the headers
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    try:
        # Test the connection first
        logger.info("Testing connection to Supabase...")
        test_response = requests.get(f"{api_url}?apikey={supabase_key}", headers=headers)
        test_response.raise_for_status()
        logger.info("Connection to Supabase successful!")
        
        # Since we can't directly create tables via REST API, we'll check if our table exists
        # and if we can interact with it
        logger.info("Checking if users table exists and is accessible...")
        
        try:
            # Try to get one user to see if the table exists
            response = requests.get(
                f"{api_url}users?select=id&limit=1",
                headers=headers
            )
            
            if response.status_code == 200:
                logger.info("Users table exists and is accessible.")
                return True
            else:
                logger.warning(f"Could not access users table: {response.text}")
                logger.info("Please create the users table in the Supabase dashboard with the following structure:")
                logger.info("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
                """)
                return False
                
        except Exception as e:
            logger.error(f"Error accessing users table: {str(e)}")
            return False
            
    except Exception as e:
        logger.error(f"Error connecting to Supabase: {str(e)}")
        return False

if __name__ == "__main__":
    if create_tables():
        print("✅ Supabase tables check successful!")
        print("Your users table is ready to use.")
    else:
        print("❌ Could not verify the Supabase tables.")
        print("Please create the users table in your Supabase dashboard with this SQL:")
        print("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
        """)
