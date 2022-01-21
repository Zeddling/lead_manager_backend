from .api import LeadViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register("", LeadViewset, "leads")

urlpatterns = router.urls
