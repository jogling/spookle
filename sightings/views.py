from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models.functions import ExtractYear
from .models import Sighting
from .forms import SightingForm

from django.db.models import Q

@login_required
def sightings(request):
    sightings = Sighting.objects.all()
    years = Sighting.objects.annotate(year=ExtractYear('date')).values_list('year', flat=True).distinct().order_by('-year')

    ghost_type = request.GET.get('ghost_type')
    location = request.GET.get('location')
    year = request.GET.get('year')

    if ghost_type:
        sightings = sightings.filter(ghost_type=ghost_type)
    if location:
        sightings = sightings.filter(location=location)
    if year:
        sightings = sightings.filter(date__year=year)

    sightings = sightings.order_by('-created_at')[:9]

    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            sighting = form.save(commit=False)
            sighting.author = request.user
            sighting.save()
            return redirect('sightings')
    else:
        form = SightingForm()

    context = {
        'form': form,
        'sightings': sightings,
        'years': years,
        'selected_ghost_type': ghost_type,
        'selected_location': location,
        'selected_year': year
    }
    return render(request, 'sightings/sightings_list.html', context)

def sighting_detail(request, sighting_id):
    sighting = get_object_or_404(Sighting, pk=sighting_id)
    return render(request, 'sightings/sighting_detail.html', {'sighting': sighting})