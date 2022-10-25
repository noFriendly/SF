from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import CustomSignupForm
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/sign/login'

@login_required
def upgrade_account(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    groups = request.user.groups
    is_author = groups.filter(name='authors').exists()
    if not is_author:
        author_group.user_set.add(user)
    return redirect('/')