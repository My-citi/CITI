from django.shortcuts import render
import json
from demo import models
from django.db.models import Q


def echarts1(request):
    all_things = models.UnemploymentRate19482010.objects.filter(year='2020').filter(code__endswith='0000').values(
        'name', 'value').distinct()
    # print(all_things)
    data_salary = []
    for i in all_things:
        i['name'] = i['name'].replace('省', '').replace('自治区', '').replace('壮族', '').replace('维吾尔', '').replace('回族', '')
        i['value'] = float(i['value'])
        data_salary.append(i)
    print(data_salary)


    DEVELP_GDP = models.City_GDP.objects.order_by('value_2019').values('name', 'value_2019')
    name = []
    value = []
    for i in DEVELP_GDP:
        name.append(i['name'])
        value.append(i['value_2019'])


    all_city_data = models.City_GDP.objects.order_by('value_2019').values('name', 'value_2019', 'value_2018',
                                                                          'value_2017', 'value_2016', 'value_2015',
                                                                          'value_2014', 'value_2013', 'value_2012',
                                                                          'value_2011', 'value_2010')
    city_data = {}
    for g in all_city_data:
        city_data.update({g['name']: [g['value_2010'], g['value_2011'], g['value_2012'], g['value_2013'],
                                      g['value_2014'], g['value_2015'], g['value_2016'], g['value_2017'],
                                      g['value_2018'], g['value_2019']]})
    patents_data = {}
    patents_pie_data = []
    for g in models.City_Patents.objects.order_by('-value_2019').values('name', 'value_2019', 'value_2018',
                                                                        'value_2017', 'value_2016', 'value_2015',
                                                                        'value_2014', 'value_2013', 'value_2012',
                                                                        'value_2011', 'value_2010'):
        patents_data.update({g['name']: [g['value_2010'], g['value_2011'], g['value_2012'], g['value_2013'],
                                         g['value_2014'], g['value_2015'], g['value_2016'], g['value_2017'],
                                         g['value_2018'], g['value_2019']]})
        patents_pie_data.append({"name": g['name'], "value": g['value_2019']})

    Renthouseprice=[]
    # print(data_salary)
    second=[]
    Third=[]
    first=[]
    for i in data_salary:
        first.append(i['value'])
    first=first[0:8]
    for i in models.Renthouseprice.objects.values('city2233', 'Average'):
        Renthouseprice.append({"name": i['city2233'], "value": round(i['Average']*50,2)})
    Money_use = [{"name": i['Name'], "value": round(i['Money']/12,2)} for i in models.Money.objects.values('Name', 'Money')]
    for i in Renthouseprice:
        second.append(i['value'])
    for i in Money_use:
        Third.append(i['value'])
    second=second[0:8]
    Third=Third[0:8]
    ddere=[]
    for i in data_salary:
        ddere.append(i['name'])
    ddere=ddere[0:8]
    # 住房 + salary + money_to_use


    potenial=[]
    for ssr in models.Potential.objects.values('Name', 'Value'):
        potenial.append({'name':ssr['Name'],'value':ssr['Value']})

    Five_00= []
    for j in models.Five.objects.values('city_name','Name'):
        Five_00.append({'name': j['city_name']})
    r = map(lambda x: x.values(), Five_00)
    ertt=[j for i in list(r) for j in i]
    ererer=[{i:ertt.count(i)} for i in ertt]
    li = [dict(t) for t in set([tuple(d.items()) for d in ererer])]
    Five_00=[]
    for i in li:
        Five_00.append({'name': list(i.keys())[0],'value':list(i.values())[0]})



    print('--------',second,Third,ddere)



    return render(request, 'index.html', {'data_salary': data_salary,
                                          'name': name,
                                          'value': value,
                                          'city_data': city_data,
                                          'patents_history_data': patents_data,
                                          'patents_pie_data': patents_pie_data[0:16],
                                          'potenial':potenial,
                                          'Five_00':Five_00,

                                          'ddere':ddere,
                                          'first':first,
                                          'second':second,
                                          'third':Third
                                          })
