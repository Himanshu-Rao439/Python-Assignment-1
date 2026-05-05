class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self,value):
        self.queue.append(value)
        print(f"{value} enqueued. Queue{self.queue}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty, can not dequeue")
        else:
            removed = self.queue.pop(0)
            print(f"{removed} dequeued. Queue {self.queue}")
    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print(f"Front Element: {self.queue[0]}")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
# q.is_empty()
# q.peek()
# q.dequeue()  again and again delete enqueue value.