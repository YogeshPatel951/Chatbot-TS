import pickle
with open("data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)
print(output)




# m,n=map(int,input().split(' '))
# _=0
# matrix=list()
# while(_<m):
#     matrix.append(list(map(int,input().split(' '))))
#     _=_+1
# i=0
# j=0
# counter=0
# msid=8108460496
# for i in range(m):
#     for j in range(n):
#         if(matrix[i][j]==1):
#             matrix[i][j]=msid
#             #corner 1
#             if(i==0 and j==0):
#                 #right
#                 if(matrix[i][j+1]==1 or matrix[i][j+1]==msid):
#                     counter=counter+1
#                     matrix[i][j+1]=msid
#                     continue
#                 #down
#                 elif(matrix[i+1][j]==1 or matrix[i+1][j]==msid):
#                     counter=counter+1
#                     matrix[i+1][j]=msid
#                     continue
#                 #diag
#                 elif(matrix[i+1][j+1]==1 or matrix[i+1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j+1]=msid
#                     continue
#             #corner 2
#             elif(i==0 and j==n-1):
#                 #right
#                 if(matrix[i][j-1]==1 or matrix[i][j-1]==msid):
#                     counter=counter+1
#                     matrix[i][j-1]==msid
#                     continue
#                 #down
#                 elif(matrix[i+1][j]==1 or matrix[i+1][j]==msid):
#                     counter=counter+1
#                     matrix[i+1][j]==msid
#                     continue
#                 #diag
#                 elif(matrix[i+1][j-1]==1 or matrix[i+1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j-1]==msid
#                     continue
#             #corner 3
#             elif(i==m-1 and j==0):
#                 #right
#                 if(matrix[i][j+1]==1 or matrix[i][j+1]==msid):
#                     counter=counter+1
#                     matrix[i][j+1]==msid
#                     continue
#                 #down
#                 elif(matrix[i-1][j]==1 or matrix[i-1][j]==msid):
#                     counter=counter+1
#                     matrix[i-1][j]==msid
#                     continue
#                 #diag
#                 elif(matrix[i-1][j+1]==1 or matrix[i-1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j+1]==msid
#                     continue
#             #corner 4
#             elif(i==m-1 and j==n-1):
#                 #right
#                 if(matrix[i][j-1]==1 or matrix[i][j-1]==msid):
#                     counter=counter+1
#                     matrix[i][j-1]==msid
#                     continue
#                 #down
#                 elif(matrix[i-1][j]==1 or matrix[i-1][j]==msid):
#                     counter=counter+1
#                     matrix[i-1][j]==msid
#                     continue
#                 #diag
#                 elif(matrix[i-1][j-1]==1 or matrix[i-1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j-1]==msid
#                     continue            
#             #Left edges
#             elif(j==0 and i>0 and i<m-1):
#                 #right
#                 if(matrix[i-1][j]==1 or matrix[i-1][j]==msid):
#                     counter=counter+1
#                     matrix[i-1][j]==msid
#                     continue
#                 #down
#                 elif(matrix[i-1][j+1]==1 or matrix[i-1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j+1]==msid
#                     continue
#                 #left
#                 elif(matrix[i][j+1]==1 or matrix[i][j+1]==msid):
#                     counter=counter+1
#                     matrix[i][j+1]==msid
#                     continue
#                 #down
#                 elif(matrix[i+1][j+1]==1 or matrix[i+1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j+1]==msid
#                     continue 
#                 #diag
#                 elif(matrix[i+1][j]==1 or matrix[i+1][j]==msid):
#                     counter=counter+1
#                     matrix[i+1][j]==msid
#                     continue



#             #Upper edges
#             elif(i==0 and j>0 and j<n-1):
#                 #right
#                 if(matrix[i][j-1]==1 or matrix[i][j-1]==msid):
#                     counter=counter+1
#                     matrix[i][j-1]==msid
#                     continue
#                 #down
#                 elif(matrix[i+1][j-1]==1 or matrix[i+1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j-1]==msid
#                     continue
#                 #left
#                 elif(matrix[i+1][j]==1 or matrix[i+1][j]==msid):
#                     counter=counter+1
#                     matrix[i+1][j]==msid
#                     continue
#                 #down
#                 elif(matrix[i+1][j+1]==1 or matrix[i+1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j+1]==msid
#                     continue 
#                 #diag
#                 elif(matrix[i][j+1]==1 or matrix[i][j+1]==msid):
#                     counter=counter+1
#                     matrix[i][j+1]==msid
#                     continue

#             #Right edges
#             elif(j==n-1 and i>0 and i<m-1):
#                 #right
#                 if(matrix[i-1][j]==1 or matrix[i-1][j]==msid):
#                     counter=counter+1
#                     matrix[i-1][j]==msid
#                     continue
#                 #down
#                 elif(matrix[i-1][j-1]==1 or matrix[i-1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j-1]==msid
#                     continue
#                 #left
#                 elif(matrix[i][j-1]==1 or matrix[i][j-1]==msid):
#                     counter=counter+1
#                     matrix[i][j-1]==msid
#                     continue
#                 #down
#                 elif(matrix[i+1][j-1]==1 or matrix[i+1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j-1]==msid
#                     continue 
#                 #diag
#                 elif(matrix[i+1][j]==1 or matrix[i+1][j]==msid):
#                     counter=counter+1
#                     matrix[i+1][j]==msid
#                     continue

#             #Bottom edges
#             elif(i==m-1 and j>0 and j<n-1):
#                 #right
#                 if(matrix[i][j-1]==1 or matrix[i][j-1]==msid):
#                     counter=counter+1
#                     matrix[i][j-1]==msid
#                     continue
#                 #down
#                 elif(matrix[i-1][j-1]==1 or matrix[i-1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j-1]==msid
#                     continue
#                 #left
#                 elif(matrix[i][j-1]==1 or matrix[i][j-1]==msid):
#                     counter=counter+1
#                     matrix[i][j-1]==msid
#                     continue
#                 #down
#                 elif(matrix[i-1][j+1]==1 or matrix[i-1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j+1]==msid
#                     continue 
#                 #diag
#                 elif(matrix[i][j+1]==1 or matrix[i][j+1]==msid):
#                     counter=counter+1
#                     matrix[i][j+1]==msid
#                     continue

              

#             else:
#                 #right
#                 if(matrix[i][j+1]==1 or matrix[i][j+1]==msid):
#                     counter=counter+1
#                     matrix[i][j+1]==msid
#                     continue
#                 #down
#                 elif(matrix[i+1][j]==1 or matrix[i+1][j]==msid):
#                     counter=counter+1
#                     matrix[i+1][j]==msid
#                     continue
#                 #left
#                 elif(matrix[i][j-1]==1 or matrix[i][j-1]==msid):
#                     counter=counter+1
#                     matrix[i][j-1]==msid
#                     continue
#                 #down
#                 elif(matrix[i-1][j]==1 or matrix[i-1][j]==msid):
#                     counter=counter+1
#                     matrix[i-1][j]==msid
#                     continue 
#                 #diag
#                 elif(matrix[i+1][j+1]==1 or matrix[i+1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j+1]==msid
#                     continue
#                 #diag
#                 elif(matrix[i-1][j+1]==1 or matrix[i-1][j+1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j+1]==msid
#                     continue
#                 #diag
#                 elif(matrix[i+1][j-1]==1 or matrix[i+1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i+1][j-1]==msid
#                     continue
#                 #diag
#                 elif(matrix[i-1][j-1]==1 or matrix[i-1][j-1]==msid):
#                     counter=counter+1
#                     matrix[i-1][j-1]==msid
#                     continue   


#         elif(matrix[i][j]==msid):
#             counter=counter+1
#         else:
#             continue
        
# print(counter)


