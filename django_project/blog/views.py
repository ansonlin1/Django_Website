from django.shortcuts import render

posts = [
	{
		'author' : 'Anson',
		'title' : 'Blog Post 1',
		'content' : 'First post content',
		'date_posted' : 'August 24, 2020'
	},
	{
		'author' : 'John',
		'title' : 'Blog Post 2',
		'content' : 'Second post content',
		'date_posted' : 'August 25, 2020'
	}
]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})