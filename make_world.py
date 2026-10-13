# -*- coding: utf-8 -*-
"""Generates world.json for the ONDEX Panorama360 page (fr-FR)."""
import json, re, sys, unicodedata

OUT = sys.argv[1] if len(sys.argv) > 1 else "world.json"

# ---------------------------------------------------------------- helpers
NB, NNB = " ", " "
def fr(s):
    """French typography: non-breaking spaces before : ; ? ! % » and after «."""
    s = s.replace("'", "’")
    s = re.sub(r" :", NB + ":", s)
    s = re.sub(r" ;", NNB + ";", s)
    s = re.sub(r" \?", NNB + "?", s)
    s = re.sub(r" !", NNB + "!", s)
    s = re.sub(r" %", NNB + "%", s)
    s = s.replace("« ", "«" + NB).replace(" »", NB + "»")
    return s

SKIP = {"url", "photo", "email", "id", "usecase", "anchor", "kit", "type", "color", "same_as", "hub", "island",
        "screen", "mode", "stage", "lang", "icon", "product", "base", "layout", "landscape", "relief", "arcs",
        "accent", "primary", "secondary", "default_theme", "ui_brand", "audience", "floor2", "slack"}
def typo(o, key=None):
    if isinstance(o, dict):
        return {k: (v if k in SKIP and isinstance(v, str) else typo(v, k)) for k, v in o.items()}
    if isinstance(o, list):
        if key in ("products", "usecases"):
            return o
        return [typo(v, key) for v in o]
    if isinstance(o, str):
        if o.startswith("http") or o.startswith("<path"):
            return o
        if key in ("value", "v"):
            return fr(o).replace(" ", NB)
        return fr(o)
    return o

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:22]

# ---------------------------------------------------------------- public resources (all opened)
def story(customer, industry, url, v, l, products, summary, source="Salesforce"):
    r = {"type": "story", "title": customer, "customer": customer, "industry": industry, "url": url, "source": source,
         "stat": {"v": v, "l": l}, "summary": summary, "verified": True}
    if products:
        r["products"] = products
    return r

S = {
 "poclain": story("Poclain Hydraulics", "Industrie · France", "https://www.salesforce.com/fr/customer-stories/poclain/",
    "+18 %", "d'offres saisies dans le CRM en un an", ["Sales Cloud", "Revenue Cloud", "Tableau", "MuleSoft"],
    "ETI industrielle familiale, Poclain centralise leads, devis et contrats dans Salesforce : plus de 90 % de connexion au CRM et +18 % d'offres saisies."),
 "airliquide": story("Air Liquide et Poclain", "Industrie · France", "https://www.salesforce.com/fr/blog/air-liquide-poclain/",
    "150 000", "références devisées dans Revenue Cloud (Poclain)", ["Revenue Cloud"],
    "Des devis encadrés par des prix minimum et cible, la fin d'Excel et de la double saisie : les données partent automatiquement vers l'ERP."),
 "saintgobain": story("Saint-Gobain", "Matériaux de construction · France", "https://www.mulesoft.com/case-studies/saint-gobain-manufacturing",
    "90", "flux MuleSoft déployés en six mois", ["MuleSoft"],
    "Saint-Gobain relie CRM, e-commerce, SAP S/4HANA et ateliers avec MuleSoft : 57 % de réutilisation des API et des devis convertis en commandes en quelques secondes.",
    source="MuleSoft"),
 "etex": story("Etex", "Matériaux de construction · Belgique", "https://www.salesforce.com/eu/blog/how-etex-uses-crm/",
    "1 800", "utilisateurs en production en 16 mois", None,
    "Le groupe de matériaux de construction réunit ses divisions sur un CRM unique : 1 800 utilisateurs en production en 16 mois."),
 "jkcement": story("JK Cement", "Ciment et matériaux · Inde", "https://www.salesforce.com/in/customer-stories/jk-cement/",
    "90 %", "des commandes passées via Salesforce", ["Consumer Goods Cloud", "Experience Cloud", "Marketing Cloud", "Tableau"],
    "Une plateforme unique pour commerciaux, distributeurs et prescripteurs : 90 % des commandes et plus de 10 000 partenaires passent par Salesforce."),
 "siemens": story("Siemens", "Industrie · Allemagne", "https://www.salesforce.com/customer-stories/siemens/",
    "2 500", "leads par mois qualifiés par Agentforce", ["Commerce Cloud", "Data 360", "Agentforce"],
    "Sur SiePortal (1,4 million d'utilisateurs enregistrés), Agentforce qualifie environ 2 500 leads par mois et ramène la réponse de quelques jours à quelques minutes."),
 "endress": story("Endress+Hauser", "Instrumentation industrielle · Suisse", "https://www.salesforce.com/customer-stories/endress-and-hauser/",
    "50 %", "des demandes traitées en autonomie (objectif)", ["Agentforce", "Data 360", "Service Cloud", "Experience Cloud"],
    "Agentforce sur le portail client, nourri par Data 360 : la moitié des demandes de service traitées en autonomie et +30 % de productivité attendus."),
 "fisher": story("Fisher & Paykel", "Électroménager · Nouvelle-Zélande", "https://www.salesforce.com/customer-stories/fisher-and-paykel/agentic-self-service/",
    "80 %", "des problèmes résolus en libre-service", ["Agentforce", "Service Cloud", "Data 360"],
    "Avec Agentforce et Data 360, les clients résolvent seuls environ 80 % de leurs problèmes ; l'assistant des conseillers recueille 75 % d'avis positifs."),
 "imerys": story("Imerys", "Minéraux industriels · France", "https://www.salesforce.com/fr/customer-stories/Imerys/",
    "+80 M€", "de ventes croisées en un an", ["Manufacturing Cloud", "Sales Cloud", "Revenue Cloud", "Marketing Cloud"],
    "Imerys passe d'une organisation produit à une organisation marché avec Manufacturing Cloud et CPQ : +80 M€ de ventes croisées en un an et des devis 32 fois plus productifs."),
 "schneider": story("Schneider Electric", "Équipements électriques · France", "https://www.salesforce.com/eu/customer-stories/schneider-electric-boosts-customer-satisfaction/",
    "15 min", "du devis à la commande pour les distributeurs", ["Sales Cloud", "Service Cloud", "MuleSoft", "Tableau"],
    "Schneider Electric génère jusqu'à 500 opportunités par jour avec Sales Cloud et l'IA, et ramène le devis-commande distributeur à 15 minutes en Amérique du Nord."),
}
DOC_REV = {"type": "doc", "title": "Agentforce for Revenue : des devis en langage naturel dans Revenue Cloud",
           "url": "https://www.salesforce.com/news/stories/agentforce-for-revenue-announcement/", "source": "Salesforce News", "verified": True}

def video(title, url, dur, kicker, stitle, summary, poster, who, color):
    return {"type": "video", "title": title, "url": url, "duration": dur, "source": "Salesforce+", "verified": True,
            "kicker": kicker, "summary_title": stitle, "summary": summary, "poster": poster, "who": who, "color": color}
P26 = "https://www.salesforce.com/plus/experience/dreamforce_2026/series/"
P25 = "https://www.salesforce.com/plus/experience/dreamforce_2025/series/"
V = {
 "mfg26": video("Manufacturing Keynote: Building an Agentic Future Together", P26 + "manufacturing_automotive_and_energy_at_dreamforce_2026/episode/episode-s1e2",
    "45:05", "Dreamforce 2026 · Keynote industrie", "L'industrie agentique",
    ["La keynote industrie de Dreamforce 2026.", "Des agents au service des industriels, de la vente aux opérations."], "Industrie", "Industriels", "#0B5CAB"),
 "rev26": video("Revenue Keynote: Beyond CPQ, One Engine, Every Experience", P26 + "sales_at_dreamforce_2026/episode/episode-s1e5",
    "47:01", "Dreamforce 2026 · Revenue", "Au-delà du CPQ",
    ["Un seul moteur pour les devis, les contrats et la facturation.", "Pour chaque canal de vente."], "Devis", "Ventes et devis", "#5A1BA9"),
 "road26": video("The Manufacturing Cloud ROI-Focused Roadmap", P26 + "manufacturing_automotive_and_energy_at_dreamforce_2026/episode/episode-s1e11",
    "32:24", "Dreamforce 2026 · Feuille de route", "La feuille de route Manufacturing",
    ["Les prochaines étapes de Manufacturing Cloud.", "Une feuille de route centrée sur le retour sur investissement."], "Feuille de route", "Manufacturing Cloud", "#2E844A"),
 "agents25": video("How AI Agents Are Transforming Manufacturing Efficiency", P25 + "manufacturing_automotive_and_energy_at_dreamforce_2025/episode/episode-s1e2",
    "08:47", "Dreamforce 2025 · En moins de 10 minutes", "Des agents pour l'efficacité",
    ["Des agents IA dans la vente industrielle.", "Le témoignage d'un industriel, en moins de dix minutes."], "Agents", "Témoignage", "#0176D3"),
 "diff25": video("Differentiated Experiences with Agentforce Manufacturing", P25 + "manufacturing_automotive_and_energy_at_dreamforce_2025/episode/episode-s1e4",
    "44:50", "Dreamforce 2025 · Agentforce Manufacturing", "Des expériences différenciantes",
    ["Agentforce Manufacturing pour les clients et les partenaires.", "Ventes, service et réseau de distribution."], "Expérience", "Manufacturing", "#032D60"),
 "pilot26": video("Turning AI Pilot Sprawl into Measurable Agentic Value", P26 + "manufacturing_automotive_and_energy_at_dreamforce_2026/episode/episode-s1e12",
    "19:51", "Dreamforce 2026 · Valeur mesurable", "Du pilote à la valeur",
    ["Passer de pilotes dispersés à une valeur mesurable.", "Le retour d'un industriel avec plusieurs agents en production."], "Valeur", "Industriels", "#06A59A"),
}
def th(title, url, dur):
    return {"type": "trailhead", "title": title, "url": "https://trailhead.salesforce.com/content/learn/" + url, "duration": dur, "source": "Trailhead", "verified": True}
