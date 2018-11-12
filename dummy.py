import pdb
pdb.set_trace()
def animals():
    return "cat", "horse", "rat"
def build_sentence(verb):
    return "%s is sleeping" % verb
def full_sentence():
    list_of_verb = animals()
    for verb in list_of_verb:
        print(build_sentence(verb))

full_sentence()        

        
