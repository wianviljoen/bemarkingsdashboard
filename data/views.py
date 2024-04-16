from django.shortcuts import render, get_object_or_404
from data.models import DataMaand


def Data_View(request, maand_naam):
    # Retrieve DataMaand object based on the provided 'maand_naam'
    data_maand = get_object_or_404(DataMaand, maand=maand_naam)

    # Retrieve Data objects related to the DataMaand
    data = data_maand.data_set.all()

    # Pass the data to the template
    return render(request, 'data/index.html', {'data': data})