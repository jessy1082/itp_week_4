# ITP Week 4 Day 2 Exercise

#Today we will pull information from the Pokemon api, put it into a dictionary, and then put that info into a new Excel file.  We will write the pseudocode as a group in class.  Be sure to follow the pseudocode, break your problems down into smaller pieces, and consult the documentation whenever you get stuck: https://pokeapi.co/api/v2/pokemon

#PSEUDO-CODE:

#GET NAME AND ABILITY FROM API
#PUT INFO IN DICTIONARY
#ADD THE DICTIONARY TO A NEW EXCEL WORKBOOK

#imports:
    #json
    #openpyxl

#Input
    #json file from pokemon api
    #workbook

#Assign response to variable

#Create workbook
    #get workbook from openpy
    #load workbook
    #assign workbook to variable
    
#Create Worksheet
    #assign sheet to variable

#Create a dictionary, assign to variable

#FUNCTION BODY
    #Convert response to json file
        #clean data(response)
            #json.loads(response.text)

    #Iterate over response
        #for each pokemon in response
            #variable key = pokemon.name
            #variable value = pokemon.abilites
            #append {key/value} pair to dictionary

    #Iterate over dictionary
        #for each item in dictionary
            #assign dictionary values to rows & cols
                #Write Name to Cell
                #Write Abilities to Cell

#Output
    #Workbook

pokemon = {
    bulbasour : {
        "name": "pokemon_name",
        "abilities": ["ability1", "ability2"]
    },
    pikachu : {
        "name": "pokemon_name",
        "abilities": ["ability1", "ability2"]
    }
}