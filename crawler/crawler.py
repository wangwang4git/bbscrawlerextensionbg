# -*- coding: utf-8 -*-
import requests

"""Main module."""

if __name__ == '__main__':
    print('hello bbs')
    # 搜索家具url
    target = 'http://bbs.oa.com/forum/search?k=%E5%AE%B6%E5%85%B7'
    # 请求header
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Cache-Control': 'no-cache',
        'Cookie': 'pgv_pvi=8951306240; pgv_pvid=7760949711; pt2gguin=o0382691460; isConventionAlert=true; x_host_key=168b10552e4-32969bfd30b4540a90f4d190b16c848bcff8e6d1; x-host-key-ngn=168b10365a9-eb593a4e1062586489a05cddc1cb669778ae843c; x-host-key-front=168b10554f1-f2ae2530dcb660a177f791ac66aa9b7a5d9f7515; pgv_si=s8996730880; TCOA_TICKET=FAF495157DF1B5E27E6B42C0ED9D4A66C1B4C2349E0082C47A92E3CBC4A9EF6386FD6355EC4DD18C90B96F47155E911890E3D07F520D3A03955FB3133E208CC4320CB864F763B8F5CD9E31B68D97E692AD4CC40D5AB9EAB9967ACA62A99C7FE6468524F7765A48246C62447A1F6AEBD8AAE00949737466688C6158E5DA13B1DA9439C22EF3FE7ED6B68DBF607F5769E6BF71ED300A12D3E8F95A50F53F407268041CB05CB8293773; TCOA=30du30EpAx; RIO_TCOA_TICKET=tof:FAF495157DF1B5E2F1FA7504FBBF75838AD8F638AAF7BF56DEC1479EB79F90440463507D7A19EED7855353BDFD7C481CCFEF72B403979638DCB3C2E67E2D931791D8B0EE3FDB5BFD1C9603823DF96256784CBEBB81BC87E48BC4EA7A6E080CD5052AFE44B8EEF5B3EB005F2DAAE2C72A069282EF4A6A9018E1F8CEBE361B9A6BA5A64890000FE9D0B174737B2AD55708F80A153315A0443BFD42D1436475998E20C5CAE38604A64591DD4118A01345928A2E2EC15F2B2E4B8A4A5EDB059854DA; SSOTicket3=E7A95E61A312BE0C3E18AE36124C7F79D6AED252AB7E43E261076BBDAD95EABBC8B7E429C98F33F9E9165A532416607784B34B9B58C9217385802693C7242B1B15E7CBED110043574053D2AAD0093450; SSOTicket2=A5F86532634B8306FC38D2197F8D727188C668670371A29DFBBD1EDD32E12E8DF68BAC747A6EFFC92F9EC422D95AD9FB01C864B5C5B2CE1EF0D7B6C19CF66FBA838742A8131021833EBBAC7FD087B2B9; t_uid=victorwwang; km_uid=victorwwang; km_u=12f5a485f92147b4a4c2b48ed4b85c38401cd9f6f3b1c69d36d7e4740574454d9ecc691da52db19b; CAKEPHP=5pi2qojoimm85ani3rejiutd83',
        'Host': 'bbs.oa.com',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://bbs.oa.com/forum/search?k=%E5%AE%B6%E5%85%B7',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    # proxies = {"http": "http://web-proxy.tencent.com:8080"}
    # req = requests.get(url=target, headers=headers, proxies=proxies)
    req = requests.get(url=target, headers=headers)
    print(req.text)
