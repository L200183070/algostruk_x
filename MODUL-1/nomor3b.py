##3b

def jumlahHurufKonsonan(hrf):
    konsonan = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z'
    a = 0
    hasil = 0
    for i in hrf:
        if i in konsonan:
            a += len(i)
        else:
            a +=0
    hasil = len(hrf),a
    return hasil
