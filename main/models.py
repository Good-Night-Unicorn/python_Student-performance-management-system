#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class jiaoshi(BaseModel):
    __doc__ = u'''jiaoshi'''
    __tablename__ = 'jiaoshi'

    __loginUser__='gonghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='gonghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    gonghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='工号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年龄' )
    zhicheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职称' )
    dianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    gonghao=VARCHAR
    mima=VARCHAR
    jiaoshixingming=VARCHAR
    xingbie=VARCHAR
    nianling=VARCHAR
    zhicheng=VARCHAR
    dianhua=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'jiaoshi'
        verbose_name = verbose_name_plural = '教师'
class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='xuehao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='xuehao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xuehao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='学号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    zhuanye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    xuehao=VARCHAR
    mima=VARCHAR
    xueshengxingming=VARCHAR
    xingbie=VARCHAR
    banji=VARCHAR
    zhuanye=VARCHAR
    shouji=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
class gonggaoxinxi(BaseModel):
    __doc__ = u'''gonggaoxinxi'''
    __tablename__ = 'gonggaoxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    biaoti=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    leixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='类型' )
    gonggaoneirong=models.TextField   (  null=True, unique=False, verbose_name='公告内容' )
    fabushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发布时间' )
    '''
    biaoti=VARCHAR
    leixing=VARCHAR
    gonggaoneirong=Text
    fabushijian=DateTime
    '''
    class Meta:
        db_table = 'gonggaoxinxi'
        verbose_name = verbose_name_plural = '公告信息'
class kechengleixing(BaseModel):
    __doc__ = u'''kechengleixing'''
    __tablename__ = 'kechengleixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='课程类型' )
    '''
    kechengleixing=VARCHAR
    '''
    class Meta:
        db_table = 'kechengleixing'
        verbose_name = verbose_name_plural = '课程类型'
class kechengxinxi(BaseModel):
    __doc__ = u'''kechengxinxi'''
    __tablename__ = 'kechengxinxi'



    __authTables__={'gonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='课程名称' )
    kechengleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='课程类型' )
    kaikeriqi=models.DateField   ( null=False, unique=False, verbose_name='开课日期' )
    shangkedidian=models.CharField ( max_length=255,null=False, unique=False, verbose_name='上课地点' )
    kechengjieshao=models.TextField   (  null=True, unique=False, verbose_name='课程介绍' )
    gonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    '''
    kechengmingcheng=VARCHAR
    kechengleixing=VARCHAR
    kaikeriqi=Date
    shangkedidian=VARCHAR
    kechengjieshao=Text
    gonghao=VARCHAR
    jiaoshixingming=VARCHAR
    '''
    class Meta:
        db_table = 'kechengxinxi'
        verbose_name = verbose_name_plural = '课程信息'
class xuankexinxi(BaseModel):
    __doc__ = u'''xuankexinxi'''
    __tablename__ = 'xuankexinxi'



    __authTables__={'gonghao':'jiaoshi','xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    kechengleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程类型' )
    kaikeriqi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='开课日期' )
    gonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    xuankeshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='选课时间' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    zhuanye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    kechengmingcheng=VARCHAR
    kechengleixing=VARCHAR
    kaikeriqi=VARCHAR
    gonghao=VARCHAR
    jiaoshixingming=VARCHAR
    xuankeshijian=DateTime
    xuehao=VARCHAR
    xueshengxingming=VARCHAR
    zhuanye=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'xuankexinxi'
        verbose_name = verbose_name_plural = '选课信息'
class chengjixinxi(BaseModel):
    __doc__ = u'''chengjixinxi'''
    __tablename__ = 'chengjixinxi'



    __authTables__={'xuehao':'xuesheng','gonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='课程名称' )
    xuehao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    chengji=models.CharField ( max_length=255,null=False, unique=False, verbose_name='成绩' )
    fabushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发布时间' )
    gonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    '''
    kechengmingcheng=VARCHAR
    xuehao=VARCHAR
    xueshengxingming=VARCHAR
    chengji=VARCHAR
    fabushijian=DateTime
    gonghao=VARCHAR
    jiaoshixingming=VARCHAR
    '''
    class Meta:
        db_table = 'chengjixinxi'
        verbose_name = verbose_name_plural = '成绩信息'
