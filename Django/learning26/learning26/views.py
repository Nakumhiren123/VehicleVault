from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def movies(request):
    return render(request,"movies.html")

def shows(request):
    return render(request,"shows.html")

def news(request):
    return render(request,"news.html")

def recipe(request):
    ingredients = ["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredients} 
    return render(request,"recipe.html",data)

def team(request):
    Wicketkeepers = ["MS Dhoni", "Sanju Samson", "Urvil Patel", "Kartik Sharma"]
    Batters = ("Ruturaj Gaikwad", "Dewald Brevis", "Sarfaraz Khan", "Ayush Mhatre")
    AllRounders = ["Ravindra Jadeja", "Shivam Dube", "Aman Khan", "Anshul Kamboj", "Jamie Overton", "Matthew Short"]
    Bowlers = ["Matheesha Pathirana", "Deepak Chahar", "Khaleel Ahmed", "Nathan Ellis", "Noor Ahmad", "Shreyas Gopal", "Mukesh Choudhary", "Gurjapneet Singh"]
    data = {"TeamName":"CSK", "CaptainName": "Ruturaj Gaikwad", "trophy":8, "wicketkeeper": Wicketkeepers, "batter": Batters, 
            "allrounder" : AllRounders, "bowler": Bowlers}
    return render(request, "teams.html", data)



def College(request):
    Departments = ["Computer Science", "Mechanical", "Electrical", "Civil"]
    Professors = ("Dr. Sharma", "Dr. Patel", "Dr. Mehta", "Dr. Rao")
    Courses = ["Data Structures", "DBMS", "Operating Systems", "Computer Networks"]
    Labs = ["DS Lab", "DBMS Lab", "OS Lab", "Networking Lab"]
    Clubs = ["Coding Club", "Robotics Club", "Cultural Club", "Sports Club"]

    data = {
        "CollegeName": "ABC Engineering College",
        "PrincipalName": "Dr. R. K. Verma",
        "EstablishedYear": 2000,
        "departments": Departments,
        "professors": Professors,
        "courses": Courses,
        "labs": Labs,
        "clubs": Clubs
    }

    return render(request, "college.html", data)
