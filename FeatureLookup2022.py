# FeatureLookup2022.py
# NS Dawn

# - - - - - - - - - - - - - - - - - - - 

# data declaration
data = {
    "i":"+++---+++000++++0--+--",
    "ɪ":"+++----++000++++0--+--",
    "u":"+++-+++++000++++0--+--",
    "ʊ":"+++-++-++000++++0--+--",
    "e":"++----+++000++++0--+--",
    "ɛ":"++-----++000++++0--+--",
    "o":"++--+++++000++++0--+--",
    "ɔ":"++--++-++000++++0--+--",
    "a":"++-++--++000++++0--+--",
    "ɑ":"++-++--++000++++0--+--",
    "æ":"++-+---++000++++0--+--",
    "y":"+++--++++000++++0--+--",
    "ʏ":"+++--+-++000++++0--+--",
    "ø":"++---++++000++++0--+--",
    "œ":"++---+-++000++++0--+--",
    "ɘ":"++--+--++000++++0--+--",
    "ʌ":"++--+--++000++++0--+--",
    "ɯ":"+++-+-+++000++++0--+--",
    "ɨ":"+++-+-+++000++++0--+--",
    "j":"-++---+++000++++0--+--",
    "w":"-++-+++++000++++0--+--",
    "ɥ":"-++--++++000++++0--+--",
    "m":"--000-0+--00-+--0-++--",
    "n":"--000-0+-++-----0-++--",
    #"n̪":"--000-0+-+++----0-++--",
    "ɳ":"--000-0+-+------0-++--",
    "ɲ":"--+---0+-+-++---0-++--",
    "ŋ":"--+-+-0+--00+---0-++--",
    "ɴ":"----+-0+--00+---0-++--",
    "l":"--000-0++++----+0+-+--",
    "ɭ":"--000-0+++-----+0+-+--",
    "ʎ":"--+---0+++-++--+0+-+--",
    "r":"--000-0++++----+0--+--",
    "ɽ":"--000-0+++-----+0--+--",
    "ʀ":"----+-0++-00+--+0--+--",
    #"t̪":"--000-0--+++----------",
    #"d̪":"--000-0--+++-------+--",
    "t":"--000-0--++-----------",
    "d":"--000-0--++--------+--",
    "ʈ":"--000-0--+------------",
    "ɖ":"--000-0--+---------+--",
    "s":"--000-0--++----++---+-",
    "z":"--000-0--++----++--+--",
    "ɬ":"--000-0--++----+-+--+-",
    "ɮ":"--000-0--++----+-+-+--",
    "θ":"--000-0--+++---+----+-",
    "ð":"--000-0--+++---+---+--",
    "ʃ":"--+---0--+-++--++---+-",
    "ʒ":"--+---0--+-++--++--+--",
    "c":"--+---0--+-++---------",
    "ɟ":"--+---0--+-++------+--",
    "ç":"--+---0--+-++--+----+-",
    "ʝ":"--+---0--+-++--+---+--",
    "tʃ":"--+---0--+-++---+-----",
    "dʒ":"--+---0--+-++---+--+--",
    "ts":"--000-0--++-----+-----",
    "dz":"--000-0--++-----+--+--",
    "pf":"--000-0---00-+--+-----",
    "bv":"--000-0---00-+--+--+--",
    "p":"--000-0---00-+--------",
    "b":"--000-0---00-+-----+--",
    "ɸ":"--000-0---00-+-+----+-",
    "β":"--000-0---00-+-+---+--",
    "f":"--000-0---00-+-++---+-",
    "v":"--000-0---00-+-++--+--",
    "k":"--+-+-0---00+---------",
    "g":"--+-+-0---00+------+--",
    "x":"--+-+-0---00+--+----+-",
    "ɣ":"--+-+-0---00+--+---+--",
    "q":"----+-0---00+---------",
    "ɢ":"----+-0---00+------+--",
    "χ":"----+-0---00+--++---+-",
    "ʁ":"----+-0---00+--++--+--",
    "ħ":"--000-0---00--++----+-",
    "ʕ":"--000-0---00--++---+--",
    "ʔ":"--000-0---00---------+",
    "h":"--000-0---00---+----+-",
    "ɦ":"--000-0---00---+---++-",
}
	
