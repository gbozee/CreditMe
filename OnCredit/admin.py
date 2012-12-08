from django.contrib import admin
from OnCredit.models import  Prepaid,Postpaid,UtilityBills,TransportBills,CableTV,CableTVSubscription,SubscriptionPlan,DataPlan

class DataPlanAdmin(admin.ModelAdmin):
	pass
class CableTVAdmin(admin.ModelAdmin):
	pass

#Define a new User admin
class CableTVSubscriptionAdmin(admin.ModelAdmin):
	pass
	
class PrepaidAdmin(admin.ModelAdmin):
	pass

class PostpaidAdmin(admin.ModelAdmin):
	pass	

class UtilityBillsAdmin(admin.ModelAdmin):
	pass

class TransPortBillsAdmin(admin.ModelAdmin):
	pass

class SubscriptionPlanAdmin(admin.ModelAdmin):
	pass

admin.site.register(DataPlan,DataPlanAdmin)
admin.site.register(CableTV, CableTVAdmin)
admin.site.register(CableTVSubscription,CableTVSubscriptionAdmin)
admin.site.register(Prepaid,PrepaidAdmin)
admin.site.register(Postpaid,PostpaidAdmin)
admin.site.register(UtilityBills,UtilityBillsAdmin)
admin.site.register(TransportBills,TransPortBillsAdmin)
admin.site.register(SubscriptionPlan,SubscriptionPlanAdmin)