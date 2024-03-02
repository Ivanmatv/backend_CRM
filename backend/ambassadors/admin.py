from django.contrib import admin
from .models import (Ambassador, Merch, Promocode, AmbassadorMerch,
                     AmbassadorPromocode)


admin.site.register(Ambassador)
admin.site.register(AmbassadorMerch)
admin.site.register(AmbassadorPromocode)
admin.site.register(Promocode)
admin.site.register(Merch)
