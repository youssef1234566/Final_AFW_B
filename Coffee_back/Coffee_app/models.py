from django.db import models

class User(models.Model):
    
    User_Email = models.CharField(max_length=250)
    User_Name = models.CharField(max_length = 300)
    User_Password = models.CharField(max_length=250)
    User_Details = models.CharField(max_length=1000)
    User_Orders = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return f"User Email: {self.User_Email} --- Orders: {self.User_Orders}"
    
    
class Product(models.Model):
    
    Product_Name = models.CharField(max_length=250)
    Product_Price = models.FloatField(null=True, blank=True)
    Product_Image = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return f"{self.Product_Name } {self.Product_Price}"
    
class Order(models.Model):
    
    Order_Details = models.CharField(max_length=1000)
    Order_Status = models.CharField(max_length=250)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Order_Shipping_Status = models.CharField(max_length = 250)
    
    def __str__(self) -> str:
        return f"{self.pk} {self.Order_Details}"
    
    