T = {
 "mfg": th("Agentforce Manufacturing Basics", "modules/manufacturing-cloud-basics", "1 h 10"),
 "mfgql": th("Agentforce Manufacturing: Quick Look", "modules/agentforce-manufacturing-quick-look", "15 min"),
 "mfgsales": th("Explore Agentforce Manufacturing for Sales", "trails/explore-manufacturing-cloud-for-sales", "2 h 30"),
 "af": th("Introduction to Agentforce", "modules/introduction-to-agentforce", "10 min"),
 "rev": th("Efficient Sales with Agentforce Revenue Management", "modules/efficient-sales-with-revenue-cloud", "1 h 10"),
 "d360": th("Data 360 Setup", "modules/customer-360-audiences-for-admins", "40 min"),
 "prm": th("Partner Relationship Management", "modules/partner-relationship-management", "30 min"),
}

def src(title, url):
    return {"title": title, "url": url}
SRC = {
 "poclain": src("Salesforce · Poclain Hydraulics", S["poclain"]["url"]),
 "airliquide": src("Salesforce · Air Liquide et Poclain", S["airliquide"]["url"]),
 "saintgobain": src("MuleSoft · Saint-Gobain", S["saintgobain"]["url"]),
 "etex": src("Salesforce · Etex", S["etex"]["url"]),
 "jkcement": src("Salesforce · JK Cement", S["jkcement"]["url"]),
 "siemens": src("Salesforce · Siemens", S["siemens"]["url"]),
 "endress": src("Salesforce · Endress+Hauser", S["endress"]["url"]),
 "fisher": src("Salesforce · Fisher & Paykel", S["fisher"]["url"]),
 "fisher_rep": src("Salesforce · Fisher & Paykel", "https://www.salesforce.com/customer-stories/fisher-and-paykel/agentic-service-rep-assistance/"),
 "imerys": src("Salesforce · Imerys", S["imerys"]["url"]),
 "schneider": src("Salesforce · Schneider Electric", S["schneider"]["url"]),
 "revenue": src("Salesforce News · Agentforce for Revenue", DOC_REV["url"]),
}
def kpi(value, label, note=None, source=None, estimate=False):
    o = {"value": value, "label": label}
    if note: o["note"] = note
    if source: o["source"] = SRC[source]
    if estimate: o["estimate"] = True
    return o
def est(value, label, note=None):
    return kpi(value, label, note, estimate=True)

# ---------------------------------------------------------------- architecture from products + systems
LAYER = {"MuleSoft": 1, "Data 360": 1, "Tableau": 1,
         "Sales Cloud": 2, "Service Cloud": 2, "Revenue Cloud": 2, "Manufacturing Cloud": 2, "Experience Cloud": 2,
         "Commerce Cloud": 2, "Marketing Cloud": 2, "Salesforce Platform": 2,
         "Agentforce": 3, "Slack": 3}
COLS = ["Systèmes ONDEX", "Données et intégration", "Applications", "Agents et collaboration"]
def arch(products, systems):
    cols = [{"label": COLS[0], "nodes": [{"id": "x-" + slug(s), "label": s, "kind": "ext"} for s in systems]}]
    for i in (1, 2, 3):
        nodes = [{"id": slug(p), "label": p, "product": p} for p in products if LAYER.get(p) == i]
        if nodes:
            cols.append({"label": COLS[i], "nodes": nodes})
    return {"columns": cols, "steps": "auto"}

# ---------------------------------------------------------------- use cases
UC = {}
def uc(id, title, short, summary, where, pain, approach, outcomes, personas, products, systems, resources, base=None):
    UC[id] = {"title": title, "short": short, "summary": summary, "where": where, "pain": pain,
              "approach": [{"title": a, "text": b, "product": c} for a, b, c in approach],
              "outcomes": outcomes, "personas": personas, "products": products,
              "architecture": arch(products, systems), "resources": resources, "_base": base}

# --- Usine
uc("usine-reclamation-lot", "Relier chaque réclamation au lot de production", "Réclamation → lot",
   "Chaque défaut signalé remonte au lot, à la ligne et à la formulation.",
   "Usine de Chevigny · laboratoire qualité, lignes d'extrusion et SAV",
   "Dans l'extrusion, un défaut d'aspect ou de géométrie se répète tant que sa cause n'est pas trouvée. Quand le SAV et la production ne partagent pas les mêmes données, l'analyse prend des semaines.",
   [("Saisir la réclamation", "Le SAV ouvre un dossier structuré : photos, référence, quantité, chantier.", "Service Cloud"),
    ("Retrouver le lot", "MuleSoft relie le dossier au lot, à la ligne et à la formulation dans l'ERP et le MES.", "MuleSoft"),
    ("Repérer les causes", "Data 360 rapproche réclamations, lots et contrôles qualité pour faire ressortir les récurrences.", "Data 360"),
    ("Alerter la qualité", "L'alerte arrive dans Slack avec le résumé du dossier et le lot concerné.", "Slack")],
   [est("−30 %", "de délai d'analyse des réclamations", "Ordre de grandeur à confirmer sur l'historique ONDEX."),
    kpi("90", "flux d'intégration MuleSoft déployés en six mois", "chez Saint-Gobain", "saintgobain")],
   ["Responsable qualité (QHSE)", "Chef de production", "Assistante SAV"],
   ["Service Cloud", "MuleSoft", "Data 360", "Agentforce", "Slack"], ["ERP", "MES", "Laboratoire qualité"],
   [S["saintgobain"], T["mfg"]])
uc("usine-campagnes-visibles", "Les campagnes de production visibles par le commerce", "Planning partagé",
   "Le commercial voit la prochaine campagne et promet une date juste.",
   "Usine de Chevigny · pilotage des lignes, planification et commerce",
   "Le planning des lignes vit hors du CRM : le commerce appelle l'ADV, qui appelle la planification. La date promise au client est prudente plutôt que compétitive.",
   [("Exposer le planning", "MuleSoft publie le planning des lignes et les stocks de l'ERP, sans ressaisie.", "MuleSoft"),
    ("L'afficher sur l'affaire", "Sur chaque opportunité : la prochaine campagne compatible et la quantité disponible.", "Sales Cloud"),
    ("Répondre en langage naturel", "« Quand puis-je livrer 320 m² de plaques translucides ? » : l'agent répond avec la date et ses hypothèses.", "Agentforce")],
   [est("−50 %", "d'appels internes entre commerce, ADV et planification"),
    est("+10 pts", "de promesses de livraison tenues")],
   ["Planificateur de production", "Technico-commercial", "Assistante ADV"],
   ["MuleSoft", "Sales Cloud", "Agentforce"], ["ERP", "MES"],
   [V["road26"], T["mfgql"]], base="Marshall")
uc("usine-voix-client-rd", "Nourrir la R&D avec la voix des clients", "Voix client → R&D",
   "Demandes de profils, coloris et performances, agrégées par marché pour la R&D.",
   "Usine de Chevigny · R&D, formulation et lignes",
   "Les idées de nouveaux produits se perdent dans les comptes rendus de visite et les e-mails. La R&D manque d'une vue chiffrée de la demande, marché par marché.",
   [("Capter les demandes", "Profils, coloris, transmission lumineuse : chaque demande spéciale est saisie sur le compte.", "Sales Cloud"),
    ("Agréger les signaux", "Data 360 rassemble demandes, réclamations et ventes par marché et par application.", "Data 360"),
    ("Résumer les tendances", "Chaque mois, un agent synthétise ce que demandent serristes, éleveurs et négoces.", "Agentforce"),
    ("Arbitrer la feuille de route", "Tableau met en regard la demande, les volumes et les marges par gamme.", "Tableau")],
   [kpi("+111 %", "d'usage de Tableau en un an", "chez Poclain Hydraulics", "poclain"),
    est("−1 mois", "sur le cycle d'étude d'un nouveau produit")],
   ["Responsable R&D", "Chef de produit", "Direction commerciale"],
   ["Sales Cloud", "Data 360", "Agentforce", "Tableau"], ["PLM et formulation", "ERP"],
   [S["poclain"], V["diff25"], T["d360"]])
# --- Stock et expéditions
uc("entrepot-commande-directe", "De la commande signée à l'ERP, sans ressaisie", "Zéro ressaisie",
   "Le devis accepté devient commande ERP et ordre de préparation.",
   "Stock et expéditions · ADV, préparation et chargement",
   "Ressaisir chaque commande dans l'ERP prend du temps et crée des erreurs de référence ou de quantité. En pleine saison, l'ADV devient le goulot d'étranglement.",
   [("Convertir le devis", "Le devis accepté devient commande, avec ses conditions et son adresse de livraison.", "Revenue Cloud"),
    ("Transmettre à l'ERP", "MuleSoft crée la commande et l'ordre de préparation dans l'ERP.", "MuleSoft"),
    ("Confirmer au client", "Un agent envoie l'accusé de réception et la date d'expédition prévue.", "Agentforce")],
   [est("−60 %", "de temps de saisie par commande"),
    kpi("Fin", "de la double saisie vers l'ERP", "chez Air Liquide et Poclain", "airliquide")],
   ["Assistante ADV", "Responsable logistique", "Préparateur de commandes"],
   ["Revenue Cloud", "MuleSoft", "Agentforce"], ["ERP", "Gestion d'entrepôt"],
   [S["airliquide"], T["rev"]], base="Marshall")
uc("entrepot-suivi-livraison", "Livraisons suivies, réserves traitées en un écran", "Livraison suivie",
   "Statut, réserves transporteur et réexpédition visibles par le client et l'ADV.",
   "Stock et expéditions · quais, transporteurs et clients livrés",
   "Des plaques abîmées au transport déclenchent appels et recherches dans plusieurs outils. Pendant ce temps, le client attend, et son chantier aussi.",
   [("Synchroniser les expéditions", "MuleSoft remonte les statuts du transporteur et les bons de livraison.", "MuleSoft"),
    ("Déclarer une réserve", "Le client signale une casse avec photos depuis son espace en ligne.", "Experience Cloud"),
    ("Traiter vite", "Le dossier déclenche réexpédition ou avoir, avec le lot et le transporteur concernés.", "Service Cloud"),
    ("Prévenir avant l'appel", "Un agent informe le client d'un retard et propose un nouveau créneau.", "Agentforce")],
   [kpi("80 %", "des problèmes résolus en libre-service", "chez Fisher & Paykel", "fisher"),
    est("−40 %", "d'appels « où en est ma commande ? »")],
   ["Assistante ADV", "Responsable transport", "Acheteur négoce"],
   ["MuleSoft", "Experience Cloud", "Service Cloud", "Agentforce"], ["ERP", "Transporteurs"],
   [S["fisher"], T["af"]], base="Casey")
