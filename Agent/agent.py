import csv
import pika
import pandas as pd
from messagebroker import Broker

filename = '..\\Sample_Data\\mosvalues_small.csv'
chunk_size = 1

class Agent:
    def __init__(self):
        broker = Broker()
        self.queue = broker.init_queue("rabbitmq")

    def read_csv(self):
        for chunks in pd.read_csv(filename, chunksize = chunk_size, header=None):
            json_chunk = chunks.to_json(orient = 'records')
            self.queue.push(json_chunk)


agent = Agent()
agent.read_csv()