from django.db import *

class IntFields(Model):

    num_2 = BigAutoField(default=1)
    num_3 = BigIntegerField(default=-1)
    num_4 = BinaryField()
    boolean = BooleanField(null=True)
