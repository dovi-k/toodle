import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


# getting all categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("name"))
    return render_template("categories.html", categories=categories)


# add category function
@app.route("/add-category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category_name = {"name": request.form.get("name"),
                         "created_by": session["user"]
                         }
        mongo.db.categories.insert_one(category_name)
        flash("New Category Added")
        return redirect(url_for("get_categories"))
    return render_template("add_category.html")


# edit category function
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# deleting category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# getting to do list items for each category
@app.route("/get_items/<category_id>")
def get_items(category_id):
    items = list(mongo.db.items.find({"category_id": category_id}))
    return render_template("items.html", items=items, category_id=category_id)


# getting to do list items for each category
@app.route("/get_item/<category_id>")
def get_item(category_id):
    items = list(mongo.db.items.find({"category_id": category_id}))
    return render_template("items_copy.html",
                           items=items, category_id=category_id)


# adding item to the list category
@app.route("/add_item/<category_id>", methods=["GET", "POST"])
def add_item(category_id):
    if request.method == "POST":
        item = {
            "category_id": category_id,
            "item": request.form.get("item_name"),
            "created_by": session["user"]
        }
        mongo.db.items.insert_one(item)
        flash("Successfully Added")
        return redirect(url_for("get_items", category_id=category_id))
    return render_template("add_item.html")


# editing list item
@app.route("/edit_item", methods=["GET", "POST"])
def edit_task(item_id):
    if request.method == "POST":
        submit = {
            "category_id": request.form.get("category_id"),
            "item_name": request.form.get("task_name"),
            "created_by": session["user"]
        }
        mongo.db.item.update({"_id": ObjectId(item_id)}, submit)
        flash("Successfully Updated")

    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    categories = mongo.db.categories.find().sort("name", 1)
    return render_template("get_item.html", item=item, categories=categories)


# deleting item from list
@app.route("/delete_item")
def delete_item(item_id):
    mongo.db.items.remove({"_id": ObjectId(item_id)})
    flash("Successfully Deleted")
    return redirect(url_for("get_item"))


# sign up function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# log in function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# log out functuon
@app.route("/logout")
def logout():
    # removing user from session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)
