from django.shortcuts import render,redirect
from homepage.models import userinfo
from .decorators import login_required
from .models import Expense
from datetime import datetime
from django.db.models import Sum

# Create your views here.
@login_required
def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login/')

    user_info = userinfo.objects.get(id=user_id)

    # Total this month
    now = datetime.now()
    total_month_expense = Expense.objects.filter(
        user_id=user_id,
        date__year=now.year,
        date__month=now.month
    ).aggregate(total=Sum('cost'))['total'] or 0

    # Total all time
    total_all_time = Expense.objects.filter(
        user_id=user_id
    ).aggregate(total=Sum('cost'))['total'] or 0
    
    category_data = Expense.objects.filter(user_id=user_id).values('category').annotate(total=Sum('cost'))

    data = {
        'name': user_info.name,
        'total_month_expense': total_month_expense,
        'total_all_time_expense': total_all_time,
        'category_data': category_data
    }

    return render(request, 'dashboard.html', data)

@login_required
def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login/')
    user_info = userinfo.objects.get(id=user_id)
    data = {
        'name' : user_info.name,
        'email' : user_info.email,
        
    }
    return render(request, 'profile.html',data)


def add_expense(request):
    if request.method == "POST":
        title = request.POST.get('title')
        cost = request.POST.get('cost')
        category = request.POST.get('category')

        user_id = request.session.get('user_id')  # ✅ Get user ID from session
        if user_id:
            Expense.objects.create(
                user_id=user_id,
                title=title,
                cost=cost,
                category=category
            )
        
        return redirect('/dashboard/')

def view_info(request):
    user_id = request.session.get('user_id')
    expenses = Expense.objects.filter(user_id=user_id)
    
    
    return render(request,'view_info.html',{'expenses' : expenses})