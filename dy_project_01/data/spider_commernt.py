import requests
import csv
import pandas as pd
from spider import get_time

def get_json(aweme_id,cursor):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "bd-ticket-guard-client-data": "eyJ0c19zaWduIjoidHMuMi4zZGIxMDMzYTUxODMwNTVmNWNkYTkwOTBmNzU5MmNlYTRiMmI1NTZhNjAwNzI0YzRmYjI0ODQ0MjcwMzBlMDRmYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJmdjVvRlFOY3ltc3BWR2FqME91OXBQa3l5dnFaOVB5WDdlc1RzRHFzRmVFPSIsInRpbWVzdGFtcCI6MTc1Nzc2NTUwM30=",
        "bd-ticket-guard-iteration-version": "1",
        "bd-ticket-guard-ree-public-key": "BKntg4uSL+aE6DgsWvdy87VGCp0vaXY3Ler1dhDlHIfXG19m5A1FliryBM+b//kBhHzuOVxqGNZwv56WNGRMlSw=",
        "bd-ticket-guard-version": "2",
        "bd-ticket-guard-web-sign-type": "1",
        "bd-ticket-guard-web-version": "2",
        "priority": "u=1, i",
        "referer": "https://www.douyin.com/?recommend=1",
        "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "uifid": "30ff7b230d01f3ed4fd5546706fc508e0725b8a99e0ba4197a991a959864baf08b442342b5ec97ae63787ff5ac8d239161b41d0e573096a6fa8534ce34d4a481b5cfcfbb9ad2156c905ecc439357bc1342ca0cca205813585617eb9be3cafa4b0e1bb16d26aa9f028494eb078e9d7ba02cec9b839e4e19bf0d11c11545a60494dd6f736ba4608e7afd0df5145fc44679b61e104bf8bbe3cdb498735ff23aa4d3",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
    }
    cookies = {
        "bd_ticket_guard_client_web_domain": "2",
        "passport_csrf_token": "f28954cf4b0fe81ce795ca53590acfea",
        "passport_csrf_token_default": "f28954cf4b0fe81ce795ca53590acfea",
        "enter_pc_once": "1",
        "UIFID_TEMP": "30ff7b230d01f3ed4fd5546706fc508e0725b8a99e0ba4197a991a959864baf0e91e39cf4a34f3a2b0f8d25185168878da0d7cf627d912478a6456122cda9e1d0d97b6f6421415f30c5b4a5e8c9ca9a2e12d0322f0b5c19325d2cd9ab19ce985b44cbac1d8fafd225a8b2bc4403e9616",
        "dy_sheight": "1067",
        "hevc_supported": "true",
        "s_v_web_id": "verify_mfeqaxhh_tweQjRBg_9hZd_4NNx_8OOD_8ECkMxdlz7Bn",
        "fpk1": "U2FsdGVkX19bkspJ1BBWT+18jWEAE/z2XmP6EtsDW6vQkJiJH/2JksGIO4/l+hJIQNKK6Vvioxo0HWaROUIrKg==",
        "fpk2": "7ceed19ee5ebdbf792f56329591ffc53",
        "is_dash_user": "1",
        "SEARCH_RESULT_LIST_TYPE": "%22single%22",
        "__security_mc_1_s_sdk_crypt_sdk": "181ee335-40a3-b721",
        "__ac_signature": "_02B4Z6wo00f01HbAoQAAAIDD-2gYilLFM3R24KWAAHV5b2",
        "download_guide": "%223%2F20250911%2F1%22",
        "WallpaperGuide": "%7B%22showTime%22%3A1757557998897%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A16%2C%22cursor2%22%3A4%2C%22hoverTime%22%3A1757562011073%7D",
        "UIFID": "30ff7b230d01f3ed4fd5546706fc508e0725b8a99e0ba4197a991a959864baf08b442342b5ec97ae63787ff5ac8d239161b41d0e573096a6fa8534ce34d4a481b5cfcfbb9ad2156c905ecc439357bc1342ca0cca205813585617eb9be3cafa4b0e1bb16d26aa9f028494eb078e9d7ba02cec9b839e4e19bf0d11c11545a60494dd6f736ba4608e7afd0df5145fc44679b61e104bf8bbe3cdb498735ff23aa4d3",
        "xgplayer_user_id": "173571025783",
        "douyin.com": "",
        "device_web_cpu_core": "20",
        "device_web_memory_size": "8",
        "architecture": "amd64",
        "home_can_add_dy_2_desktop": "%220%22",
        "dy_swidth": "1708",
        "strategyABtestKey": "%221757764955.126%22",
        "xgplayer_device_id": "15551036049",
        "passport_mfa_token": "CjWdp4OJtdzZCKXOwfAR0CLbIhwCfINf10eISiTz%2Bx%2FuDzwEG8XI%2F9egQXOyzVn5VofwGXR8FRpKCjwAAAAAAAAAAAAAT3iprMUlYbHDz59SStFGBFcOiOUCEabiqGKVXHCDuq6Lr8Zcgyz3bG8ZqVjL%2BcHRngYQkYn8DRj2sdFsIAIiAQPKpjiA",
        "d_ticket": "1589488c1fe064f06e72566ad681b5557898e",
        "passport_assist_user": "CjwxHs4T6Iq5T9otITtUKLdirbb__ad6GlcWCpypJa-aNGXE1QIzno9M-E5W2YHMTcFnhY6BNHK-l1Odg8EaSgo8AAAAAAAAAAAAAE94H8uZ0A8QqsLLQmBYIq7-U6vDWaKfrpg6ZIbzrRYJmulZ67lKpDbZapXFnYQHWMZiEKuL_A0Yia_WVCABIgEDYMpbqw%3D%3D",
        "n_mh": "fQboEs4xXmKFP5eVkIoFvVdo8WkBJ0m-Xtoxehy8CrM",
        "sid_guard": "96f7f442489af15506e13ef9ef4a3e6d%7C1757765033%7C5184000%7CWed%2C+12-Nov-2025+12%3A03%3A53+GMT",
        "uid_tt": "0d9361ae1378a6a8fdb979bd3f4d7eaf",
        "uid_tt_ss": "0d9361ae1378a6a8fdb979bd3f4d7eaf",
        "sid_tt": "96f7f442489af15506e13ef9ef4a3e6d",
        "sessionid": "96f7f442489af15506e13ef9ef4a3e6d",
        "sessionid_ss": "96f7f442489af15506e13ef9ef4a3e6d",
        "is_staff_user": "false",
        "sid_ucp_v1": "1.0.0-KDliYTYzNzQ0MjQxNmIwZTUyZDM3Y2FiNjI3YmQ5ZGRlZDVhNDE1MTEKHwikoOG07AIQqbuVxgYY7zEgDDDe95PXBTgHQPQHSAQaAmxmIiA5NmY3ZjQ0MjQ4OWFmMTU1MDZlMTNlZjllZjRhM2U2ZA",
        "ssid_ucp_v1": "1.0.0-KDliYTYzNzQ0MjQxNmIwZTUyZDM3Y2FiNjI3YmQ5ZGRlZDVhNDE1MTEKHwikoOG07AIQqbuVxgYY7zEgDDDe95PXBTgHQPQHSAQaAmxmIiA5NmY3ZjQ0MjQ4OWFmMTU1MDZlMTNlZjllZjRhM2U2ZA",
        "_bd_ticket_crypt_cookie": "aaa212ac71eafba36074679e0e22d0a6",
        "__security_mc_1_s_sdk_sign_data_key_web_protect": "7c9ebad3-4793-8a6c",
        "__security_mc_1_s_sdk_cert_key": "2b2e7442-44b4-a2d7",
        "__security_server_data_status": "1",
        "publish_badge_show_info": "%220%2C0%2C0%2C1757765035002%22",
        "DiscoverFeedExposedAd": "%7B%7D",
        "SelfTabRedDotControl": "%5B%5D",
        "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D",
        "biz_trace_id": "54d4e460",
        "odin_tt": "4e68ff1158787961f01a54e7c9f5f72abd624c32f7d0a99679c45a5c819d9bf5b7e2165a659b8d9290e514e1eecfe531",
        "session_tlb_tag": "sttt%7C1%7Clvf0Qkia8VUG4T7570o-bf________-mAp5CTjz3OZtcbkSEiAn7GY0c18ZIDub-id_SlluPmBc%3D",
        "ttwid": "1%7CspbR7NrdY5_vVJSZMtJIOg25nJnpGb3NmgVtf4ISmgo%7C1757765097%7Ca7236d69c4757cec1838a8a6ca086d598c5c20def7e66b25a0041c81c6499080",
        "IsDouyinActive": "true",
        "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1708%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.55%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A350%7D%22",
        "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22",
        "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS250ZzR1U0wrYUU2RGdzV3ZkeTg3VkdDcDB2YVhZM0xlcjFkaERsSElmWEcxOW01QTFGbGlyeUJNK2IvL2tCaEh6dU9WeHFHTlp3djU2V05HUk1sU3c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
        "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAAMkvz4-m0JcwrKGPMXtDjbXglYnXyzh-om27dq66uu-w%2F1757779200000%2F0%2F0%2F1757766100474%22",
        "FOLLOW_NUMBER_YELLOW_POINT_INFO": "%22MS4wLjABAAAAMkvz4-m0JcwrKGPMXtDjbXglYnXyzh-om27dq66uu-w%2F1757779200000%2F0%2F1757765500474%2F0%22",
        "bd_ticket_guard_client_data_v2": "eyJyZWVfcHVibGljX2tleSI6IkJLbnRnNHVTTCthRTZEZ3NXdmR5ODdWR0NwMHZhWFkzTGVyMWRoRGxISWZYRzE5bTVBMUZsaXJ5Qk0rYi8va0JoSHp1T1Z4cUdOWnd2NTZXTkdSTWxTdz0iLCJ0c19zaWduIjoidHMuMi4zZGIxMDMzYTUxODMwNTVmNWNkYTkwOTBmNzU5MmNlYTRiMmI1NTZhNjAwNzI0YzRmYjI0ODQ0MjcwMzBlMDRmYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJ1M1dWZEVpcVg2MjB3K0tKTU1EdFl0WEVubk1uVlY1L20ra3RhbTIvSHk0PSIsInNlY190cyI6IiNTdGxMODVnM1J4K0ZvS0R4SlRHcVpxWXdtSkxBRjFHek9rNXFwTS8vV0UvRUdBL09EWlVDelFZNFpYbFkifQ%3D%3D"
    }
    url = "https://www.douyin.com/aweme/v1/web/comment/list/"
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "aweme_id": aweme_id,
        "cursor": cursor,
        "count": "10",
        "item_type": "0",
        "insert_ids": "",
        "whale_cut_token": "",
        "cut_version": "1",
        "rcFT": "",
        "update_version_code": "170400",
        "pc_client_type": "1",
        "pc_libra_divert": "Windows",
        "support_h265": "1",
        "support_dash": "1",
        "cpu_core_num": "20",
        "version_code": "170400",
        "version_name": "17.4.0",
        "cookie_enabled": "true",
        "screen_width": "1708",
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
        "downlink": "1.55",
        "effective_type": "3g",
        "round_trip_time": "350",
        "webid": "7532039181900793363",
        "uifid": "30ff7b230d01f3ed4fd5546706fc508e0725b8a99e0ba4197a991a959864baf08b442342b5ec97ae63787ff5ac8d239161b41d0e573096a6fa8534ce34d4a481b5cfcfbb9ad2156c905ecc439357bc1342ca0cca205813585617eb9be3cafa4b0e1bb16d26aa9f028494eb078e9d7ba02cec9b839e4e19bf0d11c11545a60494dd6f736ba4608e7afd0df5145fc44679b61e104bf8bbe3cdb498735ff23aa4d3",
        "msToken": "meDkniXDXS_tUY_hl2fX-LRGoY74xlxKMZ0rd7OKP4plbREiPmcLJCwD-0qrR9954_jzPTx4qo-eWAh9GCYLDpxhWomLkEyPnMKIcJh5w3SwFjd3F4vyqVUeJt4-_LPor9MK7zBOgAs2zcIHKvE5lXCfvddcpZtvY8n2UpFb27bqLa6AeozQUio=",
        "a_bogus": "QJ0RkHtjxxRcPdFS8CaXe7xU67DANBuy9eTQWxMP9NTdOXeY-RP7LneAbxqJs0EDKmpzwCIHjd0AbDxcs4UTZKrpzmkDuKXRYs/5Iw8LM1HZGGkgXNyiSJbEovszU8sYuAAtNZX5ls0iIEQIIq9TAdACq/4rBcbD0r-UV2uSi29sUWSjk9/9a37sOXwqFj==",
        "verifyFp": "verify_mfeqaxhh_tweQjRBg_9hZd_4NNx_8OOD_8ECkMxdlz7Bn",
        "fp": "verify_mfeqaxhh_tweQjRBg_9hZd_4NNx_8OOD_8ECkMxdlz7Bn"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(f"响应状态码: {response.status_code}")
    print(f"响应头: {dict(response.headers)}")
    print(f"响应内容长度: {len(response.text)}")
    print(f"响应内容前200字符: '{response.text[:200]}'")
    
    # 检查是否是空响应
    if not response.text.strip():
        print("⚠️ 服务器返回空响应，可能被反爬虫拦截")
        return None
    
    # 检查响应是否为有效JSON
    try:
        return response.json()
    except ValueError as e:
        print(f"JSON解析错误: {e}")
        print(f"完整响应内容: '{response.text}'")
        return None

