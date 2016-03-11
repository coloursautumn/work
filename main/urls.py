from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
#Авторизация регистрация
	url(r'^login/', 'main.views.login'),
	url(r'^logout/', 'main.views.logout'),
	url(r'^register/', 'main.views.register'),
# Общие
	url(r'^$', 'main.views.menu'),
	url(r'^viborSpr/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.viborSpr'),
	url(r'^viborDoc/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.viborDoc'),
	url(r'^saveTsenyNomenklatury/$', 'main.views.saveTsenyNomenklatury'),
    url(r'^saveSubobj/$', 'main.views.saveSubobj'),
    url(r'^test/$', 'main.views.test'),
    url(r'^deleteObj/$', 'main.views.deleteObj'),
    url(r'^saveObj/$', 'main.views.saveObj'),

	url(r'^getIdDocKontragentaDima/$', 'main.views.getIdDocKontragentaDima'),
	url(r'^getIdKontragentDima/$', 'main.views.getIdKontragentDima'),
	url(r'^getSdelkaDlyaKontragenta/$', 'main.views.getSdelkaDlyaKontragenta'),
	url(r'^getDateOfBirthKontLitsa/$', 'main.views.getDateOfBirthKontLitsa'),
	url(r'^getContactsDlyaKontragenta/$', 'main.views.getContactsDlyaKontragenta'),

	url(r'^getIdDocKontragentaPostavshika/$', 'main.views.getIdDocKontragentaPostavshika'),
	url(r'^getIdKontragentPostavshika/$', 'main.views.getIdKontragentPostavshika'),
	url(r'^getSdelkaDlyaPostavshika/$', 'main.views.getSdelkaDlyaPostavshika'),

	url(r'^newEdinitsuForNomenklatura/$', 'main.views.newEdinitsuForNomenklatura'),
	url(r'^delEdinitsuIzmereniya/$', 'main.views.delEdinitsuIzmereniya'),

	url(r'^getTovarOptions/$', 'main.views.getTovarOptions'),
	url(r'^getTovarOptionsSTipTSen/$', 'main.views.getTovarOptionsSTipTSen'),

	url(r'^sysDoc/getSummaDocumentaForSchetaFactury/$', 'main.views.getSummaDocumentaForSchetaFactury'),#Для Счет-фактура:полученный
    url(r'^sysDoc/getSummaDocumentaForSchetaFacturyVidanniyRTU/$', 'main.views.getSummaDocumentaForSchetaFacturyVidanniyRTU'),#Для Счет-фактура:выданный
    url(r'^sysDoc/getSummaDocumentaForSchetaFacturyVidanniyVTP/$', 'main.views.getSummaDocumentaForSchetaFacturyVidanniyVTP'),#Для Счет-фактура:выданный
	
	
#Справочники
	# Сложные
	url(r'^InventarizatsiyaTovarovNaSklade/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.InventarizatsiyaTovarovNaSkladeViews'),
	url(r'^DogovoryEkvayringa/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.dogovoryekvayringa'),
	url(r'^Valyuty/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.Valyuty'),
	url(r'^Kontragenty/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.kontragenty'),
	url(r'^NomeraGTD/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.NomeraGTD'),
	url(r'^Nomenklatura/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.Nomenklatura'),
	url(r'^Banki/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.Banki'),
	url(r'^KlassifikatorEdinitsIzmereniya/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.KlassifikatorEdinitsIzmereniya'),
	# Простые
	url(r'^FizicheskieLitsa/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^TipyTSenNomenklatury/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^Sklady/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^Podrazdeleniya/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^Nomenklatura/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^VidyNomenklatury/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^StatiZatrat/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^TipyTSenNomenklaturyKontragentov/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^KlassifikatorOKOPF/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^Regiony/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^KontaktnyeLitsaKontragentov/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^KontaktnyeLitsa/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^GruppySobytiy/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^VidyKontaktnoiInformatsii/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^EdinitsyIzmereniya/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^Organizatsii/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.Organizatsii'),
	url(r'^BankovskieScheta/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^DogovoryKontragentov/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^Kassy/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^KassyKKM/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),
	url(r'^VidyOplatCHekaKKM/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.spr'),

# Документы
	url(r'^UstanovkaTSenNomenklatury/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.UstanovkaTSenNomenklatury'),

    url(r'^VozvratTovarovOtPokupatelya/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.vozvrattovarovotpokupatelya'),
    url(r'^Doverennosti/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.Doverennosti'),
    url(r'^OtchetORoznichnyhProdazhah/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.OtchetORoznichnyhProdazhah'),
    url(r'^CHekKKM/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.CHekKKMViews'),
    url(r'^GTDImport/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.GTDImportViews'),
    url(r'^PostuplenieDopRashodov/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.PostuplenieDopRashodovViews'),
    url(r'^SchetFakturaPoluchennyy/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.SchetFakturaPoluchennyyViews'),
    url(r'^VozvratTovarovPostavschiku/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.VozvratTovarovPostavschikuViews'),
    url(r'^PostuplenieTovarovUslug/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.PostuplenieTovarovUslugViews'),
    url(r'^ZakazPokupatelya/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.ZakazPokupatelyaViews'),
    url(r'^ZakazPostavschiku/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.ZakazPostavschikuViews'),
    url(r'^SchetFakturaVydannyy/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.SchetFakturaVydannyyViews'),
	url(r'^RealizatsiyaTovarovUslug/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.RealizatsiyaTovarovUslugViews'),
    url(r'^SchetNaOplatuPokupatelyu/(?P<alias>[-a-zA-Z0-9_]+)/$', 'main.views.SchetNaOplatuPokupatelyuViews'),
    # Системные
    url(r'^sysDoc/getValutaForGTDImport/$', 'main.views.getValutaForGtd'),#Для GTDImport
    url(r'^sysDoc/getIdDocKontragenta/$', 'main.views.getIdDocKontragenta'),#Для ZakazPokupatelya

]
