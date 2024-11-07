from django.shortcuts import render
from .models import Chat
import openai
import time
from userAuth.models import User

openai.api_key = API_KEY


def chat(request):
    if request.method == 'POST':
        print('here')
        question = request.POST['input']
        print(question)
        # print(request.user)
        response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        'role': 'user',
                        'content':  question
                    }]
                )
        assistant_response = response['choices'][0]['message']['content']
        assistant_response = assistant_response.strip("\n" ).strip()
        current_user = User.objects.get(id=1)
        print(current_user) 
        chat = Chat.objects.create(question=question, response=assistant_response, user=current_user)
        
        all_chats = Chat.objects.all()
        print(all_chats)
        print(chat.response)
        return render(request, 'index.html', {'current_chat': chat, 'chats': all_chats})
    if request.method == 'GET':
        try:    
            all_chats = Chat.objects.all()
        except:
            pass

        return render(request, 'index.html')