uc("entrepot-franco-zone", "Le franco de port calculé selon la zone et le volume", "Franco par zone",
   "Les règles de livraison s'appliquent d'elles-mêmes dans le devis.",
   "Stock et expéditions · conditions de transport par zone",
   "Les conditions de livraison varient selon la distance, le volume et le client, et s'appliquent souvent à la main. Chaque écart rogne la marge sans que personne ne le voie.",
   [("Modéliser les règles", "Revenue Cloud porte les règles de franco par zone, volume et type de client.", "Revenue Cloud"),
    ("Situer le chantier", "L'adresse de livraison place le chantier ou le dépôt dans la bonne zone.", "Sales Cloud"),
    ("Valider les exceptions", "Une demande d'approbation part dès qu'un commercial s'écarte de la règle.", "Salesforce Platform")],
   [est("0", "franco accordé hors règle sans validation"),
    kpi("150 000", "références devisées dans Revenue Cloud", "chez Poclain", "airliquide")],
   ["Directeur commercial", "Assistante ADV", "Responsable transport"],
   ["Revenue Cloud", "Sales Cloud", "Salesforce Platform"], ["ERP", "Grilles transporteurs"],
   [S["airliquide"], V["rev26"], T["rev"]])
# --- Export
uc("export-pilotage-pays", "Piloter les distributeurs pays par pays", "Pilotage export",
   "Potentiel, réalisé et activité par pays et par distributeur.",
   "Export · distributeurs et clients en Europe",
   "À l'export, quelques commerciaux couvrent de vastes zones à travers des distributeurs. Sans données partagées, le potentiel de chaque pays reste difficile à voir.",
   [("Unifier comptes et ventes", "Data 360 réunit comptes, commandes de l'ERP et activité commerciale par pays.", "Data 360"),
    ("Prioriser", "Un agent signale les distributeurs en retrait et les comptes à potentiel.", "Agentforce"),
    ("Planifier les visites", "Plans de compte et visites se préparent dans Sales Cloud.", "Sales Cloud"),
    ("Visualiser", "Tableau montre réalisé, potentiel et couverture, pays par pays.", "Tableau")],
   [kpi("1 800", "utilisateurs sur un CRM unique en 16 mois", "chez Etex, matériaux de construction", "etex"),
    est("+10 %", "de chiffre d'affaires export")],
   ["Responsable export", "Area manager", "Distributeur"],
   ["Data 360", "Agentforce", "Sales Cloud", "Tableau"], ["ERP", "Fichiers distributeurs"],
   [S["etex"], S["imerys"], T["mfgsales"]], base="Hunter")
uc("export-sedentaire-ia", "Chaque demande export qualifiée, dans sa langue", "Demandes export",
   "Formulaires et e-mails multilingues triés et traités sans attendre.",
   "Export · demandes entrantes en plusieurs langues",
   "Les demandes hors réseau arrivent par e-mail, dans plusieurs langues et sans qualification. Elles attendent parfois des jours avant d'atteindre la bonne personne.",
   [("Recevoir", "Formulaires du site et e-mails arrivent dans une file unique.", "Service Cloud"),
    ("Qualifier", "Un agent détecte la langue, le besoin, le pays et le distributeur compétent.", "Agentforce"),
    ("Créer l'affaire", "Les demandes sérieuses deviennent des opportunités, routées au bon commercial.", "Sales Cloud")],
   [kpi("2 500", "leads par mois qualifiés par Agentforce", "chez Siemens", "siemens"),
    est("< 1 h", "pour une première réponse")],
   ["Assistante commerciale export", "Responsable export"],
   ["Service Cloud", "Agentforce", "Sales Cloud"], ["Messagerie", "Site web"],
   [S["siemens"], T["af"]], base="Piper")
uc("export-veille-marche", "Une veille marché et concurrence, pays par pays", "Veille pays",
   "Une synthèse ciblée pour chaque commercial, au début de sa journée.",
   "Export · marchés, réglementation et concurrence",
   "Les signaux de marché (chantiers, concurrents, réglementation) arrivent dispersés et en plusieurs langues. On les découvre souvent trop tard pour agir.",
   [("Collecter", "Sources publiques et notes de visite rassemblées par pays.", "Data 360"),
    ("Synthétiser", "Un agent résume ce qui a changé et ce qui concerne chaque compte.", "Agentforce"),
    ("Partager", "La synthèse arrive dans le canal Slack de chaque pays.", "Slack")],
   [est("−2 h", "de veille par semaine et par commercial"),
    est("100 %", "des comptes clés couverts chaque semaine")],
   ["Direction commerciale", "Marketing", "Responsable export"],
   ["Data 360", "Agentforce", "Slack"], ["Sources web", "Notes de visite"],
   [V["pilot26"], T["af"]])
# --- Négoces et GSB
uc("negoce-devis-express", "Un devis en 24 h, avec le stock et la date de production", "Devis express",
   "Configurateur référence → déclinaisons, avec tarif contrat, stock et planning.",
   "Négoces et GSB · demandes de prix des négoces, artisans et intégrateurs",
   "Le prix d'une plaque dépend du profil, de la longueur, du coloris, du contrat et du stock, souvent dispersés entre ERP et tableurs. Le délai de réponse s'allonge et l'affaire refroidit.",
   [("Configurer", "Profil, coloris, longueur et accessoires de fixation, avec le tarif du contrat.", "Revenue Cloud"),
    ("Lire stock et planning", "MuleSoft interroge l'ERP : stock disponible ou prochaine campagne de production.", "MuleSoft"),
    ("Rédiger la proposition", "Un agent prépare le devis et le message d'accompagnement.", "Agentforce"),
    ("Encadrer la marge", "Une remise hors grille part en approbation avant l'envoi.", "Sales Cloud")],
   [kpi("×32", "de productivité dans la création de devis", "chez Imerys", "imerys"),
    kpi("+18 %", "d'offres saisies dans le CRM en un an", "chez Poclain Hydraulics", "poclain"),
    kpi("−75 %", "de temps de devis", "Salesforce, usage interne d'Agentforce for Revenue", "revenue")],
   ["Technico-commercial", "Assistante ADV", "Acheteur négoce"],
   ["Revenue Cloud", "MuleSoft", "Agentforce", "Sales Cloud"], ["ERP", "Tarifs"],
   [S["imerys"], S["poclain"], DOC_REV, V["rev26"], T["rev"]], base="Marshall")
uc("negoce-portail-b2b", "Un espace en ligne pour commander et suivre", "Portail négoces",
   "Réassort, documents techniques, suivi et factures en libre-service.",
   "Négoces et GSB · réassort des dépôts et des magasins",
   "Quand l'espace client est peu pratique, les distributeurs reviennent au téléphone et à l'e-mail. Chaque commande passe alors par l'ADV, même la plus simple.",
   [("Ouvrir le catalogue", "Références, prix contractuels et disponibilités dans une boutique B2B.", "Commerce Cloud"),
    ("Documenter", "Fiches techniques, notices de pose et avis techniques au même endroit.", "Experience Cloud"),
    ("Assister la commande", "Un agent aide à composer la commande et répond sur les délais.", "Agentforce")],
   [kpi("90 %", "des commandes passées via Salesforce", "chez JK Cement", "jkcement"),
    kpi("1,4 M", "d'utilisateurs enregistrés sur le portail", "chez Siemens (SiePortal)", "siemens")],
   ["Acheteur négoce", "Chef de rayon", "Assistante ADV"],
   ["Commerce Cloud", "Experience Cloud", "Agentforce"], ["ERP", "Documents techniques"],
   [S["jkcement"], S["siemens"], V["diff25"]], base="Carter")
uc("negoce-accords-cadres", "Accords-cadres et remises de fin d'année pilotés", "Accords et RFA",
   "Engagements de volume suivis au fil de l'eau, enseigne par enseigne.",
   "Négoces et GSB · accords nationaux avec les enseignes et les négoces",
   "Les remises par palier se calculent souvent en fin d'année, trop tard pour agir. En cours d'année, personne ne voit qui atteindra son palier.",
   [("Contractualiser", "Volumes, paliers et prix de chaque accord dans des accords de vente.", "Manufacturing Cloud"),
    ("Mesurer le réalisé", "MuleSoft remonte les ventes de l'ERP face à chaque engagement.", "MuleSoft"),
    ("Alerter", "Un agent signale les écarts au palier et propose l'action commerciale.", "Agentforce")],
   [kpi("+80 M€", "de ventes croisées en un an", "chez Imerys, avec Manufacturing Cloud", "imerys"),
    est("−50 %", "de temps de calcul des remises de fin d'année")],
   ["Responsable grands comptes", "Contrôleur de gestion", "Chef de marché GSB"],
   ["Manufacturing Cloud", "MuleSoft", "Agentforce"], ["ERP", "EDI enseignes"],
   [S["imerys"], V["mfg26"], T["mfgsales"]])
# --- Chantiers et poseurs
uc("chantier-visite-mobile", "Compte rendu de visite dicté, résumé, suivi", "Visite mobile",
   "Le commercial dicte sur le chantier ; l'IA résume et propose les suites.",
   "Chantiers et poseurs · visites des technico-commerciaux",
   "Sur le chantier, on note sur un carnet et l'on saisit plus tard, ou jamais. Sans mémoire partagée, le pilotage commercial avance à l'aveugle.",
   [("Préparer la visite", "Un agent prépare le brief : historique, devis ouverts, réclamations.", "Agentforce"),
    ("Saisir sur place", "Le compte rendu se dicte sur le mobile, même sans réseau.", "Sales Cloud"),
    ("Enchaîner les suites", "Le résumé crée les tâches, le devis à préparer et les relances.", "Agentforce")],
   [kpi("> 90 %", "de connexion des utilisateurs au CRM", "chez Poclain Hydraulics", "poclain"),
    est("−20 min", "de préparation par visite")],
   ["Technico-commercial", "Directeur commercial"],
   ["Agentforce", "Sales Cloud"], ["Agenda et messagerie"],
   [S["poclain"], S["schneider"], T["mfgsales"]], base="Hunter")
