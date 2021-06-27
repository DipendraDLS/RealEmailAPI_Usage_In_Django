from django.shortcuts import render

import requests

# Create your views here.

def home(request):
    if request.method == "POST":
        email = request.POST['email']


        api_key = '8d7e1b7f-022b-4bf5-8661-ac2f949a1a1c'        # With an API key you wont be limited by how many addresses you can check
                                                                # To get the  API key you need to signup in Real Email API website: https://isitarealemail.com/register
                                                                # i have signedin from my 'dipen.stha8786@gmail.com' email address
                                                                # IMP_NOTE: if you are not signed in user and u don't have API Key then also you can use this Real Email API .. But there is limitation without API Key as you can  only test for 100 emails per day

        response = requests.get(
            "https://isitarealemail.com/api/email/validate",       # API ko end point
            params={'email': email},                                # hamro email as a params pathauna parcha
            headers = {'Authorization': "Bearer " + api_key})       # API key lai chai headers vanni field ma 'Authorization' as a headers send garna parcha


        status = response.json()['status']                          # response ma ayeko kura lai json ma lageko
                                                                    # email valid cha vani status ma 'valid' response auncha else 'invalid' auncha ..
                                                                    # yedi user le jpt domain vako email eg: aaaa@bbb.com yesto diyo vani 'unknown' response auncha becz yo email bata kei tha hunaa becz mail server ko name nai jpt diyeko cha

        if status == "valid":
            context = {
                'success_response': 'The email address: ' + email + ' that you have entered is valid and exists in real world.'}
            return render(request, 'validator/home.html', context)
        else:
            context = {
                'error_response': 'The email address: ' + email + ' that you have entered does not exists in real world.'}

            return render(request, 'validator/home.html', context)

    return render(request, 'validator/home.html')
