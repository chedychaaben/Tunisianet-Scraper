import requests, json
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    # You can add more headers if needed
}


def custom_ceil(number):
    if number.is_integer():
        return int(number)
    else:
        return int(number) + 1

def get_category_pagesNumber(cat_id, nb_items):
    data = {
        'action':'getFiltredProducts',
        'params':f'page=1&nb_items={nb_items}&controller_product_ids=&current_controller=category&page_name=category&id_parent_cat={cat_id}&orderBy=price&orderWay=asc&defaultSorting=price%3Aasc&customer_groups=1&random_seed=23100214&layout=vertical&count_data=1&hide_zero_matches=1&dim_zero_matches=1&sf_position=0&include_group=0&compact=991&compact_offset=2&compact_btn=1&npp=24&default_order_by=price&default_order_way=asc&random_upd=1&reload_action=1&p_type=1&autoscroll=1&oos_behaviour=0&combinations_stock=0&combinations_existence=0&combination_results=0&url_filters=1&url_sorting=1&url_page=1&dec_sep=%2C&tho_sep=+&merged_attributes=0&merged_features=0&oos_behaviour_=0',
    }
    r = requests.post("https://www.tunisianet.com.tn/module/amazzingfilter/ajax?ajax=1", data=data, headers=headers)
    html_content = json.loads(r.text)
    number_of_articles = int(html_content['products_num'])
    number_items = custom_ceil(number_of_articles / nb_items)
    return number_items