uc("chantier-prescription", "De la prescription au chantier gagné", "Prescription suivie",
   "Un projet, plusieurs devis : on suit l'architecte jusqu'à la pose.",
   "Chantiers et poseurs · architectes, bureaux d'études et installateurs",
   "Un même projet est souvent chiffré par plusieurs installateurs à partir d'une seule prescription. Sans vue par chantier, on perd la trace du devis gagnant.",
   [("Créer le projet", "Le chantier, le prescripteur et les installateurs consultés sont reliés.", "Sales Cloud"),
    ("Relier les devis", "Chaque devis d'installateur est rattaché au même projet.", "Revenue Cloud"),
    ("Repérer les projets", "Un agent signale les chantiers à suivre dans chaque secteur.", "Agentforce")],
   [kpi("500", "opportunités par jour, au lieu de trois semaines de travail", "chez Schneider Electric", "schneider"),
    est("+20 %", "de prescriptions converties en commandes")],
   ["Prescripteur", "Technico-commercial", "Bureau d'études"],
   ["Sales Cloud", "Revenue Cloud", "Agentforce"], ["Sources chantiers"],
   [S["schneider"], T["mfgsales"]], base="Hunter")
uc("chantier-assistance-pose", "La bonne réponse de pose, au bon moment", "Aide à la pose",
   "Entraxes, fixations, pentes : des réponses tirées des notices officielles.",
   "Chantiers et poseurs · couvreurs et charpentiers sur le toit",
   "Une erreur de pose (entraxe, fixation, stockage au soleil) devient vite une réclamation. Les poseurs ont besoin d'une réponse sûre, sur place.",
   [("Centraliser les notices", "Notices, avis techniques et règles de pose dans une base de connaissances.", "Service Cloud"),
    ("Répondre sur le toit", "Un agent répond sur mobile et sur le site, en citant la notice.", "Agentforce"),
    ("Passer la main", "Les cas complexes arrivent à l'expert technique, avec photos et contexte.", "Service Cloud")],
   [kpi("50 %", "des demandes traitées en autonomie (objectif)", "chez Endress+Hauser", "endress"),
    est("−25 %", "de réclamations liées à la pose")],
   ["Couvreur", "Charpentier", "Responsable technique"],
   ["Service Cloud", "Agentforce"], ["Notices et avis techniques"],
   [S["endress"], T["af"]], base="Casey")
# --- Élevages et serres
uc("agri-conseil-lumiere", "« Quelle plaque pour ma serre ? » : un conseil 24 h/24", "Conseil serre",
   "Un agent recommande la gamme BIO, la nuance et le profil.",
   "Élevages et serres · serristes, jardineries et maraîchers",
   "Le choix dépend de la culture, de la lumière et du climat, et les questions arrivent souvent hors des heures de bureau. Le responsable technique est sollicité pour des questions simples.",
   [("Indexer les données", "Fiches techniques et données optiques mesurées en laboratoire, prêtes à être citées.", "Data 360"),
    ("Conseiller en ligne", "Sur le site, un agent recommande gamme, nuance et profil selon la culture.", "Agentforce"),
    ("Transmettre le projet", "Le projet qualifié arrive chez le commercial du secteur.", "Sales Cloud")],
   [est("−40 %", "de sollicitations techniques simples"),
    est("+15 %", "de demandes de serristes converties en projets")],
   ["Serriste", "Gérant de jardinerie", "Responsable technique"],
   ["Data 360", "Agentforce", "Sales Cloud"], ["Site web", "Fiches techniques"],
   [S["endress"], V["diff25"], T["af"]], base="Casey")
uc("agri-avant-saison", "Préparer la saison des bâtiments d'élevage", "Avant-saison",
   "Des campagnes ciblées par filière et par région, avant le pic de demande.",
   "Élevages et serres · rénovation des bâtiments d'élevage",
   "Les exploitants rénovent leurs bâtiments sur une fenêtre courte et la demande arrive d'un coup. Anticiper évite les ruptures et les délais qui s'allongent.",
   [("Prévoir", "Data 360 croise l'historique de commandes, les régions et les filières.", "Data 360"),
    ("Cibler", "Des campagnes vers les exploitations susceptibles de rénover avant la saison.", "Marketing Cloud"),
    ("Partager la prévision", "L'usine voit la demande attendue par gamme et ajuste ses campagnes.", "Tableau")],
   [kpi("×6", "de messages marketing en deux fois moins de temps", "chez JK Cement", "jkcement"),
    est("−20 %", "de ruptures en haute saison")],
   ["Responsable marketing", "Chef de marché agricole", "Planificateur"],
   ["Data 360", "Marketing Cloud", "Tableau"], ["ERP", "Boutique en ligne"],
   [S["jkcement"], V["mfg26"], T["d360"]])
uc("agri-salons-affaires", "Des salons agricoles aux affaires suivies", "Salon → affaire",
   "Chaque contact de salon est qualifié, routé et relancé.",
   "Élevages et serres · salons professionnels de l'élevage et du végétal",
   "Les contacts de salon restent souvent dans des carnets ou des tableurs. Sans relance rapide, l'intérêt retombe.",
   [("Capter", "Badges et formulaires de salon arrivent directement dans le CRM.", "Marketing Cloud"),
    ("Qualifier", "Un agent évalue le projet, relance et propose un rendez-vous.", "Agentforce"),
    ("Router", "Les projets qualifiés vont au commercial du secteur.", "Sales Cloud")],
   [kpi("Minutes", "pour répondre à un lead, au lieu de jours", "chez Siemens", "siemens"),
    est("+25 %", "de contacts de salon convertis en rendez-vous")],
   ["Responsable marketing", "Commercial secteur", "Éleveur ou serriste"],
   ["Marketing Cloud", "Agentforce", "Sales Cloud"], ["Fichiers salons", "Site web"],
   [S["siemens"], T["af"]], base="Piper")
# --- ONDEX SOLAR
uc("solaire-projet-pv", "Chiffrer un projet FIX O Bat ou FIX O Ser", "Projet PV chiffré",
   "Plaques, fixations et accessoires configurés selon la toiture.",
   "ONDEX SOLAR · toitures agricoles, industrielles et serres",
   "Un projet photovoltaïque mêle plaques, fixations et contraintes de charpente. Chiffré à la main, il prend du temps et se compare mal.",
   [("Qualifier la toiture", "Surface, pente, charpente existante et type de bâtiment sur l'affaire.", "Sales Cloud"),
    ("Configurer le kit", "Plaques, système de fixation et accessoires calculés automatiquement.", "Revenue Cloud"),
    ("Proposer", "Un agent assemble la proposition et les documents techniques.", "Agentforce")],
   [kpi("−75 %", "de temps de devis", "Salesforce, usage interne d'Agentforce for Revenue", "revenue"),
    est("+25 %", "de projets chiffrés par commercial")],
   ["Installateur photovoltaïque", "Bureau d'études", "Chef de marché solaire"],
   ["Sales Cloud", "Revenue Cloud", "Agentforce"], ["ERP", "Fiches techniques"],
   [DOC_REV, V["rev26"], T["rev"]])
uc("solaire-academie", "Former et certifier les installateurs", "Académie de pose",
   "Inscriptions, sessions et certifications suivies par installateur.",
   "ONDEX SOLAR · installateurs partenaires",
   "Une pose en surimposition demande un savoir-faire précis. Il faut savoir qui est formé avant de lui confier un chantier.",
   [("Inscrire", "Les installateurs s'inscrivent aux sessions depuis leur espace partenaire.", "Experience Cloud"),
    ("Certifier", "Le statut de certification s'affiche sur le compte du partenaire.", "Sales Cloud"),
    ("Relancer", "Rappels de recyclage et nouveautés produit envoyés au bon moment.", "Marketing Cloud")],
   [est("100 %", "des chantiers confiés à des poseurs formés"),
    est("−50 %", "de gestion administrative des formations")],
   ["Formateur", "Installateur partenaire", "Chef de marché solaire"],
   ["Experience Cloud", "Sales Cloud", "Marketing Cloud"], ["Outil de formation"],
   [T["prm"], T["af"]])
uc("solaire-reseau-installateurs", "Un réseau d'installateurs partenaires", "Réseau PV",
   "Annuaire, leads partagés et documents pour les partenaires solaires.",
   "ONDEX SOLAR · installateurs spécialisés",
   "Une nouvelle solution a besoin d'installateurs actifs et bien équipés. Sans espace partagé, les leads et les retours du terrain se perdent.",
   [("Ouvrir l'espace partenaires", "Documents, argumentaires et suivi des projets en un seul endroit.", "Experience Cloud"),
    ("Distribuer les leads", "Les demandes sont attribuées à l'installateur le plus proche.", "Sales Cloud"),
    ("Animer la communauté", "Questions, retours de chantier et nouveautés dans un canal Slack partagé.", "Slack")],
   [kpi("10 000", "partenaires de distribution actifs sur la plateforme", "chez JK Cement", "jkcement"),
    est("30", "installateurs actifs la première année")],
   ["Installateur partenaire", "Chef de marché solaire"],
   ["Experience Cloud", "Sales Cloud", "Slack"], ["Annuaire partenaires"],
   [S["jkcement"], T["prm"]])
# --- Siège et service client
uc("siege-reclamations-360", "Des réclamations tracées, relancées, soldées", "SAV 360",
   "Dossiers liés, délais suivis, avoir ou relivraison sur un seul écran.",
   "Siège · ADV et service après-vente",
   "Peu nombreuses mais lourdes, les réclamations s'égarent facilement entre e-mails et tableurs. Le client ne sait pas où en est sa demande.",
   [("Ouvrir le dossier", "E-mail, téléphone ou portail : un dossier unique, rattaché au client et à la commande.", "Service Cloud"),
    ("Orchestrer", "Dossiers parent et enfant, délais et relances automatiques.", "Service Cloud"),
    ("Résumer", "Un agent résume l'historique et propose la solution : avoir ou relivraison.", "Agentforce")],
   [kpi("75 %", "d'avis positifs des conseillers sur leur assistant IA", "chez Fisher & Paykel", "fisher_rep"),
    est("−50 %", "de délai de traitement")],
   ["Assistante ADV", "Responsable qualité", "Client négoce"],
   ["Service Cloud", "Agentforce"], ["ERP", "Messagerie"],
   [S["fisher"], T["af"]], base="Fin")
