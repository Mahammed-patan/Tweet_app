from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import *

# Create your views here.

def Index(request):
    tweets = Tweet.objects.all().order_by('-id')
    context = {'tweets': tweets}
    return render(request, 'app/home.html', context)

def create_tweet(request):
    if request.method == 'POST':
        tweet_text = request.POST.get('tweet', '')
        source = request.POST['source']
        category = request.POST.get('selection', '')
        txt_len = len(tweet_text)

        if not tweet_text or not source:
            error_message = "Please fill in both the tweet text and source."
            return render(request, 'app/home.html', {'error': error_message})

        if len(tweet_text) > 200:
            error_message = "Tweet text cannot exceed 200 characters."
            return render(request, 'app/home.html', {'error': error_message})

        new_tweet = Tweet.objects.create(text=tweet_text, source=source, category=category)
        new_tweet.save()
        print(new_tweet.text)
        print(new_tweet.source)
        print(new_tweet.category)
        print(txt_len)
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'app/home.html')

def Category_tweet(request, data=None):
    if data == 'all':
        category_tweets = Tweet.objects.filter(category='all')
    elif data == 'fresher' or data == 'experienced':
        category_tweets = Tweet.objects.filter(category=data)
    context = {'tweets': category_tweets}  # Update context to send tweets
    return render(request, 'app/home.html', context)