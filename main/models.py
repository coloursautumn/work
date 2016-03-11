from django.db import models

#
##
###
####
#####
##### Перечисления 
#####
####
###
##
#


class VidyOperatsiyCHekKKM(models.Model):
	class Meta:
		verbose_name = 'Виды операций ЧекККМ'
		verbose_name_plural = 'Виды операций ЧекККМ'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidTipaTSeny(models.Model):
	class Meta:
		verbose_name = 'Вид типа цен'
		verbose_name_plural = 'Вид типа цен'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class PolFizicheskihLits(models.Model):
	class Meta:
		verbose_name = 'Пол физического лица'
		verbose_name_plural = 'Пол физического лица'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class YUrFizLitso(models.Model):
	class Meta:
		verbose_name = 'ЮрФизЛицо'
		verbose_name_plural = 'ЮрФизЛицо'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class GruppySkladov(models.Model):
	class Meta:
		verbose_name = 'Группы складов'
		verbose_name_plural = 'Группы складов'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class GruppyBankov(models.Model):
	class Meta:
		verbose_name = 'Группы банков'
		verbose_name_plural = 'Группы банков'
	kod = models.CharField(max_length=256,null=True, blank=True)
	text = models.CharField(max_length=256,null=True, blank=True)
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')

	def __str__(self):
		return str(self.text)

class GruppyKontragentov(models.Model):
	class Meta:
		verbose_name = 'Группы контрагентов'
		verbose_name_plural = 'Группы контрагентов'
	text = models.CharField(max_length=256,null=True, blank=True)
	Kod = models.CharField(max_length=256,null=True, blank=True)

	def __str__(self):
		return str(self.text)

class VidyOperatsiyRealizatsiyaTovarov(models.Model):
	class Meta:
		verbose_name = 'Виды операций реализация товаров'
		verbose_name_plural = 'Виды операций реализация товаров'
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyVvodNachOstatkovNDS(models.Model):
	class Meta:
		verbose_name = 'Виды операций ввод Нач Остатков НДС'
		verbose_name_plural = 'Виды операций ввод Нач Остатков НДС'
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyTSennostey(models.Model):
	class Meta:
		verbose_name = 'Виды ценностей'
		verbose_name_plural = 'Виды ценностей'
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyPostupleniyaTovarov(models.Model):
	class Meta:
		verbose_name = 'Виды поступления товаров'
		verbose_name_plural = 'Виды поступления товаров'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidySkladov(models.Model):
	class Meta:
		verbose_name = 'Виды складов'
		verbose_name_plural = 'Виды складов'
	text = models.CharField(max_length=256,null=True, blank=True)

	def __str__(self):
		return str(self.text)

