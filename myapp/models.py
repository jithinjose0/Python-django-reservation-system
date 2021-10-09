from django.db import models
class tourist(models.Model):
    DISTRICT=(
        ("","---Select District---"),
        ("Alappuzha","Alappuzha"),
        ("Ernakulam","Ernakulam"),
        ("Idukki","Idukki"),
        ("Kannur","Kannur"),
        ("Kasaragod","Kasaragod"),
        ("Kollam","Kollam"),
        ("Kottayam","Kottayam"),
        ("Kozhikode","Kozhikode"),
        ("Malappuram","Malappuram"),
        ("Palakkad","Palakkad"),
        ("Pathanamthitta","Pathanamthitta"),
        ("Thiruvananthapuram","Thiruvananthapuram"),
        ("Thrissur","Thrissur"),
        ("Wayanad","Wayanad")
    )
    ownername=models.CharField(max_length=50)
    place_name = models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    des=models.CharField(max_length=100)
    place=models.CharField(max_length=25,choices=DISTRICT)
    price = models.DecimalField(decimal_places=0, max_digits=6)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.place_name

    @property
    def district(self):
        return self.DISTRICT[self.place]

class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    payment_choice = (
        ('Credit Card', 'Credit Card'),
        ('google pay','google pay'),
    )
    email = models.EmailField()
    name = models.CharField(max_length=30)
    ownername=models.CharField(max_length=50)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    placeid=models.DecimalField(decimal_places=0, max_digits=2)
    place_name = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=0, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    payment_type = models.CharField(max_length=11, choices=payment_choice,default='Credit Card')
    timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S',null=True,blank=True)

    def __str__(self):
        return self.email
        
class bookingform(models.Model):
    timeslot_list=(
        ('', 'Select'),
        ('9:00 - 10:00am','9:00 - 10:00am'),
        ('10:00 - 11:00am','10:00 - 11:00am'),
        ('11:00 - 12:00am','11:00 - 12:00am'),
        ('1:00 - 2:00pm','1:00 - 2:00pm'),
        ('2:00 - 3:00pm','2:00 - 3:00pm'),
        ('3:00 - 4:00pm','3:00 - 4:00pm'),
    )
    mem=models.IntegerField()
    date=models.DateField()
    timeslot=models.IntegerField(choices=timeslot_list)

    @property
    def time(self):
        return self.timeslot_list[self.timeslot][1]