import random
import re
import time
from front_login import front_login
import json
import sys


class test_land_page:
    def __init__(self, stop_time):
        self.driver = front_login("17701204526", "liyan0527")
        self.stop_time = stop_time

    # 商标专利
    def open_page(self, url, page_name, page, buttom):
        self.driver.get(url)
        self.driver.find_element_by_xpath(".//input[@id='search-content']").send_keys("电吹风机_技术测试")
        self.driver.find_element_by_xpath(".//div[@class='btn fl']").click()
        time.sleep(2)
        # send_phone = '16619923387'
        send_phone = self.make_phone()
        self.driver.find_element_by_xpath(".//input[@id='search_phone']").send_keys(send_phone)
        self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
        time.sleep(10)
        code = self.get_code().get(send_phone)
        print(send_phone, code)
        if code:
            self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code)
            self.driver.find_element_by_xpath(".//div[@id='download']").click()
            time.sleep(3)
            return_text = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
            print("推送结果：", return_text)
            if return_text == "专属顾问会马上联系您，为您极速办理！":
                self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                print("{}着陆页推送成功！".format(page_name))
                send_result = "推送成功"
            else:
                send_result = "未推送成功！"
                print("{}着陆页推送失败！".format(page_name))

        else:
            send_result = "未推送成功！"
            print("{}着陆页验证码错误！".format(page_name))

        infos = {
            "phone": send_phone,
            "code": code,
            "result": send_result,
            "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
            "page": page,
            "page_name": page_name,
            "location": "顶部线索"
        }
        self.write_log(infos)
        # land页面底部线索推送
        # 向下滚动页面
        if page == "land" and buttom == 1:
            self.driver.refresh()
            time.sleep(self.stop_time)
            scroll_js = "window.scrollTo(0,1000)"
            self.driver.execute_script(scroll_js)
            send_phone = self.make_phone()
            self.driver.find_element_by_xpath(".//input[@id='tan2-phone']").send_keys(send_phone)
            self.driver.find_element_by_xpath(".//div[@class='con']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
            time.sleep(10)
            code2 = self.get_code().get(send_phone)
            print(send_phone, code2)
            if code2:
                self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code2)
                self.driver.find_element_by_xpath(".//div[@id='download']").click()
                time.sleep(3)
                return_text2 = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
                print("底部线索推送结果：", return_text2)
                if return_text2 == "专属顾问会马上联系您，为您极速办理！":
                    self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                    print("{}着陆页底部线索推送成功！".format(page_name))
                    send_result2 = "推送成功"
                else:
                    send_result2 = "推送失败"
                    print("{}着陆页底部线索推送失败！".format(page_name))
            else:
                send_result2 = "推送失败"
                print("{}着陆页底部线索验证码错误！".format(page_name))

            infos2 = {
                "phone": send_phone,
                "code": code2,
                "result": send_result2,
                "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                "page": page,
                "page_name": page_name,
                "location": "底部线索"
            }

            self.write_log(infos2)
    # 版权
    def banquan_page(self, url, page_name, page, buttom):
        self.driver.get(url)
        self.driver.find_element_by_xpath(".//input[@id='search-content']").send_keys("刘冬洋_技术测试")
        # send_phone = '16619923387'
        send_phone = self.make_phone()
        self.driver.find_element_by_xpath(".//input[@class='search-phone fl']").send_keys(send_phone)
        self.driver.find_element_by_xpath(".//span[@id='form-click']").click()
        time.sleep(2)
        # self.driver.find_element_by_xpath(".//input[@id='search_phone']").send_keys(send_phone)
        self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
        time.sleep(10)
        code = self.get_code().get(send_phone)
        print(send_phone, code)
        if code:
            self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code)
            self.driver.find_element_by_xpath(".//div[@id='download']").click()
            time.sleep(3)
            return_text = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
            print("推送结果：", return_text)
            if return_text == "专属顾问会马上联系您，为您极速办理！":
                self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                print("{}着陆页推送成功！".format(page_name))
                send_result = "推送成功"
            else:
                send_result = "推送失败"
                print("{}着陆页底部线索推送失败！".format(page_name))
        else:
            send_result = "推送失败"
            print("{}着陆页底部线索验证码错误！".format(page_name))

        infos = {
            "phone": send_phone,
            "code": code,
            "result": send_result,
            "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
            "page": page,
            "page_name": page_name,
            "location": "顶部线索"
        }
        self.write_log(infos)

        # land页面底部线索推送
        # 向下滚动页面
        if page == "land" and buttom == 1:
            self.driver.refresh()
            time.sleep(self.stop_time)
            scroll_js = "window.scrollTo(0,500)"
            self.driver.execute_script(scroll_js)
            send_phone = self.make_phone()
            self.driver.find_element_by_xpath(".//input[@id='tan2-phone']").send_keys(send_phone)
            self.driver.find_element_by_xpath(".//div[@class='con']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
            time.sleep(10)
            code2 = self.get_code().get(send_phone)
            print(send_phone, code2)
            if code2:
                self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code2)
                self.driver.find_element_by_xpath(".//div[@id='download']").click()
                time.sleep(3)
                return_text2 = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
                print("底部线索推送结果：", return_text2)
                if return_text2 == "专属顾问会马上联系您，为您极速办理！":
                    self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                    print("{}着陆页底部线索推送成功！".format(page_name))
                    send_result2 = "推送成功"
                else:
                    send_result2 = "推送失败"
                    print("{}着陆页底部线索推送失败！".format(page_name))
            else:
                send_result2 = "推送失败"
                print("{}着陆页底部线索验证码错误！".format(page_name))

            infos2 = {
                "phone": send_phone,
                "code": code2,
                "result": send_result2,
                "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                "page": page,
                "page_name": page_name,
                "location": "底部线索"
            }

            self.write_log(infos2)

    # 专利交易
    def patent_mark(self, url, page_name, page, buttom):
        self.driver.get(url)
        self.driver.find_element_by_xpath(".//input[@id='search-content']").send_keys("电吹风机_技术测试")
        self.driver.find_element_by_xpath(".//span[@class='search-jy-btn fl']").click()
        time.sleep(2)
        # send_phone = '16619923387'
        send_phone = self.make_phone()
        self.driver.find_element_by_xpath(".//input[@id='same-input']").send_keys(send_phone)
        self.driver.find_element_by_xpath(".//input[@id='reg_sendsms1']").click()
        time.sleep(10)
        code = self.get_code().get(send_phone)
        print(send_phone, code)
        if code:
            self.driver.find_element_by_xpath(".//input[@id='logCode1']").send_keys(code)
            self.driver.find_element_by_xpath(".//p[@class='reseaut-btn']").click()
            time.sleep(3)
            return_text = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
            print("推送结果：", return_text)
            if return_text == "专属顾问会马上联系您，为您极速办理！":
                self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                print("{}着陆页推送成功！".format(page_name))
                send_result = "推送成功"
            else:
                send_result = "未推送成功！"
                print("{}着陆页推送失败！".format(page_name))

        else:
            send_result = "未推送成功！"
            print("{}着陆页验证码错误！".format(page_name))

        infos = {
            "phone": send_phone,
            "code": code,
            "result": send_result,
            "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
            "page": page,
            "page_name": page_name,
            "location": "顶部线索"
        }
        self.write_log(infos)

        # 专利交易中部线索狂推送
        self.driver.refresh()
        time.sleep(self.stop_time)
        scroll_js1 = "window.scrollTo(0,5000)"
        self.driver.execute_script(scroll_js1)
        send_phone = self.make_phone()
        self.driver.find_element_by_xpath(".//input[@id='bottom-input']").send_keys(send_phone)
        self.driver.find_element_by_xpath(".//div[@class='fl screen12-jy-btn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
        time.sleep(10)
        code3 = self.get_code().get(send_phone)
        print(send_phone, code3)
        if code3:
            self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code3)
            self.driver.find_element_by_xpath(".//p[@class='button']").click()
            time.sleep(3)
            return_text3 = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
            print("中部线索推送结果：", return_text3)
            if return_text3 == "专属顾问会马上联系您，为您极速办理！":
                self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                print("{}着陆页中部线索推送成功！".format(page_name))
                send_result3 = "推送成功"
            else:
                send_result3 = "推送失败"
                print("{}着陆页中部线索推送失败！".format(page_name))
        else:
            send_result3 = "推送失败"
            print("{}着陆页中部线索验证码错误！".format(page_name))

        infos3 = {
            "phone": send_phone,
            "code": code3,
            "result": send_result3,
            "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
            "page": page,
            "page_name": page_name,
            "location": "中部线索"
        }

        self.write_log(infos3)


        # land页面底部线索推送
        # 向下滚动页面
        if page == "land" and buttom == 1:
            self.driver.refresh()
            time.sleep(self.stop_time)
            scroll_js2 = "window.scrollTo(0,500)"
            self.driver.execute_script(scroll_js2)
            send_phone = self.make_phone()
            self.driver.find_element_by_xpath(".//input[@id='tan2-phone']").send_keys(send_phone)
            self.driver.find_element_by_xpath(".//div[@class='fl jy-tan2-btn']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
            time.sleep(10)
            code2 = self.get_code().get(send_phone)
            print(send_phone, code2)
            if code2:
                self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code2)
                self.driver.find_element_by_xpath(".//p[@class='button']").click()
                time.sleep(3)
                return_text2 = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
                print("底部线索推送结果：", return_text2)
                if return_text2 == "专属顾问会马上联系您，为您极速办理！":
                    self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                    print("{}着陆页底部线索推送成功！".format(page_name))
                    send_result2 = "推送成功"
                else:
                    send_result2 = "推送失败"
                    print("{}着陆页底部线索推送失败！".format(page_name))
            else:
                send_result2 = "推送失败"
                print("{}着陆页底部线索验证码错误！".format(page_name))

            infos2 = {
                "phone": send_phone,
                "code": code2,
                "result": send_result2,
                "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                "page": page,
                "page_name": page_name,
                "location": "底部线索"
            }

            self.write_log(infos2)

    # 商标交易
    def trade_mark(self, url, page_name, page, buttom):
        self.driver.get(url)
        self.driver.find_element_by_xpath(".//input[@id='search-content']").send_keys("电吹风机_技术测试")
        self.driver.find_element_by_xpath(".//div[@class='btn fl']").click()
        time.sleep(2)
        # send_phone = '16619923387'
        send_phone = self.make_phone()
        self.driver.find_element_by_xpath(".//input[@id='search_phone']").send_keys(send_phone)
        self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
        time.sleep(10)
        code = self.get_code().get(send_phone)
        print(send_phone, code)
        if code:
            self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code)
            self.driver.find_element_by_xpath(".//div[@id='download']").click()
            time.sleep(3)
            return_text = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
            print("推送结果：", return_text)
            if "专属经纪人会马上联系您！" in return_text:
                self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                print("{}着陆页推送成功！".format(page_name))
                send_result = "推送成功"
            else:
                send_result = "未推送成功！"
                print("{}着陆页推送失败！".format(page_name))

        else:
            send_result = "未推送成功！"
            print("{}着陆页验证码错误！".format(page_name))

        infos = {
            "phone": send_phone,
            "code": code,
            "result": send_result,
            "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
            "page": page,
            "page_name": page_name,
            "location": "顶部线索"
        }
        self.write_log(infos)

        # 商标交易中部线索狂推送
        self.driver.refresh()
        time.sleep(self.stop_time)
        scroll_js1 = "window.scrollTo(0,5000)"
        self.driver.execute_script(scroll_js1)
        send_phone = self.make_phone()
        self.driver.find_element_by_xpath(".//input[@id='bottom-input']").send_keys(send_phone)
        self.driver.find_element_by_xpath(".//div[@class='fr btn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
        time.sleep(10)
        code3 = self.get_code().get(send_phone)
        print(send_phone, code3)
        if code3:
            self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code3)
            self.driver.find_element_by_xpath(".//div[@id='download']").click()
            time.sleep(3)
            return_text3 = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
            print("中部线索推送结果：", return_text3)
            if "您的信息已提交成功，" in return_text3:
                self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                print("{}着陆页中部线索推送成功！".format(page_name))
                send_result3 = "推送成功"
            else:
                send_result3 = "推送失败"
                print("{}着陆页中部线索推送失败！".format(page_name))
        else:
            send_result3 = "推送失败"
            print("{}着陆页中部线索验证码错误！".format(page_name))

        infos2 = {
            "phone": send_phone,
            "code": code3,
            "result": send_result3,
            "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
            "page": page,
            "page_name": page_name,
            "location": "中部线索"
        }

        self.write_log(infos2)


        # land页面底部线索推送
        # 向下滚动页面
        if page == "land" and buttom == 1:
            self.driver.refresh()
            time.sleep(self.stop_time)
            scroll_js = "window.scrollTo(0,500)"
            self.driver.execute_script(scroll_js)
            send_phone = self.make_phone()
            self.driver.find_element_by_xpath(".//input[@id='tan2-phone']").send_keys(send_phone)
            self.driver.find_element_by_xpath(".//div[@class='fl jy-tan2-btn']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//span[@id='reg_sendsms']").click()
            time.sleep(10)
            code2 = self.get_code().get(send_phone)
            print(send_phone, code2)
            if code2:
                self.driver.find_element_by_xpath(".//input[@id='logCode']").send_keys(code2)
                self.driver.find_element_by_xpath(".//div[@id='download']").click()
                time.sleep(3)
                return_text2 = self.driver.find_element_by_xpath(".//div[@class='comm']/p").text
                print("底部线索推送结果：", return_text2)
                if "专属经纪人会马上联系您！" in return_text2:
                    self.driver.find_element_by_xpath(".//div[@class='comm']/div/a[1]").click()
                    print("{}着陆页底部线索推送成功！".format(page_name))
                    send_result2 = "推送成功"
                else:
                    send_result2 = "推送失败"
                    print("{}着陆页底部线索推送失败！".format(page_name))
            else:
                send_result2 = "推送失败"
                print("{}着陆页底部线索验证码错误！".format(page_name))

            infos2 = {
                "phone": send_phone,
                "code": code2,
                "result": send_result2,
                "time": time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                "page": page,
                "page_name": page_name,
                "location": "底部线索"
            }

            self.write_log(infos2)

    # 提取验证码
    def get_code(self):
        windows = self.driver.window_handles
        if len(windows) < 2:
            url = "https://manage.zgg.com/com/bg/sms_code.html"
            js = "window.open()"
            self.driver.execute_script(js)
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
            self.driver.get(url)
        else:
            self.driver.switch_to.window(windows[-1])
            self.driver.refresh()
        time.sleep(1)
        phones = self.driver.find_elements_by_xpath(".//tbody/tr/th")
        codes = self.driver.find_elements_by_xpath(".//tbody/tr/td")

        phone_list = []
        for phone in phones:
            # print("手机号：",phone.text)
            result = re.search("\d{11}", phone.text)
            if result:
                phone = result.group()
                phone_list.append(phone)
            else:
                continue
        print('手机号列表',phone_list)
        code_dict = dict()
        num = 0
        for code in codes:
            # print("验证码：", code.text)
            phone_key = phone_list[num]
            code_dict.update({phone_key: code.text})
            # code_dict[phone_key] = code.text
            num += 1

        print("验证码列表：", code_dict)
        self.driver.switch_to.window(windows[0])
        return code_dict

    def write_log(self, infos):
        with open("send_log.txt", "a+", encoding="utf-8") as f:
            f.write(json.dumps(infos, ensure_ascii=False)+"\n")

    # 生成手机号
    def make_phone(self):
        phone = random.randint(16619920000, 16619929999)
        return str(phone)