class VidyZatrat(models.Model):
	class Meta:
		verbose_name = 'Виды затрат'
		verbose_name_plural = 'Виды затрат'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class HarakterZatrat(models.Model):
	class Meta:
		verbose_name = 'Характер затрат'
		verbose_name_plural = 'Характер затрат'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class OtnesenieRashodovKDeyatelnostiENVD(models.Model):
	class Meta:
		verbose_name = 'Отнесение расходов к деятельности ЕНВД'
		verbose_name_plural = 'Отнесение расходов к деятельности ЕНВД'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidyOperatsiyRezervirovanieTovarov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyZayavkiNaRashodovanie(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class Vazhnost(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyZadolzhennosti(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyAkkreditivov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyRKO(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class SostoyaniyaSobytiy(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class UsloviyaSkidkiNatsenki(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyPostuplenieDopRashodov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiySpisanieBaznalichnyhDenezhnyhSredstv(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidPriemaRoznichnoyVyruchki(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyPPIshodyaschee(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyPerechisleniyVByudzhet(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyPeredachiTovarov(models.Model):
	class Meta:
		verbose_name = 'Вид передачи товаров'
		verbose_name_plural = 'Вид передачи товаров'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class TipyOplatCHekaKKM(models.Model):
	class Meta:
		verbose_name = 'Типы оплат чека ККМ'
		verbose_name_plural = 'Типы оплат чека ККМ'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidyOperatsiyPlaniruemoePostuplenieDS(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyPrihodnyyOrder(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class SostoyaniyaObektov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class UsloviyaOplatyRaschetnyhDokumentov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidVydachiDenezhnyhSredstv(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyOtvetORoznichnyhProdazhah(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyPKO(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VyhodyascheeIshodyascheeSobytie(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyKorrektirovkaDolgaPoVozvratnoyTare(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidySobytiy(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyObektovSobytiya(models.Model):
	class Meta:
		verbose_name = 'Виды объектов события'
		verbose_name_plural = 'Виды объектов события'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidyVnutrennegoZakaza(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyDenezhnyhSredstv(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyPostuplenieTovarovVNTT(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyInformatsionnyhKart(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class TipyInformatsionnyhKart(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class SposobyRaschetaTSeny(models.Model):
	class Meta:
		verbose_name = 'Способы расчета цен'
		verbose_name_plural = 'Способы расчета цен'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class SposobyRaspredeleniyaDopRashodov(models.Model):
	class Meta:
		verbose_name = 'Способы распределения доп расходов'
		verbose_name_plural = 'Способы распределения доп расходов'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class PoryadkiOkrugleniya(models.Model):
	class Meta:
		verbose_name = 'Порядки округления'
		verbose_name_plural = 'Порядки округления'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class StavkiNDS(models.Model):
	class Meta:
		verbose_name = 'Ставки НДС'
		verbose_name_plural = 'Ставки НДС'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class PoryadokRegistratsiiSchetovFakturNaAvans(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class TipyNomenklatury(models.Model):
	class Meta:
		verbose_name = 'Типы номенклатуры'
		verbose_name_plural = 'Типы номенклатуры'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VedenieVzaimoraschetovPoDogovoram(models.Model):
	class Meta:
		verbose_name = 'Ведение взаиморасчетов по договорам'
		verbose_name_plural = 'Ведение взаиморасчетов по договорам'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidyOperatsiyKorrektirovkaDolga(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyUsloviyDogovorovVzaimoraschetov(models.Model):
	class Meta:
		verbose_name = 'Виды условий договоров взаиморасчетов'
		verbose_name_plural = 'Виды условий договоров взаиморасчетов'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class SposobyRaschetaKomissionnogoVoznagrazhdeniya(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidyDogovorovKontragentov(models.Model):
	class Meta:
		verbose_name = 'Виды договоров контрагентов'
		verbose_name_plural = 'Виды договоров контрагентов'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidyOperatsiyPeremeschenieTovarov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class DeystvieNDSVStoimostiTovarov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyAgentskihDogovorov(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOtvetovPoPlatezhamKomissiya(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class VidyOperatsiyOplataOtPokupatelyaPlatezhnoyKartoy(models.Model):
	text = models.CharField(max_length=256,null=True, blank=True)

class TipyKontaktnoiInformatsii(models.Model):
	class Meta:
		verbose_name = 'Типы контактной информации'
		verbose_name_plural = 'Типы контактной информации'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

class VidyObektovKontaktnoiInformatsii(models.Model):
	class Meta:
		verbose_name = 'Виды объектов контактной информации'
		verbose_name_plural = 'Виды объектов контактной информации'
	text = models.CharField(max_length=256,null=True, blank=True)
	def __str__(self):
		return str(self.text)

#
##
###
####
#####
##### Справочники
#####
####
###
##
#

class VidyKontaktnoiInformatsii(models.Model):
	class Meta:
		verbose_name = 'Виды Контактной Информации'
		verbose_name_plural = 'Виды Контактной Информации'
	Tip = models.ForeignKey('TipyKontaktnoiInformatsii', verbose_name='Тип', null=True, blank=True, related_name='ifwrwQyE3311qSwc')
	VidObektovKontaktnoiInformatsii = models.ForeignKey('VidyObektovKontaktnoiInformatsii', verbose_name='Вид объектов контактной информации', null=True, blank=True, related_name='i2wrwQyE3311qSwc')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class TipySHtrihkodov(models.Model):
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')

class Valyuty(models.Model):
	class Meta:
		verbose_name = 'Валюты'
		verbose_name_plural = 'Валюты'
	NaimenovaniePolnoe = models.CharField(max_length=256,null=True, blank=True, verbose_name='Полностью')
	ParametryPropisiNaRusskom = models.CharField(max_length=256,null=True, blank=True, verbose_name='Параметры прописи на русском')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

# странная таблица
class KursyValyut(models.Model):
	Period = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False, verbose_name='Период')
	Valuta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False}, null=True, blank=True, verbose_name='Валюта', related_name='Q13qWOpSEQXuGsT')
	Kurs = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Курс')
	Kratnost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Кратность')
	Valyuty = models.ForeignKey('Valyuty', null=True, blank=True, verbose_name='Валюты', related_name='QBRkqWOpS33XuGsT')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')

	def __str__(self):
		return self.id

class UsloviyaProdazh(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class Banki(models.Model):
	class Meta:
		verbose_name = 'Банки'
		verbose_name_plural = 'Банки'
	KorrSchet = models.CharField(max_length=256,null=True, blank=True, verbose_name='Корр. счет')
	Gorod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Город')
	Adres = models.CharField(max_length=256,null=True, blank=True, verbose_name='Адрес')
	Telefony = models.CharField(max_length=256,null=True, blank=True, verbose_name='Телефоны')
	EtoGruppa = models.ForeignKey('GruppyBankov', null=True, blank=True, verbose_name='Группа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='БИК')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('Banki', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEyl1L14MuQM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class Podrazdeleniya(models.Model):
	class Meta:
		verbose_name = 'Подразделения'
		verbose_name_plural = 'Подразделения'
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('Podrazdeleniya', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Группа')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class FizicheskieLitsa(models.Model):
	class Meta:
		verbose_name = 'Физические Лица'
		verbose_name_plural = 'Физические Лица'
	DataRozhdeniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата рождения')
	KontaktnayaInformatsiya = models.CharField(max_length=256,null=True, blank=True, verbose_name='Контактная информация')
	UdostovereniyaLichnosti = models.CharField(max_length=256,null=True, blank=True, verbose_name='Удостоверение личности')
	OsnovnoeIzobrazhenie = models.ImageField(null=True, blank=True, upload_to='imgs/', verbose_name='Основное изображение')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEyl1L1QM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class PasportnieDannieFizLitsa(models.Model):
	class Meta:
		verbose_name = 'Паспортные данные ФизЛица'
		verbose_name_plural = 'Паспортные данные ФизЛица'
	VidDocumenta = models.ForeignKey('DokumentyUdostoveryayuschieLichnost', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Вид документа', null=True, blank=True, related_name='ifwrwQyEQ12SqSwc')
	Seriya = models.CharField(max_length=256,null=True, blank=True, verbose_name='Серия')
	Nomer = models.CharField(max_length=256,null=True, blank=True, verbose_name='Номер')
	DataVydachi = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False, verbose_name='Дата выдачи')
	KemVydan = models.CharField(max_length=250,null=True, blank=True, verbose_name='Кем выдан')
	KodPodrazdeleniya = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код подразделения')
	DataRegistratsii =  models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False, verbose_name='Дата регистрации по месту жительства')
	FizLitso = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ФизическиеЛица', null=True, blank=True, related_name='if33rwQyEQInSqSwc')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')

class TipyTsen(models.Model):
	class Meta:
		verbose_name = 'Типы цен'
		verbose_name_plural = 'Типы цен'
	TipTSenNomenklatury = models.ForeignKey('TipyTSenNomenklatury', null=True, blank=True, verbose_name='ТипЦенНоменклатуры', related_name='CeKSxAlvFLWstAlq')
	UstanovkaTSenNomenklatury = models.ForeignKey('UstanovkaTSenNomenklatury', null=True, blank=True, verbose_name='УстановкаЦенНоменклатуры', related_name='CLWelvFstAlKSxAq') #ТипыЦен

class TipyTSenNomenklatury(models.Model):
	class Meta:
		verbose_name = 'Типы цен номенклатуры'
		verbose_name_plural = 'Типы цен номенклатуры'
	ValyutaTSeny = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Валюта цены по умолчанию', null=True, blank=True, related_name='ifwrwQyEQInSqSwc')
	BazovyyTipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Базовый тип цен', null=True, blank=True, related_name='eDxURGXuZrKjbBYW')
	Rasschityvaetsya = models.BooleanField(default=False,verbose_name='Рассчитывается')
	ProtsentSkidkiNatsenki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Наценка в %')
	TSenaVlyuchaetNDS = models.BooleanField(default=False,verbose_name='Цены влючают НДС')
	VidTipaTSeny = models.ForeignKey('VidTipaTSeny', verbose_name='Вид типа цен', null=True, blank=True, related_name='eDxURG12XuZrKjbBYW')
	PoryadokOkrugleniya = models.ForeignKey('PoryadkiOkrugleniya', verbose_name='Округлять до', null=True, blank=True, related_name='QBRkqWOpSEQXuGsT')
	OkruglyatVBolshuyuStoronu = models.BooleanField(default=False,verbose_name='Округлять в большую сторону')
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	SposobRaschetaTSeny = models.ForeignKey('SposobyRaschetaTSeny', verbose_name='Способ расчета цены', null=True, blank=True, related_name='vdxepAwmUAzyGtyE')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class Sklady(models.Model):
	class Meta:
		verbose_name = 'Склады'
		verbose_name_plural = 'Склады'
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	TipTSenRoznichnoyTorgovli = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Тип цен', null=True, blank=True, related_name='PyRBBgbxaoCrBXtw')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='MOMEGlzJkDMKkGcd')
	VidSklada = models.ForeignKey('VidySkladov', verbose_name='Вид склада', null=True, blank=True, related_name='SkrfPRDIaZvIzfHY')
	NomerSektsii = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Номер секции')
	RaschetRoznichnyhTSenPoTorgovoyNatsenke = models.BooleanField(default=False,verbose_name='РасчетРозничныхЦенПоТорговойНаценке')
	EtoGruppa = models.ForeignKey('GruppySkladov', null=True, blank=True, verbose_name='Группа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('FizicheskieLitsa', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственное лицо')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class IstochnikiInformatsiiPriObraschenii(models.Model):
	PeriodAktualnostiInformatsiiPosleSobytiya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПериодАктуальностиИнформацииПослеСобытия')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class VidyDeyatelnostiKontragentov(models.Model):
	class Meta:
		verbose_name = 'Виды Деятельности Контрагентов'
		verbose_name_plural = 'Виды Деятельности Контрагентов'
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class VidyDiskontnyhKart(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class Vzaimoraschety(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class DogovoryEkvayringa(models.Model):
	class Meta:
		verbose_name = 'Договоры Эквайринга'
		verbose_name_plural = 'Договоры Эквайринга'
	Ekvayrer = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Эквайрер', null=True, blank=True, related_name='ReTkEGYLryPyHAne')
	DogovorVzaimoraschetov = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Договор взаиморасчетов', null=True, blank=True, related_name='hACDREpCvnIcWOeW')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class VidyVzaimoraschetov(models.Model):
	class Meta:
		verbose_name = 'Виды Взаиморасчетов'
		verbose_name_plural = 'Виды Взаиморасчетов'
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class BankovskieScheta(models.Model):
	class Meta:
		verbose_name = 'Банковские Счета'
		verbose_name_plural = 'Банковские Счета'
	NomerScheta = models.CharField(max_length=256,null=True, blank=True, verbose_name='Номер счета')
	BIKBanka = models.CharField(max_length=256,null=True, blank=True, verbose_name='БИК')
	KorrschetBanka = models.CharField(max_length=256,null=True, blank=True, verbose_name='Корр.счет')
	PryamieRaschety = models.BooleanField(default=False,verbose_name='Прямые расчеты')
	Bank = models.ForeignKey('Banki', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Банк', null=True, blank=True, related_name='iMnoHTBSvVDKfbYh')
	BankDlyaRaschetov = models.ForeignKey('Banki', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанкДляРасчетов', null=True, blank=True, related_name='VLOXnEXEUwplIxew')
	TekstKorrespondenta = models.CharField(max_length=256,null=True, blank=True, verbose_name='Текст наименования организации в поле "Плательщик"')
	TekstNaznacheniya = models.CharField(max_length=256,null=True, blank=True, verbose_name='ТекстНазначения')
	VidScheta = models.CharField(max_length=256,null=True, blank=True, verbose_name='Вид счета')
	ValyutaDenezhnyhSredstv = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Валюта', null=True, blank=True, related_name='zYeCXODycRAXdbOn')
	NomerIDataRazresheniya = models.CharField(max_length=256,null=True, blank=True, verbose_name='НомерИДатаРазрешения')
	DataOtkrytiya = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False, verbose_name='Дата открытия')
	DataZakrytiya = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False, verbose_name='Дата закрытия')
	MesyatsPropisyu = models.BooleanField(default=False,verbose_name='Выводить дату числом')
	SummaBezKopeek = models.BooleanField(default=False,verbose_name='Выводить сумму без копеек, если она в целых рублях')
	VivoditMesyatsVDateDocumenta2 = models.BooleanField(default=False,verbose_name='ВыводитьМесяцВДатеДокумента2')
	RedaktirovatTekstKorrespondenta = models.BooleanField(default=False,verbose_name='Редактировать текст')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.IntegerField(null=True, blank=True, verbose_name='Владелец')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class DolzhnostiOrganizatsiy(models.Model):
	class Meta:
		verbose_name = 'Должности организации'
		verbose_name_plural = 'Должности организации'
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class GruppySobytiy(models.Model):
	class Meta:
		verbose_name = 'Группы Событий'
		verbose_name_plural = 'Группы Событий'
	OpisanieSobytiya = models.CharField(max_length=256,null=True, blank=True, verbose_name='Описание события')
	VidObekta = models.ForeignKey('VidyObektovSobytiya', verbose_name='Вид объекта', null=True, blank=True, related_name='SduHcZZPjuEZAjKa')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class Polzovateli(models.Model):
	FizLitso = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ФизЛицо', null=True, blank=True, related_name='YaixVxiuStBDdbxv')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEyl1L111QM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class StatyaDvizheniyaDenezhnyhSredstv(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class DokumentyUdostoveryayuschieLichnost(models.Model):
	class Meta:
		verbose_name = 'Документы Утверждающие Личность'
		verbose_name_plural = 'Документы Утверждающие Личност'
	KodIMNS = models.CharField(max_length=256,null=True, blank=True, verbose_name='КодИМНС')
	KodPFR = models.CharField(max_length=256,null=True, blank=True, verbose_name='КодПФР')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class UstloviyaProdazh(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class Territorii(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class KlassifikatorStranMira(models.Model):
	NaimenovaniePolnoe = models.CharField(max_length=256,null=True, blank=True, verbose_name='НаименованиеПолное')
	KodAlfa2 = models.CharField(max_length=256,null=True, blank=True, verbose_name='КодАльфа2')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class Organizatsii(models.Model):
	class Meta:
		verbose_name = 'Организации'
		verbose_name_plural = 'Организации'
	INN = models.CharField(max_length=256,null=True, blank=True, verbose_name='ИНН')
	KodIMNS = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код ИМНС')
	KodPoOKATO = models.CharField(max_length=256,null=True, blank=True, verbose_name='ОКАТО')
	KodPoOKPO = models.CharField(max_length=256,null=True, blank=True, verbose_name='ОКПО')
	KPP = models.CharField(max_length=256,null=True, blank=True, verbose_name='КПП')
	NaimenovaniePlatelschikaPriPerechisleniiNalogov = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование плательщика в платежных поручениях на перечисление в бюджет')
	NaimenovaniePolnoe = models.CharField(max_length=256,null=True, blank=True, verbose_name='Полное наименование')
	OGRN = models.CharField(max_length=256,null=True, blank=True, verbose_name='ОГРН')
	OsnovnoyBankovskiySchet = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Осн. банковский счет', null=True, blank=True, related_name='FQqRDNBTHrsaGEiF')
	Prefiks = models.CharField(max_length=256,null=True, blank=True, verbose_name='Префикс')
	SvidetelstvoDataVydachi = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата выдачи')
	SvidetelstvoSeriyaNomer = models.CharField(max_length=256,null=True, blank=True, verbose_name='Серия и №')
	YUrFizLitso = models.ForeignKey('YUrFizLitso', verbose_name='Юр./Физ. лицо', null=True, blank=True, related_name='rYRNxrGWzsNqgxyB')
	OtrazhatVReglamentirovannomUchete = models.BooleanField(default=False,verbose_name='Отражать в регламентированном учете')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class SeriynyeNomeraSpr(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Vladelets = models.IntegerField(null=True, blank=True, verbose_name='Владелец')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class Kachestvo(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class Pomescheniya(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.IntegerField(null=True, blank=True, verbose_name='Владелец')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class Proekty(models.Model):
	DataNachala = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаНачала')
	DataOkonchaniya = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаОкончания')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='DYwfmgUWEUCRfRwz')
	Opisanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Описание')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEyl11L111QM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class VidyRaspredeleniyaPoProektam(models.Model):
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class StatiDvizheniyaDenezhnyhSredstv(models.Model):
	class Meta:
		verbose_name = 'Статья движения денежных средств'
		verbose_name_plural = 'Статья движения денежных средств'
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class DogovoryKontragentov(models.Model):
	class Meta:
		verbose_name = 'Договоры Контрагентов'
		verbose_name_plural = 'Договоры Контрагентов'
	ValyutaVzaimoraschetov = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Валюта', null=True, blank=True, related_name='TfzoWPfMxjShHdaO')
	VedenieVzaimoraschetov = models.ForeignKey('VedenieVzaimoraschetovPoDogovoram', verbose_name='Взаиморасчеты ведутся', null=True, blank=True, related_name='ImviCZWJiwnSuLbu')
	VidVzaimoraschetov = models.ForeignKey('VidyVzaimoraschetov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Вид взаиморасчетов', null=True, blank=True, related_name='HPgIBUTKCBCyDZYB')
	VidUsloviyDogovora = models.ForeignKey('VidyUsloviyDogovorovVzaimoraschetov', verbose_name='Условия договора', null=True, blank=True, related_name='fRUFDbqcrshHLWIO')
	DerzhatRezervBezOplatyOgranichennoeVremya = models.BooleanField(default=False,verbose_name='ДержатьРезервБезОплатыОграниченноеВремя')
	DopustimayaSummaZadolzhnosti = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Допустимая сумма задолжности')
	DopustimoeCHisloDneyZadolzhennosti = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ДопустимоеЧислоДнейЗадолженности')
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	KontrolirovatSummuZadolzhennosti = models.BooleanField(default=False,verbose_name='Контролировать сумму задолженности')
	KontrolirovatCHisloDneyZadolzhennosti = models.BooleanField(default=False,verbose_name='КонтролироватьЧислоДнейЗадолженности')
	ObosoblennyyUchetTovarovPoZakazamPokupateley = models.BooleanField(default=False,verbose_name='ОбособленныйУчетТоваровПоЗаказамПокупателей')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='sUyPhQpSyheJWeGr')
	ProtsentKomissionnogoVoznagrazhdeniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентКомиссионногоВознаграждения')
	ProtsentPredoplaty = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентПредоплаты')
	SposobRaschetaKomissionnogoVoznagrazhdeniya = models.ForeignKey('SposobyRaschetaKomissionnogoVoznagrazhdeniya', verbose_name='СпособРасчетаКомиссионногоВознаграждения', null=True, blank=True, related_name='AvkanuTeMGCPwypP')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='zMPuHCbehwQiwdpu')
	CHisloDneyRezervaBezOplaty = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ЧислоДнейРезерваБезОплаты')
	VidDogovora = models.ForeignKey('VidyDogovorovKontragentov', verbose_name='Вид договора', null=True, blank=True, related_name='ClJEjxBRoyWdWwaz')
	UchetAgentskogoNDS = models.BooleanField(default=False,verbose_name='УчетАгентскогоНДС')
	VidAgentskogoDogovora = models.ForeignKey('VidyAgentskihDogovorov', verbose_name='ВидАгентскогоДоговора', null=True, blank=True, related_name='fVYBctCGosYsWGlw')
	KontrolirovatDenezhnyeSredstvaKomitenta = models.BooleanField(default=False,verbose_name='КонтролироватьДенежныеСредстваКомитента')
	RaschetyVUslovnyhEdinitsah = models.BooleanField(default=False,verbose_name='Расчеты в условных единицах')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='от')
	Nomer = models.CharField(max_length=256,null=True, blank=True, verbose_name='Номер')
	RealizatsiyaNaEksport = models.BooleanField(default=False,verbose_name='Реализация на экспорт')
	VestiPoDokumentamRaschetovSKontragentom = models.BooleanField(default=False,verbose_name='Вести по документам расчетов с контрагентами')
	OsnovnoyProekt = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновнойПроект', null=True, blank=True, related_name='BGbKOPfzCwFeoAbp')
	OsnovnayaStatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновнаяСтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='eglMhvUfVMiSAvxR')
	SrokDeystviya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Срок действия')
	PoryadokRegistratsiiSchetovFakturNaAvansPoDogovoru = models.ForeignKey('PoryadokRegistratsiiSchetovFakturNaAvans', verbose_name='ПорядокРегистрацииСчетовФактурНаАвансПоДоговору', null=True, blank=True, related_name='kDCvEJoERGEXHgKm')
	NaimenovanieDlyaSchetaFakturyNaAvans = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НаименованиеДляСчетаФактурыНаАванс', null=True, blank=True, related_name='ICrrrvLXqdVLQPPb')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Группа договоров', null=True, blank=True, related_name='BGbKOPfz3wFe3oAbp')
	Vladelets = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='BGbKOPfz3wFeoAbp')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class StatiZatrat(models.Model):
	class Meta:
		verbose_name = 'Статьи затрат'
		verbose_name_plural = 'Статьи затрат'
	VidZatrat = models.ForeignKey('VidyZatrat', verbose_name='Вид затрат', null=True, blank=True, related_name='uULSRCMLezKrzyou')
	HarakterZatrat = models.ForeignKey('HarakterZatrat', verbose_name='Характер затрат', null=True, blank=True, related_name='sUlLetMwqCqlgmlD')
	UdalitVidRashodovNU = models.CharField(max_length=256,null=True, blank=True, verbose_name='УдалитьВидРасходовНУ')
	OtnesenieRashodovKDeyatelnostiENVD = models.ForeignKey('OtnesenieRashodovKDeyatelnostiENVD', verbose_name='Распределение', null=True, blank=True, related_name='pRHuSZESwkrbYixe')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEyl1asdfQM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class KlassifikatorEdinitsIzmereniya(models.Model):
	class Meta:
		verbose_name = 'Классификатор единиц измерения'
		verbose_name_plural = 'Классификатор единиц измерения'
	NaimenovaniePolnoe = models.CharField(max_length=256,null=True, blank=True, verbose_name='Полное наименование')
	MezhdunarodnoeSokraschenie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Международное cокращение')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class EdinitsyIzmereniya(models.Model):
	class Meta:
		verbose_name = 'Единицы Измерения'
		verbose_name_plural = 'Единицы Измерения'
	EdinitsaPoKlassifikatoru = models.ForeignKey('KlassifikatorEdinitsIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='По классификатору', null=True, blank=True, related_name='SimfiqrXvAxOIdAX')
	Ves = models.DecimalField(max_digits=15, default=0, decimal_places=4, null=True, blank=True, verbose_name='Вес')
	Obem = models.DecimalField(max_digits=15, default=0, decimal_places=4, null=True, blank=True, verbose_name='Объем')
	Koeffitsient = models.DecimalField(max_digits=15, default=1, decimal_places=4, null=True, blank=True, verbose_name='Коэффициент')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='jzTLXtWVav2ixdJ')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class AdresnyeSokrascheniya(models.Model):
	Uroven = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Уровень')
	Sokraschenie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Сокращение')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class SeriiNomenklatury(models.Model):
	SeriynyyNomer = models.CharField(max_length=256,null=True, blank=True, verbose_name='СерийныйНомер')
	Sertifikat = models.CharField(max_length=256,null=True, blank=True, verbose_name='Сертификат')
	SrokGodnosti = models.DateField(auto_now=False, auto_now_add=False, verbose_name='СрокГодности')
	NomerGTD = models.ForeignKey('NomeraGTD', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НомерГТД', null=True, blank=True, related_name='PVllaEDYZdKIfuhe')
	StranaProishozhdeniya = models.ForeignKey('KlassifikatorStranMira', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтранаПроисхождения', null=True, blank=True, related_name='LNQSvAEgLdMJhchV')
	OsnovnoeIzobrazhenie = models.ImageField(upload_to='imgs/', verbose_name='ОсновноеИзображение')
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.IntegerField(null=True, blank=True, verbose_name='Владелец')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class NomenklaturnyeGruppy(models.Model):
	EdinitsaHraneniyaOstatkov = models.ForeignKey('KlassifikatorEdinitsIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Единица хранения остатков', null=True, blank=True, related_name='pbblODnuQAyEWyDw') # изменил с Единицы хранения остатков на классификатор*
	BazovayaEdinitsaIzmereniya = models.ForeignKey('KlassifikatorEdinitsIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Базовая единица', null=True, blank=True, related_name='xnFUipPYufdPFLEe')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='Ставка НДС', null=True, blank=True, related_name='dzEylFqInLgCMuQM')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEylFqInLg2CMuQM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class VidyNomenklatury(models.Model):
	class Meta:
		verbose_name = 'Виды Номенклатуры'
		verbose_name_plural = 'Виды Номенклатуры'
	TipNomenklatury = models.ForeignKey('TipyNomenklatury', verbose_name='Тип номенклатуры', null=True, blank=True, related_name='PdGScrRUbWXMBzSM')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class TSenovyeGruppy(models.Model):
	Poryadok = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Порядок')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Roditel = models.ForeignKey('TSenovyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEylFqInLg2CMuQM')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

from django.db.models import Q

class Nomenklatura(models.Model):
	class Meta:
		verbose_name = 'Номенклатура'
		verbose_name_plural = 'Номенклатура'
	StatyaZatrat = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Статья затрат', null=True, blank=True, related_name='YHDKJDiGDbLsLaln')
	Artikul = models.CharField(max_length=256,null=True, blank=True, verbose_name='Артикул')
	BazovayaEdinitsaIzmereniya = models.ForeignKey('KlassifikatorEdinitsIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Базоваия ед.', null=True, blank=True, related_name='WLHeaJRPbvysuNKH')
	Vesovoy = models.BooleanField(default=False,verbose_name='Весовой')
	VesovoyKoeffitsientVhozhdeniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ВесовойКоэффициентВхождения')
	VestiPartionnyyUchetPoSeriyam = models.BooleanField(default=False,verbose_name='Вести партионный учет по сериям')
	VestiUchetPoSeriyam = models.BooleanField(default=False,verbose_name='Вести учет по сериям')
	VestiUchetPoHarakteristikam = models.BooleanField(default=False,verbose_name='Вести учет по характеристикам')
	EdinitsaDlyaOtchetov = models.ForeignKey('KlassifikatorEdinitsIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ед. для отчетов', null=True, blank=True, related_name='RoKzDktOcCIpxzFk') # изменил с единиц измерения на классификатор 
	EdinitsaHraneniyaOstatkov = models.ForeignKey('KlassifikatorEdinitsIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ед. хран. остатков', null=True, blank=True, related_name='MKImyKcHLOqvRUTY') # изменил с единиц измерения на классификатор
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	Nabor = models.BooleanField(default=False,verbose_name='Набор')
	NaimenovaniePolnoe = models.CharField(max_length=256,null=True, blank=True, verbose_name='НаименованиеПолное')
	NomenklaturnayaGruppa = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НоменклатурнаяГруппа', null=True, blank=True, related_name='KQeIXxrmS1АшtIDejam')
	NomerGTD = models.ForeignKey('NomeraGTD', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НомерГТД', null=True, blank=True, related_name='JhPzZKvLMctrCGOC')
	OsnovnoeIzobrazhenie = models.ImageField(null=True, blank=True, upload_to='imgs/', verbose_name='Основное изображение')
	OsnovnoyPostavschik = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновнойПоставщик', null=True, blank=True, related_name='sgruflxJCsNKgrmp')
	OtvetstvennyyMenedzherZaPokupki = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтветственныйМенеджерЗаПокупки', null=True, blank=True, related_name='QxWdtGkyVGheWsLZ')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='Ставка НДС', null=True, blank=True, related_name='UHAKjwOvnkobACoy')
	StranaProishozhdeniya = models.ForeignKey('KlassifikatorStranMira', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтранаПроисхождения', null=True, blank=True, related_name='kAhhTFHAJsCKuUKz')
	Usluga = models.BooleanField(default=False,verbose_name='Услуга')
	NomenklaturnayaGruppaZatrat = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатурная группа затрат', null=True, blank=True, related_name='HQXYqgReWhEbFWxv')
	VidNomenklatury = models.ForeignKey('VidyNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Вид номенклатуры', null=True, blank=True, related_name='BasoczyrAzFAZLsS')
	VestiSeriynyeNomera = models.BooleanField(default=False,verbose_name='ВестиСерийныеНомера')
	Komplekt = models.BooleanField(default=False,verbose_name='Комплект')
	TSenovayaGruppa = models.ForeignKey('TSenovyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЦеноваяГруппа', null=True, blank=True, related_name='iMDtiVKyHsJxOqyy')
	EdinitsaIzmereniyaMest = models.ForeignKey('KlassifikatorEdinitsIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ед. мест', null=True, blank=True, related_name='zuGVlkGrZLQgPGRP')
	DopolnitelnoeOpisanieNomenklatury = models.CharField(max_length=256,null=True, blank=True, verbose_name='ДополнительноеОписаниеНоменклатуры')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256, null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256, null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEylFqInLg2CM1uQM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"


class TipyTSenNomenklaturyKontragentov(models.Model):
	class Meta:
		verbose_name = 'Типы Цен Номенклатуры Контрагентов'
		verbose_name_plural = 'Типы Цен Номенклатуры Контрагентов'
	ValyutaTSeny = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Валюта', null=True, blank=True, related_name='qrkhPNrUYMkWKPDc')
	TSenaVlyuchaetNDS = models.BooleanField(default=False,verbose_name='Цены влючают НДС')
	TipTSenNomenklatury = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Тип цены номенклатуры', null=True, blank=True, related_name='AUQdwdCaMjdsOZGR')
	OpisanieTipaTSenyNomenklaturyKontragenta = models.CharField(max_length=256,null=True, blank=True, verbose_name='Описание')
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='iMDtiVKy1HsJxOqyy')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class NomeraGTD(models.Model):
	class Meta:
		verbose_name = 'НомераГТД'
		verbose_name_plural = 'НомераГТД'
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		return self.Kod

class Kassy(models.Model):
	class Meta:
		verbose_name = 'Кассы'
		verbose_name_plural = 'Кассы'
	ValyutaDenezhnyhSredstv = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Валюта', null=True, blank=True, related_name='YvZxINIhIrFMiZlu')
	Otvetstvennyy = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственное лицо', null=True, blank=True, related_name='YvZxINMiZlu')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Группа касс', null=True, blank=True, related_name='YvZxINIhI1rFMiZlu')
	Vladelets = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='YvZxIN1IhI1rFMiZlu')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class KassyKKM(models.Model):
	class Meta:
		verbose_name = 'Кассы ККМ'
		verbose_name_plural = 'Кассы ККМ'
	FormirovatNefiskalnyeCHeki = models.BooleanField(default=False,verbose_name='Формировать нефискальные чеки')
	SHirinaLenty = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ШиринаЛенты')
	RuchnoyRezhimFormirovaniya = models.BooleanField(default=False,verbose_name='РучнойРежимФормирования')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='Yv11IhI1rFMiZlu')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class VidyOplatCHekaKKM(models.Model):
	class Meta:
		verbose_name = 'Виды оплат чека ККМ'
		verbose_name_plural = 'Виды оплат чека ККМ'
	UdalitVidDenezhnyhSredstv = models.ForeignKey('VidyDenezhnyhSredstv', verbose_name='УдалитьВидДенежныхСредств', null=True, blank=True, related_name='ePQjcpdnIPziHkDW')
	TipOplaty = models.ForeignKey('TipyOplatCHekaKKM', verbose_name='Тип оплаты', null=True, blank=True, related_name='TLRjAVqcSOBbdcQA')
	BankKreditor = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Банк-кредитор', null=True, blank=True, related_name='ybpOMRUUsgzYplXl')
	DogovorVzaimoraschetovBankaKreditora = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Договор взаиморасчетов', null=True, blank=True, related_name='gjNiymCviFJkIPra')
	ProtsentBankovskoyKomissii = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='% банковской комиссии')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('VidyOplatCHekaKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEylnLg2CMuQM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class KlassifikatorOKOPF(models.Model):
	class Meta:
		verbose_name = 'Классификатор ОКОПФ'
		verbose_name_plural = 'Классификатор ОКОПФ'
	NaimenovaniePolnoe = models.CharField(max_length=256,null=True, blank=True, verbose_name='Полное наименование')
	BystryyVybor = models.BooleanField(default=False,verbose_name='БыстрыйВыбор')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class HarakteristikiNomenklatury(models.Model):
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.IntegerField(null=True, blank=True, verbose_name='Владелец')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class Regiony(models.Model):
	class Meta:
		verbose_name = 'Регионы'
		verbose_name_plural = 'Регионы'
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	KodRegiona = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код региона')
	KodAdresnogoElementa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Код адресного элемента')
	ZHDStantsiyaNaznacheniya = models.CharField(max_length=256,null=True, blank=True, verbose_name='Ж/Д станция')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('Regiony', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Входит в', null=True, blank=True, related_name='ybpOMRUUsgzY331l')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class IstochnikiInformatsiiPriObrascheniiPokupateley(models.Model):
	PereodAktualnostiInformatsiiPosleSobytiya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПереодАктуальностиИнформацииПослеСобытия')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class GruppyDostupaKKontragentam(models.Model):
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('GruppyDostupaKKontragentam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEyl1Lg2CMuQM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')

class RoliKontaktnyhLits(models.Model):
	class Meta:
		verbose_name = 'Роли контактных лиц'
		verbose_name_plural = 'Роли контактных лиц'
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class KontaktnyeLitsa(models.Model):
	class Meta:
		verbose_name = 'Контактные лица'
		verbose_name_plural = 'Контактные лица'
	DataRozhdeniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаРождения')
	Imya = models.CharField(max_length=256,null=True, blank=True, verbose_name='Имя')
	KolichestvoDneyDoNapominaniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КоличествоДнейДоНапоминания')
	NapominatODneRozhdeniya = models.BooleanField(default=False,verbose_name='НапоминатьОДнеРождения')
	UdalitRol = models.ForeignKey('RoliKontaktnyhLits', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьРоль', null=True, blank=True, related_name='IgwxAyhwICnYQxkf')
	UdalitDolzhnost = models.CharField(max_length=256,null=True, blank=True, verbose_name='УдалитьДолжность')
	Opisanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Описание')
	Otchestvo = models.CharField(max_length=256,null=True, blank=True, verbose_name='Отчество')
	Familiya = models.CharField(max_length=256,null=True, blank=True, verbose_name='Фамилия')
	Pol = models.ForeignKey('PolFizicheskihLits', verbose_name='Пол', null=True, blank=True, related_name='IgwxAyhwICn377xkf')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	Kontakty = models.CharField(max_length=256,null=True, blank=True, verbose_name='Контакты')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class KontaktnyeLitsaKontragentov(models.Model):
	class Meta:
		verbose_name = 'Контактные Лица Контрагентов'
		verbose_name_plural = 'Контактные Лица Контрагентов'
	DataRozhdeniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата рождения')
	Dolzhnost = models.CharField(max_length=256,null=True, blank=True, verbose_name='Должность')
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	Kontakty = models.CharField(max_length=256,null=True, blank=True, verbose_name='Контакты')
	Pol = models.ForeignKey('PolFizicheskihLits', verbose_name='Пол', null=True, blank=True, related_name='IgwxAyh1n377xkf')
	NapominatODneRozhdeniya = models.BooleanField(default=False,verbose_name='Напоминать о дне рождения')
	KolichestvoDneyDoNapominaniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Дней до напоминания')
	UdostovereniyaLichnosti = models.CharField(max_length=256,null=True, blank=True, verbose_name='Должность')
	KontaktnoeLitso = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контактное лицо', null=True, blank=True, related_name='SkfsfaaZkwKdvBwx')
	RolKontaktnogoLitsa = models.ForeignKey('RoliKontaktnyhLits', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Роль', null=True, blank=True, related_name='RUExaGGmZkBgDmJB')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Vladelets = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='Skfsfaa3KdvBwx')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	def __str__(self):
		if self.KontaktnoeLitso:
			return self.KontaktnoeLitso.Naimenovanie
		else:
			return "None"

class Kontragenty(models.Model):
	class Meta:
		verbose_name = 'Контрагенты'
		verbose_name_plural = 'Контрагенты'
	GolovnoyKontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ГоловнойКонтрагент', null=True, blank=True, related_name='bBbVbvWrmnEBOGtE')
	DokumentUdostoveryayuschiyLichnost = models.CharField(max_length=256,null=True, blank=True, verbose_name='ДокументУдостоверяющийЛичность')
	DopolnitelnoeOpisanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='ДополнительноеОписание')
	INN = models.CharField(max_length=256,null=True, blank=True, verbose_name='ИНН')
	IstochnikInformatsiiPriObraschenii = models.ForeignKey('IstochnikiInformatsiiPriObraschenii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИсточникИнформацииПриОбращении', null=True, blank=True, related_name='YJlFkNQAQTKGxcKb')
	KodPoOKPO = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код по ОКПО')
	Kommentariy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Комментарий')
	KPP = models.CharField(max_length=256,null=True, blank=True, verbose_name='КПП')
	NaimenovaniePolnoe = models.CharField(max_length=256,null=True, blank=True, verbose_name='Полное наименование')
	OsnovnoeKontaktnoeLitso = models.ForeignKey('KontaktnyeLitsaKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновноеКонтактноеЛицо', null=True, blank=True, related_name='lnnpDmTezxSjWnhr')
	OsnovnoyBankovskiySchet = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновнойБанковскийСчет', null=True, blank=True, related_name='pwJplkEgsjItQsuk')
	OsnovnoyVidDeyatelnosti = models.ForeignKey('VidyDeyatelnostiKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновнойВидДеятельности', null=True, blank=True, related_name='ZwQdjqqBeSjKrAJh')
	OsnovnoyDogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновнойДоговорКонтрагента', null=True, blank=True, related_name='bBiMNeDarNOfFzJb')
	OsnovnoyMenedzherPokupatelya = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОсновнойМенеджерПокупателя', null=True, blank=True, related_name='gdOkwkyYzQseqhpd')
	Pokupatel = models.BooleanField(default=False,verbose_name='Покупатель')
	Postavschik = models.BooleanField(default=False,verbose_name='Поставщик')
	RaspisanieRabotyStrokoy = models.CharField(max_length=256,null=True, blank=True, verbose_name='Расписание работы')
	SrokVypolneniyaZakazaPostavschikom = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СрокВыполненияЗаказаПоставщиком')
	YUrFizLitso = models.ForeignKey('YUrFizLitso', verbose_name='Юр./Физ. лицо', null=True, blank=True, related_name='KcLFSBLYmjOUGpxF')
	NeYAvlyaetsyaRezidentom = models.BooleanField(default=False,verbose_name='Нерезидент')
	OKOPF = models.ForeignKey('KlassifikatorOKOPF', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОКОПФ', null=True, blank=True, related_name='hQrBNHVGUFmhSRNg')
	Region = models.ForeignKey('Regiony', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Регион', null=True, blank=True, related_name='izLBiGMmhsaDcQax')
	GruppaDostupaKKontragentu = models.ForeignKey('GruppyDostupaKKontragentam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ГруппаДоступаККонтрагенту', null=True, blank=True, related_name='bRAEDWasXbkIjhPj')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('GruppyKontragentov', verbose_name='Группа контрагентов', null=True, blank=True, related_name='hQrBNHVGUF111hSRNg')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')
	VhoditVHolding = models.BooleanField(default=False,verbose_name='Входит в холдинг')
	def __str__(self):
		if self.Naimenovanie:
			return self.Naimenovanie
		else:
			return "None"

class InformatsionnyeKarty(models.Model):
	KodKarty = models.CharField(max_length=256,null=True, blank=True, verbose_name='КодКарты')

	VladeletsKartyPolzovateli = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВладелецКарты-Пользователи', null=True, blank=True, related_name='yOeyOIlTLfAMcuYl')
	VladeletsKartyKontragenty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВладелецКарты-Контрагенты', null=True, blank=True, related_name='saqFuleZuWGgFtLD')

	UdalitEtoPrefiksKoda = models.BooleanField(default=False,verbose_name='УдалитьЭтоПрефиксКода')
	UdalitProtsentSkidki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='УдалитьПроцентСкидки')
	VidKarty = models.ForeignKey('VidyInformatsionnyhKart', verbose_name='ВидКарты', null=True, blank=True, related_name='qZWbmuSbDUbDFEwp')
	TipKarty = models.ForeignKey('TipyInformatsionnyhKart', verbose_name='ТипКарты', null=True, blank=True, related_name='mPFcWeOzGofhhQCY')
	TipSHtrihKoda = models.ForeignKey('TipySHtrihkodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипШтрихКода', null=True, blank=True, related_name='TMhOXVTKHXnOxnro')
	VidDiskontnoyKarty = models.ForeignKey('VidyDiskontnyhKart', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВидДисконтнойКарты', null=True, blank=True, related_name='LiBtIBZcqjQzaWLG')
	EtoGruppa = models.BooleanField(default=False,verbose_name='ЭтоГруппа')
	Kod = models.CharField(max_length=256,null=True, blank=True, verbose_name='Код')
	Naimenovanie = models.CharField(max_length=256,null=True, blank=True, verbose_name='Наименование')
	Roditel = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Родитель', null=True, blank=True, related_name='dzEyl1Lg2C14MuQM')
	PometkaUdaleniya = models.BooleanField(default=False,verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Predopredelennyy = models.BooleanField(default=False,verbose_name='Предопределенный')


#
##
###
####
#####
##### Документы
#####
####
###
##
#

class UstanovkaTSenNomenklatury(models.Model):
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', null=True, blank=True, verbose_name='Ответственный', related_name='AUQRPOqGdBANgdRL')
	NeProvoditNulevyeZnacheniya = models.BooleanField(default=False,verbose_name='НеПроводитьНулевыеЗначения')
	Informatsiya = models.CharField(max_length=100,null=True, blank=True, verbose_name='Информация')
	Nomer = models.CharField(max_length=100,null=True, blank=True, verbose_name='Номер')
	Data = models.DateTimeField(null=True, blank=True, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default = False, verbose_name='ПометкаУдаления')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	def __str__(self):
		if self.Nomer:
		  return self.Nomer
		else:
		  return str(self.id)

class CHekKKM(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	TekushieVesi = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекущиеВесы')
	VidOperatsii = models.ForeignKey('VidyOperatsiyCHekKKM', null=True, blank=True,verbose_name='ВидОперации', related_name='CndWRYvQjkVo1uayX')
	Sklad = models.ForeignKey('Sklady', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', related_name='rCAmwEDiiWmYcxki')
	KassaKKM = models.ForeignKey('KassyKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='КассаККМ', related_name='mWxtmWGnqQUIILzX')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', related_name='SIkTiAupwkVlaYRt')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	CHekProbitNaKKM = models.BooleanField(default=False, verbose_name='ЧекПробитНаККМ')
	NomerCHekaKKM = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НомерЧекаККМ')
	Otvetstvennyy = models.ForeignKey('Polzovateli', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', related_name='NvoLdohHBhDlYlvK')
	DiskontnayaKarta = models.ForeignKey('InformatsionnyeKarty', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДисконтнаяКарта', related_name='TDTdFIqAYaSdyDoR')
	NomerSmenyKKM = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НомерСменыККМ')
	CHekKKMProdazha = models.ForeignKey('CHekKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЧекККМПродажа', related_name='PPlRHbwgueVcuMKu')
	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', related_name='XDmKJbNOcDeYnsui')
	Organizatsiya = models.ForeignKey('Organizatsii', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', related_name='xDmPQgIpZGFLYXcn')
	VladeletsDiskontnoyKarty = models.ForeignKey('Kontragenty', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВладелецДисконтнойКарты', related_name='jcXhGBwmHZWgsFzC')

	DokumentPartiiVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ВозвратТоваровОтПокупателя', related_name='aNtyinnCSgZIImGa')
	DokumentPartiiPrihodnyyOrderNaTovary = models.ForeignKey('PrihodnyyOrderNaTovary', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ПриходныйОрдерНаТовары', related_name='vDfLWiDFUAnaXqxY')
	DokumentPartiiPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ПоступлениеТоваровУслугВНТТ', related_name='cPupxeRTPnoJzrVI')
	DokumentPartiiOprihodovanieTovarov = models.ForeignKey('OprihodovanieTovarov', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ОприходованиеТоваров', related_name='epRMoLfdQvTYTnhh')
	DokumentPartiiPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ПоступлениеТоваровУслуг', related_name='OaXOBaCHAuruaXbU')
	DokumentPartiiOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ОтчетОРозничныхПродажах', related_name='vXhIyRvELPDlIPDS')
	DokumentPartiiRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-РеализацияТоваровУслуг', related_name='LUausoTwcGofgtnn')
	DokumentPartiiAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-АвансовыйОтчет', related_name='nZGqHygJEqJRuAcr')

	def __str__(self):
		return self.Nomer


class Doverennosti(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Organizatsiya = models.ForeignKey('Organizatsii', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', related_name='OSEEjifadQzoAYIJ')
	FizLitso = models.ForeignKey('FizicheskieLitsa', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ФизЛицо', related_name='CMDEShPLPAAaqWIf')
	Dolzhnost = models.ForeignKey('DolzhnostiOrganizatsiy', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Должность', related_name='HeJSajnbnJAMYVWb')
	BankovskiySchetOrganizatsii = models.ForeignKey('BankovskieScheta', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетОрганизации', related_name='NrhDaeXUQEgadsgQ')
	Kontragent = models.ForeignKey('Kontragenty', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', related_name='ffjacfKiEiDpcgrj')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', related_name='deWtfryEPVsfKFGV')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', related_name='MFDzDWqGSLZeWiDQ')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', related_name='TYQTLqxekVyyfrky')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', related_name='oMURvqgGrZqPkUkr')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', related_name='wmAMjYUdnqsKoSvB')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', related_name='QkHkSezGEBlqjUmU')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', related_name='QkBtvxllJoUSMfjD')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', related_name='FbiFoWkBTwlcKAbM')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', related_name='jcGDdSfSyYuTNEkE')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', related_name='LGFrEzZNXVonpkAz')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', related_name='cBsfdMlQodkIqMku')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', related_name='LPjPzvAojgZbncYh')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', related_name='BpMrWjKbgPUDYZpG')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', related_name='ZKwrRXPKjgrrkeAD')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', related_name='OPCnqSsZvCOlCByY')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', related_name='XbuZhtbrZbpcVmxW')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', related_name='lbBBpKivMJeuKxlM')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', related_name='EAEVhVXunYPQENHZ')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', related_name='EBFTppXrggdxdFbc')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', related_name='PuNeFGRnOdhNwkJV')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', related_name='RcDMBOCMIPndssjB')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', related_name='AtZLBEIFxQsHPlJy')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', related_name='SkbbDnGhzGTmXaiU')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', related_name='hqjyKpDDcuWrPXhf')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', related_name='tUPysKRqoIuBspXw')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', related_name='pOpvLSAvpqZxTHSu')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', related_name='qIrNlheJHCRCwRwO')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', related_name='QlnufmbGNAeKQgeb')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', related_name='zyJQBGXCIkzzgzrS')

	DataDeystviya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаДействия')
	NaPoluchenieOt = models.CharField(max_length=100, null=True, blank=True, verbose_name='НаПолучениеОт')
	PoDokumentu = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПоДокументу')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', related_name='bKasWUSoURdKTaIM')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', related_name='HdreSwvOydrqQNQv')

	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	def __str__(self):
		return self.Nomer


class OprihodovanieTovarov(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', related_name='wIPeyoXthixxxzez')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', related_name='MlAEIwuKkrFiOdok')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', related_name='RQSvywWqOghplLVw')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(verbose_name='ОтражатьВНалоговомУчете')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', related_name='TIDWJWMZYXmXIrQE')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Osnovanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Основание')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	InventarizatsiyaTovarovNaSklade = models.ForeignKey('InventarizatsiyaTovarovNaSklade', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнвентаризацияТоваровНаСкладе', related_name='AtKpczOxyaSkIDew')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', related_name='AMUsssZykjEmoPvr')
	SummaDokumentaRegl = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокументаРегл')
	UchityvatNDS = models.BooleanField(verbose_name='УчитыватьНДС')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(verbose_name='ПометкаУдаления')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(verbose_name='Проведен')


class SpisanieTovarov(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='LdrjLPsnOqvsVtQQ')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='tjwKRIktefseLQyY')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='BflCRJrXzoOtsCaL')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Osnovanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Основание')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	InventarizatsiyaTovarovNaSklade = models.ForeignKey('InventarizatsiyaTovarovNaSklade', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнвентаризацияТоваровНаСкладе', null=True, blank=True, related_name='xTrhjINVnjYrpbLN')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='cgwwIuWlHxVdRJJT')
	NDSvStoimostiTovarov = models.ForeignKey('DeystvieNDSVStoimostiTovarov', verbose_name='НДСвСтоимостиТоваров', null=True, blank=True, related_name='eiQOsTeqoBtXDxxE')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class DokumentRaschetovSKontragentom(models.Model):
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='ANMUHoUEiLTEcUzH')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='VgCYWbpACCMDZjin')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='bnhhaVBgLrBEkdag')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='HFCGMhVHYZiRHwkC')
	DokumentOsnovanie = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование', null=True, blank=True, related_name='MqMlGwjVzbKZQiaG')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='mHQQPjSkXQdQiwNn')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class SchetFakturaVydannyy(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	DokumentOsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='MNGqUCEtKgyhApUP')
	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='IVlTxIEoFTUcEexJ')
	DokumentOsnovaniePrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='iasDYAIlHfZwskaK')
	DokumentOsnovanieOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='fmvFdVBieUbtiFgk')
	DokumentOsnovaniePlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='gsFtEBPOsneMbWvU')
	DokumentOsnovanieVvodNachalnyhOstatkovNDS = models.ForeignKey('VvodNachalnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВводНачальныхОстатковНДС', null=True, blank=True, related_name='NOXnHtsqIXJdPZpS')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='KnQMeFAxqEqASvFx')
	DokumentOsnovanieInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='qlQErLExsrdGkNfO')
	DokumentOsnovanieDokumentRaschetovSKontragentom = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='SdEnvkIpcdSnOojg')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='KEwcDrylxElYxFQL')
	DokumentOsnovaniePlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='kvcQImVazgSJKTmI')
	DokumentOsnovanieOplataOtPokupatelyaPlatezhnoyKartoy = models.ForeignKey('OplataOtPokupatelyaPlatezhnoyKartoy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОплатаОтПокупателяПлатежнойКартой', null=True, blank=True, related_name='jHumdiUWRBrUtnXn')
	DokumentOsnovanieAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АккредитивПолученный', null=True, blank=True, related_name='zWyxpBNPKfNUYLVV')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='dNedNGdpVesZFPms')
	DokumentOsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РеализацияТоваровУслуг', null=True, blank=True, related_name='bCLxIBVVPsfVDUPF')
	DokumentOsnovaniePlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='fKHgqhrBcInhEYla')
	DokumentOsnovanieKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-КорректировкаДолга', null=True, blank=True, related_name='RCBMKzxYBXlQCTZy')

	NomerPlatezhnoRasschetnogoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерПлатежноРассчетногоДокумента')
	DataPlatezhnoRaschetnogoDokumenta = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='ДатаПлатежноРасчетногоДокумента')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='hymEcRAmqjSdNErN')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='qLYiKquvGgNyCiIA')
	NaAvans = models.BooleanField(default=False, verbose_name='НаАванс')
	Pod0 = models.BooleanField(default=False, verbose_name='Под0')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='TABaAInJVwhGXYaq')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='bbdmwyYJRBMYGBqQ')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='ydgAiOXZBXbNgBjW')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='TcEtPzmaEyOqmLEU')
	SformirovanPriVvodeNachalnyhOstatkovNDS = models.BooleanField(default=False, verbose_name='СформированПриВводеНачальныхОстатковНДС')
	UdalenValyutnayaSumma = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='УдаленВалютнаяСумма')

	def __str__(self):
		return self.Nomer


class PereotsenkaTovarovOtdannyhNaKomissiyu(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='YsemiDQfUibRpVre')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='VqZezaHzrCfPJxim')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='jJSVWrcnmpwhZULG')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='KVoiWStejGNBVKIG')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='GobGoDZltCHMnNHd')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='lXTbFHnKzItMPAjm')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='jPowfQNEVKyvofCd')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='QFlyMSQKDSjqomzT')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='peEpePXQRjlkggow')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='tCpKIWSNxfJydZGw')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='GLmTOiNyZmDsVqAW')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='ylLUFiVXFbcsTwlg')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='oCtCLSnNvXfBBMdh')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='dyVqhNXGsBZJSogw')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='qNAQZwKrkGQZGpYM')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='EJoyAYIMCkQDDPdY')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='luNqTHgDIiywcoOl')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='fclvsgPVCmqGKDRe')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='QfLMFzevmXtaRmyz')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='EiKYMUYeYPzDMVGp')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='lLpYKsmnQlNSEkBL')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='yurYajENdSXhAwna')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='mbGrqXrJuVhpdMLP')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='kFhEkAHNhVGTOwhn')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='AcmOaPvepGvYiwRp')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='TirnbzhNCBcDoPWQ')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='lZUKTowpPuvrRCeC')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='AKVuEyrQVIPZggHW')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='WssHlpDEtBICNlNn')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='AdwszcovJMXwGydn')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='royDEyRPWMFUUFOw')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='XHRAOStMtrhUaSXl')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='TFvdtAtiTTxfIJtN')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='SquecfcqBcObcuUX')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='avhbsAbEeWxJYoRN')

	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class VvodNachalnyhOstatkovNDS(models.Model):
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='cCGxmRLXXPoUboyF')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='rNeaLIBzYUUpIlBQ')
	VidOperatsii = models.ForeignKey('VidyOperatsiyVvodNachOstatkovNDS', verbose_name='ВидОперации', null=True, blank=True, related_name='MYPnnUUtrqfNtgex')
	OtrazitRasschetySKontragentami = models.BooleanField(default=False, verbose_name='ОтразитьРассчетыСКонтрагентами')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class SchetFakturaPoluchennyy(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='ptYTHqXkGkbVxGpZ')

	DokumentOsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='zDRXDaWQLsbfsfri')
	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='loeKOEyRRnsCuLxi')
	DokumentOsnovanieInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='IGdndFNOTEOluPQO')
	DokumentOsnovaniePlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='lCFjQVvsjXJPMVeC')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='QOzNCoQRAkfrebFp')
	DokumentOsnovanieRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РасходныйКассовыйОрдер', null=True, blank=True, related_name='aZixzijBOtfpoZGh')
	DokumentOsnovanieAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АккредитивПереданный', null=True, blank=True, related_name='pWHfWwXvpBOjCzvP')
	DokumentOsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='HKEsZjQYjdWsCApB')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='EfAzrUQkfwVClCnM')
	DokumentOsnovaniePlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='UdmgKinFPJppIfpo')
	DokumentOsnovanieDokumentRaschetovSKontragentom = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='hmLnHqNoyTXdlLLw')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='IjhjhbxZAzzxPwLS')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='IrYgFbKaGXTgORSK')
	DokumentOsnovanieOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='JgmCXWMrvRqGNkit')
	DokumentOsnovaniePlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='TJWHrFpYAYZDLsiq')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='xuyJFTHmvBPepukK')
	DokumentOsnovanieAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АвансовыйОтчет', null=True, blank=True, related_name='XMJkssrvgSBSyYAX')
	DokumentOsnovanieKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-КорректировкаДолга', null=True, blank=True, related_name='yKrYDcqvcNadmaJJ')

	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='ДатаВходящегоДокумента')
	SformirovanPriVvodeNachalnyhOstatkovNDS = models.BooleanField(default=False, verbose_name='СформированПриВводеНачальныхОстатковНДС')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='MhSharfUtszfODTI')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='yXyIzgvHZetxRlHK')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='rOJrOtzNARkBNuaq')
	NomerVhodyaschegoDokumentaElektronnogoObmena = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокументаЭлектронногоОбмена')
	DataVhodyaschegoDokumentaElektronnogoObmena = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='ДатаВходящегоДокументаЭлектронногоОбмена')
	NaAvans = models.BooleanField(default=False, verbose_name='НаАванс')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='KNvWPfqXnKbulpbf')

	def __str__(self):
		return self.Nomer


