from django import forms
from django.contrib import admin
from main.models import *



# Документы
class InventarizatsiyaTovarovNaSkladeForm(forms.ModelForm):
	class Meta:
		model = InventarizatsiyaTovarovNaSklade
		fields = '__all__'

class UstanovkaTSenNomenklaturyForm(forms.ModelForm):
	class Meta:
		model = UstanovkaTSenNomenklatury
		fields = '__all__'

class VozvratTovarovOtPokupatelyaForm(forms.ModelForm):
	class Meta:
		model = VozvratTovarovOtPokupatelya
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}


class ZakazPokupatelyaForm(forms.ModelForm):
	class Meta:
		model = ZakazPokupatelya
		fields = '__all__'

class ZakazPostavschikuForm(forms.ModelForm):
	class Meta:
		model = ZakazPostavschiku
		fields = '__all__'

class DoverennostiForm(forms.ModelForm):
	class Meta:
		model = Doverennosti
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataDeystviya': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}


class OtchetORoznichnyhProdazhahForm(forms.ModelForm):
	class Meta:
		model = OtchetORoznichnyhProdazhah
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class CHekKKMForm(forms.ModelForm):
	class Meta:
		model = CHekKKM
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class GTDImportForm(forms.ModelForm):
	class Meta:
		model = GTDImport
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class PostuplenieDopRashodovForm(forms.ModelForm):
	class Meta:
		model = PostuplenieDopRashodov
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataVhodyaschegoDokumenta': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

	   
class SchetFakturaPoluchennyyForm(forms.ModelForm):
	class Meta:
		model = SchetFakturaPoluchennyy
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataVhodyaschegoDokumenta': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}


class VozvratTovarovPostavschikuForm(forms.ModelForm):
	class Meta:
		model = VozvratTovarovPostavschiku
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

	

class PostuplenieTovarovUslugForm(forms.ModelForm):
	class Meta:
		model = PostuplenieTovarovUslug
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataVhodyaschegoDokumenta': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}


class ZakazPokupatelyaForm(forms.ModelForm):
	class Meta:
		model = ZakazPokupatelya
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataOplaty': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataOtgruzki': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

	

class SchetFakturaVydannyyForm(forms.ModelForm):
	class Meta:
		model = SchetFakturaVydannyy
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataPlatezhnoRaschetnogoDokumenta': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}
	

class RealizatsiyaTovarovUslugForm(forms.ModelForm):
	class Meta:
		model = RealizatsiyaTovarovUslug
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DoverennostData': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class SchetNaOplatuPokupatelyuForm(forms.ModelForm):
	class Meta:
		model = SchetNaOplatuPokupatelyu
		fields = '__all__'
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataOplaty': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataOtgruzki': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

# Таблицы 

class TipyTsenForm(forms.ModelForm):
	class Meta:
		model = TipyTsen
		fields = '__all__'

