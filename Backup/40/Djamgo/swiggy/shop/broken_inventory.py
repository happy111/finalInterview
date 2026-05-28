from .models import Product

class BrokenInventoryManager:
    def purchase_product(self, product_id):
        product = Product.objects.get(id=product_id)  # No locking!
        if product.stock > 0:
            product.stock -= 1
            product.save()
            return f"✅ Purchase successful! Remaining stock: {product.stock}"
        else:
            return "❌ Out of stock!"
