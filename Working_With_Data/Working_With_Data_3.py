import csv

name = []
legion = []
allegiance = []


def save():
    with open('Chaos_list.csv', 'w') as new_file:
        fieldnames = ['Name', 'Legion', 'Allegiance']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        if save_mode == 0:

            for i in range(len(name)):
                old_data = {'Name': name[i], 'Legion': legion[i], 'Allegiance': allegiance[i]}
                csv_writer.writerow(old_data)

            new_data = {'Name': name_new, 'Legion': legion_new, 'Allegiance': allegiance_new}
            csv_writer.writerow(new_data)

        if save_mode == 1:

            for i in range(len(name)):
                if i == num:
                    continue
                else:
                    old_data = {'Name': name[i], 'Legion': legion[i], 'Allegiance': allegiance[i]}
                    csv_writer.writerow(old_data)



with open('Chaos_list.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print("----Warlord----")
        print ("Name: ", line['Name'])
        name.append(line['Name'])
        print ("Legion: ",line['Legion'])
        legion.append(line['Legion'])
        print ("Allegiance: ",line['Allegiance'])
        allegiance.append(line['Allegiance'])


input_data = input("\nProszę wybrać działanie \n -1 Dodaj nowy wpis \n -2 Usuń istniejacy\n ")

if input_data == "1":
    name_new = input("Proszę wpisać imię nowego warlorda: ")
    legion_new = input("Prosze wpisać legion: ")
    allegiance_new = input("Proszę wpisać, którego boga wyznaje: ")
    save_mode = 0
    save()

elif input_data == "2":
    row_for_deletion = input("Proszę wpisać, który wpis ma być usunięty: ")
    num = int(row_for_deletion)
    if num <= (len(name)):
        save_mode = 1
        save()
    else:
        print("Niepoprawny wybór!")

else:
    print("Niepoprawny wybór!")
