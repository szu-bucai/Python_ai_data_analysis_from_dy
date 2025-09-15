import random
import os
import requests
import time
import string
import json
import re
import csv
def get_json(keyword,offset,count):

  headers = {
      "accept": "application/json, text/plain, */*",
      "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
      "priority": "u=1, i",
      "referer": "https://www.douyin.com/search/%E5%93%AA%E5%90%922?aid=e9967d36-514d-47cc-9747-6ca1f3a31baa&type=general&ug_source=microsoft_mz03",
      "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "uifid": "30ff7b230d01f3ed4fd5546706fc508e0725b8a99e0ba4197a991a959864baf0e91e39cf4a34f3a2b0f8d25185168878da0d7cf627d912478a6456122cda9e1d0d97b6f6421415f30c5b4a5e8c9ca9a2e12d0322f0b5c19325d2cd9ab19ce985b44cbac1d8fafd225a8b2bc4403e9616",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
  }
  cookies = {
      "bd_ticket_guard_client_web_domain": "2",
      "passport_csrf_token": "f28954cf4b0fe81ce795ca53590acfea",
      "passport_csrf_token_default": "f28954cf4b0fe81ce795ca53590acfea",
      "enter_pc_once": "1",
      "UIFID_TEMP": "30ff7b230d01f3ed4fd5546706fc508e0725b8a99e0ba4197a991a959864baf0e91e39cf4a34f3a2b0f8d25185168878da0d7cf627d912478a6456122cda9e1d0d97b6f6421415f30c5b4a5e8c9ca9a2e12d0322f0b5c19325d2cd9ab19ce985b44cbac1d8fafd225a8b2bc4403e9616",
      "x-web-secsdk-uid": "06d643dc-59b1-4be8-898f-b690160ed873",
      "douyin.com": "",
      "device_web_cpu_core": "20",
      "device_web_memory_size": "8",
      "architecture": "amd64",
      "dy_swidth": "1707",
      "dy_sheight": "1067",
      "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22",
      "hevc_supported": "true",
      "s_v_web_id": "verify_mfeqaxhh_tweQjRBg_9hZd_4NNx_8OOD_8ECkMxdlz7Bn",
      "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D",
      "fpk1": "U2FsdGVkX19bkspJ1BBWT+18jWEAE/z2XmP6EtsDW6vQkJiJH/2JksGIO4/l+hJIQNKK6Vvioxo0HWaROUIrKg==",
      "fpk2": "7ceed19ee5ebdbf792f56329591ffc53",
      "is_dash_user": "1",
      "SEARCH_RESULT_LIST_TYPE": "%22single%22",
      "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22",
      "csrf_session_id": "b32ad4a24575ae323dbb37eba70a125c",
      "ttwid": "1%7CspbR7NrdY5_vVJSZMtJIOg25nJnpGb3NmgVtf4ISmgo%7C1757554662%7Cd991f35e3c4dd2b9751f18de27e358e19ffb460e5ecf24ba934eed8724034915",
      "biz_trace_id": "c6838837",
      "__security_mc_1_s_sdk_crypt_sdk": "181ee335-40a3-b721",
      "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS250ZzR1U0wrYUU2RGdzV3ZkeTg3VkdDcDB2YVhZM0xlcjFkaERsSElmWEcxOW01QTFGbGlyeUJNK2IvL2tCaEh6dU9WeHFHTlp3djU2V05HUk1sU3c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
      "odin_tt": "46c2f51566b5234aed5b054153033c04ea6015cfa07e54af95477079af8ce6c6ad05dc935e07bf43bc53f5149beb41fcd6c5203e7140fb585c9fdba865eeb1a75dd5086b4d226edab08870306373faf2",
      "WallpaperGuide": "%7B%22showTime%22%3A1757557998897%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%7D",
      "__ac_nonce": "068c235a9008c5a21cc6d",
      "__ac_signature": "_02B4Z6wo00f01HbAoQAAAIDD-2gYilLFM3R24KWAAHV5b2",
      "download_guide": "%222%2F20250911%2F1%22",
      "IsDouyinActive": "true",
      "home_can_add_dy_2_desktop": "%221%22"
  }
  url = "https://www.douyin.com/aweme/v1/web/general/search/single/"
  params = {
      "device_platform": "webapp",
      "aid": "6383",
      "channel": "channel_pc_web",
      "search_channel": "aweme_general",
      "enable_history": "1",
      "keyword": keyword,      
      "search_source": "normal_search",
      "query_correct_type": "1",
      "is_filter_search": "0",
      "from_group_id": "",
      "disable_rs": "0",
      "offset": offset,
      "count": count,
      "need_filter_settings": "0",
      "list_type": "single",
      "pc_search_top_1_params": "{\"enable_ai_search_top_1\":1}",
      "search_id": "202509111051116E80087771EF67472B55",
      "update_version_code": "170400",
      "pc_client_type": "1",
      "pc_libra_divert": "Windows",
      "support_h265": "1",
      "support_dash": "1",
      "cpu_core_num": "20",
      "version_code": "190600",
      "version_name": "19.6.0",
      "cookie_enabled": "true",
      "screen_width": "1707",
      "screen_height": "1067",
      "browser_language": "zh-CN",
      "browser_platform": "Win32",
      "browser_name": "Edge",
      "browser_version": "140.0.0.0",
      "browser_online": "true",
      "engine_name": "Blink",
      "engine_version": "140.0.0.0",
      "os_name": "Windows",
      "os_version": "10",
      "device_memory": "8",
      "platform": "PC",
      "downlink": "10",
      "effective_type": "4g",
      "round_trip_time": "150",
      "webid": "7532039181900793363",
      
  }
  time.sleep(random.randint(1,5))
  response = requests.get(url, headers=headers, cookies=cookies, params=params)
  
  # print(response)
  # print(response.text)
  return response.json()
  
  