uc("siege-marge-pilotage", "La marge visible par client et par gamme", "Marge pilotée",
   "Prix, remises et marge visibles dès le devis.",
   "Siège · direction commerciale et contrôle de gestion",
   "On connaît souvent le chiffre d'affaires, mais pas la rentabilité par client ou par gamme. Les remises s'accordent alors sans garde-fou.",
   [("Calculer", "La marge s'affiche sur chaque ligne de devis.", "Revenue Cloud"),
    ("Encadrer", "Les seuils de remise déclenchent une approbation.", "Sales Cloud"),
    ("Analyser", "Tableau croise marge, client, gamme et zone.", "Tableau")],
   [est("+2 pts", "de marge brute"),
    est("−30 %", "de remises hors grille")],
   ["Directeur commercial", "Contrôleur de gestion", "Direction générale"],
   ["Revenue Cloud", "Sales Cloud", "Tableau"], ["ERP", "Tableaux de bord"],
   [S["airliquide"], T["rev"]])
uc("siege-comite-lundi", "Le comité commercial du lundi, en direct", "Comité en direct",
   "Affaires en cours, prévisions et signaux de la semaine, sans consolidation manuelle.",
   "Siège · direction et équipes commerciales",
   "Les chiffres des réunions se consolident à la main et datent déjà le jour du comité. Le temps passe à vérifier plutôt qu'à décider.",
   [("Prévoir", "Prévisions et affaires en cours à jour, par commercial et par marché.", "Sales Cloud"),
    ("Synthétiser", "Un agent résume la semaine : affaires gagnées, risques, réclamations.", "Agentforce"),
    ("Partager", "Un tableau de bord unique, ouvert avant la réunion.", "Tableau")],
   [kpi("20 → 1", "rapports remplacés par une seule vue", "chez JK Cement", "jkcement"),
    est("−½ jour", "de préparation par comité")],
   ["Direction générale", "Directeur commercial", "Commerciaux"],
   ["Sales Cloud", "Agentforce", "Tableau"], ["ERP", "Tableaux de bord"],
   [S["jkcement"], V["pilot26"]])

# ---------------------------------------------------------------- stages
ICON_GLOBE = "<path d='M3 12a9 9 0 1 0 18 0 9 9 0 0 0-18 0M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18'/>"
ICON_SUN = "<path d='M12 4V2M12 22v-2M4 12H2M22 12h-2M6.3 6.3 4.9 4.9M19.1 19.1l-1.4-1.4M6.3 17.7l-1.4 1.4M19.1 4.9l-1.4 1.4M8 12a4 4 0 1 0 8 0 4 4 0 0 0-8 0'/>"
ICON_HEADSET = "<path d='M4 13a8 8 0 0 1 16 0v5h-4v-5M4 13v5h4v-5'/>"
def pts(*pairs):
    return [{"anchor": a, "usecase": u} for a, u in pairs]
STAGES = [
 {"id": "usine", "kit": "pvc_plant", "tags": ["production", "planning"], "label": "Usine",
  "eyebrow": "Chevigny-Saint-Sauveur · production", "title": "Extruder, bi-orienter, contrôler",
  "text": "Formulation, coextrusion anti-UV et bi-étirage : chaque plaque naît sur les lignes de Chevigny, près de Dijon, depuis 1965.",
  "fig": {"v": 5, "suf": " ha", "cap": "un site unique : production, R&D et administration", "src": "La Gazette France, 2025"},
  "rows": [["Procédé", "bi-orientation, inventée et brevetée en 1964"], ["Savoir-faire", "coextrusion anti-UV, formulations mises au point sur site"]],
  "signs": {"plant": "USINE DE CHEVIGNY", "office": "ADV · SERVICE CLIENT"},
  "points": pts(("line", "usine-voix-client-rd"), ("control", "usine-campagnes-visibles"), ("lab", "usine-reclamation-lot")),
  "shot": {"cuts": "used"}},
 {"id": "stock", "kit": "pvc_stock", "tags": ["logistics"], "label": "Stock et expéditions",
  "eyebrow": "Logistique · Chevigny", "title": "Le bon lot, dans le bon camion",
  "text": "Plaques ondulées et planes, pièces spéciales et accessoires sont préparés, chargés et expédiés vers les négoces, les chantiers et l'export.",
  "fig": {"v": 16, "cap": "gammes au catalogue, d'ONDEX HR à ONDEX SOLAR", "src": "ondex.com, 2026"},
  "rows": [["Applications", "bâtiment, agriculture, serres, protection, photovoltaïque, bricolage"]],
  "signs": {"plant": "STOCK ET EXPÉDITIONS"},
  "points": pts(("forklifts", "entrepot-commande-directe"), ("docks", "entrepot-suivi-livraison"), ("yard", "entrepot-franco-zone"))},
 {"id": "export", "same_as": "stock", "tags": ["b2b_customers", "partners"], "label": "Export", "icon": ICON_GLOBE,
  "eyebrow": "Export · Europe", "title": "Grandir à l'export, pays par pays",
  "text": "Distributeurs et clients en Europe : depuis Chevigny, chaque marché se développe avec son réseau de distribution.",
  "fig": {"v": 24, "cap": "pays où opère le groupe AIAC, actionnaire d'ONDEX depuis 2025", "src": "AIAC, 2025"},
  "rows": [["Marchés", "bâtiment, stades, serres, élevages, logistique, bricolage"], ["Site web", "en français, anglais et allemand"]],
  "points": pts(("depart", "export-pilotage-pays"), ("office", "export-sedentaire-ia"), ("loading", "export-veille-marche"))},
 {"id": "negoce", "kit": "negoce", "tags": ["retail_network", "b2b_customers"], "label": "Négoces et GSB",
  "eyebrow": "Distribution · négoces et bricolage", "title": "Le réseau qui revend chaque plaque",
  "text": "Négoces de matériaux et enseignes de bricolage : là où artisans et particuliers trouvent les plaques ONDEX.",
  "fig": {"v": 6, "cap": "domaines d'application, du bâtiment au bricolage", "src": "ondex.com, 2026"},
  "rows": [["Canaux", "négoces de matériaux · grandes surfaces de bricolage"]],
  "signs": {"gsb": "BRICOLAGE", "negoce": "NÉGOCE MATÉRIAUX"},
  "points": pts(("rayon", "negoce-accords-cadres"), ("comptoir", "negoce-devis-express"), ("yard", "negoce-portail-b2b"))},
 {"id": "chantier", "kit": "chantier", "tags": ["field_service", "partners"], "label": "Chantiers et poseurs",
  "eyebrow": "Terrain · couvreurs et prescripteurs", "title": "Bien prescrit, bien posé",
  "text": "Charpentiers, couvreurs et bureaux d'études choisissent et posent les plaques ; le technico-commercial les accompagne, du devis à la pose.",
  "fig": {"v": 4, "pre": "×", "cap": "résistance plus de 4 fois supérieure à celle du PVC non bi-orienté", "src": "ondex.com, 2026"},
  "rows": [["Poids", "2,4 kg/m², contre 7 pour l'acier et 12 pour le fibrociment"]],
  "signs": {"site": "CHANTIER"},
  "points": pts(("rep", "chantier-visite-mobile"), ("hut", "chantier-prescription"), ("roofers", "chantier-assistance-pose"))},
 {"id": "agri", "kit": "agri_serres", "tags": ["b2b_customers", "consumers"], "label": "Élevages et serres",
  "eyebrow": "Agriculture · élevage et maraîchage", "title": "La lumière juste, pour chaque culture",
  "text": "Bâtiments d'élevage, serres et jardineries : plaques translucides, faîtages éclairants et brise-vent font entrer la lumière et l'air.",
  "fig": {"v": 100, "suf": " %", "cap": "de lumière diffusée par la nouvelle plaque translucide DIFFU100", "src": "ondex.com, 2026"},
  "rows": [["Serres", "ONDEX BIO 1, 2 et 3 · 4 nuances, du cristal à l'opaque"], ["Élevage", "lanterneaux, PERFOLUX, PERFO2"]],
  "points": pts(("cultures", "agri-conseil-lumiere"), ("herd", "agri-avant-saison"), ("cour", "agri-salons-affaires")),
  "shot": {"cuts": "used"}},
 {"id": "solaire", "same_as": "agri", "tags": ["partners"], "label": "ONDEX SOLAR", "icon": ICON_SUN,
  "eyebrow": "Photovoltaïque en surimposition", "title": "Le solaire sur les toitures existantes",
  "text": "FIX O Bat pour le bâtiment, FIX O Ser pour la serre : des panneaux posés sur plaques ONDEX, en neuf comme en rénovation, en conservant la charpente.",
  "fig": {"v": 2.4, "suf": " kg/m²", "cap": "pour la plaque, contre jusqu'à 17 kg/m² pour le fibrociment", "src": "ONDEX, communiqué ONDEX SOLAR"},
  "rows": [["Certification", "ETN"], ["Partenaires", "installateurs spécialisés"]],
  "points": pts(("pv", "solaire-projet-pv"), ("installer", "solaire-academie"), ("scaffold", "solaire-reseau-installateurs")),
  "shot": {"cuts": "used"}},
 {"id": "siege", "same_as": "usine", "tags": ["contact_center", "planning"], "label": "Siège · service client", "icon": ICON_HEADSET,
  "eyebrow": "Chevigny · ADV, SAV et direction", "title": "Chaque client suivi, chaque marge visible",
  "text": "Administration des ventes, service après-vente, marketing et direction commerciale travaillent sur le même site que l'usine.",
  "fig": {"v": 100, "pre": "~", "cap": "collaborateurs à Chevigny-Saint-Sauveur", "src": "La Gazette France, 2025"},
  "rows": [["Depuis", "1965 · ONDEX SAS depuis 2025"]],
  "points": pts(("adv", "siege-reclamations-360"), ("direction", "siege-marge-pilotage"), ("meeting", "siege-comite-lundi")),
  "shot": {"cuts": "used"}},
]

