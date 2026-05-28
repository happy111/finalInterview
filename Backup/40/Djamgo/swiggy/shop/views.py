from django.http import JsonResponse
import threading
from .threaded_inventory import ThreadSafeInventoryManager

manager = ThreadSafeInventoryManager()

def threaded_purchase_view(request, product_id):
    responses = []
    threads = []

    def make_purchase():
        result = manager.purchase_product(product_id)
        responses.append(result)

    # Simulate 5 users buying at the same time
    for _ in range(5):
        t = threading.Thread(target=make_purchase)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return JsonResponse({'results': responses})
