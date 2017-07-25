## 一. django app设计
1. user - 用户管理
2. course - 课程管理
3. organization - 机构和教师管理
4. operation - 用户操作管理
## 二. 各app的models设计

## 三. 数据表生成与修改

## 数据库设计
django app设计
users models.py 编写 
courses models.py 编写 
organization models.py 编写 

高于上面3个app的：

operation modes.py 编写

记录用户相关的操作

app model 分层

 operation

 / | \\

courses organization users

### users models.py

自定义userprofile覆盖默认user表

EmailVerifyRecord - 邮箱验证码（比较独立的功能只和users有关系)

PageBanner - 首页轮播图

### courses models.py

课程 Course - 课程基本信息

章节 Lesson - 章节信息

视频资源 Video - 视频

课程资源 CourseResource - 课程资源

### organization models.py

CourseOrg - 课程机构基本信息

Teacher - 教师基本信息

CityDict - 城市信息

### operation modes.py

UserAsk - 用户咨询

CourseComments - 用户评论

UserFavorite - 用户收藏

UserMessage - 用户消息

UserCourse - 用户学习的课程

