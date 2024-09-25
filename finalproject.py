#
# finalproject.py (Final Project)
#
# Text Analyzing 
#  

### Problem worked on with Maria Diaz Garrido, BUID: U37110909

import math

def clean_text(txt):
    """ takes a string of text txt as a parameter and returns a list 
    containing the words in txt after it has been “cleaned"""
    s=[]
    txt=txt.lower().split(' ')
    for words in txt:
        words=words.replace('.', '')
        words=words.replace(',', '')
        words=words.replace('?', '')
        words=words.replace('"', '')
        words=words.replace("'", '')
        words=words.replace("!", '')
        words=words.replace(";", '')
        words=words.replace(":", '')
        s+=[words]
    return s
                       
def stem(s):
    """ the function should then return the stem of s
    """    
    if s[-3:] == 'ing':
            s = s[:-3]
        
    elif s[-2:] == 'er':
        s = s[:-2]
        
    elif s[-1:] == 's':
        s = s[:-1]
        
    elif s[:3] == 'lov':
        s = s[:3]
            
    elif s[:5] == 'extra':
        s = s[:5]
    
    elif s[:2] == 'un':
        s = s[:2]
        
    elif s[:2] == 're':
        s = s[:2]
        
    return s

def compare_dictionaries(d1, d2):
    """take two feature dictionaries d1 and d2 as inputs, 
    and it should compute and return their log similarity 
    score – using the procedure described above"""
    if d1 == {}:
        return -50
    
    score=0
    total=0
    for key in d1:
        total+=d1[key]
        
        
    for key in d2:
        if key in d1:
            score+=(d2[key])*math.log((d1[key]/total))
            
        else:
            score+=(d2[key])*math.log((0.5/total))
            
    return score
            
    

                       
