from django.shortcuts import render
from django.shortcuts import render, reverse

import recipes

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home(request):
    template_name = 'calculator/prodauct.html'
    recipe = {}
    for key, value in DATA.items():
        new_key = f"Рецепт {key}"
        recipe[new_key] = reverse('recipies', args=[key, 1])
    return render(request, template_name, {'recipe': recipe})

def product(request, recipies, b=1):
    template_name = 'calculator/index.html'
    foods = DATA[recipies]
    recipe = {}
    for food in foods:
        recipe[food] = foods[food] * b
    return render(request, template_name, {'recipe': recipe})


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
