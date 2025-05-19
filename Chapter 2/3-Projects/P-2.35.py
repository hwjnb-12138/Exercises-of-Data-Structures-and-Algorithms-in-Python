# Write a set of Python classes that can simulate an Internet application in
#  which one party, Alice, is periodically creating a set of packets that she
#  wants to send to Bob. An Internet process is continually checking if Alice
#  has any packets to send, and if so, it delivers them to Bob’s computer, and
#  Bob is periodically checking if his computer has a packet from Alice, and,
#  if so, he reads and deletes it.
from queue import Queue
import time
import threading


class Packet:

    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.timestamp = time.time()


class Alice:

    def __init__(self):
        self.packet_queue = Queue()
        self._counter = 0
        self._running = True

    def create_packet(self, interval=5):
        while self._running:
            self._counter += 1
            packet = Packet(self._counter, f"Message {self._counter}")
            self.packet_queue.put(packet)
            time.sleep(interval)

    def stop(self):
        self._running = False


class Bob:

    def __init__(self):
        self.receive = Queue()

    def packet_manage(self, interval=5):
        while True:
            if not self.receive.empty():
                packet = self.receive.get()
                print(packet.id, packet.message)
            time.sleep(interval)


class Internet:

    def __init__(self, alice, bob):
        self._alice = alice
        self._bob = bob
        self._running = True

    def send_packet(self):
        while self._running:
            if not self._alice.packet_queue.empty():
                packet = self._alice.packet_queue.get()
                self._bob.receive.put(packet)

    def stop(self):
        self._running = False


if __name__ == "__main__":
    # 初始化系统组件
    alice = Alice()
    bob = Bob()
    internet = Internet(alice, bob)

    # 创建并启动线程
    alice_thread = threading.Thread(target=alice.generate_packet, daemon=True)
    internet_thread = threading.Thread(target=internet.deliver_packets, daemon=True)
    bob_thread = threading.Thread(target=bob.process_packets, daemon=True)

    alice_thread.start()
    internet_thread.start()
    bob_thread.start()

    try:
        # 主线程保持运行
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping system...")
        alice.stop()
        internet.stop()
