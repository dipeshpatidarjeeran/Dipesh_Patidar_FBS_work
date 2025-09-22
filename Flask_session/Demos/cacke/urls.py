from main import app

import category_op as cat
import cake_op as cak


app.add_url_rule('/addCategory',view_func=cat.addCategory,methods=["GET","POST"])
app.add_url_rule('/showAllCategory',view_func=cat.showAllCategory,methods=["GET"])
app.add_url_rule('/deleteCategory/<cid>',view_func=cat.deleteCategory,methods=["GET","POST"])
app.add_url_rule('/updateCategory/<cid>',view_func=cat.updateCategory,methods=["GET","POST"])
app.add_url_rule('/addCake',view_func=cak.addCake,methods=["GET","POST"])
