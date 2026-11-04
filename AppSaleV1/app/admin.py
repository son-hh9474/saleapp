from flask_admin.contrib.sqla import ModelView

from AppSaleV1.app.models import Category, Product, db
from AppSaleV1.app import app
from flask_admin import Admin

class ProductView(ModelView):
    column_list = ['id', 'name', 'active', 'category_id']
    column_searchable_list = ['name']
    can_export = True
    edit_modal = True
    column_editable_list = ['name', 'active']
    column_filters = ['name', 'price']


admin = Admin(app=app, name="Ecommerce's Admin")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))

