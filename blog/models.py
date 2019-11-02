from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


# models.Model을 상속받았다 > 이 모델이 데이터베이스의 테이블이 된다.
class Post(models.Model):
    # 다른 테이블 연결 시킬 때 ForeignKey를 쓰는데 이 뒤에 settings.AUTH_USER_MODEL은 뭔지 모르겠는데
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    QuerySet

    # 인스턴스 메서드
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 얘는 왜 인자가 있는거여
    @classmethod
    def publish2(clscls):
        pass

    # 첫 번째 인자가 없다? 내가 아는 staticmethod 인가?git
    @staticmethod
    def publish3():
        pass

    # Description 매직메서드라고 부른대요 :)
    def __str__(self):
        return self.title