from django.shortcuts import render_to_response, render, get_object_or_404, redirect 
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseForbidden 
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from main import models
from main import forms
import json
import importlib

from django.core import serializers
import logging
logger = logging.getLogger(__name__) # Подключаем логгер для отладки кода


#Авторизация регистрация 

def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username , password=password)
		if user is not None:
			auth.login(request , user)
			return redirect('/')
		else:
			args['login_error'] = 'Пользователь не найден'
			return render_to_response('login.html' , args)
	else:
		return render_to_response('login.html' , args)

def logout (request):
	auth.logout(request)
	return redirect('/')

def register(request):
	args = {}
	args.update(csrf(request))
	args[form] = UserCreationForm() 
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid:
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'] , password=newuser_form.cleaned_data['password2'])
			auth.login(request , newuser)
			return redirect('/')
		else:
			args['form'] = newuser_form 
	else:
		return render_to_response('register.html' , args)

# Навигация
def menu(request):
	if request.user.is_authenticated():
		username = auth.get_user(request).username
		return HttpResponse(render_to_string('menu.html', locals()))
	else:
		return HttpResponseRedirect('/login/')

# Простые справочники
@csrf_exempt
def spr(request, alias):
	if request.user.is_authenticated():
		name_obj = request.path.split('/')[1]
		model_class = getattr(models, name_obj)
		if alias!='new': # Проверяем новый или не новый
			try:
				verb_name = model_class._meta.verbose_name
				obj = model_class.objects.get(Kod=alias) # Получаем объект по токену
				objForm = getattr(forms, name_obj + 'Form')
				form = objForm(instance=obj) # Создаем форму на основе существующего объекта
				return HttpResponse(render_to_string('Spr.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  model_class()
			obj.save()
			obj.Kod = 'DL'+str(obj.id)
			obj.save()
			return HttpResponseRedirect('/'+name_obj+'/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')

# Сложные справочники
@csrf_exempt
def Organizatsii(request, alias):
	if request.user.is_authenticated():
		formOtvetstvennyeLitsaOrganizatsii = forms.OtvetstvennyeLitsaOrganizatsiiForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.Organizatsii.objects.get(Kod=alias) # Получаем объект по токену
				verb_name = models.Organizatsii._meta.verbose_name
				litsa = models.OtvetstvennyeLitsaOrganizatsii.objects.filter(Organizatsii=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				formOrganizatsii = forms.OrganizatsiiForm(instance=obj) # Создаем форму на основе существующего объекта
				mylitsa = []
				for litso in litsa:
					mylitsa.append(forms.OtvetstvennyeLitsaOrganizatsiiForm(instance=litso))

				return HttpResponse(render_to_string('Organizatsii.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.Organizatsii()
			obj.save()
			obj.Kod = str(obj.id)
			obj.save()
			return HttpResponseRedirect('/Organizatsii/'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')

@csrf_exempt
def Valyuty(request, alias):
	if request.user.is_authenticated():
		formKursyValyut = forms.KursyValyutForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.Valyuty.objects.get(Kod=alias) # Получаем объект по токену
				verb_name = models.Valyuty._meta.verbose_name
				kursy = models.KursyValyut.objects.filter(Valyuty=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				formValyuty = forms.ValyutyForm(instance=obj) # Создаем форму на основе существующего объекта
				mykursy = []
				for kurs in kursy:
					mykursy.append(forms.KursyValyutForm(instance=kurs))

				return HttpResponse(render_to_string('Valyuty.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.Valyuty()
			obj.save()
			obj.Kod = str(obj.id)
			obj.save()
			return HttpResponseRedirect('/Valyuty/'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')

		
@csrf_exempt
def Valyuty(request, alias):
	if request.user.is_authenticated():
		formKursyValyut = forms.KursyValyutForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.Valyuty.objects.get(id=alias) # Получаем объект по токену
				verb_name = models.Valyuty._meta.verbose_name
				kursy = models.KursyValyut.objects.filter(Valyuty=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				formValyuty = forms.ValyutyForm(instance=obj) # Создаем форму на основе существующего объекта
				mykursy = []
				for kurs in kursy:
					mykursy.append(forms.KursyValyutForm(instance=kurs))

				return HttpResponse(render_to_string('Valyuty.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.Valyuty()
			obj.save()
			obj.Kod = str(obj.id)
			obj.save()
			return HttpResponseRedirect('/Valyuty/'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		
@csrf_exempt
def dogovoryekvayringa(request, alias):
	if request.user.is_authenticated():
		formTarifyZaRaschetnoeObsluzhivanie = forms.TarifyZaRaschetnoeObsluzhivanieForm()
		if alias!='new': # Проверяем новый или не новый
			obj = models.DogovoryEkvayringa.objects.get(Kod=alias) # Получаем объект по токену
			verb_name = models.DogovoryEkvayringa._meta.verbose_name
			tarify = models.TarifyZaRaschetnoeObsluzhivanie.objects.filter(DogovoryEkvayringa=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
			formDogovoryEkvayringa = forms.DogovoryEkvayringaForm(instance=obj) # Создаем форму на основе существующего объекта
			mytarify = []
			for tarif in tarify:
				mytarify.append(forms.TarifyZaRaschetnoeObsluzhivanieForm(instance=tarif))

			return HttpResponse(render_to_string('dogovoryekvayringa.html', locals()))

		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.DogovoryEkvayringa()
			obj.save()
			obj.Kod = 'DL'+str(obj.id)
			obj.save()
			return HttpResponseRedirect('/DogovoryEkvayringa/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		
@csrf_exempt
def NomeraGTD(request, alias):
	if request.user.is_authenticated():
		if alias!='new': # Проверяем новый или не новый
			try:
				verb_name = models.NomeraGTD._meta.verbose_name
				obj = models.NomeraGTD.objects.get(id=alias) # Получаем объект по токену
				form = forms.NomeraGTDForm(instance=obj) # Создаем форму на основе существующего объекта
				return HttpResponse(render_to_string('NomeraGTD.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.NomeraGTD()
			obj.save()
			return HttpResponseRedirect('/NomeraGTD/'+str(obj.id)+'/')
		return HttpResponse(render_to_string('NomeraGTD.html', locals()))
	else:
		return HttpResponseRedirect('/login/')
		
def Banki(request, alias):
	if request.user.is_authenticated():
		if alias!='new': # Проверяем новый или не новый
			try:
				verb_name = models.Banki._meta.verbose_name
				obj = models.Banki.objects.get(id=alias) # Получаем объект по токену
				form = forms.BankiForm(instance=obj) # Создаем форму на основе существующего объекта
				return HttpResponse(render_to_string('Banki.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.Banki()
			obj.save()
			return HttpResponseRedirect('/Banki/'+str(obj.id)+'/')
		return HttpResponse(render_to_string('Banki.html', locals()))
	else:
		return HttpResponseRedirect('/login/')
		
def KlassifikatorEdinitsIzmereniya(request, alias):
	if request.user.is_authenticated():
		if alias!='new': # Проверяем новый или не новый
			try:
				verb_name = models.KlassifikatorEdinitsIzmereniya._meta.verbose_name
				obj = models.KlassifikatorEdinitsIzmereniya.objects.get(id=alias) # Получаем объект по токену
				form = forms.KlassifikatorEdinitsIzmereniyaForm(instance=obj) # Создаем форму на основе существующего объекта
				return HttpResponse(render_to_string('KlassifikatorEdinitsIzmereniya.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.KlassifikatorEdinitsIzmereniya()
			obj.save()
			return HttpResponseRedirect('/KlassifikatorEdinitsIzmereniya/'+str(obj.id)+'/')
		return HttpResponse(render_to_string('KlassifikatorEdinitsIzmereniya.html', locals()))
	else:
		return HttpResponseRedirect('/login/')
		
@csrf_exempt
def Nomenklatura(request, alias):
	if request.user.is_authenticated():
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.Nomenklatura.objects.get(Kod=alias) # Получаем объект по токену
				verb_name = models.Nomenklatura._meta.verbose_name
				edinitsy = models.EdinitsyIzmereniya.objects.filter(Vladelets=obj, PometkaUdaleniya=False)
				tipy = models.TipyTSenNomenklatury.objects.filter(PometkaUdaleniya=False)
				form = forms.NomenklaturaForm(instance=obj) # Создаем форму на основе существующего объекта
				formTovaryIUslugi = forms.TovaryIUslugiForm()
				formTipyTsen = forms.TipyTsenForm()

				mytipy = []
				for tip in tipy:
					mytipy.append(forms.TipyTSenNomenklaturyForm(instance=tip))
				

				return HttpResponse(render_to_string('Nomenklatura.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.Nomenklatura()
			obj.save()
			obj.Kod = 'DL'+str(obj.id)
			obj.save()
			return HttpResponseRedirect('/Nomenklatura/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def kontragenty(request, alias):
	if request.user.is_authenticated():
		formVidyDeyatelnosti = forms.VidyDeyatelnostiForm()
		if alias!='new': # Проверяем новый или не новый
			# try:
			obj = models.Kontragenty.objects.get(Kod=alias) # Получаем объект по токену
			verb_name = models.Kontragenty._meta.verbose_name
			vidy = models.VidyDeyatelnosti.objects.filter(Kontragenty=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
			formKontragenty = forms.KontragentyForm(instance=obj) # Создаем форму на основе существующего объекта
			myvidy = []
			for vid in vidy:
				myvidy.append(forms.VidyDeyatelnostiForm(instance=vid))
			return HttpResponse(render_to_string('kontragenty.html', locals()))
			# except:
			# 	raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.Kontragenty()
			obj.save()
			obj.Kod = 'DL'+str(obj.id)
			obj.save()
			return HttpResponseRedirect('/Kontragenty/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		
# Документы

@csrf_exempt
def InventarizatsiyaTovarovNaSkladeViews(request, alias):
	TovaryForm = forms.TovaryForm()
	if alias!='new': # Проверяем новый или не новый
		try:
			obj = models.InventarizatsiyaTovarovNaSklade.objects.get(Nomer=alias) # Получаем объект по токену 
			tovary = models.Tovary.objects.filter(InventarizatsiyaTovarovNaSklade=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
			InventarizatsiyaTovarovNaSklade = forms.InventarizatsiyaTovarovNaSkladeForm(instance=obj) # Создаем форму на основе существующего объекта
			# Создаем и заполняем массив форм на основе полученного массива объектов
			mytovary = []
			for tovar in tovary:
				mytovary.append(forms.TovaryForm(instance=tovar))
			return HttpResponse(render_to_string('InventarizatsiyaTovarovNaSklade.html', locals()))
		except:
			raise Http404(alias)
	else:
		# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
		obj =  models.InventarizatsiyaTovarovNaSklade()
		obj.save()
		obj.Nomer = 'DL'+ str(obj.id)
		obj.save()
		return HttpResponseRedirect('/InventarizatsiyaTovarovNaSklade/DL'+str(obj.id)+'/')

def UstanovkaTSenNomenklatury(request, alias):
	if request.user.is_authenticated():
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.UstanovkaTSenNomenklatury.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(UstanovkaTSenNomenklatury=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				UstanovkaTSenNomenklatury = forms.UstanovkaTSenNomenklatury(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('UstanovkaTSenNomenklatury.html', locals()))
			except:
				raise Http404(alias)
		else:
			pass
	else:
		return HttpResponseRedirect('/login/')
			

def SchetNaOplatuPokupatelyuViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		UslugiForm = forms.UslugiForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.SchetNaOplatuPokupatelyu.objects.get(Nomer=alias) # Получаем объект по токену 
				uslugy = models.Uslugi.objects.filter(SchetNaOplatuPokupatelyu=obj, PometkaUdaleniya=False)
				tovary = models.Tovary.objects.filter(SchetNaOplatuPokupatelyu=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				SchetNaOplatuPokupatelyu = forms.SchetNaOplatuPokupatelyuForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				myuslugy = []
				for uslga in uslugy:
					myuslugy.append(forms.UslugiForm(instance=uslga))
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('SchetNaOplatuPokupatelyu.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.SchetNaOplatuPokupatelyu()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/SchetNaOplatuPokupatelyu/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

def RealizatsiyaTovarovUslugViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		UslugiForm = forms.UslugiForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.RealizatsiyaTovarovUslug.objects.get(Nomer=alias) # Получаем объект по токену 
				uslugy = models.Uslugi.objects.filter(RealizatsiyaTovarovUslug=obj, PometkaUdaleniya=False)
				tovary = models.Tovary.objects.filter(RealizatsiyaTovarovUslug=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				RealizatsiyaTovarovUslug = forms.RealizatsiyaTovarovUslugForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				myuslugy = []
				for uslga in uslugy:
					myuslugy.append(forms.UslugiForm(instance=uslga))
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('RealizatsiyaTovarovUslug.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.RealizatsiyaTovarovUslug()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/RealizatsiyaTovarovUslug/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

def SchetFakturaVydannyyViews(request, alias):
	if request.user.is_authenticated():
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.SchetFakturaVydannyy.objects.get(Nomer=alias) # Получаем объект по токену 
				SchetFakturaVydannyy = forms.SchetFakturaVydannyyForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				
				return HttpResponse(render_to_string('SchetFakturaVydannyy.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.SchetFakturaVydannyy()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/SchetFakturaVydannyy/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def ZakazPokupatelyaViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		UslugiForm = forms.UslugiForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.ZakazPokupatelya.objects.get(Nomer=alias) # Получаем объект по токену 
				uslugy = models.Uslugi.objects.filter(ZakazPokupatelya=obj, PometkaUdaleniya=False)
				tovary = models.Tovary.objects.filter(ZakazPokupatelya=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				ZakazPokupatelyaForm = forms.ZakazPokupatelyaForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				myuslugy = []
				for uslga in uslugy:
					myuslugy.append(forms.UslugiForm(instance=uslga))
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('ZakazPokupatelya.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.ZakazPokupatelya()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/ZakazPokupatelya/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
	
@csrf_exempt
def ZakazPostavschikuViews(request, alias):
	TovaryForm = forms.TovaryForm()
	UslugiForm = forms.UslugiForm()

	if alias!='new': # Проверяем новый или не новый
		try:
			obj = models.ZakazPostavschiku.objects.get(Nomer=alias) # Получаем объект по токену 
			uslugy = models.Uslugi.objects.filter(ZakazPostavschiku=obj, PometkaUdaleniya=False)
			tovary = models.Tovary.objects.filter(ZakazPostavschiku=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
			ZakazPostavschikuForm = forms.ZakazPostavschikuForm(instance=obj) # Создаем форму на основе существующего объекта
			# Создаем и заполняем массив форм на основе полученного массива объектов
			mytovary = []
			myuslugy = []
			for uslga in uslugy:
				myuslugy.append(forms.UslugiForm(instance=uslga))
			for tovar in tovary:
				mytovary.append(forms.TovaryForm(instance=tovar))
			return HttpResponse(render_to_string('ZakazPostavschiku.html', locals()))
		except:
			raise Http404(alias)
	else:
		# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
		obj =  models.ZakazPostavschiku()
		obj.save()
		obj.Nomer = 'DL'+ str(obj.id)
		obj.save()
		return HttpResponseRedirect('/ZakazPostavschiku/DL'+str(obj.id)+'/')	

@csrf_exempt
def PostuplenieTovarovUslugViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		UslugiForm = forms.UslugiForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.PostuplenieTovarovUslug.objects.get(Nomer=alias) # Получаем объект по токену 
				uslugy = models.Uslugi.objects.filter(PostuplenieTovarovUslug=obj, PometkaUdaleniya=False)
				tovary = models.Tovary.objects.filter(PostuplenieTovarovUslug=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				PostuplenieTovarovUslug = forms.PostuplenieTovarovUslugForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				myuslugy = []
				for uslga in uslugy:
					myuslugy.append(forms.UslugiForm(instance=uslga))
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('PostuplenieTovarovUslug.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.PostuplenieTovarovUslug()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/PostuplenieTovarovUslug/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def VozvratTovarovPostavschikuViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.VozvratTovarovPostavschiku.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(VozvratTovarovPostavschiku=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				VozvratTovarovPostavschiku = forms.VozvratTovarovPostavschikuForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('VozvratTovarovPostavschiku.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.VozvratTovarovPostavschiku()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/VozvratTovarovPostavschiku/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def SchetFakturaPoluchennyyViews(request, alias):
	if request.user.is_authenticated():
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.SchetFakturaPoluchennyy.objects.get(Nomer=alias) # Получаем объект по токену 
				SchetFakturaPoluchennyy = forms.SchetFakturaPoluchennyyForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				
				return HttpResponse(render_to_string('SchetFakturaPoluchennyy.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.SchetFakturaPoluchennyy()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/SchetFakturaPoluchennyy/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def PostuplenieDopRashodovViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.PostuplenieDopRashodov.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(PostuplenieDopRashodov=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				PostuplenieDopRashodov = forms.PostuplenieDopRashodovForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('PostuplenieDopRashodov.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.PostuplenieDopRashodov()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/PostuplenieDopRashodov/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def GTDImportViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		Razdely = forms.RazdelyForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.GTDImport.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(GTDImport=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				razdely = models.Razdely.objects.filter(GTDImport=obj, PometkaUdaleniya=False)
				GTDImport = forms.GTDImportForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				myrazdely = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				for razdel in razdely:
					myrazdely.append(forms.RazdelyForm(instance=razdel))
				return HttpResponse(render_to_string('GTDImport.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.GTDImport()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/GTDImport/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def CHekKKMViews(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		Oplata = forms.OplataForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.CHekKKM.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(CHekKKM=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				oplaty = models.Oplata.objects.filter(CHekKKM=obj, PometkaUdaleniya=False)
				CHekKKM = forms.CHekKKMForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				myoplaty = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				for oplata in oplaty:
					myoplaty.append(forms.OplataForm(instance=oplata))
				return HttpResponse(render_to_string('CHekKKM.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.CHekKKM()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/CHekKKM/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def OtchetORoznichnyhProdazhah(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.OtchetORoznichnyhProdazhah.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(OtchetORoznichnyhProdazhah=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				OtchetORoznichnyhProdazhah = forms.OtchetORoznichnyhProdazhahForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))
				return HttpResponse(render_to_string('OtchetORoznichnyhProdazhah.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.OtchetORoznichnyhProdazhah()
			obj.save()
			obj.Nomer = 'DL'+ str(obj.id)
			obj.save()
			return HttpResponseRedirect('/OtchetORoznichnyhProdazhah/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		


@csrf_exempt
def Doverennosti(request, alias):
	if request.user.is_authenticated():
		TovaryForm = forms.TovaryForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.Doverennosti.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(Doverennosti=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				Doverennosti = forms.DoverennostiForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))

				return HttpResponse(render_to_string('Doverennosti.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.Doverennosti()
			obj.save()
			obj.Nomer = 'DL'+str(obj.id)
			obj.save()

			Doverennosti= forms.DoverennostiForm(instance=obj) # Создаем форму на основе только что созданного объекта
			# Проверяем валидность формы и сохраняем её
			if Doverennosti.is_valid():
				Doverennosti.save()

			return HttpResponseRedirect('/Doverennosti/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		
@csrf_exempt
def vozvrattovarovotpokupatelya(request, alias):
	if request.user.is_authenticated():
		formTovaryForm = forms.TovaryForm()
		if alias!='new': # Проверяем новый или не новый
			try:
				obj = models.VozvratTovarovOtPokupatelya.objects.get(Nomer=alias) # Получаем объект по токену 
				tovary = models.Tovary.objects.filter(VozvratTovarovOtPokupatelya=obj, PometkaUdaleniya=False) # Получаем все подобъекты, у которых ПометкаУдаление=False
				formVozvratTovarovOtPokupatelya = forms.VozvratTovarovOtPokupatelyaForm(instance=obj) # Создаем форму на основе существующего объекта
				# Создаем и заполняем массив форм на основе полученного массива объектов
				mytovary = []
				for tovar in tovary:
					mytovary.append(forms.TovaryForm(instance=tovar))

				return HttpResponse(render_to_string('vozvrattovarovotpokupatelya.html', locals()))
			except:
				raise Http404(alias)
		else:
			# Создаем новый объект, сохраняем, забиваем поле Номер конкатенацией префикса и ИД
			obj =  models.VozvratTovarovOtPokupatelya()
			obj.save()
			obj.Nomer = 'DL'+str(obj.id)
			obj.save()
			return HttpResponseRedirect('/VozvratTovarovOtPokupatelya/DL'+str(obj.id)+'/')
	else:
		return HttpResponseRedirect('/login/')
		
# Вспомогательные функции

# Функция для формирования списка объектов Doc
def viborDoc(request, alias):
	if request.user.is_authenticated():
		form = getattr(forms, alias + 'Form') # Присваиваем переменной свойства объекта из forms, имя которого соответствует конкатенации alias и 'Form'
		model_class = getattr(models, alias) # Присваиваем переменной свойства объекта из models, имя которого соответсвует alias
		verb_name = model_class._meta.verbose_name
		data = serializers.serialize( "python", model_class.objects.filter(PometkaUdaleniya=False) ) # Выполняем  метод all для полученного типа объекта и сериализуем массив
		return HttpResponse(render_to_string('viborDoc.html', locals()))
	else:
		return HttpResponseRedirect('/login/')
		
# Функция для формирования списка объектов Spr
def viborSpr(request, alias):
	if request.user.is_authenticated():
		if alias=='NomeraGTD':
			tokenId = True
		if alias=='Banki':
			tokenId = True
		if alias=='KlassifikatorEdinitsIzmereniya':
			tokenId = True
		if alias=='Valyuty':
			tokenId = True
		form = getattr(forms, alias + 'Form') # Присваиваем переменной свойства объекта из forms, имя которого соответствует конкатенации alias и 'Form'
		model_class = getattr(models, alias) # Присваиваем переменной свойства объекта из models, имя которого соответсвует alias
		verb_name = model_class._meta.verbose_name
		fields = form.Meta.fields
		values = model_class.objects.filter(PometkaUdaleniya=False).values_list(*fields)
		return HttpResponse(render_to_string('viborSpr.html', locals()))
	else:
		return HttpResponseRedirect('/login/')
		

# Функция для сохранения объекта
@csrf_exempt
def saveObj(request):
	if request.method=="POST":
		items = json.loads(request.body.decode()) # Получаем строку данных из POST запроса в формате json

		# Формируем начальные данные
		name_obj = items[0]
		items.remove(items[0])
		id_obj = items[0]
		items.remove(items[0])

		# Формируем словарь с параметрами будущего объекта
		requertPOST={}
		for param in items[0].split('&'): # Нарезаем строку с параметрами и формируем словарь данных
				requertPOST[param.split('=')[0]] = param.split('=')[1] # Пишем параметры в словарь

		form_class = getattr(forms, name_obj+'Form') # Присваиваем переменной свойства объекта из forms, имя которого соответствует конкатенации name_obj и 'Form'
		model_class = getattr(models, name_obj) # Присваиваем переменной свойства объекта из models, имя которого соответсвует name_obj
		old_obj = model_class.objects.get(id=id_obj) # Получаем объект методом get
		form = form_class(requertPOST, instance=old_obj) # Создаём форму на основе уже существующего объекта и сообщаем ей словарь с полученными параметрами
		# Проверяем валидность формы и сохраняем её
		if form.is_valid():
			form.save()
		else:
			return HttpResponse(form.errors)
		return HttpResponse("saved")

	else:
		raise Http404("GET") # Выводим ошибку 404

# Функция для сохранения подобъекта
@csrf_exempt
def saveSubobj(request):
	if request.method=="POST":
		items = json.loads(request.body.decode()) # Получаем строку данных из POST запроса в формате json
		
		# Формируем начальные данные
		sub_obj = items[0]
		items.remove(items[0])
		id_obj = items[0]
		items.remove(items[0])
		obj = items[0]
		items.remove(items[0])

		for item in items: # Перебираем массив
			# Формируем словарь с параметрами будущего объекта
			requertPOST={}
			form_class = getattr(forms, sub_obj+'Form') # Присваиваем переменной свойства объекта из forms, имя которого соответствует конкатенации sub_obj и 'Form'
			for param in item.split('&'): # Нарезаем строку с параметрами и формируем словарь данных
				if 'id_subobj' not in param:
					requertPOST[param.split('=')[0]] = param.split('=')[1] # Пишем параметры в словарь
			requertPOST[obj] = id_obj
			if item.split('&')[0].split('=')[1]!='': # Проверяем есть ли у объекта id, чтобы понять существует ли он
				id_subobj = item.split('&')[0].split('=')[1] # Получаем id объекта
				model_class = getattr(models, sub_obj) # Присваиваем переменной свойства объекта из models, имя которого соответсвует sub_obj
				old_sub_obj = model_class.objects.get(id=id_subobj) # Получаем объект методом get
				form = form_class(requertPOST, instance=old_sub_obj) # Создаём форму на основе уже существующего объекта и сообщаем ей словарь с полученными параметрами
			else:
				form = form_class(requertPOST) # Создаём форму для нового обекта и сообщаем ей словарь с полученными параметрами
			# Проверяем валидность формы и сохраняем её
			if form.is_valid():
				form.save()

	return HttpResponse("saved")

# Удаление объекта, используется для в форме выбора для удаления одного элемента.
@csrf_exempt
def deleteObj(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			item = request.POST.get('delete') # Получаем из реквеста токен в виде Номера или ИД или иного уникального поля
			# Формируем начальные данные
			name_obj = item.split('&')[0]
			token_obj = item.split('&')[1]

			model_class = getattr(models, name_obj) # Присваиваем переменной свойства объекта из models, имя которого равно name_obj
			obj = model_class.objects.get(**{token_obj.split(':')[0]:token_obj.split(':')[1]}) # Выполняем метод get для объекта модели, сообщаем поле и его значение переменными с помощью словоря и указателей
			obj.PometkaUdaleniya=True
			obj.save()
			return HttpResponse("deleted")
		else:
			raise Http404("GET")
	else:
		return HttpResponseRedirect('/login/')
		

@csrf_exempt
def getValutaForGtd(request):
	if request.method == 'POST':
		try:
			dkid = request.POST.get('id', '')
			dogovor = models.DogovoryKontragentov.objects.get(id=dkid)
			valuta = dogovor.ValyutaVzaimoraschetov
			result = ''+str(valuta)+':'
		except:
			return Http404('Options have the false value')
		
		try:
			val = models.Valyuty.objects.get(Naimenovanie = valuta)
			kurs = models.KursyValyut.objects.filter(Valyuty = val).last()
			result +=str(kurs.Kurs)
		except:
			pass
	return HttpResponse(result)

@csrf_exempt
def getIdDocKontragenta(request):
	if request.method == 'POST':
		try:
			result = ''
			kaid = request.POST.get('id', '')
			kontragent = models.Kontragenty.objects.get(id=kaid)
			dogovora = models.DogovoryKontragentov.objects.filter(Vladelets=kontragent)
			for item in dogovora:
				result += str(item.id)+':'
		except:
			return Http404('Options have the false value')
	return HttpResponse(result)

##Функции необходимые для работы ВозвратТоваровОтПокупателей
#Получение Договора Контрагента
@csrf_exempt
def getIdDocKontragentaDima(request):
	if request.method == 'POST':
		try:
			kdid = request.POST.get('id', '')
			kontragent = models.Kontragenty.objects.get(id=kdid, Pokupatel=True, PometkaUdaleniya=False)
			dogovor = models.DogovoryKontragentov.objects.get(Vladelets=kontragent, PometkaUdaleniya=False)
			return HttpResponse(dogovor.id)
		except:
			return HttpResponse('')
#Получение Контрагента
@csrf_exempt
def getIdKontragentDima(request):
	if request.method == 'POST':
		try:
			kid = request.POST.get('id', '')
			dogovor = models.DogovoryKontragentov.objects.get(id=kid)
			kontragent = models.Kontragenty.objects.filter(OsnovnoyDogovorKontragenta=dogovor, Pokupatel=True, PometkaUdaleniya=False).last()
			return HttpResponse(kontragent.id)
		except:
			return HttpResponse('')

#Получение Заказов
@csrf_exempt
def getSdelkaDlyaKontragenta(request):
	if request.method == 'POST':
		try:
			result=''
			kdid = request.POST.get('id', '')
			kontragent = models.Kontragenty.objects.get(id=kdid, Pokupatel=True, PometkaUdaleniya=False)
			zakazy = models.ZakazPokupatelya.objects.filter(Kontragent=kontragent, PometkaUdaleniya=False)
			for zakaz in zakazy:
				result+=str(zakaz.id) + '?'
			return HttpResponse(result)
		except:
			return HttpResponse('')

#Получение контактных лиц
@csrf_exempt
def getContactsDlyaKontragenta(request):
	if request.method == 'POST':
		try:
			result=''
			kdid = request.POST.get('id', '')
			kontragent = models.Kontragenty.objects.get(id=kdid, PometkaUdaleniya=False)
			contacts = models.KontaktnyeLitsaKontragentov.objects.filter(Vladelets=kontragent, PometkaUdaleniya=False)
			for contact in contacts:
				result+=str(contact.id) + '?'
			return HttpResponse(result)
		except:
			return HttpResponse('')

@csrf_exempt
def getIdDocKontragentaPostavshika(request):
	if request.method == 'POST':
		try:
			kdid = request.POST.get('id', '')
			kontragent = models.Kontragenty.objects.get(id=kdid, Postavschik=True, PometkaUdaleniya=False)
			dogovor = models.DogovoryKontragentov.objects.get(Vladelets=kontragent, PometkaUdaleniya=False)
			return HttpResponse(dogovor.id)
		except:
			return HttpResponse('')
#Получение Контрагента
@csrf_exempt
def getIdKontragentPostavshika(request):
	if request.method == 'POST':
		try:
			kid = request.POST.get('id', '')
			dogovor = models.DogovoryKontragentov.objects.get(id=kid)
			kontragent = models.Kontragenty.objects.filter(OsnovnoyDogovorKontragenta=dogovor, Postavschik=True, PometkaUdaleniya=False).last()
			return HttpResponse(kontragent.id)
		except:
			return HttpResponse('')

#Получение Заказов
@csrf_exempt
def getSdelkaDlyaPostavshika(request):
	if request.method == 'POST':
		try:
			result=''
			kdid = request.POST.get('id', '')
			kontragent = models.Kontragenty.objects.get(id=kdid, Postavschik=True, PometkaUdaleniya=False)
			zakazy = models.ZakazPokupatelya.objects.filter(Kontragent=kontragent, PometkaUdaleniya=False)
			for zakaz in zakazy:
				result+=str(zakaz.id) + '?'
			return HttpResponse(result)
		except:
			return HttpResponse('')

import logging
logger = logging.getLogger();



#Три функции Димана
@csrf_exempt
def getSummaDocumentaForSchetaFactury(request):
    if request.method=="POST":
        try:
            result = dict()
            idDocumenta = request.POST.get('idDocumenta','')
            obj = models.PostuplenieTovarovUslug.objects.get(id=idDocumenta)
            try:
                result['SummaDokumenta'] = str(obj.SummaDokumenta)
            except:
                pass
            try:
                result['Organizatsiya'] = str(obj.Organizatsiya.id)
            except:
                pass
            try:
                result['Kontragent'] = str(obj.Kontragent.id)
            except:
                pass
            try:
                result['DogovorKontragenta'] = str(obj.DogovorKontragenta.id)
            except:
                pass
           
            return HttpResponse(json.dumps(result), content_type="application/json")
 
        except:
            pass
    else:
        raise Http404()
 
@csrf_exempt
def getSummaDocumentaForSchetaFacturyVidanniyRTU(request):
    if request.method=="POST":
        try:
            result = dict()
            idDocumenta = request.POST.get('idDocumenta','')
            obj = models.RealizatsiyaTovarovUslug.objects.get(id=idDocumenta)
            try:
                result['SummaDokumenta'] = str(obj.SummaDokumenta)
            except:
                pass
            try:
                result['Organizatsiya'] = str(obj.Organizatsiya.id)
            except:
                pass
            try:
                result['Kontragent'] = str(obj.Kontragent.id)
            except:
                pass
            try:
                result['DogovorKontragenta'] = str(obj.DogovorKontragenta.id)
            except:
                pass
           
            return HttpResponse(json.dumps(result), content_type="application/json")
 
        except:
            pass
    else:
        raise Http404()
 
@csrf_exempt
def getSummaDocumentaForSchetaFacturyVidanniyVTP(request):
    if request.method=="POST":
        try:
            result = dict()
            idDocumenta = request.POST.get('idDocumenta','')
            obj = models.VozvratTovarovPostavschiku.objects.get(id=idDocumenta)
            try:
                result['SummaDokumenta'] = str(obj.SummaDokumenta)
            except:
                pass
            try:
                result['Organizatsiya'] = str(obj.Organizatsiya.id)
            except:
                pass
            try:
                result['Kontragent'] = str(obj.Kontragent.id)
            except:
                pass
            try:
                result['DogovorKontragenta'] = str(obj.DogovorKontragenta.id)
            except:
                pass
           
            return HttpResponse(json.dumps(result), content_type="application/json")
 
        except:
            pass
    else:
        raise Http404()

@csrf_exempt
def saveTsenyNomenklatury(request):
	if request.method=="POST":
		# try:
		items = json.loads(request.body.decode())
		idDocUst = items[0].split('=')[1]
		items.remove(items[0])
		idNomenklatura = items[0].split('=')[1]
		items.remove(items[0])
		obj = models.Nomenklatura.objects.get(id=idNomenklatura)

		# Создаем массив имёт для типов цен, которые хотим записать для данной нуменклатуры
		tipyTsen = []
		for item in items:
			tipTsen = item.split('&')[0].split("=")[1]
			tipyTsen.append(tipTsen)



		# Создаем массив обьектов типов цен которые хочу записать
		tipyTsenIzBasy = models.TipyTSenNomenklatury.objects.all()
		tipyTsenIzBasyName = []
		for item in tipyTsenIzBasy:
			if item.Naimenovanie in tipyTsen:
				tipyTsenIzBasyName.append(item)

		# Создаем массив типовцен которые уже записаны для данной нуменклатуры
		lockTipyTSen = []
		tovary = models.Tovary.objects.filter(Nomenklatura=obj, UstanovkaTSenNomenklatury__isnull=False)
		for tovar in tovary:
			lockTipyTSen.append(tovar.TipTSenNomenklatury)

		# Создаем массив типовцен которые ещё не закреплины за этой нуменклатурой
		freeTipy = []
		for item in tipyTsenIzBasyName:
			if item not in lockTipyTSen:
				freeTipy.append(item)

		# Пишем новые товары и закрепляем их за новым документом Установка цен.
		if len(freeTipy)>0:
			if idDocUst!='':
				ustanovkaTSenNomenklatury = models.UstanovkaTSenNomenklatury.objects.get(id=idDocUst)
			else:
				ustanovkaTSenNomenklatury = models.UstanovkaTSenNomenklatury()
				ustanovkaTSenNomenklatury.save()
				ustanovkaTSenNomenklatury.Nomer = 'DL'+str(ustanovkaTSenNomenklatury.id)
				ustanovkaTSenNomenklatury.save()
			for tip in freeTipy:
				try:
					tipytseninDoc = models.TipyTsen.objects.get(TipTSenNomenklatury=tip, UstanovkaTSenNomenklatury=ustanovkaTSenNomenklatury)
				except:
					tiptsen = models.TipyTsen(TipTSenNomenklatury=tip, UstanovkaTSenNomenklatury=ustanovkaTSenNomenklatury)
					tiptsen.save()
				requestPOST = {}
				for item in items:
					if tip.Naimenovanie == item.split('&')[0].split("=")[1]:
						requestPOST['TSena']=item.split('&')[1].split("=")[1]
						requestPOST['SposobRaschetaTSeny']=item.split('&')[2].split("=")[1]
						requestPOST['Valuta']=item.split('&')[3].split("=")[1]
						requestPOST['EdinitsaIzmereniya']=item.split('&')[4].split("=")[1]
						requestPOST['ProtsentSkidkiNatsenki']=item.split('&')[5].split("=")[1]
						requestPOST['Nomenklatura']=str(obj.id)
						requestPOST['TipTSenNomenklatury']=str(tip.id)
						requestPOST['UstanovkaTSenNomenklatury']=str(ustanovkaTSenNomenklatury.id)
						

				formTovary = forms.TovaryForm(requestPOST)
				if formTovary.is_valid():
					# logger.error('SAVE!!!!!!!!!!!')
					formTovary.save()
			result = models.Tovary.objects.filter(UstanovkaTSenNomenklatury=ustanovkaTSenNomenklatury)

			return HttpResponse(len(result))
		else:
			return HttpResponse("vse ok")

			
@csrf_exempt
def getDateOfBirthKontLitsa(request):
	if request.method == 'POST':
		# try:
			kid = request.POST.get('id', '')
			contact = models.KontaktnyeLitsa.objects.get(id=kid)
			result=str(contact.DataRozhdeniya) + '?' + str(contact.Pol) + '?' + str(contact.Kontakty)
			# return HttpResponse(contact.DataRozhdeniya+'?'+contact.Pol)
			return HttpResponse(result)
		# except:
		# 	return HttpResponse('111')

@csrf_exempt
def newEdinitsuForNomenklatura(request):
	if request.method=="POST":
		items = json.loads(request.body.decode())
		id_obj = items[0]
		items.remove(items[0])
		ediz = items[0]
		ediz_obj = models.KlassifikatorEdinitsIzmereniya.objects.get(id=ediz)
		obj = models.Nomenklatura.objects.get(id=id_obj)
		sub_obj = models.EdinitsyIzmereniya(Vladelets=obj, EdinitsaPoKlassifikatoru=ediz_obj, Koeffitsient=1, Obem=0, Ves=0)
		sub_obj.save()
		sub_obj.Kod="DL"+str(sub_obj.id)
		sub_obj.save()
		return HttpResponse(sub_obj.id)
	else:
		return HttpResponse("GET")

@csrf_exempt
def delEdinitsuIzmereniya(request):
	if request.method=="POST":
		id_obj = json.loads(request.body.decode())[0]
		obj = models.Nomenklatura.objects.get(id=id_obj)
		ei = models.EdinitsyIzmereniya.objects.filter(Vladelets=obj)
		ei.delete()
		return HttpResponse(id_obj)
	else:
		return HttpResponse("GET")

@csrf_exempt
def getTovarOptions(request):
	if request.method=="POST":
		id_tipTsen = request.POST.get('TipyTSen','')
		obj = models.TipyTSenNomenklatury.objects.get(id=id_tipTsen)
		id_nom = request.POST.get('Nomenklatura','')
		nom = models.Nomenklatura.objects.get(id=id_nom)
		tov = models.Tovary.objects.get(Nomenklatura=nom, TipTSenNomenklatury=obj)
		formTov = forms.TovaryForm(instance=tov)
		return HttpResponse(formTov)
	else:
		return HttpResponse("GET")

@csrf_exempt
def getTovarOptionsSTipTSen(request):
	if request.method=="POST":
		id_tipTsen = request.POST.get('TipyTSen','')
		support_obj = models.TipyTSenNomenklaturyKontragentov.objects.get(id=id_tipTsen)
		obj = models.TipyTSenNomenklatury.objects.get(id=support_obj.TipTSenNomenklatury.id)
		id_nom = request.POST.get('Nomenklatura','')
		nom = models.Nomenklatura.objects.get(id=id_nom)
		tov = models.Tovary.objects.get(Nomenklatura=nom, TipTSenNomenklatury=obj)
		formTov = forms.TovaryForm(instance=tov)
		return HttpResponse(formTov)
	else:
		return HttpResponse("GET")


# Системная функция, используется только мной для отладки
def test(request):
	# models.VozvratTovarovOtPokupatelya.objects.all().delete()
	# tovary = models.Tovary.objects.all()
	# tovary = models.Tovary.objects.filter(Nomenklatura=obj).exclude(UstanovkaTSenNomenklatury__isnull=True)
	# for tovar in tovary:
	# 	tovar.TipyTSenNomenklatury__Naimenovanie

	# for item in tipyTsenIzBasy:
	# 	if item.Naimenovanie not in tipyTsen:
	# tipyTsenIzBasy = models.TipyTSenNomenklatury.objects.get(id=8)
	# a = models.Tovary(TipTSenNomenklatury=tipyTsenIzBasy)
	# a.save()

	t = models.Tovary.objects.filter(UstanovkaTSenNomenklatury__isnull=False)
	# return HttpResponse()
	# t.delete()
	ts = models.TipyTsen.objects.all()
	# ts.delete()
	u = models.UstanovkaTSenNomenklatury.objects.all()
	# u.delete()

	# nnomenklatura = models.Nomenklatura.objects.get(id=6)
	# tovar.Nomenklatura = nnomenklatura
	# tovar.save()
	return HttpResponse("all ts: "+str(len(ts))+" | "+"all u: "+str(len(u))+" | "+"all t: "+str(len(t)))


