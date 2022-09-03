from django.shortcuts import render
from Ecommerce_setting.models import SiteSetting
from .models import TeamMembers


# Create about_us view
def about_us(request):
    # Start -- Fetch data from site management and TeamMember model
    introduce = SiteSetting.objects.first().introduce
    description = SiteSetting.objects.first().description
    team_members = TeamMembers.objects.all()
    # End -- Fetch data from site management and TeamMember model

    # Pass data to about_us templates
    context = {
        'introduce': introduce,
        'description': description,
        'team_members': team_members,

    }
    return render(request, 'Ecommerce_about_us/about_us.html', context)
