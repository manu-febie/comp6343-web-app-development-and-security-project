from flask import Blueprint, render_template, url_for

pages = Blueprint('pages', __name__)

@pages.route('/')
def index():
    '''
    Pages route that returns the homepage of the web app

    :return: homepage
    '''

    return render_template('index.html')
