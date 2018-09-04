
from django.contrib import admin

from .models import Question, Choice
"""
admin.site.register(Question)

admin.site.register(Choice)
"""
# Start order my crud Question 
"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
'''    
class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['choice_text'] }),
        ('Votes Number: ', {'fields' : ['votes'] })
    ]
'''
"""
# End  order my crud Question 


# Start ADD Question With Some Choice On CRUD 
## Start Avoir 3 choice a ajouté pour la question rentrer Verticalement (admin.StackedInline)
'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
'''
## End

## Start Avoir 3 choice a ajouté pour la question rentrer Horizontalement (admin.TabularInline)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
## End    


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Search Input By Question_Text
    ''' search_fields = ['question_text'] '''

    # Search Input By Question_Text AND Pub_Date in the same time with 1 input
    search_fields = ['question_text','pub_date']

    # Filter By Day, Month, Year ... Important
    list_filter = ['pub_date']

    # To Show More Data On The Table
    list_display = ('question_text', 'pub_date')

# End ADD Question With Some Choice On CRUD     


# Obligatory on End
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)