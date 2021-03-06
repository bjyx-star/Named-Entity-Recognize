import os 
import json 


root_path = "/".join(os.path.realpath(__file__).split("/")[:-2]) 


path_en_ace2004 = os.path.join(root_path, "data_preprocess/queries/en_ace04.json")
path_en_ace2005 = os.path.join(root_path, "data_preprocess/queries/en_ace05.json")
path_en_conll03 = os.path.join(root_path, "data_preprocess/queries/en_conll03.json")
path_en_genia = os.path.join(root_path, "data_preprocess/queries/en_genia.json")
path_en_ontonotes5 = os.path.join(root_path, "data_preprocess/queries/en_ontonotes5.json")
path_zh_msra = os.path.join(root_path, "data_preprocess/queries/zh_msra.json")
path_zh_ontonotes4 = os.path.join(root_path, "data_preprocess/queries/zh_ontonotes4.json")
path_zh_baidubaike = os.path.join(root_path, "data_preprocess/queries/baidubaike.json")
path_zh_ecommerce = os.path.join(root_path, "data_preprocess/queries/zh_ecommerce.json")
path_en_twitter = os.path.join(root_path, "data_preprocess/queries/en_twitter.json")



def load_query_map(query_map_path, type=None):
    with open(query_map_path, "r") as f:
        query_map = json.load(f)

    if type:
        query={"default":{},"labels":[type]}
        query["default"][type]=query_map["default"][type]
        query_map=query

    return query_map 


query_en_ace2004 = load_query_map(path_en_ace2004)
query_en_ace2005 = load_query_map(path_en_ace2005)
query_en_conll03 = load_query_map(path_en_conll03)
query_en_genia = load_query_map(path_en_genia)
query_en_ontonotes5 = load_query_map(path_en_ontonotes5)
query_zh_msra = load_query_map(path_zh_msra)
query_zh_ontonotes4 = load_query_map(path_zh_ontonotes4)
query_zh_wiki = load_query_map(path_zh_wiki)
query_en_wiki = load_query_map(path_en_wiki)
query_zh_ecommerce = load_query_map(path_zh_ecommerce)
query_zh_ecommerce_HP= load_query_map(path_zh_ecommerce, "HP")
query_zh_ecommerce_HC = load_query_map(path_zh_ecommerce, "HC")
query_en_twitter = load_query_map(path_en_twitter)

queries_for_dataset = {
    "en_ace2004": query_en_ace2004,
    "en_ace2005": query_en_ace2005,
    "en_conll03": query_en_conll03,
    "en_ontonotes5": query_en_ontonotes5,
    "en_genia": query_en_genia,
    "zh_ontonotes4": query_zh_ontonotes4,
    "zh_msra": query_zh_msra,
    "zh_wiki": query_zh_wiki,
    "en_wiki":query_en_wiki,
    "zh_ecommerce_HP":query_zh_ecommerce_HP,
    "zh_ecommerce_HC":query_zh_ecommerce_HC,
    "zh_ecommerce":query_zh_ecommerce,
    "en_twitter":query_en_twitter,

}


 
