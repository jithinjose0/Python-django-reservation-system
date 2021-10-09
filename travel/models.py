from django.db import models

# Create your models here.
class Bus(models.Model):
    source=(
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
    destination=(
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
    timeslot_list=(
        ('', 'Select'),
        ('9:00am','9:00am'),
        ('10:00am','10:00am'),
        ('11:00am','11:00am'),
        ('1:00pm','1:00pm'),
        ('2:00pm','2:00pm'),
        ('3:00pm','3:00pm'),
        ('4:00pm','4:00pm'),
        ('5:00pm','5:00pm'),
    )
    ownername=models.CharField(max_length=50)
    bus_name = models.CharField(max_length=30)
    source=models.CharField(max_length=25,choices=source)
    dest=models.CharField(max_length=25,choices=destination)
    Total_seats = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=0, max_digits=6)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    time1=models.CharField(max_length=25,choices=timeslot_list)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.bus_name

class BusBook(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    ownername = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=255)

    def __str__(self):
        return self.email
