from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from photoManage.models import Pathtree, PhotoInfoManage, PhotoInfo
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def showlist(request):
    print("------showlist")
    return render(request, 'photoManage/showlist.html')

# 接受数据查询图片信息
def showlistDetail(request):
    nodeid = request.GET.get("pid")
    # 根据当前节点ID获取下一级子节点列表对象
    treeObj = Pathtree.objects.get(id=nodeid).pathtree_set.filter(is_delete='0').values_list('id')#获取当前节点的所有子节点ID
    treeObjIdList = list(treeObj)#元组转list，上句不用values()--其转化为字典类型，操作难转list
    treeObjIdList.append(nodeid)#添加当前节点ID

    photoObjLists = PhotoInfo.phObj.filter(photopath__in = treeObjIdList).order_by("id")#查询所有符合条件的图片记录
    paginator = Paginator(photoObjLists,4)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        photoObjList = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        photoObjList = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        photoObjList = current_page.object_list



    # 获取当前节点的父节点ID
    parentnode = Pathtree.objects.get(id=nodeid)  # 当前节点ID
    parentnodeid = str(parentnode.superpath_id)

    # 返回父节点ID和列表数据
    return render(request, 'photoManage/showlist.html', {'data': parentnodeid,'currentnodeid':nodeid, 'photoinfolists': photoObjList,"page":current_page})


def jstreeDetail(request):
    # 使用ORM
    # all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
    # data = models.Pathtree.objects.values('id', 'tname', 'superpath', 'is_button')
    # json_data = toJSON(models.Pathtree.objects.all())

    queryset = Pathtree.objects.filter(is_delete=0).values('pk', 'tname', 'superpath', 'is_button')
    serialized_q = json.dumps(list(queryset), cls=DjangoJSONEncoder)

    return JsonResponse(serialized_q, safe=False)


def initSave(request):
    return  render(request, 'photoManage/initSave.html')

def savePhotoInfo(request):
    pass

def initModify(request):
    pass

def modifyPhotoinfo(request):
    pass

def delPhotoinfo(request):
    pass