from classes.BoxQueue import BoxQueue

class TestBoxQueue:
    def test_boxqueue_enqueue(self):
        bq = BoxQueue()
        bq.enqueue(1)
        assert(bq.size() == 1)

    def test_boxqueue_dequeue(self):
        bq = BoxQueue()
        bq.enqueue(1)
        bq.dequeue()
        assert(bq.size() == 0)

    def test_boxqueue_dequeue(self):
        bq = BoxQueue()
        assert(bq.is_empty() == True)
    