from django.http import HttpResponse

from django.template import loader
from django.template.loader import get_template
# def index(request):
#     latest_question_list = ['a','b','c']
#     template = loader.get_template('product/index.html')
#     context = {
#         'latest_question_list': 'string',
#     }
#     return HttpResponse(template.render(context, request))


from django.shortcuts import render
from django.http import HttpResponseRedirect

from product.forms import NameForm
from product.forms import SelectForm

from product.crawlers import Crawler

def name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # print(request.POST)
        form = NameForm(request.POST)
        print("debug 0")
        result = str(form["your_product"].value())

        print(form["your_product"].value())
        # check whether it's valid:
        if form.is_valid():
            print("insidwee......")
            a,b = Crawler.crawl('amazon',form["your_product"].value())
            dictionary = dict(zip(b, a))
            print(dictionary)
            c,d = Crawler.crawl('snapdeal',form["your_product"].value())
            print(c)
            print(d)
            dictionary2 = dict(zip(d, c))
            print(dictionary2)
            return render(request, "name.html" , {'form' : form ,'amazon_url_list':a,'amazon_names':dictionary , 'flipkart_url_list':c,'flipkart_names':dictionary2})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def results(request):  
    text = request.session.get("text", None)
    c = {'text' : text}
    return render_to_response('results.html', c)




def index(request):
    latest_question_list = ['a','b','c']
    template = get_template('/home/harshita/Desktop/myproduct/product/templates/product/index.html')
    context = {
        'latest_question_list': 'string',
    }
    return HttpResponse(template.render(context, request))

def input_crawl(result):
    a,b = Crawler_crawl('amazon','moto g3')
    print(a)
    print(b)

def selected(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SelectForm(request.POST)
        print("debugggg 0")
        resultt = (form["selected_choice"].value())
        print(resultt)
        print(form["selected_choice"].value())
        # check whether it's valid:
        if form.is_valid():
            print("debug_inside")
        else:
            print("debug !form is_valid")

            return render(request, "selected.html" , {'form' : form,'resultt':resultt})
