from django.contrib import admin
from main.models import  *

#<Банки>
# class Bankiinadmin(admin.ModelAdmin):
#     fields = ['EtoGruppa','Naimenovanie', 'KorrSchet', 'Kod', 'Gorod','Adres', 'Telefony', 'PometkaUdaleniya']
#     list_display = ('EtoGruppa','Naimenovanie', 'KorrSchet', 'Kod', 'Gorod','Adres', 'Telefony', 'PometkaUdaleniya',)
#     list_filter = ('Gorod', 'EtoGruppa')

class GruppyBankovinadmin(admin.ModelAdmin):
    fields = ['text', 'kod']
    list_display = ('text', 'kod',)
#</Банки>

#<Склады>
# class Skladyinadmin(admin.ModelAdmin):
#     list_display = ('EtoGruppa','Naimenovanie', 'Roditel','VidSklada', 'TipTSenRoznichnoyTorgovli', 'NomerSektsii', 'Podrazdelenie', 'RaschetRoznichnyhTSenPoTorgovoyNatsenke', 'Kommentariy', 'PometkaUdaleniya')
#     fieldsets = [
#         (None,               {'fields': ['EtoGruppa','Naimenovanie']}),
#         ('Общие', {'fields': ['Roditel','VidSklada', 'TipTSenRoznichnoyTorgovli', 'NomerSektsii', 'Podrazdelenie', 'RaschetRoznichnyhTSenPoTorgovoyNatsenke', 'Kommentariy']}),
#         (None,               {'fields': ['PometkaUdaleniya']}),
#     ]
#     list_filter = ('EtoGruppa', 'Roditel', 'TipTSenRoznichnoyTorgovli', 'VidSklada', 'Podrazdelenie')

class GruppySkladovinadmin(admin.ModelAdmin):
    fields = ['text']
    list_display = ('text',)

class VidyPostupleniyaTovarovinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class VidyPeredachiTovarovinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class VidySkladovinadmin(admin.ModelAdmin):
    fields = ['text']
    list_display = ('text',)
#</Склады>

#Взаиморасчеты
class VidyVzaimoraschetovinadmin(admin.ModelAdmin):
	fields = ['Naimenovanie']
	list_display = ('Naimenovanie',)

class StatiDvizheniyaDenezhnyhSredstvinadmin(admin.ModelAdmin):
	fields = ['Naimenovanie']
	list_display = ('Naimenovanie',)

# #<Типы цен номенклатуры>
# class TipyTSenNomenklaturyinadmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['Naimenovanie', 'ValyutaTSeny', 'TSenaVlyuchaetNDS']}),
#         ('Порядок назначения цен', {'fields': ['VidTipaTSeny','SposobRaschetaTSeny', 'BazovyyTipTSen', 'ProtsentSkidkiNatsenki']}),
#     	('Порядок округления цен', {'fields': ['OkruglyatVBolshuyuStoronu', 'PoryadokOkrugleniya', 'Kommentariy']}),
#     	(None,               {'fields': ['PometkaUdaleniya']}),
#     ]
#     list_display = ('Naimenovanie', 'Kod', 'PometkaUdaleniya')
#     list_filter = ('ValyutaTSeny', 'VidTipaTSeny', 'SposobRaschetaTSeny', 'BazovyyTipTSen')

class VidTipaTSenyinadmin(admin.ModelAdmin):
    fields = ['text']
    list_display = ('text',)

class SposobyRaschetaTSenyinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class PoryadkiOkrugleniyainadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)
#</Типы цен номенклатуры>

# Валюты
# class Valyutyinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'Kod', 'NaimenovaniePolnoe', 'ParametryPropisiNaRusskom', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'Kod', 'NaimenovaniePolnoe', 'ParametryPropisiNaRusskom', 'PometkaUdaleniya')

# # Подразделение
# class Podrazdeleniyainadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'Roditel', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'Roditel', 'PometkaUdaleniya')
# 	list_filter = ('Roditel',)

