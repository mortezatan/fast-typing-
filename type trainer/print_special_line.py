#from speed import Time
import time

class Word:    
    def print_special_line(self):
        """print special line of a file."""
        import random
        self.source = open("/home/morteza/pythonprojects/type_training/type trainer/realwords","r")
        self.line = random.randint(1,1962)
        self.x = str(self.line)
        self.y = self.x + "_"
        for self.line in self.source:
            if self.line.startswith(self.y):
                self.line_text = self.line
                #print(self.line_text.rstrip())

        """print only word of the special line."""
        self.start = self.line_text.index("_")
        self.end = self.line_text.index("\n")
        sys_word = self.line_text[self.start+1:self.end]
        return sys_word
        
        #print(sys_word)
        #print(start,end)



    
start_t  = float
end_t = float
    
def start(start_t):
    start_t = time.time()
    return start_t
    
def end(end_t):
    end_t = time.time()
    return end_t
    
    

an = Word()
sytem_word = an.print_special_line()
print(sytem_word)
hot_2 = start(start_t)
uesr_word = input("your word? ")
sys_word = sytem_word

class Dictation_check:
    
    text = "YOU HAVE {} ERRORS!"
    
    def check_er(self,uesr_word,sys_word):
        """if word enterd has same length, check how many incorrect letters are there."""
        if uesr_word == sys_word:
            print("good")
        elif uesr_word != sys_word:
            self.count = 0
            self.x = {}
            for v in sys_word:
                self.count += 1
                self.x[str(self.count)] = v
            self.lentgh = len(self.x) 
            self.count = 0
            for c in uesr_word:
                self.count += 1
                self.old = self.x[str(self.count)]
                self.new = self.old + c
                self.x.update({str(self.count):self.new})

            #print(x)



            false = 0
            for dic in self.x:
                #print(x[dic])
                self.check = self.x[dic]
                if len(self.check) == 2:
                    if self.check[0] != self.check[1]:
                        false += 1
                else:
                    false += 1
            
            print(self.text.format(false))


    def len_compare(self,uesr_word,sys_word):
        """check if words' length is equal or not."""
        self.w = len(uesr_word)
        self.q = len(sys_word)
        self.e = abs(self.w-self.q)
        if self.e == 0:
            self.check_er(uesr_word,sys_word)
        else:
            self.false = self.e
            print(self.text.format(self.false))


ah = Dictation_check()
ah.len_compare(uesr_word,sys_word)
hot_3 = end(end_t)
#print(hot_3,hot_2)

def time_convert(hot_3,hot_2):
        
    text_2 = "your time is" 
    time_lapsed = hot_3 - hot_2
    #minute = time_lapsed // 60
    second = time_lapsed % 60
    decimals = float(second)
    print(text_2,'{0:.3f}'.format(second))

hot_4 = time_convert(hot_3,hot_2)
