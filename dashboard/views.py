from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Pokemon
from django.core import serializers

import requests

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):

    dataset = Pokemon.objects.all()
    url ='https://pokeapi.co/api/v2/pokemon-form/'
    offset = 0
    args = {'offset': offset} if offset else {}
    response = requests.get(url, params = args)
    final_list = []

    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results', [])

        name_list = []

        if results:
            for pokemon in results:
                name_list.append(pokemon['name'])
    
    pk = 0

    for pokemon_name in name_list:
        pk += 1
        p1 = Pokemon()
        data_dict = get_pokemons_data(pokemon_name, pk)
        final_list.append(data_dict)

    data = serializers.serialize('json', dataset)
    #data = final_list
    return JsonResponse(data, safe=False)

def get_pokemons_data(pokemon_name1, pk):

    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon_name1
    response = requests.get(url)

    if response.status_code == 200:
        
        payload = response.json()
        
        weight1 = payload.get('weight', [])
        
        base_experience1 = payload.get('base_experience', [])
        
        result = payload.get('types',[])
        pokemon_species = result[0]
        pokemon_type1 = pokemon_species.get('type').get('name')

        p1 = Pokemon(pokemon_name=pokemon_name1, base_experience=base_experience1,
                     pokemon_type=pokemon_type1, weight=weight1)
        p1.save()