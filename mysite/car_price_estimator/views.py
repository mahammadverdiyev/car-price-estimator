from django.http import HttpResponse
from django.shortcuts import render
import car_price_estimator.estimator_tool as et


def index(request):
    ctx = {}
    return render(request, 'car_price_estimator/index.html', ctx)


def about(request):
    ctx = {}
    return render(request, 'car_price_estimator/about.html', ctx)


def estimate(request):
    if request.method == 'POST':
        brand = request.POST.get('auto[make_id]')
        model = request.POST.get('auto[model_id]')
        body_type = request.POST.get('auto[category_id]')
        distance_traveled = request.POST.get('auto[mileage]')
        color = request.POST.get('auto[color_id]')
        engine_power = request.POST.get('auto[power]')
        is_damaged = request.POST.get('auto[crashed]')
        is_painted = request.POST.get('auto[painted]')
        fuel_type = request.POST.get('auto[fuel_type_id]')
        powertrain = request.POST.get('auto[gear_id]')
        gearbox = request.POST.get('auto[transmission_id]')
        year = request.POST.get('auto[reg_year]')
        engine_volume = request.POST.get('auto[engine_volume]')

        new = "Bəli" if distance_traveled == '0' else 'Xeyr'

        data = {
            'brand': brand,
            'model': model,
            'year': year,
            'body_type': body_type,
            'color': color,
            'engine_volume': engine_volume,
            'engine_power': engine_power,
            'fuel_type': fuel_type,
            'distance_traveled': distance_traveled,
            'gearbox': gearbox,
            'powertrain': powertrain,
            'new': new,
            'is_damaged': is_damaged,
            'is_painted': is_painted,
        }

        prepared_data = et.prepare_data(data)

        estimated_price = et.predict_price(prepared_data)

        data['estimated_price'] = int(estimated_price)

        # print(estimated_price)

        return render(request, "car_price_estimator/result.html", data)
    else:
        return render(request, "car_price_estimator/index.html")
