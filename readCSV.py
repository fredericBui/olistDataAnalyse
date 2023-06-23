import csv
import matplotlib.pyplot as plt


# Total of data
data_lenght = 0

# Tableaux pour stocker les valeurs des colonnes
longitude = []

# Total d'éléments
total_house_median = 0

with open('customers.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    for index, row in enumerate(csv_reader):
        data_lenght += 1
        if index == 0:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])

        # if index > 0:

        #     longitude.append(row[0])
        #     latitude.append(row[1])
        #     housing_median_age.append(float(row[2]))
        #     total_rooms.append(row[3])
        #     total_bedrooms.append(row[4])
        #     population.append(row[5])
        #     households.append(row[6])
        #     median_income.append(row[7])
        #     median_house_value.append(row[8])
        #     ocean_proximity.append(row[9])

        #     if row[9] == "NEAR BAY":
        #         total_near_bey += 1
        #         if float(row[2]) < 28.639486434108527 :
        #             total_near_bey_and_younger_than_average += 1
        #         else :
        #             total_near_bey_and_older_than_average += 1
        #     else :
        #         total_far_bey += 1
        #         if float(row[2]) < 28.639486434108527 :
        #             total_far_bey_and_younger_than_average += 1
        #         else :
        #             total_far_bey_and_older_than_average += 1

        #     if float(row[2]) > 28.639486434108527 :
        #         total_house_older_than_average += 1

# # Calcul de la moyenne
# for data in housing_median_age:
#     total_house_median += data

# print("Nombre de données : " + str(data_lenght))
# print("Age moyen des maisons : " + str(total_house_median/len(longitude)) + " ans")
# print("Total de maison supérieur à la moyenne d'âge : " + str(total_house_older_than_average))
# print("Total de maison proche de la mer : " + str(total_near_bey))
# print("Total de maison loin de la mer : " + str(total_far_bey))
# print("Total de maison proche de la mer et inférieur à la moyenne d'âge : " + str(total_near_bey_and_younger_than_average))
# print("Total de maison proche de la mer et supérieur à la moyenne d'âge : " + str(total_near_bey_and_older_than_average))
# print("Total de maison loin de la mer et inférieur à la moyenne d'âge : " + str(total_far_bey_and_younger_than_average))
# print("Total de maison loin de la mer et supérieur à la moyenne d'âge : " + str(total_far_bey_and_older_than_average))

# categories = ['NearBay younger', 'NearBay older', 'FarBay younger', 'FarBay older']
# values = [total_near_bey_and_younger_than_average, total_near_bey_and_older_than_average, total_far_bey_and_younger_than_average, total_far_bey_and_older_than_average]

# # Create a bar plot
# plt.bar(categories, values)

# # Set labels and title
# plt.xlabel('Categories')
# plt.ylabel('Number of house')
# plt.title('Bay age hypothese')

# # Display the plot
# plt.show()

# Pistes :
# Distance physique
# Distance à la moyenne
# Distance temporelle

        

