from django.db import models

# Create your models here.

# 树型表
class Pathtree(models.Model):
    tname       = models.CharField(max_length=200)
    # 外键 自引用外键
    superpath   = models.ForeignKey('self',on_delete=models.CASCADE,)
    is_button = models.CharField(max_length=1)
    #表通用信息
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    modify_time = models.DateTimeField(auto_now=True)
    modify_user = models.CharField(max_length=20)
    is_delete   = models.CharField(max_length=1)

    def __str__(self):
        return self.tname
    class Meta:
        #定义数据表名
        db_table = "path_tree"





class PhotoInfoManage(models.Manager):
    def get_queryset(self):
        return super(PhotoInfoManage,self).get_queryset().filter(is_delete = '0')
    def createPhotoInfo(self,name,photop,contend,createT,createU,
                      modifyT,modifyU,isD='1'):
        photoInfo             = self.model()
        photoInfo.pname       = name
        photoInfo.photopath   = photop
        photoInfo.pcontend    = contend
        photoInfo.create_time = createT
        photoInfo.create_user = createU
        photoInfo.modify_time = modifyT
        photoInfo.modify_user = modifyU
        # photoInfo.is_delete   = isD
        return photoInfo

#图片信息表
class PhotoInfo(models.Model):
    pname       = models.CharField(max_length=200)
    photopath   = models.ForeignKey("Pathtree", on_delete=models.CASCADE,)
    pcontend    = models.TextField()
    #表通用信息
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    modify_time = models.DateTimeField(auto_now=True)
    modify_user = models.CharField(max_length=20)
    is_delete   = models.CharField(max_length=1)

    def __str__(self):
        return self.pname

    class Meta:
        #定义数据表名
        db_table = "photo_info"
        # 对象得默认排序字段，获取对象的列表时
        # ordering = ['id']  # 升序，-id降序,排序增加数据库的开销

        # 自定义模型管理器
        # 当自定义模型管理器，objects就不存在了---type object 'PhotoInfo' has no attribute 'objects'
    phObj = PhotoInfoManage()

    #定义一个类方法创建对象
    @classmethod
    # cls代表PhotoInfo自身
    def createPhotoInfo(cls,name,photop,contend,createT,createU,
                      modifyT,modifyU,isD='1'):
        photoInfo = cls(pname=name,photopath=photop,pcontend=contend,
                        create_time=createT,create_user=createU,modify_time=modifyT,
                        modify_user=modifyU,is_delete=isD)
        return photoInfo

#图片信息表
class PhotoDetail(models.Model):

    photoDInfo  = models.ForeignKey("PhotoInfo",on_delete=models.CASCADE,)
    image       = models.ImageField()
    imageInfo   = models.CharField(max_length=200)

    #表通用信息
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=20)
    modify_time = models.DateTimeField(auto_now=True)
    modify_user = models.CharField(max_length=20)
    is_delete   = models.CharField(max_length=1)


    class Meta:
        #定义数据表名
        db_table = "photo_detail"



from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pathtree):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