class TextModel:
    """blueprint for objects that model a body of text"""
    
    def __init__(self,model_name):
        """constructs a new TextModel object by accepting a string model_name 
        as a parameter and initializing the following three attributes"""
        self.name=model_name
        self.words={}
        self.word_lengths={}
        self.stems={}
        self.sentence_lengths={}
        self.punctuations={}
        
    def __repr__(self):
        """returns a string that includes the name of the model 
        as well as the sizes of the dictionaries for each feature of the text"""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuations)) + '\n'
        return s
        
    def add_string(self, s):
        """ adds a string of text s to the model by augmenting the feature 
        dictionaries defined in the constructor"""
        words=s.lower().split(' ')
        c1=0
        for w in words:
            c1+=1
            if '.' in w:
                if c1 not in self.sentence_lengths:
                    self.sentence_lengths[c1]=1
                    c1=0
                    
                else:
                    self.sentence_lengths[c1]+=1
                    c1=0
                    
            elif '!' in w:
                if c1 not in self.sentence_lengths:
                    self.sentence_lengths[c1]=1
                    c1=0
                    
                else:
                    self.sentence_lengths[c1]+=1
                    c1=0
                    
            elif '?' in w:
                if c1 not in self.sentence_lengths:
                    self.sentence_lengths[c1]=1
                    c1=0
                    
                else:
                    self.sentence_lengths[c1]+=1
                    c1=0
                    
        for w in words:
            if '.' in w:
                if '.' not in self.punctuations:
                    self.punctuations['.']=1
                    
                    
                else:
                    self.punctuations['.']+=1
                    
            elif ',' in w:
                if ',' not in self.punctuations:
                    self.punctuations[',']=1
                    
                    
                else:
                    self.punctuations[',']+=1
                    
            elif '!' in w:
                if '!' not in self.punctuations:
                    self.punctuations['!']=1
                    
                    
                else:
                    self.punctuations['!']+=1
                    
            elif '?' in w:
                if '?' not in self.punctuations:
                    self.punctuations['?']=1
                    
                    
                else:
                    self.punctuations['?']+=1
                    
            elif ':' in w:
                if ':' not in self.punctuations:
                    self.punctuations[':']=1
                    
                    
                else:
                    self.punctuations[':']+=1
                    
            elif ';' in w:
                if ';' not in self.punctuations:
                    self.punctuations[';']=1
                    
                    
                else:
                    self.punctuations[';']+=1
                    
           
        word_list = clean_text(s)
        for w in word_list:
            a=len(w)
            if w not in self.words and a not in self.word_lengths:
                self.words[w]=1
                self.word_lengths[a]=1
            elif w not in self.words and a in self.word_lengths:
                self.words[w]=1
                self.word_lengths[a]+=1
                
            elif w in self.words and a not in self.word_lengths:
                self.words[w]+=1
                self.word_lengths[a]=1
                
            else:
                self.words[w]+=1
                self.word_lengths[a]+=1
                
        
        for w in word_list:
            a=stem(w)
            if a not in self.stems:
                self.stems[a]=1
                
            else:
                self.stems[a]+=1
    
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        x = f.read()
        self.add_string(x)
        
        
        
    def save_model(self):
        """A function that demonstrates how to write a
        Python dictionary to an easily-readable file."""
        d=self.words
        a=(self.name+'_'+'words')
        f=open(a, 'w')      
        f.write(str(d))              
        f.close()
        
        d1=self.word_lengths
        b=(self.name+'_'+'word_lengths')
        d=open(b,'w')
        d.write(str(d1))
        d.close()   
        
        e1=self.stems
        b=(self.name+'_'+'stems')
        d=open(b,'w')
        d.write(str(e1))
        d.close()
        
        f1=self.sentence_lengths
        b=(self.name+'_'+'sentence_lengths')
        d=open(b,'w')
        d.write(str(f1))
        d.close()
        
        g1=self.punctuations
        b=(self.name+'_'+'punctuations')
        d=open(b,'w')
        d.write(str(g1))
        d.close()
           
    

    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object from 
        their files and assigns them to the attributes of the called TextModel"""
        
        a1=(self.name + '_' + 'word_lengths')
        f = open(a1, 'r')
        d_str = f.read()           
        f.close()
        self.word_lengths= dict(eval(d_str))
        
        b1=(self.name + '_' + 'words')
        d = open(b1, 'r')
        b_str = d.read()           
        d.close()
        self.words= dict(eval(b_str))
        
        c1=(self.name+'_'+'stems')
        d = open(c1, 'r')
        b_str = d.read()           
        d.close()
        self.stems= dict(eval(b_str))
        
        d1=(self.name+'_'+'sentence_lengths')
        d = open(d1, 'r')
        b_str = d.read()           
        d.close()
        self.sentence_lengths= dict(eval(b_str))
        
        e1=(self.name+'_'+'punctuations')
        d = open(e1, 'r')
        b_str = d.read()           
        d.close()
        self.punctuations= dict(eval(b_str))
        
        
    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores 
        measuring the similarity of self and other – one score for each type of feature"""
        scores=[]
        scores+=[compare_dictionaries(other.words, self.words)]
        scores+=[compare_dictionaries(other.word_lengths, self.word_lengths)]
        scores+=[compare_dictionaries(other.stems, self.stems)]
        scores+=[compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        scores+=[compare_dictionaries(other.punctuations, self.punctuations)]
        return scores
    
    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other “source” TextModel 
        objects (source1 and source2) and determines which of these other TextModels 
        is the more likely source of the called TextModel"""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + str(scores1))
        print('scores for ' + source2.name + str(scores2))
        
        s1=0
        s2=0
        for i in range(len(scores1)):
            if scores1[i]>scores2[i]:
                s1+=1
                
            elif scores1[i]<scores2[i]:
                s2+=1
                
        if s1>s2:
            print(self.name + ' is more likely to have come from ' + source1.name)
            
        else:
            print(self.name + ' is more likely to have come from ' + source2.name)
            
    
def run_tests():
    """ your docstring goes here """
    source1 = TextModel('HIMYM')
    source1.add_file('himym.txt')

    source2 = TextModel('MODERN FAMILY')
    source2.add_file('modernfamily.txt')

    new1 = TextModel('the g')
    new1.add_file('thegoldbergs.txt')
    new1.classify(source1, source2)


            
  
        



