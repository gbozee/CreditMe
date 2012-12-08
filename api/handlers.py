from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.constants import *
from tastypie import fields
from tastypie.serializers import Serializer
from django.contrib.auth.models import User
from tastypie.authorization import Authorization


from OnCredit.models import *

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		filtering = {
		    'username': ALL,
		}

class PrepaidResource(ModelResource):
	"""
	Authenticated entrypoint for Credit Users.
	"""
	user = fields.ForeignKey(UserResource, 'user')
	class Meta:
		queryset = Prepaid.objects.all()
		resource_name = 'prepaid'
		#serializer = Serializer(formats=['json','plist'])
		#authorization = Authorization
	# fields = ('id','network_type','amount_charged','pincode ')
	# model = Prepaid

	# @classmethod
	# def resource_uri(cls, perpaid):
	# 	return ('prepaids', [ 'json', ])

	# def read(self, request, Id=None):
	# 	"""
	# 	Returns a blogpost, if `title` is given,
	# 	otherwise all the posts.

	# 	Parameters:
	# 	 - `title`: The title of the post to retrieve.
	# 	"""
	# 	base = Prepaid.objects

	# 	if Id:
	# 		return base.get(pk=Id)
	# 	else:
	# 		return base.all()


class CableTVResource(ModelResource):
	class Meta:
		queryset=CableTV.objects.all()
		resource_name='cable-tv'
		authorization=Authorization

class CableSubscriptionResource(ModelResource):
	subscription = fields.ForeignKey(CableTVResource, 'subscription')
	class Meta:
		queryset = CableTVSubscription.objects.all()
		resource_name= 'cable-subscription'
		authorization=Authorization

class PostpaidResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')
	class Meta:
		queryset= Postpaid.objects.all()
		resource_name='postpaid'
		authorization = Authorization()
		filtering = {
			'user': ALL_WITH_RELATIONS,
            'network_type': ALL,
            'used': ALL,
            'amount_charged': ALL,
        }
        #serializer = Serializer(formats=['json','jsonp'])


class TransportResource(ModelResource):
	class Meta:
		queryset= TransportBills.objects.all()

class UtilityResource(ModelResource):
	class Meta:
		queryset= UtilityBills.objects.all()


class DataPlanResource(ModelResource):
	class Meta:
		queryset= DataPlan.objects.all()
