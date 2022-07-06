from django.db import models

from django.db import models




class  Article(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    subtitle = models.CharField(max_length=300 ,null=True, blank=True)
    subtitle2 = models.CharField(max_length=300, null=True, blank=True)
    subtitle3 = models.CharField(max_length=300, null=True, blank=True)
    subtitle4 = models.CharField(max_length=300, null=True, blank=True)
    subtitle5 = models.CharField(max_length=300 ,null=True, blank=True)
    subtitle6 = models.CharField(max_length=300, null=True, blank=True)
    text2=models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField()
    text1=models.TextField(max_length=1000, null=True, blank=True)
    text2=models.TextField(max_length=1000, null=True, blank=True)
    text3=models.TextField(max_length=1000, null=True, blank=True)
    text4=models.TextField(max_length=1000, null=True, blank=True)
    text4=models.TextField(max_length=1000, null=True, blank=True)
    text5=models.TextField(max_length=1000, null=True, blank=True)
    text6=models.TextField(max_length=1000, null=True, blank=True)
    text7=models.TextField(max_length=1000,null=True, blank=True)
    text8=models.TextField(max_length=1000,null=True, blank=True)
    text9=models.TextField(max_length=1000,null=True, blank=True)
    text10=models.TextField(max_length=1000,null=True, blank=True)
    text11=models.TextField(max_length=1000, null=True, blank=True)
    text12=models.TextField(max_length=1000,null=True, blank=True)
    text13=models.TextField(max_length=1000,null=True, blank=True)
    text14=models.TextField(max_length=1000,null=True, blank=True)
    text15=models.TextField(max_length=1000,null=True, blank=True)
    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



class Product(models.Model):
    name = models.CharField(max_length=300)
    # articles2 = models.ManyToManyField(Article, related_name='articles',null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    price = models.FloatField()
    articles=models.ManyToManyField(Article, related_name='articles',blank=True)
    link= models.CharField(max_length=300)
    discription=models.TextField(max_length=2000)
    def __str__(self):
      return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})