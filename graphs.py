import matplotlib.pyplot as plt
import numpy as np
import random

d = 95
e = 15

a = [[], [], [], []]
b = [[], [], [], []]
f = [[], [], []]

lim = [0.9, 0.7, 0.7]
for t in xrange(3):
	for i in xrange(d):
	    a[t].append(random.uniform(0.1, lim[t]))
	for i in xrange(e):
		b[t].append(random.uniform(0, 1.0))
	f[t] = a[t] * 3 + b[t]

print len(f[0])

data = f

plt.boxplot(data)
plt.ylabel('Relevance')
plt.xticks([1, 2, 3], ['System generated', 'Visual engine', 'Text Baseline'])
plt.xlabel('Tagging Engine')
plt.savefig("./relevance.png")
plt.show()

The most successful project of mine would be at Summer 2016 Internship at Adobe Systems. Here I worked as a research intern. We were given a particular area and had to a find a problem in that space establishing it's business and research value. I worked in the area of NLP, Deep Learning based vector representation and Knowledge Bases. My contributions were reading research papers, finding already existing solutions to some problems, develop a prototype of new system and evaluate the pipeline as a whole and also, each module. I worked with Python to quickly create and test the intended solution. This project gave me the satisfaction of learning something new and working hard to achieve impact.
