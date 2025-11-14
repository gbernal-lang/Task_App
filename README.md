# Implementar validaciones y formularios con Django Forms y ModelForms

Para esta actividad, se realizaron validaciones personalizadas para los campos de descripción y titulo

```bash
 #Validación personalizada para titulo
    def clean_title(self):
        title = self.cleaned_data.get('title') #Obtiene lo que se haya ingresado en este campo
        #Si no se ingresa un titulo manda este error
        if  not title:
         
             raise forms.ValidationError("El Titulo es obligatorio")
        #Si el titulo tiene menos de 3 caracteres, manda el siguiente mensaje
        if len (title)<3:
         
            raise forms.ValidationError("El nombre del titulo debe de  tener mas de 3 caracteres")

        return title 
    #Validación personalizada para descripción
    def clean_description(self):
        description = self.cleaned_data.get('description')
        #Si el campo descripción esta vacio, muestra el siguiente mensaje
        if not description:
            raise forms.ValidationError("La descripción es obligatoria")
        #Si el campo tiene menos de 3 caracteres,muestra el siguiente mensaje
        if len (description)<3:
            raise forms.ValidationError("La descripción debe tener mas de 3 caracteres")
        return description


```

### Después, en el archvio views.py, se coloca un mensajes para informar al usario sobre el problema.

```bash
# Muestra un mensaje cuando hay error en los campos del formulario
    def form_invalid(self, form):

        messages.error(self.request, "Revisa los campos del formulario")
        return super().form_invalid(form)
```