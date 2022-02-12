from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from dateutil.relativedelta import relativedelta
from calculation.forms import InterestDataForm
from calculation.models import InterestData

def HomeView(request):
    if request.method == "POST":
        form = InterestDataForm(request.POST)
        principal = int(form.data['principal'])
        end_date = datetime.strptime(form.data['release_date'], "%Y-%m-%d")
        start_date = datetime.strptime(form.data['loan_date'], "%Y-%m-%d")
        t = relativedelta(end_date, start_date)
        r = 3 if principal <= 5000 else 2
        total = interest_cal(t, principal, r)
        try:
            if form and total:
                result = InterestData(loan_date=start_date, release_date=end_date, principal=principal, total=total,
                                      rate=r)
                result.save()
                return render(request, 'index.html', {'total': total})
        except:
            return HttpResponse(
                content=
                'No Detail found.',
            )
    else:
        form = InterestDataForm()
    return render(request, 'index.html', {'form': form})


def interest_cal(t, p, r):
    """To calculate the compound and simple interest."""
    per_month = (p / 100) * r
    if not t.years or t.years == 0:
        m = per_month * t.months
        d = (per_month / 30) * t.days
        total = p + d + m
    else:
        m = per_month * t.years * 12
        new_p = m + p
        new_per_month = (new_p / 100) * r
        m = new_per_month * t.months
        d = (new_per_month / 30) * t.days
        total = new_p + m + d
    return total