class OtrazheniePostupleniyaTovarovIUslugNDS(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='aeLBJoqiHWaxlilS')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='iaRHLbxbuomwjNVj')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='MvfVUVRSYrUfkJpC')

	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='UHfzdgWXPTKluaeq')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='ztOUENqFKOLzOHOE')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='etWVgGKdKlTYDXSN')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='CzEKFOYHSUxCUPbs')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='LhrimLioErauoAcT')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='AtzBKYXbxHtqLqLj')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='zwGkYDVHRmZdTGLB')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='OfhWWRoRzWBpfuwL')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='AMvNHPTVNJuecUNf')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='xyDuxlHHqdqHUIRR')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='jbBEkxftGGiMOLwp')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='QBVEuPLddBYynOgC')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='RwUPFWNFZaHtyVBq')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='FNyIKvGgEfZcOmUV')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='kTdAqjTlPOUSKWBq')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='UaTcOIZLjZESsjhE')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='xdpXyayVurOPptEI')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='wbvVAcAnKwzghOgT')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='fLKbaQfBZpQXfsHt')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='QRKpGNpjSXQRReaZ')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='jpuMGlxActdKUOqT')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='mBEoEuHFUjoCDOTa')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='fJVzRwJsUCCeWDJQ')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='TixxbIGANyXmIQWg')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='dIhRHxjuBclBYuSg')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='LfpBhJZjvNiSqluH')

	RaschetnyyDokument = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент', null=True, blank=True, related_name='gtCXhPHLWfuKIzjo')
	DataOprihodovaniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОприходования')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='WUZQUHYCBuSBpAIL')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='frYPMhYrojqjlnrD')
	PryamayaZapisVKnigu = models.BooleanField(default=False, verbose_name='ПрямаяЗаписьВКнигу')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='YdFtPCKWnggHtOsA')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class GTDImport(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='pqjkuhOahcJXRDOj')
	NomerGTD = models.ForeignKey('NomeraGTD', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НомерГТД', null=True, blank=True, related_name='MIFmlwnyQaWTTzVa')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='xfHortZmcdxVYSoS')
	KursDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсДокумента')
	KratnostDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьДокумента')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='IqGZSdQeQmPAbcOl')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='jGyBSXkZPdNQqzLq')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	DogovorKontragentaRegl = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагентаРегл', null=True, blank=True, related_name='SazJqRRLKXgsMtiM')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='TLqMViaivQCxBMvT')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='crWqmItKLzLLZrmf')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	TamozhennyySborVal = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ТаможенныйСборВал')
	TamozhennyySbor = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ТаможенныйСбор')
	TamozhennyySHtrafVal = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ТаможенныйШтрафВал')
	TamozhennyySHtraf = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ТаможенныйШтраф')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	NDSVklyuchenoVStoimost = models.BooleanField(default=False, verbose_name='НДСВключеноВСтоимость')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='pMlLsUmkLeZUOrvf')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='WbMvqGwUnsTohHrE')

	def __str__(self):
		return self.Nomer


class OplataOtPokupatelyaPlatezhnoyKartoy(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='uMLneGuWZWaiMZHN')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='YtZaxAIOwHUzaabu')
	VidOperatsii = models.ForeignKey('VidyOperatsiyOplataOtPokupatelyaPlatezhnoyKartoy', verbose_name='ВидОперации', null=True, blank=True, related_name='RnHoaHWbKVOeMadw')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='aQyDspdHsfysChEI')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='hcQqKIFSwsmGddHu')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	NomerCHekaKKM = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НомерЧекаККМ')
	DogovorEkvayringa = models.ForeignKey('DogovoryEkvayringa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорЭквайринга', null=True, blank=True, related_name='YdEdDUBBAJZJQlkk')
	Ekvayrer = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Эквайрер', null=True, blank=True, related_name='aZYULQHoKjdLYmBL')
	DogovorVzaimoraschetovEkvayrera = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорВзаиморасчетовЭквайрера', null=True, blank=True, related_name='ETjvVOpzSEJAjdnc')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='LQFUTDfaxVjRekOY')
	VidOplaty = models.ForeignKey('VidyOplatCHekaKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВидОплаты', null=True, blank=True, related_name='AiSdNecgiUYnqdUD')
	ProtsentTorgovoyUstupki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентТорговойУступки')
	SummaTorgovoyUstupki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаТорговойУступки')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class InkassovoePorucheniePeredannoe(models.Model):
	DokumentOsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='QHGKFPhabTUyHRxD')
	DokumentOsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПокупателя', null=True, blank=True, related_name='TRtoXlKtaLRZOdYA')
	DokumentOsnovaniePlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='nSakDajHBnxgTtSi')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='DNJlmxevJsAyAcDu')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='vlkfNHgsOdiQzBZH')
	DokumentOsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РеализацияТоваровУслуг', null=True, blank=True, related_name='plagjPgqRBsnuVvB')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='pZKipxpBbNaxELMz')

	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='eitdKqUTBgvJCBFH')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='ylBCSJMmaAgFxSbD')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='dwEpshEjIzCuJkmy')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='snbFuuORghcofoRw')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='iaoyVvonBrYkgvty')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='rKWKzMYeouULpLSJ')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='hvmstChIGsHknQag')
	VidPlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидПлатежа')
	DokumentPlanirovaniyaPostupleniya = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПланированияПоступления', null=True, blank=True, related_name='JqJWDlGruQfMXgYy')
	OcherednostPlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='ОчередностьПлатежа')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	TekstPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПлательщика')
	TekstPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПолучателя')
	INNPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПлательщика')
	KPPPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППлательщика')
	INNPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПолучателя')
	KPPPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППолучателя')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='uGCGaarCrIMSLdVx')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='MjzyVKxcSegeEAhx')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='qGvJNcreqMlzXckU')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class DenezhnyyCHek(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='IQntvBIKBkZrVxpX')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='lxLuRZnUGAIGUOpe')
	Kassa = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Касса', null=True, blank=True, related_name='rJakpfVGXWTUWSyf')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='DSoNmBIJIndggWqm')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='vLnPUtjIlEhPdOey')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='VNcSMlHjXYsxCMVb')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class ObyavlenieNaVznosNalichnymi(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='zsQaIgOcEzYXyUBg')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='HsmDxAlTSsvBTVRA')
	Kassa = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Касса', null=True, blank=True, related_name='RIypdEvZsrFAbwur')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='DofUcjlISqFeiqYb')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='VXOvpBDvfkfKVEoW')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='IogRnthSjVMVNbst')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class SchetNaOplatuPostavschika(models.Model):
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='QBPRAiUFKgrqKFhJ')
	UdalitVremyaNapominaniya = models.DateField(auto_now=False, auto_now_add=False, verbose_name='УдалитьВремяНапоминания')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	DataPostupleniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаПоступления')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='MnKVdgvLaLbSruaa')
	IspolzovatPlanovuyuSebestoimost = models.BooleanField(default=False, verbose_name='ИспользоватьПлановуюСебестоимость')
	ItogPlanovayaSebestoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ИтогПлановаяСебестоимость')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='cHRDvkCQQPWrBYsa')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	UdalitNapomnitOSobytii = models.BooleanField(default=False, verbose_name='УдалитьНапомнитьОСобытии')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='jGWfaQLFDWVfaboe')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='peLTBZhyyFbtmkka')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='kzcmQsRMHhVQNHif')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='ePtVtpOsYopNeqVK')

	StrukturnayaEdinitsaBankovskieScheta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтруктурнаяЕдиница-БанковскиеСчета', null=True, blank=True, related_name='TxXKxBDSewoTyDfm')
	StrukturnayaEdinitsaKassy = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтруктурнаяЕдиница-Кассы', null=True, blank=True, related_name='rSPiuFRbBWnmaitn')

	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='njasveeCVSLDyYNA')
	UdalitKontaktnoeLitso = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьКонтактноеЛицо', null=True, blank=True, related_name='xYbnzgmTeodvfcRS')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')

	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', null=True, blank=True, related_name='CMPqzZLLkyeTfWqo')
	DokumentOsnovanieSobytie = models.ForeignKey('Sobytie', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-Событие', null=True, blank=True, related_name='QPvMJhCCwQwYLRvi')

	KontaktnyeLitsaKontragentov = models.ForeignKey('KontaktnyeLitsaKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтактныеЛицаКонтрагентов', null=True, blank=True, related_name='gWhIdOMEiDEOzMMI')
	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='BrJspkMwPCKAHmnk')
	NomerVhodyaschegoDokumentaElektronnogoObmena = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокументаЭлектронногоОбмена')
	DataVhodyaschegoDokumentaElektronnogoObmena = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокументаЭлектронногоОбмена')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class AvansovyyOtchet(models.Model):
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='zAsohdCNuonCXiHS')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	KursDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсДокумента')
	KratnostDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='pCZcMHWxjqWbyrEj')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='MtrNBfDLVWBGIhaZ')

	SkladOrderPrihodnyyOrderNaTovary = models.ForeignKey('PrihodnyyOrderNaTovary', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладОрдер-ПриходныйОрдерНаТовары', null=True, blank=True, related_name='MqirbypsbRhpQtfD')
	SkladOrderSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладОрдер-Склады', null=True, blank=True, related_name='zgFAxDDkfpQIWkKB')

	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='uEHpSocDjvJxgLue')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	FizLitso = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ФизЛицо', null=True, blank=True, related_name='lSLfyKaiRrobCfDu')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='oOAqdZlMfKVMJVGi')
	VidPostupleniya = models.ForeignKey('VidyPostupleniyaTovarov', verbose_name='ВидПоступления', null=True, blank=True, related_name='BjvetXWbeKQtPqdS')
	NDSVklyuchenVStoimost = models.BooleanField(default=False, verbose_name='НДСВключенВСтоимость')
	NaznachenieAvansa = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеАванса')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='DGeEsuftFwmwkMEU')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='NYNoohBIPMJkcQnW')

	KolichestvoDokumentov = models.CharField(max_length=100, null=True, blank=True, verbose_name='КоличествоДокументов')
	KolichestvoListov = models.CharField(max_length=100, null=True, blank=True, verbose_name='КоличествоЛистов')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class RashodnyyKassovyyOrder(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='CBPYqbWcNqYlJYKZ')
	Kassa = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Касса', null=True, blank=True, related_name='PwwSIzpOQikDBHeF')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='yQeGiWWrFyzymgMf')
	VidOperatsii = models.ForeignKey('VidyOperatsiyRKO', verbose_name='ВидОперации', null=True, blank=True, related_name='GQcKaGveIzVEIMBg')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')

	KontragentKontragenty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-Контрагенты', null=True, blank=True, related_name='qoQGqeXFAKlaqnlL')
	KontragentKassyKKM = models.ForeignKey('KassyKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-КассыККМ', null=True, blank=True, related_name='HcWvnOGTaUqzyHGF')
	KontragentSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-Склады', null=True, blank=True, related_name='SCJenVxMnnIwoXcW')
	KontragentFizicheskieLitsa = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-ФизическиеЛица', null=True, blank=True, related_name='aQQluOAVPYeqWkqM')

	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='FQAHlaLDDwxXmTAa')
	ValyutaVzaimoraschetovRabotnika = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаВзаиморасчетовРаботника', null=True, blank=True, related_name='abRxuhDXknlBDrol')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='AVPsQHquSznRKNoL')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	DataPogasheniyaAvansa = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаПогашенияАванса')
	RaschetnyyDokument = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент', null=True, blank=True, related_name='KMKGglAZbIdkrxxV')
	Vydat = models.CharField(max_length=100, null=True, blank=True, verbose_name='Выдать')
	Osnovanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Основание')
	Prilozhenie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Приложение')
	PoDokumentu = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПоДокументу')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='RclesESSWiCVTOEH')

	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='KwUWPakOiljXlPuJ')
	DokumentOsnovaniePrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='BceZrKMGRiCjbnsq')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='wbFBnFZBPBgjOEbs')
	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', null=True, blank=True, related_name='UhsHiLoBdRewnLiB')
	DokumentOsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='NWhCpIqOQUfGfESM')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='OcdynBPRTFOqrOmU')
	DokumentOsnovanieZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='ZVlDUVVsRENurvVa')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='XMXmhrAHRbhqGSPp')
	DokumentOsnovanieObyavlenieNaVznosNalichnymi = models.ForeignKey('ObyavlenieNaVznosNalichnymi', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОбъявлениеНаВзносНаличными', null=True, blank=True, related_name='KNwufKoTlytqRoXh')
	DokumentOsnovanieAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АвансовыйОтчет', null=True, blank=True, related_name='RUsRmIGfyfTPDfKB')
	DokumentOsnovanieSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПоставщика', null=True, blank=True, related_name='sxvTyPsqNZaiDgWy')

	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='MWbeMpEZlndBtvVB')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='VjRLACLtBDQNSUGP')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	VidVydachiDenezhnyhSredstv = models.ForeignKey('VidVydachiDenezhnyhSredstv', verbose_name='ВидВыдачиДенежныхСредств', null=True, blank=True, related_name='OLMhUvPXisQLecgj')
	ObyavlenieNaVznosNalichnymi = models.ForeignKey('ObyavlenieNaVznosNalichnymi', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОбъявлениеНаВзносНаличными', null=True, blank=True, related_name='lujEAEmNVvEkCUgN')
	NomerCHekaKKM = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НомерЧекаККМ')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class KorrektirovkaDolgaPoVozvratnoyTare(models.Model):
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='uZPTeMjwinjlvrUv')
	VidOperatsii = models.ForeignKey('VidyOperatsiyKorrektirovkaDolgaPoVozvratnoyTare', verbose_name='ВидОперации', null=True, blank=True, related_name='PcWwKfmZszXkqYeC')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='gvgtKVkHKrMiTDix')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='mUWwMGTebEvHSdPN')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	KursDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='QGsMkFpAzKlbZgAO')
	Osnovanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Основание')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='AzPLHuPWsCvgSSxv')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='yKuFQSKBzQLDMdlA')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='YEhPBcFKDUSoQNfM')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='VoKPWYgEFZiTdZNe')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='SJkqieMbUfoOYwPu')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='PrOmbGZjuIxpWnzj')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='mwIkFMMejFqyNsDe')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='VNGbQvTOPOjVtDnJ')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='ZemdGnUEQnpfsrhC')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='TddIIdcfkcDuflAs')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='gwwFhIzcJJLXtYIp')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='CicdfPqKuCdWIYqO')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='tECzWvmejeWLWaZO')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='tWTUkLGCYZwGPtTU')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='NzywzfWaszwydUAe')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='HkXxBhkduiiFhIGl')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='hIaJPJlvhPccrbBn')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='zVcZNUaeILXETwAw')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='WOjNKhNanvTmJxnm')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='cydytQJsCrqdpqhz')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='YMgkdmRJCbWpQXxz')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='pxUXmJjEhswXOehK')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='ocpswiBspHXUctVF')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='cjKLKuEYuZgJJHsd')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='rTRtuXhudiWMeDXD')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='wkYoEEqQtjBKSMMX')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='GGBJSTqNavnpkCYM')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='ifzQvPvtWmTUeVjV')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='WeTIXGCLsHzUlawR')

	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	KratnostDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьДокумента')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='yhgOeEApCiccbyfb')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PlatezhnyyOrderSpisanieDenezhnyhSredstv(models.Model):
	RaschetnyyDokumentInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='JTOhhXDQYSCgqWTr')
	RaschetnyyDokumentPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='gfSCTbwPBFNQFkqF')
	RaschetnyyDokumentAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-АккредитивПереданный', null=True, blank=True, related_name='VMZcycdBNzONgaJi')
	RaschetnyyDokumentPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='kTjSiJABsUIrnGja')

	DokumentOsnovanieInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='LZFjMwDYWBQdlXXh')
	DokumentOsnovaniePlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='tgIdoQRUwKnmGHRM')
	DokumentOsnovanieAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АккредитивПереданный', null=True, blank=True, related_name='umgESdbnnffpWBoE')
	DokumentOsnovanieZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='ypQIcJaaeEGIsJAS')

	Organizatsii = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организации', null=True, blank=True, related_name='ybogbfiFeJCnadnM')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='eEODXkQckyedLosn')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='BCQgJYqMPoreyKcO')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='HiSFrWWFwTcuBihL')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='SWKPhEHhBSutllGj')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='bIMvGabGteZSqkfn')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='GbOyhcdPEGTGYhyF')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='rzMTrTNtNCMAgUhf')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='cnegliJraoYFdtSv')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='GraOYVPyidZDMmgK')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	FizLitso = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ФизЛицо', null=True, blank=True, related_name='TnfcVxgWjsJbRllK')
	ValyutaVzaimoraschetovRabotnika = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаВзаиморасчетовРаботника', null=True, blank=True, related_name='bcQxUnhXbgSjJjdm')
	DataPogasheniyaAvansa = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаПогашенияАванса')
	RaschetnyyDokumentRabotnika = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокументРаботника', null=True, blank=True, related_name='SQIPXhIhejkYItpK')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class VozvratTovarovPostavschiku(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='isZseXzEIIXRvBkP')
	BankovskiySchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетОрганизации', null=True, blank=True, related_name='UhyJKeejUmGlLKlJ')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='sjcTKwdtHkYmHmMx')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='dqDpeSIIiQBDcAXH')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='trNDyBTIFXbKOXRR')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='DLlxcrZWWCkQfgZi')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='iOTqTxkPvZkwpuhB')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='sUjOZXkKoqZuznVv')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='JoeOTpGfzZsNDwvJ')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='RLvEvQdGjGFPNkAq')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='HZdwNAdfccPMciwO')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='UGhgrnjgCiXusKQi')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='QVGybEHIveGDjABZ')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='JlyrQorYNMiQuqqZ')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='pgjqCdPufiUSBhGn')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='MhOrknltNBMZfnWu')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='QQWjWblwslneMZKL')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='bfUuipbgujnFajiM')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='AvyaRBPLzIsFbRDW')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='pwHyqEdqEhkdYOHY')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='gPpAUJOKNulDpvUa')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='wHGeidwELMuAFUon')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='rlyXMRvUhezGaljC')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='pUylwzKjuRNuFljM')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='UliuIaHSJaGFTLlI')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='zINmLdAvLxuzSAfo')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='ucnXdmSyuauezIku')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='GwhFMcOICHMnNivW')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='AOJEPbReeAutdkar')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='gdJXpegMemKLRTxJ')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='cAuijQmlcuATjCeR')

	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='qqGHzKMztxGvGzjg')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='XLbSeEjVLfSUfKmK')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='ayZMDunjjrMtnDQF')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='aFVewHGxYQVOVlGr')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='wpyLWkdstUQJfuNV')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='RibcxJAAKxhnylnv')
	VidPeredachi = models.ForeignKey('VidyPeredachiTovarov', verbose_name='ВидПередачи', null=True, blank=True, related_name='MINlvdmVRRgUmcoz')
	NDSVklyuchenVStoimost = models.BooleanField(default=False, verbose_name='НДСВключенВСтоимость')
	Gruzopoluchatel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', null=True, blank=True, related_name='ocPOrCYnjrHCMVbB')
	Gruzootpravitel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузоотправитель', null=True, blank=True, related_name='LgVlbmgBKasASnkG')
	PostavschikuVystavlyaetsyaSchetFakturaNaVozvrat = models.BooleanField(default=False, verbose_name='ПоставщикуВыставляетсяСчетФактураНаВозврат')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='WsJoDUDhBMbhRMEB')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='UmnrONioWloNnMEl')

	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='pMNovUDqWnaYtzQP')

	def __str__(self):
		return self.Nomer


class PlatezhnoePoruchenieVhodyaschee(models.Model):
	DokumentOsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='NFwzDsxHnndjQYMP')
	DokumentOsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПокупателя', null=True, blank=True, related_name='mceSjFOKDYfEugCc')
	DokumentOsnovaniePlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='iNnagfyKZvtaiyLH')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='pYWNuNwAbtiRGRWf')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='KIaIaDytxtOAdrOY')
	DokumentOsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РеализацияТоваровУслуг', null=True, blank=True, related_name='vwkDfXfAcRWRZpsa')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='ezdlfxjvUuoGpCPM')

	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='yPukuhpgsNsjMAEB')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='AESsBwkkuRHQlccl')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='dWsRgfMhHdIyIfDk')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='QanhUGgeJWCPdlie')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='rwTbRHaawjRxIBfA')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='qYYfktxbiWxpSNuG')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='zncBZfOiWFwqSjyb')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='IElKkVczJbfdamVV')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='nqBqnmvLFuZFYFZo')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='yvAkNVQXSWfjZfPG')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	StatyaZatrat = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяЗатрат', null=True, blank=True, related_name='fvgOhdXDnRgqnfVT')
	NomenklaturnayaGruppa = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НоменклатурнаяГруппа', null=True, blank=True, related_name='aKogkAqepRbmLGMR')
	PodrazdelenieZatraty = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПодразделениеЗатраты', null=True, blank=True, related_name='pSnUzzwzVGnwzAKl')
	SummaUslug = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаУслуг')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class AkkreditivPoluchennyy(models.Model):
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='dQkIuYeLSESKeBxE')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='lrOleQhLVneIBsly')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='eFcQREXKhfNSxPml')

	DokumentOsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='YklYKIxmUBjQMbaG')
	DokumentOsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПокупателя', null=True, blank=True, related_name='xWLJSPZCNJrGFNNB')
	DokumentOsnovaniePlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='lMiGMWBmlGXyrrck')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='QWkWwGVcvNkrLniw')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='DekVSudMcSOgyuyL')
	DokumentOsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РеализацияТоваровУслуг', null=True, blank=True, related_name='rrgOuwwiCUpUVvUi')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='eVkVOoObxfnGOnPt')

	DokumentPlanirovaniyaPostupleniya = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПланированияПоступления', null=True, blank=True, related_name='PbgJFmVyEGyHGXAk')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='GrcqWkUdjmpDMcXr')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='EKIMFKXHqpMZPBmP')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='yUWoVdmHKGwtpYpf')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='ULLvxqPdzwxJPFAU')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='bmKyCMvfcZDrtTXl')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='CYotPKZOyhfaLEqJ')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='XKnDMoPSuLJiwIzZ')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PostuplenieTovarovUslug(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='cEWkONDvZzxxcdnf')
	VidPostupleniya = models.ForeignKey('VidyPostupleniyaTovarov', verbose_name='ВидПоступления', null=True, blank=True, related_name='oELopiJAYcaNtmol')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='ДатаВходящегоДокумента')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='RFQwOyBmvcSmqrQV')
	BankovskiySchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетКонтрагента', null=True, blank=True, related_name='itpTynScMwlJQNJn')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагентp', null=True, blank=True, related_name='kkCkWffMLYCYGKXd')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	NDSVklyuchenVStoimost = models.BooleanField(default=False, verbose_name='НДСВключенВСтоимость')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='RtrQSbRYgjQtRJcl')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='ZPYCgxwEfRYXLiim')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВНалоговомУчете')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВУправленческомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='dVfxOMvFXjvslsbI')
	RegistrirovatTSenyPostavschika = models.BooleanField(default=False, verbose_name='РегистрироватьЦеныПоставщика')

	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='aPiRRZFACSXdUJyO')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='VvIuWycFRVptuslC')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='mJYmCMYjRyBNHtVU')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='HfySlvglGydUsbhu')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='JWfJlEdSgNvQrKjk')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='GxqkBuWbodBVhEct')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='mhVjJOjkScAmSENZ')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='shJMWLWaqLXmsZGm')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='idTHavejyrCWSUyk')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='fBRRtBcPJFLfZQPc')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='BCJhAkPWkaIoaWad')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='jpXqTMyqfGftrTja')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='NGRPmLhCrtupvsCv')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='HlhbCJNkiciIKmfS')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='LVSKXizqyLJFbzcN')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='NAZRBfqPGNhXWUov')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='LhbyhwcrcaMzSoYg')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='RFTnNxJJkeqTWHhg')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='PEdOojcDYfcBhMhI')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='EmOqMSerioQkEsRM')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='CZEqfZxRVNkEiyeW')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='DnWIojfCUqXFJwHd')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='fbLbTsyZFgzQYdAA')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='IXpVWAAssQNtHlvz')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='RFzVJfGHFdvnVpJw')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='aYCDLMdHxyFrzoCR')

	SkladOrderPrihodnyyOrderNaTovary = models.ForeignKey('PrihodnyyOrderNaTovary', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладОрдер-ПриходныйОрдерНаТовары', null=True, blank=True, related_name='IcAfMPCPPPrkMhzL')
	SkladOrderSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладОрдер-Склады', null=True, blank=True, related_name='AbzxXSzzrZSDsjtH')

	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='CgXNOpvrNlUoNRjG')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='lJtKadnPrqrZtxiy')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='KmuFGHhBzVqqVlmV')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='PjVzCzEuXuLrfOlC')

	Gruzootpravitel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузоотправитель', null=True, blank=True, related_name='hZZFtNgrWigENiqx')
	Gruzopoluchatel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', null=True, blank=True, related_name='BlCpLAQkmrNBQmwx')
	NomerVhodyaschegoDokumentaElektronnogoObmena = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокументаЭлектронногоОбмена')
	DataVhodyaschegoDokumentaElektronnogoObmena = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='ДатаВходящегоДокументаЭлектронногоОбмена')

	def __str__(self):
		return self.Nomer


