import pandas as pd

# Load the input file
input_file = pd.read_excel('INA Inventory System.xlsx')

# Create the new column by concatenating all columns
input_file['new_column'] = input_file.apply(lambda x: ''.join(x.astype(str)), axis=1)

# Define the databases
database_1 = {"TAFFETA": "AA0",
"AURA": "AA1",
"BITON": "AA2",
"CIRE": "AA3",
"MESH": "AA4",
"CATS": "AA5",
"BAMBOO": "AA6",
"BOSSIS": "AA7",
"Amazon": "AA8",
"CASSEL": "AA9",
"COCKEREL": "AB0",
"KLUFT": "AB1",
"ROBEC": "AB2",
"PONGEE": "AB3",
"TWILL": "AB4",
"ACRYL": "AB5",
"FLEECE": "AB6",
"MOORE": "AB7",
"CLARKSON": "AB8",
"DUFIVE": "AB9",
"LEDDY": "AC0",
"LUCQY": "AC1",
"MICROFLEECE": "AC2",
"Perfecta": "AC3",
"SEAM TAPE": "AC4",
"RIB": "AC5",
"ARYA": "AC6",
"CHEROKEE": "AC7",
"DOBBY": "AC8",
"EMILE": "AC9",
"PUCCINO": "AD0",
"RIKA": "AD1",
"SPICA": "AD2",
"VICO": "AD3",
"KIELDER": "AD4",
"INTERLINING": "AD5",
"THERMOFUSION": "AD6",
"FUSING": "AD7",
"SCRIM": "AD8",
"MORANE": "AD9",
"OKOONA": "AE0",
"CONBR": "AE1",
"MELTEMI": "AE2",
"ELM": "AE3",
"AVARUA": "AE4",
"OMNI TECH": "AE5",
"CRINKLE": "AE6",
"MODERN": "AE7",
"Rebound Stretch MP": "AE8",
"MP Lam": "AE9",
"Loma Vista": "AF0",
"RIPSTOP CO": "AF1",
"BERGUNDTAL": "AF2",
"ALPHA": "AF3",
"HYDROPLUS": "AF4",
"HEGOA": "AF5",
"LEVANT": "AF6",
"NOTUS": "AF7",
"LYCRA": "AF8",
"MAKOGAI": "AF9",
"BASIC LINING": "AG0",
"VIRGA": "AG1",
"BELHARRA": "AG2",
"SMOOTH": "AG3",
"OG": "AG4",
"SOFT": "AG5",
"BEAUFORT": "AG6",
"REINFORCEMENT": "AG7",
"RIPSTOP": "AG8",
"NEXGEN": "AG9",
"HOLK": "AH0",
"LILAC": "AH1",
"MATUMI": "AH2",
"SODALITE": "AH3",
"TILIA": "AH4",
"YUMMY PILE": "AH5",
"PADDING": "AH6",
"NEEDLE PUNCH": "AH7",
"MICROTEMP": "AH8",
"Loft": "AH9",
"DOWNLIKE": "AI0",
"SLIMTECH": "AI1",
"SOFTERMIC": "AI2",
"DAHU": "AI3",
"soft meric": "AI4",
"Ball Padding": "AI5",
"STANDARD PES RECYCLED": "AI6",
"THERMARATOR": "AI7",
"BALI": "AI8",
"DIANA": "AI9",
"KATE": "AJ0",
"KATRINA": "AJ1",
"NAT": "AJ2",
"TULEAR": "AJ3",
"WINSTON": "AJ4",
"VICTORIA": "AJ5",
"BARCELONA": "AJ6",
"AGASSIZ": "AJ7",
"ANKA": "AJ8",
"ASCELLA": "AJ9",
"BIANCA": "AK0",
"CLINTON": "AK1",
"ADELAIDE": "AK2",
"KINNA": "AK3",
"NATAR": "AK4",
"OXMO": "AK5",
"MIMOSA": "AK6",
"QORSUK": "AK7",
"ADHESIVE": "AK8",
"SLIMY": "AK9",
"ALLEN": "AL0",
"ALUNA": "AL1",
"SMOOTHY": "AL2",
"MEKKO": "AL3",
"HINOKI": "AL4",
"MENKAR": "AL5",
"CARMEN": "AL6",
"ENETTE": "AL7",
"FAUX FUR": "AL8",
"COSTA": "AL9",
"BOSTON": "AM0",
"PESKO": "AM1",
"MILLER": "AM2",
"BAFFLE": "AM3",
"HYPALON": "AM4",
"MASSIMO": "AM5",
"SCUD": "AM6",
"LINING": "AM7",
"CORDS": "AM8",
"DRAWCORD": "AM9",
"DRAWCORD-CORDING-LACES": "AN0",
"HOOD LACE": "AN1",
"TIECORDS": "AN2",
"WAISTBAND TIECORDS": "AN3",
"BELT ELASTIC": "AN4",
"BOTTOM ELASTIC": "AN5",
"BRAID ELASTIC": "AN6",
"ELASTIC": "AN7",
"ELASTIC BAND": "AN8",
"ELASTIC BINDING": "AN9",
"ELASTIC CORD": "AO0",
"ELASTIC FLAT": "AO1",
"KNITTED": "AO2",
"ELASTIC FOR ROLL PACK": "AO3",
"ELASTIC GAITER": "AO4",
"ELASTIC LOOP": "AO5",
"ELASTIC STRING": "AO6",
"FOLDED ELASTIC": "AO7",
"HEM ELASTIC": "AO8",
"HOOD  &  CUFF ELASTIC": "AO9",
"HOOD LACET ELASTIC": "AP0",
"KNITTED ELASTIC FOR CUFF": "AP1",
"NON-ROLL ELASTIC": "AP2",
"STRAP ELASTIC": "AP3",
"THIGH ELASTIC": "AP4",
"TUNNEL ELASTIC": "AP5",
"WAIST ELASTIC": "AP6",
"HOOD LACET EYELET": "AP7",
"GROSGRAIN": "AP8",
"HANGING LOOP": "AP9",
"HERRINGBONE": "AQ0",
"ADEQUAT": "AQ1",
"ADEQUAT CAVALIER": "AQ2",
"ADEQUAT LEAFLET": "AQ3",
"ADEQUAT TAG": "AQ4",
"ADEQUAT TEXTILE": "AQ5",
"HANGTAG": "AQ6",
"HANGER": "AQ7",
"HEAT TRANSFER GLUED": "AQ8",
"ALT HEAT TRANSFER GLUED": "AQ9",
"HEAT SEAL": "AR0",
"AQUARESIST LOGO": "AR1",
"ALT LOGO LABEL": "AR2",
"BARCODE": "AR3",
"BEAD": "AR4",
"CORD ENDS": "AR5",
"CORD PULLER": "AR6",
"CORD STOPPER": "AR7",
"HOOD CORD STOPPER": "AR8",
"STOPPER-TANKA": "AR9",
"TANKA": "AS0",
"TOGGLE": "AS1",
"JOKER TAG/RFID TAG": "AS2",
"BOTTOM HOOK": "AS3",
"BOTTOM LEG SNAP BUTTON": "AS4",
"GAITER HOOK": "AS5",
"SNAP BELT": "AS6",
"SNAP CAP BELT": "AS7",
"SNAP POCKET": "AS8",
"SNAP PROTECTION": "AS9",
"SNAPS": "AT0",
"SNAPTOP BUTTON BRANDED": "AT1",
"SOCKET/STUD/POST": "AT2",
"WAIST HOOK CAP": "AT3",
"WAIST HOOK UNDERPARTS": "AT4",
"WAIST SNAP CAP": "AT5",
"WAIST SNAP UNDERPARTS": "AT6",
"WAISTBAND HOOK": "AT7",
"ADEQUAT SIZE": "AT8",
"ADEQUAT STICKER": "AT9",
"IDENTITY STICKER": "AU0",
"COLLAR LOOP": "AU1",
"GAITERS VELCRO HOOK": "AU2",
"GAITERS VELCRO LOOP": "AU3",
"HOOK": "AU4",
"HOOK & LOOP": "AU5",
"LOOP": "AU6",
"PACKABLE POCKET VELCRO": "AU7",
"STRAP VELCRO HOOK": "AU8",
"STRAP VELCRO LOOP": "AU9",
"BANDROLL": "AV0",
"BUTTON": "AV1",
"BELT": "AV2",
"BIAIS": "AV3",
"BINDING": "AV4",
"BOTTOM RIBBON": "AV5",
"BOX": "AV6",
"BUCKLE": "AV7",
"BUNGEE": "AV8",
"CARE & SIZE LABEL": "AV9",
"CARE LABEL": "AW0",
"CARTON STICKER": "AW1",
"RFID STICKER": "AW2",
"COLLAR RISER": "AW3",
"COURIER": "AW4",
"D. SIGNATURE": "AW5",
"DECATHLON LOGO": "AW6",
"DIRECT EMBROIDERY": "AW7",
"DOMYOS LOGO": "AW8",
"DRAWSTRING": "AW9",
"DRY CLAY": "AX0",
"EMBROIDERED LOGO": "AX1",
"EMBROIDERY": "AX2",
"EYELET": "AX3",
"FLY ZIP": "AX4",
"FRONT FLAP VELCRO": "AX5",
"FRONT PART": "AX6",
"FRONT ZIP": "AX7",
"GAITERS ZIP": "AX8",
"GLUE": "AX9",
"GRAPHIC": "AY0",
"GRIPPING BAND": "AY1",
"GUM TAPE": "AY2",
"HANG TAG WITH RFID": "AY3",
"HOOD TIGHTENING": "AY4",
"LABEL": "AY5",
"LABEL LOGO": "AY6",
"LAMINET": "AY7",
"LOCK PIN": "AY8",
"LYCRA Binding": "AY9",
"MAIN & CARE LABEL": "AZ0",
"MAIN LBL": "AZ1",
"MAIN ZIP PULLER": "AZ2",
"MAIN ZIPPER": "AZ3",
"MASTER POLYBAG": "AZ4",
"MOQ": "AZ5",
"NECKTAPE": "AZ6",
"OLAIAN BRANDING PATCH": "AZ7",
"OLAIAN NEW HEAT TRANSFER": "AZ8",
"OTHER COST": "AZ9",
"PACKAGING": "BA0",
"PASSION BRAND LABEL": "BA1",
"PEARL": "BA2",
"PHEMO": "BA3",
"PLASTIC LINK": "BA4",
"PLASTIC LOOP": "BA5",
"POCKET SLIDER": "BA6",
"POCKET ZIP": "BA7",
"POCKET ZIP SLIDER": "BA8",
"POCKETS PULLER": "BA9",
"POLYBAG": "BB0",
"PRINT": "BB1",
"PULLER": "BB2",
"QUECHUA LABEL": "BB3",
"QUECHUA PRINT": "BB4",
"REFLECTIVE HEAT TRANSFER": "BB5",
"RESERVE FUND": "BB6",
"RFID": "BB7",
"RFID HANGTAG": "BB8",
"RFID LABEL": "BB9",
"RFID POCKET TAG": "BC0",
"RFID TAG": "BC1",
"RING &WASHER": "BC2",
"RISER": "BC3",
"RIVET": "BC4",
"SCREEN PRINT": "BC5",
"SEALING TAPE": "BC6",
"SEAM TAPE": "BC7",
"SHAPE CAVALIER": "BC8",
"SHAPE LEAFLET": "BC9",
"SHU STICKER": "BD0",
"SIDE BOTTOM OPENING ZIP": "BD1",
"SIZE LABEL": "BD2",
"SIZE LABEL+ CARE LABEL": "BD3",
"SIZE STICKER": "BD4",
"SIZER": "BD5",
"SLIDER": "BD6",
"STICKER": "BD7",
"STOP PLASTIC WASTE": "BD8",
"STOPPER": "BD9",
"STRAP PLASTIC ACCESSORY": "BE0",
"STRETCH BLAIS": "BE1",
"STRING": "BE2",
"STUDS": "BE3",
"SWIFT TAG": "BE4",
"TAG FIT": "BE5",
"TAG PIN": "BE6",
"TEAR AWAY LABEL-MJ_CARE PACKING LABEL": "BE7",
"TEMPERATURE HANGTAG/SECONDARY HANG TAG": "BE8",
"TEST": "BE9",
"THERMOBONDED EYELET": "BF0",
"THERMOBONDED OVAL": "BF1",
"EYELET": "BF2",
"THERMOBONDED": "BF3",
"BARTACKS": "BF4",
"THERMOBONDING GLUE": "BF5",
"ASTRA": "BF6",
"TICKET": "BF7",
"TIP END": "BF8",
"TISSUE PAPER": "BF9",
"TRACEABILITY LABEL": "BG0",
"UE CONDITIONING": "BG1",
"UNIQUE LABEL": "BG2",
"UNIQUE SIZE CAVALIER": "BG3",
"UPC STICKER": "BG4",
"VAS": "BG5",
"VELCRO": "BG6",
"WAIST & HOOD TIGHTENING": "BG7",
"WAISTBAND SNAP BUTTON": "BG8",
"WASHER": "BG9",
"WEBBING": "BH0",
"WOVEN LABEL": "BH1",
"YELLOW STICKER": "BH2",
"ZIP": "BH3",
"ZIP PULLER": "BH4",
"ZIP SLIDER": "BH5",
"ZIPPER + PULLER": "BH6",
"Gramax": "BH7",
"Sylko": "BH8",
"Epic": "BH9"}

