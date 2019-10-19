
# coding: utf-8

# # 地理编码

# In[76]:


import requests


# In[77]:


key_map='e74e30eea477decea257a35187b91d58'
def geo(address:str) ->dict:
    """获取地理编码"""
    url='https://restapi.amap.com/v3/geocode/geo?parameters'
    params={
        'key':key_map,
        'address':address,
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data


# In[78]:


geo('广东省广州市从化区中山大学南方学院')


# ## 路径规划

# In[79]:


key_map='e74e30eea477decea257a35187b91d58'
def walking(origin,destination):
    """步行路径规划"""
    url='https://restapi.amap.com/v3/direction/walking?parameters'
    params={
        'key':key_map,
        'origin':origin,
        'destination':destination,
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data


# In[116]:


geo('广东省广州市从化区龙岗')


# In[81]:


walking('113.679287,23.632575','113.668051,23.600869')


# In[82]:


help(geo)


# ## 行政区域查询

# In[83]:


key_map='e74e30eea477decea257a35187b91d58'
def district(keywords):
    """行政区域查询"""
    url='https://restapi.amap.com/v3/config/district?parameters'
    params={
        'key':key_map,
        'keywords':keywords,
        'subdistrict':2,
        'extensions':'base',
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data


# In[84]:


district('深圳')


# ## 搜索POI

# In[85]:


key_map='e74e30eea477decea257a35187b91d58'
def text(keywords):
    """搜索POI"""
    url='https://restapi.amap.com/v3/place/text?parameters'
    params={
        'key':key_map,
        'keywords':'麦当劳|肯德基',
        'type':2,
        'city':'440117',
        'citylimit':'true',
        'extensions':'base',
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data
text('麦当劳|肯德基')


# ## IP定位

# In[86]:


key_map='e74e30eea477decea257a35187b91d58'
def ip():
    """IP定位"""
    url='https://restapi.amap.com/v3/ip?parameters'
    params={
        'key':key_map,
        'ip':'10.10.240.37',
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data
ip()


# ## 批量请求接口

# In[87]:


url_api="https://restapi.amap.com/v3/batch?key=<e74e30eea477decea257a35187b91d58>" 
{
    "ops": [
        {
            "url": "/v3/place/around?offset=10&page=1&key=<e74e30eea477decea257a35187b91d58>&location=116.50394379585519,39.278209477408794&output=json&radius=100000&types=080000"
        },
        {
            "url": "/v3/place/around?offset=10&page=1&key=<e74e30eea477decea257a35187b91d58>&location=118.50394379585519,39.278209477408794&output=json&radius=100000&types=080000"
        }
    ]
}


# ## 静态地图

# In[88]:


import requests
from PIL import Image
from io import BytesIO

def ditu(location):
    url_api="http://restapi.amap.com/v3/staticmap" 
    parameters = {'key': 'e74e30eea477decea257a35187b91d58', 
              'location':'113.491633,23.448368',
              'zoom':13,
              'size':'1024*768'
              }
    response=requests.get(url_api, params=parameters)
    data=Image.open(BytesIO(response.content))
    return data
ditu('113.491633,23.448368')


# ## 坐标转化

# In[118]:


key_map='e74e30eea477decea257a35187b91d58'
def convert(locations):
    """坐标转化"""
    url='https://restapi.amap.com/v3/assistant/coordinate/convert?parameters'
    params={
        'key':key_map,
        'locations':'38.65777,104.08296',
        'coordsys':'mapbar',
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data
convert('38.65777,104.08296') #百度坐标


# ## 天气查询

# In[91]:


key_map='e74e30eea477decea257a35187b91d58'
def weather(city):
    """天气查询"""
    url='https://restapi.amap.com/v3/weather/weatherInfo?parameters'
    params={
        'key':key_map,
        'city':440117 ,
        'extensions':'base',
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data


# In[92]:


weather('440117')


# ## 输入提示

# In[93]:


key_map='e74e30eea477decea257a35187b91d58'
def inputtips(keywords):
    """输入提示"""
    url='https://restapi.amap.com/v3/assistant/inputtips?parameters'
    params={
        'key':key_map,
        'keywords':'肯德基',
        'city':440117,
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data


# In[94]:


inputtips('肯德基')


# ## 交通态势

# In[95]:


key_map='e74e30eea477decea257a35187b91d58'
def circle():
    """指定线路交通态势"""
    url='https://restapi.amap.com/v3/traffic/status/circle?parameters'
    params={
        'key':key_map,
        'level':4,
        'adcode':440105,
        'name':'滨江东路',
        'extensions':'base',
        'location':'113.293046,23.103682,',
        'output':'json',
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data
circle()


# ## 地理围栏

# In[109]:


def meta():
    """创建围栏"""
    url='https://restapi.amap.com/v4/geofence/meta?key=e74e30eea477decea257a35187b91d58'
    params={
        'name':"围栏名称",
        'center':'113.293046,23.103682',
        'radius':'3000', 
        'enable': 'true',
        'repeat': 'Mon,Tues,Wed,Thur,Fri,Sat,Sun',
        'valid_time': '2019-10-19'
    }
    data=requests.post(url,json=params).json()
    return data
meta()


# ## 轨迹纠偏

# In[119]:


key_map='e74e30eea477decea257a35187b91d58'
def add(name):
    """创建服务"""
    url='https://tsapi.amap.com/v1/track/service/add'
    params={
        'key':key_map,
        'name':'广州佛山',
    }
    response=requests.post(url,params=params)
    data=response.json()
    return data
add('name')


# In[120]:


key_map='e74e30eea477decea257a35187b91d58'
def list():
    """查询服务"""
    url='https://tsapi.amap.com/v1/track/service/list'
    params={
        'key':key_map,
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data
list()


# # 在调用每一个功能的同时，思考其背后是否含有ML、AI的功能（比如计算机视觉、语音识别、推荐算法等），并整理思考的结果，在调用API代码模块中用markdown说明
# 
# ## 地理编码-获取地理编码
# *地理编码：将详细的结构化地址转换为高德经纬度坐标。且支持对地标性名胜景区、建筑物名称解析为高德经纬度坐标。*
# ## 路径规划-步行路径规划
# *路径规划API是一套以HTTP形式提供的步行、公交、驾车查询及行驶距离计算接口，返回JSON 或 XML格式的查询数据，用于实现路径规划功能的开发*
# ## 行政区域查询
# *根据用户输入的搜索条件可以帮助用户快速的查找特定的行政区域信息。*
# ## 搜索POI
# *提供多种查询POI信息的能力，其中包括关键字搜索、周边搜索、多边形搜索、ID查询四种筛选机制。*
# ## IP定位
# *根据用户输入的IP地址，能够快速的帮用户定位IP的所在位置。*
# ## 静态地图
# *静态地图服务通过返回一张地图图片响应HTTP请求，使用户能够将高德地图以图片形式嵌入自己的网页中。用户可以指定请求的地图位置、图片大小、以及在地图上添加覆盖物，如标签、标注、折线、多边形。*
# ## 坐标转换
# *坐标转换是一类简单的HTTP接口，能够将用户输入的非高德坐标（GPS坐标、mapbar坐标、baidu坐标）转换成高德坐标。*
# ## 天气查询
# *根据用户输入的adcode，查询目标区域当前/未来的天气情况。*
# ## 输入提示
# *提供根据用户输入的关键词查询返回建议列表。*
# ## 交通态势-指定线路交通态势
# *提供根据用户输入的内容能够返回希望查询的交通态势情况。*
# ## 地理围栏-创建围栏
# *提供在服务端，增删改查地理围栏的功能，同时支持对于设备与围栏关系进行监控*
# ## 轨迹纠偏-创建服务、查询服务
# *根据坐标点抓取道路，即根据给定的坐标点、车辆的方位角以及行驶速度，将用户的轨迹纠偏到路上，从而返回用户实际驾车经过的道路坐标。*
#  
# ### 整理发现
# 
# 高德API中的**路径规划**类似于人工智能AI的路径规划，计算当前道路的拥挤状况，推荐最佳的路径选择。
# 
# **静态地图**则是运用了计算机视觉，将周围的环境通过视觉语言的形式呈现出来，还有路标，位置信息，道路等。
# 
# **IP定位**、**天气查询**、**交通态势**、**输入提示**、**地理围栏**和**轨迹纠偏**，我觉得背后的是用人工智能的算法推荐，才能获得信息。

# # 尝试设计一个简单的应用（不要求写代码），至少涉及3个API功能。
# 
# ### API调用
# - 天气查询
# - 交通态势
# - 路径规划
# - 输入提示
# 
# ### 主要功能
# 
# 出门前查询当前的天气，搜索到达的目的地，搜索目的地的同时有输入提示用户，展示当前的交通路况，并为用户提供最佳的路径。
