"""
Module containing the pattern matching used fot the regex analysis of PSVD biopsies
"""

patterns = {
    "hiperplasia_nodular_regenerativa": r"[Hh]iperpl[aà]sia\s+nodular\s+regenerativa|[Hh]iperplasia\s+nodular\s+regenerativa",
    
    "cirrosi_portal_incompleta": r"[Cc]irrosi\s+portal\s+incompleta|[Cc]irrosis\s+portal\s+incompleta",
    
    "venopatia_portal_obliterativa": r"[Vv]enopat[ií]a\s+portal\s+obliterativa",
    
    "esclerosi_hepatoportal": r"[Ee]sclerosi\s+hepatoportal|[Ee]sclerosis\s+hepatoportal",
    
    "fibrosi_septal_incompleta": r"[Ff]ibrosi\s+septal\s+incompleta|[Ff]ibrosis\s+septal\s+incompleta",
    
    "herniacio_vasos_venosos_periportals": r"[Hh]erniaci[óo][n]?\s+(?:de\s+)?vasos\s+venosos\s+periportals?|[Hh]erniaci[óo][n]?\s+(?:de\s+)?vasos\s+venosos\s+periportales",
    
    "cavernomatosi": r"[Cc]avernomat[oó]si|[Cc]avernomat[oó]sis|[Cc]avernomat[oó]so|[Cc]avernomat[oó]sos",
    
    "flebosclerosi": r"[Ff]lebosclerosi|[Ff]lebosclerosis",
    
    "esclerosi_venosa": r"[Ee]sclerosi\s+venosa|[Ee]sclerosis\s+venosa",
    
    "venopenia": r"[Vv]enop[èe]nia",
    
    "dilatacio_sinusoidal": r"[Dd]ilataci[óo][n]?\s+sinuso[iï]dal",
    
    "pseudoangiomatos": r"[Pp]seudoangiomat[oó]s|[Pp]seudoangiomat[oó]si|[Pp]seudoangiomat[oó]sis|[Pp]seudoangiomat[oó]so|[Pp]seudoangiomat[oó]sos",
    
    "peliosis": r"[Pp]eliosi|[Pp]eliosis",
    
    "estenosi_portal": r"[Ee]stenosi\s+portal|[Ee]stenosis\s+portal",
    
    "vasos_aberrants_periportals": r"[Vv]asos\s+aberrants?\s+periportals?|[Vv]asos\s+aberrantes\s+periportales",
    
    "estructures_vasculars_dilatades": r"[Ee]structur[ae]s\s+vasculars?\s+dilatad[ae]s|[Ee]structuras\s+vasculares\s+dilatadas",
    
    "dilatació_sinusoïdal_no_zonal": r"[Dd]ilataci[óo][n]?\s+sinuso[iï]dal\s+no[-\s]?zonal",
    
    "fibrosi_perisinusoïdal": r"[Ff]ibrosi\s+perisinuso[iï]dal|[Ff]ibrosis\s+perisinuso[iï]dal",
    
    "dilatació_vena_porta": r"[Dd]ilataci[óo][n]?\s+(?:de\s+)?(?:la\s+)?vena\s+porta",
    
    "herniació_vena_porta": r"[Hh]erniaci[óo][n]?\s+(?:de\s+)?(?:la\s+)?vena\s+porta",
    
    "encreuament_espais_porta": r"[Ee]ncreuament\s+(?:dels\s+)?espais\s+porta|[Cc]ruzamiento\s+(?:de\s+los\s+)?espacios\s+porta",
    
    "alteracions_arquitecturals": r"[Aa]lteracions\s+arquitecturals|[Aa]lteraciones\s+arquitecturales",
    
    "proximitat_d'estructures": r"[Pp]roximitat\s+d[e']estructures|[Pp]roximidad\s+de\s+estructuras",
    
    "vasos_dilatats": r"[Vv]asos\s+dilatats|[Vv]asos\s+dilatados",
    
    "absència_branca_venosa_portal": r"[Aa]bs[èe]ncia\s+(?:de\s+)?(?:la\s+)?branca\s+venosa\s+portal|[Aa]usencia\s+(?:de\s+)?(?:la\s+)?rama\s+venosa\s+portal"
}
