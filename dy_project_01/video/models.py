from pydoc import describe
from django.db import models

# Create your models here.
class VideoData(models.Model):

  """
  视频信息表
  
  """
  username=models.TextField(verbose_name='用户名',null=True,blank=True)
  fansCount=models.BigIntegerField(verbose_name='粉丝数量',null=True,blank=True)
  describe=models.TextField(verbose_name='视频描述',null=True,blank=True)
  videoId=models.TextField(verbose_name='视频id',null=True,blank=True)
  createTime=models.TextField(verbose_name='发表时间',null=True,blank=True)
  videoTime=models.TextField(verbose_name='视频时长',null=True,blank=True)
  likeCount=models.BigIntegerField(verbose_name='点赞数量',null=True,blank=True)
  collectCount=models.BigIntegerField(verbose_name='收藏数量',null=True,blank=True)
  commentCount=models.BigIntegerField(verbose_name='评论数量',null=True,blank=True)
  downloadCount=models.BigIntegerField(verbose_name='下载数量',null=True,blank=True)
  shareCount=models.BigIntegerField(verbose_name='分享数量',null=True,blank=True)
  
  class Meta:
    verbose_name='视频信息'
    db_table='video_data'


class CommentData(models.Model):
  """
  视频评论表
  
  """

  user_id=models.TextField(verbose_name='用户id',null=True,blank=True)
  user_name=models.TextField(verbose_name='用户名',null=True,blank=True)
  comment_time=models.TextField(verbose_name='评论时间',null=True,blank=True)
  ip_address=models.TextField(verbose_name='IP地址',null=True,blank=True)
  comment_content=models.TextField(verbose_name='评论内容',null=True,blank=True)
  like_count=models.BigIntegerField(verbose_name='点赞数量',null=True,blank=True)
  video_id=models.TextField(verbose_name='视频id',null=True,blank=True)
  
  class Meta:
    verbose_name='评论信息'
    db_table='video_comment'