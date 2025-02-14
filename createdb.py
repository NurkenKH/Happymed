from app import app, db

try:
    with app.app_context():
        db.create_all()
        print("Database created successfully.")
except Exception as e:
    print(f"Error creating database: {e}")