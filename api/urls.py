# from django.conf.urls.defaults import *
# from piston.resource import Resource
# from api.handlers import *

# prepaid = Resource(PrepaidHandler)
# # postpaid = Resource(PostpaidHandler)
# cabletv = Resource(CableTVHandler)
# # transport = Resource(TransportHandler)
# # utility = Resource(UtilityHandler)
# # dataplan = Resource(DataPlanHandler)

# urlpatterns = patterns('',
# 	url(r'^prepaid/(?P<Id>\d+)$',prepaid),
# 	url(r'^prepaid$', prepaid),
# 	# url(r'^postpaid/(?P<id>\d+)$',postpaid),
# 	# url(r'^postpaid$', postpaid),
# 	url(r'^cabletv/(?P<id>\d+)$',cabletv, name='prepaids'),
# 	url(r'^cabletv$', cabletv),
# 	# url(r'^transport/(?P<id>\d+)$',transport),
# 	# url(r'^transport$', transport),
# 	# url(r'^utility/(?P<id>\d+)$',utility),
# 	# url(r'^utility$', utility),
# )