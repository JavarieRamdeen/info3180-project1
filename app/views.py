"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from fileinput import filename
import psycopg2
import os
from app import app, db
from app.forms import PropertyForm
from app.models import properties
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './info3180-project1/Images'
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

app.config['UPLOAD_PATH'] = './app/static/Images'
@app.route('/properties/create', methods=['GET', 'POST'])
def create():
    form = PropertyForm()

    title = form.title.data
    bedrooms = form.bedrooms.data
    bathrooms = form.bathrooms.data
    location = form.location.data
    price = form.price.data
    type = form.type.data
    description = form.description.data
    photo = form.photo.data
    
    if request.method == 'POST':       
        print("Hi",photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_PATH'], photo.filename))
 
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO properties (title, bedrooms, bathrooms, location, price, type, description, photo)'
        'VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
        (title,bedrooms,bathrooms,location,price,type,description,photo.filename))
        conn.commit()
        cur.close()
        conn.close()

        property= properties.query
        flash('Property was successfully added.', 'success')
        return render_template('properties.html',property=property)
    return render_template("create.html", form=form, photo=photo)

@app.route('/properties', methods=['GET', 'POST'])
def view_properties():
    property= properties.query
    return render_template('properties.html',property=property)

@app.route('/properties/<property_id>', methods=['GET', 'POST'])
def property(property_id):
    property= properties.query.filter_by(property_id=property_id)
    return render_template('property.html',property=property)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='project1',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
