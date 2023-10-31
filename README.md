## 提示
1. 有封号风险.
2. 由于文心一言的Acs-Token算法的参数不定时的变化,所以包里调用了API.感兴趣的或有自动更新方法的可以联系我.
3. 若出现了`用户访问被限制`请到[Isuue](https://github.com/XiaoXinYo/Easy-Ernie/issues/6)回复,我会及时更新Acs-Token算法的参数.
---
![Release](https://img.shields.io/badge/Release-0.1.9-blue)
---
## 介绍
简洁的调用文心一言的WebAPI.
## 需求
1. 语言: Python3.8+.
2. 包: requests.
3. 其他: 文心一言账户.
## 安装
`pip install easy-ernie --upgrade`
## Cookie
![图片1](https://s1.ax1x.com/2023/04/26/p9KDUYR.md.png)
1. 访问[文心一言](https://yiyan.baidu.com).
2. 打开开发者工具.
3. 找到应用程序(Application).
4. 在左侧点击存储(Storage)-Cookies-https://yiyan.baidu.com.
5. 在列表中点击BAIDUID.
6. 复制下方Value的值.
7. BDUSS_BFESS同理.
## 使用
### Ernie
```python
from easy_ernie import Ernie

if __name__ == '__main__':
    ernie = Ernie('BAIDUID', 'BDUSS_BFESS')
    sessionName = '你好'
    result1 = ernie.ask('你好', sessionName=sessionName)
    sessionId = result1['sessionId']
    chatBotId = result1['chatBotId']
    print(result1)
    result2 = ernie.ask('我给你发的上一个消息是什么', sessionId=sessionId, sessionName=sessionName, parentChatId=chatBotId)
    print(result2)
    ernie.deleteConversation(sessionId)
```
### FastErinie
```python
from easy_ernie import FastErnie

if __name__ == '__main__':
    fastErnie = FastErnie('BAIDUID', 'BDUSS_BFESS')
    print(fastErnie.ask('你好'))
    print(fastErnie.ask('我给你发的上一个消息是什么'))
    fastErnie.close()
```
更多方法查看[Wiki](https://github.com/XiaoXinYo/Easy-Ernie/wiki).
## 感谢
灵感来源自[acheong08](https://github.com/acheong08),[ls233](https://github.com/lss233).