class PlatezhnoeTrebovaniePoluchennoe(models.Model):
	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='QMfOowpulCELGKGi')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='lagClrWbzlKcCQlq')
	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', null=True, blank=True, related_name='EwbLnxwTgmUABSbA')
	DokumentOsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='KuYeaCEplwXvpbnF')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='GGvJCbcRsDXvrjTi')
	DokumentOsnovanieZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='hHqRFygkmQWJZEWS')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='CkafASLLESPPeUwO')
	DokumentOsnovanieSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПоставщика', null=True, blank=True, related_name='TXMwfMVFopcMAicp')

	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='lTtTBUxZDTpBRpSB')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='pdfywcRGbWaffnGm')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='QxhXbsAbKqBymlYZ')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='hteLDuJuVwChRvGb')
	VidPlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидПлатежа')
	OcherednostPlatezha = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ОчередностьПлатежа')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='eAkrLqzUzjdTDEQD')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='JWWJRCaEeiBxsUkg')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='FyCnuXNvVQpqYLtU')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='KwFzOAVAQpAFuUfS')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='GKYkitxILWYVkzyP')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='JfNwvJLXMTrfRuXd')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class OtchetKomissioneraOProdazhah(models.Model):
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='SJQZMQfFjLBREBox')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='thcCCHXuuuLgJsgP')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='ZEABxkzMFJWWbIKu')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	NomenklaturnayaGruppa = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НоменклатурнаяГруппа', null=True, blank=True, related_name='QyVKFMbDeldxOCVF')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='caSNoawrGuqnwaGO')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='VUuzTOBfDDmoRnny')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='XvIsAHaxxPIfexkt')
	ProtsentKomissionnogoVoznagrazhdeniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентКомиссионногоВознаграждения')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='ifGPWThTGsgDJoLj')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='SPHOSmNgIUTiccAl')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='sLyOjlWBtKGrXFON')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='SfmoSTQDMxIpEjSn')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='ISAVyPFRkUxDuhos')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='JqDkofmNyZRhHRkA')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='tfGitLKjYucBZWwd')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='tmzoRqrRnAANnDXq')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='RHSGfDNVmQLEGWIp')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='AnMeVtGRrOTvZxTa')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='yLKbXICpEXNwPGBM')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='KNNkutfeRtriWkup')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='XLsozfvBxzyaRHGB')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='wlCXSIOpEzYnoGiw')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='cLLDTDhSNIbbcNGr')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='jdZOzoAmJOiNUzyP')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='CTecJUrqCRJJpbiF')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='TQpDMhuwxoupnEPq')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='uLbenHHFjUSdAeYd')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='NpAOrerHQCYJmZmf')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='iNUnTIMyZRIQgmUY')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='aOiUPwRjbaCMuwlJ')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='bTAFggroyKrzPmFk')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='AyxXTgQHAauSCszI')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='WnPxRnmQIZdrDCsu')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='oDMZXFBTonoTvFzw')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='hOejuAkiNOBfkHFa')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='XAzsrFwZeYQNCErj')

	SposobRaschetaKomissionnogoVoznagrazhdeniya = models.ForeignKey('SposobyRaschetaKomissionnogoVoznagrazhdeniya', verbose_name='СпособРасчетаКомиссионногоВознаграждения', null=True, blank=True, related_name='VGipqoMVXOmSAwZl')
	StavkaNDSVoznagrazhdeniya = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДСВознаграждения', null=True, blank=True, related_name='uaZRLUqHJHNvFwgO')
	StatyaZatrat = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяЗатрат', null=True, blank=True, related_name='wdvlPXLOPqlFHKlB')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаВзаиморасчетов')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='gQxXAsoJofpyETtg')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='EbwVbtBnShWnovsO')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='GkFiJRPBFvufQiMk')

	UderzhatKomissionnoeVoznagrazhdenie = models.BooleanField(default=False, verbose_name='УдержатьКомиссионноеВознаграждение')
	Gruzootpravitel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузоотправитель', null=True, blank=True, related_name='ojerebCwTGWpmObm')
	Gruzopoluchatel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', null=True, blank=True, related_name='LtSQplkmuIBKOijZ')
	NDSVklyuchenVStoimost = models.BooleanField(default=False, verbose_name='НДСВключенВСтоимость')
	NomerVhodyaschegoDokumentaElektronnogoObmena = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокументаЭлектронногоОбмена')
	DataVhodyaschegoDokumentaElektronnogoObmena = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокументаЭлектронногоОбмена')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PostuplenieDopRashodov(models.Model):
	class Meta:
		verbose_name = 'Поступление Доп Расходов'
		verbose_name_plural = 'Поступление Доп Расходов'

	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')

	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieDopRashodov', null=True, blank=True, verbose_name='ВидОперации', related_name='EyWyqgQCsnyCiqPE')
	ValyutaDokumenta = models.ForeignKey('Valyuty', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', related_name='xyznGwCvBlMzHwJg')

	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', related_name='gieHEkfgWvPelAWM')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', related_name='MqgWbXCUoIqPEGBs')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, null=True, blank=True, decimal_places=4, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='EsPAKaUdcFaqyWdh')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='clSuXPhoNWhmFvpz')
	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', related_name='iQmDtyTSNvmVIxnn')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='JxZTUTkwOTZmosOH')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='ZHpYAwloobipUdLR')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='ZVwMyGvaBqFjvrGh')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='XpGaTFxmpDCWevYW')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='mSFohVxZvdSQoFAX')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='HHngMCVupzHGeBdX')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='JkqUCAwgQemOdiaU')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='vObepplXaIqtCNtv')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='oYqSAgbGUcQJyYrC')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='YKFIKZEgGPoMcxNA')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='uQYhIjimftXzEaeQ')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='bohPIQSSKCXTHsSe')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='hSnuVkeqhAXMaPcN')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='yvegZXTstETeEHIa')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='butnoCCQFcAYYdnO')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='WztpEuBLhURVELaF')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='CuVnASLZYsYyTvfx')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='dYkOWIDnZhaTrKhY')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='UvlQndMvpSdINwUr')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='LikbmjjJfKylMVTR')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='dHuRUagYosiFmfle')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='tXBOPyRwHyyYfAoO')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='wourvxlueNWVjRqM')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='NyKYibcLmYuXJYIz')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='pBQoAkDcXsxitXeE')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='PIpuaRtVnNkfCNDJ')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='boCvMVWktdHDnbnK')

	Soderzhanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Содержание')
	SposobRaspredeleniya = models.ForeignKey('SposobyRaspredeleniyaDopRashodov', verbose_name='СпособРаспределения', null=True, blank=True, related_name='umfgLqpXQkqYVDvf')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='wYZyGaclstHjVyaV')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='JqYBWmBwzEDLsBZt')
	NDSVklyuchenVStoimost = models.BooleanField(default=False, verbose_name='НДСВключенВСтоимость')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='ДатаВходящегоДокумента')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class ProchieZatraty(models.Model):
	UdalitZakaz = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьЗаказ', null=True, blank=True, related_name='AvFmGxQOvqhAoPfr')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='FsnHASlMdQAkRZXV')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='wqtBAHFFDuljIEar')
	UdalitOtrazhatVUkravlencheskomUchete = models.BooleanField(default=False, verbose_name='УдалитьОтражатьВУкравленческомУчете')
	UdalitOtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='УдалитьОтражатьВБухгалтерскомУчете')
	UdalitOtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='УдалитьОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='eKYmrQzffgIlxbrE')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class ZayavkaNaRashodovanieSredstv(models.Model):
	VidOperatsii = models.ForeignKey('VidyOperatsiyZayavkiNaRashodovanie', verbose_name='ВидОперации', null=True, blank=True, related_name='tSPzyqtAdSumOlbk')
	DataRashoda = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаРасхода')

	PoluchatelKassyKKM = models.ForeignKey('KassyKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Получатель-КассыККМ', null=True, blank=True, related_name='nasejANOUprkQIQm')
	PoluchatelSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Получатель-Склады', null=True, blank=True, related_name='pMobssJpmWEGvaiU')
	PoluchatelFizicheskieLitsa = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Получатель-ФизическиеЛица', null=True, blank=True, related_name='zZGKOmLpLgoIpseb')

	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='UlyTIjIWXMWYZChs')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='UwIPvkpQjJnCIgHp')
	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', null=True, blank=True, related_name='HhfSNbZXEFzOVZdU')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='gvWZroOzuLiNXBnE')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='gASLgMLKVfhZhOgY')
	DokumentOsnovanieSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПоставщика', null=True, blank=True, related_name='VQdoRreAWLJVTjtP')
	DokumentOsnovanieProchieZatraty = models.ForeignKey('ProchieZatraty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПрочиеЗатраты', null=True, blank=True, related_name='CqKpRXgEhfqvZcwR')

	FormaOplaty = models.ForeignKey('VidyDenezhnyhSredstv', verbose_name='ФормаОплаты', null=True, blank=True, related_name='oUzgvgCHunxZWlwG')

	BankovskiySchetKassaBankovskieScheta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетКасса-БанковскиеСчета', null=True, blank=True, related_name='RuikWRaRVBBjcaQq')
	BankovskiySchetKassaKassy = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетКасса-Кассы', null=True, blank=True, related_name='TWHpguKsXYHiKUst')

	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='CCsNsSirVkvujuyN')
	KursDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсДокумента')
	KratnostDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьДокумента')
	ValyutaVzaimoraschetovPodotchetnika = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаВзаиморасчетовПодотчетника', null=True, blank=True, related_name='ynurvctzzUlcTZtL')
	RaschetnyyDokument = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент', null=True, blank=True, related_name='uxHLJLYHathJXqSm')
	DataPogasheniyaAvansa = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаПогашенияАванса')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TSFO = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЦФО', null=True, blank=True, related_name='fyPiOKSZuNIPIcyh')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='nhrcrzogKUdbUaTG')

	NomenklaturaNomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура-Номенклатура', null=True, blank=True, related_name='jzTLXtWVavJFixdJ')
	NomenklaturaNomenklaturnyeGruppy = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура-НоменклатурныеГруппы', null=True, blank=True, related_name='STDGCaCEeJjIYgve')

	Sostoyanie = models.ForeignKey('SostoyaniyaObektov', verbose_name='Состояние', null=True, blank=True, related_name='pVsnNJsdFBpyeint')
	Opisanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Описание')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='OuaOIrBmgmgBApSL')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='rrhAkPChSaxLNYgP')
	AvtoRezervirovaniePoZayavke = models.BooleanField(default=False, verbose_name='АвтоРезервированиеПоЗаявке')
	AvtoRazmescheniePoZayavke = models.BooleanField(default=False, verbose_name='АвтоРазмещениеПоЗаявке')
	VklyuchatVPlatezhnyyKalendar = models.BooleanField(default=False, verbose_name='ВключатьВПлатежныйКалендарь')
	VidVydachiDenezhnyhSredstv = models.ForeignKey('VidVydachiDenezhnyhSredstv', verbose_name='ВидВыдачиДенежныхСредств', null=True, blank=True, related_name='yoxFYZncEQDUHdzk')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class InkassovoePorucheniePoluchennoe(models.Model):
	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='NiDpnNeQEYFhgdmK')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='OrMFeEkkhCPjUFFP')
	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', null=True, blank=True, related_name='nsgWiJKOtaTHRxmE')
	DokumentOsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='tEIqPvlWSFYHUpvz')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='LGnNZloESEwSOPNb')
	DokumentOsnovanieZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='xECiLPCDnPcNuTzj')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='gYBSikgUGHLHqSQB')
	DokumentOsnovanieSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПоставщика', null=True, blank=True, related_name='eVZNWiBtHxuzeNID')

	ZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='KJGitRKlcDAyUcks')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='bDUcfwdQzYgxUiaC')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='PDiudMPYCYPUFTbK')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='AKFytatvcnnatYzs')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='zbeSceuHKoqHtwyQ')
	VidPlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидПлатежа')
	OcherednostPlatezha = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ОчередностьПлатежа')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='sOrxYHsuvZuuCwIG')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='GrbEOuttvIPpebBE')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='PgzYfMAlPVufdVvH')
	VidOperatsii = models.ForeignKey('VidyOperatsiySpisanieBaznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='BJYkqOOJwyAdHumc')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='pMjnXsotKhtKXbpy')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='eKEHMzyMMDKWPASC')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PlatezhnoePoruchenieIshodyaschee(models.Model):
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='jgHxnQGGPuERxgyO')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPPIshodyaschee', verbose_name='ВидОперации', null=True, blank=True, related_name='MRNOqkxMpYZhcQWM')
	VidPlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидПлатежа')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='oGaSdVjafCGIdfsf')

	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='uFzdjXSKftyiOgHT')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='ZMPEjmhWSSyPifKp')
	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', null=True, blank=True, related_name='dIBxwoQVFajsyjJy')
	DokumentOsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='sSajnvJYJNvXoEac')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='QXsntVSuuuSkBCVb')
	DokumentOsnovanieZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='KPkAoCVWqfjBoLDL')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='QhSszhvMDpVSrEfY')
	DokumentOsnovanieSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПоставщика', null=True, blank=True, related_name='zwSMCITGMinCprab')

	INNPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПлательщика')
	INNPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПолучателя')
	KodBK = models.CharField(max_length=100, null=True, blank=True, verbose_name='КодБК')
	KodOKATO = models.CharField(max_length=100, null=True, blank=True, verbose_name='КодОКАТО')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='iRJBIrBUYHZfqJPA')
	KPPPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППлательщика')
	KPPPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППолучателя')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='mdQUEZSrNWBupNUP')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='qFMVwHyUGWuDaDkT')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	OcherednostPlatezha = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ОчередностьПлатежа')
	PokazatelDaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ПоказательДаты')
	PokazatelNomera = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПоказательНомера')
	PokazatelOsnovaniya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПоказательОснования')
	PokazatelPerioda = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПоказательПериода')
	PokazatelTipa = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПоказательТипа')
	StatusSostavitelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='СтатусСоставителя')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='hZIHIBmLxbxDEYeI')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='BTSHsMwPTiovgXAT')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='kCwaYMRTmkyWIEUr')
	TekstPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПлательщика')
	TekstPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПолучателя')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	FizLitso = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ФизЛицо', null=True, blank=True, related_name='fjwczzeuxtIOttby')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='EBcPQafPpVkkVmWU')
	ValyutaVzaimoraschetovRabotnika = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаВзаиморасчетовРаботника', null=True, blank=True, related_name='mJhgQAUozEsTBPHW')
	DataPogasheniyaAvansa = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаПогашенияАванса')
	RaschetnyyDokumentRabotnika = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокументРаботника', null=True, blank=True, related_name='xbitqkcALwZNTfqm')
	PerechislenieVByudzhet = models.BooleanField(default=False, verbose_name='ПеречислениеВБюджет')
	VidPerechisleniyaVByudzhet = models.ForeignKey('VidyPerechisleniyVByudzhet', verbose_name='ВидПеречисленияВБюджет', null=True, blank=True, related_name='UMnZVZiPGlSEBond')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PlaniruemoePostuplenieDenezhnyhSredstv(models.Model):
	VidOperatsii = models.ForeignKey('VidyOperatsiyPlaniruemoePostuplenieDS', verbose_name='ВидОперации', null=True, blank=True, related_name='MjIFRdLHGZjtbnas')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='qbnQhRCLFpkZAUAv')

	KassaKKMKassyKKM = models.ForeignKey('KassyKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КассаККМ-КассыККМ', null=True, blank=True, related_name='NWRXzbalKUKqnGuW')
	KassaKKMSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КассаККМ-Склады', null=True, blank=True, related_name='yPhntFcNerOYdmNl')

	DataPostupleniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаПоступления')

	DokumentOsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПокупателя', null=True, blank=True, related_name='LLwbmQBkOrytUXxh')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='PxLaJTAuiClpwJFs')
	DokumentOsnovanieOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетОРозничныхПродажах', null=True, blank=True, related_name='hyZgcrMsNWuljvNG')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='PhEOmRqFDeIyKejg')
	DokumentOsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РеализацияТоваровУслуг', null=True, blank=True, related_name='DWBajvAWhzCuHogU')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='zJCGFgYCtfSWaIzA')

	FormaOplaty = models.ForeignKey('VidyDenezhnyhSredstv', verbose_name='ФормаОплаты', null=True, blank=True, related_name='YbLFNEsYqETOoYqS')

	BankovskiySchetKassaBankovskieScheta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетКасса-БанковскиеСчета', null=True, blank=True, related_name='jZEhjKPkWbIaTvlS')
	BankovskiySchetKassaKassy = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетКасса-Кассы', null=True, blank=True, related_name='chyYQfTiPaeIRfvh')

	ValyutaDokumeta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумета', null=True, blank=True, related_name='UeMoERGSBmprzQMo')
	KursDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсДокумента')
	KratnostDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьДокумента')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Sostoyanie = models.ForeignKey('SostoyaniyaObektov', verbose_name='Состояние', null=True, blank=True, related_name='GaNIVWOLVVbIGGKI')
	Opisanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Описание')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='vXwibfxcpEePwBFG')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='BYgkCbLEzORUFhGf')
	StatyaOborotov = models.CharField(max_length=100, null=True, blank=True, verbose_name='СтатьяОборотов')
	TSFO = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЦФО', null=True, blank=True, related_name='gNBNbQaLWQOVcpZq')
	VklyuchatVPlatezhnyyKalendar = models.BooleanField(default=False, verbose_name='ВключатьВПлатежныйКалендарь')
	VidPriemaRoznichnoyVyruchki = models.ForeignKey('VidPriemaRoznichnoyVyruchki', verbose_name='ВидПриемаРозничнойВыручки', null=True, blank=True, related_name='uPCHrNqgbiNnaivv')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class ElektronnoePismo(models.Model):
	pass


class InventarizatsiyaTovarovNaSklade(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='UOhWaSFgIaDjuWGx')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='iblzCADvVEbUWojL')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='USxWdSVzBjXiwGPv')
	UchityvatSerii = models.BooleanField(default=False, verbose_name='УчитыватьСерии')
	UsloviyaProvedeniyaInventarizatsii = models.FileField(upload_to='files/', verbose_name='УсловияПроведенияИнвентаризации')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class OtchetORoznichnyhProdazhah(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')
	KassaKKM = models.ForeignKey('KassyKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='КассаККМ', related_name='eYTOnkECKYrxtfYt')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='uONcKbZdNMQLsqXD')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='cGGhtUkqHgCiVJIw')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	InventarizatsiyaTovarovNaSklade = models.ForeignKey('InventarizatsiyaTovarovNaSklade', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнвентаризацияТоваровНаСкладе', null=True, blank=True, related_name='mpTfCKVGCtEVXIzf')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='eIEQZTRbtYbjlPbZ')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='rZurreArOaIOVurB')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='pXiXrwHQmGKseOMo')
	VidOperatsii = models.ForeignKey('VidyOperatsiyOtvetORoznichnyhProdazhah', verbose_name='ВидОперации', null=True, blank=True, related_name='xRSVLtnKvFmgVDqK')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='mnQPRRPHMxmxwzGw')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='sUHqPTCXctBuuKEE')

	UslovieProdazh = models.ForeignKey('UstloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='cioKueFjpWsggJcY')
	DogovorEkvayringa = models.ForeignKey('DogovoryEkvayringa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорЭквайринга', null=True, blank=True, related_name='sHsiyaUpjLtElTKG')
	Ekvayrer = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Эквайрер', null=True, blank=True, related_name='VAFJvJhGXXsTlXpa')
	DogovorVzaimoraschetovEkvayrera = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорВзаиморасчетовЭквайрера', null=True, blank=True, related_name='kJCOpDJuaCLLkHQq')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='VPurQwgwBsIJiWux')
	ProchayaBeznalichnayaOplata = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПрочаяБезналичнаяОплата')

	def __str__(self):
		return self.Nomer


class PrihodnyyKassovyyOrder(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='ziiCRkAApZLPPzWF')
	Kassa = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Касса', null=True, blank=True, related_name='RMIDmdLqCMYrUhuC')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='ovJYCOMJcPUrwiRx')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPKO', verbose_name='ВидОперации', null=True, blank=True, related_name='tEzXdEHeJhFPJXrZ')

	KontragentKassyKKM = models.ForeignKey('KassyKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-КассыККМ', null=True, blank=True, related_name='HPUoxKiiAtvqJqqr')
	KontragentKontragenty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-Контрагенты', null=True, blank=True, related_name='YfFKOvnPiLRiPChO')
	KontragentSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-Склады', null=True, blank=True, related_name='mmSOesofgTQNdSjR')
	KontragentFizicheskieLitsa = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-ФизическиеЛица', null=True, blank=True, related_name='cnUWLNvCPGrXujXR')

	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='knGqZGBEmBGAinDi')
	ValyutaVzaimoraschetovRabotnika = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаВзаиморасчетовРаботника', null=True, blank=True, related_name='tJJfsRzgelJgmOib')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='JvHPdwvnjrlJeYeL')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')

	RaschetnyyDokumentPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='iZlNcCOnBxacsBkZ')
	RaschetnyyDokumentRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-РасходныйКассовыйОрдер', null=True, blank=True, related_name='ioEtGcDfxzmqelxB')
	RaschetnyyDokumentPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='jgAYOTaSdeLHBgxp')

	PrinyatoOt = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПринятоОт')
	Osnovanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Основание')
	Prilozhenie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Приложение')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='pSxnQDmeudJuIQIJ')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')

	DokumentOsnovanieDenezhnyyCHek = models.ForeignKey('DenezhnyyCHek', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ДенежныйЧек', null=True, blank=True, related_name='eGSVvQBHntboYOff')
	DokumentOsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПокупателя', null=True, blank=True, related_name='lgbLVEoBkkrdSVZL')
	DokumentOsnovanieRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РасходныйКассовыйОрдер', null=True, blank=True, related_name='VzATzyetcwUbzGqM')
	DokumentOsnovaniePlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='QtZhqxCKLiqFwkwk')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='lwpuCGnXqBejgabv')
	DokumentOsnovanieOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетОРозничныхПродажах', null=True, blank=True, related_name='DhjhuwqUdwfNPXDb')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='lIAyjLqdTFrchECy')
	DokumentOsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РеализацияТоваровУслуг', null=True, blank=True, related_name='kmnNzZEHVIWypllW')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='ZrjBTADhDCHKFqyJ')

	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='wkSSfUNNhPlKOkPS')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='TWPkDjshfoblqhhv')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='tjxRKpFoypUcqzQl')
	NomerCHekaKKM = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НомерЧекаККМ')
	VidPriemaRoznichnoyVyruchki = models.ForeignKey('VidPriemaRoznichnoyVyruchki', verbose_name='ВидПриемаРозничнойВыручки', null=True, blank=True, related_name='WYDUurquVgtlObaa')
	DenezhnyyCHek = models.ForeignKey('DenezhnyyCHek', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДенежныйЧек', null=True, blank=True, related_name='CdWBfEeXNhYsrrda')
	VyruchkaSNTT = models.BooleanField(default=False, verbose_name='ВыручкаСНТТ')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class VnutrenniyZakaz(models.Model):
	VidZakaza = models.ForeignKey('VidyVnutrennegoZakaza', verbose_name='ВидЗаказа', null=True, blank=True, related_name='TsGgAdEejHvmDHvb')
	UdalitVremyaNapominaniya = models.DateField(auto_now=False, auto_now_add=False, verbose_name='УдалитьВремяНапоминания')
	DataOtgruzki = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОтгрузки')

	ZakazchikPodrazdeleniya = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Заказчик-Подразделения', null=True, blank=True, related_name='DVKEZqSuaSCJjoaU')
	ZakazchikSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Заказчик-Склады', null=True, blank=True, related_name='xEtCgyrsdXvMtjum')

	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	UdalitNapomnitOSobytii = models.BooleanField(default=False, verbose_name='УдалитьНапомнитьОСобытии')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='xzCbOqFWulHyZVTs')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='VxgSYFlEpcfWpzND')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='OyJRmCzVCmqvLYud')
	Ispolnitel = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Исполнитель', null=True, blank=True, related_name='KjlciiuUQgTjvrTU')
	PodrazdelenieIspolnitel = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПодразделениеИсполнитель', null=True, blank=True, related_name='pKLGQMgLOXsRPWAL')
	DokumentOsnovanie = models.ForeignKey('Sobytie', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование', null=True, blank=True, related_name='gJRvZOJCtvoazbru')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PeremeschenieTovarov(models.Model):
	VidOperatsii = models.ForeignKey('VidyOperatsiyPeremeschenieTovarov', verbose_name='ВидОперации', null=True, blank=True, related_name='HFTIqiklEIQyoNgf')
	VnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВнутреннийЗаказ', null=True, blank=True, related_name='WwvspxoYzrGHrqvV')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='vCphxneAoJIZjEhE')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='kZUbefnBLpSbaQze')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='qMZFHmQTXyTcjvZg')
	SkladOtpravitel = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладОтправитель', null=True, blank=True, related_name='biuYnEypIDoXXtBt')
	SkladPoluchatel = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладПолучатель', null=True, blank=True, related_name='KgZueGrqGECfOVuX')
	NDSvStoimostiTovarov = models.ForeignKey('DeystvieNDSVStoimostiTovarov', verbose_name='НДСвСтоимостиТоваров', null=True, blank=True, related_name='tvrleHXGIsLchqLS')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PrihodnyyOrderNaTovary(models.Model):
	VidOperatsii = models.ForeignKey('VidyOperatsiyPrihodnyyOrder', verbose_name='ВидОперации', null=True, blank=True, related_name='dzUrcDmbiOxPczgQ')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='ICthhDMmktQgdujl')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='iQfQcKNWwjfFNvce')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='cjxHmNsSAPZNtCrO')
	FizLitso = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ФизЛицо', null=True, blank=True, related_name='JSeuOSOTXEKwXVhc')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='AakCpAUruVDNLryd')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='aWAssomDbAwIMiNM')
	BezPravaProdazhi = models.BooleanField(default=False, verbose_name='БезПраваПродажи')
	DokumentPeremescheniya = models.ForeignKey('PeremeschenieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПеремещения', null=True, blank=True, related_name='XYTdOqMEKjRroamH')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class VozvratTovarovOtPokupatelya(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='FWdfneabkWhKzAGL')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='aqcsDNhPgXREsFiB')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='ZmsxknRjMrgAOSwF')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВНалоговомУчете')

	SkladOrderPrihodnyyOrderNaTovary = models.ForeignKey('PrihodnyyOrderNaTovary', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладОрдер-ПриходныйОрдерНаТовары', null=True, blank=True, related_name='sleHkEhQstJXmhrw')
	SkladOrderSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладОрдер-Склады', null=True, blank=True, related_name='uWsmDdGyFmLkJTNO')

	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='IGVWfKxqLnGQKoez')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='FCZuxoRnZgOpKymI')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')

	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='fwFhRaELyHhKCbhf')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='xWVpCXAMxqLQgqUJ')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='QuglrTyULTGfzBbC')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='tGQKWcmRnbkYWsmN')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='ImcXoXrkDCcxVjBE')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='eueQYnZqoARPYwQe')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='kiheyYwmMAqTLvOm')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='fODidctPGSNYmVqq')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='REgesZbjWHbqQRio')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='McFiaUMpIZCKEfzN')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='THhYxXnXustZWnwT')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='ngxClbMXWgsLgrfA')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='HcvSEgSfunoXXZEp')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='GhdiJOtwnZuEFrEB')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='CveRhukiDSLkWjzw')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='qdXJoGbwoGiNaKqs')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='QLFaSyPTkmCKtkKE')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='LYSRygGuJJNAkNUv')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='UEdflxAkFoDQyGPQ')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='mZXLWKStSQqmWzpk')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='mUhYtbvNoebXwohH')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='imLkhDKcKUaKeCPM')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='mBORcuajOTiSjvcF')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='mnJuKceMdeoFfHff')

	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='SgJDDvoIPjsXshQj')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='LzqtNaRVgOHPLaDT')
	VidPostupleniya = models.ForeignKey('VidyPostupleniyaTovarov', verbose_name='ВидПоступления', null=True, blank=True, related_name='kyyjuIeYEHuYOSBz')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='pRgrnsjOQOhEuUpr')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='VftxiAOVZmGhXZQN')

	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='pKdFGaMIlCSQwEeL')
	DiskontnayaKarta = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДисконтнаяКарта', null=True, blank=True, related_name='aFhAAKPCGXXbCzUI')
	OtrazitVKnigePokupok = models.BooleanField(default=False, verbose_name='ОтразитьВКнигеПокупок')
	PokupatelemVystavlyaetsyaSchetFakturaNaVozvrat = models.BooleanField(default=False, verbose_name='ПокупателемВыставляетсяСчетФактураНаВозврат')
	NomerVhodyaschegoDokumentaElektronnogoObmena = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокументаЭлектронногоОбмена')
	DataVhodyaschegoDokumentaElektronnogoObmena = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокументаЭлектронногоОбмена')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	def __str__(self):
		return self.Nomer