def get_time(ctime):
  time_local=time.localtime(ctime)
  time_format=time.strftime("%Y.%m.%d",time_local)
  return time_format

def parseData(response):
  minute = response["video"]['duration']//1000//60
  second = response['video']['duration']//1000%60
  video_dict = {
    "用户名": response['author']['nickname'].strip(),
    "粉丝数量": response['author']['follower_count'],
    "视频描述": response['desc'],
    "视频id": response["aweme_id"],
    "发表时间": get_time(response['create_time']),
    "视频时长": "{:02d}:{:02d}".format(int(minute), int(second)),
    "点赞数量": response['statistics']['digg_count'],
    "收藏数量": response['statistics']['collect_count'],
    "评论数量": response["statistics"]['comment_count'],
    "下载数量": response["statistics"]['download_count'],
    "分享数量": response["statistics"]['share_count'],
  }
  print(video_dict)
  writer.writerow(video_dict)
    


def search(keyword):
  offset=0
  count=16
  while True:
    response=get_json(keyword,offset,count)
    feeds=response['data']
    
    print(f"获取到 {len(feeds)} 条数据")
    
    for  feed in feeds:
     # 检查是否有aweme_info字段
      if 'aweme_info' in feed:
        parseData(feed['aweme_info'])
      else:
         continue
      
    if response['has_more']==0:
      break

    offset=offset+count
    count=10

if __name__=="__main__":
  
  header=['用户名','粉丝数量','视频描述','视频id','发表时间','视频时长','点赞数量','收藏数量','评论数量',
  '下载数量','分享数量']
  keyword="哪吒2"
  
  # result_dir = "data/result"
  # os.makedirs(result_dir, exist_ok=True)
  
  # filename = f"{result_dir}/{keyword}_data.csv"
  
  f=open('data.csv', 'w', encoding='utf-8',newline='')
  writer=csv.DictWriter(f,header)
  writer.writeheader()
  search(keyword)
  