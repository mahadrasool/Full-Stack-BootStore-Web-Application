# from django.contrib.auth.models import get_user_model
# from django.db.models.signals import post_save
# from .models import RequestedBookList

# User = get_user_model()

# def set_created_by_user(sender, instance, created, **kwargs):
#     if created:
#         # Access the request object here (replace with your approach)
#         current_user = # Your logic to get the currently logged-in user (using request.user)
#         instance.CreatedByUserID = current_user
#     instance.save()

# post_save.connect(set_created_by_user, sender=RequestedBookList)
