from rest_framework.throttling import UserRateThrottle

class PinkuRateThrottle(UserRateThrottle):
    scope = 'pinku'