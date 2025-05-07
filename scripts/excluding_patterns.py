excluding_patterns = {
    
    # Existing patterns
    'cirrhosis': r'\b(?:cirrosi[s]?|cirr[oó]tic[oa]?|fibrosi[s]? hep[aá]tic[oa]? avan[cç]ad[oa])\b',
    'rejection': r'\b(?:recha[cz]o|rebuig|rechazo (?:celular|agudo|cr[oó]nico)|rebuig (?:cel·lular|agut|cr[òo]nic))\b',
    'hepatocarcinoma': r'\b(?:hepatocarcinoma|carcinoma hepatocelular|CHC|HCC|c[aá]ncer (?:de|del) h[ií]gado|c[àa]ncer (?:de|del) fetge)\b',
    'alcohol': r'\b(?:alcohol(?:[ií]smo|isme)?|et[ií]lico|et[ií]lic|enolismo|abuso de alcohol|abús d\'alcohol|consum (?:excessiu|cr[òo]nic) d\'alcohol|consumo (?:excesivo|cr[óo]nico) de alcohol)\b',
    'VHC': r'\b(?:VHC|hepatitis C|virus (?:de (?:la )?)?hepatitis C|virus de l\'hepatitis C|infec(?:ci[oó]n|ció) por (?:el )?VHC|infecció per VHC|hepatopat[ií]a (?:por|por el|pel) VHC|genotip[o]? (?:\d+[a-z]? )?(?:del|de la) VHC|tratamiento (?:anti|para(?: el)?) VHC|tractament (?:anti|per(?: al)?) VHC|RNA(?:-| )VHC|RNA del VHC|carga viral(?: del)? VHC|càrrega viral(?: del)? VHC|anti-VHC positivo|anti-VHC positiu|respuesta virológica (?:sostenida|mantinguda))\b',
    
    # Autoimmune Hepatitis (Hepatitis Autoinmune/Hepatitis Autoimmune)
    'hepatitis_autoimmune': r'\b(?:hepatitis auto(?:inmune|immune)|hepatitis (?:auto(?:inmunitaria|immunitària)|inmunitaria|immunitària)|HAI|malaltia hepàtica auto(?:immune|immunitària)|enfermedad hepática auto(?:inmune|inmunitaria))\b',
    
    # Hepatitis (general)
    'hepatitis': r'\b(?:hepatitis|hepatit[ie]s (?:viral|vírica)|hepatopatía inflamatoria|hepatopatia inflamatòria|inflamación (?:del|de) hígado|inflamació (?:del|de) fetge|dany hepàtic inflamatori|daño hepático inflamatorio)\b',
    
    # Metastasis (Metástasis/Metàstasi)
    'metastasis': r'\b(?:met[àa]sta(?:si[s]?)|met[àa]st[àa][st]ic[oa]?|c[àa]ncer met[àa]st[àa][st]ic[oa]?|disseminació tumoral|diseminación tumoral|lesión(?:es)? met[àa]st[àa][st]ic[oa][s]?|lesió(?:ns)? met[àa]st[àa][st]ic[oa]?)\b',
    
    # Lymphoma (Linfoma/Limfoma)
    'lymphoma': r'\b(?:l[ií]n?foma|l[ií]n?foma (?:hep[àa]tic[oa]?|no hodgkin|hodgkin|de c[èe]l·lul(?:a|es) [bt]|de c[ée]lul(?:a|as) [bt])|neoplasia linfoide|neoplàsia limfoide)\b',
    
    # Adenocarcinoma
    'adenocarcinoma': r'\b(?:adenocarcinoma|adenocarcinoma (?:hep[aà]tic[oa]?|metast[aà][st]ic[oa]?))\b',
    
    # Cholangiocarcinoma (Colangiocarcinoma)
    'cholangiocarcinoma': r'\b(?:col[aà]ngiocarcinoma|c[aà]ncer de (?:las )?v[ií]as biliares|c[àa]ncer (?:de les )?vies biliars|tumor de (?:los )?conductos biliares|tumor (?:dels )?conductes biliars|CCA)\b',
    
    # Steatohepatitis (Esteatohepatitis/Esteatohepatitis)
    'steatohepatitis': r'\b(?:esteatohepatitis|hepatitis esteató[st]ica|esteatohepatitis no alcoh[oó]lica|esteatohepatitis no alcoh[oò]lica|EHNA|EHGNA|h[ií]gado graso|fetge gras|NASH)\b'
}