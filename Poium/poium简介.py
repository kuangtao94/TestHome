from poium import PageElement,Page,PageElements

# 1.poium支持的8种定位方法

class SomePage(Page):
    elem_id = PageElement(id_='id')
    elem_name = PageElement(name_='name')
    elem_class = PageElement(class_name='class')
    elem_tag = PageElement(tag='input')
    elem_link_text = PageElement(link_text='this is link')
    elem_partial_link_text = PageElement(partial_link_text='is link')
    elem_xpath = PageElement(xpath='//*[@id="kw"]')
    elem_css = PageElement(css='#id')

# 2.设置元素超时时间 默认为10s

class BaiduPage(Page):
    search_input = PageElement(id_='kw',timeout=5)
    search_button = PageElement(id_='su',timeout=30)

# 3.设置元素描述
#当一个Page类中定义的元素非常多时，必须通过注释来增加可读性，这时可以使用的describe参数
#强调:describe参数并无实际意义，只是增加了元素定位的可读性

class LoginPage(Page):
    '''登录Page类'''
    username = PageElement(css='#loginAccount',describe='用户名')
    password = PageElement(css='#loginpwd',describe='密码')
    login_button = PageElement(css='#login_btn',describe='登录按钮')
    user_info = PageElement(css='a.nav_user_name>span',describe='用户信息')


# 4.定位一组元素

class ResultPage(Page):
    #定位一组元素
    search_input = PageElements(xpath='//div/h3/a')