# ---------------------------------------------------------------- UI (fr)
UI = {
 "start": "DÉPART", "summary": "VUE D'ENSEMBLE", "stage": "Front", "overview": "Vue complète", "all": "Tout",
 "cta": "Parcourir l'opération", "back": "Retour au début", "wheel": "ou utilisez la molette", "glance": "En bref",
 "ucs": "Cas d'usage", "tabs": ["Adaptation", "Architecture", "Ressources"], "where": "Chez",
 "challenge": "Le défi aujourd'hui", "how": "La solution", "impact": "Indicateurs visés", "who": "Qui l'utilise",
 "steps": "Étape par étape", "allConnected": "Tout est connecté", "allText": "Un seul flux, de bout en bout.",
 "videos": "À voir", "more": "Autres ressources", "stories": "Témoignages clients", "readStory": "Lire le témoignage",
 "lySys": "Systèmes {client}", "lyGuard": "Salesforce Guardian · droits d'accès et Zero Data Retention",
 "archCap": "Les mêmes couches que le QG numérique : des systèmes {client} jusqu'à la réponse, sur Salesforce Guardian.",
 "watch": "Voir sur", "open": "Ouvrir", "close": "Fermer", "prev": "Cas d'usage précédent", "next": "Cas d'usage suivant",
 "estimate": "estimation", "source": "Source ", "goTo": "Aller à", "explore": "Explorer le cas d'usage",
 "meta": "{n} fronts · {m} cas d'usage", "world": "Visite animée de l'opération", "theme": "Changer de thème",
 "auto": "Visite automatique (touche P)",
 "logotip": "Pour voir le logo sur les camions et les enseignes : déposez le fichier officiel (PNG ou SVG) sur la page, ou appuyez sur L.",
 "noRes": "Les ressources de ce cas d'usage arrivent bientôt.", "milestone": "Premier jalon réaliste", "proof": "Preuves dans l'industrie",
 "story": "Voir la feuille de route", "storyBack": "Retour à la visite 3D", "open3d": "Voir en 3D",
 "inCases": "dans {n} cas d'usage", "inCase": "dans 1 cas d'usage", "flip": "Résumé", "watchOn": "Voir sur",
 "uDown": "QG numérique", "uUp": "Retour à l'opération", "uLayer": "couche agentique", "uAgents": "Agents", "uAgent": "Agent",
 "uBase": "Basé sur", "uNone": "Pas encore d'agent pour ce front.", "presenter": "Votre contact Salesforce", "credit": "Template élaboré par",
 "estimateAll": "Estimations d'ordre de grandeur pour dimensionner la conversation : les objectifs se fixent sur la base réelle d'ONDEX.",
 "slab": {"statement": "Vision", "numbers": "En chiffres", "floaters": "Aujourd'hui", "phases": "Séquence", "groups": "Point de départ",
          "catalog": "Catalogue", "reel": "Vidéos", "panel": "Détail", "closing": "Prochaines étapes"},
}

