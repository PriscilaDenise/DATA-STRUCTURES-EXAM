# Qestion 2

class StudentQueue:
    def __init__(self): #Constructor of our class
        self.student = []   #Creating empty list 
        self.size = 0       #Initialising size of the queue as 0
        
    def enqueue_students(self, student):
        self.student.append(student)
        self.size+=1    # Increamenting queue size when a student is added

    def dequeue_students(self):
        if self.is_queue_empty():
            raise Exception("Students' queue is empty")     # Raising error when the queue is empty
        elif self.size == 0:
            raise Exception("Students' queue is empty")     # Raising error when the queue size is 1
        else:
            self.student.pop(-1)  # Removing the first student, FIFO
            self.size-=1
    
    def is_queue_empty(self):   
        if self.student is None:
            return True
    
    def current_size(self):
        return f'There are {self.size} students in the queue'


if __name__=='__main__':
    student_queue = StudentQueue() #Instantiating the class StudentQueue

    # Demonstration on how the students will join the queue:
    student_queue.enqueue_students('Denise')
    student_queue.enqueue_students('Priscila')
    student_queue.enqueue_students('Harriet')
    student_queue.enqueue_students('Muwanguzi')

    # Demonstrating how students get served
    student_queue.dequeue_students()
    student_queue.dequeue_students()
    # student_queue.dequeue_students()
    
    # Demonstrating how to assertain the size of the queue
    print(student_queue.current_size())




        
    


        