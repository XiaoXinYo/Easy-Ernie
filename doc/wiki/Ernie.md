## getConversation
```python
def getConversation(self) -> dict
```
1. 功能: 获取会话.
2. 返回示例:
```python
{
    'top': [{
        'sessionId': '17401225',
        'name': '你好',
        'state': 1,
        'creationTimestamp': 1701682120
    }],
    'normal': [{
        'sessionId': '37401225',
        'name': '你好',
        'state': 1,
        'creationTimestamp': 1701682120
    }]
}
```
## newConversation
```python
def newConversation(self, name: str) -> str
```
1. 功能: 新建会话.
2. 返回示例:
```python
'8417585'
```
## renameConversation
```python
def renameConversation(self, sessionId: str, name: str) -> bool
```
1. 功能: 重命名会话.
2. 返回示例:
```python
True
```
## deleteConversation
```python
def deleteConversation(self, sessionId: str) -> bool
```
1. 功能: 删除会话.
2. 返回示例:
```python
True
```
## deleteConversations
```python
def deleteConversations(self, sessionIds: list) -> bool
```
1. 功能: 批量删除会话.
2. 返回示例:
```python
True
```
## topConversation
```python
def topConversation(self, sessionId: str) -> bool
```
1. 功能: 置顶会话.
2. 返回示例:
```python
True
```
## cancelTopConversation
```python
def cancelTopConversation(self, sessionId: str) -> bool
```
1. 功能: 取消置顶会话.
2. 返回示例:
```python
True
```
## getConversationDetail
```python
def getConversationDetail(self, sessionId: str) -> Optional[dict]
```
1. 功能: 获取会话详情.
2. 返回示例:
```python
{
    'base': {
        'name': '你好',
        'state': 1,
        'creationTimestamp': 1701682120
    },
    'histories': [
        {
            'chatId': '168463680',
            'role': 'user',
            'text': '你好',
            'creationTimestamp': 1701677042
        },
        {
            'chatId': '168463681',
            'role': 'robot',
            'text': '你好！我很高兴为你提供帮助。请问有什么我可以为你做的吗？',
            'creationTimestamp': 1701677042
        },
        {
            'chatId': '168463679',
            'role': 'robot',
            'text': '',
            'creationTimestamp': 1701677042,
        }
    ],
    'currentChatId': '168463681'
}
```
提示: `currentChatId`为`askStream`或`ask`的`parentChatId`.
## getShareConversation
```python
def getShareConversation(self) -> list
```
1. 功能: 获取分享会话.
2. 返回示例:
```python
[
    {
    'shareId': '1521',
    'sessionId': '3110956036',
    'chatIds': ['168463680', '168463681', '168463679'],
    'key': 'IUGAEK',
    'creationTimestamp': 1701677042,
    'userId': '7654765',
    }
]
```
## deleteShareConversation
```python
def deleteShareConversation(self, shareId: str) -> bool
```
1. 功能: 删除分享会话.
2. 返回示例:
```python
True
```
## deleteShareConversations
```python
def deleteAllShareConversation(self, userId: str) -> bool
```
1. 功能: 删除全部分享会话.
2. 返回示例:
```python
True
```
## shareConversation
```python
def shareConversation(self, sessionId: str, chatIds: list) -> str
```
1. 功能: 分享会话.
2. 返回示例:
```python
'IUGAEK'
```
## askStream
```python
def askStream(self, question: str, sessionId: str, parentChatId: str) -> Generator
```
1. 功能: 流提问.
2. 返回示例:
```python
{'answer': '我画好了，欢迎对我提出反馈和建议，帮助我快速进步。', 'urls': ['http://eb118-file.cdn.bcebos.com/upload/F09A18443610CE467F76C5F67E4340B0?x-bce-process=style/wm_ai'], 'chatId': '78059153', 'done': False}

{'answer': '\n', 'urls': [], 'chatId': '78059153', 'done': False}

{'answer': '你可以完整描述你的需求来继续作画，如：“帮我画一枝晶莹剔透的牡丹花”。', 'urls': [], 'chatId': '78059153', 'done': False}

{'answer': '我画好了，欢迎对我提出反馈和建议，帮助我快速进步。\n你可以完整描述你的需求来继续作画，如：“帮我画一枝晶莹剔透的牡丹花”。', 'urls': ['http://eb118-file.cdn.bcebos.com/upload/F09A18443610CE467F76C5F67E4340B0?x-bce-process=style/wm_ai'], 'botChatId': '78059153', 'done': True}
```
提示: 首次提问`parentChatId`填`'0'`, `botChatId`作为下一次调用的`parentChatId`.
## ask
```python
def ask(self, question: str, sessionId: str, parentChatId: str) -> dcit
```
1. 功能: 提问.
2. 返回示例:
```python
{'answer': '我画好了，欢迎对我提出反馈和建议，帮助我快速进步。\n你可以完整描述你的需求来继续作画，如：“帮我画一枝晶莹剔透的牡丹花”。', 'urls': ['http://eb118-file.cdn.bcebos.com/upload/F09A18443610CE467F76C5F67E4340B0?x-bce-process=style/wm_ai'], 'botChatId': '78059153'}
```
提示: 首次提问`parentChatId`填`'0'`, botChatId作为下一次调用的`parentChatId`.