# context_processors.py
from .models import Tab

def active_tabs(request):
    # 表示フラグが True のタブのみ取得
    tabs = Tab.objects.filter(is_displayed=True)
    return {'active_tabs': tabs}