def main(page, buttom, stop_time):
    res = test_land_page(stop_time)
    if page == "land":
        base_url = "https://www.zgg.com/land/{}.html"
    elif page == "gamma":
        base_url = "https://www.zgg.com/gamma/{}.html"
    else:
        raise TypeError("页面类型错误！")

    page_dict = {"landzl": "国内专利", "landsb": "国内商标", "landgjzl": "国际专利", "landgjsb": "国际商标",
                 "landbq": "版权", "landzljy": "专利交易", "landtmjy": "商标交易"}
    for page_name in page_dict.keys():
        url = base_url.format(page_name)
        if page_name == "landbq":
            try:
                print("推送页面：", page_dict.get(page_name))
                res.banquan_page(url, page_dict.get(page_name), page, buttom)
                time.sleep(stop_time)
            except Exception as e:
                print(e)
        elif page_name == "landzljy":
            try:
                print("推送页面：", page_dict.get(page_name))
                res.patent_mark(url, page_dict.get(page_name), page, buttom)
                time.sleep(stop_time)
            except Exception as e:
                print(e)
        elif page_name == "landtmjy":
            try:
                print("推送页面：", page_dict.get(page_name))
                res.trade_mark(url, page_dict.get(page_name), page, buttom)
                time.sleep(stop_time)
            except Exception as e:
                print(e)

        else:
            try:
                print("推送页面：", page_dict.get(page_name))
                res.open_page(url, page_dict.get(page_name), page, buttom)
                time.sleep(stop_time)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    parm = sys.argv[1:]
    if parm:
        page, bottom_clue, stop_time = parm[0], parm[1], parm[2]
        main(page, int(bottom_clue), int(stop_time))