database_2 = {"COLORLESS": "AA0",
"9665": "AA1",
"13000104": "AA2",
"14000146": "AA3",
"14000215": "AA4",
"14000231": "AA5",
"14000233": "AA6",
"15000054": "AA7",
"16000094": "AA8",
"16000095": "AA9",
"34000035": "AB0",
"35000018": "AB1",
"36000020": "AB2",
"50100031": "AB3",
"50100032": "AB4",
"54000015": "AB5",
"55000009": "AB6",
"56000011": "AB7",
"079257 Black": "AB8",
"84394": "AB9",
"Black": "AC0",
"11-0103 TCX Egret": "AC1",
"11-0601 TCX Bright White": "AC2",
"11-0604 TCX Gardenia": "AC3",
"12-0720 TCX Mellow Yellow": "AC4",
"12-0729 TCX Sundress": "AC5",
"13-2804 TCX Parfait Pink": "AC6",
"13-4910 TCX Blue Tint": "AC7",
"13-6008 TCX Misty Jade": "AC8",
"14-0846 TCX Yolk Yellow": "AC9",
"14-1231 TCX Peach Cobbler": "AD0",
"14-4107 TCX Quiet Gray": "AD1",
"14-4317 TCX Cool Blue": "AD2",
"14-4816 TCX Blue Radiance": "AD3",
"150 GSM D/LINKFLASHED-GREIGE FABRIC": "AD4",
"150 gsm LOFT FLASHED-GREIGE FABRIC": "AD5",
"15-1062 TCX Gold Fusion": "AD6",
"15-1157 TCX Flame Orange": "AD7",
"15-3716 TCX Purple Rose": "AD8",
"16-1253 TCX Orange Ochre": "AD9",
"16-1506 TCX Bark": "AE0",
"16-1710 TCX Foxglove": "AE1",
"16-5930 TCX Ming Green": "AE2",
"17-0843 TCX Bronze Mist": "AE3",
"17-1736 TCX Sun Kissed Coral": "AE4",
"17-3826 TCX Aster Purple": "AE5",
"17-4140 TCX All Aboard": "AE6",
"17-4405 TCX Monument": "AE7",
"17-4730 TCX Caneel Bay": "AE8",
"17-6212 TCX Sea Spray": "AE9",
"18-0312 TCX Deep Lichen Green": "AF0",
"18-0830 TCX Butternut": "AF1",
"18-1449 TCX Ketchup": "AF2",
"18-1657 TCX Salsa": "AF3",
"18-1661 TCX Tomato Puree": "AF4",
"18-3912 TCX Grisaille": "AF5",
"18-3920 TCX Coastal Fjord": "AF6",
"18-4016 TCX December Sky": "AF7",
"18-4250 TCX Indigo Bunting": "AF8",
"1853855-DKT-G17C BLUE": "AF9",
"18-6011 TCX Duck Green": "AG0",
"18-6018 TCX Foliage Green": "AG1",
"1864413 - DKT-F16A BLUE": "AG2",
"1864415 - DKT-D12A PINK": "AG3",
"19-0203 TCX Gray Pinstripe": "AG4",
"19-0303 TCX Jet Black": "AG5",
"19-0303 TCX(Ground) / Pantone 14-4305 TCX ( Print)": "AG6",
"190303TCX": "AG7",
"19-0307 TCX Climbing Ivy": "AG8",
"19-0309 TCX Thyme": "AG9",
"19-1337 TCX Fired Brick": "AH0",
"19-1531 TCX Sun-Dried Tomato": "AH1",
"19-1619 TCX Fudge": "AH2",
"19-1725 TCX Tawny Port": "AH3",
"19-1761 TCX tangored": "AH4",
"191761 TCX": "AH5",
"19-3900 TCX Pavement": "AH6",
"19-3911 TCX Black Beauty": "AH7",
"19-3921 TCX Black Iris": "AH8",
"19-3923 TCX Navy Blazer": "AH9",
"19-3953 TCX Sodalite Blue": "AI0",
"19-4015 TCX Blue Graphite": "AI1",
"19-4048 TCX Baleine Blue": "AI2",
"19-4117 TCX Big Dipper": "AI3",
"19-4316 TCX Stargazer": "AI4",
"19-4536 TCX Crystal Teal": "AI5",
"19-4540 TCX Deep Lagoon": "AI6",
"19-5918 TCX Mountain View": "AI7",
"2002056 - DKT-N06A GREY": "AI8",
"2069061 - FLASHED-@CARBON BLACK SUPPLIER": "AI9",
"2171864-DKT-N07A BLACK": "AJ0",
"2232650 - TCX-GREIGE": "AJ1",
"2405800 - DKT-F09B BORDEAUX": "AJ2",
"2409744 - DKT-N07A BLACK": "AJ3",
"2430681-DKT-L02A BEIGE": "AJ4",
"2431150-DKT-L02A BEIGE": "AJ5",
"2436880-DKT-N07A BLACK": "AJ6",
"2463501-DKT-N07A BLACK": "AJ7",
"250 GSM STANDARD FLASHED-GREIGE FABRIC": "AJ8",
"2681655-DKT-E12A PINK": "AJ9",
"2694909 - DKT-L03A BEIGE": "AK0",
"2739833 - PAT01311-DIAMOND Emboss": "AK1",
"2739837-DKT-G17C BLUE": "AK2",
"2740729 - DKT-F16A BLUE": "AK3",
"2741751-SHENGHONG CARBON BLACK": "AK4",
"2742724-DKT-F09B BORDEAUX": "AK5",
"2743740-MC01307": "AK6",
"2781207-MC00533-N06A-N06A": "AK7",
"2783556-DKT-N11A GREY": "AK8",
"2851729 - FLASHED-@CARBON BLACK SUPPLIER": "AK9",
"2855868-MC01307-": "AL0",
"2859913-DKT-N06A GREY": "AL1",
"2869771-DKT-A10A PINK": "AL2",
"2869784-DKT-D17C BLUE": "AL3",
"2921198-DKT-F09B BORDEAUX": "AL4",
"2921204 - DKT-N09A GREY": "AL5",
"2934974 - FLASHED-GREIGE FABRIC": "AL6",
"2934974 - GREIGE FABRIC": "AL7",
"2993450-DKT-N11A GREY": "AL8",
"2994435-DKT-F16A BLUE": "AL9",
"2994576-DKT-F16A BLUE": "AM0",
"2996184-FLASHED-": "AM1",
"@CARBON BLACK SUPPLIER": "AM2",
"2997518-DKT-N06A GREY": "AM3",
"359SH": "AM4",
"3M C725 Silver Reflective": "AM5",
"3M C790 Carbon Black Reflective": "AM6",
"3M Carbon Black Reflective": "AM7",
"4023538 - DKT-N06A GREY": "AM8",
"4023539 - DKT-N07A BLACK": "AM9",
"4035315 - DKT-F09B BORDEAUX": "AN0",
"4070528-MC00533-N06AN06A": "AN1",
"4070528-MC00533-N06A-N06A": "AN2",
"4070530 - MC01307-": "AN3",
"4076418 - MC00327-N07A-N00A": "AN4",
"4079692 - DKT-N07A BLACK": "AN5",
"4079692-DKT-N07A BLACK": "AN6",
"4079693 - DKT-G19B BLUE": "AN7",
"4081782-DKT-N07A BLACK": "AN8",
"4081915 - MC01218-GREIGE": "AN9",
"4081915-MC01218-GREIGE": "AO0",
"4131961 - PAT01335-DIAMOND BIG Grey": "AO1",
"4137688-MC02848-L02B-L02B": "AO2",
"4138639 - FLASHED-@CARBON BLACK SUPPLIER": "AO3",
"4139075 - DKT-F08C BROWN": "AO4",
"4142347 - DKT-A10A PINK": "AO5",
"4142347-DKT-A10A PINK": "AO6",
"4142351-DKTest-C07B RED": "AO7",
"4156987 - MC00014-N07A-N07A": "AO8",
"4282467 - PAT13071-HEATHERFABRIC-lightgrey": "AO9",
"4282480 - DKTest-F21A TURQUOISE": "AP0",
"4310606 - DKT-F18A BLUE": "AP1",
"4469819 - DKT-E17B BLUE": "AP2",
"4505928 - FLASHED-GREIGE FABRIC": "AP3",
"4506805 - DKT-L03A BEIGE": "AP4",
"4540991 - PAT15871-THARKEY- Inkpot Blue": "AP5",
"4555126 - DKT-F16A BLUE": "AP6",
"4555127 - DKT-D12A PINK": "AP7",
"4562420 - DKT-C13B PINK": "AP8",
"4582136 - DKT-D12A PINK": "AP9",
"4582489 - DKT-G20A BLUE": "AQ0",
"4582490 - DKT-G20A BLUE": "AQ1",
"4582651 - DKT-G20A BLUE": "AQ2",
"4589287 - DKT-H09B RED": "AQ3",
"4599905 - PAT16337-KID PARKOUR SKI": "AQ4",
"4669096 - DKT-F16A BLUE": "AQ5",
"4670422 - DKT-F16A BLUE": "AQ6",
"4690076 - DKT-C13B PINK": "AQ7",
"4690088 - DKT-C13B PINK": "AQ8",
"4729004 - DKT-J17A BLUE": "AQ9",
"60 GSM LOFT- FLASHED-GREIGE FABRIC": "AR0",
"60 GSM NEEDLE PUNCHED PES FLASHED-GREIGE FABRIC": "AR1",
"638914 - Old Color Trace": "AR2",
"722TG": "AR3",
"80 GSM  D/LINK HUAFU-HB450 HEATHER GREIGE -": "AR4",
"80 GSM LOFT FLASHEDGREIGE FABRIC": "AR5",
"8210 Silver Reflective": "AR6",
"825B Black Iris Reflective": "AR7",
"8292 Black Reflective": "AR8",
"ABER ROSES": "AR9",
"Ancient Fossil": "AS0",
"Antique Silver Metallic": "AS1",
"Antique teal": "AS2",
"antique tool": "AS3",
"AquaGaurd Coil V10 Book YKK Colour 580": "AS4",
"AquaGaurd Coil V10 Book": "AS5",
"YKK Colour 908": "AS6",
"Arsenic Gold": "AS7",
"Beach": "AS8",
"Beetroot": "AS9",
"Beetroot, Faded Peach": "AT0",
"Black": "AT1",
"Black as per proto sample": "AT2",
"Black CN10 EIFFE 18 -5210 TCX": "AT3",
"Black Soot": "AT4",
"Black, Black": "AT5",
"Black, City Grey": "AT6",
"Black/Gunmetal": "AT7",
"Blaze Orange/SPECIAL COLOR": "AT8",
"Blue Cove": "AT9",
"Blue Fish": "AU0",
"BLUE FISH(special solid)": "AU1",
"Blue/White": "AU2",
"Bluestone": "AU3",
"Boil Off": "AU4",
"Bright Blue": "AU5",
"Bright Indigo": "AU6",
"Bright Orange": "AU7",
"Bright Red": "AU8",
"Bright White 11-0601tcx": "AU9",
"brilliant red": "AV0",
"Brush Stroke Firework": "AV1",
"Brush Stroke Firework/royal indigo": "AV2",
"BUBBLE GUM PINK(special Neon)": "AV3",
"bubblegum": "AV4",
"Bubblegum Pink": "AV5",
"C0391/DE408": "AV6",
"C1162": "AV7",
"C1185": "AV8",
"C1401": "AV9",
"C3156": "AW0",
"C3361": "AW1",
"C3901": "AW2",
"C4106": "AW3",
"C5711": "AW4",
"C5900": "AW5",
"C5946": "AW6",
"C6389": "AW7",
"C6952": "AW8",
"C7225": "AW9",
"C7284": "AX0",
"C7370": "AX1",
"C7497": "AX2",
"C7586": "AX3",
"C7699": "AX4",
"C7930": "AX5",
"C7932": "AX6",
"C7944": "AX7",
"C7956": "AX8",
"C7959": "AX9",
"C8133": "AY0",
"C9665": "AY1",
"C9700": "AY2",
"C9700": "AY3",
"C9710": "AY4",
"C9863": "AY5",
"C9959": "AY6",
"Camel Brown": "AY7",
"CAMO PRINT": "AY8",
"CARVICO-60026 NEW BLU CINA/DKT-C18A BLUE": "AY9",
"CARVICO-6208 INDIGO": "AZ0",
"CARVICO-6208 INDIGO/DKT-E18A BLUE": "AZ1",
"CARVICO-6274": "AZ2",
"BLUCINA": "AZ3",
"Chalk": "AZ4",
"Chiseled Stone 16-3917tcx": "AZ5",
"Cirrus Grey": "AZ6",
"Cirrus Grey, Cirrus Grey": "AZ7",
"City Grey": "AZ8",
"City Grey, City Grey": "AZ9",
"Clear": "BA0",
"Collegiate Navy": "BA1",
"Collegiate Navy, Night Tide": "BA2",
"Columbia Grey": "BA3",
"Coral": "BA4",
"coral zest": "BA5",
"Coral/Crushed plum": "BA6",
"CORD- PANOTNE 18-6011 TCX DUCK GREEN  PLASTIC- PANTONE 19-5978 TCX MOUNTAIN VIEW": "BA7",
"CORD- PANTONE 16-3917 TCX CHISELED STONE  PLASTIC-PANTONE 19-0203 TCX GRAY PINSTRIPE": "BA8",
"CORD- PANTONE 18-0830 TCX BUTTERNUT  PLASTIC- PANTONE 17-0483 TCX BRONZE MIST": "BA9",
"CORD- PANTONE 19-1337 TCX FIRED BRICK  PLASTIC PANTONE 18-1449 TCX KETCHUP": "BB0",
"CORD- PANTONE 19-4048 TCX BALEINE BLUE  PLASTIC - PANTONE 18-4250 TCX INDIGO BUNTING": "BB1",
"CORD- PANTONE 19-4117 TCX BIG DIPPER  PLASTIC- PANTONE 18-4250 TCX INDIGO BUNTING": "BB2",
"CRUSHED PLUM": "BB3",
"Dark Mountain": "BB4",
"Dark Navy": "BB5",
"Dark Nocturnal": "BB6",
"Dark Sapphire": "BB7",
"Dark Sapphire, Dark Sapphire": "BB8",
"Dark Stone": "BB9",
"Dark Stone, Chalk": "BC0",
"DDY-N07 BLACK": "BC1",
"DDY-N07 BLACK/CARBON BLACK": "BC2",
"Delta": "BC3",
"Desert": "BC4",
"Desert/SCUBA LIME": "BC5",
"DEUX DINO PRINT": "BC6",
"DH07D/C3975": "BC7",
"Dino /Grey": "BC8",
"DKT-A05B ORANGE": "BC9",
"DKT-A08A PINK": "BD0",
"DKT-A08B PINK": "BD1",
"DKT-A08E RED": "BD2",
"DKT-A10A PINK": "BD3",
"DKT-A28A YELLOW": "BD4",
"DKT-B07A ORANGE": "BD5",
"DKT-B23A GREEN": "BD6",
"DKT-B26A GREEN": "BD7",
"DKT-C13B PINK": "BD8",
"DKT-C18A BLUE": "BD9",
"DKT-C20D": "BE0",
"TURQUOISE": "BE1",
"DKT-C22A": "BE2",
"TURQUOISE": "BE3",
"DKT-D03A ORANGE": "BE4",
"DKT-D04A ORANGE": "BE5",
"DKT-D06A ORANGE": "BE6",
"DKT-D08A RED": "BE7",
"DKT-D09A RED": "BE8",
"DKT-D11A PINK": "BE9",
"DKT-D12A PINK": "BF0",
"DKT-D16A BLUE": "BF1",
"DKT-D17A BLUE": "BF2",
"DKT-D17C BLUE": "BF3",
"DKT-D19B TURQUOISE": "BF4",
"DKT-D19B": "BF5",
"TURQUOISE": "BF6",
"DKT-D21A": "BF7",
"TURQUOISE": "BF8",
"DKT-D28B GREEN": "BF9",
"DKT-E05A ORANGE": "BG0",
"DKT-E05A ORANGE": "BG1",
"DKT-E12A PINK": "BG2",
"DKT-E17B BLUE": "BG3",
"DKT-E18A BLUE": "BG4",
"DKT-E18A BLUE/CARVICO-6208 INDIGO": "BG5",
"DKT-E19A BLUE": "BG6",
"DKT-E23B GREEN": "BG7",
"DKTest-F10C BORDEAUX": "BG8",
"DKTEST-F11C PURPLE": "BG9",
"DKTest-H02B YELLOW": "BH0",
"DKTest-H20C TURQUOISE": "BH1",
"DKTest-H23B GREEN": "BH2",
"DKTest-J14A PURPLE": "BH3",
"DKTest-K07A BEIGE": "BH4",
"DKTest-K12A PURPLE": "BH5",
"DKTest-K22A GREEN": "BH6",
"DKTest-L07B PINK": "BH7",
"DKT-F08A BROWN": "BH8",
"DKT-F08B BROWN": "BH9",
"DKT-F09A BORDEAUX": "BI0",
"DKT-F09B BORDEAUX": "BI1",
"DKT-F10C BORDEAUX": "BI2",
"DKT-F11A PURPLE": "BI3",
"DKT-F12A PURPLE": "BI4",
"DKT-F16A BLUE": "BI5",
"DKT-F17A BLUE": "BI6",
"DKT-F18A BLUE": "BI7",
"DKT-F20A TURQUOISE": "BI8",
"DKT-F20A TURQUOISE": "BI9",
"DKT-F20A": "BJ0",
"TURQUOISE": "BJ1",
"DKT-G03B BROWN": "BJ2",
"DKT-G03C BROWN": "BJ3",
"DKT-G08A BROWN": "BJ4",
"DKT-G17C BLUE": "BJ5",
"DKT-G19A BLUE": "BJ6",
"DKT-G19B BLUE": "BJ7",
"DKT-G20A BLUE": "BJ8",
"DKT-G20A BLUE": "BJ9",
"DKT-G23B GREEN": "BK0",
"DKT-G23B GREEN": "BK1",
"DKT-G24A GREEN": "BK2",
"DKT-G26A KHAKI": "BK3",
"DKT-G28B KHAKI": "BK4",
"DKT-H10A PINK": "BK5",
"DKT-H17A BLUE": "BK6",
"DKT-H17B BLUE": "BK7",
"DKT-H23B GREEN": "BK8",
"DKT-J14A PURPLE": "BK9",
"DKT-J25A KHAKI": "BL0",
"DKT-K03A BEIGE": "BL1",
"DKT-K03C BROWN": "BL2",
"DKT-K10A GREY": "BL3",
"DKT-K12A PURPLE": "BL4",
"DKT-K20A GREY": "BL5",
"DKT-K20B GREY": "BL6",
"DKT-K22A GREEN": "BL7",
"DKT-K24A KHAKI": "BL8",
"DKT-K26A KHAKI": "BL9",
"DKT-K26B KHAKI": "BM0",
"DKT-K27A KHAKI": "BM1",
"DKT-K27B KHAKI": "BM2",
"DKT-L02A BEIGE": "BM3",
"DKT-L02B BEIGE": "BM4",
"DKT-L03A BEIGE": "BM5",
"DKT-L07B PINK": "BM6",
"DKT-L14A PURPLE": "BM7",
"DKT-L18B GREY": "BM8",
"DKT-L21A": "BM9",
"TURQUOISE": "BN0",
"DKT-N00A WHITE": "BN1",
"DKT-N01A GREY": "BN2",
"DKT-N02A GREY": "BN3",
"DKT-N03A GREY": "BN4",
"DKT-N05A GREY": "BN5",
"DKT-N06A GREY": "BN6",
"DKT-N06B GREY": "BN7",
"DKT-N07A BLACK": "BN8",
"DKT-N07B BLACK": "BN9",
"DKT-N07C BLACK": "BO0",
"DKT-N08A GREY": "BO1",
"DKT-N11A GREY": "BO2",
"DKT-N12A GREY": "BO3",
"DKT-N13A WHITE": "BO4",
"DTM - THREAD ONLY": "BO5",
"DTM Shell 1": "BO6",
"Dusty Pink": "BO7",
"EB CAMO /Black soot": "BO8",
"Faded Peach": "BO9",
"FG305": "BP0",
"FLASHED- GREIGE FABRIC": "BP1",
"FLASHED-": "BP2",
"@POLAR BLACK": "BP3",
"FLASHED-@CARBON BLACK SUPPLIER": "BP4",
"FLASHED-@CW247 H RIFT GREY": "BP5",
"FLASHED-@ULTRA BLACK": "BP6",
"FLASHED-@ULTRA BLACK /DKT-N07A BLACK": "BP7",
"FLASHED-GREIGE FABRIC": "BP8",
"Flowers": "BP9",
"Flowers/Blue Cove": "BQ0",
"Geo Trangle Print": "BQ1",
"GN07S": "BQ2",
"GN07X": "BQ3",
"GN15Y": "BQ4",
"GN16Q": "BQ5",
"GN16Y": "BQ6",
"GN17V": "BQ7",
"GN23H": "BQ8",
"GN47B": "BQ9",
"GN47F": "BR0",
"GN47K": "BR1",
"GN47Z": "BR2",
"GRADIENT CHECK(was Multi)": "BR3",
"Granite Purple": "BR4",
"Green Artichoke": "BR5",
"GREIGE FABRIC": "BR6",
"Greystone": "BR7",
"GryBlu": "BR8",
"H206-HGREY": "BR9",
"HR107": "BS0",
"HTH-A08A PINK": "BS1",
"HTH-F12A- HEATHER PURPLE": "BS2",
"HTH-F20A- HEATHER TURQUOISE": "BS3",
"HTH-G03C BROWN": "BS4",
"HTH-G24A- HEATHER GREEN": "BS5",
"HTH-N00A- HEATHER WHITE": "BS6",
"HTH-N02A HEATHER GREY": "BS7",
"HTH-N03A- HEATHER GREY": "BS8",
"HTH-N06A HEATHER DARK GREY": "BS9",
"HTH-N11A HEATHER GREY": "BT0",
"HUAFU H125CY": "BT1",
"HUAFU-H122 MEDIUM HEATHER GREY": "BT2",
"HUAFU-HB450 HEATHER GREIGE -80 D/LINK": "BT3",
"Icy Morn": "BT4",
"Interstellar Noise": "BT5",
"Interstellar Noise/Blue cove2": "BT6",
"Jet Stream": "BT7",
"Key West": "BT8",
"Large Ikat": "BT9",
"Large Ikat/lavender Sunrise": "BU0",
"LARGE TROPICAL FLORAL PRINT": "BU1",
"LARGE TROPICAL PRINT/blue cove": "BU2",
"lavendar sunrise": "BU3",
"Lemons": "BU4",
"Lemons/Yellow charm": "BU5",
"Light Grey": "BU6",
"Light Jade": "BU7",
"LK212": "BU8",
"Marionberry": "BU9",
"Mars": "BV0",
"Mars/TEAL CREAM": "BV1",
"MC00014-N07A-N07A": "BV2",
"MC00014-N07A N07A /MC01307-": "BV3",
"MC00093-E18A-G17C": "BV4",
"MC00109-GREIGE-N07B": "BV5",
"MC00375-G17C-G17C": "BV6",
"MC00529-N00A- N07B": "BV7",
"MC00533-N06A- N06A": "BV8",
"MC00533-N06A-N06A": "BV9",
"MC00575-N07B GREIGE": "BW0",
"MC00575-N07B- GREIGE": "BW1",
"MC00792-G17C-H17B(17C BLUE)": "BW2",
"MC00809-L03A- L03A": "BW3",
"MC01127-J19A- K20A": "BW4",
"MC01301-G19B- G19B": "BW5",
"MC01307-": "BW6",
"MC01422-N12A- N12A": "BW7",
"MC01653-G23B- G23B": "BW8",
"MC01697-L02A- L02A": "BW9",
"MC01704-F20A- J25A(TURQUOISE)": "BX0",
"MC01893-F09B D08A (RED)": "BX1",
"MC02029-N02A- N02A": "BX2",
"MC02620-H101CY- GREIGE": "BX3",
"MC02848-L02B- L02B": "BX4",
"MC02848-L02BL02B": "BX5",
"MC02848-L02B-L02B": "BX6",
"MC04514-TK12A-TF10C": "BX7",
"MC04857-TK22A- TK22A": "BX8",
"MC04926-N07C- N07C": "BX9",
"MC06215-G23A G23B (GREEN)": "BY0",
"MC06507-F11C F11B(PURPLE)": "BY1",
"MC06509-TK22A- B23A": "BY2",
"MC06691-FLCARFLCAR- FLCAR": "BY3",
"MC07105- GREIGE-L03B": "BY4",
"MC07318": "BY5",
"MC07408-H23B- H23B": "BY6",
"MC07512-F10C- F10C": "BY7",
"MC07512-F10C-F10C": "BY8",
"MC07595-HTH- N03A-GREIGE": "BY9",
"MC07723-F08B- TK07A": "BZ0",
"MC07741- GREIGE-N10B": "BZ1",
"MC07790-HTH- N00A-GREIGE": "BZ2",
"MC07817-N07B- G24A": "BZ3",
"MC08601-H23B- G24A": "BZ4",
"MC09023-H09B- H09B": "BZ5",
"ME203": "BZ6",
"Metal": "BZ7",
"MIDNIGHT (19-3921 TCX)": "BZ8",
"MOUNTAIN SITE/BLUE MOUNTAIN": "BZ9",
"MP216": "CA0",
"mystical Rose": "CA1",
"Natural Fur": "CA2",
"Navy": "CA3",
"Navy Blue": "CA4",
"Navy/Copper": "CA5",
"NCS-DARK NAVY": "CA6",
"NCS-MAORI": "CA7",
"NCS-TRUE DARK BLUE": "CA8",
"NCS-WHITE": "CA9",
"New Olive": "CB0",
"Night Wave": "CB1",
"Night Wave, Aqua Haze": "CB2",
"Nimbus Grey": "CB3",
"Nocturnal": "CB4",
"NS118": "CB5",
"Old Color Trace": "CB6",
"OM314": "CB7",
"ORANGE TWIST": "CB8",
"ORCHID DELIGHT": "CB9",
"PACIFICA GREEN": "CC0",
"Papaya Juice": "CC1",
"Parrot Floral": "CC2",
"Parrot Floral/topiary green": "CC3",
"PAT02190-CANVASBLACK": "CC4",
"PAT03516-": "CC5",
"SQUAREBLACK": "CC6",
"PAT03530-": "CC7",
"PALMMINT": "CC8",
"PAT03556-": "CC9",
"CLOUDBLUE": "CD0",
"PAT05004-LIGNED CHINE GREY": "CD1",
"PAT05422-NEWWAVESBLUE": "CD2",
"PAT05446-GRADIENTBLUE": "CD3",
"PAT07134- LIGNED CHINE BLUE": "CD4",
"PAT07975-BASE CAMP DARK BLUE": "CD5",
"PAT08060-": "CD6",
"CONFETTI BLUE": "CD7",
"PAT08067-": "CD8",
"GRADIENT STRATS": "CD9",
"GREEN": "CE0",
"PAT08317-RADICAL-petrol": "CE1",
"PAT09148-ALL YUKU GREEN": "CE2",
"PAT10060-WOMAN AQUA": "CE3",
"PAT11335-": "CE4",
"PALMITO-black": "CE5",
"PAT11339-TRENDYBLUE": "CE6",
"PAT11384-SURFERGIRL BLUE": "CE7",
"PAT13973 FEVERFEATHER-G19A": "CE8",
"PAT14165-POP": "CE9",
"STRIPE BLUE": "CF0",
"PAT14166-POP STRIPE BLACK": "CF1",
"PAT14173-VENICE": "CF2",
"BLUE": "CF3",
"PAT14180-BIG": "CF4",
"PALM BLUE": "CF5",
"PAT14185-COMICS": "CF6",
"CORAL": "CF7",
"PAT14190-SUNSTRIPE GREEN": "CF8",
"PAT14191-": "CF9",
"SUNSTRIPE BLACK": "CG0",
"PAT14192-": "CG1",
"PALMPANTER": "CG2",
"BLACK": "CG3",
"PAT14197-": "CG4",
"FLAMINDARK": "CG5",
"BLACK": "CG6",
"PAT14209-SYMBOL BLACK": "CG7",
"PAT14608-": "CG8",
"popstripes": "CG9",
"PAT14612-PEONY": "CH0",
"PAT15011-ALL DAISY MINT": "CH1",
"PAT15112-ALL TIGER DARK BLUE": "CH2",
"PAT15115-ALL PALM YELLOW": "CH3",
"PAT15796-NAGA N00A": "CH4",
"PAT17537-TRAME": "CH5",
"WIND": "CH6",
"PAT18254-ALL WILD GREIGE": "CH7",
"Peach": "CH8",
"Peach Blossom": "CH9",
"Pelican/mystical rose": "CI0",
"Plastic Puller 14-0846tcx, cord 12-0729tcx": "CI1",
"Plastic Puller 15-1242 TCX Cord 14-1231 TCX": "CI2",
"Plastic Puller 16-1253 TCX Cord 14-1231 TCX": "CI3",
"Plastic Puller 17-4530 TCX Cord 19-4535 TCX": "CI4",
"Plastic Puller 18-0312 TCX Cord 19-0309 TCX": "CI5",
"Plastic Puller 18-0312tcx, cord 19-0309tcx": "CI6",
"Plastic Puller 19-0303 TCX Cord 17-4405 TCX": "CI7",
"Plastic Puller 19-0303TCX": "CI8",
"Cord 19-0303TCX w/ reflective ticking": "CI9",
"Plastic Puller 19-0303TCX": "CJ0",
"Cord 17-4405tcx w/ reflective ticking": "CJ1",
"Plastic puller 19-0303tcx, cord 17-4405tcx19-0303tcx": "CJ2",
"Plastic Puller 19-1531tcx, cord 18-1661tcx": "CJ3",
"Plastic Puller 19-1761 TCX Cord 18-1661 TCX": "CJ4",
"Plastic Puller 19-4540 TCX Cord 17-4730 TCX": "CJ5",
"POLAR / FLASHED-@CARBON BLACK SUPPLIER": "CJ6",
"PRINT": "CJ7",
"QI407": "CJ8",
"QL305": "CJ9",
"Radiation": "CK0",
"RAINBOW SORBET": "CK1",
"Range Stripe": "CK2",
"Range Stripe/papaya juice": "CK3",
"REALLY ROYAL": "CK4",
"Reflective Black": "CK5",
"Reflective Silver": "CK6",
"SAB 	R-Matte Lt.Black Nickel R514": "CK7",
"SAB 0871": "CK8",
"SAB 1556": "CK9",
"SAB 1757": "CL0",
"SAB 2543": "CL1",
"SAB 3887": "CL2",
"SAB 4307": "CL3",
"SAB 4382": "CL4",
"Safari": "CL5",
"Scotdic CN10 Black": "CL6",
"SCOTDIC CN-10 M": "CL7",
"scuba lime": "CL8",
"Sea Salt": "CL9",
"Sea Wave": "CM0",
"Shark": "CM1",
"SHENGHONG-CARBON BLACK": "CM2",
"SI412": "CM3",
"Slate Blue": "CM4",
"SOLID BLACK SOOT": "CM5",
"SOLID BRILLIANT RED": "CM6",
"SOLID REALLY ROYAL": "CM7",
"Spicy": "CM8",
"Spring Blue": "CM9",
"Stock": "CN0",
"Stone Green": "CN1",
"Summer Peach": "CN2",
"SUNDAY FLORAL PRINT": "CN3",
"SUNNY SIDE UP": "CN4",
"Sunset Orange": "CN5",
"Synapse": "CN6",
"Synapse/greystone": "CN7",
"TCX-GREIGE": "CN8",
"TEXTURE DRIP STRIPE": "CN9",
"TEXTURE DRIP STRIPE/Bubblegum Pink/Blue Fish": "CO0",
"TEXTURE DRIP STRIPE/Turquoise blue": "CO1",
"topiart green": "CO2",
"Topiary Green": "CO3",
"TROPICAL PRINT/Pink": "CO4",
"Turquoise Blue": "CO5",
"UNKNOWN COLOR": "CO6",
"VE01536-P06882- N13A": "CO7",
"Vivid White": "CO8",
"Warp Red": "CO9",
"White": "CP0",
"White/Black": "CP1",
"Wild Fuchsia": "CP2",
"Wild Geranium": "CP3",
"Wild Geranium, Wild Geranium": "CP4",
"WRHT_001FSC": "CP5",
"X6-Matte Black Enamel": "CP6",
"Yellow": "CP7",
"YKK 056": "CP8",
"YKK 066": "CP9",
"YKK 071": "CQ0",
"YKK 149": "CQ1",
"YKK 292": "CQ2",
"YKK 311": "CQ3",
"YKK 377": "CQ4",
"YKK 385": "CQ5",
"YKK 398": "CQ6",
"YKK 512": "CQ7",
"YKK 533": "CQ8",
"YKK 542": "CQ9",
"YKK 553": "CR0",
"YKK 580": "CR1",
"YKK 842": "CR2",
"YKK 880": "CR3",
"YKK 960": "CR4",
"YKK H3": "CR5"}