#<Физические Лица>
# class PasportnieDannieFizLitsainadmin(admin.ModelAdmin):
# 	fields = ['VidDocumenta', 'Seriya', 'Nomer', 'DataVydachi', 'KemVydan', 'KodPodrazdeleniya', 'DataRegistratsii', 'FizLitso', 'PometkaUdaleniya']
# 	list_display = ('VidDocumenta', 'Seriya', 'Nomer', 'DataVydachi', 'KemVydan', 'KodPodrazdeleniya', 'DataRegistratsii', 'FizLitso',)
# 	def get_model_perms(self, request):
# 		return {}

# class PasportnieDannieFizLitsainline(admin.StackedInline):
#     model = PasportnieDannieFizLitsa
#     extra = 0

# class DokumentyUdostoveryayuschieLichnostinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'KodIMNS', 'KodPFR', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'KodIMNS', 'KodPFR', 'PometkaUdaleniya')
# 	def get_model_perms(self, request):
# 		return {}

# class FizicheskieLitsainadmin(admin.ModelAdmin):
# 	fieldsets = [
#         (None,               {'fields': ['Naimenovanie']}),
#         ('Основные', {'fields': ['DataRozhdeniya','OsnovnoeIzobrazhenie', 'KontaktnayaInformatsiya']}),
#         (None,               {'fields': ['PometkaUdaleniya']}),
#     ]
# 	list_display = ('Naimenovanie', 'DataRozhdeniya', 'OsnovnoeIzobrazhenie', 'KontaktnayaInformatsiya', 'PometkaUdaleniya')
# 	inlines = [PasportnieDannieFizLitsainline,]
#</Физические Лица>

# class TarifyZaRaschetnoeObsluzhivanieinadmin(admin.ModelAdmin):
# 	fields = ['VidOplaty', 'ProtsentTorgovoyUstupki', 'PometkaUdaleniya']
# 	list_display = ('VidOplaty', 'ProtsentTorgovoyUstupki', 'PometkaUdaleniya')

# class TarifyZaRaschetnoeObsluzhivanieinline(admin.StackedInline):
# 	model = TarifyZaRaschetnoeObsluzhivanie
# 	extra = 0
# 	fields = ['VidOplaty', 'ProtsentTorgovoyUstupki']

# Договоры эквайринга
# class DogovoryEkvayringainadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'Ekvayrer', 'DogovorVzaimoraschetov', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'Ekvayrer', 'DogovorVzaimoraschetov', 'PometkaUdaleniya')
# 	inlines = [TarifyZaRaschetnoeObsluzhivanieinline,]
# 	list_filter = ('Ekvayrer', 'DogovorVzaimoraschetov')

class TipyOplatCHekaKKMinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

# class Nomenklaturainadmin(admin.ModelAdmin):
# 	fieldsets = [
#         (None,               {'fields': ['OsnovnoeIzobrazhenie','Naimenovanie', 'Artikul', 'VidNomenklatury', 'BazovayaEdinitsaIzmereniya', 'VestiUchetPoHarakteristikam', 'EdinitsaHraneniyaOstatkov', 'VestiUchetPoSeriyam', 'EdinitsaDlyaOtchetov', 'VestiPartionnyyUchetPoSeriyam', 'EdinitsaIzmereniyaMest']}),
#         ('По умолчанию', {'fields': ['Vesovoy', 'StavkaNDS', 'StatyaZatrat', 'NomenklaturnayaGruppaZatrat', 'Kommentariy']}),
#         (None,               {'fields': ['PometkaUdaleniya']}),
#     ]
# 	list_display = ('Naimenovanie', 'Artikul', 'PometkaUdaleniya')
# 	list_filter = ('VidNomenklatury', 'BazovayaEdinitsaIzmereniya', 'StavkaNDS','StatyaZatrat', 'NomenklaturnayaGruppaZatrat')

# class VidyNomenklaturyinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'TipNomenklatury', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'TipNomenklatury', 'PometkaUdaleniya')
# 	list_filter = ('TipNomenklatury',)

class StavkiNDSinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class TipyNomenklaturyinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class VidyZatratinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

# class KlassifikatorEdinitsIzmereniyainadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'MezhdunarodnoeSokraschenie', 'Kod', 'NaimenovaniePolnoe', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'MezhdunarodnoeSokraschenie', 'Kod', 'NaimenovaniePolnoe', 'PometkaUdaleniya')
# 	def get_model_perms(self, request):
# 		return {}

