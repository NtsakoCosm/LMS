from django.db.models import Model,CharField,ForeignKey,CASCADE,TextField ,PROTECT, ManyToManyField
                                



class Facualty(Model):
    name = CharField(max_length=45)
    description = CharField(max_length=1000)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Faculties'


class Programme(Model):
    facualty = ForeignKey(Facualty,on_delete=CASCADE)
    title = CharField(max_length=75)
    mininum = CharField(max_length=25)
    maximum = CharField(max_length=25)
    description = TextField(default="Description")
    modules = ManyToManyField(to="module.Module")
    

    def __str__(self):
        return  self.title

    def get_modules(self):
        return self.module_set.all()


    class Meta:
        verbose_name_plural = 'Programmes'


class CareerOption(Model):
    title = CharField(max_length=75)
    facualty = ForeignKey(Facualty,on_delete=CASCADE,default=1)
    programme = ForeignKey(Programme,on_delete=PROTECT)
    
    description = TextField()

    def __str__(self):
        return self.title














