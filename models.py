import numpy as np
from numpy.random import *
import random
import pprint

pp = pprint.PrettyPrinter(indent=2)

class Sample:
	def __init__(self,hostility,repr_rate,is_alive):
		self.hostility = hostility
		self.repr_rate = repr_rate
		self.is_alive = is_alive


class Simulation:
	def __init__(self,num_of_samples,hostility_factor,nutrition_units=150):
		self.num_of_samples = num_of_samples
		self.num_of_samples_conf = randint(0,self.num_of_samples+1)
		self.num_of_samples_single = num_of_samples - self.num_of_samples_conf
		self.samples = self.generateSamples(self.num_of_samples_conf,self.num_of_samples_single,hostility_factor)
		#print(pp.pprint(self.samples))
		#self.batches = self.generateBatches(self.samples)
		#print(pp.pprint(self.batches))


	def generateSamples(self,num_of_samples_confronting,num_of_samples_single,hostility_factor):

		samples_array = []

		if hostility_factor > num_of_samples_confronting:
			hostility_factor = num_of_samples_confronting

		num_of_samples = num_of_samples_confronting + num_of_samples_single
		hostile_samples_num = hostility_factor
		friendly_samples_num = num_of_samples - hostile_samples_num - num_of_samples_single

		hostile_sample = Sample(1,1,1)
		friendly_sample = Sample(0,1,1)

		print(f"number of samples: {num_of_samples}  \nnumber of singular samples: {num_of_samples_single} \nnumber of paired samples: {num_of_samples_confronting}")

		for hostile in range(hostile_samples_num):
			samples_array.append(hostile_sample)

		for friendly in range(hostile_samples_num):
			samples_array.append(friendly_sample)

		random.shuffle(samples_array)

		samples_array = self.generateBatches(samples_array)

		for neutral in range(num_of_samples_single):
			neutral_sample = [Sample(randint(0,2),0,0)]
			samples_array.append(neutral_sample)

		random.shuffle(samples_array)

		pp.pprint(samples_array)

		return samples_array

	def generateBatches(self,samples,batch_size=2):
		return [samples[i:i + batch_size] for i in range(0, len(samples), batch_size)]

	def sampleInteraction(self,batch):
		first = batch[0]
		second = batch[1]
		if (first.hostility == 1 and second.hostility == 0):

			first.repr_rate = 0.5*randint(1,3)
			first.is_alive = 1

			second.repr_rate = 0
			second.is_alive = 0.5*randint(1,3)


		if (first.hostility == 0 and second.hostility == 1):

			first.repr_rate = 0.5*randint(1,3)
			first.is_alive = 1

			second.repr_rate = 0
			second.is_alive = 0.5*randint(1,3)

	def countSamples(self,samples):
		n = 0
		for i in samples:
			for j in i:
				n+=1
		return n

	def destroySample(self,samples,batch_index,sample_index,samples_num):

		#samples_num -= 1
		del samples[batch_index][sample_index]

		return samples_num-1

	def populateSamples(self,batches):
		return 1

num = 300
sdf = Simulation(3,10)

print(f"number of sample objects: {sdf.countSamples(sdf.samples)}")

new_num = sdf.destroySample(sdf.samples,0,0,sdf.num_of_samples)


pp.pprint(sdf.samples)
#pp.pprint(sdf.samples)

print(f"number of sample objects: {sdf.countSamples(sdf.samples)}")
