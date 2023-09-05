import openai
from django.shortcuts import render


def chatbot(request):
    predefined_responses = {
        "destination_question": "This is a response about destinations.",
        "accommodation_question": "Here's some information about accommodations.",
        # Define more predefined responses here.
    }

    # Retrieve the user's question from the HTTP POST data
    user_question = request.POST.get('question', '')

    # Look up the predefined response based on the user's question
    response = predefined_responses.get(user_question, '')

    # Use OpenAI API to generate a response based on user_question
    openai.api_key = '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'
    
    if user_question:
        ai_response = openai.Completion.create(
            engine="davinci",  # You can choose an appropriate OpenAI engine
            prompt=user_question,
            max_tokens=50,  # Adjust as needed
            n=1,  # Number of responses to generate
            stop=None  # You can specify stop words to control response length
        )
        combined_response = response + ai_response.choices[0].text
    else:
        combined_response = response

    return render(request, 'chatbot/chatbot.html', {'response': combined_response})
