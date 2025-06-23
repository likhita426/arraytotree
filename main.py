def build(arr,tree,n,s,e):
    if s==e:
        tree[n]=arr[s]
        return
    else:
        mid=(s+e)//2
        build(arr,tree,2*n+1,s,mid)
        build(arr,tree,2*n+2,mid+1,e)
        tree[n]=tree[2*n+1]+tree[2*n+2]
arr=[3,1,2,5,6]
tree=[0]*(4*len(arr))
build(arr,tree,0,0,len(arr)-1)
print(tree)
        
    
