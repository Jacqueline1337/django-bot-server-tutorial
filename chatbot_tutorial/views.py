from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render


def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    Info = {
     'advice': ["""Do what you want but make sure it's nothing that would impact you negatively.""","""Try everything.""","""Failing is okay you learn from it. However sometimes it's better to learn from the mistakes of others.""","""If your worried about college then make an appointment with your college adviser.""","""Challenge yourself and take things seriously.""","""Stay open-minded.""","""Do internships related to the career you wish to follow.""",
                """Apply early to scholarships."""],
     'motivation':    ["""A river cuts through rock, not because of its power, but because of its persistence. - Jim Watkins""","""Long-term consistency trumps short-term intensity. - Bruce Lee""","""Work hard in silence, let your success be your noise. -Frank Ocean""","""Raise your words, not voice. It is rain that grows flowers, not thunder. - Rumi""","""Don't wait for a opportunity. Create it. -Unknown""","""Push yourself because, no one else is going to do it for you. -Unknown""",
                """Don't watch the clock; do what it does. Keep going. -Sam Levenson"""],
     'fun facts':   ["""I like learning new languages. - Jacqueline M.""","""I want to become a orthopedic surgeon. - Jacqueline M.""","""I want to open up my own clinic. - Jacqueline M.""","""I like going swimming and hiking. - Jacqueline M.""","""I like traveling. - Jacqueline M.""","""I was born in Ukraine. - Vanesa M.""","""My parents are my BFF's. - Vanesa M.""","""I am Baptist. - Vanesa M.""","""I am uber conservative. - Vanesa M.""","""I want to adopt 10 kids. - Vanesa M.""",""" I love macarons. - Julia D.""","""My favorite show is Gossip Girl (Team Blair). - Julia D.""","""I hope to visit Japan someday
. - Julia D.""","""I'm not very outdoorsy, but I love horseback riding
. - Julia D.""",
                """My favorite flowers are Calla Lilies and Peonies."""],
     }

    result_message = {
        'type': 'text'
    }
    if 'motivation' in message['text']:
        result_message['text'] = random.choice(Info['motivation'])

    elif 'advice' in message['text']:
        result_message['text'] = random.choice(Info['advice'])

    elif 'fun facts' in message['text']:
        result_message['text'] = random.choice(Info['fun facts'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in hearing advice, motivation, or fun facts about us please feel free to tell me so."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in hearing advise, motivation, or fun facts about us please feel free to tell me so."
    return result_message