# class StatiZatratinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'VidZatrat', 'HarakterZatrat', 'OtnesenieRashodovKDeyatelnostiENVD', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'VidZatrat', 'HarakterZatrat', 'OtnesenieRashodovKDeyatelnostiENVD', 'PometkaUdaleniya')
# 	def get_model_perms(self, request):
# 		return {}

class HarakterZatratinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class OtnesenieRashodovKDeyatelnostiENVDinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

# Номенклатура
# class Nomenklaturainline(admin.StackedInline):
# 	model = Nomenklatura
# 	extra = 0
# 	fields = ['OsnovnoeIzobrazhenie','Naimenovanie', 'Artikul', 'VidNomenklatury', 'BazovayaEdinitsaIzmereniya', 'VestiUchetPoHarakteristikam', 'EdinitsaHraneniyaOstatkov', 'VestiUchetPoSeriyam', 'EdinitsaDlyaOtchetov', 'VestiPartionnyyUchetPoSeriyam', 'EdinitsaIzmereniyaMest', 'Vesovoy', 'StavkaNDS', 'StatyaZatrat', 'NomenklaturnayaGruppaZatrat', 'Kommentariy', 'PometkaUdaleniya']

# class NomenklaturnyeGruppyinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'StavkaNDS', 'BazovayaEdinitsaIzmereniya', 'EdinitsaHraneniyaOstatkov', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'StavkaNDS', 'BazovayaEdinitsaIzmereniya', 'EdinitsaHraneniyaOstatkov', 'PometkaUdaleniya')
# 	inlines = [Nomenklaturainline,]
# 	def get_model_perms(self, request):
# 		return {}

#Номера ГТД
# class NomeraGTDinadmin(admin.ModelAdmin):
# 	fields = ['Kod', 'Kommentariy', 'PometkaUdaleniya']
# 	list_display = ('Kod', 'Kommentariy', 'PometkaUdaleniya')

# # Типы цен номенклатуры Контрагентов
# class TipyTSenNomenklaturyKontragentovinadmin(admin.ModelAdmin):
# 	fields = ['Vladelets', 'Naimenovanie', 'TipTSenNomenklatury', 'ValyutaTSeny', 'TSenaVlyuchaetNDS', 'OpisanieTipaTSenyNomenklaturyKontragenta', 'Kommentariy', 'PometkaUdaleniya']
# 	list_display = ('Vladelets', 'Naimenovanie', 'TipTSenNomenklatury', 'ValyutaTSeny', 'TSenaVlyuchaetNDS', 'OpisanieTipaTSenyNomenklaturyKontragenta', 'Kommentariy', 'PometkaUdaleniya')
# 	list_filter = ('Vladelets', 'TipTSenNomenklatury', 'ValyutaTSeny')

# # Контрагенты
# class VidyDeyatelnostiinline(admin.StackedInline):
# 	model = VidyDeyatelnosti
# 	extra = 0
# 	fields = ['VidDeyatelnosti','Otvetstvennyy']

# class Kontragentyinadmin(admin.ModelAdmin):
# 	fieldsets = [
#         (None,               {'fields': ['Naimenovanie']}),
#         ('Общее', {'fields': ['YUrFizLitso', 'NeYAvlyaetsyaRezidentom', 'Pokupatel', 'Postavschik', 'OKOPF', 'Roditel', 'NaimenovaniePolnoe', 'INN', 'KPP', 'KodPoOKPO', 'RaspisanieRabotyStrokoy', 'Region', 'VhoditVHolding', 'GolovnoyKontragent']}),
#     	(None,               {'fields': ['PometkaUdaleniya']}),
#     ]
# 	list_display = ('Naimenovanie', 'YUrFizLitso', 'NeYAvlyaetsyaRezidentom', 'Pokupatel', 'Postavschik', 'OKOPF', 'Roditel', 'NaimenovaniePolnoe', 'INN', 'KPP', 'KodPoOKPO', 'RaspisanieRabotyStrokoy', 'Region', 'VhoditVHolding', 'GolovnoyKontragent', 'PometkaUdaleniya')
# 	inlines = [VidyDeyatelnostiinline,]
# 	list_filter = ('YUrFizLitso', 'Pokupatel','Postavschik', 'Roditel', 'Region', 'GolovnoyKontragent')

