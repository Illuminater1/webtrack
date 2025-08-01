from flask import Blueprint, render_template
from ..user.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/admin')
@admin_required
def admin_index():
    title = 'Панель администратора'
    return render_template('admin/index.html', page_title=title)
