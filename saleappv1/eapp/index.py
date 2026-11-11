import math
from typing import Type

from flask import render_template, request
from flask import redirect
from flask_login import login_user
from saleappv1.eapp import app, dao, login



@app.route("/")
def index():
    products = dao.load_products(kw=request.args.get('kw'),
                                 cate_id=request.args.get('category_id'),
                                 page=int(request.args.get('page', 1)))
    page_size = app.config['PAGE_SIZE']
    return render_template('index.html', products=products, pages=math.ceil(dao.count_products()/page_size))


@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    print(type(username), type(password))
    u = dao.authenticate(username=username, password=password)
    if u:
        login_user(user=u)
    return redirect('/admin')

@app.route('/register')
def register_view():
    return render_template('login.html')

@app.context_processor
def common_responses():
    categories = dao.load_categories()

    return {
        'categories': categories
    }
@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    with app.app_context():
        from saleappv1.eapp import admin
        app.run(debug=True)
