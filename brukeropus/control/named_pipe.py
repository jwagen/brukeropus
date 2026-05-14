

class NamedPipeClient:
    def __init__(self, pipe_name=r"\\.\pipe\OPUS"):
        # Retry opening. Mostly usefull for unittesting with rapid open close
        for _ in range(10):
            try:
                self.pipe = open(pipe_name, "r+b", 0)
                break
            except OSError:
                import time
                time.sleep(0.1)

    def disconnect(self):
        self.pipe.close()

    def request(self, item, timeout=5000):
        self.pipe.write(f"{item}\r\n".encode())
        #self.pipe.flush()
        # TODO: Use windows api for reading pipes with timeout
        data = self.pipe.read(1000)
        return data