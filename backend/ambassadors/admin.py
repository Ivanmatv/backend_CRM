from django.contrib import admin
from .models import (Ambassador,
                     Promocode,
                     WorkIt,
                     AmbassadorMerch,
                     AmbassadorPromocode)


admin.site.register(Ambassador)
admin.site.register(Promocode)
admin.site.register(WorkIt)
admin.site.register(AmbassadorMerch)
admin.site.register(AmbassadorPromocode)
