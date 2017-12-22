import math
from collections import namedtuple

Frequency = namedtuple("Frequency", ["Value", "Occurance"]);

def AFrequency(data,val):
    return Frequency(Value=val,Occurance=data.count(val));

def SomeFrequencies(data,vals):
    freq = [];
    for i in range(len(vals)):
        count = 0;
        freq.append(AFrequency(data,vals[i]))
    return freq;

def AllFrequencies(data):
    freq = [];
    done = [];
    for i in range(len(data)):
        current = data[i];
        if not(current in done):
            done.append(current);
            freq.append(AFrequency(data,current));
    return freq;

def Mean(data):
    total = 0;
    for val in data:
        total += val;
    return total/len(data);

def MeanFromFrequency(data):
    total = 0;
    for val in data:
        total += val;
    return total/len(data);

def StandardDeviation(data):
    mean = Mean(data);
    deviation = [(val - mean)**2 for val in data];
    variance = math.sqrt(Mean(deviation));
    return variance;

def BasselSD(data):
    total = 0;
    for val in data:
        total += val;
    mean = total/len(data)-1;
    deviation = [(val - mean)**2 for val in data];
    variance = math.sqrt(Mean(deviation));
    return variance;

def MeanAbsoluteDeviation(data):
    mean = Mean(data);
    deviation = [abs((val - mean)) for val in data];
    return Mean(deviation);

def Median(data):
    med = [val for val in data];
    med.sort();
    if even(len(med)):
        one = len(med)/2;
        two = one + 1;
        return (med[one] + med[two])//2;
    else:
        return med[len(med)//2];

def even(number):
    return abs(number % 2) == 0;

def MedianAbsoluteDeviation(data):
    medain = Median(data);
    deviation = [abs((val - medain)) for val in data];
    return Median(deviation);

def Mode(data):
    freq = AllFrequencies(data);
    mode = freq[0];
    for val in freq:
        if(mode.Occurance < val.Occurance):
            mode = val;
    return mode.Value;

def Range(data):
    higest = data[0];
    lowest = data[0];
    for val in data:
        if(higest < val):
            higest = val;
        if(lowest > val):
            lowest = val;
    return higest - lowest;
