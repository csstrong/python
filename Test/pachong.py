import requests
import re
import lxml.html


class ExamSpider(object):
    def __init__(self):
        self.base_url = 'http://datamining.comratings.com/exam'
        self.r_session = requests.session()

    def down_first(self):
        """
        进行第一次访问
        :return: sessionid
        """
        res = self.r_session.get(self.base_url)
        sessionid = res.cookies.get_dict().get('session')
        return sessionid

    def down_second(self, cookie):
        """
        进行第二次访问
        :param cookie: 访问需要的完整cookie
        :return: 响应结果
        """
        result = self.r_session.get(self.base_url + '3', cookies=cookie)
        return result.content

    def f1(self, a):
        """
        获得js动态加载的cookie
        :param a: 第一次访问获得到的cookie中的sessionid
        :return: js动态加载的cookie
        """
        encoderchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        b = ""
        i = 0
        length = len(a)
        while i < length:
            # charCodeAt() 方法可返回指定位置的字符的 Unicode 编码
            c = ord(a[i]) & 0xff
            i += 1
            if i == length:
                b += encoderchars[c >> 2]
                b += encoderchars[(c & 0x3) << 4]
                b += "=="
                break
            c2 = ord(a[i])
            i += 1
            if i == length:
                b += encoderchars[c >> 2]
                b += encoderchars[((c & 0x3) << 4) | ((c2 & 0xf0) >> 4)]
                b += encoderchars[(c2 & 0xf) << 2]
                b += "="
                break
            c3 = ord(a[i])
            i += 1
            b += encoderchars[c >> 2]
            b += encoderchars[((c & 0x3) << 4) | ((c2 & 0xf0) >> 4)]
            b += encoderchars[((c2 & 0xf) << 2) | ((c3 & 0xc0) >> 6)]
            b += encoderchars[c3 & 0x3f]
        return b

    def make_cookie(self, sessionid):
        """
        获得完整的cookie
        :param sessionid: 第一访问得到的sessionid
        :return: 完整的cookie
        """
        lt = []
        lt.append("session=" + sessionid + ';')
        lt.append("c1=" + self.f1(sessionid[1:4]) + ';')
        lt.append("c2=" + self.f1(sessionid))

        cookie = {
            'Cookie': " ".join(lt)
        }
        return cookie

    def save_result(self, result):
        """
        将结果保存进文件中
        :param result: 第二次访问的响应结果
        :return:
        """

        with open("iptest.html", "wb") as fp:
            fp.write(result)

    def get_content_ip(self, result):
        result_data = result.decode("utf8")
        none_list = re.findall(r'\.([A-Z]+){display:none}', result_data, re.S)
        # print(none_list)
        div_pattern = re.compile('<div.*?</div>')
        div_none_list = div_pattern.sub("", result_data)

        span_pattern = re.compile('<span style="display:none">.*?</span>')
        span_none_list = span_pattern.sub("", div_none_list)

        span_pattern1 = re.compile(
            '<span class="' + none_list[0] + '">(.*?)</span>')
        span_none_list1 = span_pattern1.sub("", span_none_list)

        span_pattern2 = re.compile(
            '<span class="' + none_list[1] + '">(.*?)</span>')
        span_none_list2 = span_pattern2.sub("", span_none_list1)

        ip_html_list = span_none_list2.split("<br>")[1:]
        ip_list = []
        for ip_html in ip_html_list:
            html = lxml.html.fromstring(ip_html.replace("\n", ""))
            ip_str = html.xpath("//text()")
            ip = ""
            for i in ip_str:
                ip += i
            ip_list.append(ip)
        print(ip_list)
        print(len(ip_list))

    def run(self):
        """
        运行主线程
        :return:
        """
        sesionid = self.down_first()
        cookie = self.make_cookie(sesionid)
        result = self.down_second(cookie)
        self.get_content_ip(result)
        self.save_result(result)


if __name__ == '__main__':
    crawl = ExamSpider()
    crawl.run()