class ZakazPostavschiku(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='OYUuPISXigpoxKjM')
	UdalitVremyaNapominaniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='УдалитьВремяНапоминания')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	DataPostupleniya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаПоступления')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='pxsJMUAgCDJyJYXU')
	IspolzovatPlanovuyuSebestoimost = models.BooleanField(default=False, verbose_name='ИспользоватьПлановуюСебестоимость')
	ItogPlanovayaSebestoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ИтогПлановаяСебестоимость')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='VajEMGeXkcsWYdoh')
	UdalitKontaktnoeLitso = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьКонтактноеЛицо', null=True, blank=True, related_name='oHKnpqHyttevukeW')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	UdalitNapomnitOSobytii = models.BooleanField(default=False, verbose_name='УдалитьНапомнитьОСобытии')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='pymSthsMSukqmozc')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='HGadEmopPopOuTDz')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='MVbIvlqCVPRUbqfj')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='eZWruVzVpDictprY')

	StrukturnayaEdinitsaBankovskieScheta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтруктурнаяЕдиница-БанковскиеСчета', null=True, blank=True, related_name='fLAfplGPRhflERQk')
	StrukturnayaEdinitsaKassy = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтруктурнаяЕдиница-Кассы', null=True, blank=True, related_name='UJyMbSniKoLeZLDZ')

	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='stpFqOjzrAkUWNil')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='paiAQFYmXindxeJW')
	KontaktnoeLitsoKontragenta = models.ForeignKey('KontaktnyeLitsaKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтактноеЛицоКонтрагента', null=True, blank=True, related_name='wgavdXtwwpfycdEx')
	
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PlatezhnoeTrebovanieVystavlennoe(models.Model):
	DokumentOsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='PcDStDMoBopuQZPl')
	DokumentOsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПокупателя', null=True, blank=True, related_name='TzJZGiTEGJOcJohP')
	DokumentOsnovaniePlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='ElwUhEgfKsEnjPAQ')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='sZUbVLOTsqSdOFug')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='vDsDbqVbBXlGVzRL')
	DokumentOsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РеализацияТоваровУслуг', null=True, blank=True, related_name='GjWHuRRWFmuSMuMi')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='fCldCVdoRZAlmpYe')

	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='RrteqMMJVUvOwCNn')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='TBLscloPTSNeaAhZ')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='AaxrBUfVSHdULKBW')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='dIqYrXLzfDDlkyfE')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='mpPUBZUvzOBxzFrG')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='gxBFWYktbHbVFriA')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='ZtLJAblvDfkIOUwm')
	VidPlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидПлатежа')
	OcherednostPlatezha = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ОчередностьПлатежа')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	TekstPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПлательщика')
	TekstPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПолучателя')
	INNPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПлательщика')
	KPPPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППлательщика')
	INNPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПолучателя')
	KPPPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППолучателя')
	SrokDlyaAktsepta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СрокДляАкцепта')
	UslovieOplaty = models.ForeignKey('UsloviyaOplatyRaschetnyhDokumentov', verbose_name='УсловиеОплаты', null=True, blank=True, related_name='KVCliqXuCWqxGWeg')
	OsnovanieDlyaBezaktseptnogoSpisaniya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ОснованиеДляБезакцептногоСписания')
	DataOtsylkiDokumentov = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОтсылкиДокументов')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='rkCadBptVVYlTYNK')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='bpgVRJjajQuHOXzf')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='rSRMoueiyhzBdpoj')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class AkkreditivPeredannyy(models.Model):
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='rfYlFlrlgOKzoqol')
	VidAkkreditiva = models.ForeignKey('VidyAkkreditivov', verbose_name='ВидАккредитива', null=True, blank=True, related_name='IubkGTELCRtnjiKt')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='UzyctZEpFiXSgZgO')
	VidPlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидПлатежа')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='zxBbZiYZiZwLPmdi')

	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='zuMIHPWbSMmYNJKD')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='kUqwuiKTmvvNyTwT')
	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', null=True, blank=True, related_name='NNDqaepAHgEMRBRe')
	DokumentOsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='uMUlrScqmRFrBIVC')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='ElsfULJpKdheylqA')
	DokumentOsnovanieZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='ynfuVNUiaJeXNQFL')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='sjySVOzJfZgwXgaO')
	DokumentOsnovanieSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПоставщика', null=True, blank=True, related_name='NnRpACKZgaGOBXnq')

	DokumentyKPredyavleniyu = models.CharField(max_length=100, null=True, blank=True, verbose_name='ДокументыКПредъявлению')
	DopolnitelnyeUsloviya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ДополнительныеУсловия')
	ZAyavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗАявкаНаРасходованиеСредств', null=True, blank=True, related_name='cokAGnVbGyZdhmnQ')
	INNPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПлательщика')
	INNPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ИННПолучателя')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='PZAEEcdKjFqEUCEq')
	KPPPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППлательщика')
	KPPPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='КПППолучателя')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='nEdXROEhTmMmuApG')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='uJPNwzAprCDoAkSK')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	OtrazhatVOperUchete = models.BooleanField(default=False, verbose_name='ОтражатьВОперУчете')
	SrokDeystviya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='СрокДействия')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='BAjzpzBiTIZMOgPJ')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	SchetDeponenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='СчетДепонента')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='nQMgUBPNlqrrwjBa')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='FWCQZvYxubDRMrMW')
	TekstPlatelschika = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПлательщика')
	TekstPoluchatelya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТекстПолучателя')
	UslovieProdazh = models.ForeignKey('UsloviyaOplatyRaschetnyhDokumentov', verbose_name='УсловиеПродаж', null=True, blank=True, related_name='hpprYWceINHNNnPW')
	CHastichnayaOplata = models.BooleanField(default=False, verbose_name='ЧастичнаяОплата')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='dZxNooLrCOqwmAXl')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PostuplenieTovarovUslugVNTT(models.Model):
	BankovskiySchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетКонтрагента', null=True, blank=True, related_name='jRgUsCWqRfVgRsGe')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='ERZWMVqsXjTSXLfY')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieTovarovVNTT', verbose_name='ВидОперации', null=True, blank=True, related_name='SkAFOjoyGXhDrNUs')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='gFYHkIEuLIGsWTCW')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='TCqRuCvvkuxGOmir')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	NDSVklyuchenVStoimost = models.BooleanField(default=False, verbose_name='НДСВключенВСтоимость')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='EzAvHzUPYZLNZcRf')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='QrKfrmxlOpAWaokf')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='mhXUQszecyOTQldc')
	RegistrirovatTSenyPostavschika = models.BooleanField(default=False, verbose_name='РегистрироватьЦеныПоставщика')

	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='lnetWfHcBAWOWnzi')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='ZZibVrIrPxAqdJlS')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='MujkjOqnGnviGtRx')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='duKkQyGBzSPbbyMt')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='kcklAXvtaqRUBudO')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='JpDpspcAstahACYE')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='igcorYTSPBlmqvYX')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='omKLELgTFzInRpxW')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='DKjrGzadokiAFuEq')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='InxqlltUfUOfmGJA')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='CkVffttVOhZcjxIJ')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='XTOVPDmZSXaoDATV')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='YLXEGyAqYPtcLSFe')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='DPPtXlzuqGNWhOMo')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='mlNIOHvIMMHSfBGm')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='ZfOtLpxOyOvYTZXL')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='dUoNZtyeXozFmSoQ')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='SShRvhJWoIDnEBOS')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='UvWiAseniBqtJrGZ')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='CrLADSKvZjlcPvep')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='bMKKkkflbkwsBoUs')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='slgpdOjpygYUjoIz')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='lWvBYqezGXXGEavL')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='TbAdcfZTtXxQaEar')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='iowMxYXLlZwmSXNr')

	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='fQkunNjQamEnAVRi')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='YaBBiZpxVOvmvrJs')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	DokumentPeremescheniya = models.ForeignKey('PeremeschenieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПеремещения', null=True, blank=True, related_name='JUxywGgoFTYFVSmA')
	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='ggsyHpnbwvRQtiYA')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='nesEejtXDswgxgpb')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='qFHQLXMVAqnIsrQV')

	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class OtchetKomitentuOProdazhah(models.Model):
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='OiwJDjkdpfBcUVpd')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='MMGnXIKdSZMvzXYc')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	SposobRaschetaKomissionnogoVoznagrazhdeniya = models.ForeignKey('SposobyRaschetaKomissionnogoVoznagrazhdeniya', verbose_name='СпособРасчетаКомиссионногоВознаграждения', null=True, blank=True, related_name='mJnxdwNIDjspGokB')
	UderzhatKomissionnoeVoznagrazhdenie = models.BooleanField(default=False, verbose_name='УдержатьКомиссионноеВознаграждение')
	SummaVoznagrazhdeniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаВознаграждения')
	StavkaNDSVoznagrazhdeniya = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДСВознаграждения', null=True, blank=True, related_name='GedaPdRhgbaLnDWR')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='wmQKYdZjVHooKydH')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='SqSBlnQrPMmIeEVl')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='rNjoSSIbojCWbVdQ')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='ZKeZtragTcGEIvnD')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='QuRVgtQCiyqPCmHt')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='AsimewmhfPzeNHpf')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='ASKmdfFUPVIKkfAc')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='EsDJBBkplVSJBaeL')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='oZjiyADcYXarCaJq')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='IUhUXCFgwbeKFpyA')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='AVHQaLXJyqBgjPUq')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='RFzyoLSlPaBVWhLb')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='XCByWyDKcgHFlIEg')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='QAnhArqILEdNQEey')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='xFccpXIobLgKGxbN')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='AkeHRlhaFDakwikp')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='CHnCnUmNnIvAvxGF')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='LSogKVgfoAccNJBS')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='YQDHYhvwagggSgvm')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='gpQVKXtcDpRKBWoS')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='tCCiieKLtzdPGFjU')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='gmAfnxDxovdifuds')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='gxFbFioyRMaKeUBp')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='equrDDDCZPisJVXf')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='KXhNcauAjqAnHnvF')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='lEOrzVfaDHDVJNav')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='KNKHcCwZnRQLVMiw')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='dUtePzJUmmnWGYJJ')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='xemOrqWaYLWwKbWe')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='qoFDbPMGfezREeCL')

	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='AdenkUsGyKoMHHmg')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	ProtsentKomissionnogoVoznagrazhdeniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентКомиссионногоВознаграждения')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='NJFNMpVDinfPrCdV')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='PxBopNxRDKSkmIXx')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='lubKZdjNuaGXMOCb')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='PktpkwnlPzLCZtSm')

	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class RealizatsiyaTovarovUslug(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	VidOperatsii = models.ForeignKey('VidyOperatsiyRealizatsiyaTovarov', verbose_name='ВидОперации', null=True, blank=True, related_name='XgasBzsxZWPoaumx')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='nJXnSyVdYOJwoQbG')
	BankovskiySchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетОрганизации', null=True, blank=True, related_name='LoTvDgPpyllFYwVA')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=True, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='iQFyFtFVmrXNJPIy')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='xEHouaFschImQtjb')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='keHksmNmxhGbdKHT')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='GhBTaUVzYApPqWFm')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='hMnRGodyxyHhJwDD')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='YOnTTbOmyxrLjbtF')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='GYqnBkTtcvQexksC')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='gGppCiiZMaaKYEsl')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='LCtINMdIrTkGhhau')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='hriyeHUHEJsatkxn')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='YcHwPcGiDlKKvpBr')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='JKZbaUNURblyXhQY')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='nOuQoWSYNURHkiCl')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='dJFIbjoEBQVxkffe')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='IhVvgIwPjJCIzNPB')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='VPMQTarbOYoRgJDE')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='iOUrCbpLqHfSBiMv')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='kZxpMaRNPlQDcpif')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='PNJznrKSmLtFiRgy')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='SggWqKTxMETxmZhT')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='pVCApomPIGuVWkSe')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='vYkVpSPaVzWDDyIB')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='erlZazxqFEECnPRy')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='aQmXlxbfNIVovFzv')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='OKdoudxxegNjeHkZ')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='yjVxnBLzlyNfDxsG')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='HbRxRLsxssJIjIPd')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='NHojXIPTTVhdcEmZ')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='ouckJBpKBQIBeAUs')

	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='DaWeCgfYHpRdaBiq')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='dSkuEVdbfsDpJIUJ')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='HtZAtuKAYqQJgEoX')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='FrybprReAaqGBfJI')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='KDLpNLjjLmXZCkjl')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='eVIGAEphDXMdVRlZ')
	VidPeredachi = models.ForeignKey('VidyPeredachiTovarov', verbose_name='ВидПередачи', null=True, blank=True, related_name='UpGGpEfEXHCSWcZD')
	AdresDostavki = models.CharField(max_length=100, null=True, blank=True, verbose_name='АдресДоставки')
	Gruzopoluchatel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', null=True, blank=True, related_name='FTnEGflnNqFEkPge')
	Gruzootpravitel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузоотправитель', null=True, blank=True, related_name='FTnEGflnNqFEkPgae')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='uFpcpSUByCAdBEts')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='NQyJEFkIQhilhqTp')

	DiskontnayaKarta = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДисконтнаяКарта', null=True, blank=True, related_name='IApQIzUUTBroJpNs')
	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='wavFojtbAYiiptVd')
	OtklyuchitKontrolVzaimoraschetov = models.BooleanField(default=False, verbose_name='ОтключитьКонтрольВзаиморасчетов')
	OtpuskRazreshil = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтпускРазрешил', null=True, blank=True, related_name='WbztJjjXYahoXHba')
	OtpuskProizvel = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтпускПроизвел', null=True, blank=True, related_name='XfDLxESiJBOJbpRk')
	DoverennostNomer = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ДоверенностьНомер')
	DoverennostData = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДоверенностьДата')
	DoverennostVydana = models.CharField(max_length=100, null=True, blank=True, verbose_name='ДоверенностьВыдана')
	DoverennostCHerezKogo = models.CharField(max_length=100, null=True, blank=True, verbose_name='ДоверенностьЧерезКого')
	DopolnenieKAdresuDostavki = models.CharField(max_length=100, null=True, blank=True, verbose_name='ДополнениеКАдресуДоставки')

	def __str__(self):
		return self.Nomer


class PlatezhnyyOrderPostuplenieDenezhnyhSredstv(models.Model):
	RaschetnyyDokumentPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='LOgXUHGjbeOlQFDk')
	RaschetnyyDokumentInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='xpHBNQiLYOyyoufp')
	RaschetnyyDokumentPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='fQMMmLzygdTAYAbl')
	RaschetnyyDokumentAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент-АккредитивПолученный', null=True, blank=True, related_name='jYyXETCpNLjcdQQN')

	DokumentOsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПокупателя', null=True, blank=True, related_name='dKupWhTdlCaQZahH')
	DokumentOsnovaniePlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='VgNzCOMTjvgAUlnL')
	DokumentOsnovaniePlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='wQATagNppmOQQDXH')
	DokumentOsnovanieInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='aPZRkNNTirhszBoy')
	DokumentOsnovaniePlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='PLhLmCOjegKYdgFD')
	DokumentOsnovanieAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АккредитивПолученный', null=True, blank=True, related_name='eNqVGLLqHualBzxF')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='CxXUGdSmXXiYkJRP')

	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='zyuHcLhlKgiqDayD')
	SchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетОрганизации', null=True, blank=True, related_name='HwrrBJttHRGzIrVG')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='YjbkeVgAFyxLigam')
	SchetKontragenta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетКонтрагента', null=True, blank=True, related_name='YsLhMhEgNuJPJJjl')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='CsKEfrmeOdsicDKd')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='LPEBnmOZKSQEBQLW')
	VidOperatsii = models.ForeignKey('VidyOperatsiyPostuplenieBeznalichnyhDenezhnyhSredstv', verbose_name='ВидОперации', null=True, blank=True, related_name='PwxoCJvcmfPwrFFB')
	OtrazhenoVOperUchete = models.BooleanField(default=False, verbose_name='ОтраженоВОперУчете')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='sMuHkkgGcAxvbYRq')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='uNjYGOxRDFtDdVOr')
	Oplacheno = models.BooleanField(default=False, verbose_name='Оплачено')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='GjUdHEwmytzjaqsU')
	KursNaDatuPriobreteniyaRealizatsiiValyuty = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсНаДатуПриобретенияРеализацииВалюты')
	NaznacheniePlatezha = models.CharField(max_length=100, null=True, blank=True, verbose_name='НазначениеПлатежа')
	StatyaZatrat = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяЗатрат', null=True, blank=True, related_name='kCpJkHmOdzkwEKNN')
	NomenklaturnayaGruppa = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НоменклатурнаяГруппа', null=True, blank=True, related_name='TJRRUAvbbOGssmsO')
	PodrazdelenieZatraty = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПодразделениеЗатраты', null=True, blank=True, related_name='fwGuHPWMFqktenTo')
	SummaUslug = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаУслуг')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class SchetNaOplatuPokupatelyu(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	AdresDostavki = models.CharField(max_length=100, null=True, blank=True, verbose_name='АдресДоставки')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='UrKeXeDtLxfccEuG')
	UdalitVremyaNapominaniya = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='УдалитьВремяНапоминания')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	DataOtgruzki = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОтгрузки')
	DiskontnayaKarta = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДисконтнаяКарта', null=True, blank=True, related_name='JGyKwqxrDArEhMSw')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='BZMPwakJtnMFHEbw')
	ZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПокупателя', null=True, blank=True, related_name='YrSsArXXpMUoqFDJ')
	IspolzovatPlanovuyuSebestoimost = models.BooleanField(default=False, verbose_name='ИспользоватьПлановуюСебестоимость')
	ItogPlanovayaSebestoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ИтогПлановаяСебестоимость')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')

	KontragentKontragenty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-Контрагенты', null=True, blank=True, related_name='lJWWdbcLTAoOKxxZ')
	Kontragentstr = models.CharField(max_length=100, null=True, blank=True, verbose_name='Контрагент-str')

	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	UdalitNapomnitOSobytii = models.BooleanField(default=False, verbose_name='УдалитьНапомнитьОСобытии')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='hiuzCEfHxnJaUSGV')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='xzwSwMfQXQknFkkl')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='EizBTiYzBsvvTlfM')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='MFxRCqFaXVOsuNWT')

	StrukturnayaEdinitsaBankovskieScheta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтруктурнаяЕдиница-БанковскиеСчета', null=True, blank=True, related_name='eNpiMpTnPSAPPkRM')
	StrukturnayaEdinitsaKassy = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтруктурнаяЕдиница-Кассы', null=True, blank=True, related_name='pQnIsirgjrLKzFOA')

	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='kQQogTAwKqlWCxMa')

	UdalitKontaktnoeLitsoKontaktnyeLitsa = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьКонтактноеЛицо-КонтактныеЛица', null=True, blank=True, related_name='YtEpsFMftYmtCboh')
	UdalitKontaktnoeLitsostr = models.CharField(max_length=100, null=True, blank=True, verbose_name='УдалитьКонтактноеЛицо-str')

	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	Gruzopoluchatel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', null=True, blank=True, related_name='fMouNrbSWtYjCues')

	KontaktnoeLitsoKontragentastr = models.CharField(max_length=100, null=True, blank=True, verbose_name='КонтактноеЛицоКонтрагента-str')
	KontaktnoeLitsoKontragentaKontaktnyeLitsaKontragentov = models.ForeignKey('KontaktnyeLitsaKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтактноеЛицоКонтрагента-КонтактныеЛицаКонтрагентов', null=True, blank=True, related_name='zQgxNlFJPqZbSPcR')

	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='sJdYEneKNwePSXyC')
	DopolnenieKAdresuDostavki = models.CharField(max_length=100, null=True, blank=True, verbose_name='ДополнениеКАдресуДоставки')
	Gruzootpravitel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузоотправитель', null=True, blank=True, related_name='XgJxjsKgedlhayed')

	def __str__(self):
		return self.Nomer


