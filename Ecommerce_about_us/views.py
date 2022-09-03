from django.shortcuts import render
from Ecommerce_setting.models import SiteSetting
from .models import TeamMembers


def about_us(request):
    introduce = SiteSetting.objects.first().introduce
    description = SiteSetting.objects.first().description
    team_members = TeamMembers.objects.all()

    # Pass data to about_us templates
    context = {
        'introduce': introduce,
        'description': description,
        'team_members': team_members,

    }
    return render(request, 'Ecommerce_about_us/about_us.html', context)
