import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE

# 1. Load data
df = pd.read_csv('data.csv')

# 2. Understand data
print(df.info())
print(df.describe())
print(df.isnull().sum())

# 3. Handle duplicates
df.duplicatesd().sum()
df.drop_duplicates(inplace=True)

# 4. Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)  # Numerical
df.fillna(df.mode().iloc[0], inplace=True)  # Categorical

# 5. Handle outliers (IQR method)
for col in df.select_dtypes(include=[np.number]).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]

# 6. Encode categorical variables
le = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    if col != 'target':  # Don't encode target yet
        df[col] = le.fit_transform(df[col])

# Or one hot encoders
df = pd.get_dummies(df, drop_first=True)

# 7. Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# 8. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 9. Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 10. Handle imbalanced data (if needed)
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Ready for modeling!
