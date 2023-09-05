import openai
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def chatbot(request):
    predefined_responses = {
    "destinations": [
        {
            "Destination1": "Queen Elizabeth National Park",
            "Destination2": "Bwindi Impenetrable",
            "Destination3": "Source of the Nile"
        }
    ],
    "accommodation": [
        {
            "Accommodation1": "Mweya Lodge in Queen Elizabeth National Park",
            "Accommodation2": "Ngorongoro Hotel in Bwindi Impenetrable",
            "Accommodation3": "Riverside Campsite near the Source of the Nile"
        }
    ],
    "activities": [
        {
            "Activity1": "Safari and wildlife viewing in Queen Elizabeth National Park",
            "Activity2": "Gorilla trekking in Bwindi Impenetrable Forest",
            "Activity3": "White-water rafting at the Source of the Nile"
        }
    ]
}

    user_question = request.POST.get('question', '')
    response = ''

    if 'destination' in user_question.lower():
        response = predefined_responses.get('destinations', [])
    elif 'accommodation' in user_question.lower():
        response = predefined_responses.get('accommodation', [])
    elif 'activity or activities' in user_question.lower():
        response = predefined_responses.get('activities', [])
    else:
        response = "I'm not sure how to answer that. You can ask about destinations, accommodations, or activities in Uganda."

    openai.api_key = ''

    if user_question:
        ai_response = openai.Completion.create(
            engine="davinci",
            prompt=user_question,
            max_tokens=50,
            n=1,
            stop=None
        )
        combined_response = response + [ai_response.choices[0].text]
    else:
        combined_response = response

    return render(request, 'chatbot/chatbot.html', {'response': combined_response})
