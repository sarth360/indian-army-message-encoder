from django.shortcuts import render
from .forms import MessageForm
from .utils import encode_message

def encode_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            day_type = form.cleaned_data['day_type']
            encoded_message = encode_message(message, day_type)
            return render(request, 'encoder/result.html', {'encoded_message': encoded_message})
    else:
        form = MessageForm()
    return render(request, 'encoder/encode.html', {'form': form})

