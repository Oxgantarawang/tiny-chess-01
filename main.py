import json,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
def post(p,b):return json.load(u.urlopen(U+p,json.dumps(b).encode()))
V=(0,100,320,330,500,900,0)
KN=(33,31,18,14,-14,-18,-31,-33)
KI=(1,-1,16,-16,15,17,-15,-17)
BD=(15,17,-15,-17)
RD=(1,-1,16,-16)
KK=KN+KI
OF=((),(),KN,BD,RD,BD+RD,KI)
CK=[15]*128
for s,v in((0,13),(7,14),(4,12),(112,7),(119,11),(116,3)):CK[s]=v
SQ=[f for f in range(128)if not f&136]
PT=[[0]*64,[(i//8-1)*9 for i in range(64)]]+[[(3-max(abs(i%8-3),abs(i//8-3)))*m for i in range(64)]for m in(8,6,3,2,-10)]
B=[0]*128;T=1;C=0;KS=[4,116];Z=[];N=0;LIM=125000
class X(Exception):0
def att(s,w):
 for o in(15,17):
  x=s-o*w
  if not x&136 and B[x]==w:return 1
 for o in KK:
  x=s+o
  if not x&136 and B[x]==(2*w if o in KN else 6*w):return 1
 for o in BD+RD:
  x=s+o
  while not x&136:
   p=B[x]
   if p:
    if p==5*w or p==(3*w if o in BD else 4*w):return 1
    break
   x+=o
 return 0
def gen(cp):
 ms=[];A=ms.append
 for f in SQ:
  p=B[f]
  if p*T<=0:continue
  a=abs(p)
  if a==1:
   d=16*T;t=f+d
   if not B[t]:
    if t>111 or t<8:
     for q in(5,2):A((10000+V[q],f|t<<7|q<<14))
    elif not cp:
     A((0,f|t<<7))
     if f>>4==1+5*(T<0) and not B[f+2*d]:A((0,f|(f+2*d)<<7))
   for o in(-1,1):
    t=f+d+o
    if t&136:continue
    q=B[t]
    if q*T<0:
     v=V[abs(q)]
     if t>111 or t<8:
      for pr in(5,2):A((10000+V[pr]+10*v,f|t<<7|pr<<14))
     else:A((10*v-6,f|t<<7))
  else:
   for o in OF[a]:
    t=f+o
    while not t&136:
     q=B[t]
     if q:
      if q*T<0:A((10*V[abs(q)],f|t<<7))
      break
     if not cp:A((0,f|t<<7))
     if a in(2,6):break
     t+=o
 if not cp:
  k=4+112*(T<0);e=-T
  if not att(k,e):
   for b,d in((1,1),(2,-1))if T>0 else((4,1),(8,-1)):
    if C&b and not B[k+d] and not B[k+2*d] and(d>0 or not B[k+3*d])and not att(k+d,e) and not att(k+2*d,e):A((0,k|(k+2*d)<<7))
 ms.sort(reverse=True)
 return ms
def mk(m):
 global T,C
 f=m&127;t=m>>7&127;pr=m>>14&7;p=B[f];a=abs(p);cap=B[t]
 Z.append((m,cap,C))
 if a==6:
  KS[(1-T)//2]=t
  if t-f==2:B[t-1]=B[t+1];B[t+1]=0
  elif f-t==2:B[t+1]=B[t-2];B[t-2]=0
 B[t]=pr*T if pr else p;B[f]=0;C&=CK[f]&CK[t]
 T=-T
def um():
 global T,C
 m,cap,C=Z.pop();T=-T;f=m&127;t=m>>7&127;pr=m>>14&7;p=B[t]
 B[f]=T if pr else p;B[t]=cap
 if abs(p)==6:
  KS[(1-T)//2]=f
  if abs(t-f)==2:
   r=t-1 if t-f==2 else t+1;o=t+1 if t-f==2 else t-2;B[o]=B[r];B[r]=0
def ev():
 s=0
 for f in SQ:
  p=B[f]
  if not p:continue
  a=abs(p);i=f&7|f>>1&56
  if p<0:i^=56
  v=V[a]+PT[a][i]
  s+=v if p>0 else -v
 for w in(1,-1):
  k=KS[(1-w)//2]
  for o in(15,16,17):
   if not(k+o*w)&136 and B[k+o*w]==w:s+=30*w
 return s*T
def sr(a,b,d,y):
 global N,T;N+=1
 if N>LIM:raise X
 j=(1-T)//2;ck=att(KS[j],-T)
 if d>2 and not ck:
  T=-T;s=-sr(-b,-b+1,d-3,y+1);T=-T
  if s>=b:return b
 if d<=0 and not ck:
  s=ev()
  if s>=b:return b
  if s>a:a=s
 ms=gen(0) if d>0 or ck else gen(1);best=-10**6
 for _,m in ms:
  mk(m)
  if att(KS[j],T):um();continue
  s=-sr(-b,-a,d-1,y+1);um()
  if s>best:best=s
  if s>a:a=s
  if a>=b:break
 return best if best!=-10**6 else(-10**5+y if ck else(a if d<=0 else 0))
def uci(m):
 f=m&127;t=m>>7&127;q=m>>14&7;g=lambda x:"abcdefgh"[x&7]+str(x//16+1)
 return g(f)+g(t)+("nbrq"[q-2] if q else"")
def setfen(f):
 global T,C,B
 B=[0]*128;del Z[:];p=f.split();s=112
 for ch in p[0]:
  if ch=="/":s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   v="PNBRQK".find(ch.upper())+1;B[s]=v if ch.isupper() else -v
   if abs(B[s])==6:KS[0 if B[s]>0 else 1]=s
   s+=1
 T=1-2*(p[1]=="b");C=sum(1<<"KQkq".find(ch)for ch in p[2]if ch!="-")
def think(legal):
 global N;N=0
 ms=[m for _,m in gen(0) if uci(m) in legal];best=ms[0]
 for d in range(1,9):
  try:
   a=-10**6;r=[];bd=best
   for m in ms:
    mk(m);s=-sr(-10**6,1-a,d-1,1);um();r.append((s,m))
    if s>a:a=s;bd=m
   r.sort(key=lambda t:-t[0]);ms=[m for _,m in r];best=bd
  except X:break
 return uci(best)
while True:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  setfen(g["fen"]);m=think(g["legal_moves"]);g=post("/move",{"game":g["game"],"move":m})
