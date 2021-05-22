from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args
import pandas as pd

app = Flask(__name__)
#app.template_folder = ''

df = pd.read_csv('data.csv')
data = df.to_dict(orient = 'records')


def get_page_per_users(offset=0, per_page=20):
    """method to create data per page """  
    return data[offset: offset + per_page]

@app.route('/')
def index():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(data)
    pagination_users = get_page_per_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, 
                            per_page=per_page, 
                            total=total,
                            css_framework='bootstrap4')
    return render_template('index.html',
                           data=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)
                           

if __name__ == '__main__':
    app.run(debug=True)       
