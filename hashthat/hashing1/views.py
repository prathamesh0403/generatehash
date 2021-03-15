from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib

# Create your views here.
def index(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            hash_text = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=hash_text)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = hash_text
                hash.save()
            return redirect('hash', hash=hash_text)
    form = HashForm()
    return render(request , 'index.html', {'form':form})

def hash(request, hash):
    hash = Hash.objects.get(hash=hash)
    return render(request, 'hash.html', {'hash':hash})