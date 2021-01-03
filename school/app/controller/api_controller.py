from django.shortcuts import render
import requests, ast, json, urllib.request

def covid_info(request):
    url = 'https://api.kawalcorona.com/indonesia/'
    response = requests.get(url)
    data = response.json()
    if str(data)[0] == '[' :
        context1 = ast.literal_eval(str(data)[1:-1])
    else:
        context1 = ast.literal_eval(str(data))

    url2 = 'https://www.news.developeridn.com/'
    response2 = urllib.request.urlopen(url2)
    data2 = json.loads(response2.read().decode("utf-8"))
    if str(data2)[0] == '[' :
        context2 = ast.literal_eval(str(data2)[1:-1])
    else:
        context2 = ast.literal_eval(str(data2))
    
    context = {
        'covid' : context1,
        'news' : context2,
    }
    return render(request, 'appTemp/api/covid_info.html', context)