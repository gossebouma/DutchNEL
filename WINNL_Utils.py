import pandas

winnl = pandas.read_json('WiNNL/dutch_winnl_data.json')


# ## Access an item
# 
# Rows are annotations for individual sentences. An alternative is to retrieve oby article URL, ie all text for an article, to improve matching for entities identified by last name only. 
# 

def winnl_annotations(Id) :
    row = winnl.loc[Id]
    gold = set()
    for token in row['qid'] :
        if token.startswith('B-') :
            qid = token.replace('B-','')
            gold.add(qid)
    return gold 

def winnl_text(Id) :
    return winnl.loc[Id]['original']


def winnl2mgenre(Id) :
    row = winnl.loc[Id]
    annotation = []
    for anno in row['qid'] :
        if anno.startswith('B-') :
            annotation.append(anno.removeprefix("B-"))
    items = []
    for qid_item in annotation :  
        inside = 0
        string = ""
        for (tok,qid) in zip(row['tokens'],row['qid']) :
            if qid == 'O' :
                if inside :
                    sep = " [END] "
                    inside = 0 
                else :
                    sep = " "  
            else :
                qidsplit = qid.split('-')
                if qidsplit[1] == qid_item :
                    if qidsplit[0] == "B" :
                        sep = " [START] "
                        inside = 1 
                    else :
                        sep = " "
                else :
                    sep = " " 
            string = string + sep + tok
        items.append((string,qid_item))
    return items 
        