def scrape_page(page_number, cat_id, nb_items):
    print('Scraping ',nb_items, ' From Page : ' ,page_number)
    nb_items = 24
    data = {
        'action':'getFiltredProducts',
        'params':f'id_manufacturer=0&id_supplier=0&page={page_number}&nb_items={nb_items}&controller_product_ids=&current_controller=category&page_name=category&id_parent_cat={cat_id}&orderBy=price&orderWay=asc&defaultSorting=price%3Aasc&customer_groups=1&random_seed=23100214&layout=vertical&count_data=1&hide_zero_matches=1&dim_zero_matches=1&sf_position=0&include_group=0&compact=991&compact_offset=2&compact_btn=1&npp=24&default_order_by=price&default_order_way=asc&random_upd=1&reload_action=1&p_type=1&autoscroll=1&oos_behaviour=0&combinations_stock=0&combinations_existence=0&combination_results=0&url_filters=1&url_sorting=1&url_page=1&dec_sep=%2C&tho_sep=+&merged_attributes=0&merged_features=0&oos_behaviour_=0&available_options%5Bm%5D%5B0%5D=687%2C486%2C918%2C680%2C186%2C718%2C13%2C343%2C56%2C581%2C584%2C63%2C558%2C709%2C640%2C543%2C860%2C805%2C100%2C417%2C1054%2C1095%2C366%2C331%2C471%2C135%2C38%2C1035%2C660%2C823%2C914%2C68%2C698%2C489%2C668%2C907%2C835%2C868%2C67%2C37%2C509%2C106%2C97%2C621%2C827%2C1061%2C119%2C911%2C84%2C309%2C268%2C190%2C192%2C169%2C431%2C1102%2C1103%2C894%2C885%2C782%2C994%2C123%2C791%2C633%2C963%2C177%2C350%2C79%2C1055%2C669%2C1027%2C430%2C700%2C594%2C545%2C511%2C843%2C606%2C1021%2C567%2C970%2C520%2C455%2C1000%2C714%2C257%2C624%2C730%2C909%2C696%2C1039%2C682%2C989%2C342%2C128%2C379%2C997%2C657%2C572%2C796%2C296%2C330%2C450%2C508%2C317%2C521%2C269%2C239%2C18%2C96%2C608%2C416%2C263%2C538%2C188%2C456%2C515%2C672%2C869%2C834%2C320%2C414%2C275%2C728%2C52%2C443%2C759%2C917%2C1083%2C755%2C879%2C729%2C316%2C51%2C941%2C328%2C82%2C864%2C283%2C948%2C943%2C246%2C466%2C601%2C69%2C754%2C541%2C418%2C367%2C482%2C878%2C522%2C146%2C303%2C566%2C380%2C150%2C231%2C935%2C1016%2C1004%2C1074%2C111%2C1066%2C1065%2C1064%2C1063%2C1070%2C1068%2C1072%2C1069%2C1071%2C1067%2C183%2C527%2C953%2C604%2C514%2C164%2C306%2C134%2C689%2C103%2C786%2C996%2C851%2C950%2C453%2C59%2C480%2C481%2C44%2C36%2C645%2C267%2C261%2C78%2C252%2C141%2C185%2C487%2C799%2C29%2C199%2C733%2C127%2C758%2C635%2C404%2C1026%2C302%2C46%2C769%2C1033%2C781%2C801%2C427%2C368%2C364%2C764%2C299%2C73%2C1062%2C162%2C958%2C1052%2C290%2C651%2C71%2C475%2C1100%2C48%2C1017%2C745%2C393%2C363%2C898%2C325%2C870%2C955%2C787%2C452%2C193%2C142%2C464%2C492%2C1015%2C1045%2C832%2C163%2C90%2C1024%2C932%2C14%2C241%2C349%2C937%2C131%2C773%2C391%2C569%2C741%2C683%2C501%2C561%2C505%2C152%2C655%2C307%2C332%2C167%2C632%2C254%2C304%2C988%2C985%2C315%2C1028%2C991%2C301%2C962%2C701%2C376%2C250%2C1009%2C278%2C631%2C667%2C523%2C596%2C922%2C986%2C288%2C570%2C333%2C925%2C242%2C637%2C503%2C653%2C881%2C658%2C740%2C644%2C285%2C251%2C776%2C785%2C721%2C873%2C679%2C822%2C312%2C490%2C75%2C1084%2C674%2C323%2C661%2C406%2C151%2C462%2C338%2C798%2C528%2C435%2C905%2C420%2C237%2C534%2C373%2C322%2C577%2C392%2C470%2C1018%2C555%2C616%2C774%2C47%2C99%2C230%2C136%2C813%2C484%2C830%2C297%2C797%2C156%2C723%2C55%2C249%2C22%2C478%2C1094%2C1097%2C568%2C157%2C428%2C1088%2C407%2C748%2C720%2C862%2C88%2C57%2C512%2C702%2C240%2C65%2C516%2C454%2C647%2C174%2C118%2C936%2C387%2C371%2C375%2C711%2C153%2C1050%2C439%2C816%2C573%2C216%2C882%2C725%2C39%2C761%2C783%2C548%2C6%2C223%2C165%2C137%2C491%2C424%2C62%2C1087%2C31%2C30%2C861%2C286%2C901%2C551%2C451%2C576%2C945%2C792%2C292%2C34%2C993%2C191%2C734%2C1047%2C7%2C8%2C820%2C944%2C790%2C626%2C92%2C114%2C929%2C340%2C334%2C883%2C85%2C738%2C999%2C846%2C1101%2C154%2C921%2C707%2C939%2C806%2C341%2C1056%2C300%2C235%2C180%2C717%2C173%2C506%2C808%2C53%2C124%2C233%2C713%2C852%2C1037%2C1029%2C752%2C1005%2C978%2C789%2C507%2C681%2C388%2C607%2C817%2C259%2C468%2C737%2C196%2C750%2C977%2C1048%2C649%2C483%2C1075%2C749%2C692%2C716%2C211%2C552%2C826%2C460%2C850%2C40%2C179%2C726%2C642%2C500%2C780%2C920%2C255%2C200%2C432%2C1002%2C327%2C1093%2C498%2C845%2C1010%2C872%2C685%2C113%2C287%2C775%2C859%2C526%2C502%2C952%2C170%2C284%2C767%2C3%2C550%2C722%2C110%2C447%2C1082%2C50%2C212%2C9%2C1057%2C329%2C158%2C81%2C814%2C248%2C436%2C445%2C21%2C260%2C175%2C553%2C463%2C208%2C402%2C202%2C181%2C311%2C98%2C11%2C314%2C27%2C386%2C308%2C715%2C1073%2C902%2C294%2C652%2C176%2C383%2C855%2C1085%2C588%2C706%2C804%2C336%2C856%2C863%2C818%2C1041%2C981%2C461%2C206%2C742%2C354%2C518%2C1076%2C634%2C33%2C967%2C313%2C440%2C1078%2C972%2C15%2C1032%2C189%2C612%2C784%2C770%2C688%2C542%2C204%2C965%2C1099%2C222%2C928%2C374%2C356%2C968%2C358%2C844%2C389%2C841%2C335%2C485%2C161%2C234%2C494%2C339%2C1013%2C1014%2C756%2C877%2C930%2C771%2C677%2C1086%2C842%2C274%2C305%2C947%2C583%2C727%2C705%2C1092%2C1008%2C172%2C1003%2C904%2C166%2C549%2C412%2C94%2C628%2C638%2C324%2C866%2C847%2C441%2C159%2C17%2C811%2C743%2C232%2C618%2C938%2C107%2C530%2C293%2C979%2C592%2C663%2C694%2C148%2C788%2C236%2C280%2C126%2C664%2C765%2C954%2C949%2C934%2C271%2C703%2C665%2C337%2C810%2C42%2C205%2C980%2C747%2C673%2C778%2C865%2C1036%2C1038%2C1044%2C122%2C821%2C360%2C101%2C554%2C219%2C403%2C411%2C160%2C946%2C228%2C465%2C281%2C326%2C390%2C840%2C662%2C273%2C794%2C884%2C544%2C532%2C291%2C220%2C565%2C961%2C444%2C238%2C590%2C397%2C1090%2C425%2C24%2C1001%2C60%2C1051%2C998%2C1012%2C975%2C145%2C277%2C976%2C446%2C793%2C678%2C623%2C591%2C833%2C574%2C648%2C438%2C1060%2C434%2C369%2C580%2C195%2C923%2C224%2C400%2C957%2C143%2C121%2C517%2C951%2C32%2C971%2C807%2C735%2C564%2C560%2C1007%2C992%2C365%2C531%2C910%2C854%2C697%2C708%2C399%2C819%2C321%2C266%2C178%2C372%2C1080%2C1011%2C437%2C876%2C357%2C736%2C598%2C213%2C112%2C102%2C676%2C473%2C396%2C442%2C198%2C1077%2C803%2C593%2C265%2C559%2C670%2C659%2C310%2C990%2C777%2C1025%2C394%2C586%2C1079%2C93%2C58%2C12%2C906%2C26%2C295%2C933%2C467%2C795%2C474%2C319%2C540%2C802%2C247%2C675%2C370%2C80%2C1058%2C184%2C931%2C867%2C630%2C43%2C347%2C448%2C187%2C857%2C276%2C513%2C348%2C479%2C108%2C966%2C95%2C203%2C974%2C353%2C890%2C1098%2C227%2C744%2C973%2C815%2C1043%2C927%2C359%2C221%2C138%2C423%2C264%2C563%2C609%2C346%2C919%2C825%2C524%2C1105%2C318%2C41%2C83%2C809%2C772%2C91%2C690%2C147%2C64%2C654%2C139%2C641%2C557%2C155%2C345%2C497%2C289%2C401%2C547%2C488%2C1053%2C982%2C625%2C536%2C413%2C262%2C377%2C874%2C731%2C800%2C429%2C245%2C763%2C693%2C74%2C385%2C695%2C880%2C643%2C45%2C298%2C656%2C344%2C244%2C35%2C408%2C117%2C686%2C398%2C533%2C197%2C995%2C459%2C639%2C384%2C282%2C1022%2C753%2C5%2C256%2C578%2C1020%2C395%2C61%2C916%2C768%2C149%2C495%2C875%2C209%2C1096%2C666%2C535%2C529%2C837%2C49%2C585%2C125%2C104%2C25%2C132%2C171%2C960%2C207%2C983%2C258%2C766%2C1059%2C959%2C546%2C120%2C352%2C144%2C140%2C1089%2C828%2C987%2C253%2C650%2C912%2C272%2C853%2C838%2C510%2C582%2C426%2C836%2C746%2C1031%2C1104%2C732%2C556%2C848%2C218%2C646%2C225%2C1091%2C129%2C779%2C76%2C1034%2C270%2C627%2C458%2C587%2C1046%2C897%2C1019%2C72%2C1030%2C824%2C415%2C579%2C214%2C913%2C724%2C924%2C410%2C1042%2C229%2C831%2C469%2C1006%2C4%2C719%2C449%2C476%2C493%2C600%2C942%2C182%2C409%2C1049%2C382%2C1040%2C605%2C629%2C10%2C351%2C684%2C613%2C858%2C751%2C984%2C168%2C571%2C915%2C849%2C839%2C525%2C760%2C757%2C133%2C940%2C956%2C812%2C210%2C562%2C194%2C871%2C908%2C1081%2C361%2C597%2C739%2C381%2C130%2C964%2C19%2C243&available_options%5Bf%5D%5B168%5D=2910%2C2987%2C2990%2C2988%2C2992%2C3445%2C4357%2C4435%2C3002%2C4055%2C3554%2C2991%2C3139%2C3983%2C3867%2C3003%2C3121%2C3122%2C3004%2C3464%2C3637%2C3006%2C3548%2C3469%2C3710&available_options%5Bf%5D%5B169%5D=3931%2C2914%2C2913%2C2912%2C4388%2C2997%2C4387%2C3869%2C4086&available_options%5Bf%5D%5B165%5D=2897%2C2896&available_options%5Bf%5D%5B189%5D=3247%2C3246&available_options%5Bf%5D%5B76%5D=91%2C278%2C90&available_options%5Bf%5D%5B184%5D=3136%2C3135&available_options%5Bf%5D%5B84%5D=4109%2C3603%2C3604%2C4211%2C4189%2C3606%2C4396%2C4411%2C4054%2C3605%2C3607&sliders%5Bp%5D%5B0%5D%5Bfrom%5D=219&sliders%5Bp%5D%5B0%5D%5Bmin%5D=219&sliders%5Bp%5D%5B0%5D%5Bto%5D=14999&sliders%5Bp%5D%5B0%5D%5Bmax%5D=14999',

    }
    r = requests.post("https://www.tunisianet.com.tn/module/amazzingfilter/ajax?ajax=1", data=data, headers=headers)
    r.encoding = 'utf-8'
    html_content = json.loads(r.text)['product_list_html']
    # Setting the products number
    products_num = int(json.loads(r.text)['products_num'])

    total_of_pages = custom_ceil(products_num / nb_items)
    #print(total_of_pages)

    soupHTML = BeautifulSoup(html_content, 'html.parser')

    articleTAGS = soupHTML.find_all("article")
    for i in range(len(articleTAGS)):
        articleTAG = articleTAGS[i]
        if i == 0 or i == 1:
            object = {
                "product_title": articleTAG.find('h2').text,
                "reference": articleTAG.find('span', {'class':'product-reference'}).text,
                "price": articleTAG.find('span',{'class':'price'}).text,
                "discount": articleTAG.find('span' ,{'class':'discount-amount'}).text if articleTAG.find('span', {'class': 'discount-amount'}) is not None else 0, 
                "brand": articleTAG.find('div', {'class':'product-manufacturer'}).find('a')['href'],
                "brand_image_url": articleTAG.find('div', {'class':'product-manufacturer'}).find('img')['src'],
                "availability": articleTAG.find('div', {'id':'stock_availability'}).find('span')['class'][0] == "in-stock",
                "description": articleTAG.find('div', {'itemprop': 'description'}).text,#.text.encode('latin-1').decode('utf-8', 'replace'), #.text.strip('\n')
                "product_images": [img['src'] for img in articleTAG.find('a', {'class':'thumbnail'}).find_all('img')],
                "details_page_url": articleTAG.find('h2').find('a')['href'],
                "found_in_page": page_number,
                "position_in_page": i+1
                }
            print(object["product_title"])

