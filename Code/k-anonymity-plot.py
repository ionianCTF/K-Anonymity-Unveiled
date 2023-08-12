from k-anonymity import *

def plot():
    k_list=[]
    per_list=[]
    per2_list=[]
    per3_list=[]

    k=100
    for k in range (0,k):
        percentage = k_anonymize('/content/sample_data/heart.csv', k, ["Age","Cholesterol","FastingBS"])
        percentage2 = k_anonymize('/content/sample_data/heart.csv', k, ["Age","Cholesterol","FastingBS"], {"Cholesterol": 80, "Age": 20})
        k_list.append(k)
        per_list.append(percentage)
        per2_list.append(percentage2)

    plt.xlabel("Value of k")
    plt.ylabel("Percentage of anonymized rows")
    plt.ylim(0, 100)
    plt.xlim(0,k)
    plt.plot(k_list, per_list, label='line 1')
    plt.plot(k_list, per2_list,"g", label='line 2')
    plt.legend(['Anonymized dataset without Generalization', 'Anonymized dataset with attribute generalization applied to Age and Cholesterol'])
    plt.show()

#k_anonymize('heart.csv', 20, ["Cholesterol","FastingBS"], generalization_intervals={"Cholesterol": 80})


plot()

def plot2():
    k_list=[]
    per_list=[]
    per2_list=[]
    per3_list=[]

    k=100
    for k in range (0,k):
        percentage = k_anonymize('/content/sample_data/heart.csv', k, ["Age"])
        percentage2 = k_anonymize('/content/sample_data/heart.csv', k, ["Age","Sex"])
        k_list.append(k)
        per_list.append(percentage)
        per2_list.append(percentage2)

    plt.xlabel("Value of k")
    plt.ylabel("Percentage of anonymized rows")
    plt.ylim(0, 100)
    plt.xlim(0,k)
    plt.plot(k_list, per_list, label='line 1')
    plt.plot(k_list, per2_list,"g", label='line 2')
    plt.legend(['Quasi-Identifiers for anonymization: Age', 'Quasi-Identifiers for anonymization: Age, Sex'])
    plt.show()

plot2()
