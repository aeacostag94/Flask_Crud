from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db


# Blueprints to separate the app into many parts and have control of all theroute used.

contacts = Blueprint("contacts", __name__)

# All the routes working from get method.

#Form and List


@contacts.route("/")
def home():
    # Listing all the data
    contacts = Contact.query.all()

    # for i in contacts:
    #     print (i.id)
    # Test the for to show all the elements.

    return render_template("index.html", contacts=contacts)

############## CREATE FUNCTION################


@contacts.route("/new", methods=["POST"])
def add_contact():
    #     # request allow to see the data sent in the POST methods
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added")

# #This print is just to check the values are coming
    print(new_contact)
    print(fullname)
    return redirect("/")

############## UPDATE FUNCTION################


@contacts.route("/update/<id>", methods=["POST", "GET"])
def update(id):

    # This conditional is to know if the info is comming from POST or GET method, if the info is comming for a GET it will make consult of the values but if is comming from a POST is going to make the update.
    #
    contact = Contact.query.get(id)
    if request.method == "POST":
        
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]


        db.session.commit()

        flash("Contact Updated")
        
        print("Contact Updated")
        return redirect(url_for("contacts.home"))
    else:
        contact = Contact.query.get(id)

    return render_template("update.html", contact=contact)

############## DELETE FUNCTION################
# If the route has another value after the name of the route, its means it needs another value to work, in this case delete url needs the id to delete the contact.
# And the functions it self need the same value as well like this:


@contacts.route("/delete/<id>")
def delete(id):
    # contact=Contact.query.get(id)
    db.session.delete(Contact.query.get(id))
    db.session.commit()

    print("Contact Deleted")

    flash("Contact Deleted")

    return redirect(url_for("contacts.home"))
