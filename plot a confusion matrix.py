df = pd.read_csv('book1.csv')
df

X_semM = df.drop(['Programming','Fluid Mechanics'], axis=1)
X_sem_M


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

clf_en_max_dep5  = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=0)

# split X and y into training and testing sets
X_train_M, X_test_M, y_train_M, y_test_M= train_test_split(X_M, y, test_size = 0.33, random_state = 42)

clf_en_max_dep5.fit(X_train_M, y_train_M)
y_pred_M=clf_en_max_dep5.predict(X_test_M)

#entropy
confusion_matrix = metrics.confusion_matrix(y_test_M, y_pred_M)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['A',
            'B', 
            'C',  
            'D'])

cm_display.plot()

plt.show()