# ---------------------------------------------------------------- Digital HQ copy (fr translation of the built-in copy)
HQ = {
 "dock": {"l0": "Guardian", "l1": "Data 360", "l2": "Customer 360", "l3": "Agentforce", "l4": "AIforce", "all": "Tout"},
 "dockT": {"l0": "Salesforce Guardian avec Zero Data Retention", "l1": "Data 360 · Intégration, fédération et harmonisation",
           "l2": "Customer 360 · Applications, sémantique et intelligence des processus", "l3": "Agentforce · Main-d'œuvre numérique",
           "l4": "AIforce · Interface en direct", "all": "Salesforce, moteur de la révolution agentique"},
 "face": {"l0": ["Salesforce Guardian", "avec Zero Data Retention"], "l1": ["Data 360", "Intégration, fédération et harmonisation"],
          "l2": ["Customer 360", "Applications, sémantique et processus"], "l3": ["Agentforce", "Main-d'œuvre numérique"],
          "l4": ["AIforce", "Interface en direct"]},
 "legend": {"gold": "Les données d'{client} : elles restent dans le périmètre de confiance",
            "white": "Vers le modèle : juste ce qu'il faut pour répondre, sans conservation"},
 "steps": {
  "intro": {"eyebrow": "Sous l'opération", "title": "Le QG numérique d'{client}",
            "text": "Cinq couches travaillent ensemble pour que chaque question de l'opération reçoive une réponse fiable.",
            "spine": "La question descend de l'opération : « {q} »",
            "rows": [["Couches", "Guardian, Data 360, Customer 360, Agentforce et AIforce"], ["Agents", "{nOwn} agents de l'opération et {nJobLit} prêts à l'emploi"]],
            "cta": "Commencer par la base"},
  "l0": {"title": "La confiance comme fondation",
         "text": "Les données d'{client} restent protégées : chaque agent ne voit que ce que son utilisateur peut voir, et le modèle n'en conserve rien.",
         "spine": "La question arrive avec les droits du commercial : il ne voit que ce qu'il peut voir.",
         "rows": [["Modèles", "Anthropic, AWS, Google, NVIDIA, OpenAI et Salesforce"], ["Règle", "Un agent ne voit que ce que voit la personne qui demande"]]},
  "l1": {"title": "Un contexte qui comprend le métier",
         "text": "Une seule vue de l'activité, avec des données connectées là où elles vivent déjà.",
         "spine": "Stocks et commandes de l'ERP arrivent intégrés ; les zones de livraison, fédérées.",
         "rows": [["Intégrés", "{intHubs}"], ["Fédérés (Zero Copy)", "{fedHubs}"]]},
  "l2": {"title": "Là où vivent les règles du métier",
         "text": "Les applications et les règles qui font déjà tourner le travail : personnes et agents suivent le même processus.",
         "spine": "Revenue Cloud applique le tarif du contrat, les remises et les règles de franco.",
         "rows": [["Applications utilisées", "{nLit}"], ["Sémantique", "{objects}"]]},
  "l3": {"title": "Une main-d'œuvre numérique",
         "text": "Un agent sur chaque front, aux côtés des équipes : chacun consacre son temps à ce qui compte le plus.",
         "spine": "Marshall vérifie le stock et le planning des lignes, puis prépare le devis avec l'agent du front.",
         "rows": [["Agents de l'opération", "{nPods}, un par front"], ["Prêts à l'emploi", "{jobsLit}"]]},
  "l4": {"title": "Salesforce là où le travail se fait",
         "text": "Les réponses arrivent dans les outils que l'équipe utilise déjà, avec la même sécurité.",
         "spine": "La réponse arrive dans Slack : le commercial valide la proposition en un clic.",
         "rows": [["Interfaces", "Claude · Slack · Coworker · Mobile"], ["Harnais", "MCP, API, plug-ins et skills"]]},
  "all": {"eyebrow": "Vue d'ensemble", "title": "{client}, une entreprise agentique",
          "text": "Personnes et agents font avancer ensemble la réussite des clients, avec des données unifiées et la confiance Salesforce dans chaque réponse.",
          "close": "Personnes et agents, ensemble.", "follow": "Suivre la question", "chips": "Le parcours d'un cas d'usage",
          "foot": "Certaines fonctionnalités sont en bêta ou seront annoncées plus tard ; périmètre et disponibilité peuvent évoluer."}},
 "hs": {
  "lvlD": ["Sécurité, droits d'accès et Zero Data Retention pour chaque requête.", "Intégration, fédération et harmonisation du contexte.",
           "Applications, sémantique et intelligence des processus.", "Un agent par front, plus des agents prêts à l'emploi.",
           "La plateforme dans toutes les interfaces d'IA."],
  "guardian": {"t": "Salesforce Guardian", "s": "Salesforce Guardian",
               "d": "Chaque requête vers un modèle franchit cette porte de confiance avec les droits existants.",
               "c": "Chez {client} : chaque agent utilise les droits de son utilisateur.",
               "x": "Sécurité et gouvernance sur chaque requête : droits, règles et Zero Data Retention."},
  "gate": {"t": "Porte de confiance", "s": "Porte de confiance", "d": "Chaque requête vers un modèle part d'ici, avec les droits et règles existants."},
  "zdr": {"t": "Zero Data Retention", "s": "Zero Data Retention", "d": "Les données servent à répondre ; le fournisseur du modèle n'en garde rien.",
          "c": "Chez {client} : tarifs, marges et données clients ne sont jamais conservés par le modèle."},
  "models": {"t": "Choix du modèle", "s": "Modèles", "d": "Anthropic, AWS, Google, NVIDIA, OpenAI ou Salesforce : le bon modèle pour chaque tâche."},
  "integration": {"t": "Intégration", "d": "Chaque système se connecte une fois et partage un même contexte fiable.", "c": "Chez {client} : {intHubs}."},
  "federation": {"t": "Fédération (Zero Copy)", "s": "Zero Copy", "d": "Les données restent où elles vivent : ni déplacées, ni copiées.", "c": "Chez {client} : {fedHubs}."},
  "harmonization": {"t": "Harmonisation", "d": "Chaque source est rapprochée d'un modèle commun et d'un profil unifié.",
                    "c": "Chez {client} : un compte, un chantier, une référence, une seule version."},
  "memory": {"t": "Métadonnées et mémoire", "s": "Métadonnées et mémoire", "d": "Ce que signifie chaque donnée, et la mémoire qu'utilisent les agents.",
             "c": "Chez {client} : chaque agent connaît l'historique de chaque compte et de chaque chantier."},
  "semantics": {"t": "Sémantique", "s": "Sémantique", "d": "Les objets métier et leurs relations, avec le même sens pour tous.", "c": "Chez {client} : {objects}."},
  "flows": {"t": "Processus et actions", "s": "Processus et actions", "d": "Processus, droits et actions dont héritent les agents pour faire le travail.",
            "c": "Chez {client} : remises, franco et approbations deviennent des règles."},
  "app": {"c": "Chez {client} : {ucs}."},
  "appN": {"sales": "Ventes", "service": "Service", "field": "Field Service", "marketing": "Marketing", "commerce": "Commerce", "revenue": "Revenue",
           "industries": "Industries", "tableau": "Tableau", "ithr": "IT et RH", "supply": "Supply Chain", "netzero": "Net Zero"},
  "appD": {"sales": "Affaires, opportunités et prévisions au même endroit.", "service": "Des dossiers résolus sur tous les canaux, avec tout le contexte.",
           "field": "Interventions, planification et techniciens mobiles.", "marketing": "Campagnes et parcours, B2B et B2C.",
           "commerce": "Commande en ligne et boutiques, B2B et B2C.", "revenue": "Devis, contrat et facturation en un seul flux.",
           "industries": "Modèles et processus métier, prêts à l'emploi.", "tableau": "Des analyses fiables pour décider.",
           "ithr": "Les demandes des collaborateurs résolues dans Slack et les portails.",
           "supply": "Approvisionnement et back-office de bout en bout, avec Agentforce Operations (Regrello).",
           "netzero": "Empreinte carbone sur les scopes 1, 2 et 3, avec Agentforce Net Zero."},
  "pod": {"t": "Agent {stage}"},
  "ready": {"t": "Agents prêts à l'emploi", "d": "Des agents Agentforce prêts à déployer, par fonction et par secteur.", "c": "Chez {client} : {jobsLit}."},
  "builder": {"t": "Agent Builder", "d": "Tout agent peut être construit, avec les règles et les droits de l'entreprise."},
  "claude": {"t": "Claude", "chip": "beta", "d": "Salesforce dans Claude : un serveur MCP prêt à l'emploi avec 37 compétences commerciales."},
  "slack": {"t": "Slack", "d": "Slackforce : le contexte et les actions Salesforce dans chaque conversation, avec Slackbot.",
            "c": "Chez {client} : commerce, ADV et qualité décident dans Slack, sans changer d'outil."},
  "lightning": {"t": "Agentforce Coworker", "d": "Un coéquipier IA qui travaille à vos côtés et fait appel à vos agents."},
  "toolkit": {"t": "Headless Toolkit", "d": "Architecture ouverte : MCP, API, plug-ins et skills sur toute la plateforme."},
  "informatica": {"t": "Informatica", "d": "Qualité des données : nettoie, fusionne les doublons, garde une seule version de chaque fiche.",
                  "c": "Chez {client} : unifie comptes, contacts et références articles."},
  "tableau": {"t": "Tableau · Knowledge Engine", "d": "Indicateurs, relations et règles reliés : chaque agent répond avec le même sens.",
              "c": "Chez {client} : ventes, marges et réclamations reliées pour répondre en quelques secondes."},
  "fabric": {"t": "MuleSoft Agent Fabric", "d": "Enregistre, orchestre et gouverne chaque agent, Salesforce ou tiers.",
             "c": "Chez {client} : les agents de chaque front et ceux des partenaires, sous les mêmes règles."},
  "mcp": {"t": "MCP · le harnais", "d": "Apporte les données, les droits et les règles Salesforce à toute IA.",
          "c": "Chez {client} : on interroge depuis Slack ou le mobile, sans ouvrir Salesforce.",
          "x": "Le harnais enveloppe l'IA dans le contexte, les règles, les droits et la gouvernance de Salesforce. Grâce à MCP, chaque interface les utilise directement : les administrateurs connectent une fois, sans nouvel identifiant à gérer."},
  "phone": {"t": "Mobile", "s": "Mobile", "d": "Le même agent et la même réponse sur le téléphone, avec les mêmes droits.",
            "c": "Chez {client} : le technico-commercial dicte ses visites et valide ses devis depuis le chantier."},
  "job": {
   "Piper": {"t": "Piper · leads entrants", "role": "Leads entrants", "d": "Travaille le site et la messagerie, et transforme les leads entrants en opportunités.",
             "sayG": "Je travaille le site et la messagerie, et je transforme les leads entrants en opportunités.",
             "c": "Chez {client} : qualifie les demandes du site, des salons et de l'export.",
             "say": "Chez ONDEX, je qualifie les demandes du site, des salons et de l'export, dans leur langue."},
   "Hunter": {"t": "Hunter · vente sortante", "role": "Vente sortante", "d": "Fait avancer les affaires, de la recherche au premier contact, avec les commerciaux.",
              "sayG": "Je fais avancer les affaires, de la recherche au premier contact, avec les commerciaux.",
              "c": "Chez {client} : prépare les visites et repère les chantiers à suivre.",
              "say": "Chez ONDEX, je prépare les visites des technico-commerciaux et je repère les projets à suivre."},
   "Casey": {"t": "Casey · agent d'aide", "role": "Aide client et Field Service", "d": "Répond par voix, SMS, WhatsApp et chat ; planifie les interventions Field Service.",
             "sayG": "Je réponds par la voix, SMS, WhatsApp et chat, et je planifie les interventions Field Service.",
             "c": "Chez {client} : répond aux poseurs et aux serristes, et suit les livraisons.",
             "say": "Chez ONDEX, je réponds aux poseurs et aux serristes, et je préviens les clients d'un retard de livraison."},
   "Fin": {"t": "Fin · agent client", "role": "Expérience client", "d": "Résout les parcours clients complexes sur tous les canaux.",
           "sayG": "Je résous les parcours clients complexes sur tous les canaux.",
           "c": "Chez {client} : mène les réclamations jusqu'à leur solution, sur tous les canaux.",
           "say": "Chez ONDEX, je mène chaque réclamation jusqu'à l'avoir ou la relivraison, sur tous les canaux."},
   "Carter": {"t": "Carter · agent d'achat", "role": "Achat en ligne", "d": "Aide à choisir, répond aux questions et finalise la commande dans le chat.",
              "sayG": "J'aide à choisir, je réponds aux questions et je finalise la commande dans le chat.",
              "c": "Chez {client} : aide les négoces à passer commande en ligne.",
              "say": "Chez ONDEX, j'aide les négoces à composer leur commande en ligne et je réponds sur les délais."},
   "Paige": {"t": "Paige · service IT et RH", "role": "Service IT et RH", "d": "Résout les demandes des collaborateurs dans Slack et les portails.",
             "sayG": "Je résous les demandes des collaborateurs dans Slack et les portails."},
   "Marshall": {"t": "Marshall · supply chain", "role": "Supply chain", "d": "Le super-agent du back-office : exécute chaque processus et trace chaque étape.",
                "sayG": "J'exécute les processus de back-office de bout en bout et je trace chaque étape.",
                "c": "Chez {client} : vérifie stock et planning, transforme les devis en commandes.",
                "say": "Chez ONDEX, je vérifie le stock et le planning des lignes, et je transforme les devis acceptés en commandes."}},
  "own": {
   "usine": {"say": "Je relie réclamations et lots, je partage le planning des lignes et j'aide l'ADV et la direction à suivre clients et marges."},
   "stock": {"say": "Je transforme les devis en commandes, je suis chaque livraison et j'aide l'équipe export à piloter chaque pays."},
   "negoce": {"say": "Je prépare les devis avec le stock et le planning, j'ouvre l'espace de commande et je suis chaque accord-cadre."},
   "chantier": {"say": "Je prépare les visites, je suis les prescriptions jusqu'au chantier et je réponds aux poseurs sur le toit."},
   "agri": {"say": "Je conseille serristes et éleveurs, je relance les contacts de salon et j'accompagne les projets ONDEX SOLAR."}},
  "hub": {"c": "Chez {client} : {stage} · {mode}."},
  "hubT": {"iot": "Lignes d'extrusion : cadences, lots et état des équipements.", "erp": "Commandes, stocks, tarifs et planning.",
           "gis": "Zones de livraison, distances et franco.", "billing": "Factures, avoirs et documents.",
           "contact": "Téléphone et e-mails des clients.", "hr": "Collaborateurs, dossiers, accès et demandes internes.",
           "lake": "Contrôles qualité et indicateurs historiques."},
  "hubN": {"iot": "MES", "erp": "ERP", "gis": "SIG", "billing": "Facturation", "contact": "Centre de contact", "hr": "RH", "lake": "Lac de données"},
  "modeN": {"integrated": "intégré", "federated": "fédéré (Zero Copy)"}},
 "chip": {"beta": "Bêta", "pilot": "Pilote"},
 "lab": {"integration": "Intégration", "federation": "Fédération · Zero Copy", "harmonization": "Harmonisation", "memory": "Métadonnées et mémoire",
         "apps": "Applications", "semantics": "Sémantique", "flows": "Processus et actions", "pods": "Un agent par front de l'opération",
         "own": "Agents de l'opération", "ready": "Prêts à l'emploi", "builder": "Tout agent peut être construit", "ops": "Opérations",
         "usesApps": "Applications utilisées", "toolkit": "Headless Toolkit",
         "port": {"mcp": "MCP", "api": "API", "plugins": "Plug-ins", "skills": "Skills"},
         "screen": {"claude": "Claude · Salesforce dans Claude", "slack": "Slack · Slackforce", "lightning": "Agentforce Coworker", "phone": "Mobile"}},
 "spine": {"marks": ["Systèmes {qStage}", "Intégration", "Harmonisation", "{qApp}", "{qAgent}", "Porte de confiance",
                     "{qModel} : juste ce qu'il faut, sans conservation", "{qScreen}"],
           "back": "La réponse revient comme nouveau contexte"},
 "screenUI": {"ask": "Question", "answer": "Réponse en direct", "confirm": "Confirmer", "channel": "# commerce", "mobile": "Agentforce"},
 "chatUI": {"hiJob": "Bonjour ! Je suis {name}, un agent Agentforce prêt à l'emploi.", "hiOwn": "Bonjour ! Je suis l'agent {stage} d'{client}.",
            "ownRole": "Conçu avec Agentforce pour {client}", "ownDo": "Voici ce dont je m'occupe dans l'opération :",
            "jobUC": "J'aide sur ces cas d'usage :", "now": "En ce moment"},
 "ops": {"face": ["Operation 360", "Applications, sémantique et processus"], "dock": "Operation 360",
         "dockT": "Operation 360 · Applications, sémantique et intelligence des processus",
         "lvlD": "Les applications, la sémantique et les processus de l'opération.",
         "l2": {"title": "Là où vivent les règles de l'opération",
                "text": "Les processus qui font déjà tourner le terrain, l'approvisionnement et les actifs : personnes et agents suivent le même chemin."}},
}