def main():
    category_id = 338
    nb_items = 24

    total_of_pages = get_category_pagesNumber(category_id,nb_items)

    for page in range(1,total_of_pages+1):
        scrape_page(page, category_id, nb_items)

main()

def getAllCategories():
    # this will return a list of objects
    # categories = [
    #   {"id": 1, "grand_parent_cat":"Informatique", "parent_cat":"Ordinateur Portable", "name":"Pc Portable"}, 
    #   {"id": 2, "grand_parent_cat":"Impression", "parent_cat":"Imprimantes", "name": "Imprimante À Réservoir Intégré"}
    # ]
    # After making a quick tour on the categories, we noticed two major things
    # 1) If the Grandparent categorie has childs then it's better to only take the childs 
    # 2) If the grandparent categorie has no childs then we should take it as parent and grandparent categorie

    r = requests.get("https://www.tunisianet.com.tn/", headers=headers)
    soupHTML = BeautifulSoup(r.text, 'html.parser')
    menu_verticalSOUP = soupHTML.find("div", {"class":"menu-vertical"}).find("ul", {"class":"menu-content top-menu"})

    list_of_categories = []
    grand_parent_categoriesSOUP = menu_verticalSOUP.find_all("li", {"class":"level-1"})
    print(len(grand_parent_categoriesSOUP))
    for grand_parent_categorie in grand_parent_categoriesSOUP:
        this_grand_parent_name = grand_parent_categorie.find('span').text.strip()
        
        for child in grand_parent_categorie.find_all("li"):
            if 'item-header' in child["class"]:
                list_of_categories.append({"GrandParent": this_grand_parent_name, "Parent":child.text.strip(), "categories":[], "has_childs":None})
            elif 'item-line' in child["class"]:
                list_of_categories[-1]["categories"].append({"id":re.search(r'.com.tn/(\d+)-', child.find("a")['href']).group(1), "name": child.text.strip()})

    # Classifing By Childs or not
    for cat in list_of_categories:
        if cat["categories"] == []:
            cat["has_childs"] = False
        else:
            cat["has_childs"] = True
    # OK
    print(list_of_categories)

#getAllCategories()