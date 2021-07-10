from django.shortcuts import render,HttpResponse
from utils.tencent.sms import send_sms_single
import random
from django.conf import settings
# Create your views here.

def send_sms(request):
    '''发送短信
        ?tpl=login  -> 1006413
        ?tpl=1006416 ->1006416
    '''
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')

    code = random.randrange(1000,9999)
    res = send_sms_single('13917754978',template_id,[code,])
    if res['result'] == 0:
        return HttpResponse('成功了')
    else:
        return HttpResponse(res['errmsg'])

