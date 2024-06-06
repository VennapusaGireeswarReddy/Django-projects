from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 

# write your views here.

def report(request): 
    if request.method == 'POST': 
        city = request.POST.get('city')
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=f6fda004cef1bc0c65b5e3a8f7a7226a').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "countrycode": str(list_of_data['sys']['country']),
             "city" :city,
            "coordinate": str(list_of_data['coord']['lon']) + ', '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
        return render(request,'report.html',{"data":data})
    else: 
        data ={} 
    return render(request, "report.html", )