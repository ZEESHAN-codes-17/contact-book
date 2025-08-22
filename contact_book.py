
contacts = []



choice = 0

while choice != 4:
      
      print("Press 1 to add contacts")
      print("press 2 to view contacts")
      print("press 3 to search contacts")
      print("press 4 to exit")

      choice = int(input("enter your choice: "))

      if choice == 1:
            name = input("enter contact name: ")
            number = int(input("enter contact number: "))
            contact ={name: number}
            contacts.append(contact)
            print("contact saved!")
            list_as_str = str(contacts)
            with open("contactbook.txt", 'a') as f:
                  f.write(f"{name}:{number}\n")
      elif choice == 2:
            with open("contactbook.txt", 'r') as f:
                  print(f.read())
      elif choice == 3:
            search = input("enter name to search the contacts: ").lower()
            found = False
            with open('contactbook.txt', 'r') as f:
                  
             for line in f:
                  name, number = line.strip().split(":")
                  if search == name.lower():
                        print(f'{name} → {number}')
                        found = True
                        break
                        
            if not found:    
                        print("not found")
      elif choice == 4:
            print("goodbye")                                   
                        