def parseData(feed, awesme_id):
    ip_label=feed['ip_label']
    try:
        username=feed['user']['nickname']
    except:
        username='暂无用户名'
    
    comment_dict={
        '用户id':feed['user']['uid'],
        "用户名":username,
        "评论时间":get_time(feed['create_time']),
        'IP地址':ip_label,
        '评论内容':feed['text'],
        '点赞数量':feed['digg_count'],
        '视频id':awesme_id
    }
    print(comment_dict)
    writer.writerow(comment_dict)


def search_comment(aweme_id):
    cursor=10
    page=1
    while True:
        response=get_json(aweme_id,cursor)
        
        # 检查响应是否有效
        if response is None:
            print(f"获取评论失败，视频ID: {aweme_id}")
            break
            
        try:
            if response['comments'] is None:
                break
        
            feeds=response['comments']
            for feed in feeds:
                parseData(feed,aweme_id)
                break

            if response['has_more']==0:
                break
            cursor+=20
            page+=1
            if page>20:
                break
        except Exception as e:
            print(f'爬取失败，错误{e}')

if __name__=="__main__":
    header=['用户id','用户名','评论时间','IP地址','评论内容','点赞数量','视频id']
    
    
    f=open('comment_data.csv', 'w', encoding='utf-8',newline='')
    writer=csv.DictWriter(f,header)
    writer.writeheader()
    df=pd.read_csv('data.csv')
    for index,row in df.iterrows():
        search_comment(row['视频id'])
        break