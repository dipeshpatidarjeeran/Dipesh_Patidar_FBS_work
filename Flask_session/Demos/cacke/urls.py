from main import app

import category_op as cat
import cake_op as cak
import admin as a
import user

app.add_url_rule('/addCategory',view_func=cat.addCategory,methods=["GET","POST"])
app.add_url_rule('/showAllCategory',view_func=cat.showAllCategory,methods=["GET"])
app.add_url_rule('/deleteCategory/<cid>',view_func=cat.deleteCategory,methods=["GET","POST"])
app.add_url_rule('/updateCategory/<cid>',view_func=cat.updateCategory,methods=["GET","POST"])
app.add_url_rule('/addCake',view_func=cak.addCake,methods=["GET","POST"])


app.add_url_rule('/adminLogin',view_func=a.adminLogin,methods=["GET","POST"])
app.add_url_rule('/adminLogout',view_func=a.adminLogout)
app.add_url_rule('/adminDashboard',view_func=a.adminDashboard)

app.add_url_rule("/",view_func=user.homepage)
app.add_url_rule("/searchCake",view_func=user.searchData, methods=["GET","POST"])
app.add_url_rule("/MakePayment",view_func=user.MakePayment,methods = ["GET","POST"])



create table Order_Master (order_id int primary key auto_increment,date_of_order date,amount float);
alter table mycart add order_id int ;
alter table mycart add foreign key(order_id) references order_master(order_id) ;
alter table mycart add status int default  0;