class GruppyKontragentovinadmin(admin.ModelAdmin):
    fields = ['text']
    list_display = ('text',)

# class VidyDeyatelnostiinadmin(admin.ModelAdmin):
# 	fields = ['VidDeyatelnosti', 'Otvetstvennyy', 'PometkaUdaleniya']
# 	list_display = ('VidDeyatelnosti', 'Otvetstvennyy')
# 	def get_model_perms(self, request):
# 		return {}
# ЮрФизЛица
class YUrFizLitsoinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

# class KlassifikatorOKOPFinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'NaimenovaniePolnoe', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'NaimenovaniePolnoe', 'PometkaUdaleniya')
# 	def get_model_perms(self, request):
# 		return {}
# Регионы
# class Regionyinadmin(admin.ModelAdmin):
# 	fields = ['Roditel', 'KodAdresnogoElementa', 'KodRegiona', 'Naimenovanie', 'ZHDStantsiyaNaznacheniya', 'Kommentariy', 'PometkaUdaleniya']
# 	list_display = ('Roditel', 'KodAdresnogoElementa', 'KodRegiona', 'Naimenovanie', 'ZHDStantsiyaNaznacheniya', 'Kommentariy', 'PometkaUdaleniya')
# 	def get_model_perms(self, request):
# 		return {}

class VidyDeyatelnostiKontragentovinadmin(admin.ModelAdmin):
	fields = ['Naimenovanie']
	list_display = ('Naimenovanie',)

# class KontaktnyeLitsaKontragentovinadmin(admin.ModelAdmin):
# 	fieldsets = [
#         (None,               {'fields': ['KontaktnoeLitso']}),
#         ('Личные данные', {'fields': ['DataRozhdeniya', 'Pol', 'NapominatODneRozhdeniya', 'KolichestvoDneyDoNapominaniya', 'UdostovereniyaLichnosti']}),
#         ('Данные работника', {'fields': ['Vladelets', 'Dolzhnost', 'RolKontaktnogoLitsa']}),
#         (None,               {'fields': ['Kontakty', 'Kommentariy','PometkaUdaleniya']}),
#     ]
# 	list_display = ('KontaktnoeLitso', 'Vladelets', 'Naimenovanie', 'Kod', 'Kontakty', 'Kommentariy', 'PometkaUdaleniya')
# 	list_filter = ('KontaktnoeLitso', 'Vladelets', 'RolKontaktnogoLitsa','Pol')

# Контактные Лица
# class KontaktnyeLitsainadmin(admin.ModelAdmin):
# 	fields = ['Imya', 'Familiya', 'Otchestvo', 'Naimenovanie','DataRozhdeniya','Pol', 'Kontakty', 'PometkaUdaleniya']
# 	list_display = ()
# 	def get_model_perms(self, request):
# 		return {}

class PolFizicheskihLitsinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class RoliKontaktnyhLitsinadmin(admin.ModelAdmin):
	fields = ['Naimenovanie']
	list_display = ('Naimenovanie',)

# class GruppySobytiyinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'VidObekta', 'OpisanieSobytiya', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'VidObekta', 'OpisanieSobytiya',)
# 	list_filter = ('VidObekta', 'PometkaUdaleniya')

class VidyObektovSobytiyainadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

# class VidyKontaktnoiInformatsiiinadmin(admin.ModelAdmin):
# 	fields = ['Tip', 'Naimenovanie', 'VidObektovKontaktnoiInformatsii', 'PometkaUdaleniya']
# 	list_display = ('Tip', 'Naimenovanie', 'VidObektovKontaktnoiInformatsii', 'PometkaUdaleniya')
# 	list_filter = ('Tip',)

class TipyKontaktnoiInformatsiiinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class VidyObektovKontaktnoiInformatsiiinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

# #Единицы Измерения
# class EdinitsyIzmereniyainadmin(admin.ModelAdmin):
# 	fields = ['Vladelets', 'EdinitsaPoKlassifikatoru', 'Naimenovanie', 'Ves', 'Obem', 'Koeffitsient', 'PometkaUdaleniya']
# 	list_display = ('Vladelets', 'EdinitsaPoKlassifikatoru', 'Naimenovanie', 'Ves', 'Obem', 'Koeffitsient', 'PometkaUdaleniya')
# 	list_filter = ('Vladelets','EdinitsaPoKlassifikatoru')

