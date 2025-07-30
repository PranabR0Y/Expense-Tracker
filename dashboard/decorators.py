from django.shortcuts import redirect


def login_required(view_func):
    def wrapper(request,*args,**krgs):
        if 'user_id' not in request.session:
            return redirect('/login/')
        return view_func(request,*args,**krgs)# ✅ Proceed to actual view

    return wrapper