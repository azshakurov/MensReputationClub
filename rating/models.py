from django.db import models


class Rating(models.Model):
    """

    """
    full_name = models.CharField(max_length=50, name='full_name')
    username = models.CharField(max_length=20, name='username')
    pwd = models.CharField(max_length=20, name='pwd')
    cv_file = models.FileField(name='cv_file', null=True)
    avatar = models.ImageField(name='avatar', null=True)
    create_time = models.DateTimeField(auto_created=True, name='create_time')
    edit_time = models.DateTimeField(auto_created=True, name='edit_time')


    #
    # def __init__(self):
    #     super(Rating, self).__init__()