database_3 = {"No Size": "AA0",
"1 inch": "AA1",
"1.5 MM": "AA2",
"5 MM": "AA3",
"10 MM": "AA4",
"15 MM": "AA5",
"30 MM": "AA6",
"10/11Y": "AA7",
"10/11Y=54 CM": "AA8",
"10=23 CM": "AA9",
"10=55 CM": "AB0",
"10=57 CM": "AB1",
"10=64 CM": "AB2",
"101 Cm": "AB3",
"10-11 Y": "AB4",
"10-11 y21 cm": "AB5",
"10-11 years": "AB6",
"10-11 years  14": "AB7",
"10-11 years  52": "AB8",
"10-11/ans 14": "AB9",
"10-11/ans 56": "AC0",
"10-11=16 CM": "AC1",
"10-11=62 CM": "AC2",
"10-11Y": "AC3",
"10-11Y=56 CM": "AC4",
"10-12 Years": "AC5",
"10-12=12 CM": "AC6",
"10-12Y": "AC7",
"102 Cm": "AC8",
"104 Cm": "AC9",
"106 Cm": "AD0",
"108 Cm": "AD1",
"10Y": "AD2",
"11 MM": "AD3",
"110 Cm": "AD4",
"113 Cm": "AD5",
"115 Cm": "AD6",
"12 MM": "AD7",
"12*21": "AD8",
"12.5 MM": "AD9",
"12/13Y=58 CM": "AE0",
"12=19 CM": "AE1",
"12=24 CM": "AE2",
"12=59 CM": "AE3",
"12=68 CM": "AE4",
"12-13 y21 cm": "AE5",
"12-13 years": "AE6",
"12-13 years 15": "AE7",
"12-13 years 56": "AE8",
"12-13=18 CM": "AE9",
"12-13=64 CM": "AF0",
"12-13ans 14": "AF1",
"12-13ans 59": "AF2",
"12-13Y=60 CM": "AF3",
"12-14 Years": "AF4",
"12-14=14 CM": "AF5",
"12-14-14 CM": "AF6",
"12-24=30": "AF7",
"12M": "AF8",
"12M/PCB-42": "AF9",
"12Y": "AG0",
"14 Cm": "AG1",
"14/15Y": "AG2",
"14/15Y=62 CM": "AG3",
"14=20 CM": "AG4",
"14=26 CM": "AG5",
"14=63 CM": "AG6",
"14=64 CM": "AG7",
"14=70 CM": "AG8",
"14-15 y23 cm": "AG9",
"14-15 years": "AH0",
"14-15 years 16": "AH1",
"14-15 years 61.5": "AH2",
"14-15=18 CM": "AH3",
"14-15=20 CM": "AH4",
"14-15=65 CM": "AH5",
"14-15ans 14": "AH6",
"14-15ans 63": "AH7",
"14-15Y=62 CM": "AH8",
"14-16 Years": "AH9",
"14-16-14 CM": "AI0",
"14-16Y": "AI1",
"14Y": "AI2",
"14Y 20 Cm": "AI3",
"15 CM": "AI4",
"16 Cm": "AI5",
"16 MM": "AI6",
"16x22 inch": "AI7",
"16.00*25.00*0.0250": "AI8",
"18 Cm": "AI9",
"18M": "AJ0",
"18M/PCB-42": "AJ1",
"19 Cm": "AJ2",
"19 MM": "AJ3",
"2 MM": "AJ4",
"2 PART": "AJ5",
"2.5 MM": "AJ6",
"20 Cm": "AJ7",
"20 MM": "AJ8",
"20X45MM": "AJ9",
"22.75 * 16.55 * 0.0250 Inch": "AK0",
"2-3 years": "AK1",
"2-3 years 38": "AK2",
"2-3=40 CM": "AK3",
"2-3A": "AK4",
"2-3A 38 Cm": "AK5",
"2-3Y/PCB-40": "AK6",
"2-3Y=9 CM": "AK7",
"24.5x34.5 inch": "AK8",
"24/27": "AK9",
"24050135 S": "AL0",
"2450137 M": "AL1",
"2450138 2XL": "AL2",
"2450139 L": "AL3",
"2450140 3XL": "AL4",
"2450141 XL": "AL5",
"2450199 S": "AL6",
"2450200 XS": "AL7",
"2450201 L": "AL8",
"2450202 M": "AL9",
"2450203 3XL": "AM0",
"2450204 4XL": "AM1",
"2450205 XL": "AM2",
"2450206 2XL": "AM3",
"24M": "AM4",
"24M/PCB-40": "AM5",
"25 MM": "AM6",
"2-5=35 MM": "AM7",
"26*28*6 cm": "AM8",
"26+5+5*55 cm": "AM9",
"26x40+6 Cm": "AN0",
"28 Cm": "AN1",
"28x20+6 Cm": "AN2",
"2MM": "AN3",
"2XL Size": "AN4",
"2XL / W38 L31": "AN5",
"2XL / W41 L34": "AN6",
"2XL 102": "AN7",
"2XL 20": "AN8",
"2XL 24": "AN9",
"2XL 25": "AO0",
"2XL 68 Cm": "AO1",
"2XL 70": "AO2",
"2XL 72 Cm": "AO3",
"2XL 74": "AO4",
"2XL//25CM": "AO5",
"2XL=130 CM": "AO6",
"2XL=163 CM": "AO7",
"2XL=164": "AO8",
"2XL=21 CM": "AO9",
"2XL=68 CM": "AP0",
"2XL=70 CM": "AP1",
"2XL=76 CM": "AP2",
"2XL=78 CM": "AP3",
"2XL=80 CM": "AP4",
"2XL=82 CM": "AP5",
"2XL=88 CM": "AP6",
"2XL-3XL 70 cm": "AP7",
"2XL--4XL 22 Cm": "AP8",
"2XL-4XL=22 CM": "AP9",
"2XL-5XL 19.5 Cm": "AQ0",
"3 MM": "AQ1",
"3 Y=16 CM": "AQ2",
"3 Y=40 CM": "AQ3",
"3 Years": "AQ4",
"3 inch": "AQ5",
"3=37 CM": "AQ6",
"30 X 42 Cm": "AQ7",
"30 x 60 Cm": "AQ8",
"30 inch / S (L33)": "AQ9",
"30.5 CM": "AR0",
"30+4+4+70 Cm": "AR1",
"30X200MM": "AR2",
"32 inch / M (L33)": "AR3",
"34 -30": "AR4",
"3-4 years": "AR5",
"3-4 years 40": "AR6",
"34 inch / L (L34)": "AR7",
"34.50*24.50*0.0250": "AR8",
"3-4=42 CM": "AR9",
"34-36=11 CM": "AS0",
"34-36=14 CM": "AS1",
"34-36=18 CM": "AS2",
"34-38=11 CM": "AS3",
"34-38=19 CM": "AS4",
"3-4Y": "AS5",
"3-4Y 40 Cm": "AS6",
"3-4Y/PCB-38": "AS7",
"3-4Y=11 CM": "AS8",
"35 MM": "AS9",
"36 14": "AT0",
"36 62 Cm": "AT1",
"36 L-30": "AT2",
"36=88 CM": "AT3",
"37 inch / XL (L34)": "AT4",
"38 14": "AT5",
"38 62 Cm": "AT6",
"38 L-31": "AT7",
"38/40=14 CM": "AT8",
"38/40=30.5": "AT9",
"38=122 CM": "AU0",
"38=90 CM": "AU1",
"38-42=12 CM": "AU2",
"38-42=15 CM": "AU3",
"38-42=17 CM": "AU4",
"38-42=19 CM": "AU5",
"38-44=17 CM": "AU6",
"3XL Size": "AU7",
"3XL / W41 L31": "AU8",
"3XL / W44 L34": "AU9",
"3XL 102": "AV0",
"3XL- 19.5 cm": "AV1",
"3XL 20": "AV2",
"3XL 24": "AV3",
"3XL 26.5": "AV4",
"3XL 70 Cm": "AV5",
"3XL 72": "AV6",
"3XL 74 Cm": "AV7",
"3XL 76": "AV8",
"3XL=22 CM": "AV9",
"3XL=70 CM": "AW0",
"3XL=80 CM": "AW1",
"3XL=88 CM": "AW2",
"3XL-4XL 19.5": "AW3",
"3XL-5XL 19.5 cm": "AW4",
"3XL-5XL//27CM": "AW5",
"4 Y=17 CM": "AW6",
"4 Y=42 CM": "AW7",
"4 Years": "AW8",
"4=42 CM": "AW9",
"40 16": "AX0",
"40 64": "AX1",
"40 64 Cm": "AX2",
"40 L-31": "AX3",
"40 MM": "AX4",
"40=125 CM": "AX5",
"40=90 CM": "AX6",
"40-46=20 CM": "AX7",
"40-48=13 CM": "AX8",
"40X30X20": "AX9",
"41 inch / 2XL (L34)": "AY0",
"42 16": "AY1",
"42 64 Cm": "AY2",
"42 L-31": "AY3",
"42*20'' 7+7": "AY4",
"42/44=32.5": "AY5",
"42=128 CM": "AY6",
"42=90 CM": "AY7",
"42-46=16 CM": "AY8",
"44 18": "AY9",
"44 66": "AZ0",
"44 66 Cm": "AZ1",
"44 L-31": "AZ2",
"44 inch / 3XL (L34)": "AZ3",
"44/46=18 CM": "AZ4",
"44=132 CM": "AZ5",
"44=92 CM": "AZ6",
"44-46=13 CM": "AZ7",
"44-46=16 CM": "AZ8",
"44-46=20 CM": "AZ9",
"45 MM": "BA0",
"4-5 years": "BA1",
"4-5 years 43": "BA2",
"45*75 cm": "BA3",
"4-5=46 CM": "BA4",
"45MM": "BA5",
"4-5Y 44 Cm": "BA6",
"4-5Y/PCB-38": "BA7",
"4-5Y=11 CM": "BA8",
"46 18": "BA9",
"46 66 Cm": "BB0",
"46 Cm": "BB1",
"46 L31": "BB2",
"46=136 CM": "BB3",
"46=18 CM": "BB4",
"46=34.5": "BB5",
"46=92 CM": "BB6",
"48 20": "BB7",
"48 68 Cm": "BB8",
"48 Cm": "BB9",
"48 inch / 4XL (L34)": "BC0",
"48=140 CM": "BC1",
"48=21 CM": "BC2",
"4XL Size": "BC3",
"4XL 72 cm": "BC4",
"4XL 76 Cm": "BC5",
"4XL/ W48 L34": "BC6",
"4XL=78 CM": "BC7",
"5 MM": "BC8",
"5 PART": "BC9",
"5 Y=19 CM": "BD0",
"5 Y=47 CM": "BD1",
"5 Years": "BD2",
"5 inch": "BD3",
"5=45 CM": "BD4",
"50 Cm": "BD5",
"50 MM": "BD6",
"50*80 cm": "BD7",
"50=144 CM": "BD8",
"50=149 CM": "BD9",
"52 Cm": "BE0",
"52=149 CM": "BE1",
"56 cm": "BE2",
"5-6 years": "BE3",
"5-6 years  45": "BE4",
"5-6=14 CM": "BE5",
"5-6=48 CM": "BE6",
"5-6=56 CM": "BE7",
"5-6ans 12": "BE8",
"5-6ans 47": "BE9",
"5-6Y 46 Cm": "BF0",
"5-6Y/PCB-38": "BF1",
"5-6Y=11 CM": "BF2",
"6 PART": "BF3",
"6=21 CM": "BF4",
"6=48 CM": "BF5",
"6=52 CM": "BF6",
"6=58 CM": "BF7",
"60 Cm": "BF8",
"60X20X20": "BF9",
"60X40X20": "BG0",
"60X40X40": "BG1",
"61 cm": "BG2",
"6-10=18 CM": "BG3",
"62 Cm": "BG4",
"62X86MM": "BG5",
"63 cm": "BG6",
"64 Cm": "BG7",
"65 cm": "BG8",
"66 Cm": "BG9",
"68 Cm": "BH0",
"6-8 Years": "BH1",
"6-8=12 CM": "BH2",
"6Y": "BH3",
"6Y-12Y 18 Cm": "BH4",
"7 MM": "BH5",
"7/8Y=50 CM": "BH6",
"70 cm": "BH7",
"7-11Y=16 CM": "BH8",
"7-8 y 19  cm": "BH9",
"7-8 years": "BI0",
"7-8 years 12.5": "BI1",
"7-8 years 48": "BI2",
"7-8=14 CM": "BI3",
"7-8=58 CM": "BI4",
"7-8ans 12": "BI5",
"7-8ans 49": "BI6",
"7-8Y=50 CM": "BI7",
"8 MM": "BI8",
"8/9Y": "BI9",
"8/9Y=52 CM": "BJ0",
"8=22 CM": "BJ1",
"8=50 CM": "BJ2",
"8=55 CM": "BJ3",
"8=62 CM": "BJ4",
"8-10 Years": "BJ5",
"8-10-12 CM": "BJ6",
"85 Cm": "BJ7",
"86 Cm": "BJ8",
"87 Cm": "BJ9",
"88 Cm": "BK0",
"8-9 y21 cm": "BK1",
"8-9 years": "BK2",
"8-9 years 13": "BK3",
"8-9 years 50": "BK4",
"8-9=16 CM": "BK5",
"8-9=60 CM": "BK6",
"8-9ans 14": "BK7",
"8-9ans 53": "BK8",
"8-9Y=52 CM": "BK9",
"8MM": "BL0",
"8Y": "BL1",
"9 inch": "BL2",
"90 Cm": "BL3",
"92 Cm": "BL4",
"17 CM": "BL5",
"22 CM": "BL6",
"DCB-418": "BL7",
"DCB-422": "BL8",
"DCB-521": "BL9",
"DCB-530": "BM0",
"DCB-616": "BM1",
"DCT-238": "BM2",
"DCT-338": "BM3",
"DCT-342": "BM4",
"IU": "BM5",
"L Size": "BM6",
"L / W33 L31": "BM7",
"L / W34 L34": "BM8",
"L 100": "BM9",
"L 18": "BN0",
"L 22": "BN1",
"L 23": "BN2",
"L 63 cm": "BN3",
"L 66 cm": "BN4",
"L 68": "BN5",
"L 70 Cm": "BN6",
"L=116 CM": "BN7",
"L=143 CM": "BN8",
"L=20 CM": "BN9",
"L=64 CM": "BO0",
"L=66 CM": "BO1",
"L=72 CM": "BO2",
"L=76 CM": "BO3",
"L=80 CM": "BO4",
"L=84 CM": "BO5",
"L-2XL 18 cm": "BO6",
"L-2XL=13.5": "BO7",
"L-2XL=20 CM": "BO8",
"L-2XL=23.5": "BO9",
"L-3XL=18 CM": "BP0",
"Lw34,L34": "BP1",
"L-XL 66 Cm": "BP2",
"L-XL//23CM": "BP3",
"M Size": "BP4",
"M / W30 L31": "BP5",
"M / W32 L33": "BP6",
"M 18": "BP7",
"M 20.5": "BP8",
"M 22": "BP9",
"M 62 cm": "BQ0",
"M 64": "BQ1",
"M 66": "BQ2",
"M 68 Cm": "BQ3",
"M 99": "BQ4",
"M=111 CM": "BQ5",
"M=134": "BQ6",
"M=138 CM": "BQ7",
"M=20 CM": "BQ8",
"M=62 CM": "BQ9",
"M=64 CM": "BR0",
"M=70 CM": "BR1",
"M=74 CM": "BR2",
"M=78 CM": "BR3",
"M=82 CM": "BR4",
"Mw32,L33": "BR5",
"M-XL 18 Cm": "BR6",
"M-XL=20 CM": "BR7",
"S Size": "BR8",
"S / W28 L31": "BR9",
"S / W30 L33": "BS0",
"S 18": "BS1",
"S 19": "BS2",
"S 22": "BS3",
"S 61 cm": "BS4",
"S 64": "BS5",
"S 66": "BS6",
"S 68 Cm": "BS7",
"S 99": "BS8",
"S,M,L=18 CM": "BS9",
"S,M=16 CM": "BT0",
"S,M=18 CM": "BT1",
"S=106 CM": "BT2",
"S=128 CM": "BT3",
"S=132 CM": "BT4",
"S=19 CM": "BT5",
"S=62 CM": "BT6",
"S=64 CM": "BT7",
"S=70 CM": "BT8",
"S=74 CM": "BT9",
"S=78 CM": "BU0",
"S=82 CM": "BU1",
"S-2XL=16 CM": "BU2",
"S-L=30": "BU3",
"S-M 17": "BU4",
"S-M 64 cm": "BU5",
"Sw30,L33": "BU6",
"S--XL 20 Cm": "BU7",
"S-XL=20 CM": "BU8",
"UK10 / M (L31)": "BU9",
"UK12-14 / L (L31)": "BV0",
"UK14-16 / XL(L31)": "BV1",
"UK18 / 2XL (L31)": "BV2",
"UK20-22/3XL(L31)": "BV3",
"UK4-6 / XS (L30)": "BV4",
"UK6-8 / S (L31)": "BV5",
"XL Size": "BV6",
"XL / W35 L31": "BV7",
"XL / W37 L34": "BV8",
"XL 100": "BV9",
"XL 20": "BW0",
"XL 23": "BW1",
"XL 23.5": "BW2",
"XL 65.5 cm": "BW3",
"XL 68": "BW4",
"XL 68 cm": "BW5",
"XL 70": "BW6",
"XL 70 Cm": "BW7",
"XL 72": "BW8",
"XL,2XL,3XL=20 CM": "BW9",
"XL=123 CM": "BX0",
"XL=153": "BX1",
"XL=153 CM": "BX2",
"XL=21 CM": "BX3",
"XL=66 CM": "BX4",
"XL=68 CM": "BX5",
"XL=74 CM": "BX6",
"XL=76 CM": "BX7",
"XL=78 CM": "BX8",
"XL=80 CM": "BX9",
"XL=86 CM": "BY0",
"XL-2XL=32": "BY1",
"XLw37,L34": "BY2",
"XS Size": "BY3",
"XS / W26 L30": "BY4",
"XS 21": "BY5",
"XS 62 cm": "BY6",
"XS 64": "BY7",
"XS~S=18 CM": "BY8",
"XS=15 CM": "BY9",
"XS=19 CM": "BZ0",
"XS=28": "BZ1",
"XS=60 CM": "BZ2",
"XS=68 CM": "BZ3",
"XS=72 CM": "BZ4",
"XS=76 CM": "BZ5",
"XS-M 17 cm": "BZ6",
"XS-M//21CM": "BZ7",
"XS-M=11.5": "BZ8",
"XS-M=19 CM": "BZ9",
"XS-M=21.5": "CA0",
"XS-S 17 Cm": "CA1",
"XXS~XS=16 CM": "CA2",}

# Define a function to check for matches in the databases
def check_databases(row):
    code = ''
    for word, value in database_1.items():
        if word.lower() in row.lower():
            code += value
            break
    else:
        code += 'none1'
    for word, value in database_2.items():
        if word.lower() in row.lower():
            code += value
            break
    else:
        code += 'none2'
    for word, value in database_3.items():
        if word.lower() in row.lower():
            code += value
            break
    else:
        code += 'none3'
    return code

# Apply the function to the new column and create a new dataframe with all columns and the 'codes' column
output_file = input_file.copy()
output_file.insert(0, 'HKD code', output_file['new_column'].apply(check_databases))
output_file.drop(columns='new_column', inplace=True)

# Save the result to a new file
output_file.to_excel('output_file.xlsx', index=False)
