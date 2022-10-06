import pywinauto
import itertools
import time

pwa_app = pywinauto.application.Application()
w_handle = pywinauto.findwindows.find_windows(title=u'\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u041a\u0440\u0438\u043c\u0438\u043d\u0430\u043b\u0438\u0441\u0442 "\u041c\u0430\u0441\u0442\u0435\u0440 \u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445" v.12.0.0.46')[0]
pwa_app.connect(handle=w_handle)
window = pwa_app.window(handle=w_handle)
for i in itertools.product('9876543210', repeat=4):
    num = ''.join(i)
    print(num)
    window['Edit'].set_text(num)
    window['ПроверкаButton'].click()
    time.sleep(1)

# ПроверкаButton Проверка

