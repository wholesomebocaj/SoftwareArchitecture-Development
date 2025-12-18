from .views import get_dashboard_url

def dashboard_link(request):
    """
    This adds 'dashboard_url' into every template automatically.
    """
    if not request.user.is_authenticated:
        return {"dashboard_url": None}

    return {"dashboard_url": get_dashboard_url(request.user)}
