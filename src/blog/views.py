from django.shortcuts import render

# Create your views here.
# Create your tests here.
def Home(request):
    template_name = 'home.html'
    return render(request, template_name)

def Blog(request):
    template_name = 'Blog/blog.html'
    context = {}
    return render(request, template_name, context)
