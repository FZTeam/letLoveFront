import re
import requests
import time
import demjson

url = '''https://h5.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_act_all?uin=2094531487&hostuin=3185948277&scope=0&filter=all&flag=1&refresh=0&firstGetGroup=0&mixnocache=0&scene=0&begintime=undefined&icServerTime=&start=%d&count=1&sidomain=qzonestyle.gtimg.cn&useutf8=1&outputhtmlfeed=1&refer=2&r=0.9325275746721156&g_tk=1908316279&qzonetoken=2aac648d0dd9df840d05b1779e22aca5765890f174a90b00b5d13567a3d549a966e10014a441afb127&g_tk=1908316279'''

headers = {
  'cookie': '''pgv_pvi=1220986880; RK=mRgx5srEMW; ptcz=6b5edf55152bf438c8b33df6e7cbfd210a6ec530a87806548c78a90f164860da; pgv_pvid=2448556092; luin=o0906568311; lskey=00010000fab741f947f0d5cc3b91366dc8a30888d67425f119dc18d72012c41783e79d747f7c8a11c48f2c3d; _qpsvr_localtk=0.682125533234472; pgv_si=s9939652608; pgv_info=ssid=s4468550966; uin=o2094531487; skey=@YXsUMgNbk; p_uin=o2094531487; pt4_token=VSxen9S7yYmLgd5UJnhZtmYBeLc-kBVhisFoW5I6zuY_; p_skey=5N3k*gOORDM2AJX4433RXDltVyAUkTtP7F0*wB80QuI_; Loading=Yes; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0; __Q_w_s__QZN_TodoMsgCnt=1; rv2=80A82DBA0C550FE48F8E5BE62ED38A9EAC0B0646570954898F; property20=AFA2B2A944E05FB5879ED311763ACF71747705F158A44B81A11A3002F87585D77FC0566C29FE96CD'''
}
for i in range(23):
  bas_url = url % (i * 40)
  res = requests.get(url,headers=headers)
  print(res.text)
  js_obj = re.findall(r'_Callback\(([\d\D]*)\);', res.text)[0]

  print(demjson.decode(js_obj))
  # print(type(json.loads(js_obj)))
  # print(res.text)
  time.sleep(1)

