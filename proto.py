import numpy as np
import readline
from collections import defaultdict

def cosine_similarity(vec1, vec2):
	return np.dot(vec1, vec2)

def str2vec(input, unique_flavours):
	vector = np.zeros(len(unique_flavours)).astype(np.float32)
	for flav in unique_flavours:
		if flav in input:
		    vector[unique_flavours.index(flav)] += 1.0
	return vector / np.linalg.norm(vector)

def word2vec(words, unique_flavours):
	vector = np.zeros(len(unique_flavours)).astype(np.float32)
	for i in words:
		idx = unique_flavours.index(i)
		vector[idx] += 1.0
	return vector / np.linalg.norm(vector)

input_path = "training_sets/mission_hill.csv"
print "Loading model:", input_path
data = defaultdict(list)
flavours = []
with open(input_path) as file:
	
	for line in file:
		split_line = line.split(",")
		flavour = split_line[0].strip()
		wine = split_line[1].strip()
		data[wine].append(flavour)
		flavours.append(flavour)

unique_flavours = list(set(flavours))

vecs = dict()

for key in data.keys():
	vecs[key] = word2vec(data[key], unique_flavours)

print "Model loaded."


while True:
	input = raw_input("Enter a dish:")

	if input is "quit":
		break

	input = input.lower()
	print "for input:", input
	input_vec = str2vec(input, unique_flavours)
	scores = dict()
	total = 0
	for key in vecs.keys():
		scores[key] = cosine_similarity(vecs[key], input_vec)
		total+=scores[key]

	for key, value in reversed(sorted(scores.iteritems(), key=lambda (k,v): (v,k))):
		print "%s: %%%s" % (key, int(value * 100/total))