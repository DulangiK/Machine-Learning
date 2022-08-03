sem=batch
bins = [0,40,50,60,70,100]
group_names=['F','S','C','B','A']
sem['grade']=pd.cut(batch['student_mark'],bins,labels=group_names)
sem
