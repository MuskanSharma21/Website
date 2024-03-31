from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)

# Configure MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:VivMus@2024@localhost/EvolveGuru'
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    mob_no = db.Column(db.String(20))
    profession = db.Column(db.String(50))

    
# Route for home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for registration form
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        mob_no = request.form['mob_no']
        profession = request.form['profession']

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create new User instance
        new_user = User(name=name, email=email, password=hashed_password, mob_no=mob_no, profession=profession)

        # Add new user to the database
        db.session.add(new_user)
        db.session.commit()

        return "Registration successful"  # You can redirect to a success page if needed
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Your login logic here
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
