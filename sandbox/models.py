from django.db import models

# Create your models here.
class Sandbox(models.Model):
    """ サンドボックス """
    name = models.CharField(max_length=20)
    #文字列項目 必須（指定がない場合は必須項目）
    text = models.CharField(max_length=10)    
    #文字列項目 空欄OK（DB上は null 不許可 ）
    txblank = models.CharField(max_length=10,blank=True)
    #文字列項目 NULLOK (DB上も null 許可)
    txnull = models.CharField(max_length=10,null=True)
    
    TEST_CHOICES = [
        ("JP","JAPAN"),
        ("US","AMERICA"),
        ("UK","UNITED KINGDOM")
    ]
    #フォームで表示する場合デフォルトがセレクトボックス
    choice = models.CharField(max_length=10, choices=TEST_CHOICES,null=True)