features = [
"syllabic", "vocalic", "high", "low", "back", "round", "atr", "sonorant", "approximant", "coronal", "anterior", "distributed", "dorsal", "labial", "pharyngeal", "continuant", "strident", "lateral", "nasal", "voice", "aspirated", "glottalized"
]

abbreviations = [
    (" syll ", " syllabic "),
    (" voc ", " vocalic "),
    (" hi ", " high "),
    (" lo ", " low "),
    (" bk ", " back "),
    (" rd ", " round "),
    (" son ", " sonorant "),
    (" approx ", " approximant "),
    (" cor ", " coronal "),
    (" ant ", " anterior "),
    (" dist ", " distributed "),
    (" dor ", " dorsal "),
    (" lab ", " labial "),
    (" phar ", " pharyngeal "),
    (" cont ", " continuant "),
    (" str ", " strident "),
    (" lat ", " lateral "),
    (" nas ", " nasal "),
    (" lat ", " lateral "),
    (" voi ", " voice "),
    (" asp ", " aspirated "),
    (" glot ", " glottalized ")
]


# - - - - - - - - - - - - - - - - - - - 

# fn that converts the string data declared into referenceable dictionaries
def dict_convert(in_string) :

    dict_entry = {}
    assert len(in_string) == len(features)
    for e in range(len(in_string)) :
        dict_entry[features[e]] = in_string[e]

    return dict_entry

# fn that prints dicts
def dict_print(in_dict) :
    for key in in_dict :
        print(key + ": [" + in_dict[key] + "]")

# fn that interprets the command and returns a string to be split
def cmd_parse(instr) :
    out = instr.strip() # strip extra spaces on both sides
    out = out.lower() # make everything lowercase
    replace_list = abbreviations
    for r in replace_list:
        out = out.replace(r[0], r[1]) # allow for abbrivations

    out = out.replace("<", "").replace(">", "") # remove erroneous syntax

    return out
    
    
# - - - - - - - - - - - - - - - - - - - 

# fn init
def init() :
    for key in data :
        data[key] = dict_convert(data[key])
    print("Welcome to FeatureLookup.py.")
    print("Type <help> for help.")

