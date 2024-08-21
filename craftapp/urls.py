from django.urls import path
from . import views



urlpatterns = [

    # path('',views.index),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('sellerhome/',views.sellerhome,name="sellerhome"),
    path('tutorhome/',views.tutorhome,name="tutorhome"),
    path('userhome/',views.userhome,name="userhome"),

    path('seller_reg/',views.seller_reg,name="seller_reg"),
    path('user_reg/',views.user_reg,name="user_reg"),
    path('tutor_reg/',views.tutor_reg,name="tutor_reg"),

    # path('appointment/',views.appointment,name="appointment"),

    path('call-to-action/',views.call_to_action,name="call-to-action"),
    path('classes/',views.classes,name="classes"),
    path('contact/',views.contact,name="contact"),
    path('facility/',views.facility,name="facility"),
    path('index/',views.index,name="index"),
    path('team/',views.team,name="team"),
    path('testimonials/',views.testmonial,name="testimonials"),

    path('sellerlogin/',views.sellerlogin,name="sellerlogin"),
    path('tutorlogin/',views.tutorlogin,name="tutorlogin"),
    path('userlogin/',views.userlogin,name="userlogin"),

    path('craftselling/',views.craftselling,name="craftselling"),
    path('accessory_selling/',views.accessory_selling,name="accessory_selling"),
    path('seller_profile/',views.seller_profile,name="seller_profile"),
    path('seller_manage_items/',views.seller_manage_items,name="seller_manage_items"),
    
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('deletee_itemm/<int:id>',views.deletee_itemm,name='deletee_itemm'),
 
    path('tutor_profile/',views.tutor_profile,name="tutor_profile"),
    path('user_profile/',views.user_profile,name="user_profile"),
    path('sellerupdate/',views.sellerupdate,name="sellerupdate"),
    path('updatesellerprofile/',views.updatesellerprofile,name="updatesellerprofile"),
    path('user_update/',views.user_update,name="user_update"),
    path('tutor_update/',views.tutor_update,name="tutor_update"),
    path('updatetutorprofile/',views.updatetutorprofile,name="updatetutorprofile"),
    
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_user/',views.admin_user,name="admin_user"),
    path('admin_user_remove/<int:id>',views.admin_user_remove,name='admin_user_remove'),
    path('admin_reg_user/',views.admin_reg_user,name="admin_reg_user"),
    path('admin_reg_user_remove/<int:id>',views.admin_reg_user_remove,name='admin_reg_user_remove'),
    path('admin_accesories/',views.admin_accesories,name="admin_accesories"),
    path('admin_accesories_remove/<int:id>',views.admin_accesories_remove,name='admin_accesories_remove'),
    path('admin_seller/',views.admin_seller,name="admin_seller"),
    path('admin_seller_remove/<int:id>',views.admin_seller_remove,name='admin_seller_remove'),
    path('admin_tutor/',views.admin_tutor,name="admin_tutor"),
    path('admin_tutor_remove/<int:id>',views.admin_tutor_remove,name='admin_tutor_remove'),
    path('admin_craft_selling/',views.admin_craft_selling,name="admin_craft_selling"),
    path('admin_craft_remove/<int:id>',views.admin_craft_remove,name='admin_craft_remove'),
    # path("listitems/",views.listitems,name="listitems"),
    # path("craft_listitems/",views.craft_listitems,name="craft_listitems"),
    path("accessory_list_items/", views.accessory_list_items, name="accessory_list_items"),
    path("craft_list_items/", views.craft_list_items, name="craft_list_items"),
    path('cart/<int:id>',views.cart,name='cart'),
    path('addcart/',views.addcart,name='addcart'),
    path('cartlist/',views.cartlist,name='cartlist'),
    path('craftcart/<int:id>',views.craftcart,name='craftcart'),
    path('craftaddcart/',views.addcraftcart,name='addcraftcart'),
    path('craftcartlist/',views.craftcartlist,name='craftcartlist'),
    path('delete1/<int:id>',views.delete1,name='delete1'),
    path('delete2/<int:id>',views.delete2,name='delete2'),
    path('payment/',views.payment,name='payment'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('payment1/',views.payment1,name='payment1'),
    path('paymenthandler1/', views.paymenthandler1, name='paymenthandler1'),
    path('videos/', views.video_list, name='video_list'),
    path('videos/add/',views. add_video, name='add_video'),
    path('videos/edit/<int:pk>/', views.edit_video, name='edit_video'),
    path('videos/delete/<int:pk>/', views.delete_video, name='delete_video'),
    path('user/videos/', views.user_video_list, name='user_video_list'),  # New URL for user video list
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    # path('edit_accerios/<int:item_id>/', views.edit_accerios, name='edit_accerios'),
    # path('deletee_itemm/<int:id>/', views.craftdeletee_itemm, name='deletee_itemm'),
    path('edit_accerios/<int:item_id>/', views.edit_accerios, name='edit_accerios'),
    path('craftdeletee_itemm/<int:id>/', views.deletee_itemm, name='craftdeletee_itemm'),
]