from django.urls import path, include
from myapp.views import render_student_form, register_student, render_user_form, register_user, render_book_details, \
    book_details, render_consumer_details, consumer_details, render_item_inventory, item_inventory, \
    render_student_status, student_status, render_bank_details, bank_details, get_student_data, \
    get_student_status, get_item_inventory, del_bank_details

urlpatterns = [
    path('show_student_form', render_student_form),
    path('register_student', register_student),
    path('show_user_form', render_user_form),
    path('register_user', register_user ),
    path('rbd', render_book_details ),
    path('save_book', book_details ),
    path('abc', render_consumer_details ),
    path('save_details', consumer_details ),
    path('created', render_item_inventory),
    path('sold',item_inventory ),
    path('student',render_student_status ),
    path('status',student_status ),
    path('bank',render_bank_details ),
    path('details',bank_details ),
    path('get_student_data',get_student_data),
    # path('bank_data', get_bank_details),
    path('student_status',get_student_status),
    path('student_status',get_student_status),
    path('inventory',get_item_inventory),
    path('del_name',del_bank_details),
]
