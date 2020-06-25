#Q3)From an alphanumeric phone number, display phone no. ph = 'abc99ef67d8992'
#output: 99678992df ->since it has only 8 no's, put the characters at the last 2 positions of ph
#(which are d and f here)to make it 10 digit
def phone(ph):
    s1=''
    for i in ph:
        p=i.isnumeric()
        if p==True:
            s1=s1+i
            ph = ph.replace(i, '').strip()        
    l=10-len(s1)        
    s2=ph[::-1]
    al=s2[0:l]
    s1=s1+al
    return s1
#ph ='abc99ef67d8992'       
#a=phone(ph) 
#print(a)

#Q4) Print maximum length of substring that has more number of 
#continuous one's sum = [1,1,1,0,1,0,1,0] output=[1,1,1]

def one(s):
    s+=str(0)
    w=n=""
    m=0
    for i in s:
        if(i==1):
            n+=str(i)
        else:
            if(len(n)>m):
                m=len(n)
                w=n
            n=""
    return w

#s=[1,1,1,0,0,1,1,1,1,1]
#one(s)


#Q1) list=['1','2','3','4','5','6'] inorder to add upto 9 no: of ways to group : 
#[4,5] or [1,2,6] both gives 9 but take the longest list ans: [1,2,6]
def llist(num,n):
    a=[int(i) for i in num]
    b=[]
    for i in range(0,len(a)):
        sums=0
        counter=[]
        for j in range(i,len(a)):
            sums=sums+a[j]
            if(sums==n):
                counter.append(a[j])
                b.append(counter)
                break
            elif(sums>n):
                del counter[-1]
                sums=sums-n
            else:
                counter.append(a[j])
    a=[len(i) for i in b]
    return(max(a))
#l=['1','2','3','4','5','6']
#n=9
#b=llist(l,n)
#print(b)