class KorrektirovkaDolga(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='kHBPqpxAILBmZfGt')
	KontragentDebitor = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтрагентДебитор', null=True, blank=True, related_name='OMYGbqDEGCqkZIcW')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='uLebfGmCZVoGybrt')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='fReqGBUiebUxxMLX')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	VidOperatsii = models.ForeignKey('VidyOperatsiyKorrektirovkaDolga', verbose_name='ВидОперации', null=True, blank=True, related_name='EAzflbhFqMOMjPTo')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='etRKShJMXIGMZaAy')
	KursDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсДокумента')
	KratnostDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьДокумента')
	KontragentKreditor = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтрагентКредитор', null=True, blank=True, related_name='aOSnqRdLsnVfcFFx')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='qCwhBvNeQTDaCrWl')

	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='gBrHgOfKUBpGewMd')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='nUFShYdHHuBuBlZA')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='XraqGTMHJHbMhgIA')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='ePaHIEbXnBGBzJXb')

	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class VozvratTovarovPostavschikuIzNTT(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='IjWtGQnnpNcJwdaD')
	BankovskiySchetOrganizatsii = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанковскийСчетОрганизации', null=True, blank=True, related_name='GbUcwLzXCPdqNAfN')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	OtrazhatVNalogovomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВНалоговомУчете')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='REuLCYIhKWomgNAJ')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='iXsNFHSHcAjOTynb')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='CsCEOHWeKMWsRjoO')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='eauQNQfJKnSIRIQc')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='WfeUkfSADSDfFRMg')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='EFYGjFGbiWNAOpZC')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='oCNUwgTGcmkCgJke')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='PpBHXPtzpLjIwaow')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='kdJfLOThKWxmWexr')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='XtlCFCTUvlAWJfSx')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='apgYTqEnRCAVANzN')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='FmrpQYhklvfxhtcb')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='dweCEQOUPdyvSGYs')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='tbuAePLbcyXhASQA')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='xVOpGWYuRGlBqWaK')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='FyEAybBfRIpUCfds')
	SdelkaPlatezhnyyOrderDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='gozipWDcLtScmANd')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='eNbvBVtWPjHQfdkT')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='rhKXwoGWxjuyFlMH')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='AYKCHKgWuVffgfrD')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='WUbiknaYbtHwdSSa')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='HrnERvOsRJdSwWxh')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='aFygFSHhTixSbKDQ')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='sgjgqKAuYlFjmaSE')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='IykzakvMyhPrZoRW')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='pZTyFOpfLPvDExXj')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='gygByUauPUHUnGGi')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='zXKbFrOdsmolUsPu')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='pFmhUBKjBPCeIjpQ')

	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='GdxhRAtjmjTmXSNC')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='WYvPEFAvbhOwxplx')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='FvOFdTbuUYpiJVpc')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='VjfhJbEgCoRsYgAS')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='BXFIJmQKgJjlqNDM')
	UchityvatNDS = models.BooleanField(default=False, verbose_name='УчитыватьНДС')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='nxHgRwlzvrwGfPoz')
	NDSVklyuchenVStoimost = models.BooleanField(default=False, verbose_name='НДСВключенВСтоимость')
	Gruzopoluchatel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', null=True, blank=True, related_name='BkXgedaEwZPplaFF')
	PostavschikuVystavlyaetsyaSchetFakturaNaVozvrat = models.BooleanField(default=False, verbose_name='ПоставщикуВыставляетсяСчетФактураНаВозврат')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='rCfmXVSDlBjrWpjr')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='xajhasLtyGRzAjiD')

	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', null=True, blank=True, related_name='XxPqSSAtrwIuQCas')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class RezervirovanieTovarov(models.Model):
	ZakazZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Заказ-ЗаказПокупателя', null=True, blank=True, related_name='NjfzxABDZtICSLoN')
	ZakazVnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Заказ-ВнутреннийЗаказ', null=True, blank=True, related_name='WbjQxXlCMnkGMDpw')

	VidOperatsii = models.ForeignKey('VidyOperatsiyRezervirovanieTovarov', verbose_name='ВидОперации', null=True, blank=True, related_name='LnSeFqFuANpZRkIG')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='nQZPVreDNyiYlzgf')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='lBTxTtFqDLqsrZsZ')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='YqhTHJYgJnEhGfbn')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='djjzyMszsfODuywm')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class PereotsenkaTovarovPrinyatyhNaKomissiyu(models.Model):
	OtrazhatVUpravlencheskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВУправленческомУчете')
	OtrazhatVBuhgalterskomUchete = models.BooleanField(default=False, verbose_name='ОтражатьВБухгалтерскомУчете')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='wDOFyteBIUtghcIo')
	Sklad = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Склад', null=True, blank=True, related_name='kMVtjLPJxgPjpOyh')
	TipTSen = models.ForeignKey('TipyTSenNomenklaturyKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', null=True, blank=True, related_name='SOnwductjRSCPvQN')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='lUJixiMGqMsLiUPK')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='vNsiQztwYdNyIcWF')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='DxERyPIhhMfqGHwO')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='ipPmgiIOwBmVmZkW')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='CPsbrzzRDWSseBOP')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='cizAokgrtvZWWomd')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='NPTamVPGAsmuWIPn')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='VuFphYZeQrSYEhBA')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='oWqoaiQLjpdsADsN')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='aRbAbccQIKIsGrBp')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='CjTbMftklhxxULXa')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='PziFzSQAqfeluDyJ')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='hyUYXqTTaTXlVNMe')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='nUhKWzKSxDAXycDY')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='twwTgChzArKKewUe')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='LczJzTjhWrWAKxEp')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='geIEGGvwWNuMYBvF')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='mqJBprMbKSgnhFfM')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='YAIdUyYlaGzIsySS')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='HndwvJLdrauLJxOK')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='ZCGhlQRfrLFwcEfy')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='iSdfPbkmkOivoQPC')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='iKihqpJXyQOwehCz')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='CbAdOoBWFEeepNQZ')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='JXYqSyotuszkERoz')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='jOnvmdzaxgnxRRji')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='UkfcrcaARvmIlBou')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='eXEirdgcxfofnYKG')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='nWFmTeXkfsTDzLEF')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='IxkezDWipOQCaIWm')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='skGcKvNJjRZBXRbX')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='kWLGIOUCSFJLVAtk')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='ffJaAFoLbdUQsOeD')

	NomerVhodyaschegoDokumentaElektronnogoObmena = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокументаЭлектронногоОбмена')
	DataVhodyaschegoDokumentaElektronnogoObmena = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокументаЭлектронногоОбмена')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class Sobytie(models.Model):
	AdresElektronnoyPochty = models.CharField(max_length=100, null=True, blank=True, verbose_name='АдресЭлектроннойПочты')
	Vazhnost = models.ForeignKey('Vazhnost', verbose_name='Важность', null=True, blank=True, related_name='TeXIWmqGVUeVHSbB')
	VidObekta = models.ForeignKey('VidyObektovSobytiya', verbose_name='ВидОбъекта', null=True, blank=True, related_name='RKzbdSWmWgNsceXF')
	VidSobytiya = models.ForeignKey('VidySobytiy', verbose_name='ВидСобытия', null=True, blank=True, related_name='dOcHSYCKZXHyhJaq')
	UdalitVremyaNapominaniya = models.DateField(auto_now=False, auto_now_add=False, verbose_name='УдалитьВремяНапоминания')
	IstochnikiInformatsiiPriObraschenii = models.ForeignKey('IstochnikiInformatsiiPriObrascheniiPokupateley', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИсточникиИнформацииПриОбращении', null=True, blank=True, related_name='BasZRvILuNlUELFU')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')

	KontaktnoeLitsoKontaktnyeLitsa = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтактноеЛицо-КонтактныеЛица', null=True, blank=True, related_name='gRzoQtZUfjXQfffn')
	KontaktnoeLitsoKontaktnyeLitsaKontragentov = models.ForeignKey('KontaktnyeLitsaKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтактноеЛицо-КонтактныеЛицаКонтрагентов', null=True, blank=True, related_name='PHnlzWnmtHaGQRGt')
	KontaktnoeLitsostr = models.CharField(max_length=100, null=True, blank=True, verbose_name='КонтактноеЛицо-str')

	KontragentKontragenty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент-Контрагенты', null=True, blank=True, related_name='clEyHnGNxMyGCYmj')
	Kontragentstr = models.CharField(max_length=100, null=True, blank=True, verbose_name='Контрагент-str')

	UdalitNapomnitOSobytii = models.BooleanField(default=False, verbose_name='УдалитьНапомнитьОСобытии')
	NachaloSobytiya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='НачалоСобытия')
	OkonchanieSobytiya = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ОкончаниеСобытия')
	OpisanieSobytiya = models.CharField(max_length=100, null=True, blank=True, verbose_name='ОписаниеСобытия')

	OsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='FQnWsxjIwpUpKmVL')
	OsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='zANLsiRvHvrxhzvX')
	OsnovanieZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ЗаказПокупателя', null=True, blank=True, related_name='TWDpHjGAfLsNozSS')
	OsnovaniePrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='BQTbQtvMUJBGoTQd')
	OsnovaniePlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='nCrVgbSlGwhvCRVZ')
	OsnovanieRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-РасходныйКассовыйОрдер', null=True, blank=True, related_name='uYdalPFfjOGeGozM')
	OsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ЗаказПоставщику', null=True, blank=True, related_name='dbLtSeIIoGkPOtYj')
	OsnovanieRezervirovanieTovarov = models.ForeignKey('RezervirovanieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-РезервированиеТоваров', null=True, blank=True, related_name='yOpxXePWscaCbLLR')
	OsnovanieVnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ВнутреннийЗаказ', null=True, blank=True, related_name='iWjkGYUoxiqJHiMH')
	OsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='TqeiTMGUDinUzFVH')
	OsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='uHTtDFPRIjOeNhOa')
	OsnovanieSobytie = models.ForeignKey('Sobytie', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-Событие', null=True, blank=True, related_name='pUGiywMIZbrihCji')
	OsnovaniePereotsenkaTovarovPrinyatyhNaKomissiyu = models.ForeignKey('PereotsenkaTovarovPrinyatyhNaKomissiyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ПереоценкаТоваровПринятыхНаКомиссию', null=True, blank=True, related_name='OYUbmdmWZWuGWcsC')
	OsnovaniePereotsenkaTovarovOtdannyhNaKomissiyu = models.ForeignKey('PereotsenkaTovarovOtdannyhNaKomissiyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ПереоценкаТоваровОтданныхНаКомиссию', null=True, blank=True, related_name='UXDDxhPwTMzGQHnF')
	OsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ВозвратТоваровПоставщику', null=True, blank=True, related_name='OEmFKFGajwPJcjtG')
	OsnovaniePlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='wPaqdAPvmUmkOSbm')
	OsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='CsTvNTHwpmXxzdyJ')
	OsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='bnLzOHFHxTnZFOHq')
	OsnovanieRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-РеализацияТоваровУслуг', null=True, blank=True, related_name='CsAOYfXwOoSOHENU')
	OsnovanieSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-СчетНаОплатуПоставщика', null=True, blank=True, related_name='LAeBRgbPtRRWilZB')
	OsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-СчетНаОплатуПокупателю', null=True, blank=True, related_name='kUZCOCXkSwFkQrMU')
	OsnovanieElektronnoePismo = models.ForeignKey('ElektronnoePismo', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Основание-ЭлектронноеПисьмо', null=True, blank=True, related_name='aqxYRZQExAXCMuPq')

	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='HDZfNjcdKBMDBsAp')
	Proekt = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект', null=True, blank=True, related_name='YruTHEEBeZJwWfWH')
	SoderzhanieSobytiya = models.CharField(max_length=100, null=True, blank=True, verbose_name='СодержаниеСобытия')
	SostoyanieSobytiya = models.ForeignKey('SostoyaniyaSobytiy', verbose_name='СостояниеСобытия', null=True, blank=True, related_name='ddgRMpolMLcyFdyp')
	TipSobytiya = models.ForeignKey('VyhodyascheeIshodyascheeSobytie', verbose_name='ТипСобытия', null=True, blank=True, related_name='xIbYxkOzxotmJCBI')
	Pomeschenie = models.ForeignKey('Pomescheniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Помещение', null=True, blank=True, related_name='RKCTKyOmGdxdaQuW')
	Territoriya = models.ForeignKey('Territorii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Территория', null=True, blank=True, related_name='QfNFzLJHOTTDyQTj')
	EstVlazheniya = models.BooleanField(default=False, verbose_name='ЕстьВлажения')
	KontaktnoeLitsoKontragenta = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтактноеЛицоКонтрагента', null=True, blank=True, related_name='UkqmkWozEHPBglgc')
	UdalitIntervalNapominaniya = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='УдалитьИнтервалНапоминания')
	PredmetKontakta = models.CharField(max_length=100, null=True, blank=True, verbose_name='ПредметКонтакта')
	GruppaSobytiya = models.ForeignKey('GruppySobytiy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ГруппаСобытия', null=True, blank=True, related_name='jtbUTdojPVDubvss')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


class ZakazPokupatelya(models.Model):
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')

	AdresDostavki = models.CharField(max_length=100, null=True, blank=True, verbose_name='АдресДоставки')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='kLSsEsSNMWnjAVeX')
	UdalitVremyaNapominaniya = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='УдалитьВремяНапоминания')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	DataOtgruzki = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОтгрузки')
	DiskontnayaKarta = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДисконтнаяКарта', null=True, blank=True, related_name='dHIGrDaMwQldNBsM')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='iqivxxXwnWZgWKrP')
	IspolzovatPlanovuyuSebestoimost = models.BooleanField(default=False, verbose_name='ИспользоватьПлановуюСебестоимость')
	ItogPlanovayaSebestoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ИтогПлановаяСебестоимость')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='UOTUOKrkJjukubTI')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	UdalitNapomnitOSobytii = models.BooleanField(default=False, verbose_name='УдалитьНапомнитьОСобытии')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='BEcuLDOnXZLcxmvv')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='PCZxmJXovznOgbcN')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='XiXzYYKycMRqWfHi')
	StrukturnayaEdinitsa = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтруктурнаяЕдиница', null=True, blank=True, related_name='zvBJGRcSZKILkSyA')
	SkladGruppa = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СкладГруппа', null=True, blank=True, related_name='hGHtZDPaQzsDgGOY')
	SummaVklyuchaetNDS = models.BooleanField(default=False, verbose_name='СуммаВключаетНДС')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	TipTSen = models.ForeignKey('TipyTSenNomenklatury', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ТипЦен', related_name='owscZmTgJzmigPFQ')
	UdalitKontaktnoeLitso = models.ForeignKey('KontaktnyeLitsa', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьКонтактноеЛицо', related_name='iZwqgHcBcUPidVEU')
	UchityvatNDS = models.BooleanField(verbose_name='УчитыватьНДС', default=False)
	Gruzopoluchatel = models.ForeignKey('Kontragenty', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', related_name='qaMzTQvofirybtHz')
	KontaktnoeLitsoKontragenta = models.ForeignKey('KontaktnyeLitsaKontragentov', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='КонтактноеЛицоКонтрагента', related_name='uSraKFnvOXnCbQlz')
	UslovieProdazh = models.ForeignKey('UsloviyaProdazh', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='УсловиеПродаж', related_name='lvsvgnuWIKylNQvV')
	DopolnenieKAdresuDostavki = models.CharField(max_length=100, null=True, blank=True, verbose_name='ДополнениеКАдресуДоставки')

	DokumentOsnovanieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ЗаказПоставщику', related_name='YSdkQPljAApRVUAu')
	DokumentOsnovanieSobytie = models.ForeignKey('Sobytie', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-Событие', related_name='EQxSofqWUbrYCiED')
	DokumentOsnovanieSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-СчетНаОплатуПокупателю', related_name='EMxUebFBGSzBaAXz')

	Gruzootpravitel = models.ForeignKey('Kontragenty', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузоотправитель', related_name='PuRIcMTDvFtoXPJz')
	NomerVhodyaschegoDokumentaElektronnogoObmena = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокументаЭлектронногоОбмена')
	DataVhodyaschegoDokumentaElektronnogoObmena = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='ДатаВходящегоДокументаЭлектронногоОбмена')

	def __str__(self):
		return self.Nomer


class VvodNachilnyhOstatkovNDS(models.Model):
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='tqTjsmcmKlkyWDdU')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='kALpPZLGadFCbtTi')
	VidOperatsii = models.ForeignKey('VidyOperatsiyVvodNachOstatkovNDS', verbose_name='ВидОперации', null=True, blank=True, related_name='vKAWVPNLUgqtSsji')
	OtrazitRaschetySKontragentami = models.BooleanField(default=False, verbose_name='ОтразитьРасчетыСКонтрагентами')


class OtrazhenieRealizatsiiTovarovIUslugNDS(models.Model):
	Organizatsiya = models.ForeignKey('Organizatsii', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Организация', null=True, blank=True, related_name='lAxdIYweRXzqHMia')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='vBBdmwoNjluvomDo')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='bouSUAdDRpjqqmqr')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='wAGLtddXuANZtoJC')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='fKozSFurkCIJzfxJ')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='SkZndXPLqpcbmpSf')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='RgcyHAkDUjrNNqGi')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='oBkEHoTlYiGMpYam')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='lGskOhDtWMaXPZCR')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='usbNQKjYJYbeGiJi')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='uPojkvQwFHtIFrEc')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='wWXhqqTDlEZEHSOL')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='rpGqKQhxsvLAUSLl')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='jJqycJHhrMQWBomJ')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='XexdcUChBFAWyydm')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='fMVkelLXsWteeRId')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='sdRuLjEsCwnANqyI')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='oHMguiJDuyUKuhCV')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='wYZepEMJKxKBajeU')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='NkumAfyonsjMDAit')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='ooslNRBEOVzlrTwh')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='qJpaiCXjimojSOdB')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='wJbQikzrSAvTwdnK')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='fWgprMEdQjtFjLaU')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='kiouxcgKtafYdVwh')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='vWOaZDDhgfpsMgKJ')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='njUFtEZReGvbFYIv')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='aSXJKPswCFDPoMCH')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='IXTFkjNBTSqWDUyG')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='CJsnbJuzNjbOAAhq')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='bZeMglpQmnkebsXW')

	RaschetnyyDokument = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасчетныйДокумент', null=True, blank=True, related_name='XharMWDUIACcYdfT')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	SummaDokumenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаДокумента')
	Kommentariy = models.CharField(max_length=100, null=True, blank=True, verbose_name='Комментарий')
	ValyutaDokumenta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаДокумента', null=True, blank=True, related_name='COAzuxVPSdlzOLyZ')
	PryamayaZapisVKnigu = models.BooleanField(default=False, verbose_name='ПрямаяЗаписьВКнигу')
	Gruzootpravitel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузоотправитель', null=True, blank=True, related_name='jtxdIaHKgRYjakub')
	Gruzopoluchatel = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Грузополучатель', null=True, blank=True, related_name='fjsdKVlLaGyhUrXe')
	Otvetstvennyy = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='hTLcuVDnOMwLdtpi')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Nomer = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер')
	Data = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')
	Ssylka = models.IntegerField(null=True, blank=True, verbose_name='Ссылка')
	Proveden = models.BooleanField(default=False, verbose_name='Проведен')


#
##
###
####
#####
###### Таблицы
#####
####
###
##
#

class OtvetstvennyeLitsaOrganizatsii(models.Model):
	FizicheskoeLitso = models.ForeignKey('FizicheskieLitsa', limit_choices_to={'PometkaUdaleniya': False}, verbose_name='ФизЛицо', null=True, blank=True, related_name='S3duHcZEZAjKa')
	DolzhnostiOrganizatsiy = models.ForeignKey('DolzhnostiOrganizatsiy', limit_choices_to={'PometkaUdaleniya': False}, verbose_name='Должность', null=True, blank=True, related_name='SduHcZ1ZEZAjKa')
	Organizatsii = models.ForeignKey('Organizatsii', null=True, blank=True, related_name='SdcZZPju2EZAjKa')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')

class Oplata(models.Model):
	CHekKKM = models.ForeignKey('CHekKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЧекККМ', related_name='gdufYaDYUQiixVJG')
	VidOplaty = models.ForeignKey('VidyOplatCHekaKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВидыОплатЧекаККМ', related_name='UaCGoKu1QtqjXlgUp')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='Удалить')


class DataNomerDokumentovOplaty(models.Model):
	DataPlatezhnoRaschetnogoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаПлатежноРасчетногоДокумента')
	NomerPlatezhnoRasschetnogoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерПлатежноРассчетногоДокумента')
	SchetFakturaPoluchennyy = models.ForeignKey('SchetFakturaPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактураПолученный', null=True, blank=True, related_name='DTnfxJopZnHXeumI')
	SchetFakturaVydannyy = models.ForeignKey('SchetFakturaVydannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактураВыданный', null=True, blank=True, related_name='JCZwlEuOwLoXUnUd')


class DokumentyOsnovaniya(models.Model):
	DokumentOsnovanieVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='hfcDzAaJuwayHNsR')
	DokumentOsnovanieVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='ABRCaaeFAbNIMdFv')
	DokumentOsnovanieInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='HUulfgudrxXNsBmc')
	DokumentOsnovaniePlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='SnklEKjtTaWWIJON')
	DokumentOsnovaniePostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеДопРасходов', null=True, blank=True, related_name='kIpphmCBKfqVAWUH')
	DokumentOsnovanieRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-РасходныйКассовыйОрдер', null=True, blank=True, related_name='IKIiCpSxoBwslXWi')
	DokumentOsnovanieAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АккредитивПереданный', null=True, blank=True, related_name='tSptAryhAjIwKEmW')
	DokumentOsnovaniePostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='tgrJqkeUPGQsuXYH')
	DokumentOsnovanieOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='vvxwKgVWdIOSBjUU')
	DokumentOsnovaniePlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='jtOeBWTeoqyGwnhD')
	DokumentOsnovanieDokumentRaschetovSKontragentom = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='oKBkScQngsZCWgzk')
	DokumentOsnovanieVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ВозвратТоваровПоставщику', null=True, blank=True, related_name='wwbYWljNOsFRmkhf')
	DokumentOsnovaniePostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='RXMgCcIKyETNHUMB')
	DokumentOsnovanieOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='brKtFKnNPUYNTdis')
	DokumentOsnovaniePlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='UblyKIkEppnIhtFM')
	DokumentOsnovanieOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='RiTgsQUjSPCMzlIV')
	DokumentOsnovanieAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-АвансовыйОтчет', null=True, blank=True, related_name='bqIPDrdSUwCLPeVt')
	DokumentOsnovanieKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОснование-КорректировкаДолга', null=True, blank=True, related_name='VVACpsMLDwcPeOlb')

	SchetFakturaPoluchennyy = models.ForeignKey('SchetFakturaPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактураПолученный', null=True, blank=True, related_name='gwtmSlywtLkfdeVv')
	SchetFakturaVydannyy = models.ForeignKey('SchetFakturaVydannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактураВыданный', null=True, blank=True, related_name='WQWiCpNUfEZuKKzG')


class Avansy(models.Model):
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='ffAcpRcXpCktVMtS')

	SchetFakturaPoluchennyy = models.ForeignKey('SchetFakturaPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактураПолученный', null=True, blank=True, related_name='MlFGcxMEkacAplWp')
	SchetFakturaVydannyy = models.ForeignKey('SchetFakturaVydannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактураВыданный', null=True, blank=True, related_name='uuIZMvXzfBiihHNw')


class Razdely(models.Model):
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')
	TamozhennayaStoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ТаможеннаяСтоимость')
	StavkaPoshliny = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СтавкаПошлины')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='NCYBkAMfeixdFDFP')
	SummaPoshliny = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаПошлины')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	PoshlinaVValyute = models.BooleanField(default=False, verbose_name='ПошлинаВВалюте')
	NDSVValyute = models.BooleanField(default=False, verbose_name='НДСВВалюте')
	TamozhennayaStoimostVValyuteReglUcheta = models.BooleanField(default=True, verbose_name='ТаможеннаяСтоимостьВВалютеРеглУчета')
	GTDImport = models.ForeignKey('GTDImport', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ГТДИмпорт', null=True, blank=True, related_name='QgXamWyYOSefEUWC')


class TovaryIUslugi(models.Model):
	Nomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='kyEyBgugYNDNAwZR')
	EdinitsaIzmereniya = models.ForeignKey('EdinitsyIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЕдиницаИзмерения', null=True, blank=True, related_name='sexkOkmAKvtzpQnI')
	Kolichestvo = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Количество')
	KolichestvoMest = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КоличествоМест')
	Koeffitsient = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Коэффициент')
	TSena = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Цена')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='bUkIHDedneQRbleS')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	VvodNachilnyhOstatkovNDS = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВводНачильныхОстатковНДС', null=True, blank=True, related_name='TwScQIWnoJMhtjVD')
	OtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='YYQpSmBsgiwZehUA')


class DannyePoSF(models.Model):
	VvodNachilnyhOstatkovNDS = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВводНачильныхОстатковНДС', null=True, blank=True, related_name='hAKRLWfxzhaTCFqu')
	KlyuchStroki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КлючСтроки')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='wMNPoyEFdTJVmPXk')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='PVMgNHZxECdCBYmz')

	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='SpvWGokXTAQgWQJN')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='gcLFTtIOIIkwTHFW')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='ueWXWgUFvWznyRqt')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='IuvyDOWYqspqypBh')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='jWhOqhbSwMIavEYz')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='CcLIxuiiiVHPwRKu')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='YeEIpoHFmyAYyUdu')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='rxaPRZhzjbUZkmiq')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='oMERvtqOoUMHaJza')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='rIWWKroKAAHQcYxW')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='vIWgSEVEwpmsvJVy')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='mWJmxUpquiYbMByq')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='GlZfMlLKeBiytVot')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='zmTJpuhJjBHBHbdG')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='GXFXwaHJSwdDGXbo')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='EAOzodtazdihCyCq')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='cOwQuHSRUHcQfIrd')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='COtBFXuCmAsMuncx')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='PfYEgabfMsQyiwxA')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='WDhgvcoPuMWmOuzr')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='CoBcQnGOuQbjvGmF')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='QGxMqWiIamWkusYn')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='HxyMIhuhVQqYHFKn')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='lcjmPmsrrTzJfKIh')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='YaGYiGilznIRUgzL')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='hSDQPqCeNzXjMCfk')

	PredyavlenSF = models.BooleanField(default=False, verbose_name='ПредъявленСФ')
	DataSF = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаСФ')
	NomerSF = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерСФ')
	DataPlatezhnoRaschetnogoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаПлатежноРасчетногоДокумента')
	NomerPlatezhnoRasschetnogoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерПлатежноРассчетногоДокумента')

	SchetFakturaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='vwfWdGuylZsQfZev')
	SchetFakturaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='XwepPXoiidFHifLR')
	SchetFakturaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='DEjIGYUPAyODYBEe')
	SchetFakturaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='qAwTmPGORPikxIUG')
	SchetFakturaGTDImport = models.ForeignKey('GTDImport', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ГТДИмпорт', null=True, blank=True, related_name='VFRnMSZmEHNLDeHQ')
	SchetFakturaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПоступлениеДопРасходов', null=True, blank=True, related_name='blZPPvtcsVqdDHdC')
	SchetFakturaOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='gglDCRUCMiBnunol')
	SchetFakturaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='PKsYDEbPskUaKNPA')
	SchetFakturaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='wpBcqqWvrJNkLZcc')
	SchetFakturaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='VZuUFfNRpTgCRrTR')
	SchetFakturaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='nrTubCeQJBJadeRq')
	SchetFakturaSchetFakturaVydannyy = models.ForeignKey('SchetFakturaVydannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-СчетФактураВыданный', null=True, blank=True, related_name='OUwFIwWJpIhagrSa')
	SchetFakturaDokumentRaschetovSKontragentom = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='EJEsTnXhHYDMoxpi')
	SchetFakturaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ВозвратТоваровПоставщику', null=True, blank=True, related_name='QGXOtqDUOsHVOHBu')
	SchetFakturaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='ljBzMvFSijrFgbNU')
	SchetFakturaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-АккредитивПолученный', null=True, blank=True, related_name='MSPmnlEQpfrANdUN')
	SchetFakturaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='nwhTHCqNguOFuyeU')
	SchetFakturaSchetFakturaPoluchennyy = models.ForeignKey('SchetFakturaPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-СчетФактураПолученный', null=True, blank=True, related_name='xhXBlDXBUaTrBzLq')
	SchetFakturaOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='XATvKhdtbiRKHxlW')
	SchetFakturaOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтчетОРозничныхПродажах', null=True, blank=True, related_name='ROdGaYYpUKytMKBi')
	SchetFakturaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='khaGqhrSAsmLVZqI')
	SchetFakturaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-РеализацияТоваровУслуг', null=True, blank=True, related_name='KnOhWBuRCCzyyobD')
	SchetFakturaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='IvUtUybKTUumahvS')

	SummaBezNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДС')
	NDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДС')
	SummaBezNDSOplata = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСОплата')
	NDSOplata = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСОплата')
	SummaBezNDSVklyuchenoVStoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСВключеноВСтоимость')
	NDSVklyuchenoVStoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСВключеноВСтоимость')
	SummaBezNDSStavka0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДССтавка0')
	NDSStavka0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДССтавка0')
	SummaBezNDSPredyavleno = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПредъявлено')
	NDSPredyavleno = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПредъявлено')
	SummaBezNDSPredyavleno = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПредъявлено')
	NDSPredyavleno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПредъявлено0')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	SummaVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаВзаиморасчетов')
	ValyutaVzaimoraschetov = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаВзаиморасчетов', null=True, blank=True, related_name='KrBJRpoTcEkYGaeV')
	ValyutaAvansa = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаАванса', null=True, blank=True, related_name='XglYIvtwFIvYnKRZ')
	ValyutnayaSummaSNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ВалютнаяСуммаСНДС')
	SummaBezNDSPodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПодтверждено0')
	NDSPodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПодтверждено0')
	SummaBezNDSNePodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСНеПодтверждено0')
	NDSNePodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСНеПодтверждено0')
	SummaBezNDSPredyavlenoNePodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПредъявленоНеПодтверждено0')
	NDSPredyavlenoNePodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПредъявленоНеПодтверждено0')
	VvodNachilnyhOstatkovNDS = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВводНачильныхОстатковНДС', null=True, blank=True, related_name='fmjPuDjKbZzJsmLP')