# fn main
def main() :
    set = {}
    init()
    
    on = True
    while on :
        user_input = input("\033[1m\n>> \033[0m")
        parsed_user_input = cmd_parse(user_input)
        if parsed_user_input == "": # do nothing with empty strings
            continue
        if user_input.strip() != parsed_user_input : # if the parser guessed something, tell the user.
            print("\033[1mInterpreted: <\033[0m " + parsed_user_input + " \033[1m>\033[0m")
        # print()
        cmd = parsed_user_input.split()

        if cmd[0] == "end" :
            print("FeatureLookup.py terminated.\n")
            on = False
        elif cmd[0] == "help" :
            # print("This program is a translation of the PHONOLOGICAL FEATURES CHART (vers. 2015-2, based on Hayes 2009), for ease of use.")
            print("This program is a compliation of feature data for use in phonology. This is a specific version for use with UCSC LING 101, Spring 2022, with Professor Jaye Padgett.")
            print("- - - - - - - - -")
            print("This program includes 4 basic functions, as follows:\n")
            print("The <list> function lists all items of a given type.\nUsage: list\n       list <phoneme>\n       list <feature> <+/-/0>\n")
            print("The <compare> function lists the similar features of any amount of phonemes. \nUsage: compare <phoneme1> <phomeme2> ...\n")
            print("The <contrast> function lists the different features of two phonemes. \nUsage: contrast <phoneme1> <phomeme2>\n")
            print("The <end> function terminates the program.\nUsage: end")
            print("- - - - - - - - -")
            print("This program covers the basic phonemes provided by the chart, and does not include diacritics.")
            print("Type <list> for a list of all phonemes in this program's dictionary.")
            print("Type <advanced> for more advanced functionality.")
        elif cmd[0] == "advanced" :
            print("The <set> function allows the user to hold a certain subset of phonemes.")
            print("Simply typing <set> will print the current set.")
            print("Phonemes can be added or deleted from the set.")
            print("The set can also be filtered to only phonemes of a specific feature.")
            print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
        elif cmd[0] in ["list", "l"] : 
            if len(cmd) == 1 :
                i = 0
                for entry in data :
                    i += 1 
                    print("{0:<4}".format(entry), end = (" " if i % 8 != 0 else "\n"))
                if i % 8 != 0 :
                    print("")
            elif len(cmd) == 2:
                if cmd[1] in data :
                    dict_print (data[cmd[1]])
                else :
                    print("Feature value must be specified as +, -, or 0." if cmd[1] in features else "Phoneme <" + cmd[1] + "> not found.")
                    print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")
            elif len(cmd) == 3 :
                if cmd[1] in features :
                    if cmd[2] in ["+", "-", "0"] :
                        i = 0
                        for entry in data : 
                            if data[entry][cmd[1]] == cmd[2] :
                                i += 1
                                print("{0:<4}".format(entry), end = (" " if i % 8 != 0 else "\n"))
                        if i % 8 != 0 :
                            print("")
                        if i == 0 : 
                            print("No phoneme with the given feature was found.")
                    else : 
                        print("Feature value must be +, -, or 0.")
                        print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")  
                else :
                    print("Feature <" + cmd[1] + "> not found.")
                    print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")  
            else : 
                print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")
        elif cmd[0] in ["compare", "com"] :
            '''
            if len(cmd) == 3 :
                if cmd[1] in data and cmd[2] in data : 
                    compare_dict = {}
                    for entry in data[cmd[1]] :
                        if data[cmd[1]][entry] ==  data[cmd[2]][entry] :
                            compare_dict[entry] = data[cmd[1]][entry]
                    if len(compare_dict) == 0 :
                        print("No similarities were found.")
                    else :
                        dict_print(compare_dict)
                else : 
                    print("Phonemes not found or invalid.")
                    print("Usage: compare <phoneme1> <phomeme2>")
            else : 
                print("Usage: compare <phoneme1> <phomeme2>")
            '''
            if len(cmd) > 1 :
                for phone in cmd[1:] :
                    if phone not in data :
                        print("Phonemes not found or invalid.")
                        print("Usage: compare <phoneme1> <phomeme2> ...")
                        break
                else :
                    compare_dict = {}
                    for entry in data[cmd[1]] :
                        for phone in cmd[2:] :
                            if data[cmd[1]][entry] != data[phone][entry] :
                                break
                        else :
                            compare_dict[entry] = data[cmd[1]][entry]
                    if len(compare_dict) == 0 :
                        print("No similarities were found.")
                    else :
                        dict_print(compare_dict)
            else :
                print("Usage: compare <phoneme1> <phomeme2> ...")
                
        elif cmd[0] in ["contrast", "con"] :
            if len(cmd) == 3 :
                if cmd[1] in data and cmd[2] in data : 
                    contrast_dict = {}
                    for entry in data[cmd[1]] :
                        if data[cmd[1]][entry] !=  data[cmd[2]][entry] :
                            contrast_dict[entry] = data[cmd[1]][entry] + "/" + data[cmd[2]][entry]
                    if len(contrast_dict) == 0 :
                        print("No differences were found.")
                    else :
                        dict_print(contrast_dict)
                else : 
                    print("Phonemes not found or invalid.")
                    print("Usage: contrast <phoneme1> <phomeme2>")
            else : 
                print("Usage: contrast <phoneme1> <phomeme2>")
        elif cmd[0] in ["set", "s"] :
            f = True
            if len(cmd) == 1 :
                pass
            elif len(cmd) == 2 :
                if cmd[1] == "clear" :
                    set = {}
                    print("Set cleared.")
                    f = False
                else : 
                    f = False
                    print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
            elif len(cmd) == 3 :
                if cmd[1] == "add" :
                    if cmd[2] == "all" :
                        for entry in data :
                            set[entry] = data[entry]
                    elif cmd[2] in data :
                        set[cmd[2]] = data[cmd[2]]
                    else :
                        f = False
                        print("Feature value must be specified as +, -, or 0." if cmd[2] in features else "Phoneme <" + cmd[1] + "> not found.")
                        print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
                elif cmd[1] in ["delete", "del"] :
                    if cmd[2] == "all" :
                        set = {}
                    elif cmd[2] in set :
                        del set[cmd[2]]
                    elif cmd[2] in data :
                        f = False
                        print("Phoneme <" + cmd[2] + "> not in set.")
                    else : 
                        f = False
                        print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
                else : 
                    f = False
                    print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
            elif len(cmd) == 4 :
                if cmd[1] == "add" :
                    if cmd[2] in features :
                        if cmd[3] in ["+", "-", "0"] :
                            for entry in data :
                                if data[entry][cmd[2]] == cmd[3] :
                                    set[entry] = data[entry]
                        else : 
                            f = False
                            print("Feature value must be +, -, or 0.")
                            print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
                    else :
                        print("Feature <" + cmd[2] + "> not found.")
                        f = False
                elif cmd[1] in ["delete", "del"] :
                    if cmd[2] in features :
                        if cmd[3] in ["+", "-", "0"] :
                            delete_entries = []
                            for entry in set :
                                if set[entry][cmd[2]] == cmd[3] :
                                    delete_entries.append(entry)
                            if len(delete_entries) != 0 :
                                for entry in delete_entries :
                                    del set[entry]
                            else :
                                print("No entries deleted.")                                
                        else : 
                            f = False
                            print("Feature value must be +, -, or 0.")
                            print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
                    else :
                        print("Feature <" + cmd[2] + "> not found.")
                        f = False
                elif cmd[1] == "filter" :
                    if cmd[2] in features :
                        if cmd[3] in ["+", "-", "0"] :
                            delete_entries = []
                            for entry in set :
                                if set[entry][cmd[2]] != cmd[3] :
                                    delete_entries.append(entry)
                            if len(delete_entries) != 0 :
                                for entry in delete_entries :
                                    del set[entry]
                            else :
                                print("No entries filtered.")                                
                        else : 
                            f = False
                            print("Feature value must be +, -, or 0.")
                            print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")
                    else :
                        print("Feature <" + cmd[2] + "> not found.")
                        f = False
            else : 
                f = False
                print("Usage: set\n       set clear\n       set add <phoneme>\n       set add <feature> <+/-/0>\n       set add all\n       set delete <phoneme>\n       set delete <feature> <+/-/0>\n       set filter <feature> <+/-/0>")


            if f :
                if len(set) != 0 :
                    i = 0
                    for entry in set :
                        i += 1
                        print("{0:<4}".format(entry), end = (" " if i % 8 != 0 else "\n"))
                    if i % 8 != 0 :
                        print("")
                else :
                    print("Set is empty. Enter <set add all> to add all phonemes.")
        elif cmd[0] == "" : 
            pass
        else :
            print("Command <" + cmd[0] + "> not understood.")

# - - - - - - - - - - - - - - - - - - - 

if __name__ == '__main__' :
    main()

# - - - - - - - - - - - - - - - - - - - 
# PARSING COMMAND FOR .CSV FILES (ignore)
"""
# PARSING LINE 1
text = input()
print(text.replace(",",'''", "'''))

# PARSING DATA
text = ''''''
lines = text.split("\n")

for line in lines: 
    entry = line.split(",")
    output = ""
    output += '''"'''
    output += entry[0]
    output += '''":"'''
    for i in range(len(entry) - 1) :
        output += entry[i+1]
    output += '''",'''
    print(output)


"""