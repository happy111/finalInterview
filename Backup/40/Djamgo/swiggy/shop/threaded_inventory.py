from .models import Product

# class ThreadedInventoryManager:
#     def purchase_product(self, product_id):
#         product = Product.objects.get(id=product_id)  # No locking or transaction
#         if product.stock > 0:
#             product.stock -= 1
#             product.save()
#             return f"✅ Purchase successful! New stock: {product.stock}"
#         else:
#             return "❌ Out of stock!"


#
import threading
from .models import Product
from django.db import transaction

lock = threading.Lock()  # shared lock

class ThreadSafeInventoryManager:
    def purchase_product(self, product_id):
        with lock:
            try:
                product = Product.objects.get(id=product_id)
                if product.stock > 0:
                    product.stock -= 1
                    product.save()
                    return f"✅ Purchase successful! New stock: {product.stock}"
                else:
                    return "❌ Out of stock!"
            except Product.DoesNotExist:
                return "❌ Product not found!"