class DopolnitelnyeSvedeniya(models.Model):
	VvodNachilnyhOstatkovNDS = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВводНачильныхОстатковНДС', null=True, blank=True, related_name='xuUzIBkRhcYmVLYV')
	KlyuchStroki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КлючСтроки')
	VidTSennosti = models.ForeignKey('VidyTSennostey', verbose_name='ВидЦенности', null=True, blank=True, related_name='qTYgcgJKMBpVdHaC')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='oLIPJyZnaVNsfYAD')
	SummaBezNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДС')
	NDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДС')
	Nomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='WUZwrvWLTdsrJrMQ')

	DokumentOplatyPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='CsuZjkiUmGyBcXOJ')
	DokumentOplatyPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='PKcpXPqYRFxFIEFF')
	DokumentOplatyRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-РасходныйКассовыйОрдер', null=True, blank=True, related_name='fSLsMvXvHIpZPFZC')
	DokumentOplatyVvodNachalnyhOstatkovNDS = models.ForeignKey('VvodNachalnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ВводНачальныхОстатковНДС', null=True, blank=True, related_name='FHgxQzBQjuCqkGPx')
	DokumentOplatyPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='BUjCmfwfRgalwHpc')
	DokumentOplatyPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='CeIRALPHAYWnUJCv')
	DokumentOplatyOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ОтчетОРозничныхПродажах', null=True, blank=True, related_name='pcZsmJearIBzKljD')
	DokumentOplatyOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='dmzMbAHOhsvqqgxP')
	DokumentOplatyAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-АвансовыйОтчет', null=True, blank=True, related_name='glRoRhgJkWCfgFlo')
	DokumentOplatyPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='JUfSQqAljCkawSDT')

	DokumentOtgruzkiOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОтгрузки-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='IdbUhTiTONjsSPYp')
	DokumentOtgruzkiOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОтгрузки-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='WpMPerxJvZpYYVRM')
	DokumentOtgruzkiRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОтгрузки-РеализацияТоваровУслуг', null=True, blank=True, related_name='aMjSJEAEYiAOOxrf')

	SummaBezNDSOplata = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСОплата')
	NDSOplata = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСОплата')
	SummaBezNDSVklyuchenoVStoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСВключеноВСтоимость')
	NDSVklyuchenoVStoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСВключеноВСтоимость')
	SummaBezNDSStavka0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДССтавка0')
	NDSStavka0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДССтавка0')
	SummaBezNDSPredyavleno = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПредъявлено')
	NDSPredyavleno = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПредъявлено')
	SummaBezNDSPodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПодтверждено0')
	NDSPredyavleno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПредъявлено0')
	ValyutnayaSummaSNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ВалютнаяСуммаСНДС')
	SummaBezNDSPodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПодтверждено0')
	NDSPodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПодтверждено0')
	NDSNePodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСНеПодтверждено0')
	StavkaNDSNePodtverzhdena0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СтавкаНДСНеПодтверждена0')
	SummaBezNDSPredyavlenoNePodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБезНДСПредъявленоНеПодтверждено0')
	NDSPredyavlenoNePodtverzhdeno0 = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='НДСПредъявленоНеПодтверждено0')
	StranaProishozhdeniya = models.ForeignKey('KlassifikatorStranMira', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтранаПроисхождения', null=True, blank=True, related_name='nkaJvlmfKxgxNtOW')
	NomerGTD = models.ForeignKey('NomeraGTD', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НомерГТД', null=True, blank=True, related_name='SHKgTDaPwazyiruG')
	VvodNachilnyhOstatkovNDS = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВводНачильныхОстатковНДС', null=True, blank=True, related_name='mxVLVbJryyEFdPCK')


class RaschetySKontragentami(models.Model):
	VvodNachilnyhOstatkovNDS = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВводНачильныхОстатковНДС', null=True, blank=True, related_name='oIqjceKADhXqoWON')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='QTkjXOtDwwfzpykg')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='IoAtbZnPcAqYJRLh')

	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='tbGsCcGzdSaNAhFn')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='hSaPtvdeutNckaio')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='uUVZzmyMZlEtceEo')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='QnKppkkRokOBfnLk')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='ysuGhuiIrnflsrsA')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='vQIcNPGqmQBejLWx')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='HDgXVcvViVZeRcbG')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='lAxKHpcWhJYwUcKN')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='RvNLggieGZrQWnux')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='zsjTJzhVnZDkeAou')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='sqYVUqtEUKahCsmp')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='AYzJlmlocwjKdelE')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='hjUnDNObkajgaGxx')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='cMulyoQBxiqfJZqw')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='nqSsCJaVmhkyZYPQ')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='EBYKZIyhPhrEjgsn')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='GFdfTbdfdtkPizTG')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='NrLfMwDXYltQLPSU')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='UIEQeZZdssUpcgBl')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='HyVxUawqYQcKudJD')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='ffyobdjmeHLohzVk')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='XCzUWcmIdNAwOOby')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='JtnkllfJgFOfcHTI')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='bgFVdusLJzYaSuId')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='ZKYnEGSGrSXotseb')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='ABQIEMXKIZbOcpHO')

	ValyutaVzaimoraschetov = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВалютаВзаиморасчетов', null=True, blank=True, related_name='MbOZUYNVvnoichNq')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	SummaVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаВзаиморасчетов')
	ValyutnayaSummaVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ВалютнаяСуммаВзаиморасчетов')

	DokumentOplatyPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='TatsKJrcMBHoMdnu')
	DokumentOplatyPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='ZGZXywICrhxyrEGu')
	DokumentOplatyRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-РасходныйКассовыйОрдер', null=True, blank=True, related_name='abKoumVBngFssqAN')
	DokumentOplatyVvodNachalnyhOstatkovNDS = models.ForeignKey('VvodNachalnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ВводНачальныхОстатковНДС', null=True, blank=True, related_name='rrcarSzBxRWzNCEc')
	DokumentOplatyPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='LexklBmrxzKtvdYV')
	DokumentOplatySchetFakturaVydannyy = models.ForeignKey('SchetFakturaVydannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-СчетФактураВыданный', null=True, blank=True, related_name='gsNWmtLiLBnspxzL')
	DokumentOplatyDokumentRaschetovSKontragentom = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='aIKScEQZrFSZGVoJ')
	DokumentOplatyPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='WkqsjYhGVwOyTOuP')
	DokumentOplatyAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-АвансовыйОтчет', null=True, blank=True, related_name='qDoplsQEubvOoVSy')
	DokumentOplatyPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументОплаты-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='ELYymQSOticlidSm')

	Avans = models.BooleanField(default=False, verbose_name='Аванс')

	SchetFakturaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='UCfxpnCJbkcQRItR')
	SchetFakturaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='rLVfCWNhTeUaxdhd')
	SchetFakturaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='RGFPQMBtfosqQdAB')
	SchetFakturaGTDImport = models.ForeignKey('GTDImport', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ГТДИмпорт', null=True, blank=True, related_name='TTWegcXIHFzcruNn')
	SchetFakturaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='sIBViQpDYugrZyXx')
	SchetFakturaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПоступлениеДопРасходов', null=True, blank=True, related_name='vlXYAeQXABpphAys')
	SchetFakturaOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='dtraUtCZflxMoiZs')
	SchetFakturaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='WscNTLvCQJIhMWdN')
	SchetFakturaSpisanieTovarov = models.ForeignKey('SpisanieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-СписаниеТоваров', null=True, blank=True, related_name='PmNsqoHMPRceKFFj')
	SchetFakturaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='UvzfNDOBTlYkeyyc')
	SchetFakturaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='wERxlKshUnKAaTZV')
	SchetFakturaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='nGkHdMDEAVqXSIdL')
	SchetFakturaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='JPTvqIGHuMXVXrDq')
	SchetFakturaDokumentRaschetovSKontragentom = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='TjyCUOAjnIccoszG')
	SchetFakturaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ВозвратТоваровПоставщику', null=True, blank=True, related_name='SZOWobnXXifWyWVi')
	SchetFakturaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-АккредитивПолученный', null=True, blank=True, related_name='qNLLfXHPIcupSbPr')
	SchetFakturaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='bDpgRTefxuCRjyHd')
	SchetFakturaSchetFakturaPoluchennyy = models.ForeignKey('SchetFakturaPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-СчетФактураПолученный', null=True, blank=True, related_name='ftKYhDPsZjWSYVOr')
	SchetFakturaOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='ZyHNqsctYYMBThgb')
	SchetFakturaOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтчетОРозничныхПродажах', null=True, blank=True, related_name='hgxCesRcwwfRSrdK')
	SchetFakturaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='zkBjOYteCatxoJgI')
	SchetFakturaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-РеализацияТоваровУслуг', null=True, blank=True, related_name='kywJNEkqcDkVWCWf')
	SchetFakturaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура-КорректировкаДолга', null=True, blank=True, related_name='fXBSycRuRnJKouGd')

	RaschetySByudzhetom = models.BooleanField(default=False, verbose_name='РасчетыСБюджетом')
	VvodNachilnyhOstatkovNDS = models.ForeignKey('VvodNachilnyhOstatkovNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВводНачильныхОстатковНДС', null=True, blank=True, related_name='inVcWOVjYuxkVLIW')


class VidyDeyatelnosti(models.Model):
	class Meta:
		verbose_name = 'Виды деятельности'
		verbose_name_plural = 'Виды деятельности'

	VidDeyatelnosti = models.ForeignKey('VidyDeyatelnostiKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Вид деятельности', null=True, blank=True, related_name='UaCGoKuQtqjXlgUp')
	Otvetstvennyy = models.ForeignKey('KontaktnyeLitsaKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Ответственный', null=True, blank=True, related_name='vErLizhvhuZpCwsL')
	Kontragenty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагенты', null=True, blank=True, related_name='GDBMcpWDRaHuFlNk')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')

class MenedzheryPokupatelya(models.Model):
	MenedzherPokupatelya = models.ForeignKey('Polzovateli', limit_choices_to={'PometkaUdaleniya': False},verbose_name='МенеджерПокупателя', null=True, blank=True, related_name='gYdcweBrcwWCZUyP')
	Kontragenty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагенты', null=True, blank=True, related_name='iqzgddOCNrReLuae')


class TarifyZaRaschetnoeObsluzhivanie(models.Model):
	class Meta:
		verbose_name = 'Тарифы За Расчетное Обслуживание'
		verbose_name_plural = 'Тарифы За Расчетное Обслуживание'

	VidOplaty = models.ForeignKey('VidyOplatCHekaKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Вид оплаты', null=True, blank=True, related_name='wcSalTbxRRyeQpcB')
	ProtsentTorgovoyUstupki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='% торговой уступки')
	DogovoryEkvayringa = models.ForeignKey('DogovoryEkvayringa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорыЭквайринга', null=True, blank=True, related_name='HhRdVwHeJJWVkJhJ')
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')


class Tovary(models.Model):
    Valuta = models.ForeignKey('Valyuty', limit_choices_to={'PometkaUdaleniya': False}, null=True, blank=True, verbose_name='Валюта', related_name='Q1QXuG3qWOpSEsT')
    SposobRaschetaTSeny = models.ForeignKey('SposobyRaschetaTSeny', null=True, blank=True, verbose_name='СпособРасчетаЦены', related_name='xOaZnjgxEtIquOcr')
    TipTSenNomenklatury = models.ForeignKey('TipyTSenNomenklatury', null=True, blank=True, verbose_name='ТипЦенНоменклатуры', related_name='aZxtIquOnjgxEOcr')
    NaimenovanieTovara = models.CharField(max_length=80, null=True, blank=True, verbose_name='НаименованиеТовара')
    UstanovkaTSenNomenklatury = models.ForeignKey('UstanovkaTSenNomenklatury', null=True, blank=True, verbose_name='УстановкаЦенНоменклатуры', related_name='ajgquOEOcZxnxtIr') #Товары
    EdinitsaPoKlassifikatoru = models.ForeignKey('KlassifikatorEdinitsIzmereniya', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЕдиницаПоКлассификатору', related_name='YbzoCjLGfXzICuxv')
    CHekKKM = models.ForeignKey('CHekKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЧекККМ', related_name='YbGICuzofXzCjLxv')
    Doverennosti = models.ForeignKey('Doverennosti', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='Доверенности', related_name='YWdghVYhiQBHoyPO')
    PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')
    Kachestvo = models.ForeignKey('Kachestvo', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Качество', null=True, blank=True, related_name='WCMMi1NFybRdVTBlX')
    SpisanieTovarov = models.ForeignKey('SpisanieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СписаниеТоваров', null=True, blank=True, related_name='RLZfGxucGdmKdOfj')
    PereotsenkaTovarovOtdannyhNaKomissiyu = models.ForeignKey('PereotsenkaTovarovOtdannyhNaKomissiyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПереоценкаТоваровОтданныхНаКомиссию', null=True, blank=True, related_name='DvmgxhxlOSQjOtqi')
    EdinitsaIzmereniya = models.ForeignKey('EdinitsyIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЕдиницаИзмерения', null=True, blank=True, related_name='DJsqsISmpCqKiuaA')
    EdinitsaIzmereniyaMest = models.ForeignKey('EdinitsyIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЕдиницаИзмеренияМест', null=True, blank=True, related_name='IRJhmzMzIhdEmSOQ')
    Kolichestvo = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Количество')
    KolichestvoMest = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КоличествоМест')
    Koeffitsient = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Коэффициент')
    Nomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='hhhmibGyDcuWOGGZ')
    PlanovayaSebestoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПлановаяСебестоимость')
    ProtsentSkidkiNatsenki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентСкидкиНаценки')
 
    RazmeschenieSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Размещение-Склады', null=True, blank=True, related_name='MiNFShtqvHeQEwjl')
    RazmeschenieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Размещение-ЗаказПоставщику', null=True, blank=True, related_name='rCRuWKNAtoGSQWlP')
    RazmeschenieVnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Размещение-ВнутреннийЗаказ', null=True, blank=True, related_name='fBgYDWDZGshOocFi')
 
    StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='NVVBbCiFwmDnaRRy')
    Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
    SummaTovara = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаТовара')
    SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
    SummaPoshliny = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаПошлины')
    HarakteristikaNomenklatury = models.ForeignKey('HarakteristikiNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ХарактеристикаНоменклатуры', null=True, blank=True, related_name='KYcjeUDgCmbGsoTS')
    TSena = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Цена')
    ProtsentAvtomaticheskihSkidok = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентАвтоматическихСкидок')
    UslovieAvtomaticheskoySkidki = models.ForeignKey('UsloviyaSkidkiNatsenki', verbose_name='УсловиеАвтоматическойСкидки', null=True, blank=True, related_name='PIFSooIrNCqiidgl')
 
    ZnachenieUsloviyaAvtomaticheskoySkidkiVidyDiskontnyhKart = models.ForeignKey('VidyDiskontnyhKart', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗначениеУсловияАвтоматическойСкидки-ВидыДисконтныхКарт', null=True, blank=True, related_name='SurGWGnsriFjwETi')
    ZnachenieUsloviyaAvtomaticheskoySkidkiInformatsionnyeKarty = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗначениеУсловияАвтоматическойСкидки-ИнформационныеКарты', null=True, blank=True, related_name='ansANFIfPdXTIjSo')
    ZnachenieUsloviyaAvtomaticheskoySkidkiint = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ЗначениеУсловияАвтоматическойСкидки-int')
 
    KlyuchStroki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КлючСтроки')
    SeriyaNomenklatury = models.ForeignKey('SeriiNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СерияНоменклатуры', null=True, blank=True, related_name='cCmkOQdkZksGEiTQ')
    SchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетНаОплатуПоставщика', null=True, blank=True, related_name='uhRIqcAEuGSwUfeg')
    AvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АвансовыйОтчет', null=True, blank=True, related_name='jsGJVFqJgPnslVjT')
    VozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровПоставщику', null=True, blank=True, related_name='HTNKmHxTNwzWoAvU')
    PostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслуг', null=True, blank=True, related_name='CxCPMVbaxAiZtobh')
    OtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='vXLlrPGDhjfJRhgE')
    PostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеДопРасходов', null=True, blank=True, related_name='yckmklADRtdKwbeb')
    InventarizatsiyaTovarovNaSklade = models.ForeignKey('InventarizatsiyaTovarovNaSklade', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнвентаризацияТоваровНаСкладе', null=True, blank=True, related_name='faTAjiyVPWYYZuRc')
    OtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетОРозничныхПродажах', null=True, blank=True, related_name='IAMHBGHbpRJgqFMv')
    VnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВнутреннийЗаказ', null=True, blank=True, related_name='HvnSBPZTUSZelJwi')
    PeremeschenieTovarov = models.ForeignKey('PeremeschenieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПеремещениеТоваров', null=True, blank=True, related_name='mXUyqfDGrtqYCULy')
    PrihodnyyOrderNaTovary = models.ForeignKey('PrihodnyyOrderNaTovary', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПриходныйОрдерНаТовары', null=True, blank=True, related_name='OxFourVDFvPwdWGl')
    VozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='CpkakMFoAFzXxPuY')
    ZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПоставщику', null=True, blank=True, related_name='UvPPEPMbaKpPymqG')
    PostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='ZQYbqBXpGofafste')
    OtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетКомитентуОПродажах', null=True, blank=True, related_name='GDionNEharXBzHNs')
    RealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РеализацияТоваровУслуг', null=True, blank=True, related_name='OYIpsFgJJRYQNqlW')
    SchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетНаОплатуПокупателю', null=True, blank=True, related_name='bjYUKYfCDjHurMsK')
    VozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='mXSvHlgmkypYMXkz')
    RezervirovanieTovarov = models.ForeignKey('RezervirovanieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РезервированиеТоваров', null=True, blank=True, related_name='jaqAFopklLeRcKhH')
    PereotsenkaTovarovPrinyatyhNaKomissiyu = models.ForeignKey('PereotsenkaTovarovPrinyatyhNaKomissiyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПереоценкаТоваровПринятыхНаКомиссию', null=True, blank=True, related_name='iLCFjsVSexxvIspC')
    ZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПокупателя', null=True, blank=True, related_name='brzAdGxPyxIapsAk')
    GTDImport = models.ForeignKey('GTDImport', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ГТДИмпорт', null=True, blank=True, related_name='WCMMiNFybRdVTBlX')
 
    OprihodovanieTovarov = models.ForeignKey('OprihodovanieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОприходованиеТоваров', null=True, blank=True, related_name='dVMiNFyTWCMbRBlX')
    FakturnayaStoimost = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ФактурнаяСтоимость')
    DokumentPartiiVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ВозвратТоваровОтПокупателя', related_name='VffdFzyUjuyiZPej')
    DokumentPartiiPrihodnyyOrderNaTovary = models.ForeignKey('PrihodnyyOrderNaTovary', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ПриходныйОрдерНаТовары', related_name='eWxLhwyHxkzkNbNX')
    DokumentPartiiPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ПоступлениеТоваровУслугВНТТ', related_name='YHHbPoalUILRfIeE')
    DokumentPartiiOprihodovanieTovarov = models.ForeignKey('OprihodovanieTovarov', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ОприходованиеТоваров', related_name='AtgsjjowgxvPeLKk')
    DokumentPartiiPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ПоступлениеТоваровУслуг', related_name='qoEndbmNwyFMTbMD')
    DokumentPartiiOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', blank=True, null=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-ОтчетОРозничныхПродажах', related_name='OuEMYIItbdxGWnoo')
    DokumentPartiiRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', blank=True, null=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-РеализацияТоваровУслуг', related_name='aHlYDZHxXPBpkJfK')
    DokumentPartiiAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', blank=True, null=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПартии-АвансовыйОтчет', related_name='xQlmegnJolZMrZup')

class VozvratnayaTara(models.Model):
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')
	SpisanieTovarov = models.ForeignKey('SpisanieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СписаниеТоваров', null=True, blank=True, related_name='LCoUZTFScLtCAQQa')
	Nomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='YwXWvEcSsrxWxZOi')
	Kolichestvo = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Количество')
	TSena = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Цена')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')

	RazmeschenieZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Размещение-ЗаказПоставщику', null=True, blank=True, related_name='ynhPaqpDYxqsiquI')
	RazmeschenieVnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Размещение-ВнутреннийЗаказ', null=True, blank=True, related_name='iXkZfZAoNruciuUv')
	RazmeschenieSklady = models.ForeignKey('Sklady', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Размещение-Склады', null=True, blank=True, related_name='pSyWjzQHTfqLzIzl')

	SchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетНаОплатуПоставщика', null=True, blank=True, related_name='ZKsbamvkOVEuoAeN')
	AvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АвансовыйОтчет', null=True, blank=True, related_name='JzwVSNdUrNBxIzqC')
	KorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='CoMuIlueXwQXafbd')
	VozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровПоставщику', null=True, blank=True, related_name='WRZSPHCGXhGgkhTS')
	PostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслуг', null=True, blank=True, related_name='kTOAyawpFdzdkcbu')
	VnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВнутреннийЗаказ', null=True, blank=True, related_name='JvOBfRXgckboNrhu')
	PeremeschenieTovarov = models.ForeignKey('PeremeschenieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПеремещениеТоваров', null=True, blank=True, related_name='zkzXMxJPjxGkMPsk')
	PrihodnyyOrderNaTovary = models.ForeignKey('PrihodnyyOrderNaTovary', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПриходныйОрдерНаТовары', null=True, blank=True, related_name='fELPMlHIUkAtmeVe')
	VozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='yRTbcxMQSfxZSZmt')
	ZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПоставщику', null=True, blank=True, related_name='HDVbQFhSJSDUweht')
	PostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='acHJwoUJlfSCYAUv')
	RealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РеализацияТоваровУслуг', null=True, blank=True, related_name='oHcABWHIGbgIASNV')
	SchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетНаОплатуПокупателю', null=True, blank=True, related_name='CSLSxDJQCcdRxAXH')
	VozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='KHwucmTgOkzfYzHO')
	RezervirovanieTovarov = models.ForeignKey('RezervirovanieTovarov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РезервированиеТоваров', null=True, blank=True, related_name='yFVUXjgUhlQlGZAh')
	ZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПокупателя', null=True, blank=True, related_name='NnoHPdBBxYmtgKmr')


class Uslugi(models.Model):
	PometkaUdaleniya = models.BooleanField(default=False, verbose_name='ПометкаУдаления')
	Soderzhanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Содержание')
	Kolichestvo = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Количество')
	TSena = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Цена')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='McGauwQJiBJhYSAX')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	Nomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='dlBiqIRGmPQQKnIq')
	ProtsentSkidkiNatsenki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентСкидкиНаценки')
	ProtsentAvtomaticheskihSkidok = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентАвтоматическихСкидок')
	UslovieAvtomaticheskoySkidki = models.ForeignKey('UsloviyaSkidkiNatsenki', verbose_name='УсловиеАвтоматическойСкидки', null=True, blank=True, related_name='kYanJkltQYvOjygX')

	ZnachenieUsloviyaAvtomaticheskoySkidkiVidyDiskontnyhKart = models.ForeignKey('VidyDiskontnyhKart', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗначениеУсловияАвтоматическойСкидки-ВидыДисконтныхКарт', null=True, blank=True, related_name='eIGPytSPlnTxMakr')
	ZnachenieUsloviyaAvtomaticheskoySkidkiInformatsionnyeKarty = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗначениеУсловияАвтоматическойСкидки-ИнформационныеКарты', null=True, blank=True, related_name='SxPetQaZaarXvmXH')
	ZnachenieUsloviyaAvtomaticheskoySkidkiint = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ЗначениеУсловияАвтоматическойСкидки-int')

	SchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетНаОплатуПоставщика', null=True, blank=True, related_name='CkiplRtVhObaAYDE')
	PostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслуг', null=True, blank=True, related_name='djcQqiZkuyyBkvor')
	ZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПоставщику', null=True, blank=True, related_name='CWbGObtRGRKVnALg')
	PostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='XhwSLXswavAqwscp')
	RealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РеализацияТоваровУслуг', null=True, blank=True, related_name='lHULQQmLnXLwmlGY')
	SchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетНаОплатуПокупателю', null=True, blank=True, related_name='VpZLwtavXmSmECfQ')
	ZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПокупателя', null=True, blank=True, related_name='IMVcVMPhLgiSJMyp')
	NomenklaturnayaGruppa = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НоменклатурнаяГруппа', null=True, blank=True, related_name='IMVcfDPhLgiSJMyp')
	StatyaZatrat = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяЗатрат', null=True, blank=True, related_name='CkiplGfVhObaAYDE')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='CkiplAYDEGfVhOba')


class SostavNabora(models.Model):
	CHekKKM = models.ForeignKey('CHekKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЧекККМ', related_name='yrEMfTqJdkxBUzBr') 
	Nomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='jRyRWfeMGiosguMK')
	HarakteristikaNomenklatury = models.ForeignKey('HarakteristikiNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ХарактеристикаНоменклатуры', null=True, blank=True, related_name='BLXBRzWHTnnzHSFu')
	Kolichestvo = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Количество')
	EdinitsaIzmereniya = models.ForeignKey('EdinitsyIzmereniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЕдиницаИзмерения', null=True, blank=True, related_name='uxOErDMGWChmQiul')
	KlyuchStroki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КлючСтроки')
	TSena = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Цена')
	SeriyaNomenklatury = models.ForeignKey('SeriiNomenklatury', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СерияНоменклатуры', null=True, blank=True, related_name='hfuHKKqZKmonuUiI')
	OtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетОРозничныхПродажах', null=True, blank=True, related_name='YHyOXTAyOaHBiHnS')
	VozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='NUJQigBeAVidHdud')
	RealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РеализацияТоваровУслуг', null=True, blank=True, related_name='hwdLLbRYpMtlTMok')
	SchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетНаОплатуПокупателю', null=True, blank=True, related_name='ZEbHhAZySDmqUzoM')
	ZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаказПокупателя', null=True, blank=True, related_name='QWrcxkPGYsiOcStL')


class StoronnieLitsa(models.Model):
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='pUCqXtAagseVFfoH')

	LitsoKontaktnyeLitsa = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Лицо-КонтактныеЛица', null=True, blank=True, related_name='hpcHXeeSsKGzpSML')
	LitsoKontaktnyeLitsaKontragentov = models.ForeignKey('KontaktnyeLitsaKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Лицо-КонтактныеЛицаКонтрагентов', null=True, blank=True, related_name='uyHpZBAmgwlvHlZW')

	UdalitLitso = models.ForeignKey('KontaktnyeLitsa', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьЛицо', null=True, blank=True, related_name='OykYnBYaZNfQcWwb')
	Sobytie = models.ForeignKey('Sobytie', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Событие', null=True, blank=True, related_name='kqWNcPazzbBPJkvO')

class SeriynyeNomera(models.Model):
	CHekKKM = models.ForeignKey('CHekKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЧекККМ', related_name='bTSYlQtDMeJMuwxc')
	KlyuchSvyazi = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КлючСвязи')
	SeriynyyNomer = models.ForeignKey('SeriynyeNomera', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СерийныйНомер', null=True, blank=True, related_name='BEEfsWMIBsxhmddVY')
	AvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АвансовыйОтчет', null=True, blank=True, related_name='tISLubKsqAPiwDmj')
	VozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровПоставщику', null=True, blank=True, related_name='rfgTIxXgirCTXJGR')
	PostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслуг', null=True, blank=True, related_name='qcZOwSXVdWKQskcK')
	OtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='sppqcjRmvfbmAkET')
	OtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетОРозничныхПродажах', null=True, blank=True, related_name='ZVCojsnUxXGwnGML')
	VozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='xaFeLgnInDbLYnAk')
	PostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='lQxuPQKDyrEZFMQN')
	RealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РеализацияТоваровУслуг', null=True, blank=True, related_name='ukgHpdCnaJnrOGWc')
	VozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='cdvVwgZhzlcrQJSu')


class DokumentyRaschetovSKontragentom(models.Model):
	DoRaSKoVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='qVUytXsjCrlwhZlT')
	DoRaSKoVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='fuLvDJtEmAMzIhAw')
	DoRaSKoPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='qdMEFYbUOVuBAcvS')
	DoRaSKoInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='cafxthDyIwakgzgp')
	DoRaSKoPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='jkEFWdZVlIluijSC')
	DoRaSKoPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеДопРасходов', null=True, blank=True, related_name='iyzHAIFCTVnkdIzV')
	DoRaSKoOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='uMhUGptJTrvUCerJ')
	DoRaSKoRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РасходныйКассовыйОрдер', null=True, blank=True, related_name='lPNKwleDmBeZomdw')
	DoRaSKoPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='iTaZLsHYGidRfQfD')
	DoRaSKoAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПереданный', null=True, blank=True, related_name='rgtPtrdRQkawywBK')
	DoRaSKoPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='sFETNtfrCsXGKjhs')
	DoRaSKoOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='VDzdEteasQGZTBXO')
	DoRaSKoInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='pLIZJlFHVtpWAlHF')
	DoRaSKoKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='vvtwXAjpEeteqUMM')
	DoRaSKoPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='lncCgMgGBEmbCIeq')
	DoRaSKoDoRaSKo = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ДокументыРасчетовСКонтрагентом', null=True, blank=True, related_name='DaCtvIeoKmGfSThl')
	DoRaSKoVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщику', null=True, blank=True, related_name='swBDfGOiDzobUaeL')
	DoRaSKoPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='XqFONsSAHZLxZJgJ')
	DoRaSKoOplataOtPokupatelyaPlatezhnoyKartoy = models.ForeignKey('OplataOtPokupatelyaPlatezhnoyKartoy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОплатаОтПокупателяПлатежнойКартой', null=True, blank=True, related_name='cSDbcnfoZmFpQCKz')
	DoRaSKoAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПолученный', null=True, blank=True, related_name='hnRLPUQzvLkrYjfV')
	DoRaSKoPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='omRkLovPxpCMRbPZ')
	DoRaSKoOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='InjptmkbjPqMBEYT')
	DoRaSKoPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='AJJdGLWzUbaVYjry')
	DoRaSKoOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='ietiUzFCloLFYZPz')
	DoRaSKoRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РеализацияТоваровУслуг', null=True, blank=True, related_name='opYPhPlbzSZpKqAB')
	DoRaSKoAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АвансовыйОтчет', null=True, blank=True, related_name='FxoFsihGNQYAabBj')
	DoRaSKoPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='oGaHkUJxiGMGuvfc')
	DoRaSKoKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолга', null=True, blank=True, related_name='JovnyyLYUFrfdOZZ')

	SummaVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаВзаиморасчетов')
	SummaRegl = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаРегл')
	DataOplaty = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаОплаты')
	VozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровПоставщику', null=True, blank=True, related_name='YjWucdBnQEyfETWn')
	PostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслуг', null=True, blank=True, related_name='LOkPCCpKLGNyZDWb')
	OtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='uctWJpQkPGsKZqvJ')
	VozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='iuigdujhEXWEtRRy')
	PostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='VUSoBwoojDyQsmKA')
	OtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетКомитентуОПродажах', null=True, blank=True, related_name='qxVIVBnmmGttSdOY')


