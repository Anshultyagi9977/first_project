from django.shortcuts import render, HttpResponse
from myapp.models import StudentData, UserData, BookDetails, ConsumerDetails, ItemInventory, StudentStatus, BankDetails


# Create your views here.
def render_student_form(request):
    return render(request, 'student_form.html')

def register_student(request):
    print(request.__dict__)
    if request.method == 'POST':
        name = request.POST.get('name')
        std = request.POST.get('std')
        rollNo = request.POST.get('rollno')

        student_data = StudentData()
        student_data.name = name
        student_data.std = std
        student_data.roll_no = rollNo

        student_data.save()
        return HttpResponse("you are successfully registered")

def render_user_form(request):
    return render(request, 'user_form.html')

def register_user(request):

    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add1')
        city = request.POST.get('city')
        zip = request.POST.get('zip')

        user_form = UserData()
        user_form.name = name
        user_form.email = email
        user_form.address = add1
        user_form.address2 = add2
        user_form.city = city
        user_form.zip = zip

        user_form.save()
        return HttpResponse("you are sussesfully submitted")


def render_book_details(request):
    return render(request, 'book_details.html')

def book_details(request):

    if request.method =='POST':

        book_detail = BookDetails()
        book_detail.book_name = request.POST.get('name')
        book_detail. book_id =request.POST.get('Book_id')
        book_detail.book_author = request.POST.get('Book_author')
        book_detail.assigned =request.POST.get('assigned')
        book_detail.due_date = request.POST.get('Due_Date')

        book_detail.save()
        return HttpResponse("yor book detail has been saved")

def render_consumer_details(request):
    return render(request,'consumer_details.html')

def consumer_details(request):

    if request.method =='POST':

        consumer_details = ConsumerDetails()
        consumer_details.name = request.POST.get('Name')
        consumer_details.mobile_No = request.POST.get('Mobile_No')
        consumer_details.location = request.POST.get('Location')
        if request.POST.get('Active') == "on":
            consumer_details.active = True
        else:
            consumer_details.active = False
        consumer_details.started_date = request.POST.get('Started_Date')

        consumer_details.save()
        return HttpResponse("your consumer details has been saved")

def render_item_inventory(request):
    return render(request,'Item_Inventory.html')

def item_inventory(request):

    if request.method == 'POST':


        item_inventory = ItemInventory()
        item_inventory.Item_Name = request.POST.get('Item_Name')
        item_inventory.Piece_Created = request.POST.get('Piece_Created')
        item_inventory. Piece_Sold = request.POST.get('Piece_Sold')
        if request.POST.get('Piece_Sold') >= request.POST.get('Piece_Created'):
            item_inventory.Out_Of_Stock = True
        else:
            item_inventory.In_Stock = True


        item_inventory.save()
        return HttpResponse("your item in inventory")

def render_student_status(request):
    return render(request,'student_status.html')

def student_status(request):

    if request.method == 'POST':
        req_att = request.POST.get('Required_Attendence')

        student_status = StudentStatus()
        student_status.name = request.POST.get('Name')
        student_status.required_attendence = req_att
        student_status.present = request.POST.get('Present')
        student_status.total_days = request.POST.get('Total_Days')
        per_attend = (int(request.POST.get('Present'))*100)/int(request.POST.get('Total_Days'))

        if per_attend >= int(req_att):
            student_status.allowed = True
        else:
            student_status.detained = True

        student_status.save()
        return HttpResponse('student detained list' )

def render_bank_details(request):
    return render(request,'bank_details.html')

def bank_details(request):

    if request.method =='POST':

        bank_details = BankDetails()
        bank_details.name = request.POST.get('Name')
        bank_details.age = request.POST.get('Age')
        if request.POST.get('Expired') == "on":
            bank_details.expired = True
            bank_details.active = False
        else:
            bank_details.expired = False
            bank_details.active = True


        bank_details.save()
        return HttpResponse("submit data")







