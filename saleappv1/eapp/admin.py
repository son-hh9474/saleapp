from flask import redirect
from flask_admin.contrib.sqla import ModelView
from saleappv1.eapp.models import Category, Product, UserRoleEnum
from flask_admin import Admin, BaseView, expose
from saleappv1.eapp import app, db
from flask_login import logout_user, current_user
admin = Admin(app=app, name="E-commerce's Admin")

class AdminModeView(ModelView):

    def is_accessible(self) -> bool:

        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class ProductView(AdminModeView):
    column_list = ['id', 'name', 'price', 'category_id']
    column_searchable_list = ['name']
    can_export = True
    column_filters = ['name', 'price']
    edit_modal = True
    column_editable_list = ['name']

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

admin.add_view(AdminModeView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view((LogoutView(name="Đăng xuất")))