# Организации
# class Organizatsiiinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'YUrFizLitso', 'Prefiks','OtrazhatVReglamentirovannomUchete', 'NaimenovaniePolnoe', 'NaimenovaniePlatelschikaPriPerechisleniiNalogov', 'OsnovnoyBankovskiySchet', 'INN', 'KPP', 'OGRN', 'KodIMNS', 'SvidetelstvoDataVydachi', 'SvidetelstvoSeriyaNomer', 'KodPoOKATO', 'KodPoOKPO', 'PometkaUdaleniya']
# 	list_display = ('Naimenovanie', 'YUrFizLitso', 'Prefiks','OtrazhatVReglamentirovannomUchete', 'NaimenovaniePolnoe', 'NaimenovaniePlatelschikaPriPerechisleniiNalogov', 'OsnovnoyBankovskiySchet', 'INN', 'KPP', 'OGRN', 'KodIMNS', 'SvidetelstvoDataVydachi', 'SvidetelstvoSeriyaNomer', 'KodPoOKATO', 'KodPoOKPO', 'PometkaUdaleniya')
# 	list_filter = ('YUrFizLitso','OsnovnoyBankovskiySchet')

# class BankovskieSchetainadmin(admin.ModelAdmin):
# 	fields = ['NomerScheta', 'VidScheta', 'ValyutaDenezhnyhSredstv', 'BIKBanka', 'KorrschetBanka', 'PryamieRaschety', 'RedaktirovatTekstKorrespondenta', 'TekstKorrespondenta', 'MesyatsPropisyu', 'SummaBezKopeek', 'DataOtkrytiya', 'DataZakrytiya', 'Naimenovanie', 'PometkaUdaleniya']
# 	list_display = ('NomerScheta', 'VidScheta', 'ValyutaDenezhnyhSredstv', 'BIKBanka', 'KorrschetBanka', 'PryamieRaschety', 'RedaktirovatTekstKorrespondenta', 'TekstKorrespondenta', 'MesyatsPropisyu', 'SummaBezKopeek', 'DataOtkrytiya', 'DataZakrytiya', 'Naimenovanie',)
# 	def get_model_perms(self, request):
# 		return {}

# class DogovoryKontragentovinadmin(admin.ModelAdmin):
# 	fieldsets = [
#         (None,               {'fields': ['Organizatsiya', 'Vladelets', 'Roditel', 'Naimenovanie', 'VidDogovora', 'Nomer', 'Data', 'SrokDeystviya']}),
#         ('Общее', {'fields': ['VedenieVzaimoraschetov', 'ValyutaVzaimoraschetov', 'VestiPoDokumentamRaschetovSKontragentom','RaschetyVUslovnyhEdinitsah', 'RealizatsiyaNaEksport', 'VidVzaimoraschetov', 'VidUsloviyDogovora', 'KontrolirovatSummuZadolzhennosti', 'DopustimayaSummaZadolzhnosti']}),
#         (None,               {'fields': ['PometkaUdaleniya']}),
#     ]
# 	list_display =('Organizatsiya', 'Vladelets', 'Roditel', 'Naimenovanie', 'VidDogovora', 'Nomer', 'Data', 'SrokDeystviya', 'VedenieVzaimoraschetov', 'ValyutaVzaimoraschetov', 'VestiPoDokumentamRaschetovSKontragentom','RaschetyVUslovnyhEdinitsah', 'RealizatsiyaNaEksport', 'VidVzaimoraschetov', 'VidUsloviyDogovora', 'KontrolirovatSummuZadolzhennosti', 'DopustimayaSummaZadolzhnosti',)
# 	def get_model_perms(self, request):
# 		return {}

class VidyDogovorovKontragentovinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class VedenieVzaimoraschetovPoDogovoraminadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class VidyUsloviyDogovorovVzaimoraschetovinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class SposobyRaspredeleniyaDopRashodovinadmin(admin.ModelAdmin):
	fields = ['text']
	list_display = ('text',)

