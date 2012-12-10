from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.constants import *
from tastypie import fields
from tastypie.serializers import Serializer
from django.contrib.auth.models import User
from tastypie.authorization import Authorization


from OnCredit.models import *

class TemplateResource(ModelResource):
	class Meta:
		include_resource_uri = False
		filtering = {
			'user': ALL_WITH_RELATIONS,
            'network_type': ALL,
            'used': ALL,
            'amount_charged': ALL,
        }
		
	def alter_list_data_to_serialize(self,request,data_dict):
		if isinstance(data_dict,dict):
			if 'meta' in data_dict:
				#Get rid of the meta objects
				del(data_dict['meta'])
		return data_dict
	

class UserResource(TemplateResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		filtering = {
		    'username': ALL,
		}		

class PrepaidResource(TemplateResource):
	"""
	Authenticated entrypoint for Credit Users.
	"""
	user = fields.ForeignKey(UserResource, 'user')
	class Meta:
		queryset = Prepaid.objects.all()
		resource_name = 'prepaid'

class CableTVResource(TemplateResource):
	class Meta:
		queryset=CableTV.objects.all()
		resource_name='cable-tv'
		authorization=Authorization

class CableSubscriptionResource(TemplateResource):
	subscription = fields.ForeignKey(CableTVResource, 'subscription')
	class Meta:
		queryset = CableTVSubscription.objects.all()
		resource_name= 'cable-subscription'
		authorization=Authorization

class PostpaidResource(TemplateResource):
	user = fields.ForeignKey(UserResource, 'user')
	class Meta:
		queryset= Postpaid.objects.all()
		resource_name='postpaid'
		authorization = Authorization()
		

class TransportResource(TemplateResource):
	class Meta:
		queryset= TransportBills.objects.all()

class UtilityResource(TemplateResource):
	class Meta:
		queryset= UtilityBills.objects.all()


class DataPlanResource(TemplateResource):
	class Meta:
		queryset= DataPlan.objects.all()
