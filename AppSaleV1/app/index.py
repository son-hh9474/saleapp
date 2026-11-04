import math

from flask import render_template, request

from AppSaleV1.app import app, dao


@app.route("/")
def index():

    product = dao.load_products(kw=request.args.get('kw'),
                                cate_id=request.args.get('category_id'),
                                page=int(request.args.get('page', 1)))


    page_size = app.config['PAGE_SIZE']

    return render_template("index.html", product=product, page=math.ceil(dao.count_product()/page_size))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.context_processor
def common_responses():
    return {
        'categories' : dao.load_categories()
    }

if __name__ == "__main__":
    with app.app_context():
        from AppSaleV1.app import admin
        app.run(debug=True)
