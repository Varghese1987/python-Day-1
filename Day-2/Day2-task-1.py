#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     06-08-2020
# Copyright:   (c) Lenovo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
#Sort the list
    l1 = [3, 1, 4, 2, 5]
    l1.sort()
    print(l1)

#print the squares of all the number in the list
    l2 = [3, 1, 4, 2, 5]
    squares = list(map(lambda x: x**2, l2))
    print(squares)

#print all the elements in the list
    l3 = [(105, "d"),(21, "z"),(0, "v")]
    result = [k for v in l3 for k in v]
    print(result)

#Print all the value in the list
    l = [{"color": "red","value": "#f00"},{"color": "green","value": "#0f0"},{"color": "blue","value": "#00f"}]
    for k, v in [(k, v) for x in l for (k, v) in x.items()]:
        print(k,v)

#print the hex codes of all colors
    hexVal = [x["value"] for x in l]
    print(hexVal)

#print the hex value of green
    hexValGreen = [x["value"] for x in l if(x["color"]=="green")]
    print(hexValGreen)

#Print the languages that are inferior to Python
    py = {'Python': 'Rocks', 'inferior': ['java', 'cobol']}
    result = [py[i] for i in py if(i=="inferior")]
    print(result)

#Print my Bill
    prices = {'apple': 0.40, 'banana': 0.50}
    my_purchase = {'apple': 1,'banana': 6}
    result=0
    for i in my_purchase:
        result += my_purchase[i]*prices[i]
    print(result)

    junk ={
        "characters":
            {
                "Lonestar":
                    {
                        "id": 55923,
                        "role": "renegade",
                        "items": [
                            "space winnebago",
                            "leather jacket"
                        ]
                    },
                "Barfolomew":
                    {
                        "id": 55924,
                        "role": "mawg",
                        "items": [
                            "peanut butter jar",
                            "waggy tail"
                        ]
                    },
                "Dark Helmet":
                    {
                        "id": 99999,
                        "role": "Good is dumb",
                        "items": [
                            "Shwartz",
                            "helmet"
                        ]
                    },
                "Skroob":
                    {
                        "id": 12345,
                        "role": "Spaceballs CEO",
                        "items": [
                            "luggage"
                        ]
                    }
            }
    }


    def list_all_values(json):

        for key, value in json.items():
            if type(value) is dict:
                list_all_values(value)
            else:
                print(key, ":", value)

    list_all_values(junk)

    def list_all_role(json):

        for key, value in json.items():
            if type(value) is dict:
                list_all_role(value)
            else:
                if key == "role":
                    print(value)

    list_all_role(junk)

    omg = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}}

#Get the first array value for the key 2
    result = {v[0] for k,v in omg.items() if k==2}
    print(result)

#Print all the array value for the key 2
    result = {v[i] for k,v in omg.items() if k==2 for i in range(len(v))}
    print(result)

#Print value of key 'a','b','c','d','e'
    def list_all(json):
        for key, value in json.items():
            if type(key) == str:
                print(value)
            if type(value) is dict:
                list_all(value)

    list_all(omg)

#Print the sum of the array with key 'e'
    from functools import reduce
    def list_all_sum(json):
        for key, value in json.items():
            if key == "e":
                result = reduce((lambda x,y : x+y),value)
                print(result)
            if type(value) is dict:
                list_all_sum(value)

    list_all_sum(omg)


#set value of key 'e' to ['Chera','Chola','Pandiya']
    def update_tree(tree,key,value):
        if key in tree:
            tree[key] = value
        for branch in tree.values():
            if type(branch) is dict:
                update_tree(branch,key,value)

    new = ['Chera','Chola','Pandiya']
    update_tree(omg,"e",new)
    print(omg['a']['b']['c']['d']['e'])


    body = {
        'query': {
            'filtered': {
                'query': {
                    'match': {
                        'description': 'addictive'
                    }
                },
                'filter': {
                    'term': {
                        'created_by': 'Mats'
                    }
                }
            }
        }
    }

    def list1(json):

        for key, value in json.items():
            if type(value) is dict:
                list1(value)
            else:
                if value == "Mats":
                    print(value)

    list1(body)

    def update_value(tree,key,value):
        if key in tree:
            tree[key] = value
        for branch in tree.values():
            if type(branch) is dict:
                update_value(branch,key,value)

    update_value(body,"filter","Mats")
    print(body["query"]['filtered']['filter'])

    movie_box = {
        "Robin Hood: Men in Tights": {
            "imdb_stars": 6.7,
            "length": 104,
            "stars": [
                {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
                {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"}
            ]
        }
    }

# print the IMDB star rating ( 6.7)
    def imdb(json):
        for key, value in json.items():
            if type(value) is dict:
                imdb(value)
            else:
                if key == "imdb_stars":
                    print(value)

    imdb(movie_box)

# print the length of the movie
    def length(json):
        for key, value in json.items():
            if type(value) is dict:
                length(value)
            else:
                if key == "length":
                    print(value)

    length(movie_box)

    print(movie_box["Robin Hood: Men in Tights"])

if __name__ == '__main__':
    main()
