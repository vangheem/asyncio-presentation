import asyncio
import threading


class PrintThread(threading.Thread):

    def __init__(self, id):
        self.id = id
        super().__init__(target=self)

    def __call__(self):
        self._loop = asyncio.new_event_loop()
        self._loop.run_until_complete(self._run())

    async def _run(self):
        for idx in range(3):
            await asyncio.sleep(idx)
            print('Hello {} from thread {}'.format(
                idx, self.id
            ))


threads = []
for i in range(5):
    thread = PrintThread(i)
    threads.append(thread)
    thread.start()
print(f'Waiting to finish')
for thread in threads:
    thread.join()
print('done')
