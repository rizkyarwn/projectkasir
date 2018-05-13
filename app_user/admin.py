"""from django.contrib.auth.models import User, Group

group = Group(name="User")
group.save()
user = User.objects.get(pk=1)
user.groups.add(group)"""