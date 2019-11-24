from poium import Page,PageElement

'''
创建BaiduPage类，使其继承poium库中的Page类，调用PageElement类定义元素定位，
并赋值给变量search_input和search_button。
'''

class BaiduPage(Page):
    '''百度Page层 百度页面封装操作到的元素'''
    search_input = PageElement(id_ = 'kw')
    search_button = PageElement(id_ = 'su')
