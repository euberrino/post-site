from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404, HttpResponse

posts={
   "Mi first post":"This is the first post I ever write in a webpage.",
   "Getting to know me":"I've got many interests. The purpose of this blog is to share my learning trip with you guys.",
   "My pytohon journey": "I've been coding for 4 years now. It's been a long time. Back in those days I used to be such a mess.",
   "Mental Healthcare lessons":"I sometimes struggle with it, as I want to learn and learn and there is infinte information going out each and every single day. Here are my tips for staying updated and not getting mentally burnt out in the try.",

}

# Create your views here.
def index(request):
   last_posts=list(reversed(posts))[0:3]
   print(last_posts)
   return  render(request, 'blog/index.html',{'posts':last_posts})

def get_all_posts(request):
   return render(request, 'blog/posts.html',{'posts':posts})

def get_post(request,slug):
   try:
    return render(request,'blog/post.html',{'name':slug,'text':posts[slug]})
   except:
      raise Http404()