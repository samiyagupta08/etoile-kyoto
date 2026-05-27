from django.shortcuts import render, redirect
from .models import Reservation
from datetime import datetime

def reserve(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests')

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time = datetime.strptime(time_str, '%H:%M').time()
            guests = int(guests)
            
            reservation = Reservation.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
                guests=guests,
                special_requests=special_requests
            )
            
            return render(request, 'reservations/reserve.html', {
                'success': True,
                'reservation': reservation
            })
        except Exception as e:
            return render(request, 'reservations/reserve.html', {
                'error': 'Invalid inputs. Please check your reservation details.',
                'values': request.POST
            })

    return render(request, 'reservations/reserve.html')
