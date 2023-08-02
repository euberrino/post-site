from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404, HttpResponse
from datetime import date

# posts={
#    "Mi first post":"This is the first post I ever write in a webpage.",
#    "Getting to know me":"I've got many interests. The purpose of this blog is to share my learning trip with you guys.",
#    "My pytohon journey": "I've been coding for 4 years now. It's been a long time. Back in those days I used to be such a mess.",
#    "Mental Healthcare lessons":"I sometimes struggle with it, as I want to learn and learn and there is infinte information going out each and every single day. Here are my tips for staying updated and not getting mentally burnt out in the try.",

# }
posts = [
    {
        "slug": "my-first-post",
        "image": "writing-blog.jpg",
        "author": "chat gpt",
        "date": date(2023, 7, 21),
        "title": "The Bioengineer’s Blog: Adventures in Data, Product, and Python",
        "excerpt": """Welcome to The Bioengineer’s Blog: Adventures in Data, Product, and Python! My name is Eugenia and I’m a 26-year-old bioengineer with a passion for data analysis,
   product development, and teaching. Join me as I share my experiences and insights into the world of bioengineering and beyond. From python development to biostatistics, 
   fitness to writing, there’s never a dull moment in the life of a bioengineer. Stay tuned for more posts!""",
        "content": """
   Hello world! My name is Eugenia and I’m a 26-year-old bioengineer. I’ve worked as a python developer, though my main focus is in data and product. 
   I also teach biostatistics at the university and love learning new things. 
   In this blog, I’ll be sharing my experiences and insights into the world of bioengineering,
   data analysis, and product development. I’ll also be talking about my passion for teaching and how I find writing to be a stimulating and rewarding experience.
   When I’m not working or teaching, you can find me training at the gym or at home. Fitness is an important part of my life and helps me stay focused and energized.
   I’m excited to share my journey with you and hope you’ll join me on this adventure. Stay tuned for more posts!
   """
    }
]


def get_date(post):
    return post['date']

# Create your views here.


def index(request):
    last_posts = sorted(posts, key=get_date)[-3:]
    print(last_posts)
    return render(request, 'blog/index.html', {'posts': last_posts})


def get_all_posts(request):
    return render(request, 'blog/posts.html', {'posts': posts})


def get_post(request, slug):
    try:
      selected_post = next(post for post in posts if post['slug']==slug)
      return render(request, 'blog/post.html', {'post': selected_post})
    except:
        raise Http404()
