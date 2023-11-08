#导入包
import webbrowser

import webbrowser


urls=(
    "https://ys.mihoyo.com/cloud/?utm_source=default#/",
    "https://autopatchcn.yuanshen.com/client_app/download/cloudgame/pc/20231030180101_PHhNgJrC9cK6xCuT/cypcmihoyo/yscloud_4.2.0.exe",
    "www.yuanshen.com",
    "https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default"
)


for url in urls:
    webbrowser.open(url)
