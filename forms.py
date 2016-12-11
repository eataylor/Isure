
from django import forms

from tagging.models import Tag
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import authenticate
from  django.core.exceptions import ObjectDoesNotExist 

from Isure.models  import Directory,AccessList 

from Isure.widgets import DropDownMultiple
#from Isure.models  import Directory 

class DirectoryForm(forms.ModelForm):


    #tags = forms.CharField(max_length=100, min_length=20)
    tags = forms.Field(widget=DropDownMultiple)

    def __init__(self, *args, **kwargs):
        self.base_fields['tags'].widget.choices = Tag.objects.values_list('id', 'name')
        super(MyForm, self).__init__(*args, **kwargs)
   

    #class Meta:

        #model = Directory

class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(label=_("Username"), max_length=30)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("Please enter a correct username and password. Note that both fields are case-sensitive."))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))

        # TODO: determine whether this should move to its own method.
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))

        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

class LoginForm(AuthenticationForm):  
    username = forms.CharField(label= 'username', max_length=30)
    password = forms.CharField(label= 'password', widget=forms.PasswordInput) 
    
    def clean_username(self):
       
      username_local = self.cleaned_data.get('username')
      return username_local   
      
class ContactForm(forms.Form): 

      yourname = forms.CharField(required=True,label='yourname',error_messages={'required': 'Your Name Please'})
       
      youremail = forms.EmailField(required=True,label='youremail',error_messages={'required': ' Your Email Please'})
      

      def clean_youremail(self):
       
          youremail_local = self.cleaned_data.get('youremail')
          return youremail_local

       

      def clean_yourname(self):
          yourname_local = self.cleaned_data.get('yourname')

class SearchForm(forms.Form):

  prin_min = forms.CharField(required=False,label='prin_min') 
  prin_max = forms.CharField(required=False,label='prin_max') 

  emp_min = forms.CharField(required=False,label='emp_min') 
  emp_max = forms.CharField(required=False,label='emp_max')

  rev_min = forms.CharField(required=False,label='rev_min') 
  rev_max = forms.CharField(required=False,label='rev_max')

  comm_min = forms.CharField(required=False,label='comm_min') 
  comm_max = forms.CharField(required=False,label='comm_max') 

  bene_min = forms.CharField(required=False,label='bene_min') 
  bene_max = forms.CharField(required=False,label='bene_max')

  pers_min = forms.CharField(required=False,label='pers_min') 
  pers_max = forms.CharField(required=False,label='pers_max')    
   

  crm  = forms.ChoiceField(label="Select a CRM System",choices=(),
                                   
                                  widget=forms.Select(attrs={'class':'form-control','style': 'height:34px'})) 

  ams  = forms.ChoiceField(label="Select a AMS System",choices=(),
                                   
                                  widget=forms.Select(attrs={'class':'form-control','style': 'height:34px'}))  
 
   
                                  
  def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        choices = []
        choices2 = []
        found = []
        topchoice = ['choose',"---Choose from the list ---"]
        #choices = [(mem.CRM, mem.CRM) for mem in Directory.objects.order_by('CRM')]
        #choices.extend(EXTRA_CHOICES)
        choices.append(topchoice)
        for mem in Directory.objects.order_by('CRM'):
            if mem.CRM != '' and [mem.CRM,mem.CRM] not in choices:
               thislist = [mem.CRM,mem.CRM]
               choices.append(thislist)
               found.append(mem.CRM)
        self.fields['crm'].choices = choices
        choices2.append(topchoice)
        for mem in Directory.objects.order_by('AMS'):
            if mem.AMS != '' and [mem.AMS,mem.AMS] not in choices2:
               thislist = [mem.AMS,mem.AMS]
               choices2.append(thislist)
        self.fields['ams'].choices = choices2

  def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        prin_min = cleaned_data.get("prin_min")
        prin_max = cleaned_data.get("prin_max")
         
        crm = cleaned_data.get("crm")
        if crm == "choose":
           print "****Didn't get crm*****",crm
        else:
           print "*****Got crm *****" 

class SignupForm(forms.Form): 

            
	    error_messages = {
		'password_mismatch': _("The two password fields didn't match."),
	    }

            email_id = forms.EmailField(required=True,label='email_id',error_messages={'required': ' Please Enter a valid email address'})
	    password = forms.CharField(required=True,label='Password',error_messages={'required': ' Please Enter a password'} )
		
	   
	    password2 = forms.CharField(label="Password confirmation",error_messages={"Required": "Enter the same password as above, for verification."})
	 
            """
	    class Meta:
		model = User
		fields = ("username",)
		field_classes = {'username': UsernameField}

	    def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		if self._meta.model.USERNAME_FIELD in self.fields:
		    self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})
            """
	    def clean_password(self):
                if self.data['password'] != self.data['password2']:
                   raise forms.ValidationError('Passwords are not the same')
                return self.data['password']
		#return password2

            def clean_email_id(self):
                email_id_local = self.cleaned_data.get('email_id')
                try:
                  print "****Trying Directory "
                  thisMember = Directory.objects.get(ContactEmail=email_id_local)
                  
                except ObjectDoesNotExist:
                   try:
                      print "*** Trying Access "
                      thisAccessList = AccessList.objects.get(email=email_id_local)
                   except ObjectDoesNotExist:
                      raise forms.ValidationError('Email addr is not in the Intersure nor AccessList Directories')
  
                return email_id_local
	      
	 
