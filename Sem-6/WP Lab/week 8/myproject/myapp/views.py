from django.shortcuts import render, redirect

def first_page(request):
    subjects = ["Math", "Science", "History", "English", "Computer Science"]
    
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        subject = request.POST.get("subject")

        request.session["name"] = name
        request.session["roll"] = roll
        request.session["subject"] = subject

        return redirect("second_page")  
    
    return render(request, "firstPage.html", {"subjects": subjects})

def second_page(request):
    name = request.session.get("name", "Unknown")
    roll = request.session.get("roll", "Unknown")
    subject = request.session.get("subject", "Unknown")

    return render(request, "secondPage.html", {"name": name, "roll": roll, "subject": subject})
