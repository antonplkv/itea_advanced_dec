from threading import Thread
import time

def testing_threads(time_to_sleep):
    time.sleep(time_to_sleep)
    print('Func called')


#sync ouptut
# start = time.time()
# for i in range(20):
#     testing_threads()


thread_list = []
start = time.time()
for i in range(20):
    t = Thread(target=testing_threads, name=f'MyThread-{i}', daemon=True)
    thread_list.append(t)



t = Thread(target=testing_threads, daemon=False, args=(10, ), kwargs={})
t.start()

print('I AM THE MAIN THREAD')