class DolzhnostiOrganizatsiyinadmin(admin.ModelAdmin):
	fields = ['Naimenovanie']
	list_display = ('Naimenovanie',)

# class Kassyinadmin(admin.ModelAdmin):
# 	fields = ['Vladelets', 'Roditel', 'Naimenovanie', 'ValyutaDenezhnyhSredstv', 'Otvetstvennyy']
# 	list_display = ('Vladelets', 'Roditel', 'Naimenovanie', 'ValyutaDenezhnyhSredstv', 'Otvetstvennyy',)

# class KassyKKMinadmin(admin.ModelAdmin):
# 	fields = ['Vladelets', 'Naimenovanie', 'FormirovatNefiskalnyeCHeki']
# 	list_display = ('Vladelets', 'Naimenovanie', 'FormirovatNefiskalnyeCHeki',)

# class VidyOplatCHekaKKMinadmin(admin.ModelAdmin):
# 	fields = ['Naimenovanie', 'TipOplaty', 'BankKreditor', 'DogovorVzaimoraschetovBankaKreditora', 'ProtsentBankovskoyKomissii']
# 	list_display = ('Naimenovanie', 'TipOplaty',)

# class VozvratTovarovOtPokupatelyainadmin(admin.ModelAdmin):
# 	fields = ['Nomer'] 
# 	list_display = ('Nomer',)

admin.site.register(SposobyRaspredeleniyaDopRashodov, SposobyRaspredeleniyaDopRashodovinadmin)
admin.site.register(DolzhnostiOrganizatsiy, DolzhnostiOrganizatsiyinadmin)
admin.site.register(StatiDvizheniyaDenezhnyhSredstv, StatiDvizheniyaDenezhnyhSredstvinadmin)


admin.site.register(VidyUsloviyDogovorovVzaimoraschetov, VidyUsloviyDogovorovVzaimoraschetovinadmin)
admin.site.register(VedenieVzaimoraschetovPoDogovoram, VedenieVzaimoraschetovPoDogovoraminadmin)
admin.site.register(VidyDogovorovKontragentov, VidyDogovorovKontragentovinadmin)
admin.site.register( VidyObektovKontaktnoiInformatsii,VidyObektovKontaktnoiInformatsiiinadmin )
admin.site.register( TipyKontaktnoiInformatsii, TipyKontaktnoiInformatsiiinadmin)
admin.site.register( VidyObektovSobytiya, VidyObektovSobytiyainadmin)
admin.site.register( RoliKontaktnyhLits, RoliKontaktnyhLitsinadmin)
admin.site.register( PolFizicheskihLits, PolFizicheskihLitsinadmin)
admin.site.register( VidyDeyatelnostiKontragentov, VidyDeyatelnostiKontragentovinadmin)
admin.site.register( YUrFizLitso, YUrFizLitsoinadmin)
admin.site.register( GruppyKontragentov, GruppyKontragentovinadmin)
admin.site.register( OtnesenieRashodovKDeyatelnostiENVD, OtnesenieRashodovKDeyatelnostiENVDinadmin)
admin.site.register( HarakterZatrat, HarakterZatratinadmin)
admin.site.register( VidyZatrat, VidyZatratinadmin)
admin.site.register( TipyNomenklatury, TipyNomenklaturyinadmin)
admin.site.register( StavkiNDS, StavkiNDSinadmin)
admin.site.register( TipyOplatCHekaKKM, TipyOplatCHekaKKMinadmin)
admin.site.register( PoryadkiOkrugleniya, PoryadkiOkrugleniyainadmin)
admin.site.register( SposobyRaschetaTSeny, SposobyRaschetaTSenyinadmin)
admin.site.register( VidTipaTSeny, VidTipaTSenyinadmin)
admin.site.register( VidySkladov, VidySkladovinadmin)
admin.site.register( GruppySkladov, GruppySkladovinadmin)
admin.site.register( GruppyBankov, GruppyBankovinadmin)
admin.site.register( VidyVzaimoraschetov, VidyVzaimoraschetovinadmin)
admin.site.register( VidyPostupleniyaTovarov, VidyPostupleniyaTovarovinadmin)
admin.site.register( VidyPeredachiTovarov, VidyPeredachiTovarovinadmin)