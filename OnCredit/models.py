from django.db import models
from django.contrib.auth.models import User
import datetime
from OnCredit.custom import *
from django.db.models.signals import post_save

# Create your models here.

#Abstract base class for buying recharge cards on credit
NETWORK = (('MTN','MTN'),('Airtel','Airtel'),('Globacom','Globacom'),('Etisalat','Etisalat'),
			('Starcomms','Starcomms'),('Multilinks','Multilinks'),('Visafone','Visafone'),)
RECHARGE_TYPE = (('Virtual', 'Virtual'),('SMS', 'SMS'),)
PAYMENT_MODE = (('Debit', 'Debit'),('Credit', 'Credit'),)
AMOUNT_ALLOWED = (('50','50'),('100','100'),('200','200'),('400','400'),('500','500'),('750','750'),('1000','1000'),
				('1300','1300'),('1500','1500'),('1600','1600'),('2000','2000'),('3000','3000'),('3500','3500'),
				('4000','4000'),('5000','5000'),('6000','6000'),('6500','6500'),('7500','7500'),('8000','8000'),
				('10000','10000'),('15000','15000'),('18000','18000'),)
DURATION = (('Daily','Daily'),('Weekly','Weekly'),('Monthly','Monthly'),('Monthly Daytime','Monthly Daytime'),
			('Monthly Nighthours','Monthly Nighthours'),('Monthly Weekends','Monthly Weekends '),('Quarterly','Quarterly'),)
DATA_PLAN = (('BIS','BIS'),('10mb','10mb'),('25mb','25mb'),('50mb','50mb'),('150mb','150mb'),('200mb','200mb'),
			('375mb','375mb'),('750mb','750mb'),('1G','1G'),('1.5G','1.5G'),('3G','3G'),('4.5G','4.5G'),('6G','6G'),
			('7.5G','7.GG'),('9G','9G'),('10G','10G'),('15G','15G'),('20G','20G'),)


# class CreditUser(models.Model):
# 	accountName = models.CharField(max_length = 10)
# 	email_addr = models.EmailField()
# 	phone_number = models.CharField(max_length= 11)
# 	total_amount_borrowed = models.DecimalField(max_digits=9,decimal_places=2)
# 	pin = IntegerRangeField(min_value = 4)
	

# 	def __unicode__ (self):
# 		return self.accountName
class Recharge(models.Model):
	user = models.ForeignKey(User)
	network_type = models.CharField(choices=NETWORK, max_length=15)
	amount_charged = models.CharField(choices=AMOUNT_ALLOWED, max_length=10)
	pincode = models.CharField(max_length=30)
	used = models.BooleanField(default=False)
	def __unicode__(self):
		return "%s subscribed for" % self.network_type

# Model for prepaid recharge
class Prepaid(Recharge):	
	pass

#Model for postpaid recharge
class Postpaid(Recharge):
	duration = models.CharField(choices=DURATION, max_length=30)
	
		
#Abstract base model for TV, Transport and Utilities
class Subscription(models.Model):
	user = models.ForeignKey(User)
	subscriber_name = models.CharField(max_length=60)
	card_num = models.CharField(max_length=15)
	amount_charged = models.DecimalField(max_digits=9,decimal_places=2)

#model for utility bills
class UtilityBills(Subscription):
	pass

#model for transport bills
class TransportBills(Subscription):
	pass

#subscription plan to be used by cable TV
class SubscriptionPlan(models.Model):
	plan_name = models.CharField(max_length=30)
	plan_amount = models.DecimalField(max_digits=9,decimal_places=2)

	def __unicode__(self):
		
		return "%s - %d" % (self.plan_name, self.plan_amount)

#cable tv to be used by cabletvsubscription

class CableTV(models.Model):	
	name = models.CharField(max_length=30)
	subscription_plan = models.ForeignKey(SubscriptionPlan)
	def __unicode__(self):		
		return "%s - %s" % (self.name, self.subscription_plan)

class CableTVSubscription(Subscription):
	subscription = models.ForeignKey(CableTV)

	def __unicode__(self):		
		return " %s by %s" % (self.subscription, self.subsriber_name)

class DataPlan(models.Model):
	user = models.ForeignKey(User)
	network = models.CharField(choices=NETWORK,max_length=15)
	data_plan = models.CharField(choices=DATA_PLAN, max_length=10)
	duration = models.CharField(choices=DURATION, max_length=30)
	amount = models.CharField(choices=AMOUNT_ALLOWED, max_length=10)

	def __unicode__(self):
		return "%s - %s - %s -%s " % (self.network, self.data_plan, self.duration, self.amount)





# class Ratings(models.Model):
# 	credit_user = models.ForeignKey(CreditUser)
# 	STARS = Choices(('ROOKIE','rookie'),('AMATEUR','amateur'),('AVERAGE','average'),('PROFESSIONAL','professional'),('MASTERS','masters'),)
# 	no_of_stars = models.IntegerField(choices=STARS, default=STARS.ROOKIE)
# 	bonus_point = models.IntegerField()
