from django.shortcuts import render


def about(request):

    sdata = dict(request.session)

    data = {
        "site_name": "Site name",
        "detail": "Site detail",
        "sdata": sdata,
    }

    return render(request, 'store/about.html', data)
