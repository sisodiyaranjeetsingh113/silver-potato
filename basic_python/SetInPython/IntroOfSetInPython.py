
'''
print(st[0])
st[0]=100
del st
print(st)
'''

'''
st.clear()
print(st)

'''
st={1,5,3,2,7,1,6}
print(st)
print(len(st))
print(type(st))

st3={4,5,6}
st1={1,2,3,4}

st2=st.difference(st1)
print(st2)
st2=st.difference(st1,st3)
print(st2)
st2=st1.union(st3)
print(st2)

st2=st1.isdisjoint(st3)
print(st2)

st2=st1.intersection(st3)
print(st2)

