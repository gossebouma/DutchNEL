# DutchNEL Named Entity Linking for Dutch

Scripts for evaluating Named Entity Linking for Dutch on existing datasets (WinNL, Damuel, MultiNERD)

RQ1 : How well do existing multilingual linkers perform for Dutch?

## Resources
*  damuel https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-5047

* mewli-X en/of xtreme (ik snap nog niet helemaal wat de verhouding tussen datasets hier is)  (Dit betekent iig dat je zelf de scripts moet draaien om NL data te maken)


https://github.com/google-research/google-research/blob/43e61cf4eb057588cdabcc9eb8f0bcd4e13cf4a8/dense_representations_for_entity_retrieval/mel/mewsli-x.md#L4
https://github.com/google-research/xtreme

* WiNNL dan is er ook nog: https://aclanthology.org/2024.dlnld-1.3.pdf Als ik het goed begrijp is dit nog een evaluatie corpus, maar ik kan het corpus zelf nergens vinden. Mss de auteurs eens mailen.
* yet another option: https://huggingface.co/Babelscape/wikineural-multilingual-ner
* also check multiNERD, automatically annotated silver quality data (for training, testing?)

Systemen om te evalueren: BELA, mGenre. Waarschuwing: ik heb beide nog niet kunnen installeren (als ik de bela documentatie goed begrijp zijn er pretrained modellen die we kunnen gebruiken. bij mGenre loop ik steeds there is also a huggingface version of mgenre, https://huggingface.co/facebook/mgenre-wiki
seems less work to install (tho still might need to download the trie)

relik seems also SOTA but for EN only (Navigli and others, on huggingface as well)

see also https://github.com/topics/entity-linking
tegen version conflicts aan)

https://github.com/facebookresearch/BELA/tree/main
https://github.com/facebookresearch/GENRE/tree/main

# Systems

RQ2: Is het mogelijk een bestaande entity linker voor het Engels aan te passen voor NL?

* REL
https://github.com/informagi/REL

Dat betekent dat je ipv Engelse Wikipedia NL Wikiedia text moet gebruiken voor trainen. Lijkt haalbaar, ook omdat NL veel kleiner is, maar preprocessing kan nog lastig zijn, en trainen moet je ws op het cluster doen.

(en misschien ook nog: sommige van deze systemen doen alleen entity disambiguation, en maken gebruik van een aparte module voor entity recognition (bv spacy). Dan zou je ook nog kunnen kijken naar wat daar op het moment het beste werkt voor het NL)

* spacy/dbpedia entity linker, works for Dutch as well

https://github.com/MartinoMensio/spacy-dbpedia-spotlight?tab=readme-ov-file

use as baseline?

* other baselines: spacy ner/nec + wikidata entity finder api
* babelfy (online demo? api? sources provides a link to wikidata (sparql access?), how to filter named entities (not concepts) only? seems to be possible, See http://babelfy.org/guide
babel does have wikidata links as well, not sure whether these are included in babelfy (examples suggest only dbpedia ids)

* refined -- retrain for dutch 
but see: https://aclanthology.org/2023.findings-emnlp.1007.pdf
https://github.com/amazon-science/ReFinED/tree/mrefined
this describes mrefined, multilingual refined!!
but not for dutch? see also for copy with slightly more info and model??
https://github.com/mrpeerat/mReFinED
seems we still need to create a dataset fom scratch, but should in theory work by adding/replacing languages with nl lg code, and running the scripts
there is also a huggingface version of mgenre, https://huggingface.co/facebook/mgenre-wiki
seems less work to install (tho still might need to download the trie)

# Other

relik seems also SOTA but for EN only (Navigli and others, on huggingface as well)

see also https://github.com/topics/entity-linking