class KursyValyutForm(forms.ModelForm):
	class Meta:
		model = KursyValyut
		fields = '__all__'
		widgets = {
			'Period': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class TovaryForm(forms.ModelForm):
	class Meta:
		model = Tovary
		fields = '__all__'

class OtvetstvennyeLitsaOrganizatsiiForm(forms.ModelForm):
	class Meta:
		model = OtvetstvennyeLitsaOrganizatsii
		fields = '__all__'

class RazdelyForm(forms.ModelForm):
	class Meta:
		model = Razdely
		fields = '__all__'


class UslugiForm(forms.ModelForm):
	class Meta:
		model = Uslugi
		fields = '__all__'

class OplataForm(forms.ModelForm):
	class Meta:
		model = Oplata
		fields = '__all__'

# class PasportnieDannieFizLitsaForm(forms.ModelForm):
# 	class Meta:
# 		model = PasportnieDannieFizLitsa
# 		fields = '__all__'

class TarifyZaRaschetnoeObsluzhivanieForm(forms.ModelForm):
	class Meta:
		model = TarifyZaRaschetnoeObsluzhivanie
		fields = '__all__'

class VidyDeyatelnostiForm(forms.ModelForm):
	class Meta:
		model = VidyDeyatelnosti
		fields = '__all__'

# Cправочники:

#<Банки>
class BankiForm(forms.ModelForm):
	class Meta:
		model = Banki
		fields = ('id','Kod','EtoGruppa','Naimenovanie', 'KorrSchet', 'Gorod','Adres', 'Telefony')

# class GruppyBankovForm(forms.ModelForm):
# 	class Meta:
# 		model = GruppyBankov
# 		fields = ('kod','text')
#</Банки>

#<Склады>
class SkladyForm(forms.ModelForm):
	class Meta:
		model = Sklady
		fields = ('Kod','EtoGruppa','Naimenovanie','Roditel','VidSklada', 'TipTSenRoznichnoyTorgovli', 'NomerSektsii', 'Podrazdelenie', 
			'RaschetRoznichnyhTSenPoTorgovoyNatsenke', 'Kommentariy')

class GruppySkladovForm(forms.ModelForm):
	class Meta:
		model = GruppySkladov
		fields = ('text',)

class VidySkladovForm(forms.ModelForm):
	class Meta:
		model = VidySkladov
		fields = ('text',)
#</Склады>

#Взаиморасчеты
# class VidyVzaimoraschetovForm(forms.ModelForm):
# 	class Meta:
# 		model = VidyVzaimoraschetov
# 		fields = ('Kod','Naimenovanie')

#<Типы цен номенклатуры>
class TipyTSenNomenklaturyForm(forms.ModelForm):
	class Meta:
		model = TipyTSenNomenklatury
		fields = ('Kod','Naimenovanie', 'ValyutaTSeny', 'TSenaVlyuchaetNDS', 'VidTipaTSeny','SposobRaschetaTSeny', 'BazovyyTipTSen', 
			'ProtsentSkidkiNatsenki', 'OkruglyatVBolshuyuStoronu', 'PoryadokOkrugleniya', 'Kommentariy')

class VidTipaTSenyForm(forms.ModelForm):
	class Meta:
		model = VidTipaTSeny
		fields = ('text',)

class SposobyRaschetaTSenyForm(forms.ModelForm):
	class Meta:
		model = SposobyRaschetaTSeny
		fields = ('text',)

class PoryadkiOkrugleniyaForm(forms.ModelForm):
	class Meta:
		model = PoryadkiOkrugleniya
		fields = ('text',)
#</Типы цен номенклатуры>

# <Валюты>
class ValyutyForm(forms.ModelForm):
	class Meta:
		model = Valyuty
		fields = ('id','Kod', 'Naimenovanie', 'NaimenovaniePolnoe', 'ParametryPropisiNaRusskom')

# Подразделение
class PodrazdeleniyaForm(forms.ModelForm):
	class Meta:
		model = Podrazdeleniya
		fields = ('Kod','Naimenovanie', 'Roditel')

# #<Физические Лица>
# class PasportnieDannieFizLitsaForm(forms.ModelForm):
# 	class Meta:
# 		model = PasportnieDannieFizLitsa
# 		fields = ('VidDocumenta', 'Seriya', 'Nomer', 'DataVydachi', 'KemVydan', 'KodPodrazdeleniya', 'DataRegistratsii', 
# 			'FizLitso','PometkaUdaleniya')

# class DokumentyUdostoveryayuschieLichnostForm(forms.ModelForm):
# 	class Meta:
# 		model = DokumentyUdostoveryayuschieLichnost
# 		fields = ('Naimenovanie', 'KodIMNS', 'KodPFR')

class FizicheskieLitsaForm(forms.ModelForm):
	class Meta:
		model = FizicheskieLitsa
		fields = ('Kod','Naimenovanie', 'DataRozhdeniya','OsnovnoeIzobrazhenie','UdostovereniyaLichnosti', 'KontaktnayaInformatsiya')
		widgets = {
			'DataRozhdeniya': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

#</Физические Лица>

# Договоры эквайринга
class DogovoryEkvayringaForm(forms.ModelForm):
	class Meta:
		model = DogovoryEkvayringa
		fields = ('Kod','Naimenovanie', 'Ekvayrer', 'DogovorVzaimoraschetov')

class TipyOplatCHekaKKMForm(forms.ModelForm):
	class Meta:
		model = TipyOplatCHekaKKM
		fields = ('text',)

class NomenklaturaForm(forms.ModelForm):
	class Meta:
		model = Nomenklatura
		fields = ('Kod','OsnovnoeIzobrazhenie', 'NomenklaturnayaGruppa', 'Naimenovanie', 'Artikul', 'VidNomenklatury', 'BazovayaEdinitsaIzmereniya', 
			'VestiUchetPoHarakteristikam', 'EdinitsaHraneniyaOstatkov', 'VestiUchetPoSeriyam', 'EdinitsaDlyaOtchetov', 
			'VestiPartionnyyUchetPoSeriyam', 'EdinitsaIzmereniyaMest','Vesovoy', 'NaimenovaniePolnoe', 'StavkaNDS', 'StatyaZatrat', 
			'NomenklaturnayaGruppaZatrat', 'Kommentariy', 'StranaProishozhdeniya', 'NomerGTD')

class VidyNomenklaturyForm(forms.ModelForm):
	class Meta:
		model = VidyNomenklatury
		fields = ('Kod','Naimenovanie', 'TipNomenklatury')

class StavkiNDSForm(forms.ModelForm):
	class Meta:
		model = StavkiNDS
		fields = ('text',)

class TipyNomenklaturyForm(forms.ModelForm):
	class Meta:
		model = TipyNomenklatury
		fields = ('text',)

class VidyZatratForm(forms.ModelForm):
	class Meta:
		model = VidyZatrat
		fields = ('text',)

class KlassifikatorEdinitsIzmereniyaForm(forms.ModelForm):
	class Meta:
		model = KlassifikatorEdinitsIzmereniya
		fields = ('id','Kod','Naimenovanie', 'MezhdunarodnoeSokraschenie',  'NaimenovaniePolnoe')

class StatiZatratForm(forms.ModelForm):
	class Meta:
		model = StatiZatrat
		fields = ('Kod', 'Roditel', 'Naimenovanie', 'VidZatrat', 'HarakterZatrat', 'OtnesenieRashodovKDeyatelnostiENVD')

class HarakterZatratForm(forms.ModelForm):
	class Meta:
		model = HarakterZatrat
		fields = ('text',)

class OtnesenieRashodovKDeyatelnostiENVDForm(forms.ModelForm):
	class Meta:
		model = OtnesenieRashodovKDeyatelnostiENVD
		fields = ('text',)

#Номера ГТД
class NomeraGTDForm(forms.ModelForm):
	class Meta:
		model = NomeraGTD
		fields = ('id', 'Kod', 'Kommentariy')

# Типы цен номенклатуры Контрагентов
class TipyTSenNomenklaturyKontragentovForm(forms.ModelForm):
	class Meta:
		model = TipyTSenNomenklaturyKontragentov
		fields = ('Kod','Vladelets', 'Naimenovanie', 'TipTSenNomenklatury', 'ValyutaTSeny', 'TSenaVlyuchaetNDS', 
			'OpisanieTipaTSenyNomenklaturyKontragenta', 'Kommentariy')

# Контрагенты
class KontragentyForm(forms.ModelForm):
	class Meta:
		model = Kontragenty
		fields = ('Kod','Naimenovanie', 'YUrFizLitso', 'NeYAvlyaetsyaRezidentom', 'Pokupatel', 'Postavschik', 'OKOPF', 'Roditel', 
			'NaimenovaniePolnoe', 'INN', 'KPP', 'KodPoOKPO', 'RaspisanieRabotyStrokoy', 'Region', 'VhoditVHolding', 
			'GolovnoyKontragent', 'Kommentariy', 'OsnovnoyDogovorKontragenta', 'OsnovnoyMenedzherPokupatelya', 'GolovnoyKontragent')

class GruppyKontragentovForm(forms.ModelForm):
	class Meta:
		model = GruppyKontragentov
		fields = ('text',)

# ЮрФизЛица
class YUrFizLitsoForm(forms.ModelForm):
	class Meta:
		model = YUrFizLitso
		fields = ('text',)

class KlassifikatorOKOPFForm(forms.ModelForm):
	class Meta:
		model = KlassifikatorOKOPF
		fields = ('Kod','Naimenovanie', 'NaimenovaniePolnoe')

# Регионы
class RegionyForm(forms.ModelForm):
	class Meta:
		model = Regiony
		fields = ('Kod','Roditel', 'KodAdresnogoElementa', 'KodRegiona', 'Naimenovanie', 'ZHDStantsiyaNaznacheniya', 
			'Kommentariy')

class VidyDeyatelnostiKontragentovForm(forms.ModelForm):
	class Meta:
		model = VidyDeyatelnostiKontragentov
		fields = ('Kod','Naimenovanie')

class KontaktnyeLitsaKontragentovForm(forms.ModelForm):
	class Meta:
		model = KontaktnyeLitsaKontragentov
		fields = ('Kod','KontaktnoeLitso', 'DataRozhdeniya', 'Pol', 'NapominatODneRozhdeniya', 'KolichestvoDneyDoNapominaniya', 
			'UdostovereniyaLichnosti', 'Vladelets', 'Dolzhnost', 'RolKontaktnogoLitsa', 'Kontakty', 'Kommentariy')
		widgets = {
			'DataRozhdeniya': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class KontaktnyeLitsaForm(forms.ModelForm):
	class Meta:
		model = KontaktnyeLitsa
		fields = ('Kod','Imya', 'Familiya', 'Otchestvo', 'Naimenovanie','DataRozhdeniya','Pol', 'Kontakty')
		widgets = {
			'DataRozhdeniya': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class PolFizicheskihLitsForm(forms.ModelForm):
	class Meta:
		model = PolFizicheskihLits
		fields = ('text',)

class RoliKontaktnyhLitsForm(forms.ModelForm):
	class Meta:
		model = RoliKontaktnyhLits
		fields = ('Kod','Naimenovanie')

class GruppySobytiyForm(forms.ModelForm):
	class Meta:
		model = GruppySobytiy
		fields = ('Kod','Naimenovanie', 'VidObekta', 'OpisanieSobytiya')

class VidyObektovSobytiyaForm(forms.ModelForm):
	class Meta:
		model = VidyObektovSobytiya
		fields = ('text',)

class VidyObektovSobytiyaForm(forms.ModelForm):
	class Meta:
		model = VidyObektovSobytiya
		fields = ('text',)

class VidyKontaktnoiInformatsiiForm(forms.ModelForm):
	class Meta:
		model = VidyKontaktnoiInformatsii
		fields = ('Kod','Tip', 'Naimenovanie', 'VidObektovKontaktnoiInformatsii')

class TipyKontaktnoiInformatsiiForm(forms.ModelForm):
	class Meta:
		model = TipyKontaktnoiInformatsii
		fields = ('text',)

class VidyObektovKontaktnoiInformatsiiForm(forms.ModelForm):
	class Meta:
		model = VidyObektovKontaktnoiInformatsii
		fields = ('text',)

class TovaryIUslugiForm(forms.ModelForm):
	class Meta:
		model = TovaryIUslugi
		fields = ('EdinitsaIzmereniya',)

#Единицы Измерения
class EdinitsyIzmereniyaForm(forms.ModelForm):
	class Meta:
		model = EdinitsyIzmereniya
		fields = ('Kod','Vladelets', 'EdinitsaPoKlassifikatoru', 'Naimenovanie', 'Ves', 'Obem', 'Koeffitsient')

class OrganizatsiiForm(forms.ModelForm):
	class Meta:
		model = Organizatsii
		fields = ('Kod','Naimenovanie', 'YUrFizLitso', 'Prefiks','OtrazhatVReglamentirovannomUchete', 'NaimenovaniePolnoe', 
			'NaimenovaniePlatelschikaPriPerechisleniiNalogov', 'OsnovnoyBankovskiySchet', 'INN', 'KPP', 'OGRN', 'KodIMNS', 
			'SvidetelstvoDataVydachi', 'SvidetelstvoSeriyaNomer', 'KodPoOKATO', 'KodPoOKPO')
		widgets = {
			'SvidetelstvoDataVydachi': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
		}

class BankovskieSchetaForm(forms.ModelForm):
	class Meta:
		model = BankovskieScheta
		fields = ('Kod','NomerScheta', 'VidScheta', 'ValyutaDenezhnyhSredstv', 'BIKBanka', 'KorrschetBanka', 'PryamieRaschety', 
			'RedaktirovatTekstKorrespondenta', 'TekstKorrespondenta', 'MesyatsPropisyu', 'SummaBezKopeek', 'DataOtkrytiya', 
			'DataZakrytiya', 'Naimenovanie')
		widgets = {
			'DataOtkrytiya': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'DataZakrytiya': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class DogovoryKontragentovForm(forms.ModelForm):
	class Meta:
		model = DogovoryKontragentov
		fields = ('Kod','Organizatsiya', 'Vladelets', 'Roditel', 'Naimenovanie', 'VidDogovora', 'Nomer', 'Data', 'SrokDeystviya',
			'VedenieVzaimoraschetov', 'ValyutaVzaimoraschetov', 'VestiPoDokumentamRaschetovSKontragentom','RaschetyVUslovnyhEdinitsah', 
			'RealizatsiyaNaEksport', 'VidVzaimoraschetov', 'VidUsloviyDogovora', 'KontrolirovatSummuZadolzhennosti', 
			'DopustimayaSummaZadolzhnosti')
		widgets = {
			'Data': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'}),
			'SrokDeystviya': forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
		}

class VidyDogovorovKontragentovForm(forms.ModelForm):
	class Meta:
		model = VidyDogovorovKontragentov
		fields = ('text',)

class VedenieVzaimoraschetovPoDogovoramForm(forms.ModelForm):
	class Meta:
		model = VedenieVzaimoraschetovPoDogovoram
		fields = ('text',)

class VidyUsloviyDogovorovVzaimoraschetovForm(forms.ModelForm):
	class Meta:
		model = VidyUsloviyDogovorovVzaimoraschetov
		fields = ('text',)

class KassyForm(forms.ModelForm):
	class Meta:
		model = Kassy
		fields = ('Kod','Vladelets', 'Roditel', 'Naimenovanie', 'ValyutaDenezhnyhSredstv', 'Otvetstvennyy')

class KassyKKMForm(forms.ModelForm):
	class Meta:
		model = KassyKKM
		fields = ('Kod','Vladelets', 'Naimenovanie', 'FormirovatNefiskalnyeCHeki')

class VidyOplatCHekaKKMForm(forms.ModelForm):
	class Meta:
		model = VidyOplatCHekaKKM
		fields = ('Kod','Naimenovanie', 'TipOplaty', 'BankKreditor', 'DogovorVzaimoraschetovBankaKreditora', 'ProtsentBankovskoyKomissii')