UNDER = {
 "hubs": [{"type": "erp", "label": "ERP et stocks", "stage": "stock", "mode": "integrated"},
          {"type": "iot", "label": "MES des lignes", "stage": "usine", "mode": "integrated"},
          {"type": "contact", "label": "Téléphone et e-mail", "stage": "siege", "mode": "integrated"},
          {"type": "billing", "label": "Facturation et GED", "stage": "siege", "mode": "integrated"},
          {"type": "lake", "label": "Qualité et indicateurs", "stage": "usine", "mode": "federated"},
          {"type": "gis", "label": "Zones de livraison", "stage": "stock", "mode": "federated"}],
 "question": {"text": "Peut-on livrer ce chantier avant le 20 juillet, au bon prix et avec notre marge ?",
              "usecase": "negoce-devis-express", "hub": "erp", "island": "revenue", "screen": "slackforce"},
 "objects": ["Compte", "Distributeur", "Chantier", "Devis", "Commande", "Référence", "Lot de production", "Réclamation", "Livraison", "Accord-cadre"],
 "agents": [],
 "copy": HQ,
}
for sid in [s for s in STAGES]:
    for p in sid["points"]:
        u = p["usecase"]
        a = {"usecase": u, "stage": sid["id"]}
        if UC[u]["_base"]:
            a["base"] = UC[u]["_base"]
        UNDER["agents"].append(a)
for u in UC.values():
    u.pop("_base", None)

# ---------------------------------------------------------------- story (roadmap)
STORY = {"label": "Feuille de route", "sections": [
 {"type": "statement", "label": "Vision",
  "eyebrow": "Usine · Stock · Export · Négoces · Chantiers · Élevages et serres · Solaire · Siège",
  "text": "Chaque plaque, de l'usine au chantier.", "muted": "Un agent aux côtés de chaque équipe.",
  "lead": "Agentforce sur Data 360 relie l'usine de Chevigny, le stock, l'export, les négoces, les chantiers et les exploitations : les devis partent plus vite, les réclamations remontent au lot, les poseurs trouvent la bonne réponse et chaque marché se pilote avec les mêmes données. Les équipes gardent ce qui demande du jugement et de la relation."},
 {"type": "numbers", "label": "En chiffres", "items": [
   {"text": "1965", "label": "lancement de l'extrusion à Chevigny", "src": "ondex.com"},
   {"v": 5, "suf": " ha", "label": "de site : production, R&D et administration", "src": "La Gazette France, 2025"},
   {"v": 100, "pre": "~", "label": "collaborateurs", "src": "La Gazette France, 2025"},
   {"v": 16, "label": "gammes au catalogue", "src": "ondex.com"},
   {"v": "auto:usecases", "label": "cas d'usage identifiés"}]},
 {"type": "phases", "label": "Séquence", "word": "Trois étapes", "eyebrow": "Séquence",
  "title": "Dans quel ordre, et ce que chaque étape rend possible",
  "text": "Commencer là où le commerce et l'ADV le ressentent chaque jour, relier ensuite l'usine et le stock, puis ouvrir le réseau aux négoces, aux installateurs et à l'export.",
  "items": [
   {"phase": 1, "title": "Le cœur commercial", "text": "Devis configurés, comptes rendus de visite, réclamations tracées et pilotage hebdomadaire.",
    "note": "**Rend possible :** des données commerciales fiables, partagées par tous.",
    "usecases": ["negoce-devis-express", "chantier-visite-mobile", "siege-reclamations-360", "siege-comite-lundi"]},
   {"phase": 2, "title": "Relier l'usine et le stock", "text": "Commandes sans ressaisie, planning visible, réclamations rattachées au lot et marge pilotée.",
    "note": "**S'appuie sur :** l'intégration de l'ERP et du MES.",
    "usecases": ["entrepot-commande-directe", "usine-campagnes-visibles", "usine-reclamation-lot", "siege-marge-pilotage"]},
   {"phase": 3, "title": "Ouvrir le réseau", "text": "Espace négoces, réseau d'installateurs ONDEX SOLAR, conseil serre en ligne et pilotage export.",
    "note": "**S'appuie sur :** un catalogue et des données client uniques.",
    "usecases": ["negoce-portail-b2b", "solaire-reseau-installateurs", "agri-conseil-lumiere", "export-pilotage-pays"]}]},
 {"type": "catalog", "label": "Catalogue", "eyebrow": "Catalogue complet", "title": "Tous les cas d'usage, par front",
  "text": "Des hypothèses de valeur fondées sur le fonctionnement des industriels des matériaux de construction et sur ce qui est déjà en production chez des industriels comparables. Chacune s'ouvre en 3D avec son adaptation, son architecture et ses ressources."},
 {"type": "reel", "label": "Vidéos", "eyebrow": "Dreamforce · Salesforce+", "title": "À voir en action",
  "lead": "Quatre sessions sur la façon dont les industriels avancent déjà avec les agents.",
  "videos": [V["mfg26"], V["rev26"], V["road26"], V["agents25"]], "note": "Sessions en anglais."},
 {"type": "closing", "label": "Prochaines étapes", "color": "sage", "eyebrow": "Prochaines étapes",
  "title": "De la carte au premier cas d'usage en production",
  "rows": [["Choisir le premier périmètre", "Devis configurés et visites mobiles pour l'équipe commerciale France."],
           ["Cartographier les données", "ERP, tarifs, planning des lignes et documents techniques : les flux à relier en premier."],
           ["Mesurer dès le premier jour", "Délai de devis, réclamations et taux de transformation, pour fixer des objectifs réels."]],
  "thanks": "Merci", "foot": ["ONDEX | Salesforce", "Panorama360 · Matériaux de construction · 2026"],
  "legal": ["**Statut du document.** Support de travail pour une conversation de valeur. Les cas d'usage sont **proposés**, non engagés : aucun périmètre, aucune licence ni aucun calendrier n'ont été arrêtés. Les indicateurs sont des **références d'autres entreprises ou des estimations** pour dimensionner la discussion, pas des engagements contractuels : les objectifs se fixent avec ONDEX sur sa base réelle.",
            "**Marques.** ONDEX et ses marques appartiennent à leurs propriétaires. Le monde 3D est une illustration ; le logo n'apparaît qu'avec le fichier officiel et l'accord d'ONDEX.",
            "**Sources publiques.** ondex.com (à propos, gammes, applications, ONDEX SOLAR), La Gazette France (juillet 2025), AIAC (septembre 2025) ; témoignages clients et annonces sur salesforce.com et mulesoft.com."]}]}

WORLD = {
 "lang": "fr",
 "meta": {"client": "ONDEX", "partner": "Salesforce", "topic": "PVC bi-orienté", "audience": "executive",
          "title": "ONDEX | Salesforce — Chaque plaque, de l'usine au chantier", "loader": "ONDEX · PVC bi-orienté"},
 "brand": {"primary": "#0A3D54", "secondary": "#00697B", "accent": "#00697B", "logo": "ondex-logo.png", "logo_plate": True},
 "world": {"layout": "compact", "relief": "hills",
           "landscape": {"preset": "temperate", "cattle": True,
                         "pal": {"warm": {"FA": "#E8D9A0", "FB": "#C9DA9E", "FC": "#E6D682", "ROOF": "#C8735A"}}}},
 "intro": {"eyebrow": "Art du possible · PVC bi-orienté", "title": "Chaque plaque, de l'usine au chantier.",
           "text": "Un agent aux côtés de chaque équipe ONDEX, des lignes de bi-orientation de Chevigny jusqu'aux négoces, aux exploitations et aux toitures solaires.",
           "cta": "Parcourir l'opération"},
 "stages": STAGES,
 "final": {"eyebrow": "Carte interactive · 8 fronts", "title": "Là où ONDEX devient agentique",
           "text": "Touchez un front pour y revenir : chaque « + » ouvre ce qu'il résout, les indicateurs qu'il fait bouger et la façon dont les briques Salesforce se connectent.",
           "cta": "Retour au début", "arcs": "hub"},
 "ui": UI,
 "usecases": UC,
 "story": STORY,
 "presenter": {"name": "Patrick Pelot", "title": "Senior Account SE", "company": "Salesforce", "email": "ppelot@salesforce.com",
               "photo": "https://avatars.slack-edge.com/2020-12-11/1591684660400_c6210db8ffcc5a0d7b60_original.png"},
 "underworld": UNDER,
 "sources": [
  {"title": "ONDEX · À propos", "url": "https://www.ondex.com/a-propos/", "note": "capital, depuis 1965, bi-orientation brevetée en 1964, >4× résistance, 2,4 kg/m² vs 7 (acier) et 12 (fibrociment), historique, AIAC 2025, ONDEX SOLAR"},
  {"title": "ONDEX · Accueil", "url": "https://www.ondex.com/", "note": "16 gammes, 6 applications, DIFFU100 lumière 100 % diffusante"},
  {"title": "ONDEX · Serres et jardineries", "url": "https://www.ondex.com/application-serres-et-jardineries/", "note": "3 gammes BIO, 4 nuances"},
  {"title": "ONDEX · Communiqué ONDEX SOLAR", "url": "https://www.ondex.com/wp-content/uploads/2026/01/CommPresse_SOLAR_Diffuse.pdf", "note": "2,4 kg/m² vs jusqu'à 17 kg/m² fibrociment, FIX O Bat / FIX O Ser, certification ETN, partenariats installateurs"},
  {"title": "La Gazette France, 25 juillet 2025", "url": "https://www.lagazettefrance.fr/article/chevigny-saint-sauveur-renolit-ondex-rachetee-par-un-investisseur-industriel-americain", "note": "site de 5 ha, environ 100 collaborateurs"},
  {"title": "AIAC, 30 septembre 2025", "url": "https://www.aiac.com/news/aiac-acquires-ondex-from-renolit-group", "note": "acquisition, marchés, 122 sites dans 24 pays"},
  {"title": "Témoignages clients", "url": "https://www.salesforce.com/fr/customer-stories/", "note": "Poclain, Air Liquide, Imerys, Schneider Electric, Etex, JK Cement, Siemens, Endress+Hauser, Fisher & Paykel ; Saint-Gobain sur mulesoft.com"}],
 "_note": "Generated by make_world.py — kits pvc_plant, pvc_stock, negoce, chantier, agri_serres live in assets/js/world/k6-ondex.js of the skill copy.",
}

json.dump(typo(WORLD), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", OUT, "·", len(STAGES), "stages ·", len(UC), "use cases")