class SeriynyeNomeraSostavNabora(models.Model):
	CHekKKM = models.ForeignKey('CHekKKM', null=True, blank=True, limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЧекККМ', related_name='sJltoHwlAPIKrKHB') # переместить в СерийныеНомераСоставНабора
	KlyuchSvyazi = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КлючСвязи')
	SeriynyyNomer = models.ForeignKey('SeriynyeNomera', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СерийныйНомер', null=True, blank=True, related_name='wGjNzHgwgwZPTChQ')
	OtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетОРозничныхПродажах', null=True, blank=True, related_name='GSMghfMuaanRpZfo')
	VozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='cMaEVOFLVTjHHjpk')
	RealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РеализацияТоваровУслуг', null=True, blank=True, related_name='qtrnvpbQFQJITwqL')


class OplataPlatezhnymiKartami(models.Model):
	VidOplaty = models.ForeignKey('VidyOplatCHekaKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВидОплаты', null=True, blank=True, related_name='WEwnhMjntJTdRUmf')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	ProtsentTorgovoyUstupki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентТорговойУступки')
	SummaTorgovoyUstupki = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаТорговойУступки')
	OtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетОРозничныхПродажах', null=True, blank=True, related_name='jspPEmtgaRiUStJj')


class ProdazhaPoDiskontnymKartam(models.Model):
	DiskontnayaKarta = models.ForeignKey('InformatsionnyeKarty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДисконтнаяКарта', null=True, blank=True, related_name='wUgFQoimsHNLVzna')
	VladeletsDiskontnoykarty = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВладелецДисконтнойкарты', null=True, blank=True, related_name='ToINJVbACnBPvbnM')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	OtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетОРозничныхПродажах', null=True, blank=True, related_name='OlkrKHCcYiGYGUIL')


class OplataBankovskimiKreditami(models.Model):
	VidOplaty = models.ForeignKey('VidyOplatCHekaKKM', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ВидОплаты', null=True, blank=True, related_name='djyOcfYWFtYBeEGU')
	BankKreditor = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='БанкКредитор', null=True, blank=True, related_name='mDoMMsPnNJzrJtIh')
	DogovorVzaimoraschetovBankaKreditora = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорВзаиморасчетовБанкаКредитора', null=True, blank=True, related_name='yVFoceelkDBFpoAA')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	ProtsentBankovskoyKomissii = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='ПроцентБанковскойКомиссии')
	SummaBankovskoyKomissii = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаБанковскойКомиссии')
	OtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетОРозничныхПродажах', null=True, blank=True, related_name='yXCsCevJxVkpDgpe')


class RekvizityKontragenta(models.Model):
	Rekvizit = models.CharField(max_length=100, null=True, blank=True, verbose_name='Реквизит')
	Znachenie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Значение')
	Predstavlenie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Представление')
	TipKontragenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='ТипКонтрагента')
	PlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='SMHyfXirRaEheOfb')
	AkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АккредитивПереданный', null=True, blank=True, related_name='RVJCQvbBvxFHNMsI')
	PlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='lfGVftkewOsIyavM')
	InkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='OFpihurGUFxQNlLY')
	PlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='dTwcSQaBBROGUkIK')
	PlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='DvKmXgmstnjouERB')
	AkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АккредитивПолученный', null=True, blank=True, related_name='alWsfsRCXuMVNhBx')
	PlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='MrJuaOTHuZZEHixg')
	InkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='ogkVQIDpihiMmtAB')
	PlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='SChHwwWazBPWpqdf')


class RazmeschenieZayavki(models.Model):
	MestoRazmescheniyaBankovskieScheta = models.ForeignKey('BankovskieScheta', limit_choices_to={'PometkaUdaleniya': False},verbose_name='МестоРазмещения-БанковскиеСчета', null=True, blank=True, related_name='LkXdGlnAGESSbMKv')
	MestoRazmescheniyaPlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='МестоРазмещения-ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='XjzareDQBsRUVvQD')
	MestoRazmescheniyaKassy = models.ForeignKey('Kassy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='МестоРазмещения-Кассы', null=True, blank=True, related_name='SeXBGRmMhRvNDddW')

	SummaPlatezha = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаПлатежа')
	ZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='mfWClAAqwYPWCvyq')


class Zatraty(models.Model):
	NomenklaturnayaGruppa = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НоменклатурнаяГруппа', null=True, blank=True, related_name='ilQVYYUjDAQrpMgX')
	StatyaZatrat = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяЗатрат', null=True, blank=True, related_name='OwXDowCSwxmCgXrr')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	UdalitSummaRegl = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='УдалитьСуммаРегл')
	Zakaz = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Заказ', null=True, blank=True, related_name='qTaYmsVZysRUOgXo')
	ProchieZatraty = models.ForeignKey('ProchieZatraty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПрочиеЗатраты', null=True, blank=True, related_name='AcpscVErfGRCqoug')


class RasshifrovkaPlatezha(models.Model):
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='GQCAvloIKselWpcM')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='fUoJnZUaOmpHTiqk')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='ENHfKzqazegiUkAu')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='TLjOcbToKgBghgjb')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='nunrwJtBHFznKYSG')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='rKHhitQnnQaqdUne')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='dpbdSeoOWdftSWTO')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='ngUOEbIHihLOGszw')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='kPnucjHwFsupXpFP')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='RpVbhlxFRSZTTlsY')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='YXKWucbaXuntINlY')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='PfJMCdCkIZOAKnLD')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='WLJYwoLqlxdRsstZ')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='RUQmZJJFJGjrfebP')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='fFmfOCfgmnsqkBPE')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='rzPQhRFmHnCgXLnx')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='ZPCiWObsOfECkmhA')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='EqmJfSWTaCgooLnR')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='REhKITomMeSmqmpv')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='icFjmwadcziwDIzx')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='HXxChJocrzfxRwhd')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='zGSMnVmbyIYFkaGH')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='wcRsVIPCTwJSnvAb')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='JUHptDyRwBjZHFVO')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='NRLItPUYUXVZKmjM')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='zxDJjdVSvNOcvHsr')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='wLpyODBHoMfTqodv')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='XpHXARnZlcxuHHcb')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='lhmWGNyQHudAVjCu')

	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	SummaPlatezha = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаПлатежа')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	SummaVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаВзаиморасчетов')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='HokfHSdBspKNDrID')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	StatyaDvizheniyaDenezhnyhSredstv = models.ForeignKey('StatiDvizheniyaDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяДвиженияДенежныхСредств', null=True, blank=True, related_name='rDDZTIuCNLxDFLDb')
	DokumentPlanirovaniyaPlatezha = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументПланированияПлатежа', null=True, blank=True, related_name='umfWEqaCcebMcSqH')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='OSLIgrqrafKTuOOn')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='yLZpHvmcEJImGepI')

	KursVzaimoraschetovPlan = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетовПлан')
	SummaPlatezhaPlan = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаПлатежаПлан')

	DoRaSKoVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='PCNSLQWItcuMevlv')
	DoRaSKoVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='LzKKxbVYvddOhCIg')
	DoRaSKoPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='jHMHWxWfUyoevFLD')
	DoRaSKoInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='eqhuWmpMOxwUYnbN')
	DoRaSKoPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='PgqTACXGWDxOCCZv')
	DoRaSKoPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеДопРасходов', null=True, blank=True, related_name='kGvbxPhFxbNeYqOT')
	DoRaSKoOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='lMBVcpQdciXlzAPC')
	DoRaSKoRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РасходныйКассовыйОрдер', null=True, blank=True, related_name='KKHbZHQzmsDUNfxk')
	DoRaSKoPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='NWuhiBlegvboKzPq')
	DoRaSKoAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПереданный', null=True, blank=True, related_name='JZjUnldKEgWByvuU')
	DoRaSKoPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='NspbhxGKchYySYSS')
	DoRaSKoOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='NSbkmIoidufzxhBu')
	DoRaSKoInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='qExnDCbaIdOBDXvc')
	DoRaSKoKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='lavZdbdQtxvNsiQz')
	DoRaSKoPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='hfTEVPSiFvHeskQY')
	DoRaSKoDoRaSKo = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='pbQjrbNzvCugflBi')
	DoRaSKoVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщику', null=True, blank=True, related_name='ANXAzdzFXgNJfDDZ')
	DoRaSKoPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='XTMGDomzfhAIOwOs')
	DoRaSKoAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПолученный', null=True, blank=True, related_name='gkpSOMuhFOlSWwZb')
	DoRaSKoPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='LIIPwaSEUeeiIlec')
	DoRaSKoOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='qntXGMFvYfaiisZX')
	DoRaSKoPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='nFAuStIUGeQrabDO')
	DoRaSKoOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='QKBXnIcjWwZCCNtQ')
	DoRaSKoRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РеализацияТоваровУслуг', null=True, blank=True, related_name='DAhLSoZnBscvXyqI')
	DoRaSKoAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АвансовыйОтчет', null=True, blank=True, related_name='gTEjzZgiJwRbohBf')
	DoRaSKoPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='VuSspMOSyDMXGHbD')
	DoRaSKoKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолга', null=True, blank=True, related_name='KOOWZRcLizsdhsvn')

	ZayavkaNaRashodovanieSredstv = models.ForeignKey('ZayavkaNaRashodovanieSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ЗаявкаНаРасходованиеСредств', null=True, blank=True, related_name='uLPZqyfcUVIozVSf')
	InkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='RnJXNgrVrobIYePb')
	PlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='lFiZMDNQJCRLhzOb')
	PlaniruemoePostuplenieDenezhnyhSredstv = models.ForeignKey('PlaniruemoePostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПланируемоеПоступлениеДенежныхСредств', null=True, blank=True, related_name='IDgBKJuReONWvJhv')
	PrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПриходныйКассовыйОрдер', null=True, blank=True, related_name='veYtYSuTnWKoESOt')
	PlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='LHeBrJmaWZhBdRRa')
	AkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АккредитивПереданный', null=True, blank=True, related_name='qXKllTpglvPcnIsw')
	PlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='AxJhqWqAvjZopuVC')
	InkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='ybAgXQNDkBqOkoRo')
	RashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='РасходныйКассовыйОрдер', null=True, blank=True, related_name='SDUTHeGwhtyRzQLA')
	PlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='GWbNUNZsvrmFmlMZ')
	PlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='RmEOinmFhYXKtvYX')
	AkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АккредитивПолученный', null=True, blank=True, related_name='ZCPXMiHvgXDPzFty')
	PlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='LteLsEItxqQELfTS')


class Prochee(models.Model):
	VidDokVhodyaschiy = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидДокВходящий')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	Postavschik = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Поставщик', null=True, blank=True, related_name='JMojXwxGJrVaDPhI')
	SchetFaktura = models.ForeignKey('SchetFakturaPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СчетФактура', null=True, blank=True, related_name='EIAGnWcAQBfsLyEV')
	Nomenklatura = models.ForeignKey('Nomenklatura', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Номенклатура', null=True, blank=True, related_name='eYoCWPpgdIzUsLvD')
	Soderzhanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Содержание')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='tjpiChShylpPatji')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')

	ZakazZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Заказ-ЗаказПокупателя', null=True, blank=True, related_name='VQRBPVHUpGfYejNi')
	ZakazVnutrenniyZakaz = models.ForeignKey('VnutrenniyZakaz', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Заказ-ВнутреннийЗаказ', null=True, blank=True, related_name='spainYiyPordgror')

	NomenklaturnayaGruppa = models.ForeignKey('NomenklaturnyeGruppy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='НоменклатурнаяГруппа', null=True, blank=True, related_name='KxggPQrVnxrPBkBR')
	Podrazdelenie = models.ForeignKey('Podrazdeleniya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Подразделение', null=True, blank=True, related_name='NVUFhBCqRBDTZNsT')
	StatyaZatrat = models.ForeignKey('StatiZatrat', limit_choices_to={'PometkaUdaleniya': False},verbose_name='СтатьяЗатрат', null=True, blank=True, related_name='VzLmrpWwOwODBJGQ')

	UdalitProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьПроект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='gsTyHXJLtTYaPgbG')
	UdalitProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='УдалитьПроект-Проекты', null=True, blank=True, related_name='qiaobRcShWqJjAjr')

	PredyavlenSF = models.BooleanField(default=False, verbose_name='ПредъявленСФ')
	DataSF = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name='ДатаСФ')
	NomerSF = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерСФ')
	AvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АвансовыйОтчет', null=True, blank=True, related_name='GqVSAavjzNvUItMg')


class OplataPostavschikam(models.Model):
	VidDokVhodyaschiy = models.CharField(max_length=100, null=True, blank=True, verbose_name='ВидДокВходящий')
	DataVhodyaschegoDokumenta = models.DateField(auto_now=False, auto_now_add=False, verbose_name='ДатаВходящегоДокумента')
	NomerVhodyaschegoDokumenta = models.CharField(max_length=100, null=True, blank=True, verbose_name='НомерВходящегоДокумента')
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	Kontragent = models.ForeignKey('Kontragenty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Контрагент', null=True, blank=True, related_name='XFXfIQJXtlAliScm')
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='ystWAlhrwifGNqOU')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='tmesVygsGumzepTr')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='AsjIEEwMtTqIeAwx')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='MVHEOLpcwXnZzjrY')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='GrgmLlpxgklmMIPz')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='lCTxrdudZnjVOGFz')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='FFwrPWUWGVvMNOjg')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='vjIrQgBtbKOBtfme')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='KsNYznjQwwyhLScg')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='WharHmWshjsnudRs')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='sJxlEEcfBBtcjibo')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='ZqOYKZvvxHTGVzeZ')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='QQgDZemQvJdnipgU')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='LkfTVEmUihdQgeaO')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='hhyBqapsxZONlKyU')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='HcqnFqVBWBKWtkkG')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='HPBLssAmsDhxyApM')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='ymxnhGVOkqmDFvoY')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='AAMVtREVTEtDOOrN')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='LZoDyNGMOfiybmvP')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='XHgyFXxOGUqLjyBT')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='vgKtAgzFTYsSBwsO')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='iSnQJBuMolcnovWX')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='WrEmaaioazhYFQKm')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='qUpbjdAvEcQMyvXD')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='kcpciEkpUaQgSMft')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='edHoKeEkjDXzqeDS')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='ubIBECbpFgXOxSTD')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='RqgxCyhGpakebdyQ')

	Soderzhanie = models.CharField(max_length=100, null=True, blank=True, verbose_name='Содержание')
	SummaVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаВзаиморасчетов')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')

	DoRaSKoVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='KURMNAhaqzgWrsuq')
	DoRaSKoVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='CuVpwPNhzlwrGtor')
	DoRaSKoPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='NAerhFbvlCRJAJIJ')
	DoRaSKoInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='phLmEZEDBZSwUNNn')
	DoRaSKoPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='FqLzgSmKIfRARRhe')
	DoRaSKoPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеДопРасходов', null=True, blank=True, related_name='TbPSINXoBwPKqPhv')
	DoRaSKoOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='tDotoUVZGmybXqXe')
	DoRaSKoRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РасходныйКассовыйОрдер', null=True, blank=True, related_name='EKsCbIpNpkatuFmM')
	DoRaSKoPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='svXxyFDXYPhsNiKL')
	DoRaSKoAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПереданный', null=True, blank=True, related_name='WkggsgEntnCYZACe')
	DoRaSKoPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='LXJFrBbLFcZNxldV')
	DoRaSKoOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='iGVzrsGuvugqZOfF')
	DoRaSKoInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='xXWskSPtkmBGkHvw')
	DoRaSKoKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='QFuclVqPNohLWVlu')
	DoRaSKoPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='aKVeZLMFpQEsDnBZ')
	DoRaSKoDoRaSKo = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='wGfXbpcAfTcgmGTj')
	DoRaSKoVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщику', null=True, blank=True, related_name='GbSERaVFkowYarQA')
	DoRaSKoPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='DgdBpkFRTQFnCFNH')
	DoRaSKoAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПолученный', null=True, blank=True, related_name='cGjEbvNLXKgiXKIR')
	DoRaSKoPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='ojMkgLDJDpQyeraf')
	DoRaSKoOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='ZtVPhChldQRdpozZ')
	DoRaSKoPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='kxqlTKuNeLfVUVnr')
	DoRaSKoOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='SVnjmgEcobEaySCZ')
	DoRaSKoRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РеализацияТоваровУслуг', null=True, blank=True, related_name='BqvEIurGyyuuxbJi')
	DoRaSKoAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АвансовыйОтчет', null=True, blank=True, related_name='RVQxJSIPxoWNIoWV')
	DoRaSKoPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='LDejKrGfxPLxpCfg')
	DoRaSKoKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолга', null=True, blank=True, related_name='zZrIbcIDfmUsjDGT')

	ProektVidyRaspredeleniyaPoProektam = models.ForeignKey('VidyRaspredeleniyaPoProektam', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-ВидыРаспределенияПоПроектам', null=True, blank=True, related_name='fHUMEtWfqzfGcFTf')
	ProektProekty = models.ForeignKey('Proekty', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Проект-Проекты', null=True, blank=True, related_name='TtoiHNfNKectMbNj')

	AvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АвансовыйОтчет', null=True, blank=True, related_name='EtzkTATWobxorklj')


class VydannyeAvansy(models.Model):
	DokumentAvansaPoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументАванса-ПоручениеИсходящее', null=True, blank=True, related_name='yZLXbKiztUYsAXpB')
	DokumentAvansaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументАванса-РасходныйКассовыйОрдер', null=True, blank=True, related_name='oTdiVevUBugTxcXx')
	DokumentAvansaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументАванса-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='vRqEAEVYLeDZftXf')

	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	AvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='АвансовыйОтчет', null=True, blank=True, related_name='deRcBdRuVsspSFeT')


class DenezhnyeSredstva(models.Model):
	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	StavkaNDS = models.ForeignKey('StavkiNDS', verbose_name='СтавкаНДС', null=True, blank=True, related_name='PZdDZLeIEuqkziay')
	SummaNDS = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНДС')
	VidOtchetaPoPlatezham = models.ForeignKey('VidyOtvetovPoPlatezhamKomissiya', verbose_name='ВидОтчетаПоПлатежам', null=True, blank=True, related_name='dSXVNQmQKRzRfLbv')
	OtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='XEeIVusGeJhQeODB')
	OtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ОтчетКомитентуОПродажах', null=True, blank=True, related_name='LNsLijbftGOFMgra')


class SummyDolga(models.Model):
	DogovorKontragenta = models.ForeignKey('DogovoryKontragentov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДоговорКонтрагента', null=True, blank=True, related_name='KalRWJkOGFcJfLvk')

	SdelkaVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='kvmonesAGGvdgBDn')
	SdelkaVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='AizSLktzEVTgAwlY')
	SdelkaZakazPokupatelya = models.ForeignKey('ZakazPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПокупателя', null=True, blank=True, related_name='iNOmakQfKbKIDVgK')
	SdelkaPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='eJMBlxltKRdsVClk')
	SdelkaInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='HkZOmiiunniDkMGn')
	SdelkaPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='KdlncSknDBsfrFwQ')
	SdelkaPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеДопРасходов', null=True, blank=True, related_name='RKhDDuwGUItLemdi')
	SdelkaRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РасходныйКассовыйОрдер', null=True, blank=True, related_name='ZkKWoufUkLtuJRJt')
	SdelkaPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='fkVyUuXiObRFTfHM')
	SdelkaZakazPostavschiku = models.ForeignKey('ZakazPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ЗаказПоставщику', null=True, blank=True, related_name='ltdWAfUyUvilMwKH')
	SdelkaAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПереданный', null=True, blank=True, related_name='dVUsMCJBzCtnvmOT')
	SdelkaPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='WEdBKBQUgWLmmUyb')
	SdelkaOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='zmkJGRmvLTrnWLUw')
	SdelkaInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='NbcICrHcLPRnEBFW')
	SdelkaKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='wPfUiiMaiRYzTUNN')
	SdelkaPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='XBqFUIkzvIWPSIIy')
	SdelkaVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ВозвратТоваровПоставщику', null=True, blank=True, related_name='XJTpoZNgvsRmFKqO')
	SdelkaPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='SfhUmsWGhHPgLxJz')
	SdelkaAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АккредитивПолученный', null=True, blank=True, related_name='hIAILSlrQZiGTmga')
	SdelkaPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='DSaoNezhWVTdisen')
	SdelkaPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='mAPwAmDaCzWdpRMN')
	SdelkaOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='QHbCbvJrCPJRazlX')
	SdelkaRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-РеализацияТоваровУслуг', null=True, blank=True, related_name='BZrFkyPWWSRTEioT')
	SdelkaAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-АвансовыйОтчет', null=True, blank=True, related_name='pjtgejyzcjowzhFY')
	SdelkaSchetNaOplatuPostavschika = models.ForeignKey('SchetNaOplatuPostavschika', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПоставщика', null=True, blank=True, related_name='NQeBlFaixrAWeJAG')
	SdelkaPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='KbkkZquYMVpaNRnG')
	SdelkaSchetNaOplatuPokupatelyu = models.ForeignKey('SchetNaOplatuPokupatelyu', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-СчетНаОплатуПокупателю', null=True, blank=True, related_name='xywNTgXaLDECWsca')
	SdelkaKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='Сделка-КорректировкаДолга', null=True, blank=True, related_name='CNDSFpItXCKpLVen')

	Summa = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='Сумма')
	UdalitUmenshenieDolgaKontragenta = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='УдалитьУменьшениеДолгаКонтрагента')
	KursVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КурсВзаиморасчетов')
	KratnostVzaimoraschetov = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='КратностьВзаиморасчетов')
	VidZadolzhennosti = models.ForeignKey('VidyZadolzhennosti', verbose_name='ВидЗадолженности', null=True, blank=True, related_name='cyucpJgkejTjsIQs')

	DoRaSKoVozvratTovarovPostavschikuIzNTT = models.ForeignKey('VozvratTovarovPostavschikuIzNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщикуИзНТТ', null=True, blank=True, related_name='WsFlmtXiAbHHvngQ')
	DoRaSKoVozvratTovarovOtPokupatelya = models.ForeignKey('VozvratTovarovOtPokupatelya', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровОтПокупателя', null=True, blank=True, related_name='bZgRipziFYOdjOBa')
	DoRaSKoPrihodnyyKassovyyOrder = models.ForeignKey('PrihodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПриходныйКассовыйОрдер', null=True, blank=True, related_name='hDehUwWwgNzBXhZg')
	DoRaSKoInkassovoePorucheniePoluchennoe = models.ForeignKey('InkassovoePorucheniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПолученное', null=True, blank=True, related_name='sZjmqjBoRTrbAXsq')
	DoRaSKoPlatezhnoePoruchenieIshodyaschee = models.ForeignKey('PlatezhnoePoruchenieIshodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеИсходящее', null=True, blank=True, related_name='LvGiSJtywsqEppJk')
	DoRaSKoPostuplenieDopRashodov = models.ForeignKey('PostuplenieDopRashodov', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеДопРасходов', null=True, blank=True, related_name='QCTlgZDmTFLasWTl')
	DoRaSKoOtrazhenieRealizatsiiTovarovIUslugNDS = models.ForeignKey('OtrazhenieRealizatsiiTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеРеализацииТоваровИУслугНДС', null=True, blank=True, related_name='zdgkBgMMdGPtziTf')
	DoRaSKoRashodnyyKassovyyOrder = models.ForeignKey('RashodnyyKassovyyOrder', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РасходныйКассовыйОрдер', null=True, blank=True, related_name='RcyhwpLDBiNyAQqJ')
	DoRaSKoPlatezhnoeTrebovanieVystavlennoe = models.ForeignKey('PlatezhnoeTrebovanieVystavlennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеВыставленное', null=True, blank=True, related_name='psHJTDEoDliWSGsB')
	DoRaSKoAkkreditivPeredannyy = models.ForeignKey('AkkreditivPeredannyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПереданный', null=True, blank=True, related_name='nvVKVTSuASqQewSv')
	DoRaSKoPostuplenieTovarovUslugVNTT = models.ForeignKey('PostuplenieTovarovUslugVNTT', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслугВНТТ', null=True, blank=True, related_name='uXuWfZcbJmsQVIMv')
	DoRaSKoOtchetKomitentuOProdazhah = models.ForeignKey('OtchetKomitentuOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомитентуОПродажах', null=True, blank=True, related_name='vJqRuvSHrHtfJatD')
	DoRaSKoInkassovoePorucheniePeredannoe = models.ForeignKey('InkassovoePorucheniePeredannoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ИнкассовоеПоручениеПереданное', null=True, blank=True, related_name='gUFUWqqHLUYwTnom')
	DoRaSKoKorrektirovkaDolgaPoVozvratnoyTare = models.ForeignKey('KorrektirovkaDolgaPoVozvratnoyTare', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолгаПоВозвратнойТаре', null=True, blank=True, related_name='SgCzTQvuWUkfLzcr')
	DoRaSKoPlatezhnyyOrderSpisanieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderSpisanieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерСписаниеДенежныхСредств', null=True, blank=True, related_name='WFVFvHahrbOWAmMb')
	DoRaSKoDoRaSKo = models.ForeignKey('DokumentRaschetovSKontragentom', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ДокументРасчетовСКонтрагентом', null=True, blank=True, related_name='UdJFSNHFFnmhzViC')
	DoRaSKoVozvratTovarovPostavschiku = models.ForeignKey('VozvratTovarovPostavschiku', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ВозвратТоваровПоставщику', null=True, blank=True, related_name='bBsjDVTIKSSfaYVV')
	DoRaSKoPlatezhnoePoruchenieVhodyaschee = models.ForeignKey('PlatezhnoePoruchenieVhodyaschee', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеПоручениеВходящее', null=True, blank=True, related_name='tGAltdoBOJRmbsFq')
	DoRaSKoOplataOtPokupatelyaPlatezhnoyKartoy = models.ForeignKey('OplataOtPokupatelyaPlatezhnoyKartoy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОплатаОтПокупателяПлатежнойКартой', null=True, blank=True, related_name='TZvJcusavnVjxypf')
	DoRaSKoAkkreditivPoluchennyy = models.ForeignKey('AkkreditivPoluchennyy', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АккредитивПолученный', null=True, blank=True, related_name='wWBnobXOIKimVgAI')
	DoRaSKoPostuplenieTovarovUslug = models.ForeignKey('PostuplenieTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПоступлениеТоваровУслуг', null=True, blank=True, related_name='HJWdCATJCbnAqsOK')
	DoRaSKoOtrazheniePostupleniyaTovarovIUslugNDS = models.ForeignKey('OtrazheniePostupleniyaTovarovIUslugNDS', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтражениеПоступленияТоваровИУслугНДС', null=True, blank=True, related_name='xkBaDWptPHDPBzpw')
	DoRaSKoOtchetORoznichnyhProdazhah = models.ForeignKey('OtchetORoznichnyhProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетОРозничныхПродажах', null=True, blank=True, related_name='mMevoMffrWBMedCw')
	DoRaSKoPlatezhnoeTrebovaniePoluchennoe = models.ForeignKey('PlatezhnoeTrebovaniePoluchennoe', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежноеТребованиеПолученное', null=True, blank=True, related_name='LODHcNPLKgTlkxLx')
	DoRaSKoOtchetKomissioneraOProdazhah = models.ForeignKey('OtchetKomissioneraOProdazhah', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ОтчетКомиссионераОПродажах', null=True, blank=True, related_name='ixvzwSPZodaXMNFP')
	DoRaSKoRealizatsiyaTovarovUslug = models.ForeignKey('RealizatsiyaTovarovUslug', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-РеализацияТоваровУслуг', null=True, blank=True, related_name='mjUFgryAJAiOWqKD')
	DoRaSKoAvansovyyOtchet = models.ForeignKey('AvansovyyOtchet', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-АвансовыйОтчет', null=True, blank=True, related_name='dlHPaQcZimVSrZTN')
	DoRaSKoPlatezhnyyOrderPostuplenieDenezhnyhSredstv = models.ForeignKey('PlatezhnyyOrderPostuplenieDenezhnyhSredstv', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-ПлатежныйОрдерПоступлениеДенежныхСредств', null=True, blank=True, related_name='mxvntZpayAxYzRvJ')
	DoRaSKoKorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='ДокументРасчетовСКонтрагентом-КорректировкаДолга', null=True, blank=True, related_name='LQKBDZbrquSlaNSM')

	SummaRegl = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаРегл')
	SummaNU = models.DecimalField(max_digits=15, decimal_places=4, null=True, blank=True, verbose_name='СуммаНУ')
	KorrektirovkaDolga = models.ForeignKey('KorrektirovkaDolga', limit_choices_to={'PometkaUdaleniya': False},verbose_name='КорректировкаДолга', null=True, blank=True, related_name='IlxmLyoHBVuFqORS')