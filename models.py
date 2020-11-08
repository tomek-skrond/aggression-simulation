import numpy as np
from numpy.random import *
import random
import pprint

pp = pprint.PrettyPrinter(indent=1)

class Sample:
	def __init__(self,hostility,repr_rate,is_alive):
		self.hostility = hostility
		self.repr_rate = repr_rate
		self.is_alive = is_alive


class Simulation:
	def __init__(self,num_of_samples,hostility_factor,nutrition_units=150):
		self.num_of_samples_conf = randint(0,num_of_samples+1)
		self.num_of_samples_single = num_of_samples - self.num_of_samples_conf
		self.samples = self.generateSamples(self.num_of_samples_conf,self.num_of_samples_single,hostility_factor)
		#print(pp.pprint(self.samples))
		self.batches = self.generateBatches(self.samples)
		print(pp.pprint(self.batches))


	def generateSamples(self,num_of_samples_confronting,num_of_samples_single,hostility_factor):

		samples_array = []

		if hostility_factor > num_of_samples_confronting:
			hostility_factor = num_of_samples_confronting

		num_of_samples = num_of_samples_confronting + num_of_samples_single
		hostile_samples_num = hostility_factor
		friendly_samples_num = num_of_samples - hostile_samples_num - num_of_samples_single

		hostile_sample = Sample(1,1,1)
		friendly_sample = Sample(0,1,1)

		print(num_of_samples,num_of_samples_single,num_of_samples_confronting,sep=" ")

		for hostile in range(hostile_samples_num):
			samples_array.append(hostile_sample)

		for friendly in range(hostile_samples_num):
			samples_array.append(friendly_sample)
		
		for neutral in range(num_of_samples_single):
			neutral_sample = Sample(randint(0,2),1,1)
			samples_array.append(neutral_sample)

		random.shuffle(samples_array)

		return samples_array

	def generateBatches(self,samples,batch_size=2):
		return [samples[i:i + batch_size] for i in range(0, len(samples), batch_size)]

	def sampleInteraction(self,batch):
		if (batch[0].hostility == 1 and batch[1].hostility == 0) or (batch[0].hostility == 0 and batch[1].hostility == 1):
			return 12			

	def populateSamples(self,batches):
		return 1

sdf = Simulation(300,2)

'''
n = 0
for i in sdf.batches:
	print(i)
	n+=1

print(n)
'''